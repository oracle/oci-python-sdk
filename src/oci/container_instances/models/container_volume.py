# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerVolume(object):
    """
    A Volume represents a directory with data that is accessible across multiple containers in a
    ContainerInstance.
    """

    #: A constant which can be used with the volume_type property of a ContainerVolume.
    #: This constant has a value of "EMPTYDIR"
    VOLUME_TYPE_EMPTYDIR = "EMPTYDIR"

    #: A constant which can be used with the volume_type property of a ContainerVolume.
    #: This constant has a value of "CONFIGFILE"
    VOLUME_TYPE_CONFIGFILE = "CONFIGFILE"

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerVolume object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.container_instances.models.ContainerEmptyDirVolume`
        * :class:`~oci.container_instances.models.ContainerConfigFileVolume`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ContainerVolume.
        :type name: str

        :param volume_type:
            The value to assign to the volume_type property of this ContainerVolume.
            Allowed values for this property are: "EMPTYDIR", "CONFIGFILE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type volume_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'volume_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'volume_type': 'volumeType'
        }

        self._name = None
        self._volume_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['volumeType']

        if type == 'EMPTYDIR':
            return 'ContainerEmptyDirVolume'

        if type == 'CONFIGFILE':
            return 'ContainerConfigFileVolume'
        else:
            return 'ContainerVolume'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ContainerVolume.
        The name of the volume. This has be unique cross single ContainerInstance.


        :return: The name of this ContainerVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContainerVolume.
        The name of the volume. This has be unique cross single ContainerInstance.


        :param name: The name of this ContainerVolume.
        :type: str
        """
        self._name = name

    @property
    def volume_type(self):
        """
        **[Required]** Gets the volume_type of this ContainerVolume.
        The type of volume.

        Allowed values for this property are: "EMPTYDIR", "CONFIGFILE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The volume_type of this ContainerVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """
        Sets the volume_type of this ContainerVolume.
        The type of volume.


        :param volume_type: The volume_type of this ContainerVolume.
        :type: str
        """
        allowed_values = ["EMPTYDIR", "CONFIGFILE"]
        if not value_allowed_none_or_none_sentinel(volume_type, allowed_values):
            volume_type = 'UNKNOWN_ENUM_VALUE'
        self._volume_type = volume_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
