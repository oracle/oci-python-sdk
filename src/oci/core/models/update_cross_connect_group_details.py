# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCrossConnectGroupDetails(object):
    """
    UpdateCrossConnectGroupDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCrossConnectGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateCrossConnectGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateCrossConnectGroupDetails.
        :type display_name: str

        :param customer_reference_name:
            The value to assign to the customer_reference_name property of this UpdateCrossConnectGroupDetails.
        :type customer_reference_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateCrossConnectGroupDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'customer_reference_name': 'str',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'customer_reference_name': 'customerReferenceName',
            'freeform_tags': 'freeformTags'
        }

        self._defined_tags = None
        self._display_name = None
        self._customer_reference_name = None
        self._freeform_tags = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateCrossConnectGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateCrossConnectGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateCrossConnectGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateCrossConnectGroupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateCrossConnectGroupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateCrossConnectGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateCrossConnectGroupDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateCrossConnectGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def customer_reference_name(self):
        """
        Gets the customer_reference_name of this UpdateCrossConnectGroupDetails.
        A reference name or identifier for the physical fiber connection that this cross-connect
        group uses.


        :return: The customer_reference_name of this UpdateCrossConnectGroupDetails.
        :rtype: str
        """
        return self._customer_reference_name

    @customer_reference_name.setter
    def customer_reference_name(self, customer_reference_name):
        """
        Sets the customer_reference_name of this UpdateCrossConnectGroupDetails.
        A reference name or identifier for the physical fiber connection that this cross-connect
        group uses.


        :param customer_reference_name: The customer_reference_name of this UpdateCrossConnectGroupDetails.
        :type: str
        """
        self._customer_reference_name = customer_reference_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateCrossConnectGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateCrossConnectGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateCrossConnectGroupDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateCrossConnectGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
