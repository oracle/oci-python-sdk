# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from os import path
import argparse

try:
    import oci
    from oci.identity.models import CreatePolicyDetails, CreateGroupDetails
except ImportError as error:
    print(error)
    print("")
    print("OCI libraries not installed. Please install them with 'pip3 install oci'")
    exit(-1)


def create_soc_group():
    """Function to create a specified or default SOC group"""
    print("Creating group " + groupName)
    request = CreateGroupDetails()
    request.compartment_id = tcompartment_id
    request.name = groupName
    request.description = "Created with the SOC setup script"
    try:
        group = identity.create_group(request)
        group_id = group.data.id
        print(group_id)
    except oci.exceptions.ServiceError as e:
        if e.status == 409:
            print("Group already exists...")
            return

        else:
            print("Operational Error" + e.message)


def main():
    print("Adding IAM policy for WAF Access...")

    create_soc_group()
    waf_policy = CreatePolicyDetails()
    waf_policy.compartment_id = compartment_id
    waf_policy.name = 'waas_iam_policy'
    waf_policy.description = "Allows SOC team to appropriately access WAF, audit and metric services"
    waf_policy.statements = statements
    try:
        identity.create_policy(waf_policy)
    except oci.exceptions.ServiceError as e:
        if e.status == 409:
            print("Policy exists, do nothing")
            return
        else:
            print(e)
            return
    print("Added the policy successfully")


if __name__ == "__main__":
    OCIConfigFile = '~/.oci/config'
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", action="store", help="Tenancy configuration file")
    parser.add_argument("-g", "--group", action="store", help="Policy Group Name")
    parser.add_argument("-o", "--OCID", action="store", help="Specify the OCID of the comapartment to associate this "
                                                             "policy")
    args = parser.parse_args()
    if args.group is not None:
        groupName = args.group
    else:
        print("Group name is missing")
        exit(-1)
    if args.config is not None and path.exists(args.config):
        OCIConfigFile = args.config
    compartment_id = args.OCID
    if compartment_id is None:
        print("Provide the OCID of the compartment to which the new policies will be associated with")
        exit(-1)

    print("OCI Config :" + OCIConfigFile + "  Compartment OCID : " + compartment_id)

    # Set up config
    config = oci.config.from_file(OCIConfigFile, "DEFAULT")
    # Create a service client
    identity = oci.identity.IdentityClient(config)
    tcompartment_id = config['tenancy']

    statement1 = "Allow group " + groupName + " to manage waas-family in compartment id " + compartment_id
    statement2 = "Allow group " + groupName + " to read audit-events in compartment id " + compartment_id +\
                 " where target.metrics.namespace='oci_waf'"
    statement3 = "Allow group " + groupName + " to read metrics in compartment id " + compartment_id +\
                 " where target.metrics.namespace='oci_waf'"
    statements = [statement1, statement2, statement3]
    main()
