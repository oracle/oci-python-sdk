# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Application(object):
    """
    An application contains functions and defined attributes shared between those functions, such as network configuration and configuration. Avoid entering confidential information.
    """

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Application object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Application.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Application.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Application.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Application.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param config:
            The value to assign to the config property of this Application.
        :type config: dict(str, str)

        :param subnet_ids:
            The value to assign to the subnet_ids property of this Application.
        :type subnet_ids: list[str]

        :param syslog_url:
            The value to assign to the syslog_url property of this Application.
        :type syslog_url: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Application.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Application.
        :type defined_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this Application.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Application.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'config': 'dict(str, str)',
            'subnet_ids': 'list[str]',
            'syslog_url': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'config': 'config',
            'subnet_ids': 'subnetIds',
            'syslog_url': 'syslogUrl',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._config = None
        self._subnet_ids = None
        self._syslog_url = None
        self._freeform_tags = None
        self._defined_tags = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Application.
        The `OCID`__ of the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Application.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Application.
        The `OCID`__ of the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Application.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Application.
        The OCID of the compartment that contains the application.


        :return: The compartment_id of this Application.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Application.
        The OCID of the compartment that contains the application.


        :param compartment_id: The compartment_id of this Application.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Application.
        The display name of the application. The display name is unique within the compartment containing the application.


        :return: The display_name of this Application.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Application.
        The display name of the application. The display name is unique within the compartment containing the application.


        :param display_name: The display_name of this Application.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Application.
        The current state of the application.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Application.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Application.
        The current state of the application.


        :param lifecycle_state: The lifecycle_state of this Application.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def config(self):
        """
        Gets the config of this Application.
        Application configuration for functions in this application (passed as environment variables). Can be overridden by function configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :return: The config of this Application.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this Application.
        Application configuration for functions in this application (passed as environment variables). Can be overridden by function configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :param config: The config of this Application.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def subnet_ids(self):
        """
        Gets the subnet_ids of this Application.
        The `OCID`__s of the subnets in which to run functions in the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_ids of this Application.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this Application.
        The `OCID`__s of the subnets in which to run functions in the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_ids: The subnet_ids of this Application.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def syslog_url(self):
        """
        Gets the syslog_url of this Application.
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
        The syslog URL must be reachable from all of the subnets configured for the application.
        Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL.

        Example: `tcp://logserver.myserver:1234`


        :return: The syslog_url of this Application.
        :rtype: str
        """
        return self._syslog_url

    @syslog_url.setter
    def syslog_url(self, syslog_url):
        """
        Sets the syslog_url of this Application.
        A syslog URL to which to send all function logs. Supports tcp, udp, and tcp+tls.
        The syslog URL must be reachable from all of the subnets configured for the application.
        Note: If you enable the OCI Logging service for this application, the syslogUrl value is ignored. Function logs are sent to the OCI Logging service, and not to the syslog URL.

        Example: `tcp://logserver.myserver:1234`


        :param syslog_url: The syslog_url of this Application.
        :type: str
        """
        self._syslog_url = syslog_url

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Application.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Application.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Application.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Application.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Application.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Application.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Application.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Application.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def time_created(self):
        """
        Gets the time_created of this Application.
        The time the application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Application.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Application.
        The time the application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Application.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Application.
        The time the application was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Application.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Application.
        The time the application was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Application.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
