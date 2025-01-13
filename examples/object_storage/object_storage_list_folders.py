# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# object_storage_list_folders.py
#
# @author: Marco Canto and Adi Zohar
#
# Supports Python 3
#
# DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
# count objects and file size of folders within buckets with option to filter by prefix and write to file
#
##########################################################################
# Application Command line parameters
#
#   -c config  - Config file section to use (tenancy profile)
#   -t profile - Profile in config file, DEFAULT as default
#   -p proxy   - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip        - Use Instance Principals for Authentication
#   -dt        - Use Instance Principals with delegation token for cloud shell
#   -f         - write to file
#   -sb source_bucket
#   -sp source_prefix_include
#   -sr source_region
#   -sn source_namespace
##########################################################################
import oci
import argparse
import datetime
import sys
import os
import re

from collections import defaultdict

##########################################################################
# Pre Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    default="",
    dest="config_profile",
    help="Config file section to use (tenancy profile)",
)
parser.add_argument(
    "-p", default="", dest="proxy", help="Set Proxy (i.e. www-proxy-server.com:80) "
)
parser.add_argument(
    "-ip",
    action="store_true",
    default=False,
    dest="is_instance_principals",
    help="Use Instance Principals for Authentication",
)
parser.add_argument(
    "-dt",
    action="store_true",
    default=False,
    dest="is_delegation_token",
    help="Use Delegation Token for Authentication",
)
parser.add_argument(
    "-c", default="", dest="config_file", help="Config File (default=~/.oci/config)"
)
parser.add_argument("-sb", default="", dest="source_bucket", help="Source Bucket Name")
parser.add_argument(
    "-sp", default="", dest="source_prefix", help="Source Prefix Include"
)
parser.add_argument("-sr", default="", dest="source_region", help="Source Region")
parser.add_argument(
    "-sn",
    default="",
    dest="source_namespace",
    help="Source Namespace (Default current connection)",
)
parser.add_argument(
    "-f", type=argparse.FileType("w"), dest="file", help="Output to file (as csv)"
)

cmd = parser.parse_args()

if len(sys.argv) < 1:
    parser.print_help()
    raise SystemExit

if not cmd.source_bucket:
    print("Source bucket parameter is required !!!\n")
    parser.print_help()
    raise SystemExit

# Update Variables based on the parameters
config_file = cmd.config_file if cmd.config_file else oci.config.DEFAULT_LOCATION
config_profile = (
    cmd.config_profile if cmd.config_profile else oci.config.DEFAULT_PROFILE
)


##########################################################################
# Create signer for Authentication
# Input - config_file, config_profile and is_instance_principals and is_delegation_token
# Output - config and signer objects
##########################################################################
def create_signer(
    config_file, config_profile, is_instance_principals, is_delegation_token
):
    # if instance principals authentications
    if is_instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {"region": signer.region, "tenancy": signer.tenancy_id}
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
            env_config_file = os.environ.get("OCI_CONFIG_FILE")
            env_config_section = os.environ.get("OCI_CONFIG_PROFILE")

            # check if file exist
            if env_config_file is None or env_config_section is None:
                print(
                    "*** OCI_CONFIG_FILE and OCI_CONFIG_PROFILE env variables not found, abort. ***"
                )
                print("")
                raise SystemExit

            config = oci.config.from_file(env_config_file, env_config_section)
            delegation_token_location = config["delegation_token_file"]

            with open(delegation_token_location, "r") as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
                # get signer from delegation token
                signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
                    delegation_token=delegation_token
                )

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
            (config_profile if config_profile else oci.config.DEFAULT_PROFILE),
        )
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content"),
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
    print("#" * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print("#" * chars)


##########################################################################
# Print Info
##########################################################################
def print_command_info(source_namespace):
    print_header("Running List/Count Objects")
    print("Written By Adi Zohar, June 2020")
    print("Starts at           :" + get_time(full=True))
    print("Command Line        : " + " ".join(x for x in sys.argv[1:]))
    print("Source Namespace    : " + source_namespace)
    print("Source Bucket       : " + cmd.source_bucket)
    print("Source Prefix       : " + cmd.source_prefix)


##############################################################################
# Count Objects
##############################################################################
def main():
    object_storage_client = None
    source_bucket = cmd.source_bucket
    source_prefix = cmd.source_prefix
    source_namespace = cmd.source_namespace

    # get signer
    config, signer = create_signer(
        cmd.config_file,
        cmd.config_profile,
        cmd.is_instance_principals,
        cmd.is_delegation_token,
    )

    # if region is specified
    if cmd.source_region:
        config["region"] = cmd.source_region

    try:
        # connect and fetch namespace
        print("\nConnecting to Object Storage Service...")
        object_storage_client = oci.object_storage.ObjectStorageClient(
            config, signer=signer
        )
        if cmd.proxy:
            object_storage_client.base_client.session.proxies = {"https": cmd.proxy}

        # retrieve namespace from object storage
        if not source_namespace:
            source_namespace = object_storage_client.get_namespace(
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

    except Exception as e:
        print("\nError connecting to Object Storage - " + str(e))
        raise SystemExit

    print("Success.")

    # print information
    print_command_info(source_namespace)
    print_header("Start Processing...")
    if cmd.file:
        print("Writing to file..." + cmd.file.name)

    # if output to file
    file = None
    if cmd.file:
        file = open(cmd.file.name + ".csv", "w+")
        file.write("Folder Name,Size (KB),File Count\n")

    # start processing
    count = 0
    size = 0
    next_starts_with = None

    # This regex will capture every section of the path
    regex = r"([^/]+)/"

    while True:
        response = object_storage_client.list_objects(
            source_namespace,
            source_bucket,
            start=next_starts_with,
            prefix=source_prefix,
            fields="size,timeCreated,timeModified,storageTier",
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY,
        )
        next_starts_with = response.data.next_start_with

        folders = defaultdict(float)
        file_count = defaultdict(int)

        for object_file in response.data.objects:
            count += 1
            size += object_file.size
            if not object_file.name.endswith("/"):
                matches = re.findall(regex, object_file.name)
                current_path = ""

                # Loop over each match
                for match in matches:
                    # Concatenate the current match to the current path
                    current_path += match + "/"
                    # Add the current path to the subpaths
                    folders[current_path] += object_file.size / 1024
                    file_count[current_path] += 1

                continue

        format_row = "{:<50} | {:>10} | {:>7}"

        if not cmd.file:
            print(format_row.format("Folder Name", "Size (KB)", "Count"))
            print("-" * 80)
        for folder, f_size in sorted(
            folders.items(), key=lambda item: item[1], reverse=True
        ):
            if not cmd.file:
                print(
                    # f"Folder: {folder:<50} | Size:{'{:.2f}'.format(round(f_size,2)):>10} KB | Count: {file_count[folder]:>5}"
                    format_row.format(
                        folder, "{:.2f}".format(round(f_size, 2)), file_count[folder]
                    )
                )
            if cmd.file:
                file.write(str(folder) + "," + "{:.2f}".format(round(f_size, 2)) + "," + str(file_count[folder]) + "\n")

        if not next_starts_with:
            break

    # final output
    print_header("Completed")
    print("Completed at :  " + get_time(True))
    print("Total Files  : " + str("{:20,.0f}".format(count)).rjust(20))
    print("Total Size   : " + str("{:20,.0f}".format(size)).rjust(20))

    if cmd.file:
        file.write("Total Files : " + str("{:10,.0f}".format(count)).rjust(10) + "  Size : " + str("{:20,.0f}".format(size)).rjust(20))
        file.close()


##############################################################################
# Execute
##############################################################################
if __name__ == "__main__":
    main()
