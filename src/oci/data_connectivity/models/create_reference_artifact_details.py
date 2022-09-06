# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateReferenceArtifactDetails(object):
    """
    Represents the info required for creating a DCMS artifact reference.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateReferenceArtifactDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_artifact_id:
            The value to assign to the service_artifact_id property of this CreateReferenceArtifactDetails.
        :type service_artifact_id: str

        """
        self.swagger_types = {
            'service_artifact_id': 'str'
        }

        self.attribute_map = {
            'service_artifact_id': 'serviceArtifactId'
        }

        self._service_artifact_id = None

    @property
    def service_artifact_id(self):
        """
        **[Required]** Gets the service_artifact_id of this CreateReferenceArtifactDetails.
        The unique ID of the service that is referencing a data asset.


        :return: The service_artifact_id of this CreateReferenceArtifactDetails.
        :rtype: str
        """
        return self._service_artifact_id

    @service_artifact_id.setter
    def service_artifact_id(self, service_artifact_id):
        """
        Sets the service_artifact_id of this CreateReferenceArtifactDetails.
        The unique ID of the service that is referencing a data asset.


        :param service_artifact_id: The service_artifact_id of this CreateReferenceArtifactDetails.
        :type: str
        """
        self._service_artifact_id = service_artifact_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
