# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerVersion(object):
    """
    Container version metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param created_by:
            The value to assign to the created_by property of this ContainerVersion.
        :type created_by: str

        :param time_created:
            The value to assign to the time_created property of this ContainerVersion.
        :type time_created: datetime

        :param version:
            The value to assign to the version property of this ContainerVersion.
        :type version: str

        """
        self.swagger_types = {
            'created_by': 'str',
            'time_created': 'datetime',
            'version': 'str'
        }

        self.attribute_map = {
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'version': 'version'
        }

        self._created_by = None
        self._time_created = None
        self._version = None

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this ContainerVersion.
        The OCID of the user or principal that pushed the version.


        :return: The created_by of this ContainerVersion.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this ContainerVersion.
        The OCID of the user or principal that pushed the version.


        :param created_by: The created_by of this ContainerVersion.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerVersion.
        The creation time of the version.


        :return: The time_created of this ContainerVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerVersion.
        The creation time of the version.


        :param time_created: The time_created of this ContainerVersion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ContainerVersion.
        The version name.


        :return: The version of this ContainerVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ContainerVersion.
        The version name.


        :param version: The version of this ContainerVersion.
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
