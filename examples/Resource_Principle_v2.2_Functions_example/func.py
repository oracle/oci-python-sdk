# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example uses functions service to get the rpv2.2 token, for how to use functions, please refer fn Tutorials: https://fnproject.io/tutorials/
# Users can set up Fn locally or with oci cloud shell, the tutoials can be found here: https://www.oracle.com/webfolder/technetwork/tutorials/infographics/oci_functions_cloudshell_quickview/functions_quickview_top/functions_quickview/index.html

import io
import json
import logging
import oci
# used by functions service
from fdk import response


def list_regions(client):
    try:
        resp = client.list_regions()
        logging.getLogger().info("region info:", resp.data)
    except oci.exceptions.ServiceError as e:
        logging.getLogger().error("service error: {0}, error code: {1}, opc-request-id: {2}".format(e.message, e.code, e.request_id))
        return e
    return resp.data


def handler(ctx, data: io.BytesIO = None):  # noqa: E999
    rpv2 = oci.auth.signers.get_resource_principals_signer()
    # Print the Resource Principal Security Token
    logging.getLogger().info("resource principle token:", rpv2.get_security_token())

    # Note the config is passed in as an empty dictionary.  A populated config
    # is not needed when using an EphemeralResourcePrincipalSigner
    iam_client = oci.identity.IdentityClient({}, signer=rpv2)

    resp = list_regions(iam_client)
    return response.Response(
        ctx, response_data=json.dumps(
            {"regions:": str(resp)}),
        headers={"Content-Type": "application/json"}
    )
