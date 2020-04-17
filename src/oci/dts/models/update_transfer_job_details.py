# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTransferJobDetails(object):
    """
    UpdateTransferJobDetails model.
    """

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferJobDetails.
    #: This constant has a value of "CLOSED"
    LIFECYCLE_STATE_CLOSED = "CLOSED"

    #: A constant which can be used with the device_type property of a UpdateTransferJobDetails.
    #: This constant has a value of "DISK"
    DEVICE_TYPE_DISK = "DISK"

    #: A constant which can be used with the device_type property of a UpdateTransferJobDetails.
    #: This constant has a value of "APPLIANCE"
    DEVICE_TYPE_APPLIANCE = "APPLIANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTransferJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UpdateTransferJobDetails.
            Allowed values for this property are: "CLOSED"
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this UpdateTransferJobDetails.
        :type display_name: str

        :param device_type:
            The value to assign to the device_type property of this UpdateTransferJobDetails.
            Allowed values for this property are: "DISK", "APPLIANCE"
        :type device_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTransferJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTransferJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'display_name': 'str',
            'device_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'device_type': 'deviceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._lifecycle_state = None
        self._display_name = None
        self._device_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UpdateTransferJobDetails.
        Allowed values for this property are: "CLOSED"


        :return: The lifecycle_state of this UpdateTransferJobDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UpdateTransferJobDetails.

        :param lifecycle_state: The lifecycle_state of this UpdateTransferJobDetails.
        :type: str
        """
        allowed_values = ["CLOSED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateTransferJobDetails.

        :return: The display_name of this UpdateTransferJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateTransferJobDetails.

        :param display_name: The display_name of this UpdateTransferJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def device_type(self):
        """
        Gets the device_type of this UpdateTransferJobDetails.
        Allowed values for this property are: "DISK", "APPLIANCE"


        :return: The device_type of this UpdateTransferJobDetails.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this UpdateTransferJobDetails.

        :param device_type: The device_type of this UpdateTransferJobDetails.
        :type: str
        """
        allowed_values = ["DISK", "APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(device_type, allowed_values):
            raise ValueError(
                "Invalid value for `device_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._device_type = device_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateTransferJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateTransferJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateTransferJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateTransferJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateTransferJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateTransferJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateTransferJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateTransferJobDetails.
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
