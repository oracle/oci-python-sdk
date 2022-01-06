# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateEsxiHostDetails(object):
    """
    The ESXi host information to be updated.
    """

    #: A constant which can be used with the next_sku property of a UpdateEsxiHostDetails.
    #: This constant has a value of "HOUR"
    NEXT_SKU_HOUR = "HOUR"

    #: A constant which can be used with the next_sku property of a UpdateEsxiHostDetails.
    #: This constant has a value of "MONTH"
    NEXT_SKU_MONTH = "MONTH"

    #: A constant which can be used with the next_sku property of a UpdateEsxiHostDetails.
    #: This constant has a value of "ONE_YEAR"
    NEXT_SKU_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the next_sku property of a UpdateEsxiHostDetails.
    #: This constant has a value of "THREE_YEARS"
    NEXT_SKU_THREE_YEARS = "THREE_YEARS"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateEsxiHostDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateEsxiHostDetails.
        :type display_name: str

        :param next_sku:
            The value to assign to the next_sku property of this UpdateEsxiHostDetails.
            Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"
        :type next_sku: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateEsxiHostDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateEsxiHostDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'next_sku': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'next_sku': 'nextSku',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._next_sku = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateEsxiHostDetails.
        A descriptive name for the ESXi host. It's changeable.
        Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the SDDC.

        Avoid entering confidential information.


        :return: The display_name of this UpdateEsxiHostDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateEsxiHostDetails.
        A descriptive name for the ESXi host. It's changeable.
        Esxi Host name requirements are 1-16 character length limit, Must start with a letter, Must be English letters, numbers, - only, No repeating hyphens, Must be unique within the SDDC.

        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateEsxiHostDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def next_sku(self):
        """
        Gets the next_sku of this UpdateEsxiHostDetails.
        The billing option to switch to after the existing billing cycle ends.
        If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
        :func:`list_supported_skus`.

        Allowed values for this property are: "HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"


        :return: The next_sku of this UpdateEsxiHostDetails.
        :rtype: str
        """
        return self._next_sku

    @next_sku.setter
    def next_sku(self, next_sku):
        """
        Sets the next_sku of this UpdateEsxiHostDetails.
        The billing option to switch to after the existing billing cycle ends.
        If `nextSku` is null or empty, `currentSku` continues to the next billing cycle.
        :func:`list_supported_skus`.


        :param next_sku: The next_sku of this UpdateEsxiHostDetails.
        :type: str
        """
        allowed_values = ["HOUR", "MONTH", "ONE_YEAR", "THREE_YEARS"]
        if not value_allowed_none_or_none_sentinel(next_sku, allowed_values):
            raise ValueError(
                "Invalid value for `next_sku`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._next_sku = next_sku

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateEsxiHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateEsxiHostDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateEsxiHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateEsxiHostDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateEsxiHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateEsxiHostDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateEsxiHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateEsxiHostDetails.
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
