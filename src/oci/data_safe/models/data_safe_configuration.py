# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSafeConfiguration(object):
    """
    A Data Safe configuration for a tenancy and region.
    """

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DataSafeConfiguration.
    #: This constant has a value of "NA"
    LIFECYCLE_STATE_NA = "NA"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSafeConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this DataSafeConfiguration.
        :type is_enabled: bool

        :param url:
            The value to assign to the url property of this DataSafeConfiguration.
        :type url: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DataSafeConfiguration.
        :type compartment_id: str

        :param time_enabled:
            The value to assign to the time_enabled property of this DataSafeConfiguration.
        :type time_enabled: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataSafeConfiguration.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DataSafeConfiguration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DataSafeConfiguration.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'url': 'str',
            'compartment_id': 'str',
            'time_enabled': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'url': 'url',
            'compartment_id': 'compartmentId',
            'time_enabled': 'timeEnabled',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._is_enabled = None
        self._url = None
        self._compartment_id = None
        self._time_enabled = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this DataSafeConfiguration.
        Indicates if Data Safe is enabled.


        :return: The is_enabled of this DataSafeConfiguration.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DataSafeConfiguration.
        Indicates if Data Safe is enabled.


        :param is_enabled: The is_enabled of this DataSafeConfiguration.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def url(self):
        """
        Gets the url of this DataSafeConfiguration.
        The URL of the Data Safe service.


        :return: The url of this DataSafeConfiguration.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DataSafeConfiguration.
        The URL of the Data Safe service.


        :param url: The url of this DataSafeConfiguration.
        :type: str
        """
        self._url = url

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DataSafeConfiguration.
        The OCID of the tenancy used to enable Data Safe.


        :return: The compartment_id of this DataSafeConfiguration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataSafeConfiguration.
        The OCID of the tenancy used to enable Data Safe.


        :param compartment_id: The compartment_id of this DataSafeConfiguration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_enabled(self):
        """
        Gets the time_enabled of this DataSafeConfiguration.
        The date and time Data Safe was enabled, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_enabled of this DataSafeConfiguration.
        :rtype: datetime
        """
        return self._time_enabled

    @time_enabled.setter
    def time_enabled(self, time_enabled):
        """
        Sets the time_enabled of this DataSafeConfiguration.
        The date and time Data Safe was enabled, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_enabled: The time_enabled of this DataSafeConfiguration.
        :type: datetime
        """
        self._time_enabled = time_enabled

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataSafeConfiguration.
        The current state of Data Safe.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataSafeConfiguration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataSafeConfiguration.
        The current state of Data Safe.


        :param lifecycle_state: The lifecycle_state of this DataSafeConfiguration.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DataSafeConfiguration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DataSafeConfiguration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DataSafeConfiguration.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DataSafeConfiguration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DataSafeConfiguration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DataSafeConfiguration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DataSafeConfiguration.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DataSafeConfiguration.
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
