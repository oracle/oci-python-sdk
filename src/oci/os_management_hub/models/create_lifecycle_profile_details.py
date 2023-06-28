# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_profile_details import CreateProfileDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLifecycleProfileDetails(CreateProfileDetails):
    """
    Description of a lifecycle registration profile to be created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLifecycleProfileDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.CreateLifecycleProfileDetails.profile_type` attribute
        of this class is ``LIFECYCLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateLifecycleProfileDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLifecycleProfileDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateLifecycleProfileDetails.
        :type description: str

        :param management_station_id:
            The value to assign to the management_station_id property of this CreateLifecycleProfileDetails.
        :type management_station_id: str

        :param profile_type:
            The value to assign to the profile_type property of this CreateLifecycleProfileDetails.
            Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"
        :type profile_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLifecycleProfileDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLifecycleProfileDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_stage_id:
            The value to assign to the lifecycle_stage_id property of this CreateLifecycleProfileDetails.
        :type lifecycle_stage_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'management_station_id': 'str',
            'profile_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_stage_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'management_station_id': 'managementStationId',
            'profile_type': 'profileType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_stage_id': 'lifecycleStageId'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._management_station_id = None
        self._profile_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_stage_id = None
        self._profile_type = 'LIFECYCLE'

    @property
    def lifecycle_stage_id(self):
        """
        **[Required]** Gets the lifecycle_stage_id of this CreateLifecycleProfileDetails.
        The OCID of the lifecycle stage from which the registration profile will inherit its software source.


        :return: The lifecycle_stage_id of this CreateLifecycleProfileDetails.
        :rtype: str
        """
        return self._lifecycle_stage_id

    @lifecycle_stage_id.setter
    def lifecycle_stage_id(self, lifecycle_stage_id):
        """
        Sets the lifecycle_stage_id of this CreateLifecycleProfileDetails.
        The OCID of the lifecycle stage from which the registration profile will inherit its software source.


        :param lifecycle_stage_id: The lifecycle_stage_id of this CreateLifecycleProfileDetails.
        :type: str
        """
        self._lifecycle_stage_id = lifecycle_stage_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
