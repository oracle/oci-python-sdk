# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicaOverrides(object):
    """
    By default a read replica inherits the MySQL version, shape, and configuration of the source DB system.
    If you want to override any of these, provide values in the properties, mysqlVersion, shapeName,
    and configurationId. If you set a property value to \"\", then the value is inherited from its
    source DB system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicaOverrides object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mysql_version:
            The value to assign to the mysql_version property of this ReplicaOverrides.
        :type mysql_version: str

        :param shape_name:
            The value to assign to the shape_name property of this ReplicaOverrides.
        :type shape_name: str

        :param configuration_id:
            The value to assign to the configuration_id property of this ReplicaOverrides.
        :type configuration_id: str

        """
        self.swagger_types = {
            'mysql_version': 'str',
            'shape_name': 'str',
            'configuration_id': 'str'
        }

        self.attribute_map = {
            'mysql_version': 'mysqlVersion',
            'shape_name': 'shapeName',
            'configuration_id': 'configurationId'
        }

        self._mysql_version = None
        self._shape_name = None
        self._configuration_id = None

    @property
    def mysql_version(self):
        """
        Gets the mysql_version of this ReplicaOverrides.
        The MySQL version to be used by the read replica.


        :return: The mysql_version of this ReplicaOverrides.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this ReplicaOverrides.
        The MySQL version to be used by the read replica.


        :param mysql_version: The mysql_version of this ReplicaOverrides.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def shape_name(self):
        """
        Gets the shape_name of this ReplicaOverrides.
        The shape to be used by the read replica. The shape determines the resources allocated:
        CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes.
        To get a list of shapes, use the :func:`list_shapes` operation.


        :return: The shape_name of this ReplicaOverrides.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this ReplicaOverrides.
        The shape to be used by the read replica. The shape determines the resources allocated:
        CPU cores and memory for VM shapes, CPU cores, memory and storage for non-VM (bare metal) shapes.
        To get a list of shapes, use the :func:`list_shapes` operation.


        :param shape_name: The shape_name of this ReplicaOverrides.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def configuration_id(self):
        """
        Gets the configuration_id of this ReplicaOverrides.
        The OCID of the Configuration to be used by the read replica.


        :return: The configuration_id of this ReplicaOverrides.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """
        Sets the configuration_id of this ReplicaOverrides.
        The OCID of the Configuration to be used by the read replica.


        :param configuration_id: The configuration_id of this ReplicaOverrides.
        :type: str
        """
        self._configuration_id = configuration_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
