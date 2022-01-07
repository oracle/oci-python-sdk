# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_container_repository_compartment_details import ChangeContainerRepositoryCompartmentDetails
from .change_repository_compartment_details import ChangeRepositoryCompartmentDetails
from .container_configuration import ContainerConfiguration
from .container_image import ContainerImage
from .container_image_collection import ContainerImageCollection
from .container_image_layer import ContainerImageLayer
from .container_image_signature import ContainerImageSignature
from .container_image_signature_collection import ContainerImageSignatureCollection
from .container_image_signature_summary import ContainerImageSignatureSummary
from .container_image_summary import ContainerImageSummary
from .container_repository import ContainerRepository
from .container_repository_collection import ContainerRepositoryCollection
from .container_repository_readme import ContainerRepositoryReadme
from .container_repository_summary import ContainerRepositorySummary
from .container_version import ContainerVersion
from .create_container_image_signature_details import CreateContainerImageSignatureDetails
from .create_container_repository_details import CreateContainerRepositoryDetails
from .create_generic_repository_details import CreateGenericRepositoryDetails
from .create_repository_details import CreateRepositoryDetails
from .generic_artifact import GenericArtifact
from .generic_artifact_collection import GenericArtifactCollection
from .generic_artifact_summary import GenericArtifactSummary
from .generic_repository import GenericRepository
from .generic_repository_summary import GenericRepositorySummary
from .remove_container_version_details import RemoveContainerVersionDetails
from .repository import Repository
from .repository_collection import RepositoryCollection
from .repository_summary import RepositorySummary
from .restore_container_image_details import RestoreContainerImageDetails
from .update_container_configuration_details import UpdateContainerConfigurationDetails
from .update_container_repository_details import UpdateContainerRepositoryDetails
from .update_generic_artifact_by_path_details import UpdateGenericArtifactByPathDetails
from .update_generic_artifact_details import UpdateGenericArtifactDetails
from .update_generic_repository_details import UpdateGenericRepositoryDetails
from .update_repository_details import UpdateRepositoryDetails

# Maps type names to classes for artifacts services.
artifacts_type_mapping = {
    "ChangeContainerRepositoryCompartmentDetails": ChangeContainerRepositoryCompartmentDetails,
    "ChangeRepositoryCompartmentDetails": ChangeRepositoryCompartmentDetails,
    "ContainerConfiguration": ContainerConfiguration,
    "ContainerImage": ContainerImage,
    "ContainerImageCollection": ContainerImageCollection,
    "ContainerImageLayer": ContainerImageLayer,
    "ContainerImageSignature": ContainerImageSignature,
    "ContainerImageSignatureCollection": ContainerImageSignatureCollection,
    "ContainerImageSignatureSummary": ContainerImageSignatureSummary,
    "ContainerImageSummary": ContainerImageSummary,
    "ContainerRepository": ContainerRepository,
    "ContainerRepositoryCollection": ContainerRepositoryCollection,
    "ContainerRepositoryReadme": ContainerRepositoryReadme,
    "ContainerRepositorySummary": ContainerRepositorySummary,
    "ContainerVersion": ContainerVersion,
    "CreateContainerImageSignatureDetails": CreateContainerImageSignatureDetails,
    "CreateContainerRepositoryDetails": CreateContainerRepositoryDetails,
    "CreateGenericRepositoryDetails": CreateGenericRepositoryDetails,
    "CreateRepositoryDetails": CreateRepositoryDetails,
    "GenericArtifact": GenericArtifact,
    "GenericArtifactCollection": GenericArtifactCollection,
    "GenericArtifactSummary": GenericArtifactSummary,
    "GenericRepository": GenericRepository,
    "GenericRepositorySummary": GenericRepositorySummary,
    "RemoveContainerVersionDetails": RemoveContainerVersionDetails,
    "Repository": Repository,
    "RepositoryCollection": RepositoryCollection,
    "RepositorySummary": RepositorySummary,
    "RestoreContainerImageDetails": RestoreContainerImageDetails,
    "UpdateContainerConfigurationDetails": UpdateContainerConfigurationDetails,
    "UpdateContainerRepositoryDetails": UpdateContainerRepositoryDetails,
    "UpdateGenericArtifactByPathDetails": UpdateGenericArtifactByPathDetails,
    "UpdateGenericArtifactDetails": UpdateGenericArtifactDetails,
    "UpdateGenericRepositoryDetails": UpdateGenericRepositoryDetails,
    "UpdateRepositoryDetails": UpdateRepositoryDetails
}
