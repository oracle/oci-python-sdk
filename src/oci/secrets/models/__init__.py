# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .base64_secret_bundle_content_details import Base64SecretBundleContentDetails
from .secret_bundle import SecretBundle
from .secret_bundle_content_details import SecretBundleContentDetails
from .secret_bundle_version_summary import SecretBundleVersionSummary

# Maps type names to classes for secrets services.
secrets_type_mapping = {
    "Base64SecretBundleContentDetails": Base64SecretBundleContentDetails,
    "SecretBundle": SecretBundle,
    "SecretBundleContentDetails": SecretBundleContentDetails,
    "SecretBundleVersionSummary": SecretBundleVersionSummary
}
