# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import sys
import os.path
from hashlib import md5
from codecs import decode
from time import sleep


# This script provides a basic example of how to upload and delete an API key
# using the Python SDK.
#
# This script accepts one argument:
#
#   * The path to the public API key to upload.
#
# The script relies on having a config file for the other variables.
# More information on the config file can be found here:
#    https://docs.cloud.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm
#
# Note, you must already have an API key associated with your user to call the
# APIs so this example shows you how to add a second key, or you could create
# a new user and use the steps here to upload a key to that user.
#
# More information on Keys and API Signing can be found here:
#    https://docs.cloud.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm
#


def get_fingerprint(key):

    # There should be more error checking here, but to keep the example simple
    # the error checking has been omitted.
    m = md5()

    # Strip out the parts of the key that are not used in the fingerprint
    # computation.
    key = key.replace(b'-----BEGIN PUBLIC KEY-----\n', b'')
    key = key.replace(b'\n-----END PUBLIC KEY-----', b'')

    # The key is base64 encoded and needs to be decoded before getting the md5
    # hash
    decoded_key = decode(key, "base64")
    m.update(decoded_key)
    hash = m.hexdigest()

    # Break the hash into 2 character parts.
    length = 2
    parts = list(hash[0 + i:length + i] for i in range(0, len(hash), length))

    # Join the parts with a colon seperator
    fingerprint = ":".join(parts)

    return fingerprint


def is_key_already_uploaded(keys, fingerprint):
    for key in keys:
        if key.fingerprint == fingerprint:
            return True

    return False


# Check there are enough arguments
if len(sys.argv) != 2:
    raise RuntimeError('This script expects an argument of a path to the public API key')

# Verify the path to the public key exists
public_key_path = sys.argv[1]
if not os.path.exists(public_key_path):
    raise RuntimeError('This argument must be a valid path to a public API key')

# Open the key file and store the contents
with open(public_key_path, 'rb') as f:
    public_key = f.read().strip()

# Get the fingerprint for the key
fingerprint = get_fingerprint(public_key)
print("Fingerprint of API key: {}".format(fingerprint))

# Read the config file and initialize the identity client
config = oci.config.from_file()
identity = oci.identity.IdentityClient(config)

# Check to see if this key is already associated with the user.
if is_key_already_uploaded(identity.list_api_keys(config['user']).data, fingerprint):
    print("Key with fingerprint {} has already been added to user".format(fingerprint))
    sys.exit()

# Initialize the CreateApiKeyDetails model
key_details = oci.identity.models.CreateApiKeyDetails(key=public_key.decode())

# Upload the key
response = identity.upload_api_key(config['user'], key_details)

# Results of uploading key
print("Results of uploading key")
print(response.data)

# Check to see if the key is in the list of keys.
# This is pretty crude and just checks that the fingerprint is in the list
# of keys.  If you want to do something similar you should also check that
# the lifecycle_state is "ACTIVE"
while True:
    if is_key_already_uploaded(identity.list_api_keys(config['user']).data, fingerprint):
        print("Sucessfully uploaded API key {}".format(public_key_path))
        break
    sleep(2)

# Delete key and wait a bit.
identity.delete_api_key(config['user'], fingerprint)
sleep(2)

# Verify the key has been deleted.
if not is_key_already_uploaded(identity.list_api_keys(config['user']).data, fingerprint):
    print("Deleted uploaded API key.")
else:
    print("Failed to delete uploaded API key.")
