# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how you can build Python SDK client's configuration.
# Using the default configuration location ~/.oci/config, you can use config.from_file() to load any profile.
# Since config is a dict, you can manually initiate the dict, the key should include : user, key_file, fingerprint,
# tenancy and region; if You prefer to use key_content directly rather than getting from the file it is also possible,
# then you can check it with config.validate_config().

import oci

# Default config file and profile
default_config = oci.config.from_file()

# validate the default config file
oci.config.validate_config(default_config)

# Since config is a dict, you can also build it manually and check it with config.validate_config().
config_with_key_file = {
    "user": 'ocid1.user.oc1..aaaaaaaa65abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmn',
    "key_file": '~/.oci/oci_api_key.pem',
    "fingerprint": '11:22:33:44:55:66:77:88:99:0a:1b:2c:3d:4e:5f:6g',
    "tenancy": 'ocid1.tenancy.oc1..aaaaaaaa5nfwo53cezleyy6t73v6rn6knhu3molvptnl3kcq34l5ztenancy',
    "region": 'us-phoenix-1'
}
oci.config.validate_config(config_with_key_file)

# If you want to use the private key which is not in the key file, key_content can be the backup of key_file.
pem_prefix = '-----BEGIN RSA PRIVATE KEY-----\n'
pem_suffix = '\n-----END RSA PRIVATE KEY-----'
key = "aaaaabbbbbbbcccccc..."    # The content of your private key
key_content = '{}{}{}'.format(pem_prefix, key, pem_suffix)

config_with_key_content = {
    "user": 'ocid1.user.oc1..aaaaaaaa65abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmn',
    "key_content": key_content,
    "fingerprint": '11:22:33:44:55:66:77:88:99:0a:1b:2c:3d:4e:5f:6g',
    "tenancy": 'ocid1.tenancy.oc1..aaaaaaaa5nfwo53cezleyy6t73v6rn6knhu3molvptnl3kcq34l5ztenancy',
    "region": 'us-phoenix-1'
}
oci.config.validate_config(config_with_key_content)
