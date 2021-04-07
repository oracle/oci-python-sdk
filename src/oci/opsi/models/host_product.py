# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostProduct(HostConfigurationMetricGroup):
    """
    Product metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostProduct object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostProduct.metric_name` attribute
        of this class is ``HOST_PRODUCT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostProduct.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostProduct.
        :type time_collected: datetime

        :param vendor:
            The value to assign to the vendor property of this HostProduct.
        :type vendor: str

        :param name:
            The value to assign to the name property of this HostProduct.
        :type name: str

        :param version:
            The value to assign to the version property of this HostProduct.
        :type version: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'vendor': 'str',
            'name': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'vendor': 'vendor',
            'name': 'name',
            'version': 'version'
        }

        self._metric_name = None
        self._time_collected = None
        self._vendor = None
        self._name = None
        self._version = None
        self._metric_name = 'HOST_PRODUCT'

    @property
    def vendor(self):
        """
        Gets the vendor of this HostProduct.
        Vendor of the product


        :return: The vendor of this HostProduct.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this HostProduct.
        Vendor of the product


        :param vendor: The vendor of this HostProduct.
        :type: str
        """
        self._vendor = vendor

    @property
    def name(self):
        """
        Gets the name of this HostProduct.
        Name of the product


        :return: The name of this HostProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HostProduct.
        Name of the product


        :param name: The name of this HostProduct.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this HostProduct.
        Version of the product


        :return: The version of this HostProduct.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this HostProduct.
        Version of the product


        :param version: The version of this HostProduct.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
