# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import logging

from examples.container_image_signing.utils import sign_and_upload_container_image_signature_metadata
from examples.container_image_signing.utils import get_and_verify_image_signature_metadata
from src.oci.artifacts.artifacts_client import ArtifactsClient
from src.oci.config import from_file


def main():

    # Default config file and profile
    config = from_file()
    # Create artifact
    artifacts_client = ArtifactsClient(config)

    # Upload Image and Signature Flow
    kms_key_id = "ocid1.key.oc1..exampleuniqueID"
    kms_key_version_id = "ocid1.keyversion.oc1..exampleuniqueID"
    signing_algo = "SHA_512_RSA_PKCS_PSS"
    compartment_id = "ocid1.compartment.oc1..exampleuniqueID"
    image_id = "ocid1.containerimage.oc1..exampleuniqueID"
    description = "Image built by TC"
    metadata = "{\"buildNumber\":\"123\"}"

    signature = sign_and_upload_container_image_signature_metadata(artifacts_client, config, kms_key_id,
                                                                   kms_key_version_id,
                                                                   signing_algo, compartment_id, image_id,
                                                                   description, metadata)
    logging.INFO("A signature has been successfully uploaded: %s", signature)

    # Pull Image and Verify Signature Flow
    repo_name = "repo-name"
    trusted_keys = ["ocid1.key.oc1..keyId1", "ocid1.key.oc1..keyId2"]
    image_digest = "sha256:12345"

    verified = get_and_verify_image_signature_metadata(artifacts_client, compartment_id, False, repo_name, image_digest, trusted_keys)
    if verified:
        logging.INFO("At least one of the signatures is verified")
    else:
        logging.WARN("None of the signatures is verified")


if __name__ == '__main__':
    main()
