# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci

# Overview of Autonomous Data Warehouse
# https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adwoverview.htm

# Load the default configuration
config = oci.config.from_file()

# Set the compartment_id. You can use any compartment in your tenancy which
# has privalages for creating an Autonomous Data Warehouse
compartment_id = config["tenancy"]


def create_adw(db_client):
    # Create the model and populate the values
    # See: https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/adwcreating.htm
    adw_request = oci.database.models.CreateAutonomousDataWarehouseDetails()

    adw_request.compartment_id = compartment_id
    adw_request.cpu_core_count = 1
    adw_request.data_storage_size_in_tbs = 1
    adw_request.db_name = "EXAMPLE"
    adw_request.display_name = "PYSDK-EXAMPLE"
    adw_request.license_model = adw_request.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE
    # Remeber this is only an example.  Please change the password.
    adw_request.admin_password = "Welcome1!SDK"

    adw_response = db_client.create_autonomous_data_warehouse(
        create_autonomous_data_warehouse_details=adw_request,
        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

    adw_id = adw_response.data.id
    print("Created Automated Data Warehouse {}".format(adw_id))

    return adw_id


def delete_adw(db_client, adw_id):
    # Delete the autonomous data warehouse
    response = db_client.delete_autonomous_data_warehouse(adw_id)
    print(response.data)


if __name__ == "__main__":
    # Initialize the client
    db_client = oci.database.DatabaseClient(config)

    adw_id = create_adw(db_client)
    delete_adw(db_client, adw_id)
