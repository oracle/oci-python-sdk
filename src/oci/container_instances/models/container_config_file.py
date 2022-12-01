# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerConfigFile(object):
    """
    The file that is mounted on a container instance through a volume mount.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerConfigFile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_name:
            The value to assign to the file_name property of this ContainerConfigFile.
        :type file_name: str

        :param data:
            The value to assign to the data property of this ContainerConfigFile.
        :type data: str

        :param path:
            The value to assign to the path property of this ContainerConfigFile.
        :type path: str

        """
        self.swagger_types = {
            'file_name': 'str',
            'data': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'file_name': 'fileName',
            'data': 'data',
            'path': 'path'
        }

        self._file_name = None
        self._data = None
        self._path = None

    @property
    def file_name(self):
        """
        **[Required]** Gets the file_name of this ContainerConfigFile.
        The name of the file. The fileName should be unique across the volume.


        :return: The file_name of this ContainerConfigFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this ContainerConfigFile.
        The name of the file. The fileName should be unique across the volume.


        :param file_name: The file_name of this ContainerConfigFile.
        :type: str
        """
        self._file_name = file_name

    @property
    def data(self):
        """
        **[Required]** Gets the data of this ContainerConfigFile.
        The base64 encoded contents of the file. The contents are decoded to plain text before mounted as a file to a container inside container instance.


        :return: The data of this ContainerConfigFile.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ContainerConfigFile.
        The base64 encoded contents of the file. The contents are decoded to plain text before mounted as a file to a container inside container instance.


        :param data: The data of this ContainerConfigFile.
        :type: str
        """
        self._data = data

    @property
    def path(self):
        """
        Gets the path of this ContainerConfigFile.
        (Optional) Relative path for this file inside the volume mount directory. By default, the file is presented at the root of the volume mount path.


        :return: The path of this ContainerConfigFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ContainerConfigFile.
        (Optional) Relative path for this file inside the volume mount directory. By default, the file is presented at the root of the volume mount path.


        :param path: The path of this ContainerConfigFile.
        :type: str
        """
        self._path = path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
