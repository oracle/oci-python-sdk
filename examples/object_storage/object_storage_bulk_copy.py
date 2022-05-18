# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# object_storage_bulk_copy.py
#
# @author: Tim S and Adi Z
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
#    Bulk copy object storage bucket to other bucket with parallel threads
#
##########################################################################
# Application Command line parameters
#
#   -c config  - Config file section to use (tenancy profile)
#   -t profile - Profile in config file, DEFAULT as default
#   -p proxy   - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip        - Use Instance Principals for Authentication
#   -dt        - Use Instance Principals with delegation token for cloud shell
#   -sb source_bucket
#   -sr source_region
#   -sn source_namespace
#   -sp source_prefix_include
#   -se source_prefix_exclude
#   -db destination_bucket
#   -dr destination_region
#   -ig ignore_check_exist
##########################################################################

import pickle
import threading
import time
import queue
import oci
import argparse
import datetime
import sys
import os


##########################################################################
# Pre Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
parser.add_argument('-c', default="", dest='config_file', help="Config File (default=~/.oci/config)")
parser.add_argument('-sb', default="", dest='source_bucket', help='Source Bucket Name')
parser.add_argument('-sr', default="", dest='source_region', help='Source Region (Default current connection)')
parser.add_argument('-sn', default="", dest='source_namespace', help='Source Namespace (Default current connection)')
parser.add_argument('-sp', default="", dest='source_prefix_include', help='Source Prefix Include')
parser.add_argument('-se', default="", dest='source_prefix_exclude', help='Source Prefix Exclude')
parser.add_argument('-db', default="", dest='destination_bucket', help='Destination Bucket Name')
parser.add_argument('-dr', default="", dest='destination_region', help='Destination Region')
parser.add_argument('-dn', default="", dest='destination_namespace', help='Destination Namespace (Default current connection)')
parser.add_argument('-ig', action='store_true', default=False, dest='ignore_exist', help='Ignore Check if files exist at Destination')
cmd = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()
    raise SystemExit

if not cmd.source_bucket or not cmd.destination_bucket:
    print("Source and Destination buckets parameters are required !!!\n")
    parser.print_help()
    raise SystemExit

# Worker configuration
request_worker_count = 50
status_worker_count = 50
status_interval = 60

# Try timeout
base_retry_timeout = 2
max_retry_timeout = 16**2

# Global  Variables and queues
data = {}
data_lock = threading.Lock()
dest_bucket_memory = {}

known_q = queue.Queue()
update_q = queue.Queue()

# Global Variables
object_storage_client = None
object_storage_client_dest = None

source_bucket = cmd.source_bucket
source_region = cmd.source_region
source_namespace = cmd.source_namespace
destination_namespace = cmd.destination_namespace
source_prefix = cmd.source_prefix_include
source_prefix_exclude = cmd.source_prefix_exclude
destination_bucket = cmd.destination_bucket
destination_region = cmd.destination_region
state_file = source_bucket + "." + destination_bucket + ".wrk"

# Update Variables based on the parameters
config_file = (cmd.config_file if cmd.config_file else oci.config.DEFAULT_LOCATION)
config_profile = (cmd.config_profile if cmd.config_profile else oci.config.DEFAULT_PROFILE)


##########################################################################
# Create signer for Authentication
# Input - config_file, config_profile and is_instance_principals and is_delegation_token
# Output - config and signer objects
##########################################################################
def create_signer(config_file, config_profile, is_instance_principals, is_delegation_token):

    # if instance principals authentications
    if is_instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer

        except Exception:
            print_header("Error obtaining instance principals certificate, aborting")
            raise SystemExit

    # -----------------------------
    # Delegation Token
    # -----------------------------
    elif is_delegation_token:

        try:
            # check if env variables OCI_CONFIG_FILE, OCI_CONFIG_PROFILE exist and use them
            env_config_file = os.environ.get('OCI_CONFIG_FILE')
            env_config_section = os.environ.get('OCI_CONFIG_PROFILE')

            # check if file exist
            if env_config_file is None or env_config_section is None:
                print("*** OCI_CONFIG_FILE and OCI_CONFIG_PROFILE env variables not found, abort. ***")
                print("")
                raise SystemExit

            config = oci.config.from_file(env_config_file, env_config_section)
            delegation_token_location = config["delegation_token_file"]

            with open(delegation_token_location, 'r') as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
                # get signer from delegation token
                signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)

                return config, signer

        except KeyError:
            print("* Key Error obtaining delegation_token_file")
            raise SystemExit

        except Exception:
            raise

    # -----------------------------
    # config file authentication
    # -----------------------------
    else:
        config = oci.config.from_file(
            (config_file if config_file else oci.config.DEFAULT_LOCATION),
            (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
        )
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        return config, signer


##############################################################################
# get time
##############################################################################
def get_time(full=False):
    if full:
        return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    else:
        return str(datetime.datetime.now().strftime("%H:%M:%S"))


##########################################################################
# Print header centered
##########################################################################
def print_header(name):
    chars = int(90)
    print("")
    print('#' * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print('#' * chars)


##########################################################################
# Print Info
##########################################################################
def print_command_info():
    print_header("Running Object Storage Bulk Copy")
    print("Written by Tim S and Adi Z, July 2020")
    print("Starts at        : " + get_time(True))
    print("Command Line     : " + ' '.join(x for x in sys.argv[1:]))
    print("Source Namespace : " + source_namespace)
    print("Source Region    : " + source_region)
    print("Source Bucket    : " + source_bucket)
    print("Source Prefix    : " + source_prefix)
    print("Dest   Namespace : " + destination_namespace)
    print("Dest   Region    : " + destination_region)
    print("Dest   Bucket    : " + destination_bucket)
    print("State  File      : " + state_file)


##############################################################################
# copy_request_worker
##############################################################################
def copy_request_worker():
    while True:
        object_ = known_q.get()
        state = get_state_for_object(object_)

        response = None
        interval_exp = base_retry_timeout
        while True:
            try:
                response = copy_object(source_namespace, source_bucket, object_, destination_namespace, destination_region, destination_bucket, object_)
                break

            except Exception:
                if interval_exp > max_retry_timeout:
                    raise

                print("  Received %s from API for object %s, will wait %s seconds before retrying." % (response.status, object_, interval_exp))

                time.sleep(interval_exp)
                interval_exp **= 2
                continue

        state['work-request-id'] = response.headers.get('opc-work-request-id')
        state['status'] = 'REQUESTED'

        set_state_for_object(object_, state, persist=False)
        known_q.task_done()


##############################################################################
# work_request_status_worker
##############################################################################
def work_request_status_worker():
    while True:
        object_ = update_q.get()
        state = get_state_for_object(object_)

        interval_exp = base_retry_timeout
        while True:
            try:
                response = object_storage_client.get_work_request(state['work-request-id'])
                state['status'] = response.data.status
                break

            except Exception:
                if interval_exp > max_retry_timeout:
                    raise

                print("  Received %s from API for work request %s, will wait %s seconds before retrying." % (response.status, state['work-request-id'], interval_exp))

                time.sleep(interval_exp)
                interval_exp **= 2
                continue

        set_state_for_object(object_, state, persist=False)
        update_q.task_done()


##############################################################################
# add_objects_to_queue
##############################################################################
def load_dest_bucket_to_mem(object_storage_client_dest, destination_namespace, destination_bucket):

    global dest_bucket_memory
    loaded_page = 0

    next_starts_with = None
    while True:
        response = object_storage_client_dest.list_objects(destination_namespace, destination_bucket, start=next_starts_with, prefix=source_prefix, fields="md5", retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
        next_starts_with = response.data.next_start_with

        if loaded_page % 100 == 0 and loaded_page > 0:
            print(get_time() + " -    Loaded " + str(len(dest_bucket_memory)) + " files...")

        for osb in response.data.objects:
            dest_bucket_memory[str(osb.name)] = str(osb.md5)

        if not next_starts_with:
            break

        loaded_page += 1

    print(get_time() + " -    Loaded " + str(len(dest_bucket_memory)) + " files.")


##############################################################################
# add_objects_to_queue
##############################################################################
def add_objects_to_queue(ns, bucket):
    global known_q
    global dest_bucket_memory

    count = 0
    skipped = 0
    next_starts_with = None
    while True:
        response = object_storage_client.list_objects(ns, bucket, start=next_starts_with, prefix=source_prefix, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
        next_starts_with = response.data.next_start_with

        for object_ in response.data.objects:
            if source_prefix and not object_.name.startswith(source_prefix):
                continue
            if source_prefix_exclude and object_.name.startswith(source_prefix_exclude):
                continue

            # skip if exist in the dest bucket (Option is to use MD5 for comparison)
            if str(object_.name) in dest_bucket_memory:
                skipped += 1
                if skipped % 100000 == 0:
                    print(get_time() + " -    Skipped " + str(skipped) + " exist files...")
                continue

            set_state_for_object(object_.name, {'status': 'KNOWN'}, persist=False)
            known_q.put(object_.name)
            count += 1

            if count % 100000 == 0:
                print(get_time() + " -    Added " + str(count) + " files to queue...")

        if not next_starts_with:
            break

    # if skipped files, print
    if skipped > 0:
        print(get_time() + " -    Skipped " + str(skipped) + " exist files...")

    save_all_state()
    return count


##############################################################################
# set_state_for_object
##############################################################################
def set_state_for_object(object_, state, persist=True):
    global data
    data_lock.acquire()
    data[object_] = state

    if persist:
        with open(state_file, 'wb') as sf:
            pickle.dump(data, sf, protocol=pickle.HIGHEST_PROTOCOL)

    data_lock.release()
    return data[object_]


##############################################################################
# save_all_state
##############################################################################
def save_all_state():
    data_lock.acquire()
    with open(state_file, 'wb') as sf:
        pickle.dump(data, sf, protocol=pickle.HIGHEST_PROTOCOL)
    data_lock.release()


##############################################################################
# get_state_for_object
##############################################################################
def get_state_for_object(object_):
    return data[object_]


##############################################################################
# get_work_request_count_by_status
##############################################################################
def get_work_request_count_by_status(status):
    return len([x for x in data.keys() if data[x].get('status') == status])


##############################################################################
# copy_object
##############################################################################
def copy_object(src_ns, src_b, src_o, dst_ns, dst_r, dst_b, dst_o):
    copy_request = oci.object_storage.models.copy_object_details.CopyObjectDetails()
    copy_request.source_object_name = src_o
    copy_request.destination_namespace = dst_ns
    copy_request.destination_region = dst_r
    copy_request.destination_bucket = dst_b
    copy_request.destination_object_name = dst_o

    return object_storage_client.copy_object(src_ns, src_b, copy_request)


##############################################################################
# update_all_work_requests_status
##############################################################################
def update_all_work_requests_status(ns, bucket):
    for object_ in data.keys():
        state = get_state_for_object(object_)

        if state['status'] not in ('KNOWN', 'COMPLETED', 'FAILED', 'CANCELED'):
            update_q.put(object_)

    update_q.join()
    save_all_state()


##############################################################################
# connect to objec storage
##############################################################################
def connect_to_object_storage():

    # global parameters
    global source_region
    global destination_region
    global source_namespace
    global destination_namespace
    global object_storage_client
    global object_storage_client_dest

    print_header("Connecting to Object Storage")

    # get signer
    config, signer = create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)

    # assign region from config file
    if not source_region:
        source_region = config['region']
    if not destination_region:
        destination_region = config['region']

    try:
        # connect to source region
        print("\nConnecting to Object Storage Service for source region - " + source_region)
        object_storage_client = oci.object_storage.ObjectStorageClient(config, signer=signer)
        if cmd.proxy:
            object_storage_client.base_client.session.proxies = {'https': cmd.proxy}

        # retrieve namespace from object storage
        if not source_namespace:
            source_namespace = object_storage_client.get_namespace(retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
        print("Succeed.")

    except Exception as e:
        print("\nError connecting to object storage at source region - " + str(e))
        raise SystemExit

    try:
        # connect to destination object storage
        print("\nConnecting to Object Storage Service for destination region - " + destination_region)
        config_destination = config
        config_destination['region'] = destination_region
        object_storage_client_dest = oci.object_storage.ObjectStorageClient(config_destination, signer=signer)
        if cmd.proxy:
            object_storage_client_dest.base_client.session.proxies = {'https': cmd.proxy}

        # retrieve namespace from object storage
        if not destination_namespace:
            destination_namespace = object_storage_client_dest.get_namespace(retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
        print("Succeed.")

    except Exception as e:
        print("\nError connecting to object storage at destination region - " + str(e))
        raise SystemExit


##############################################################################
# main
##############################################################################
def main():

    # connect to object storage
    connect_to_object_storage()

    # print command info
    print_command_info()

    print_header("Start Processing")
    print(get_time() + " - Creating %s copy request workers." % (request_worker_count))
    for i in range(request_worker_count):
        worker = threading.Thread(target=copy_request_worker)
        worker.daemon = True
        worker.start()

    print(get_time() + " - Creating %s status workers." % (status_worker_count))
    for i in range(status_worker_count):
        worker = threading.Thread(target=work_request_status_worker)
        worker.daemon = True
        worker.start()

    if not cmd.ignore_exist:
        print(get_time() + " - Loading list of objects from destination bucket (%s) to ignore exiting files." % (destination_bucket))
        load_dest_bucket_to_mem(object_storage_client_dest, destination_namespace, destination_bucket)

    print(get_time() + " - Getting list of objects from source bucket (%s). Copies will start immediately." % (source_bucket))
    count = add_objects_to_queue(source_namespace, source_bucket)
    print(get_time() + " -    Enqueued %s objects to be copied" % (count))

    if count > 0:
        print_header("Finish queuing files, start checking")

    while count > 0:
        print(get_time() + " - Waiting %s seconds before checking status." % (status_interval))
        time.sleep(status_interval)

        if get_work_request_count_by_status('KNOWN') > 0 or get_work_request_count_by_status('REQUESTED') > 0:
            print(get_time() + " - Determining copy status")
            update_all_work_requests_status(source_namespace, source_bucket)

        data_lock.acquire()
        print(get_time() + " -    KNOWN: %s, REQUESTED: %s, COMPLETED: %s, FAILED: %s, CANCELED: %s"
              % (
                  get_work_request_count_by_status('KNOWN'),
                  get_work_request_count_by_status('REQUESTED'),
                  get_work_request_count_by_status('COMPLETED'),
                  get_work_request_count_by_status('FAILED'),
                  get_work_request_count_by_status('CANCELED'))
              )

        if get_work_request_count_by_status('KNOWN') == 0 and get_work_request_count_by_status('REQUESTED') == 0:
            data_lock.release()
            break
        else:
            data_lock.release()

    known_q.join()
    print_header("Copy Completed at " + get_time())


##############################################################################
# Execute
##############################################################################
if __name__ == '__main__':
    main()
