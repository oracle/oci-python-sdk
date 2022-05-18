# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# object_storage_bulk_delete.py
#
# @author: Adi Zohar
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
#    Bulk delete with parallel threads
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
#   -sp source_prefix
#   -sr source_region
#   -sn source_namespace
##########################################################################

import threading
import time
import queue
import oci
import argparse
import datetime
import sys
import click
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
parser.add_argument('-sp', default="", dest='source_prefix', help='Source Prefix Include')
parser.add_argument('-se', default="", dest='source_prefix_exclude', help='Source Prefix Exclude')
parser.add_argument('-exclude_dirs', action='store_true', default=False, dest='source_exclude_dirs', help='Exclude Directories')
parser.add_argument('-sn', default="", dest='source_namespace', help='Source Namespace (Default current connection)')
parser.add_argument('-sr', default="", dest='source_region', help='Source Region')
cmd = parser.parse_args()

if len(sys.argv) < 1:
    parser.print_help()
    raise SystemExit

if not cmd.source_bucket:
    print("Source bucket parameter is required !!!\n")
    parser.print_help()
    raise SystemExit


source_bucket = cmd.source_bucket
source_prefix = cmd.source_prefix

# Parameters
worker_count = 40
status_interval = 60

base_retry_timeout = 2
max_retry_timeout = 16**2

# global queue
q = queue.Queue()

# Global Variables
object_storage_client = None
source_namespace = ""
source_bucket = cmd.source_bucket
source_prefix = cmd.source_prefix
source_namespace = cmd.source_namespace
source_prefix_exclude = cmd.source_prefix_exclude
source_region = cmd.source_region
source_exclude_dirs = cmd.source_exclude_dirs

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
    print_header("Running Object Storage Bulk Delete")
    print("Written by Adi Zohar, July 2020")
    print("Starts at             : " + get_time(full=True))
    print("Command Line          : " + ' '.join(x for x in sys.argv[1:]))
    print("Source Namespace      : " + source_namespace)
    print("Source Bucket         : " + source_bucket)
    print("Source Prefix Include : " + source_prefix)
    print("Source Prefix Exclude : " + source_prefix_exclude)
    print("Source Region         : " + source_region)
    if source_exclude_dirs:
        print("Source Exclude Dirs   : True")


##############################################################################
# Worker
##############################################################################
def worker():
    while True:
        object_ = q.get()

        interval_exp = base_retry_timeout
        while True:
            response = None
            try:
                response = object_storage_client.delete_object(source_namespace, source_bucket, object_)
                break

            except Exception as e:
                if e.status == 400:
                    break

                if interval_exp > max_retry_timeout:
                    print("  ERROR: Failed to request delete of %s" % (object_))
                    raise

                if response:
                    print("  Received %s from API for object %s, will wait %s seconds before retrying." % (response.status, object_, interval_exp))
                else:
                    print("  Received error from API for object %s, will wait %s seconds before retrying." % (object_, interval_exp))

                time.sleep(interval_exp)
                interval_exp **= 2
                continue

        q.task_done()


##############################################################################
# Add object to Q
##############################################################################
def add_objects_to_queue(ns, source_bucket):
    global q

    count = 0
    next_starts_with = None
    while True:
        response = object_storage_client.list_objects(ns, source_bucket, start=next_starts_with, prefix=source_prefix, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
        next_starts_with = response.data.next_start_with

        for object_ in response.data.objects:
            if source_prefix_exclude and object_.name.startswith(source_prefix_exclude):
                continue
            if source_exclude_dirs and "/" in object_.name:
                continue

            q.put(object_.name)
            count += 1

            if count % 100000 == 0:
                print(get_time() + " -    Added " + str(count) + " files to queue...")

        if not next_starts_with:
            break

    return count


##############################################################################
# connect to object storage
##############################################################################
def connect_to_object_storage():
    global source_namespace
    global object_storage_client
    global source_region

    # get signer
    config, signer = create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)

    # if region is specified
    if source_region:
        config['region'] = source_region
    else:
        source_region = config['region']

    try:
        # connect and fetch namespace
        print("\nConnecting to Object Storage Service...")
        object_storage_client = oci.object_storage.ObjectStorageClient(config, signer=signer)
        if cmd.proxy:
            object_storage_client.base_client.session.proxies = {'https': cmd.proxy}

        # retrieve namespace from object storage
        if not source_namespace:
            source_namespace = object_storage_client.get_namespace(retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
        print("Succeed.")

    except Exception as e:
        print("\nError connecting to Object Storage - " + str(e))
        raise SystemExit


##############################################################################
# Main
##############################################################################
def main():

    # connect to object storage
    connect_to_object_storage()

    # command info
    print_command_info()

    if not click.confirm('\nAre you sure you want to continue deleting ?'):
        raise SystemExit

    print_header("Start Processing")
    print(get_time() + " - Creating %s workers." % (worker_count))
    for i in range(worker_count):
        w = threading.Thread(target=worker)
        w.daemon = True
        w.start()

    print(get_time() + " - Getting list of objects from source source_bucket (%s). delete will start immediately." % (source_bucket))
    count = add_objects_to_queue(source_namespace, source_bucket)
    print(get_time() + " - Enqueued %s objects to be deleted" % (count))

    while count > 0:
        print(get_time() + " - Waiting %s seconds before checking status." % (status_interval))
        time.sleep(status_interval)

        if q.qsize() == 0:
            print(get_time() + " - deletion of all objects has been requested.")
            break
        else:
            print(get_time() + " - %s object deletes remaining to requested." % (q.qsize()))

    q.join()

    print_header("Completed")
    print("Completed at :  " + get_time(True))


##############################################################################
# Execute
##############################################################################
if __name__ == '__main__':
    main()
