# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HcxLicenseSummary(object):
    """
    HCX on-premise license information summary.
    """

    #: A constant which can be used with the status property of a HcxLicenseSummary.
    #: This constant has a value of "AVAILABLE"
    STATUS_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the status property of a HcxLicenseSummary.
    #: This constant has a value of "CONSUMED"
    STATUS_CONSUMED = "CONSUMED"

    #: A constant which can be used with the status property of a HcxLicenseSummary.
    #: This constant has a value of "DEACTIVATED"
    STATUS_DEACTIVATED = "DEACTIVATED"

    #: A constant which can be used with the status property of a HcxLicenseSummary.
    #: This constant has a value of "DELETED"
    STATUS_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new HcxLicenseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param activation_key:
            The value to assign to the activation_key property of this HcxLicenseSummary.
        :type activation_key: str

        :param status:
            The value to assign to the status property of this HcxLicenseSummary.
            Allowed values for this property are: "AVAILABLE", "CONSUMED", "DEACTIVATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param system_name:
            The value to assign to the system_name property of this HcxLicenseSummary.
        :type system_name: str

        """
        self.swagger_types = {
            'activation_key': 'str',
            'status': 'str',
            'system_name': 'str'
        }

        self.attribute_map = {
            'activation_key': 'activationKey',
            'status': 'status',
            'system_name': 'systemName'
        }

        self._activation_key = None
        self._status = None
        self._system_name = None

    @property
    def activation_key(self):
        """
        **[Required]** Gets the activation_key of this HcxLicenseSummary.
        HCX on-premise license key value


        :return: The activation_key of this HcxLicenseSummary.
        :rtype: str
        """
        return self._activation_key

    @activation_key.setter
    def activation_key(self, activation_key):
        """
        Sets the activation_key of this HcxLicenseSummary.
        HCX on-premise license key value


        :param activation_key: The activation_key of this HcxLicenseSummary.
        :type: str
        """
        self._activation_key = activation_key

    @property
    def status(self):
        """
        **[Required]** Gets the status of this HcxLicenseSummary.
        status of HCX on-premise license

        Allowed values for this property are: "AVAILABLE", "CONSUMED", "DEACTIVATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this HcxLicenseSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HcxLicenseSummary.
        status of HCX on-premise license


        :param status: The status of this HcxLicenseSummary.
        :type: str
        """
        allowed_values = ["AVAILABLE", "CONSUMED", "DEACTIVATED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def system_name(self):
        """
        Gets the system_name of this HcxLicenseSummary.
        Name of the system that consumed the HCX on-premise license


        :return: The system_name of this HcxLicenseSummary.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """
        Sets the system_name of this HcxLicenseSummary.
        Name of the system that consumed the HCX on-premise license


        :param system_name: The system_name of this HcxLicenseSummary.
        :type: str
        """
        self._system_name = system_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
