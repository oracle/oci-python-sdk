# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEndpointDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateEndpointDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateEndpointDetails.
        :type description: str

        :param model_id:
            The value to assign to the model_id property of this UpdateEndpointDetails.
        :type model_id: str

        :param inference_units:
            The value to assign to the inference_units property of this UpdateEndpointDetails.
        :type inference_units: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'model_id': 'str',
            'inference_units': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'model_id': 'modelId',
            'inference_units': 'inferenceUnits',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._model_id = None
        self._inference_units = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateEndpointDetails.
        A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.


        :return: The display_name of this UpdateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateEndpointDetails.
        A user-friendly display name for the resource. It should be unique and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateEndpointDetails.
        A short description of the endpoint.


        :return: The description of this UpdateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateEndpointDetails.
        A short description of the endpoint.


        :param description: The description of this UpdateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def model_id(self):
        """
        Gets the model_id of this UpdateEndpointDetails.
        The `OCID`__ of the model to associate with the endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The model_id of this UpdateEndpointDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this UpdateEndpointDetails.
        The `OCID`__ of the model to associate with the endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param model_id: The model_id of this UpdateEndpointDetails.
        :type: str
        """
        self._model_id = model_id

    @property
    def inference_units(self):
        """
        Gets the inference_units of this UpdateEndpointDetails.
        Number of replicas required for this endpoint. This will be optional parameter.


        :return: The inference_units of this UpdateEndpointDetails.
        :rtype: int
        """
        return self._inference_units

    @inference_units.setter
    def inference_units(self, inference_units):
        """
        Sets the inference_units of this UpdateEndpointDetails.
        Number of replicas required for this endpoint. This will be optional parameter.


        :param inference_units: The inference_units of this UpdateEndpointDetails.
        :type: int
        """
        self._inference_units = inference_units

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
