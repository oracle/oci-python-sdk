# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmSummary(object):
    """
    A summary of properties for the specified alarm.
    For information about alarms, see `Alarms Overview`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    For information about endpoints and signing API requests, see
    `About the API`__. For information about available SDKs and tools, see
    `SDKS and Other Tools`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/usingapi.htm
    __ https://docs.cloud.oracle.com/iaas/Content/API/Concepts/sdks.htm
    """

    #: A constant which can be used with the severity property of a AlarmSummary.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a AlarmSummary.
    #: This constant has a value of "ERROR"
    SEVERITY_ERROR = "ERROR"

    #: A constant which can be used with the severity property of a AlarmSummary.
    #: This constant has a value of "WARNING"
    SEVERITY_WARNING = "WARNING"

    #: A constant which can be used with the severity property of a AlarmSummary.
    #: This constant has a value of "INFO"
    SEVERITY_INFO = "INFO"

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AlarmSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AlarmSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AlarmSummary.
        :type compartment_id: str

        :param metric_compartment_id:
            The value to assign to the metric_compartment_id property of this AlarmSummary.
        :type metric_compartment_id: str

        :param namespace:
            The value to assign to the namespace property of this AlarmSummary.
        :type namespace: str

        :param query:
            The value to assign to the query property of this AlarmSummary.
        :type query: str

        :param severity:
            The value to assign to the severity property of this AlarmSummary.
            Allowed values for this property are: "CRITICAL", "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param destinations:
            The value to assign to the destinations property of this AlarmSummary.
        :type destinations: list[str]

        :param suppression:
            The value to assign to the suppression property of this AlarmSummary.
        :type suppression: oci.monitoring.models.Suppression

        :param is_enabled:
            The value to assign to the is_enabled property of this AlarmSummary.
        :type is_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AlarmSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AlarmSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AlarmSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'metric_compartment_id': 'str',
            'namespace': 'str',
            'query': 'str',
            'severity': 'str',
            'destinations': 'list[str]',
            'suppression': 'Suppression',
            'is_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'metric_compartment_id': 'metricCompartmentId',
            'namespace': 'namespace',
            'query': 'query',
            'severity': 'severity',
            'destinations': 'destinations',
            'suppression': 'suppression',
            'is_enabled': 'isEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._metric_compartment_id = None
        self._namespace = None
        self._query = None
        self._severity = None
        self._destinations = None
        self._suppression = None
        self._is_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AlarmSummary.
        The `OCID`__ of the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AlarmSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlarmSummary.
        The `OCID`__ of the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AlarmSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AlarmSummary.
        A user-friendly name for the alarm. It does not have to be unique, and it's changeable.

        This name is sent as the title for notifications related to this alarm.

        Example: `High CPU Utilization`


        :return: The display_name of this AlarmSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AlarmSummary.
        A user-friendly name for the alarm. It does not have to be unique, and it's changeable.

        This name is sent as the title for notifications related to this alarm.

        Example: `High CPU Utilization`


        :param display_name: The display_name of this AlarmSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AlarmSummary.
        The `OCID`__ of the compartment containing the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AlarmSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AlarmSummary.
        The `OCID`__ of the compartment containing the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AlarmSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metric_compartment_id(self):
        """
        **[Required]** Gets the metric_compartment_id of this AlarmSummary.
        The `OCID`__ of the compartment containing the metric
        being evaluated by the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The metric_compartment_id of this AlarmSummary.
        :rtype: str
        """
        return self._metric_compartment_id

    @metric_compartment_id.setter
    def metric_compartment_id(self, metric_compartment_id):
        """
        Sets the metric_compartment_id of this AlarmSummary.
        The `OCID`__ of the compartment containing the metric
        being evaluated by the alarm.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param metric_compartment_id: The metric_compartment_id of this AlarmSummary.
        :type: str
        """
        self._metric_compartment_id = metric_compartment_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this AlarmSummary.
        The source service or application emitting the metric that is evaluated by the alarm.

        Example: `oci_computeagent`


        :return: The namespace of this AlarmSummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this AlarmSummary.
        The source service or application emitting the metric that is evaluated by the alarm.

        Example: `oci_computeagent`


        :param namespace: The namespace of this AlarmSummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def query(self):
        """
        **[Required]** Gets the query of this AlarmSummary.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval depend on the specified time range. More
        interval values are supported for smaller time ranges. Supported grouping functions: `grouping()`, `groupBy()`.
        For details about Monitoring Query Language (MQL), see `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service.
        See `Supported Services`__.

        Example of threshold alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

          -----

        Example of absence alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

          -----

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :return: The query of this AlarmSummary.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this AlarmSummary.
        The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of
        the Monitoring service interprets results for each returned time series as Boolean values,
        where zero represents false and a non-zero value represents true. A true value means that the trigger
        rule condition has been met. The query must specify a metric, statistic, interval, and trigger
        rule (threshold or absence). Supported values for interval depend on the specified time range. More
        interval values are supported for smaller time ranges. Supported grouping functions: `grouping()`, `groupBy()`.
        For details about Monitoring Query Language (MQL), see `Monitoring Query Language (MQL) Reference`__.
        For available dimensions, review the metric definition for the supported service.
        See `Supported Services`__.

        Example of threshold alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

          -----

        Example of absence alarm:

          -----

            CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

          -----

        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices


        :param query: The query of this AlarmSummary.
        :type: str
        """
        self._query = query

    @property
    def severity(self):
        """
        **[Required]** Gets the severity of this AlarmSummary.
        The perceived severity of the alarm with regard to the affected system.

        Example: `CRITICAL`

        Allowed values for this property are: "CRITICAL", "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this AlarmSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this AlarmSummary.
        The perceived severity of the alarm with regard to the affected system.

        Example: `CRITICAL`


        :param severity: The severity of this AlarmSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "ERROR", "WARNING", "INFO"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def destinations(self):
        """
        **[Required]** Gets the destinations of this AlarmSummary.
        A list of destinations to which the notifications for this alarm will be delivered.
        Each destination is represented by an `OCID`__ related to the supported destination service.
        For example, a destination using the Notifications service is represented by a topic OCID.
        Supported destination services: Notifications Service. Limit: One destination per supported destination service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The destinations of this AlarmSummary.
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this AlarmSummary.
        A list of destinations to which the notifications for this alarm will be delivered.
        Each destination is represented by an `OCID`__ related to the supported destination service.
        For example, a destination using the Notifications service is represented by a topic OCID.
        Supported destination services: Notifications Service. Limit: One destination per supported destination service.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param destinations: The destinations of this AlarmSummary.
        :type: list[str]
        """
        self._destinations = destinations

    @property
    def suppression(self):
        """
        Gets the suppression of this AlarmSummary.
        The configuration details for suppressing an alarm.


        :return: The suppression of this AlarmSummary.
        :rtype: oci.monitoring.models.Suppression
        """
        return self._suppression

    @suppression.setter
    def suppression(self, suppression):
        """
        Sets the suppression of this AlarmSummary.
        The configuration details for suppressing an alarm.


        :param suppression: The suppression of this AlarmSummary.
        :type: oci.monitoring.models.Suppression
        """
        self._suppression = suppression

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this AlarmSummary.
        Whether the alarm is enabled.

        Example: `true`


        :return: The is_enabled of this AlarmSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AlarmSummary.
        Whether the alarm is enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this AlarmSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AlarmSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this AlarmSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AlarmSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this AlarmSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AlarmSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this AlarmSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AlarmSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this AlarmSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AlarmSummary.
        The current lifecycle state of the alarm.

        Example: `DELETED`


        :return: The lifecycle_state of this AlarmSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AlarmSummary.
        The current lifecycle state of the alarm.

        Example: `DELETED`


        :param lifecycle_state: The lifecycle_state of this AlarmSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
