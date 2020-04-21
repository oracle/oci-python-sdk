# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOdaInstanceDetails(object):
    """
    Properties that are required to create a Digital Assistant instance.
    """

    #: A constant which can be used with the shape_name property of a CreateOdaInstanceDetails.
    #: This constant has a value of "DEVELOPMENT"
    SHAPE_NAME_DEVELOPMENT = "DEVELOPMENT"

    #: A constant which can be used with the shape_name property of a CreateOdaInstanceDetails.
    #: This constant has a value of "PRODUCTION"
    SHAPE_NAME_PRODUCTION = "PRODUCTION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOdaInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateOdaInstanceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateOdaInstanceDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOdaInstanceDetails.
        :type compartment_id: str

        :param shape_name:
            The value to assign to the shape_name property of this CreateOdaInstanceDetails.
            Allowed values for this property are: "DEVELOPMENT", "PRODUCTION"
        :type shape_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOdaInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOdaInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'shape_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'shape_name': 'shapeName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._shape_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateOdaInstanceDetails.
        User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.


        :return: The display_name of this CreateOdaInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateOdaInstanceDetails.
        User-friendly name for the instance. Avoid entering confidential information. You can change this value anytime.


        :param display_name: The display_name of this CreateOdaInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateOdaInstanceDetails.
        Description of the Digital Assistant instance.


        :return: The description of this CreateOdaInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOdaInstanceDetails.
        Description of the Digital Assistant instance.


        :param description: The description of this CreateOdaInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOdaInstanceDetails.
        Identifier of the compartment.


        :return: The compartment_id of this CreateOdaInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOdaInstanceDetails.
        Identifier of the compartment.


        :param compartment_id: The compartment_id of this CreateOdaInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this CreateOdaInstanceDetails.
        Shape or size of the instance.

        Allowed values for this property are: "DEVELOPMENT", "PRODUCTION"


        :return: The shape_name of this CreateOdaInstanceDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this CreateOdaInstanceDetails.
        Shape or size of the instance.


        :param shape_name: The shape_name of this CreateOdaInstanceDetails.
        :type: str
        """
        allowed_values = ["DEVELOPMENT", "PRODUCTION"]
        if not value_allowed_none_or_none_sentinel(shape_name, allowed_values):
            raise ValueError(
                "Invalid value for `shape_name`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._shape_name = shape_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOdaInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for
        cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOdaInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOdaInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for
        cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOdaInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOdaInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOdaInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOdaInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOdaInstanceDetails.
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
