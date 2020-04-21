# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_notebook_session_compartment_details import ChangeNotebookSessionCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .create_model_details import CreateModelDetails
from .create_model_provenance_details import CreateModelProvenanceDetails
from .create_notebook_session_details import CreateNotebookSessionDetails
from .create_project_details import CreateProjectDetails
from .model import Model
from .model_provenance import ModelProvenance
from .model_summary import ModelSummary
from .notebook_session import NotebookSession
from .notebook_session_configuration_details import NotebookSessionConfigurationDetails
from .notebook_session_shape_summary import NotebookSessionShapeSummary
from .notebook_session_summary import NotebookSessionSummary
from .project import Project
from .project_summary import ProjectSummary
from .update_model_details import UpdateModelDetails
from .update_model_provenance_details import UpdateModelProvenanceDetails
from .update_notebook_session_details import UpdateNotebookSessionDetails
from .update_project_details import UpdateProjectDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for data_science services.
data_science_type_mapping = {
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeNotebookSessionCompartmentDetails": ChangeNotebookSessionCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateModelProvenanceDetails": CreateModelProvenanceDetails,
    "CreateNotebookSessionDetails": CreateNotebookSessionDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "Model": Model,
    "ModelProvenance": ModelProvenance,
    "ModelSummary": ModelSummary,
    "NotebookSession": NotebookSession,
    "NotebookSessionConfigurationDetails": NotebookSessionConfigurationDetails,
    "NotebookSessionShapeSummary": NotebookSessionShapeSummary,
    "NotebookSessionSummary": NotebookSessionSummary,
    "Project": Project,
    "ProjectSummary": ProjectSummary,
    "UpdateModelDetails": UpdateModelDetails,
    "UpdateModelProvenanceDetails": UpdateModelProvenanceDetails,
    "UpdateNotebookSessionDetails": UpdateNotebookSessionDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
