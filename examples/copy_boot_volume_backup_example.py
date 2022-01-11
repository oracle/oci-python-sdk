# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example demonstrates how to copy boot volume backups to a different region and wait on the copy status.
#
# # USAGE:
# `python examples/copy_boot_volume_backup_example.py  \
#        --boot-volume-backup-id 'foo' \
#        --destination-region '<destination_region>' \
#        --display_name 'bar' \
#        --kms-key-id 'baz'`
#
# Example (copying from us-phoenix-1 to eu-frankfurt-1 :
# `python examples/copy_boot_volume_backup_example.py  \
#        --boot-volume-backup-id 'ocid1.bootvolumebackup.oc1.phx.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
#        --destination-region 'us-ashburn-1'
#        --display-name 'copied backup from phoenix' \
#        --kms-key-id 'ocid1.key.oc1.iad.aaaaaaaaaaaaa.bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'`
#
# This script accepts up to for arguments:
#   - boot-volume-backup-id: is the OCID of the boot volume backup to copy.
#   - destination-region: is the name of the region to copy the boot volume backup to.
#   - display_name (optional): is the new display name of the copied boot volume backup.
#     If omitted, the copied boot volume backup will have the same display name as the source backup.
#   - kms-key-id (optional): is the OCID of the kms key to use in the destination region to encrypt
# the copied backup with. If not specified, a platform ad-master key will be used.


import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--boot-volume-backup-id',
                    help='the OCID of the boot volume backup to copy',
                    required=True
                    )
parser.add_argument('--destination-region',
                    help='the name of the destination region to copy the backup to',
                    required=True
                    )

parser.add_argument('--display-name',
                    help='the display name of the copied boot volume backup. If not specified, '
                         'defaults to the same as the original backup\'s display name',
                    required=False
                    )

parser.add_argument('--kms-key-id',
                    help='the OCID of the kms key in the destination region to encrypt the copied boot volume backup',
                    required=False
                    )
args = parser.parse_args()

source_backup_id = args.boot_volume_backup_id
destination_region = args.destination_region
kms_key_id = args.kms_key_id
display_name = args.display_name

# load config and create clients one for BlockstorageClient and another for BlockstorageClientCompositeOperations.
source_config = oci.config.from_file()
print('Copying boot volume backup with ID {} from {} to {} using new display name: {} and kms key id: {} \n'.format(
    source_backup_id, source_config["region"], destination_region, display_name, kms_key_id))
blockstorage_client = oci.core.BlockstorageClient(source_config)
blockstorage_composite_client = oci.core.BlockstorageClientCompositeOperations(blockstorage_client)
copied_backup = blockstorage_composite_client.copy_boot_volume_backup_and_wait_for_work_request(
    boot_volume_backup_id=source_backup_id,
    copy_boot_volume_backup_details=oci.core.models.CopyBootVolumeBackupDetails(
        destination_region=destination_region,
        display_name=display_name,
        kms_key_id=kms_key_id
    )).data
print('Backup successfully copied: {}'.format(copied_backup))
print('Example script done')
