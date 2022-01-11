# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Example of signing binary bodies outside of SDK. In this example we register a lookup using a lookup content file in
# csv format which is then signed by user.
#
# This example takes 3 arguments
#   - Namespace where the lookup is created.
#   - Path of the lookup content file
#   - Name of the lookup to be created.
#

import sys
import oci
import hashlib
import base64


def register_lookup_using_content_file(client, namespace, content_file_body, lookup_name):
    resp = client.register_lookup(namespace_name=namespace, register_lookup_content_file_body=content_file_body,
                                  name=lookup_name, type="Lookup")
    print(resp.data)


if len(sys.argv) != 4:
    raise RuntimeError('Please provide only 3 arguments namely namespace_name, content_file_body_path & lookup_name')

# Get the arguments from CLI
namespace = sys.argv[1]
content_file_body_path = sys.argv[2]
lookup_name = sys.argv[3]

config = oci.config.from_file()
log_analytics = oci.log_analytics.LogAnalyticsClient(config)
with open(content_file_body_path, "rb") as content_file_body:
    # Record original position
    original_position = content_file_body.tell()

    # Sign the stream manually
    m = hashlib.sha256()
    base64digest = base64.b64encode(m.digest())
    base64string = base64digest.decode("utf-8")

    # Update the SHA256 header
    log_analytics.base_client.session.headers['x-content-sha256'] = base64string

    # Rewind the body
    content_file_body.seek(original_position)

    # Register the lookup
    register_lookup_using_content_file(log_analytics, namespace=namespace, content_file_body=content_file_body,
                                       lookup_name=lookup_name)

    # Remove the SHA256 header as it is no longer required
    log_analytics.base_client.session.headers.pop('x-content-sha256')
