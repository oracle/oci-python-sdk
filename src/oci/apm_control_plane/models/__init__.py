# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .apm_domain import ApmDomain
from .apm_domain_summary import ApmDomainSummary
from .base_domain_details import BaseDomainDetails
from .base_key_details import BaseKeyDetails
from .change_apm_domain_compartment_details import ChangeApmDomainCompartmentDetails
from .create_apm_domain_details import CreateApmDomainDetails
from .data_key import DataKey
from .data_key_summary import DataKeySummary
from .generate_data_key_details import GenerateDataKeyDetails
from .remove_data_key_details import RemoveDataKeyDetails
from .update_apm_domain_details import UpdateApmDomainDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for apm_control_plane services.
apm_control_plane_type_mapping = {
    "ApmDomain": ApmDomain,
    "ApmDomainSummary": ApmDomainSummary,
    "BaseDomainDetails": BaseDomainDetails,
    "BaseKeyDetails": BaseKeyDetails,
    "ChangeApmDomainCompartmentDetails": ChangeApmDomainCompartmentDetails,
    "CreateApmDomainDetails": CreateApmDomainDetails,
    "DataKey": DataKey,
    "DataKeySummary": DataKeySummary,
    "GenerateDataKeyDetails": GenerateDataKeyDetails,
    "RemoveDataKeyDetails": RemoveDataKeyDetails,
    "UpdateApmDomainDetails": UpdateApmDomainDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
