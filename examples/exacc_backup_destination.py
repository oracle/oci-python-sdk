# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of CRUD(Create, Read, Update, Delete) operations
# on BackupDestination resource.

# Usage: python exacc_backup_destination.py

import oci

# Load the default configuration
config = oci.config.from_file()

# Set the compartment_id.
compartment_id = config["tenancy"]


def create_backup_destination(db_client):
    backup_destination_request = oci.database.models.CreateNFSBackupDestinationDetails()

    backup_destination_request.compartment_id = compartment_id
    backup_destination_request.display_name = "PYSDK-EXAMPLE"
    backup_destination_request.local_mount_point_path = "Users/path"
    backup_destination_request.defined_tags = None
    backup_destination_request.freeform_tags = None

    backup_destination_response = db_client.create_backup_destination(
        create_backup_destination_details=backup_destination_request
    )

    backup_destination_id = backup_destination_response.data.id
    print("Created Backup Destination {}".format(backup_destination_id))

    return backup_destination_id


def update_backup_destination(db_client, backup_destination_id):
    backup_destination_request = oci.database.models.UpdateBackupDestinationDetails()
    backup_destination_request.localMountPointPath = "Users/updated_path"

    backup_destination_response = db_client.update_backup_destination(
        backup_destination_id=backup_destination_id,
        update_backup_destination_details=backup_destination_request)

    print(backup_destination_response.data)


def delete_backup_destination(db_client, backup_destination_id):
    response = db_client.delete_backup_destination(backup_destination_id)
    print(response.data)


def get_backup_destination(db_client, backup_destination_id):
    response = db_client.get_backup_destination(backup_destination_id)
    print(response.data)


if __name__ == "__main__":
    # Initialize the client
    db_client = oci.database.DatabaseClient(config)

    backup_destination_id = create_backup_destination(db_client)

    update_backup_destination(db_client, backup_destination_id)

    get_backup_destination(db_client, backup_destination_id)

    delete_backup_destination(db_client, backup_destination_id)
