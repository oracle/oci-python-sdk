# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example demonstrates how to copy boot volume backups to a different region and wait on the copy status.
#
# # USAGE:
# `python examples/copy_boot_volume_backup_example.py  \
#        --volume-backup-id 'foo' \
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

# load config and create clients (one for the source region and one for the destination region).
source_config = oci.config.from_file()
destination_config = source_config.copy()
destination_config["region"] = destination_region
source_blockstorage_client = oci.core.BlockstorageClient(source_config)
destination_blockstorage_client = oci.core.BlockstorageClient(destination_config)

print('Copying boot volume backup with ID {} from {} to {} using new display name: {} and kms key id: {} \n'.format(
    source_backup_id, source_config["region"], destination_region, display_name, kms_key_id))
result = source_blockstorage_client.copy_boot_volume_backup(
    source_backup_id,
    oci.core.models.CopyBootVolumeBackupDetails(
        destination_region=destination_region,
        display_name=display_name,
        kms_key_id=kms_key_id
    )
)

print('Copy boot volume backup response status: {}, copied backup: {}\n'.format(result.status, result.data))
print('Waiting for the copied backup to be in available state...')

# query the destination region for the copied' backup's status and wait for it to be available.
copied_backup = oci.wait_until(
    destination_blockstorage_client,
    destination_blockstorage_client.get_boot_volume_backup(result.data.id),
    'lifecycle_state',
    'AVAILABLE'
).data

print('Backup successfully copied: {}'.format(copied_backup))
print('Example script done')
