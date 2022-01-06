# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApmDomainDetails(object):
    """
    The information about the new APM domain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApmDomainDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateApmDomainDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateApmDomainDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateApmDomainDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateApmDomainDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateApmDomainDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateApmDomainDetails.
        :type is_free_tier: bool

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_free_tier': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_free_tier': 'isFreeTier'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_free_tier = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateApmDomainDetails.
        Display name of the APM domain.


        :return: The display_name of this CreateApmDomainDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateApmDomainDetails.
        Display name of the APM domain.


        :param display_name: The display_name of this CreateApmDomainDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateApmDomainDetails.
        Description of the APM domain.


        :return: The description of this CreateApmDomainDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateApmDomainDetails.
        Description of the APM domain.


        :param description: The description of this CreateApmDomainDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateApmDomainDetails.
        The OCID of the compartment corresponding to the APM domain.


        :return: The compartment_id of this CreateApmDomainDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateApmDomainDetails.
        The OCID of the compartment corresponding to the APM domain.


        :param compartment_id: The compartment_id of this CreateApmDomainDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateApmDomainDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateApmDomainDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateApmDomainDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateApmDomainDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateApmDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateApmDomainDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateApmDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateApmDomainDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this CreateApmDomainDetails.
        Indicates whether this is an \"Always Free\" resource. The default value is false.


        :return: The is_free_tier of this CreateApmDomainDetails.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this CreateApmDomainDetails.
        Indicates whether this is an \"Always Free\" resource. The default value is false.


        :param is_free_tier: The is_free_tier of this CreateApmDomainDetails.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
