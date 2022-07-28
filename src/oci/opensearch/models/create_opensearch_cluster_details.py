# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOpensearchClusterDetails(object):
    """
    The configuration details for a new OpenSearch cluster.
    """

    #: A constant which can be used with the master_node_host_type property of a CreateOpensearchClusterDetails.
    #: This constant has a value of "FLEX"
    MASTER_NODE_HOST_TYPE_FLEX = "FLEX"

    #: A constant which can be used with the master_node_host_type property of a CreateOpensearchClusterDetails.
    #: This constant has a value of "BM"
    MASTER_NODE_HOST_TYPE_BM = "BM"

    #: A constant which can be used with the data_node_host_type property of a CreateOpensearchClusterDetails.
    #: This constant has a value of "FLEX"
    DATA_NODE_HOST_TYPE_FLEX = "FLEX"

    #: A constant which can be used with the data_node_host_type property of a CreateOpensearchClusterDetails.
    #: This constant has a value of "BM"
    DATA_NODE_HOST_TYPE_BM = "BM"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOpensearchClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateOpensearchClusterDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOpensearchClusterDetails.
        :type compartment_id: str

        :param software_version:
            The value to assign to the software_version property of this CreateOpensearchClusterDetails.
        :type software_version: str

        :param master_node_count:
            The value to assign to the master_node_count property of this CreateOpensearchClusterDetails.
        :type master_node_count: int

        :param master_node_host_type:
            The value to assign to the master_node_host_type property of this CreateOpensearchClusterDetails.
            Allowed values for this property are: "FLEX", "BM"
        :type master_node_host_type: str

        :param master_node_host_bare_metal_shape:
            The value to assign to the master_node_host_bare_metal_shape property of this CreateOpensearchClusterDetails.
        :type master_node_host_bare_metal_shape: str

        :param master_node_host_ocpu_count:
            The value to assign to the master_node_host_ocpu_count property of this CreateOpensearchClusterDetails.
        :type master_node_host_ocpu_count: int

        :param master_node_host_memory_gb:
            The value to assign to the master_node_host_memory_gb property of this CreateOpensearchClusterDetails.
        :type master_node_host_memory_gb: int

        :param data_node_count:
            The value to assign to the data_node_count property of this CreateOpensearchClusterDetails.
        :type data_node_count: int

        :param data_node_host_type:
            The value to assign to the data_node_host_type property of this CreateOpensearchClusterDetails.
            Allowed values for this property are: "FLEX", "BM"
        :type data_node_host_type: str

        :param data_node_host_bare_metal_shape:
            The value to assign to the data_node_host_bare_metal_shape property of this CreateOpensearchClusterDetails.
        :type data_node_host_bare_metal_shape: str

        :param data_node_host_ocpu_count:
            The value to assign to the data_node_host_ocpu_count property of this CreateOpensearchClusterDetails.
        :type data_node_host_ocpu_count: int

        :param data_node_host_memory_gb:
            The value to assign to the data_node_host_memory_gb property of this CreateOpensearchClusterDetails.
        :type data_node_host_memory_gb: int

        :param data_node_storage_gb:
            The value to assign to the data_node_storage_gb property of this CreateOpensearchClusterDetails.
        :type data_node_storage_gb: int

        :param opendashboard_node_count:
            The value to assign to the opendashboard_node_count property of this CreateOpensearchClusterDetails.
        :type opendashboard_node_count: int

        :param opendashboard_node_host_ocpu_count:
            The value to assign to the opendashboard_node_host_ocpu_count property of this CreateOpensearchClusterDetails.
        :type opendashboard_node_host_ocpu_count: int

        :param opendashboard_node_host_memory_gb:
            The value to assign to the opendashboard_node_host_memory_gb property of this CreateOpensearchClusterDetails.
        :type opendashboard_node_host_memory_gb: int

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateOpensearchClusterDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateOpensearchClusterDetails.
        :type subnet_id: str

        :param vcn_compartment_id:
            The value to assign to the vcn_compartment_id property of this CreateOpensearchClusterDetails.
        :type vcn_compartment_id: str

        :param subnet_compartment_id:
            The value to assign to the subnet_compartment_id property of this CreateOpensearchClusterDetails.
        :type subnet_compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOpensearchClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOpensearchClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateOpensearchClusterDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'software_version': 'str',
            'master_node_count': 'int',
            'master_node_host_type': 'str',
            'master_node_host_bare_metal_shape': 'str',
            'master_node_host_ocpu_count': 'int',
            'master_node_host_memory_gb': 'int',
            'data_node_count': 'int',
            'data_node_host_type': 'str',
            'data_node_host_bare_metal_shape': 'str',
            'data_node_host_ocpu_count': 'int',
            'data_node_host_memory_gb': 'int',
            'data_node_storage_gb': 'int',
            'opendashboard_node_count': 'int',
            'opendashboard_node_host_ocpu_count': 'int',
            'opendashboard_node_host_memory_gb': 'int',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'vcn_compartment_id': 'str',
            'subnet_compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'software_version': 'softwareVersion',
            'master_node_count': 'masterNodeCount',
            'master_node_host_type': 'masterNodeHostType',
            'master_node_host_bare_metal_shape': 'masterNodeHostBareMetalShape',
            'master_node_host_ocpu_count': 'masterNodeHostOcpuCount',
            'master_node_host_memory_gb': 'masterNodeHostMemoryGB',
            'data_node_count': 'dataNodeCount',
            'data_node_host_type': 'dataNodeHostType',
            'data_node_host_bare_metal_shape': 'dataNodeHostBareMetalShape',
            'data_node_host_ocpu_count': 'dataNodeHostOcpuCount',
            'data_node_host_memory_gb': 'dataNodeHostMemoryGB',
            'data_node_storage_gb': 'dataNodeStorageGB',
            'opendashboard_node_count': 'opendashboardNodeCount',
            'opendashboard_node_host_ocpu_count': 'opendashboardNodeHostOcpuCount',
            'opendashboard_node_host_memory_gb': 'opendashboardNodeHostMemoryGB',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'vcn_compartment_id': 'vcnCompartmentId',
            'subnet_compartment_id': 'subnetCompartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._software_version = None
        self._master_node_count = None
        self._master_node_host_type = None
        self._master_node_host_bare_metal_shape = None
        self._master_node_host_ocpu_count = None
        self._master_node_host_memory_gb = None
        self._data_node_count = None
        self._data_node_host_type = None
        self._data_node_host_bare_metal_shape = None
        self._data_node_host_ocpu_count = None
        self._data_node_host_memory_gb = None
        self._data_node_storage_gb = None
        self._opendashboard_node_count = None
        self._opendashboard_node_host_ocpu_count = None
        self._opendashboard_node_host_memory_gb = None
        self._vcn_id = None
        self._subnet_id = None
        self._vcn_compartment_id = None
        self._subnet_compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateOpensearchClusterDetails.
        The name of the cluster. Avoid entering confidential information.


        :return: The display_name of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateOpensearchClusterDetails.
        The name of the cluster. Avoid entering confidential information.


        :param display_name: The display_name of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOpensearchClusterDetails.
        The OCID of the compartment to create the cluster in.


        :return: The compartment_id of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOpensearchClusterDetails.
        The OCID of the compartment to create the cluster in.


        :param compartment_id: The compartment_id of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def software_version(self):
        """
        **[Required]** Gets the software_version of this CreateOpensearchClusterDetails.
        The version of the software the cluster is running.


        :return: The software_version of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """
        Sets the software_version of this CreateOpensearchClusterDetails.
        The version of the software the cluster is running.


        :param software_version: The software_version of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._software_version = software_version

    @property
    def master_node_count(self):
        """
        **[Required]** Gets the master_node_count of this CreateOpensearchClusterDetails.
        The number of master nodes to configure for the cluster.


        :return: The master_node_count of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._master_node_count

    @master_node_count.setter
    def master_node_count(self, master_node_count):
        """
        Sets the master_node_count of this CreateOpensearchClusterDetails.
        The number of master nodes to configure for the cluster.


        :param master_node_count: The master_node_count of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._master_node_count = master_node_count

    @property
    def master_node_host_type(self):
        """
        **[Required]** Gets the master_node_host_type of this CreateOpensearchClusterDetails.
        The instance type for the cluster's master nodes.

        Allowed values for this property are: "FLEX", "BM"


        :return: The master_node_host_type of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._master_node_host_type

    @master_node_host_type.setter
    def master_node_host_type(self, master_node_host_type):
        """
        Sets the master_node_host_type of this CreateOpensearchClusterDetails.
        The instance type for the cluster's master nodes.


        :param master_node_host_type: The master_node_host_type of this CreateOpensearchClusterDetails.
        :type: str
        """
        allowed_values = ["FLEX", "BM"]
        if not value_allowed_none_or_none_sentinel(master_node_host_type, allowed_values):
            raise ValueError(
                "Invalid value for `master_node_host_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._master_node_host_type = master_node_host_type

    @property
    def master_node_host_bare_metal_shape(self):
        """
        Gets the master_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        The bare metal shape for the cluster's master nodes.


        :return: The master_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._master_node_host_bare_metal_shape

    @master_node_host_bare_metal_shape.setter
    def master_node_host_bare_metal_shape(self, master_node_host_bare_metal_shape):
        """
        Sets the master_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        The bare metal shape for the cluster's master nodes.


        :param master_node_host_bare_metal_shape: The master_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._master_node_host_bare_metal_shape = master_node_host_bare_metal_shape

    @property
    def master_node_host_ocpu_count(self):
        """
        **[Required]** Gets the master_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        The number of OCPUs to configure for the cluser's master nodes.


        :return: The master_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._master_node_host_ocpu_count

    @master_node_host_ocpu_count.setter
    def master_node_host_ocpu_count(self, master_node_host_ocpu_count):
        """
        Sets the master_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        The number of OCPUs to configure for the cluser's master nodes.


        :param master_node_host_ocpu_count: The master_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._master_node_host_ocpu_count = master_node_host_ocpu_count

    @property
    def master_node_host_memory_gb(self):
        """
        **[Required]** Gets the master_node_host_memory_gb of this CreateOpensearchClusterDetails.
        The amount of memory in GB, to configure per node for the cluster's master nodes.


        :return: The master_node_host_memory_gb of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._master_node_host_memory_gb

    @master_node_host_memory_gb.setter
    def master_node_host_memory_gb(self, master_node_host_memory_gb):
        """
        Sets the master_node_host_memory_gb of this CreateOpensearchClusterDetails.
        The amount of memory in GB, to configure per node for the cluster's master nodes.


        :param master_node_host_memory_gb: The master_node_host_memory_gb of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._master_node_host_memory_gb = master_node_host_memory_gb

    @property
    def data_node_count(self):
        """
        **[Required]** Gets the data_node_count of this CreateOpensearchClusterDetails.
        The number of data nodes to configure for the cluster.


        :return: The data_node_count of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._data_node_count

    @data_node_count.setter
    def data_node_count(self, data_node_count):
        """
        Sets the data_node_count of this CreateOpensearchClusterDetails.
        The number of data nodes to configure for the cluster.


        :param data_node_count: The data_node_count of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._data_node_count = data_node_count

    @property
    def data_node_host_type(self):
        """
        **[Required]** Gets the data_node_host_type of this CreateOpensearchClusterDetails.
        TThe instance type for the cluster's data nodes.

        Allowed values for this property are: "FLEX", "BM"


        :return: The data_node_host_type of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._data_node_host_type

    @data_node_host_type.setter
    def data_node_host_type(self, data_node_host_type):
        """
        Sets the data_node_host_type of this CreateOpensearchClusterDetails.
        TThe instance type for the cluster's data nodes.


        :param data_node_host_type: The data_node_host_type of this CreateOpensearchClusterDetails.
        :type: str
        """
        allowed_values = ["FLEX", "BM"]
        if not value_allowed_none_or_none_sentinel(data_node_host_type, allowed_values):
            raise ValueError(
                "Invalid value for `data_node_host_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._data_node_host_type = data_node_host_type

    @property
    def data_node_host_bare_metal_shape(self):
        """
        Gets the data_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        The bare metal shape for the cluster's data nodes.


        :return: The data_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._data_node_host_bare_metal_shape

    @data_node_host_bare_metal_shape.setter
    def data_node_host_bare_metal_shape(self, data_node_host_bare_metal_shape):
        """
        Sets the data_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        The bare metal shape for the cluster's data nodes.


        :param data_node_host_bare_metal_shape: The data_node_host_bare_metal_shape of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._data_node_host_bare_metal_shape = data_node_host_bare_metal_shape

    @property
    def data_node_host_ocpu_count(self):
        """
        **[Required]** Gets the data_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        The number of OCPUs to configure for the cluster's data nodes.


        :return: The data_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._data_node_host_ocpu_count

    @data_node_host_ocpu_count.setter
    def data_node_host_ocpu_count(self, data_node_host_ocpu_count):
        """
        Sets the data_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        The number of OCPUs to configure for the cluster's data nodes.


        :param data_node_host_ocpu_count: The data_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._data_node_host_ocpu_count = data_node_host_ocpu_count

    @property
    def data_node_host_memory_gb(self):
        """
        **[Required]** Gets the data_node_host_memory_gb of this CreateOpensearchClusterDetails.
        The amount of memory in GB, to configure per node for the cluster's data nodes.


        :return: The data_node_host_memory_gb of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._data_node_host_memory_gb

    @data_node_host_memory_gb.setter
    def data_node_host_memory_gb(self, data_node_host_memory_gb):
        """
        Sets the data_node_host_memory_gb of this CreateOpensearchClusterDetails.
        The amount of memory in GB, to configure per node for the cluster's data nodes.


        :param data_node_host_memory_gb: The data_node_host_memory_gb of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._data_node_host_memory_gb = data_node_host_memory_gb

    @property
    def data_node_storage_gb(self):
        """
        **[Required]** Gets the data_node_storage_gb of this CreateOpensearchClusterDetails.
        The amount of storage in GB, to configure per node for the cluster's data nodes.


        :return: The data_node_storage_gb of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._data_node_storage_gb

    @data_node_storage_gb.setter
    def data_node_storage_gb(self, data_node_storage_gb):
        """
        Sets the data_node_storage_gb of this CreateOpensearchClusterDetails.
        The amount of storage in GB, to configure per node for the cluster's data nodes.


        :param data_node_storage_gb: The data_node_storage_gb of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._data_node_storage_gb = data_node_storage_gb

    @property
    def opendashboard_node_count(self):
        """
        **[Required]** Gets the opendashboard_node_count of this CreateOpensearchClusterDetails.
        The number of OpenSearch Dashboard nodes to configure for the cluster.


        :return: The opendashboard_node_count of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._opendashboard_node_count

    @opendashboard_node_count.setter
    def opendashboard_node_count(self, opendashboard_node_count):
        """
        Sets the opendashboard_node_count of this CreateOpensearchClusterDetails.
        The number of OpenSearch Dashboard nodes to configure for the cluster.


        :param opendashboard_node_count: The opendashboard_node_count of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._opendashboard_node_count = opendashboard_node_count

    @property
    def opendashboard_node_host_ocpu_count(self):
        """
        **[Required]** Gets the opendashboard_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.


        :return: The opendashboard_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._opendashboard_node_host_ocpu_count

    @opendashboard_node_host_ocpu_count.setter
    def opendashboard_node_host_ocpu_count(self, opendashboard_node_host_ocpu_count):
        """
        Sets the opendashboard_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        The number of OCPUs to configure for the cluster's OpenSearch Dashboard nodes.


        :param opendashboard_node_host_ocpu_count: The opendashboard_node_host_ocpu_count of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._opendashboard_node_host_ocpu_count = opendashboard_node_host_ocpu_count

    @property
    def opendashboard_node_host_memory_gb(self):
        """
        **[Required]** Gets the opendashboard_node_host_memory_gb of this CreateOpensearchClusterDetails.
        The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.


        :return: The opendashboard_node_host_memory_gb of this CreateOpensearchClusterDetails.
        :rtype: int
        """
        return self._opendashboard_node_host_memory_gb

    @opendashboard_node_host_memory_gb.setter
    def opendashboard_node_host_memory_gb(self, opendashboard_node_host_memory_gb):
        """
        Sets the opendashboard_node_host_memory_gb of this CreateOpensearchClusterDetails.
        The amount of memory in GB, to configure for the cluster's OpenSearch Dashboard nodes.


        :param opendashboard_node_host_memory_gb: The opendashboard_node_host_memory_gb of this CreateOpensearchClusterDetails.
        :type: int
        """
        self._opendashboard_node_host_memory_gb = opendashboard_node_host_memory_gb

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateOpensearchClusterDetails.
        The OCID of the cluster's VCN.


        :return: The vcn_id of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateOpensearchClusterDetails.
        The OCID of the cluster's VCN.


        :param vcn_id: The vcn_id of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateOpensearchClusterDetails.
        The OCID of the cluster's subnet.


        :return: The subnet_id of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateOpensearchClusterDetails.
        The OCID of the cluster's subnet.


        :param subnet_id: The subnet_id of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def vcn_compartment_id(self):
        """
        **[Required]** Gets the vcn_compartment_id of this CreateOpensearchClusterDetails.
        The OCID for the compartment where the cluster's VCN is located.


        :return: The vcn_compartment_id of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._vcn_compartment_id

    @vcn_compartment_id.setter
    def vcn_compartment_id(self, vcn_compartment_id):
        """
        Sets the vcn_compartment_id of this CreateOpensearchClusterDetails.
        The OCID for the compartment where the cluster's VCN is located.


        :param vcn_compartment_id: The vcn_compartment_id of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._vcn_compartment_id = vcn_compartment_id

    @property
    def subnet_compartment_id(self):
        """
        **[Required]** Gets the subnet_compartment_id of this CreateOpensearchClusterDetails.
        The OCID for the compartment where the cluster's subnet is located.


        :return: The subnet_compartment_id of this CreateOpensearchClusterDetails.
        :rtype: str
        """
        return self._subnet_compartment_id

    @subnet_compartment_id.setter
    def subnet_compartment_id(self, subnet_compartment_id):
        """
        Sets the subnet_compartment_id of this CreateOpensearchClusterDetails.
        The OCID for the compartment where the cluster's subnet is located.


        :param subnet_compartment_id: The subnet_compartment_id of this CreateOpensearchClusterDetails.
        :type: str
        """
        self._subnet_compartment_id = subnet_compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOpensearchClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOpensearchClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOpensearchClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOpensearchClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOpensearchClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOpensearchClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOpensearchClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOpensearchClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateOpensearchClusterDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreateOpensearchClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateOpensearchClusterDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreateOpensearchClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
