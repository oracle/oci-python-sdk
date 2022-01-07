# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafTrafficDatum(object):
    """
    A time series of traffic data for the  Web Application Firewall configured for a policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafTrafficDatum object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_observed:
            The value to assign to the time_observed property of this WafTrafficDatum.
        :type time_observed: datetime

        :param time_range_in_seconds:
            The value to assign to the time_range_in_seconds property of this WafTrafficDatum.
        :type time_range_in_seconds: int

        :param tenancy_id:
            The value to assign to the tenancy_id property of this WafTrafficDatum.
        :type tenancy_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WafTrafficDatum.
        :type compartment_id: str

        :param waas_policy_id:
            The value to assign to the waas_policy_id property of this WafTrafficDatum.
        :type waas_policy_id: str

        :param traffic_in_bytes:
            The value to assign to the traffic_in_bytes property of this WafTrafficDatum.
        :type traffic_in_bytes: int

        """
        self.swagger_types = {
            'time_observed': 'datetime',
            'time_range_in_seconds': 'int',
            'tenancy_id': 'str',
            'compartment_id': 'str',
            'waas_policy_id': 'str',
            'traffic_in_bytes': 'int'
        }

        self.attribute_map = {
            'time_observed': 'timeObserved',
            'time_range_in_seconds': 'timeRangeInSeconds',
            'tenancy_id': 'tenancyId',
            'compartment_id': 'compartmentId',
            'waas_policy_id': 'waasPolicyId',
            'traffic_in_bytes': 'trafficInBytes'
        }

        self._time_observed = None
        self._time_range_in_seconds = None
        self._tenancy_id = None
        self._compartment_id = None
        self._waas_policy_id = None
        self._traffic_in_bytes = None

    @property
    def time_observed(self):
        """
        Gets the time_observed of this WafTrafficDatum.
        The date and time the traffic was observed, rounded down to the start of the range, and expressed in RFC 3339 timestamp format.


        :return: The time_observed of this WafTrafficDatum.
        :rtype: datetime
        """
        return self._time_observed

    @time_observed.setter
    def time_observed(self, time_observed):
        """
        Sets the time_observed of this WafTrafficDatum.
        The date and time the traffic was observed, rounded down to the start of the range, and expressed in RFC 3339 timestamp format.


        :param time_observed: The time_observed of this WafTrafficDatum.
        :type: datetime
        """
        self._time_observed = time_observed

    @property
    def time_range_in_seconds(self):
        """
        Gets the time_range_in_seconds of this WafTrafficDatum.
        The number of seconds this data covers.


        :return: The time_range_in_seconds of this WafTrafficDatum.
        :rtype: int
        """
        return self._time_range_in_seconds

    @time_range_in_seconds.setter
    def time_range_in_seconds(self, time_range_in_seconds):
        """
        Sets the time_range_in_seconds of this WafTrafficDatum.
        The number of seconds this data covers.


        :param time_range_in_seconds: The time_range_in_seconds of this WafTrafficDatum.
        :type: int
        """
        self._time_range_in_seconds = time_range_in_seconds

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this WafTrafficDatum.
        The tenancy OCID of the data.


        :return: The tenancy_id of this WafTrafficDatum.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this WafTrafficDatum.
        The tenancy OCID of the data.


        :param tenancy_id: The tenancy_id of this WafTrafficDatum.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WafTrafficDatum.
        The compartment OCID of the data.


        :return: The compartment_id of this WafTrafficDatum.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WafTrafficDatum.
        The compartment OCID of the data.


        :param compartment_id: The compartment_id of this WafTrafficDatum.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def waas_policy_id(self):
        """
        Gets the waas_policy_id of this WafTrafficDatum.
        The policy OCID of the data.


        :return: The waas_policy_id of this WafTrafficDatum.
        :rtype: str
        """
        return self._waas_policy_id

    @waas_policy_id.setter
    def waas_policy_id(self, waas_policy_id):
        """
        Sets the waas_policy_id of this WafTrafficDatum.
        The policy OCID of the data.


        :param waas_policy_id: The waas_policy_id of this WafTrafficDatum.
        :type: str
        """
        self._waas_policy_id = waas_policy_id

    @property
    def traffic_in_bytes(self):
        """
        Gets the traffic_in_bytes of this WafTrafficDatum.
        Traffic in bytes.


        :return: The traffic_in_bytes of this WafTrafficDatum.
        :rtype: int
        """
        return self._traffic_in_bytes

    @traffic_in_bytes.setter
    def traffic_in_bytes(self, traffic_in_bytes):
        """
        Sets the traffic_in_bytes of this WafTrafficDatum.
        Traffic in bytes.


        :param traffic_in_bytes: The traffic_in_bytes of this WafTrafficDatum.
        :type: int
        """
        self._traffic_in_bytes = traffic_in_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
