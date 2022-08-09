#!/usr/bin/env python3
##########################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# check_connectivity.py - to check if policies granted the proper roles
# @author: Adi Zohar
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
import oci
import requests
import sys

# Get Instance Principles Signer
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
config = {'region': signer.region, 'tenancy': signer.tenancy_id}
tenancy_id = signer.tenancy_id
curr_region = signer.region

try:
    print("\n   Connecting to Identity Service...")
    identity = oci.identity.IdentityClient(config, signer=signer)
    print("   Okay.")

    print("\n   Check Tenancy Details Access...")
    tenancy = identity.get_tenancy(tenancy_id).data
    print("   Okay.")

    print("\n   Get List of Regions...")
    regions = identity.list_regions()
    print("   Okay.")

    print("\n   Check running in home region...")
    home_region_array = next(item for item in regions.data if str(item.key) == str(tenancy.home_region_key))
    home_region = str(home_region_array.name)
    print("   Home    Region = " + home_region)
    print("   Current Region = " + curr_region)
    if home_region == curr_region:
        print("   Okay.")
    else:
        print("   Error, Installation must be in Home Region, please change to " + home_region + " and re-run the stack, Aborting...")
        sys.exit()

    print("\n   Check Compartment List Access...")
    all_compartments = identity.list_compartments(tenancy_id, compartment_id_in_subtree=True).data
    print("   Okay...")

    print("\n   Check Access to Cost and Usage Object Storage...")
    object_storage = oci.object_storage.ObjectStorageClient(config, signer=signer)
    objects = object_storage.list_objects("bling", tenancy_id, fields="timeCreated,size").data
    print("   Okay.")

    print("\n   Check Access to OCI Public Rates URL (Required Internet Access)...")
    api_url = "https://itra.oraclecloud.com/itas/.anon/myservices/api/v1/products?partNumber=B88206"
    resp = requests.get(api_url, headers={'X-Oracle-Accept-CurrencyCode': 'USD'})
    print("   Okay.")

    print("\n   Check Completed Successfully.")
    print("   Tenant Name : " + str(tenancy.name))
    print("   Tenant Id   : " + tenancy.id)
    print("")

except oci.exceptions.ServiceError as e:
    print("Error oci.exceptions.ServiceError")
    print(e)
except oci.exceptions.RequestException as e:
    print("Error oci.exceptions.RequestException")
    print(e)
except Exception as e:
    print("Error Exception")
    print(e)
