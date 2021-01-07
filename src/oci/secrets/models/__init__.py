# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
