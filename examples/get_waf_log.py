# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script collects logs from WAF and uploads them to the Object Storage.  The tool will pick up log deltas.
# That is, it will first determine when was the last time logs were fetched from WAF.  It will then fetch just
# the logs from that day until yesterday. For example, say you last ran the tool on June 15, 2020.  The tool
# had fetched logs until June 14, 2020 (i.e. the previous day).  Now if you run the tool today - June 25 - it
# will fetch logs from June 15 until yesterday, i.e., June 24.
#
# So the idea is, if you run this tool everyday in a cron job, you will have WAF logs for each day.  You may
# write an Object Storage retention policy to delete old log files or move them to Archive Storage.
#
# Usage:
# python get_waf_log.py -w waf_policy_id -b object_storage_bucket_name
#
# The script uses the default OCI SDK/CLI configuration file ~/.oci/config .

# import sys
import argparse
from datetime import datetime, timedelta
import oci


# Custom function for sorting list.
def get_time_created_field(log_file):
    return log_file.time_created


# This function finds the date of the latest logfile uploaded to the Object Storage.
# If there are no files, then it retuns None.
def get_latest_logfile_date(object_storage, namespace):

    # Log files uploaded on to the Object Storage are prefixed with "WafLogs".
    list_log_objects = object_storage.list_objects(namespace, bucket_name, fields='name,timeCreated', prefix="WafLogs")
    list_log_files = list_log_objects.data.objects
    log_files_num = len(list_log_files)

    if log_files_num == 0:
        print("There are no log files in the Object Storage.")
        return
    else:
        # Sort the list on "timeCreated" in descending order.
        list_log_files.sort(key=get_time_created_field, reverse=True)

        # Get the timestamp of the topmost element.
        topmost_time_stamp = list_log_files[0].time_created
        print("Timestamp of the latest log file {}".format(topmost_time_stamp))

        time_stamp = datetime(topmost_time_stamp.year, topmost_time_stamp.month, topmost_time_stamp.day).date()

        return time_stamp


def upload_logs_to_object_storage(waf_logs):

    object_storage = oci.object_storage.ObjectStorageClient(config)
    namespace = object_storage.get_namespace().data

    current_datetime = datetime.now()
    object_name = "WafLogs-" + str(current_datetime)

    print("Uploading new object to Object Storage - {!r}".format(object_name))
    object_storage.put_object(namespace,
                              bucket_name,
                              object_name,
                              bytes(str(waf_logs), 'utf-8'))


def main():

    # Create a service client.
    waf_client = oci.waas.WaasClient(config)

    # First we need to find out when was the last time logs were fetched from WAF.  We will then fetch
    # logs from the next day until yesterday.  For this, we will query the Object Storage.
    object_storage = oci.object_storage.ObjectStorageClient(config)
    namespace = object_storage.get_namespace().data

    # Start by getting hold of yesterday's time_stamp.
    yesterday = datetime.utcnow().date().today() - timedelta(days=1)

    # Query Object Storage.
    latest_log_fetch_timestamp = get_latest_logfile_date(object_storage, namespace)

    if latest_log_fetch_timestamp is None:
        # No logs have been uploaded to the object Storage.  Fetch all logs from WAF for a week until
        # yesterday and upload them to the Object Storage.
        weekback = yesterday - timedelta(days=7)

        fetch_logs_from_time = datetime(weekback.year,
                                        weekback.month,
                                        weekback.day)
    else:
        # If we fetched it today, do nothing.
        if latest_log_fetch_timestamp == datetime.utcnow().date().today():
            print("Skip fetching- already fetched today.")
            return
        else:
            # Otherwise, fetch logs from the latest_log_fetch_date.
            fetch_logs_from_time = datetime(latest_log_fetch_timestamp.year,
                                            latest_log_fetch_timestamp.month,
                                            latest_log_fetch_timestamp.day)

    # Fetch the logs from the day when the logs were fetched last
    # until yesterday 11:59:59:999999 pm, i.e. just before midnight.
    fetch_logs_until_time = datetime(yesterday.year,
                                     yesterday.month,
                                     yesterday.day,
                                     23,
                                     59,
                                     59,
                                     999999)

    print("Fetching logs from {0} until {1}".format(fetch_logs_from_time, fetch_logs_until_time))

    response = waf_client.list_waf_logs(waf_policy_id,
                                        time_observed_greater_than_or_equal_to=fetch_logs_from_time,
                                        time_observed_less_than=fetch_logs_until_time)

    if response.status == 200:
        upload_logs_to_object_storage(response.data)
    else:
        print("Could not fetch logs from WAF - HTTP Status = {}.".format(response.status))
        exit(-1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-w",
                        "--waf-policy-id",
                        action="store",
                        help="OCID of the WAF Policy",
                        required=True)
    parser.add_argument("-b",
                        "--bucket-name",
                        action="store",
                        help="Name of Object Storage Bucket hosting the WAF log files",
                        required=True)

    args = parser.parse_args()

    # Get hold of the arguments.
    waf_policy_id = args.waf_policy_id
    bucket_name = args.bucket_name

    try:
        # Set up config.
        config = oci.config.from_file()
    except oci.exceptions.ConfigFileNotFound as e:
        print("")
        print("ConfigFileNotFound: {}".format(e))
        print("")
        exit(-1)

    main()
