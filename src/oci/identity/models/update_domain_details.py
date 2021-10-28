# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDomainDetails(object):
    """
    Update domain details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDomainDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateDomainDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDomainDetails.
        :type display_name: str

        :param is_hidden_on_login:
            The value to assign to the is_hidden_on_login property of this UpdateDomainDetails.
        :type is_hidden_on_login: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDomainDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDomainDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'is_hidden_on_login': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'is_hidden_on_login': 'isHiddenOnLogin',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._is_hidden_on_login = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateDomainDetails.
        The domain description


        :return: The description of this UpdateDomainDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDomainDetails.
        The domain description


        :param description: The description of this UpdateDomainDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDomainDetails.
        The mutable display name of the domain


        :return: The display_name of this UpdateDomainDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDomainDetails.
        The mutable display name of the domain


        :param display_name: The display_name of this UpdateDomainDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_hidden_on_login(self):
        """
        Gets the is_hidden_on_login of this UpdateDomainDetails.
        Indicates whether domain is hidden on login screen or not.


        :return: The is_hidden_on_login of this UpdateDomainDetails.
        :rtype: bool
        """
        return self._is_hidden_on_login

    @is_hidden_on_login.setter
    def is_hidden_on_login(self, is_hidden_on_login):
        """
        Sets the is_hidden_on_login of this UpdateDomainDetails.
        Indicates whether domain is hidden on login screen or not.


        :param is_hidden_on_login: The is_hidden_on_login of this UpdateDomainDetails.
        :type: bool
        """
        self._is_hidden_on_login = is_hidden_on_login

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDomainDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDomainDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDomainDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDomainDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDomainDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDomainDetails.
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
