# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaptureFilter(object):
    """
    A capture filter contains a set of *:func:`capture_filter_rule_details`* governing what traffic a *:class:`Vtap`* mirrors.
    The capture filter is created with no rules defined, and it must have at least one rule for the VTAP to start mirroring traffic.
    """

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CaptureFilter.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the filter_type property of a CaptureFilter.
    #: This constant has a value of "VTAP"
    FILTER_TYPE_VTAP = "VTAP"

    def __init__(self, **kwargs):
        """
        Initializes a new CaptureFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CaptureFilter.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CaptureFilter.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CaptureFilter.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CaptureFilter.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this CaptureFilter.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CaptureFilter.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param filter_type:
            The value to assign to the filter_type property of this CaptureFilter.
            Allowed values for this property are: "VTAP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        :param time_created:
            The value to assign to the time_created property of this CaptureFilter.
        :type time_created: datetime

        :param vtap_capture_filter_rules:
            The value to assign to the vtap_capture_filter_rules property of this CaptureFilter.
        :type vtap_capture_filter_rules: list[oci.core.models.VtapCaptureFilterRuleDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'filter_type': 'str',
            'time_created': 'datetime',
            'vtap_capture_filter_rules': 'list[VtapCaptureFilterRuleDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'filter_type': 'filterType',
            'time_created': 'timeCreated',
            'vtap_capture_filter_rules': 'vtapCaptureFilterRules'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._filter_type = None
        self._time_created = None
        self._vtap_capture_filter_rules = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CaptureFilter.
        The `OCID`__ of the compartment containing the capture filter.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CaptureFilter.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CaptureFilter.
        The `OCID`__ of the compartment containing the capture filter.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CaptureFilter.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CaptureFilter.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CaptureFilter.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CaptureFilter.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CaptureFilter.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CaptureFilter.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CaptureFilter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CaptureFilter.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CaptureFilter.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CaptureFilter.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CaptureFilter.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CaptureFilter.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CaptureFilter.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CaptureFilter.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this CaptureFilter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CaptureFilter.
        The capture filter's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this CaptureFilter.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CaptureFilter.
        The capture filter's current administrative state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CaptureFilter.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CaptureFilter.
        The capture filter's current administrative state.


        :param lifecycle_state: The lifecycle_state of this CaptureFilter.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def filter_type(self):
        """
        Gets the filter_type of this CaptureFilter.
        Indicates which service will use this capture filter

        Allowed values for this property are: "VTAP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this CaptureFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this CaptureFilter.
        Indicates which service will use this capture filter


        :param filter_type: The filter_type of this CaptureFilter.
        :type: str
        """
        allowed_values = ["VTAP"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            filter_type = 'UNKNOWN_ENUM_VALUE'
        self._filter_type = filter_type

    @property
    def time_created(self):
        """
        Gets the time_created of this CaptureFilter.
        The date and time the capture filter was created, in the format defined by `RFC3339`__.

        Example: `2021-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this CaptureFilter.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CaptureFilter.
        The date and time the capture filter was created, in the format defined by `RFC3339`__.

        Example: `2021-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this CaptureFilter.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vtap_capture_filter_rules(self):
        """
        Gets the vtap_capture_filter_rules of this CaptureFilter.
        The set of rules governing what traffic a VTAP mirrors.


        :return: The vtap_capture_filter_rules of this CaptureFilter.
        :rtype: list[oci.core.models.VtapCaptureFilterRuleDetails]
        """
        return self._vtap_capture_filter_rules

    @vtap_capture_filter_rules.setter
    def vtap_capture_filter_rules(self, vtap_capture_filter_rules):
        """
        Sets the vtap_capture_filter_rules of this CaptureFilter.
        The set of rules governing what traffic a VTAP mirrors.


        :param vtap_capture_filter_rules: The vtap_capture_filter_rules of this CaptureFilter.
        :type: list[oci.core.models.VtapCaptureFilterRuleDetails]
        """
        self._vtap_capture_filter_rules = vtap_capture_filter_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
