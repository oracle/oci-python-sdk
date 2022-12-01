# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_container_volume_details import CreateContainerVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerConfigFileVolumeDetails(CreateContainerVolumeDetails):
    """
    The configuration files to pass to the container using volume mounts.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerConfigFileVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.CreateContainerConfigFileVolumeDetails.volume_type` attribute
        of this class is ``CONFIGFILE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateContainerConfigFileVolumeDetails.
        :type name: str

        :param volume_type:
            The value to assign to the volume_type property of this CreateContainerConfigFileVolumeDetails.
            Allowed values for this property are: "EMPTYDIR", "CONFIGFILE"
        :type volume_type: str

        :param configs:
            The value to assign to the configs property of this CreateContainerConfigFileVolumeDetails.
        :type configs: list[oci.container_instances.models.ContainerConfigFile]

        """
        self.swagger_types = {
            'name': 'str',
            'volume_type': 'str',
            'configs': 'list[ContainerConfigFile]'
        }

        self.attribute_map = {
            'name': 'name',
            'volume_type': 'volumeType',
            'configs': 'configs'
        }

        self._name = None
        self._volume_type = None
        self._configs = None
        self._volume_type = 'CONFIGFILE'

    @property
    def configs(self):
        """
        Gets the configs of this CreateContainerConfigFileVolumeDetails.
        Contains key value pairs which can be mounted as individual files inside the container. The value needs to be base64 encoded. It is decoded to plain text before the mount.


        :return: The configs of this CreateContainerConfigFileVolumeDetails.
        :rtype: list[oci.container_instances.models.ContainerConfigFile]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """
        Sets the configs of this CreateContainerConfigFileVolumeDetails.
        Contains key value pairs which can be mounted as individual files inside the container. The value needs to be base64 encoded. It is decoded to plain text before the mount.


        :param configs: The configs of this CreateContainerConfigFileVolumeDetails.
        :type: list[oci.container_instances.models.ContainerConfigFile]
        """
        self._configs = configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
