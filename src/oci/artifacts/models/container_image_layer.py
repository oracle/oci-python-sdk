# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerImageLayer(object):
    """
    The container image layer metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerImageLayer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param digest:
            The value to assign to the digest property of this ContainerImageLayer.
        :type digest: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this ContainerImageLayer.
        :type size_in_bytes: int

        :param time_created:
            The value to assign to the time_created property of this ContainerImageLayer.
        :type time_created: datetime

        """
        self.swagger_types = {
            'digest': 'str',
            'size_in_bytes': 'int',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'digest': 'digest',
            'size_in_bytes': 'sizeInBytes',
            'time_created': 'timeCreated'
        }

        self._digest = None
        self._size_in_bytes = None
        self._time_created = None

    @property
    def digest(self):
        """
        **[Required]** Gets the digest of this ContainerImageLayer.
        The sha256 digest of the image layer.


        :return: The digest of this ContainerImageLayer.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """
        Sets the digest of this ContainerImageLayer.
        The sha256 digest of the image layer.


        :param digest: The digest of this ContainerImageLayer.
        :type: str
        """
        self._digest = digest

    @property
    def size_in_bytes(self):
        """
        **[Required]** Gets the size_in_bytes of this ContainerImageLayer.
        The size of the layer in bytes.


        :return: The size_in_bytes of this ContainerImageLayer.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this ContainerImageLayer.
        The size of the layer in bytes.


        :param size_in_bytes: The size_in_bytes of this ContainerImageLayer.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerImageLayer.
        An RFC 3339 timestamp indicating when the layer was created.


        :return: The time_created of this ContainerImageLayer.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerImageLayer.
        An RFC 3339 timestamp indicating when the layer was created.


        :param time_created: The time_created of this ContainerImageLayer.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
