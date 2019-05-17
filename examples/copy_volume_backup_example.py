# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This example demonstrates how to copy volume backups to a different region and wait on the copy status.
#
# # USAGE:
# `python examples/copy_volume_backup_example.py  \
#        --volume-backup-id 'foo' \
#        --destination-region '<destination_region>' \
#        --display_name 'bar' \
#        --kms-key-id 'baz'`
#
# Example (copying from us-phoenix-1 to eu-frankfurt-1 :
# `python examples/copy_volume_backup_example.py  \
#        --volume-backup-id 'ocid1.volumebackup.oc1.phx.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
#        --destination-region 'eu-frankfurt-1'
#        --display_name 'copied backup from phoenix' \
#        --kms-key-id 'ocid1.key.oc1.fra.aaaaaaaaaaaaa.bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'`
#
# This script accepts up to for arguments:
#   - volume-backup-id: is the OCID of the volume backup to copy.
#   - destination-region: is the name of the region to copy the volume backup to.
#   - display_name (optional): is the new display name of the copied volume backup. If omitted, the copied volume backup
# will have the same display name as the source backup.
#   - kms-key-id (optional): is the OCID of the kms key to use in the destination region to encrypt
# the copied backup with. If not specified, a platform ad-master key will be used.


import oci
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--volume-backup-id',
                    help='the OCID of the volume backup to copy',
                    required=True
                    )
parser.add_argument('--destination-region',
                    help='the name of the destination region',
                    required=True
                    )

parser.add_argument('--display-name',
                    help='the display name of the copied backup. If not specified, '
                         'defaults to the same as the original backup\'s display name',
                    required=False
                    )

parser.add_argument('--kms-key-id',
                    help='the OCID of the kms key in the destination region to encrypt the copied backup',
                    required=False
                    )
args = parser.parse_args()

source_backup_id = args.volume_backup_id
destination_region = args.destination_region
kms_key_id = args.kms_key_id
display_name = args.display_name

# load config and create clients (one for the source region and one for the destination region).
source_config = oci.config.from_file()
destination_config = source_config.copy()
destination_config["region"] = destination_region
source_blockstorage_client = oci.core.BlockstorageClient(source_config)
destination_blockstorage_client = oci.core.BlockstorageClient(destination_config)

print('Copying backup with ID {} from {} to {} using new display name: {} and kms key id: {} \n'.format(
    source_backup_id, source_config["region"], destination_region, display_name, kms_key_id))
result = source_blockstorage_client.copy_volume_backup(
    source_backup_id,
    oci.core.models.CopyVolumeBackupDetails(
        destination_region=destination_region,
        display_name=display_name,
        kms_key_id=kms_key_id
    )
)

print('Copy backup response status: {}, copied backup: {}\n'.format(result.status, result.data))
print('Waiting for the copied backup to be in available state...')

# query the destination region for the copied' backup's status and wait for it to be available.
copied_backup = oci.wait_until(
    destination_blockstorage_client,
    destination_blockstorage_client.get_volume_backup(result.data.id),
    'lifecycle_state',
    'AVAILABLE'
).data

print('Backup successfully copied: {}'.format(copied_backup))
print('Example script done')
