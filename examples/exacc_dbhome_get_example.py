# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# This script provides an example of how use database CLI in terms of:
#   - Retrieving a DbHome within a given VmCluster

# Usage: python exacc_dbhome_get_example.py <OCID of a DbHome>

import oci
import sys

if len(sys.argv) < 2:
    print("Missing argument! an OCID for a DbHome!")

db_home_id = sys.argv[1]

config = oci.config.from_file()
client = oci.database.DatabaseClient(config)

response = client.get_db_home(db_home_id=db_home_id)

print(response.data)
