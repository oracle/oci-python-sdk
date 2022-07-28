# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResizeOpensearchClusterVerticalDetails(object):
    """
    The OCPU and memory configuration to update on an existing OpenSearch cluster for `vertical resizing`__.

    __ https://docs.cloud.oracle.com/iaas/Content/search-opensearch/Tasks/resizingacluster.htm#vertical
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResizeOpensearchClusterVerticalDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param master_node_host_ocpu_count:
            The value to assign to the master_node_host_ocpu_count property of this ResizeOpensearchClusterVerticalDetails.
        :type master_node_host_ocpu_count: int

        :param master_node_host_memory_gb:
            The value to assign to the master_node_host_memory_gb property of this ResizeOpensearchClusterVerticalDetails.
        :type master_node_host_memory_gb: int

        :param data_node_host_ocpu_count:
            The value to assign to the data_node_host_ocpu_count property of this ResizeOpensearchClusterVerticalDetails.
        :type data_node_host_ocpu_count: int

        :param data_node_host_memory_gb:
            The value to assign to the data_node_host_memory_gb property of this ResizeOpensearchClusterVerticalDetails.
        :type data_node_host_memory_gb: int

        :param data_node_storage_gb:
            The value to assign to the data_node_storage_gb property of this ResizeOpensearchClusterVerticalDetails.
        :type data_node_storage_gb: int

        :param opendashboard_node_host_ocpu_count:
            The value to assign to the opendashboard_node_host_ocpu_count property of this ResizeOpensearchClusterVerticalDetails.
        :type opendashboard_node_host_ocpu_count: int

        :param opendashboard_node_host_memory_gb:
            The value to assign to the opendashboard_node_host_memory_gb property of this ResizeOpensearchClusterVerticalDetails.
        :type opendashboard_node_host_memory_gb: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ResizeOpensearchClusterVerticalDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ResizeOpensearchClusterVerticalDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'master_node_host_ocpu_count': 'int',
            'master_node_host_memory_gb': 'int',
            'data_node_host_ocpu_count': 'int',
            'data_node_host_memory_gb': 'int',
            'data_node_storage_gb': 'int',
            'opendashboard_node_host_ocpu_count': 'int',
            'opendashboard_node_host_memory_gb': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'master_node_host_ocpu_count': 'masterNodeHostOcpuCount',
            'master_node_host_memory_gb': 'masterNodeHostMemoryGB',
            'data_node_host_ocpu_count': 'dataNodeHostOcpuCount',
            'data_node_host_memory_gb': 'dataNodeHostMemoryGB',
            'data_node_storage_gb': 'dataNodeStorageGB',
            'opendashboard_node_host_ocpu_count': 'opendashboardNodeHostOcpuCount',
            'opendashboard_node_host_memory_gb': 'opendashboardNodeHostMemoryGB',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._master_node_host_ocpu_count = None
        self._master_node_host_memory_gb = None
        self._data_node_host_ocpu_count = None
        self._data_node_host_memory_gb = None
        self._data_node_storage_gb = None
        self._opendashboard_node_host_ocpu_count = None
        self._opendashboard_node_host_memory_gb = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def master_node_host_ocpu_count(self):
        """
        Gets the master_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        The number of OCPUs to configure for the cluster's master nodes.


        :return: The master_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._master_node_host_ocpu_count

    @master_node_host_ocpu_count.setter
    def master_node_host_ocpu_count(self, master_node_host_ocpu_count):
        """
        Sets the master_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        The number of OCPUs to configure for the cluster's master nodes.


        :param master_node_host_ocpu_count: The master_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._master_node_host_ocpu_count = master_node_host_ocpu_count

    @property
    def master_node_host_memory_gb(self):
        """
        Gets the master_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of memory in GB, to configure for the cluster's master nodes.


        :return: The master_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._master_node_host_memory_gb

    @master_node_host_memory_gb.setter
    def master_node_host_memory_gb(self, master_node_host_memory_gb):
        """
        Sets the master_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of memory in GB, to configure for the cluster's master nodes.


        :param master_node_host_memory_gb: The master_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._master_node_host_memory_gb = master_node_host_memory_gb

    @property
    def data_node_host_ocpu_count(self):
        """
        Gets the data_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        The number of OCPUs to configure for the cluster's data nodes.


        :return: The data_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._data_node_host_ocpu_count

    @data_node_host_ocpu_count.setter
    def data_node_host_ocpu_count(self, data_node_host_ocpu_count):
        """
        Sets the data_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        The number of OCPUs to configure for the cluster's data nodes.


        :param data_node_host_ocpu_count: The data_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._data_node_host_ocpu_count = data_node_host_ocpu_count

    @property
    def data_node_host_memory_gb(self):
        """
        Gets the data_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of memory in GB, to configure for the cluster's data nodes.


        :return: The data_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._data_node_host_memory_gb

    @data_node_host_memory_gb.setter
    def data_node_host_memory_gb(self, data_node_host_memory_gb):
        """
        Sets the data_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of memory in GB, to configure for the cluster's data nodes.


        :param data_node_host_memory_gb: The data_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._data_node_host_memory_gb = data_node_host_memory_gb

    @property
    def data_node_storage_gb(self):
        """
        Gets the data_node_storage_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of storage in GB, to configure per node for the cluster's data nodes.


        :return: The data_node_storage_gb of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._data_node_storage_gb

    @data_node_storage_gb.setter
    def data_node_storage_gb(self, data_node_storage_gb):
        """
        Sets the data_node_storage_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of storage in GB, to configure per node for the cluster's data nodes.


        :param data_node_storage_gb: The data_node_storage_gb of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._data_node_storage_gb = data_node_storage_gb

    @property
    def opendashboard_node_host_ocpu_count(self):
        """
        Gets the opendashboard_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.


        :return: The opendashboard_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._opendashboard_node_host_ocpu_count

    @opendashboard_node_host_ocpu_count.setter
    def opendashboard_node_host_ocpu_count(self, opendashboard_node_host_ocpu_count):
        """
        Sets the opendashboard_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.


        :param opendashboard_node_host_ocpu_count: The opendashboard_node_host_ocpu_count of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._opendashboard_node_host_ocpu_count = opendashboard_node_host_ocpu_count

    @property
    def opendashboard_node_host_memory_gb(self):
        """
        Gets the opendashboard_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.


        :return: The opendashboard_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        :rtype: int
        """
        return self._opendashboard_node_host_memory_gb

    @opendashboard_node_host_memory_gb.setter
    def opendashboard_node_host_memory_gb(self, opendashboard_node_host_memory_gb):
        """
        Sets the opendashboard_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.


        :param opendashboard_node_host_memory_gb: The opendashboard_node_host_memory_gb of this ResizeOpensearchClusterVerticalDetails.
        :type: int
        """
        self._opendashboard_node_host_memory_gb = opendashboard_node_host_memory_gb

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ResizeOpensearchClusterVerticalDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ResizeOpensearchClusterVerticalDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResizeOpensearchClusterVerticalDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ResizeOpensearchClusterVerticalDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ResizeOpensearchClusterVerticalDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ResizeOpensearchClusterVerticalDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResizeOpensearchClusterVerticalDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ResizeOpensearchClusterVerticalDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
