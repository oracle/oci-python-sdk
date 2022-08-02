# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to move an instance from one compartment to another using Python SDK.
# This script will:
#
#    * Read user configuration
#    * Construct ComputeClient using user configuration
#    * Construct ChangeInstanceCompartmentDetails()
#    * Call change_instance_compartment() in oc.core.ComputeClient()
#    * List Instance and its attached resources before and after move operation
#
# This script takes the following arguments
#
#    * The instance id of an instance
#    * The target compartment id
#    * if_match (Optional)
#          The Instance will be moved only if the etag you provide matches the resource's current etag value.
#    * opc_retry_token (Optional)
#          A token that uniquely identifies a request so it can be retried in case of a timeout or server error
#          without risk of executing that same action again. Retry tokens expire after 24 hours, but can be
#          invalidated before then due to conflicting operations
#
#
# Usage :
#    change_instance_compartment_example.py --instance-id=<Instance Id>
#                                           --compartment-id=<Compartment Id>
#                                           [ --if-match=<ETag> ]
#                                           [ --opc-retry-token=<String> ]
#
#

from __future__ import print_function
import sys

import oci
from oci.core import ComputeClient
from oci.core.models import ChangeInstanceCompartmentDetails
from oci.work_requests import WorkRequestClient


if_match = None
infoEnabled = True
instance_id = None
compartment_id = None
opc_retry_token = None


def info(message):
    if infoEnabled:
        print("[INFO] " + message)


def error(message):
    if infoEnabled:
        print("[ERROR]" + message)


def errorExit(message):
    if infoEnabled:
        print("[ERROR]" + message)
        print("[ERROR] Change-Instance-Compartment failed ")
    exit(1)


def handleScriptFailureAndExit(failureInfo, exc):
    if exc is not None:
        print("[ERROR] : Unexpected failure: " + failureInfo + ": ", exc)
    exit(1)


def successExit():
    info(' Change-Instance-Compartment completed  ')
    exit(0)


def usage(status):
    print(" ")
    print(" change_instance_compartment_example.py <params>")
    print(" ")
    print(" Parameters: ")
    print(" ")
    print(" --instance-id=<instance id>        # Required: Instance Id")
    print(" --compartment-id=<compartment id>  # Required: Target Compartment Id")
    print(" --help                             # Optional: Help text")
    print(" --if-match=<ETag>                  # Optional: ETag")
    print(" --opc-retry-token=<String>         # Optional: OPC retry token string")
    print("                                                                     ")
    exit(status)


def exampleMain():
    parseCommandLine()
    performChangeCompartment()


def performChangeCompartment():
    global compute_client
    global work_request_client
    global availability_domain
    try:
        # read oci config
        config = oci.config.from_file()

        # create ComputeClient() with configuration
        compute_client = ComputeClient(config)

        # create WorkRequestClient() with configuration
        work_request_client = WorkRequestClient(config)

        response = getInstanceResponse()
        availability_domain = response.data.availability_domain
        source_compartment_id = response.data.compartment_id
        if source_compartment_id == target_compartment_id:
            errorExit(" Source and target compartment ids are same !")

        # List instance info before move
        info(' ')
        info(' Instance info before compartment move : ')
        info('   ETag : ' + response.headers['etag'])
        printInstanceInfo(source_compartment_id)

        # create ChangeInstanceCompartmentDetails() with compartment_id
        compartment_details = ChangeInstanceCompartmentDetails()
        compartment_details.compartment_id = target_compartment_id

        info(' ')
        info(' Moving Instance to target compartment ...')
        # call change_instance_compartment() on ComputeClient
        response = compute_client.change_instance_compartment(instance_id, compartment_details,
                                                              if_match=if_match, opc_retry_token=opc_retry_token)

        # List instance info after move
        waitForMoveCompletion(response)
        info(' ')
        info(' Instance info after compartment move : ')
        if 'etag' in response.headers.keys():
            info('   ETag : ' + response.headers['etag'])
        printInstanceInfo(target_compartment_id)
        successExit()
    except Exception:
        info(' Unexpected error ')
        raise


def getInstanceResponse():
    # wait until the instance changes its state from "MOVING" to any other state
    return oci.wait_until(
        compute_client,
        compute_client.get_instance(instance_id),
        evaluate_response=lambda r: r.data.lifecycle_state != 'MOVING'
    )


def waitForMoveCompletion(response):
    if 'opc-work-request-id' in response.headers.keys():
        opc_work_request_id = response.headers['opc-work-request-id']
        info('   opc-work-request-id ' + opc_work_request_id)
        info('   Querying the status of move operation using opc-work-request-id')
        # Get WorkRequest from WorkRequestClient()
        work_request = work_request_client.get_work_request(opc_work_request_id)
        info('   Work completion percentage : ' + str(work_request.data.percent_complete))
        if (work_request.data.percent_complete < 100.0):
            info('   Waiting for work completion ...')
            # wait until the work is complete or the percent_complete is 100.0
            oci.wait_until(
                work_request_client,
                work_request_client.get_work_request(opc_work_request_id),
                evaluate_response=lambda r: r.data.percent_complete >= 100.0

            )
            info('   Work completed')


def printInstanceInfo(id):
    global compartment_id
    compartment_id = id
    info('   Compartment id : ' + compartment_id)
    printVolumeAttachmentsInfo()
    printVnicAttachmentsInfo()
    printBootVolumeAttachmentsInfo()
    printConsoleConnectionsInfo()
    printConsoleHistoryAttachmentsInfo()


def printVolumeAttachmentsInfo():
    volume_attachments = oci.pagination.list_call_get_all_results(
        compute_client.list_volume_attachments,
        compartment_id,
        instance_id=instance_id
    ).data
    if volume_attachments:
        info('   Volume attachments: ')
        for volume_attachment in volume_attachments:
            info('     Volume id :' + volume_attachment.volume_id)
            info('     Compartment id :' + volume_attachment.compartment_id)
            info('     State :' + volume_attachment.lifecycle_state)
            info('')


def printVnicAttachmentsInfo():
    vnic_attachments = oci.pagination.list_call_get_all_results(
        compute_client.list_vnic_attachments,
        compartment_id,
        instance_id=instance_id
    ).data
    if vnic_attachments:
        info('   Vnic Attachments: ')
        for vnic_attachment in vnic_attachments:
            info('     Vnic id : ' + vnic_attachment.vnic_id)
            info('     Compartment id :' + vnic_attachment.compartment_id)
            info('     State :' + vnic_attachment.lifecycle_state)
            info('')


def printBootVolumeAttachmentsInfo():
    boot_volume_attachments = oci.pagination.list_call_get_all_results(
        compute_client.list_boot_volume_attachments,
        availability_domain,
        compartment_id,
        instance_id=instance_id
    ).data
    if boot_volume_attachments:
        info('   Boot Volume Attachments: ')
        for boot_volume_attachment in boot_volume_attachments:
            info('     Volume id :' + boot_volume_attachment.boot_volume_id)
            info('     Compartment id :' + boot_volume_attachment.compartment_id)
            info('     State :' + boot_volume_attachment.lifecycle_state)
            info('')


def printConsoleConnectionsInfo():
    console_connections = oci.pagination.list_call_get_all_results(
        compute_client.list_instance_console_connections,
        compartment_id,
        instance_id=instance_id
    ).data
    if console_connections:
        info('   Console Connections: ')
        for console_connection in console_connections:
            info('     Console connection id :  ' + console_connection.id)
            info('     Compartment id :' + console_connection.compartment_id)
            info('     State :' + console_connection.lifecycle_state)
            info('')


def printConsoleHistoryAttachmentsInfo():
    console_history_attachments = oci.pagination.list_call_get_all_results(
        compute_client.list_console_histories,
        compartment_id,
        instance_id=instance_id
    ).data
    if console_history_attachments:
        info('   Console History Attachments: ')
        for console_history_attachment in console_history_attachments:
            info('     Console History id :  ' + console_history_attachment.id)
            info('     Compartment id :' + console_history_attachment.compartment_id)
            info('     State :' + console_history_attachment.lifecycle_state)
            info('')


def parseCommandLine():
    global instance_id
    global target_compartment_id
    global if_match
    global opc_retry_token

    scriptFileArg = sys.argv[0]
    if len(sys.argv) == 1:
        usage(status=1)

    for argStr in sys.argv:
        if argStr == "--help":
            usage(status=0)
        elif argStr.startswith("--instance-id="):
            instance_id = argStr.split("=")[1]
            info('   Instance id : ' + instance_id)
        elif argStr.startswith("--compartment-id="):
            target_compartment_id = argStr.split("=")[1]
            info('   Compartment id : ' + target_compartment_id)
        elif argStr.startswith("--if-match="):
            if_match = argStr.split("=")[1]
            info('   if_match : ' + if_match)
        elif argStr.startswith("--opc-retry-token="):
            opc_retry_token = argStr.split("=")[1]
            info('   opc_retry_token : ' + opc_retry_token)
        else:
            if argStr != scriptFileArg:
                info(' ERROR: unknown command line argument supplied to script: ' + argStr)
                usage(status=1)
    if instance_id is None:
        info(' *** Missing input argument : --instance-id ')
        usage(status=1)
    if target_compartment_id is None:
        info(' *** Missing input argument : --compartment-id ')
        usage(status=1)


class MainWork:
    exampleMain()
