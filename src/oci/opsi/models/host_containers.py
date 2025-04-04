# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostContainers(HostConfigurationMetricGroup):
    """
    Host Containers details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostContainers object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostContainers.metric_name` attribute
        of this class is ``HOST_CONTAINERS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostContainers.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES", "HOST_FILESYSTEM_CONFIGURATION", "HOST_GPU_CONFIGURATION", "HOST_CONTAINERS"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostContainers.
        :type time_collected: datetime

        :param container_id:
            The value to assign to the container_id property of this HostContainers.
        :type container_id: str

        :param container_name:
            The value to assign to the container_name property of this HostContainers.
        :type container_name: str

        :param container_image:
            The value to assign to the container_image property of this HostContainers.
        :type container_image: str

        :param container_image_tag:
            The value to assign to the container_image_tag property of this HostContainers.
        :type container_image_tag: str

        :param container_image_digest:
            The value to assign to the container_image_digest property of this HostContainers.
        :type container_image_digest: str

        :param container_ports:
            The value to assign to the container_ports property of this HostContainers.
        :type container_ports: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'container_id': 'str',
            'container_name': 'str',
            'container_image': 'str',
            'container_image_tag': 'str',
            'container_image_digest': 'str',
            'container_ports': 'str'
        }
        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'container_id': 'containerId',
            'container_name': 'containerName',
            'container_image': 'containerImage',
            'container_image_tag': 'containerImageTag',
            'container_image_digest': 'containerImageDigest',
            'container_ports': 'containerPorts'
        }
        self._metric_name = None
        self._time_collected = None
        self._container_id = None
        self._container_name = None
        self._container_image = None
        self._container_image_tag = None
        self._container_image_digest = None
        self._container_ports = None
        self._metric_name = 'HOST_CONTAINERS'

    @property
    def container_id(self):
        """
        Gets the container_id of this HostContainers.
        Container Id (full)


        :return: The container_id of this HostContainers.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this HostContainers.
        Container Id (full)


        :param container_id: The container_id of this HostContainers.
        :type: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        """
        Gets the container_name of this HostContainers.
        Container Name


        :return: The container_name of this HostContainers.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """
        Sets the container_name of this HostContainers.
        Container Name


        :param container_name: The container_name of this HostContainers.
        :type: str
        """
        self._container_name = container_name

    @property
    def container_image(self):
        """
        Gets the container_image of this HostContainers.
        Container Image


        :return: The container_image of this HostContainers.
        :rtype: str
        """
        return self._container_image

    @container_image.setter
    def container_image(self, container_image):
        """
        Sets the container_image of this HostContainers.
        Container Image


        :param container_image: The container_image of this HostContainers.
        :type: str
        """
        self._container_image = container_image

    @property
    def container_image_tag(self):
        """
        Gets the container_image_tag of this HostContainers.
        Container Image Tag (version)


        :return: The container_image_tag of this HostContainers.
        :rtype: str
        """
        return self._container_image_tag

    @container_image_tag.setter
    def container_image_tag(self, container_image_tag):
        """
        Sets the container_image_tag of this HostContainers.
        Container Image Tag (version)


        :param container_image_tag: The container_image_tag of this HostContainers.
        :type: str
        """
        self._container_image_tag = container_image_tag

    @property
    def container_image_digest(self):
        """
        Gets the container_image_digest of this HostContainers.
        Container Image Digest


        :return: The container_image_digest of this HostContainers.
        :rtype: str
        """
        return self._container_image_digest

    @container_image_digest.setter
    def container_image_digest(self, container_image_digest):
        """
        Sets the container_image_digest of this HostContainers.
        Container Image Digest


        :param container_image_digest: The container_image_digest of this HostContainers.
        :type: str
        """
        self._container_image_digest = container_image_digest

    @property
    def container_ports(self):
        """
        Gets the container_ports of this HostContainers.
        Container open ports


        :return: The container_ports of this HostContainers.
        :rtype: str
        """
        return self._container_ports

    @container_ports.setter
    def container_ports(self, container_ports):
        """
        Sets the container_ports of this HostContainers.
        Container open ports


        :param container_ports: The container_ports of this HostContainers.
        :type: str
        """
        self._container_ports = container_ports

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
