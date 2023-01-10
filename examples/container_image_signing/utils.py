# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

import re
import json
import base64
import logging

from oci.regions import REALMS, REGION_REALMS
from oci.artifacts.models.create_container_image_signature_details import CreateContainerImageSignatureDetails
from oci.key_management.models.sign_data_details import SignDataDetails
from oci.key_management.kms_crypto_client import KmsCryptoClient
from oci.key_management.models.verify_data_details import VerifyDataDetails


def sign_and_upload_container_image_signature_metadata(artifacts_client, config, key_id, key_version_id, signing_algorithm,
                                                       compartment_id, image_id,
                                                       description, metadata):
    """
    SignAndUploadContainerImageSignatureMetadata calls KMS to sign the message then calls OCIR to upload the returned signature

    :param artifacts_client: Artifacts client
    :param config: Config file
    :param key_id: The OCID of the kmsKeyId used to sign the container image. eg) ocid1.key.oc1..exampleuniqueID. Max length: 255, Min length:1
    :param key_version_id: The OCID of the kmsKeyVersionId used to sign the container image. eg) ocid1.keyversion.oc1..exampleuniqueID. Max length: 255, Min length:1
    :param signing_algorithm: The algorithm to be used for signing. These are the only supported signing algorithms for container images.
    - SHA_224_RSA_PKCS_PSS
    - SHA_256_RSA_PKCS_PSS
    - SHA_384_RSA_PKCS_PSS
    - SHA_512_RSA_PKCS_PSS
    :param compartment_id: The OCID of the compartment in which the container repository exists. eg) ocid1.compartment.oc1..exampleuniqueID. Max length: 100, Min length: 1
    :param image_id: The OCID of the container image. eg) ocid1.containerimage.oc1..exampleuniqueID. Max length: 255, Min length:1
    :param repo_path: The docker repository path. eg) odx-registry/busybox
    :param digest: The sha256 digest of the docker image. eg) sha256:12345
    :param description: An user inputted message.
    :param metadata:  An user defined information about the container image in JSON format eg) {"buildNumber":"123"}
    restriction:
    - should only contains alphanumeric key strings.
    - should be alphabetically sorted.
    - should not have whitespaces or escape characters.
    :return: The signed container image signature metadata.
    """
    signing_algo_kms = mapping_sign_data_details_signing_algorithm.get(signing_algorithm)
    if signing_algo_kms is None:
        raise Exception("The sign data details signing algorithm is not valid. Please check.")
    signing_algo_ocir = mapping_create_container_image_signature_details_signing_algorithm.get(signing_algorithm)
    if signing_algo_ocir is None:
        raise Exception("The create container image signature details signing algorithm is not valid. Please check.")
    region = config.get("region")

    # Create KMS client
    kms_crypto_client = build_vault_crypto_client(config, key_id, region)

    # Get container image metadata
    logging.info("Obtaining container image metadata by the image ID")
    container_image = get_container_image_metadata(artifacts_client, image_id)
    logging.info("Container image metadata: %s", container_image)

    # Generate message
    message = {
        "description": description,
        "imageDigest": container_image.digest,
        "kmsKeyId": key_id,
        "kmsKeyVersionId": key_version_id,
        "metadata": metadata,
        "region": region,
        "repositoryName": container_image.repository_name,
        "signingAlgorithm": signing_algorithm
    }
    json_string = json.dumps(message, separators=(',', ':'))
    encoded_json = base64.b64encode(json_string.encode()).decode()

    # Sign image digest
    logging.info("Generating signature")
    signed_data = sign_container_image(
        kms_crypto_client, encoded_json, key_id, key_version_id, signing_algo_kms)
    logging.info("Signature: %s", signed_data)

    # Upload signature metadata
    logging.info("Uploading signature")
    container_image_signature_uploaded = upload_signature_metadata(artifacts_client, compartment_id,
                                                                   image_id, key_id, key_version_id, signing_algo_ocir,
                                                                   encoded_json, signed_data.signature)
    logging.info("Uploaded signature: %s\nMessage: %s\nID: %s\n", container_image_signature_uploaded.signature,
                 container_image_signature_uploaded.message, container_image_signature_uploaded.id)
    return container_image_signature_uploaded


def get_and_verify_image_signature_metadata(artifacts_client, config, compartment_id, compartment_id_in_subtree,
                                            repository_name, image_digest, trusted_keys):
    """
    GetAndVerifyImageSignatureMetadata calls OCIR to list all the signatures satisfying the user provided criterion then
    calls KMS to verify the returned signatures

    :param artifacts_client: Artifacts client
    :param config: Config file
    :param compartment_id: The OCID of the compartment in which the container repository exists. eg) ocid1.compartment.oc1..exampleuniqueID. MAX length: 100, MIN length 1
    :param compartment_id_in_subtree: When set to true, the hierarchy of compartments is traversed
    :param repository_name: The repository name in which the container image exists eg) busybox
    :param image_digest: The sha256 digest of the docker image. eg) sha256:12345
    :param trusted_keys: List of OCIDs of the kmsKeyId used to sign the container image.
    :return: Boolean to indicate if any of the signatures of the container image is verified
    """
    return get_and_verify_image_signature_metadata_helper(artifacts_client, config, compartment_id,
                                                          compartment_id_in_subtree, repository_name, image_digest,
                                                          trusted_keys, None)


def get_and_verify_image_signature_metadata_helper(artifacts_client, config, compartment_id, compartment_id_in_subtree,
                                                   repository_name, image_digest, trusted_keys, page):

    logging.info("Fetching signatures")
    try:
        signature_collection, next_page = list_container_image_signatures_with_repo_path(
            artifacts_client, compartment_id, compartment_id_in_subtree, repository_name, image_digest, page)
    except Exception:
        logging.error("Unable to get container image signature list using repo path.")
        return False
    logging.info("Fetched signature: %d signature in compartment %s with image URL: %s:%s. Remaining count %d",
                 len(signature_collection.items), compartment_id, repository_name, image_digest,
                 signature_collection.remaining_items_count)

    # Filter out the keys
    container_image_signature_summaries = filter_item_by_trusted_keys(signature_collection.items, trusted_keys)
    if len(container_image_signature_summaries) == 0:
        raise Exception("No signature in the image was signed by the supplied trusted keys")
    logging.info("Filtered out %d signatures by the trusted keys",
                 len(signature_collection.items) - len(container_image_signature_summaries))

    # Verify signature
    logging.info("Verifying signature")
    verified = verify_signatures(config, container_image_signature_summaries)
    if verified is False and next_page is not None:
        return get_and_verify_image_signature_metadata_helper(artifacts_client, config, compartment_id,
                                                              compartment_id_in_subtree, repository_name, image_digest,
                                                              trusted_keys, next_page)
    return verified


def sign_container_image(kms_crypto_client, message, key_id, key_version_id, signing_algorithm):
    sign_data_details = SignDataDetails(
        message=message,
        key_id=key_id,
        key_version_id=key_version_id,
        signing_algorithm=signing_algorithm,
        message_type=SignDataDetails.MESSAGE_TYPE_RAW
    )

    response = kms_crypto_client.sign(sign_data_details)
    return response.data


def upload_signature_metadata(artifacts_client, compartment_id, image_id, key_id, key_version_id, signing_algorithm,
                              message, signature):
    signature_details = CreateContainerImageSignatureDetails(
        compartment_id=compartment_id,
        image_id=image_id,
        kms_key_id=key_id,
        kms_key_version_id=key_version_id,
        message=message,
        signature=signature,
        signing_algorithm=signing_algorithm
    )
    response = artifacts_client.create_container_image_signature(signature_details)
    if response.status != 200:
        raise Exception("Failed to upload the signature to OCI Registry. Status code: %d", response.status)
    return response.data


# Build the KmsCryptoClient based on the vault extension OCID in the keyId
def build_vault_crypto_client(config, key_id, region):
    split_list = re.split("ocid1\\.key\\.([\\w-]+)\\.([\\w-]+)\\.([\\w-]+)\\.([\\w]){60}", key_id)
    if len(split_list) < 4:
        raise Exception("Failed to split key ocid. Please check the kms_key_id is correct.")
    vault_ext = split_list[3]
    realm_name = REGION_REALMS.get(region)
    second_level_domain = REALMS.get(realm_name)
    crypto_endpoint = "https://" + vault_ext + "-crypto.kms." + region + "." + second_level_domain

    kms_crypto_client = KmsCryptoClient(config, crypto_endpoint)
    return kms_crypto_client


def list_container_image_signatures_with_repo_path(artifacts_client, compartment_id, compartment_id_in_subtree,
                                                   repository_name, image_digest, page):
    response = artifacts_client.list_container_image_signatures(
        compartment_id=compartment_id,
        compartment_id_in_subtree=compartment_id_in_subtree,
        repository_name=repository_name,
        image_digest=image_digest,
        page=page)
    if response.status != 200:
        raise Exception("Failed to list the signatures of repository_name %s, image_digest %s, status_code %d",
                        repository_name, image_digest, response.status)
    return response.data, response.next_page


def is_trusted_key(key, trusted_keys):
    for k in trusted_keys:
        if k == key:
            return True
    return False


def filter_item_by_trusted_keys(items, trusted_keys):
    ret = []
    for item in items:
        if is_trusted_key(item.kms_key_id, trusted_keys):
            ret.append(item)
    return ret


def verify_signatures(config, container_image_signature_summary):
    region = config.get("region")

    for signature_summary in container_image_signature_summary:
        if signature_summary is not None:
            vault_crypto_client = build_vault_crypto_client(config, signature_summary.kms_key_id, region)
            algo = mapping_verify_data_details_signing_algorithm.get(signature_summary.signing_algorithm)
            if algo is None:
                raise Exception("The verify data details signing algorithm is not valid. Please check.")
            verified_data = verify_signature(
                vault_crypto_client,
                signature_summary.message,
                signature_summary.signature,
                signature_summary.kms_key_id,
                signature_summary.kms_key_version_id,
                algo
            )
            if verified_data.is_signature_valid:
                return True

    return False


def verify_signature(kms_crypto_client, message, signature, key_id, key_version_id, signing_algorithm):
    verify_data_details = VerifyDataDetails(
        key_id=key_id,
        key_version_id=key_version_id,
        signing_algorithm=signing_algorithm,
        message=message,
        signature=signature
    )
    response = kms_crypto_client.verify(verify_data_details)
    return response.data


def get_container_image_metadata(artifacts_client, image_id):
    container_image = artifacts_client.get_container_image(image_id)
    return container_image.data


mapping_create_container_image_signature_details_signing_algorithm = {
    "SHA_224_RSA_PKCS_PSS": CreateContainerImageSignatureDetails.SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS,
    "SHA_256_RSA_PKCS_PSS": CreateContainerImageSignatureDetails.SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS,
    "SHA_384_RSA_PKCS_PSS": CreateContainerImageSignatureDetails.SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS,
    "SHA_512_RSA_PKCS_PSS": CreateContainerImageSignatureDetails.SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS
}

mapping_sign_data_details_signing_algorithm = {
    "SHA_224_RSA_PKCS_PSS": SignDataDetails.SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS,
    "SHA_256_RSA_PKCS_PSS": SignDataDetails.SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS,
    "SHA_384_RSA_PKCS_PSS": SignDataDetails.SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS,
    "SHA_512_RSA_PKCS_PSS": SignDataDetails.SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS
}

mapping_verify_data_details_signing_algorithm = {
    "SHA_224_RSA_PKCS_PSS": VerifyDataDetails.SIGNING_ALGORITHM_SHA_224_RSA_PKCS_PSS,
    "SHA_256_RSA_PKCS_PSS": VerifyDataDetails.SIGNING_ALGORITHM_SHA_256_RSA_PKCS_PSS,
    "SHA_384_RSA_PKCS_PSS": VerifyDataDetails.SIGNING_ALGORITHM_SHA_384_RSA_PKCS_PSS,
    "SHA_512_RSA_PKCS_PSS": VerifyDataDetails.SIGNING_ALGORITHM_SHA_512_RSA_PKCS_PSS
}
