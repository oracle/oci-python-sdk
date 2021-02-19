import oci
from unittest.mock import patch

from examples.container_image_signing.utils import sign_and_upload_container_image_signature_metadata
from examples.container_image_signing.utils import get_and_verify_image_signature_metadata
from src.oci.artifacts.artifacts_client import ArtifactsClient
from src.oci.artifacts.models.container_image_signature import ContainerImageSignature
from src.oci.artifacts.models.container_image_signature_collection import ContainerImageSignatureCollection
from src.oci.artifacts.models.container_image_signature_summary import ContainerImageSignatureSummary
from src.oci.key_management.kms_crypto_client import KmsCryptoClient
from src.oci.key_management.models.signed_data import SignedData
from src.oci.key_management.models.verified_data import VerifiedData
from tests.util import get_resource_path

kms_key_id = "ocid1.key.oc1.region_name.bbqc3acqaadfa.abyhqljtb2hrommkvjggqn7zr3y3kt3akybs75qzoq7us6fwda2fcnoyzgbq"
kms_key_version_id = "ocid1.keyversion.oc1.region_name.bnpxdhjuaabm4.ccufmawjxiaaa.ab2g6ljrxaw42yqgd2rnv5yjbwmhztovk562lzjqqrcjnw"
signing_algo = "SHA_512_RSA_PKCS_PSS"
compartment_id = "ocid1.compartment.oc1..exampleuniqueID"
image_id = "ocid1.containerimage.oc1..exampleuniqueID"
repo_path = "tenancy-namespace/repo-name/image-name"
image_digest = "sha256:12345"
description = "Image built by TC"
metadata = "{\"buildNumber\":\"123\"}"

sign_data = SignedData()
sign_data.signature = "example_sign_data_signature"
sign_data_details_response = oci.Response(
    status=None,
    data=sign_data,
    headers=None,
    request=None
)

container_image_signature = ContainerImageSignature()
container_image_signature.signature = "example_sign_data_signature"
container_image_signature_response = oci.Response(
    status=200,
    data=container_image_signature,
    headers=None,
    request=None
)

container_image_signature_collection = ContainerImageSignatureCollection()
container_image_signature_collection.items = [
    ContainerImageSignatureSummary(
        kms_key_id="ocid1.key.oc1.region_name.bbqc3acqaadfa.abyhqljtb2hrommkvjggqn7zr3y3kt3akybs75qzoq7us6fwda2fcnoyzgb0",
        signing_algorithm="SHA_256_RSA_PKCS_PSS"
    ),
    ContainerImageSignatureSummary(
        kms_key_id="ocid1.key.oc1.region_name.bbqc3acqaadfa.abyhqljtb2hrommkvjggqn7zr3y3kt3akybs75qzoq7us6fwda2fcnoyzgb1",
        signing_algorithm="SHA_256_RSA_PKCS_PSS"
    ),
    ContainerImageSignatureSummary(
        kms_key_id="ocid1.key.oc1.region_name.bbqc3acqaadfa.abyhqljtb2hrommkvjggqn7zr3y3kt3akybs75qzoq7us6fwda2fcnoyzgb2",
        signing_algorithm="SHA_256_RSA_PKCS_PSS"
    )
]
container_image_signature_collection_response = oci.Response(
    status=200,
    data=container_image_signature_collection,
    headers=None,
    request=None
)

verify_data = VerifiedData(
    is_signature_valid=True
)
verify_signature_response = oci.Response(
    status=200,
    data=verify_data,
    headers=None,
    request=None
)


@patch.object(KmsCryptoClient, 'sign', return_value=sign_data_details_response)
@patch.object(ArtifactsClient, 'create_container_image_signature', return_value=container_image_signature_response)
def test_sign_and_upload_container_image_signature_metadata(sign_data_details_response, container_image_signature_response):
    # Default config file and profile
    config = oci.config.from_file(file_location=get_resource_path('config'))
    # Create artifact
    artifacts_client = ArtifactsClient(config)

    # Upload Image and Signature Flow
    signature = sign_and_upload_container_image_signature_metadata(artifacts_client, config, kms_key_id,
                                                                   kms_key_version_id, signing_algo, compartment_id,
                                                                   image_id, repo_path, image_digest, description,
                                                                   metadata)

    assert signature is not None
    assert signature.signature == "example_sign_data_signature"


@patch.object(ArtifactsClient, 'list_container_image_signatures', return_value=container_image_signature_collection_response)
@patch.object(KmsCryptoClient, 'verify', return_value=verify_signature_response)
def test_get_and_verify_image_signature_metadata(container_image_signature_collection_response, verify_signature_response):
    # Default config file and profile
    config = oci.config.from_file(file_location=get_resource_path('config'))
    # Create artifact
    artifacts_client = ArtifactsClient(config)

    # Pull Image and Verify Signature Flow
    repo_name = "repo-name"
    trusted_keys = ["ocid1.key.oc1.region_name.bbqc3acqaadfa.abyhqljtb2hrommkvjggqn7zr3y3kt3akybs75qzoq7us6fwda2fcnoyzgb0",
                    "ocid1.key.oc1.region_name.bbqc3acqaadfa.abyhqljtb2hrommkvjggqn7zr3y3kt3akybs75qzoq7us6fwda2fcnoyzgb1"]

    verified = get_and_verify_image_signature_metadata(artifacts_client, config, compartment_id, False, repo_name,
                                                       image_digest,
                                                       trusted_keys)
    assert verified is True
