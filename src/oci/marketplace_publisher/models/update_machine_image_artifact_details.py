# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201

from .update_artifact_details import UpdateArtifactDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMachineImageArtifactDetails(UpdateArtifactDetails):
    """
    Details to update Machine Image Artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMachineImageArtifactDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.UpdateMachineImageArtifactDetails.artifact_type` attribute
        of this class is ``MACHINE_IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateMachineImageArtifactDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this UpdateMachineImageArtifactDetails.
        :type display_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this UpdateMachineImageArtifactDetails.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART", "MACHINE_IMAGE", "STACK"
        :type artifact_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMachineImageArtifactDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMachineImageArtifactDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param machine_image:
            The value to assign to the machine_image property of this UpdateMachineImageArtifactDetails.
        :type machine_image: oci.marketplace_publisher.models.UpdateMachineImageDetails

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'artifact_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'machine_image': 'UpdateMachineImageDetails'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'artifact_type': 'artifactType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'machine_image': 'machineImage'
        }
        self._compartment_id = None
        self._display_name = None
        self._artifact_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._machine_image = None
        self._artifact_type = 'MACHINE_IMAGE'

    @property
    def machine_image(self):
        """
        Gets the machine_image of this UpdateMachineImageArtifactDetails.

        :return: The machine_image of this UpdateMachineImageArtifactDetails.
        :rtype: oci.marketplace_publisher.models.UpdateMachineImageDetails
        """
        return self._machine_image

    @machine_image.setter
    def machine_image(self, machine_image):
        """
        Sets the machine_image of this UpdateMachineImageArtifactDetails.

        :param machine_image: The machine_image of this UpdateMachineImageArtifactDetails.
        :type: oci.marketplace_publisher.models.UpdateMachineImageDetails
        """
        self._machine_image = machine_image

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
