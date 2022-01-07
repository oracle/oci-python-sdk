# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTagDefaultDetails(object):
    """
    CreateTagDefaultDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTagDefaultDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTagDefaultDetails.
        :type compartment_id: str

        :param tag_definition_id:
            The value to assign to the tag_definition_id property of this CreateTagDefaultDetails.
        :type tag_definition_id: str

        :param value:
            The value to assign to the value property of this CreateTagDefaultDetails.
        :type value: str

        :param is_required:
            The value to assign to the is_required property of this CreateTagDefaultDetails.
        :type is_required: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'tag_definition_id': 'str',
            'value': 'str',
            'is_required': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'tag_definition_id': 'tagDefinitionId',
            'value': 'value',
            'is_required': 'isRequired'
        }

        self._compartment_id = None
        self._tag_definition_id = None
        self._value = None
        self._is_required = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateTagDefaultDetails.
        The OCID of the compartment. The tag default will be applied to all new resources created in this compartment.


        :return: The compartment_id of this CreateTagDefaultDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTagDefaultDetails.
        The OCID of the compartment. The tag default will be applied to all new resources created in this compartment.


        :param compartment_id: The compartment_id of this CreateTagDefaultDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tag_definition_id(self):
        """
        **[Required]** Gets the tag_definition_id of this CreateTagDefaultDetails.
        The OCID of the tag definition. The tag default will always assign a default value for this tag definition.


        :return: The tag_definition_id of this CreateTagDefaultDetails.
        :rtype: str
        """
        return self._tag_definition_id

    @tag_definition_id.setter
    def tag_definition_id(self, tag_definition_id):
        """
        Sets the tag_definition_id of this CreateTagDefaultDetails.
        The OCID of the tag definition. The tag default will always assign a default value for this tag definition.


        :param tag_definition_id: The tag_definition_id of this CreateTagDefaultDetails.
        :type: str
        """
        self._tag_definition_id = tag_definition_id

    @property
    def value(self):
        """
        **[Required]** Gets the value of this CreateTagDefaultDetails.
        The default value for the tag definition. This will be applied to all new resources created in the compartment.


        :return: The value of this CreateTagDefaultDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CreateTagDefaultDetails.
        The default value for the tag definition. This will be applied to all new resources created in the compartment.


        :param value: The value of this CreateTagDefaultDetails.
        :type: str
        """
        self._value = value

    @property
    def is_required(self):
        """
        Gets the is_required of this CreateTagDefaultDetails.
        If you specify that a value is required, a value is set during resource creation (either by
        the user creating the resource or another tag defualt). If no value is set, resource
        creation is blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :return: The is_required of this CreateTagDefaultDetails.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this CreateTagDefaultDetails.
        If you specify that a value is required, a value is set during resource creation (either by
        the user creating the resource or another tag defualt). If no value is set, resource
        creation is blocked.

        * If the `isRequired` flag is set to \"true\", the value is set during resource creation.
        * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

        Example: `false`


        :param is_required: The is_required of this CreateTagDefaultDetails.
        :type: bool
        """
        self._is_required = is_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
