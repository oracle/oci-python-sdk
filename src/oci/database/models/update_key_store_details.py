# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateKeyStoreDetails(object):
    """
    Details for updating the key store.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateKeyStoreDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type_details:
            The value to assign to the type_details property of this UpdateKeyStoreDetails.
        :type type_details: oci.database.models.KeyStoreTypeDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateKeyStoreDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateKeyStoreDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type_details': 'KeyStoreTypeDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type_details': 'typeDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._type_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def type_details(self):
        """
        Gets the type_details of this UpdateKeyStoreDetails.

        :return: The type_details of this UpdateKeyStoreDetails.
        :rtype: oci.database.models.KeyStoreTypeDetails
        """
        return self._type_details

    @type_details.setter
    def type_details(self, type_details):
        """
        Sets the type_details of this UpdateKeyStoreDetails.

        :param type_details: The type_details of this UpdateKeyStoreDetails.
        :type: oci.database.models.KeyStoreTypeDetails
        """
        self._type_details = type_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateKeyStoreDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateKeyStoreDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateKeyStoreDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateKeyStoreDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateKeyStoreDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateKeyStoreDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateKeyStoreDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateKeyStoreDetails.
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
