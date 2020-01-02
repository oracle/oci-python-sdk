# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import requests
from oci.config import from_file
from oci.signer import Signer

config = from_file()
auth = Signer(
    tenancy=config['tenancy'],
    user=config['user'],
    fingerprint=config['fingerprint'],
    private_key_file_location=config['key_file'],
    pass_phrase=config['pass_phrase']
)

endpoint = 'https://identity.us-phoenix-1.oraclecloud.com/20160918/users/'

body = {
    'compartmentId': config['tenancy'],  # root compartment
    'name': 'TestUser',
    'description': 'Created with a raw request'
}

response = requests.post(endpoint, json=body, auth=auth)
response.raise_for_status()

print(response.json()['id'])
