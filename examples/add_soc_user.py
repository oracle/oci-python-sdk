# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from os import path

import argparse
try:
    import oci
    from oci.identity.models import CreateUserDetails, AddUserToGroupDetails, CreateApiKeyDetails
except ImportError as error:
    print(error)
    print("")
    print("OCI libraries not installed. Please install them with 'pip3 install oci'")
    exit(-1)


def search_soc_group():
    """Function to search a specified SOC group"""
    global group_id
    structured_search = oci.resource_search.models.StructuredSearchDetails(query="query group resources where name = '" + groupName + "'", type='Structured', matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
    results = search_client.search_resources(structured_search)
    for result in results.data.items:
        if debug:
            print("Group ID : " + result.identifier)
        group_id = result.identifier


def create_soc_user():
    """Create a SOC user, upload public key and add the user to the SOC group"""
    # Load Public Key
    apikeydetails = CreateApiKeyDetails()
    with open(fileName, "r") as certfile:
        data = certfile.read()
    apikeydetails.key = data

    # Populate a user request
    request = CreateUserDetails()
    request.compartment_id = compartment_id
    request.name = userName
    request.description = "SOC User created For WAF Access"

    try:
        user = identity.create_user(request)
        uid = user.data.id

    except oci.exceptions.ServiceError as e:
        if e.status == 409:
            print("User '" + request.name + "' already exists.")
            structured_user_search = oci.resource_search.models.StructuredSearchDetails(
                query="query user resources where name = '" + userName + "'",
                type='Structured',
                matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
            results = search_client.search_resources(structured_user_search)
            for result in results.data.items:
                if debug:
                    print("User ID : " + result.identifier)
                uid = result.identifier
        else:
            print(e)
    # Upload the user's public cert for API Access
    try:
        identity.upload_api_key(uid, apikeydetails)
        print("User's public key is uploaded successfully")
    except oci.exceptions.ServiceError as e:
        if e.status == 409:
            print("User " + userName + " already has a public key associated, do nothing")
        else:
            print(e)
    # Add the newly created user to the SOC Group
    try:
        add_soc_member(uid)
    except oci.exceptions.ServiceError as e:
        if e.status == 409:
            print("User" + userName + " has been already added to the group :" + groupName)
        else:
            print(e)


def add_soc_member(uid):
    """Add a given user OCID to the SOC group"""
    request = AddUserToGroupDetails()
    request.group_id = group_id
    request.user_id = uid
    try:
        identity.add_user_to_group(request)
    except oci.exceptions.ServiceError as e:
        if e.status == 409:
            print("User is already a member of the group " + groupName)
        else:
            print(e)


def main():
    print("Creating user : " + userName + " and adding to OCI group: " + groupName)
    search_soc_group()
    create_soc_user()


if __name__ == "__main__":
    groupName = 'SOC'
    debug = False
    OCIConfigFile = '~/.oci/config'
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Turn on debug mode")
    parser.add_argument("-c", "--config", action="store", help="Tenancy configuration file")
    parser.add_argument("-u", "--username", action="store", help="specify the username to add.")
    parser.add_argument("-g", "--groupname", action="store", default="soc",
                        help="Specify the group name to add this SOC user to. Defaults to 'SOC'.")
    parser.add_argument("-f", "--certpath", action="store", type=str, help="Specify absolute path to the public key file in PEM format, See - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#How")
    args = parser.parse_args()
    if args.debug is not None:
        debug = args.debug
    if args.config is not None and path.exists(args.config):
        OCIConfigFile = args.config
    userName = args.username
    if userName is None:
        print("Username is mandatory, provide the username as -u username")
        exit(-1)
    groupName = args.groupname
    fileName = args.certpath
    if fileName is None or not path.exists(fileName):
        print("Public Certificate file not provided or does not exist, provide the filepath as -f filepath")
        exit(-1)
    if debug:
        print(userName, " : " + groupName + " : " + fileName)

    # Set up config
    config = oci.config.from_file(OCIConfigFile, "DEFAULT")
    # Create a service client
    identity = oci.identity.IdentityClient(config)

    compartment_id = config["tenancy"]
    search_client = oci.resource_search.ResourceSearchClient(config)
    group_id = ""
    main()
