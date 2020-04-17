# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSoftwareSourceDetails(object):
    """
    Information for updating a software source on the management system
    """

    #: A constant which can be used with the checksum_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "SHA1"
    CHECKSUM_TYPE_SHA1 = "SHA1"

    #: A constant which can be used with the checksum_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "SHA256"
    CHECKSUM_TYPE_SHA256 = "SHA256"

    #: A constant which can be used with the checksum_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "SHA384"
    CHECKSUM_TYPE_SHA384 = "SHA384"

    #: A constant which can be used with the checksum_type property of a UpdateSoftwareSourceDetails.
    #: This constant has a value of "SHA512"
    CHECKSUM_TYPE_SHA512 = "SHA512"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSoftwareSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateSoftwareSourceDetails.
        :type description: str

        :param maintainer_name:
            The value to assign to the maintainer_name property of this UpdateSoftwareSourceDetails.
        :type maintainer_name: str

        :param maintainer_email:
            The value to assign to the maintainer_email property of this UpdateSoftwareSourceDetails.
        :type maintainer_email: str

        :param maintainer_phone:
            The value to assign to the maintainer_phone property of this UpdateSoftwareSourceDetails.
        :type maintainer_phone: str

        :param checksum_type:
            The value to assign to the checksum_type property of this UpdateSoftwareSourceDetails.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512"
        :type checksum_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'maintainer_name': 'str',
            'maintainer_email': 'str',
            'maintainer_phone': 'str',
            'checksum_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'maintainer_name': 'maintainerName',
            'maintainer_email': 'maintainerEmail',
            'maintainer_phone': 'maintainerPhone',
            'checksum_type': 'checksumType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._maintainer_name = None
        self._maintainer_email = None
        self._maintainer_phone = None
        self._checksum_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSoftwareSourceDetails.
        User friendly name for the software source


        :return: The display_name of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSoftwareSourceDetails.
        User friendly name for the software source


        :param display_name: The display_name of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateSoftwareSourceDetails.
        Information specified by the user about the software source


        :return: The description of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSoftwareSourceDetails.
        Information specified by the user about the software source


        :param description: The description of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._description = description

    @property
    def maintainer_name(self):
        """
        Gets the maintainer_name of this UpdateSoftwareSourceDetails.
        Name of the person maintaining this software source


        :return: The maintainer_name of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._maintainer_name

    @maintainer_name.setter
    def maintainer_name(self, maintainer_name):
        """
        Sets the maintainer_name of this UpdateSoftwareSourceDetails.
        Name of the person maintaining this software source


        :param maintainer_name: The maintainer_name of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._maintainer_name = maintainer_name

    @property
    def maintainer_email(self):
        """
        Gets the maintainer_email of this UpdateSoftwareSourceDetails.
        Email address of the person maintaining this software source


        :return: The maintainer_email of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._maintainer_email

    @maintainer_email.setter
    def maintainer_email(self, maintainer_email):
        """
        Sets the maintainer_email of this UpdateSoftwareSourceDetails.
        Email address of the person maintaining this software source


        :param maintainer_email: The maintainer_email of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._maintainer_email = maintainer_email

    @property
    def maintainer_phone(self):
        """
        Gets the maintainer_phone of this UpdateSoftwareSourceDetails.
        Phone number of the person maintaining this software source


        :return: The maintainer_phone of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._maintainer_phone

    @maintainer_phone.setter
    def maintainer_phone(self, maintainer_phone):
        """
        Sets the maintainer_phone of this UpdateSoftwareSourceDetails.
        Phone number of the person maintaining this software source


        :param maintainer_phone: The maintainer_phone of this UpdateSoftwareSourceDetails.
        :type: str
        """
        self._maintainer_phone = maintainer_phone

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this UpdateSoftwareSourceDetails.
        The yum repository checksum type used by this software source

        Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512"


        :return: The checksum_type of this UpdateSoftwareSourceDetails.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this UpdateSoftwareSourceDetails.
        The yum repository checksum type used by this software source


        :param checksum_type: The checksum_type of this UpdateSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["SHA1", "SHA256", "SHA384", "SHA512"]
        if not value_allowed_none_or_none_sentinel(checksum_type, allowed_values):
            raise ValueError(
                "Invalid value for `checksum_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._checksum_type = checksum_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSoftwareSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateSoftwareSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSoftwareSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateSoftwareSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSoftwareSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateSoftwareSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSoftwareSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateSoftwareSourceDetails.
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
