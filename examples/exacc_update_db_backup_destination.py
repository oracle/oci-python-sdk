# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Updating a DB with BackupDestination

# Usage: python exacc_update_db_backup_destination.py <OCID of a DB> <OCID of Backup Destination>

import sys
import oci

if len(sys.argv) < 3:
    print("Missing arguments! an OCID for a database and backup destination OCID are the required arguments")

database_id = sys.argv[1]
backup_destination_id = sys.argv[2]

config = oci.config.from_file()
db_client = oci.database.DatabaseClient(config)

backup_destination_details = oci.database.models.BackupDestinationDetails(
    id=backup_destination_id,
    type="NFS"
)

backup_destination_list = [backup_destination_details]

db_backup_config_bd = oci.database.models.db_backup_config.DbBackupConfig(
    backup_destination_details=backup_destination_list
)

update_database = oci.database.models.UpdateDatabaseDetails(
    db_backup_config=db_backup_config_bd
)

response = db_client.update_database(database_id, update_database)

print(response.data)
# DB with backup_destination updated
