# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci

# Overview of Autonomous Data Warehouse
# https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm

# Load the default configuration
config = oci.config.from_file()

# Set the compartment_id. You can use any compartment in your tenancy which
# has privileges for creating an Autonomous Database
compartment_id = config["tenancy"]


def create_adb(db_client):
    # Create the model and populate the values
    # See: https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/adbcreating.htm
    adb_request = oci.database.models.CreateAutonomousDatabaseDetails()

    adb_request.compartment_id = compartment_id
    adb_request.cpu_core_count = 1
    adb_request.data_storage_size_in_tbs = 1
    adb_request.db_name = "adbexample2"
    adb_request.display_name = "PYSDK-ADB-EXAMPLE"
    adb_request.db_workload = "OLTP"
    adb_request.license_model = adb_request.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE
    adb_request.admin_password = "Welcome1!SDK"
    adb_request.is_auto_scaling_enabled = True

    adb_response = db_client.create_autonomous_database(
        create_autonomous_database_details=adb_request,
        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

    print("Created Automated Database {}".format(adb_response.data.id))

    return adb_response.data.id


def delete_adb(db_client, adb_id):
    # Delete the autonomous database
    response = db_client.delete_autonomous_database(adb_id)
    print(response)


def update_adb(db_client, adb_id):
    # Create the model and populate the values
    # See: https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/adbcreating.htm
    adb_request = oci.database.models.UpdateAutonomousDatabaseDetails()

    adb_request.cpu_core_count = 2
    adb_request.data_storage_size_in_tbs = 2
    adb_request.is_auto_scaling_enabled = True

    adb_response = db_client.update_autonomous_database(adb_id,
                                                        update_autonomous_database_details=adb_request,
                                                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

    print("Created Automated Data Warehouse {}".format(adb_response.data.id))

    return adb_response.data.id


if __name__ == "__main__":
    # Initialize the client
    db_client = oci.database.DatabaseClient(config)
    adb_id = create_adb(db_client)
    delete_adb(db_client, adb_id)
