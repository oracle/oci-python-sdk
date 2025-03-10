# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOpensearchClusterPipelineDetails(object):
    """
    The configuration details for a new OpenSearch cluster pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOpensearchClusterPipelineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateOpensearchClusterPipelineDetails.
        :type display_name: str

        :param max_ocpu_count:
            The value to assign to the max_ocpu_count property of this CreateOpensearchClusterPipelineDetails.
        :type max_ocpu_count: int

        :param min_ocpu_count:
            The value to assign to the min_ocpu_count property of this CreateOpensearchClusterPipelineDetails.
        :type min_ocpu_count: int

        :param max_memory_gb:
            The value to assign to the max_memory_gb property of this CreateOpensearchClusterPipelineDetails.
        :type max_memory_gb: int

        :param min_memory_gb:
            The value to assign to the min_memory_gb property of this CreateOpensearchClusterPipelineDetails.
        :type min_memory_gb: int

        :param pipeline_configuration_body:
            The value to assign to the pipeline_configuration_body property of this CreateOpensearchClusterPipelineDetails.
        :type pipeline_configuration_body: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOpensearchClusterPipelineDetails.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateOpensearchClusterPipelineDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateOpensearchClusterPipelineDetails.
        :type subnet_id: str

        :param vcn_compartment_id:
            The value to assign to the vcn_compartment_id property of this CreateOpensearchClusterPipelineDetails.
        :type vcn_compartment_id: str

        :param subnet_compartment_id:
            The value to assign to the subnet_compartment_id property of this CreateOpensearchClusterPipelineDetails.
        :type subnet_compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOpensearchClusterPipelineDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOpensearchClusterPipelineDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateOpensearchClusterPipelineDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'max_ocpu_count': 'int',
            'min_ocpu_count': 'int',
            'max_memory_gb': 'int',
            'min_memory_gb': 'int',
            'pipeline_configuration_body': 'str',
            'compartment_id': 'str',
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
            'max_ocpu_count': 'maxOcpuCount',
            'min_ocpu_count': 'minOcpuCount',
            'max_memory_gb': 'maxMemoryGB',
            'min_memory_gb': 'minMemoryGB',
            'pipeline_configuration_body': 'pipelineConfigurationBody',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'vcn_compartment_id': 'vcnCompartmentId',
            'subnet_compartment_id': 'subnetCompartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._max_ocpu_count = None
        self._min_ocpu_count = None
        self._max_memory_gb = None
        self._min_memory_gb = None
        self._pipeline_configuration_body = None
        self._compartment_id = None
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
        **[Required]** Gets the display_name of this CreateOpensearchClusterPipelineDetails.
        The name of the cluster pipeline. Avoid entering confidential information.


        :return: The display_name of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateOpensearchClusterPipelineDetails.
        The name of the cluster pipeline. Avoid entering confidential information.


        :param display_name: The display_name of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def max_ocpu_count(self):
        """
        **[Required]** Gets the max_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        The maximum pipeline capacity, in OCPUs.


        :return: The max_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        :rtype: int
        """
        return self._max_ocpu_count

    @max_ocpu_count.setter
    def max_ocpu_count(self, max_ocpu_count):
        """
        Sets the max_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        The maximum pipeline capacity, in OCPUs.


        :param max_ocpu_count: The max_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        :type: int
        """
        self._max_ocpu_count = max_ocpu_count

    @property
    def min_ocpu_count(self):
        """
        **[Required]** Gets the min_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        The minimum pipeline capacity, in OCPUs.


        :return: The min_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        :rtype: int
        """
        return self._min_ocpu_count

    @min_ocpu_count.setter
    def min_ocpu_count(self, min_ocpu_count):
        """
        Sets the min_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        The minimum pipeline capacity, in OCPUs.


        :param min_ocpu_count: The min_ocpu_count of this CreateOpensearchClusterPipelineDetails.
        :type: int
        """
        self._min_ocpu_count = min_ocpu_count

    @property
    def max_memory_gb(self):
        """
        **[Required]** Gets the max_memory_gb of this CreateOpensearchClusterPipelineDetails.
        The maximum amount of memory in GB, for the pipeline.


        :return: The max_memory_gb of this CreateOpensearchClusterPipelineDetails.
        :rtype: int
        """
        return self._max_memory_gb

    @max_memory_gb.setter
    def max_memory_gb(self, max_memory_gb):
        """
        Sets the max_memory_gb of this CreateOpensearchClusterPipelineDetails.
        The maximum amount of memory in GB, for the pipeline.


        :param max_memory_gb: The max_memory_gb of this CreateOpensearchClusterPipelineDetails.
        :type: int
        """
        self._max_memory_gb = max_memory_gb

    @property
    def min_memory_gb(self):
        """
        **[Required]** Gets the min_memory_gb of this CreateOpensearchClusterPipelineDetails.
        The minimum amount of memory in GB, for the pipeline.


        :return: The min_memory_gb of this CreateOpensearchClusterPipelineDetails.
        :rtype: int
        """
        return self._min_memory_gb

    @min_memory_gb.setter
    def min_memory_gb(self, min_memory_gb):
        """
        Sets the min_memory_gb of this CreateOpensearchClusterPipelineDetails.
        The minimum amount of memory in GB, for the pipeline.


        :param min_memory_gb: The min_memory_gb of this CreateOpensearchClusterPipelineDetails.
        :type: int
        """
        self._min_memory_gb = min_memory_gb

    @property
    def pipeline_configuration_body(self):
        """
        **[Required]** Gets the pipeline_configuration_body of this CreateOpensearchClusterPipelineDetails.
        The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :return: The pipeline_configuration_body of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._pipeline_configuration_body

    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, pipeline_configuration_body):
        """
        Sets the pipeline_configuration_body of this CreateOpensearchClusterPipelineDetails.
        The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :param pipeline_configuration_body: The pipeline_configuration_body of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._pipeline_configuration_body = pipeline_configuration_body

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOpensearchClusterPipelineDetails.
        The OCID of the compartment to create the pipeline in.


        :return: The compartment_id of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOpensearchClusterPipelineDetails.
        The OCID of the compartment to create the pipeline in.


        :param compartment_id: The compartment_id of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateOpensearchClusterPipelineDetails.
        The OCID of the pipeline's VCN.


        :return: The vcn_id of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateOpensearchClusterPipelineDetails.
        The OCID of the pipeline's VCN.


        :param vcn_id: The vcn_id of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateOpensearchClusterPipelineDetails.
        The OCID of the pipeline's subnet.


        :return: The subnet_id of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateOpensearchClusterPipelineDetails.
        The OCID of the pipeline's subnet.


        :param subnet_id: The subnet_id of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def vcn_compartment_id(self):
        """
        **[Required]** Gets the vcn_compartment_id of this CreateOpensearchClusterPipelineDetails.
        The OCID for the compartment where the pipeline's VCN is located.


        :return: The vcn_compartment_id of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._vcn_compartment_id

    @vcn_compartment_id.setter
    def vcn_compartment_id(self, vcn_compartment_id):
        """
        Sets the vcn_compartment_id of this CreateOpensearchClusterPipelineDetails.
        The OCID for the compartment where the pipeline's VCN is located.


        :param vcn_compartment_id: The vcn_compartment_id of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._vcn_compartment_id = vcn_compartment_id

    @property
    def subnet_compartment_id(self):
        """
        **[Required]** Gets the subnet_compartment_id of this CreateOpensearchClusterPipelineDetails.
        The OCID for the compartment where the pipwline's subnet is located.


        :return: The subnet_compartment_id of this CreateOpensearchClusterPipelineDetails.
        :rtype: str
        """
        return self._subnet_compartment_id

    @subnet_compartment_id.setter
    def subnet_compartment_id(self, subnet_compartment_id):
        """
        Sets the subnet_compartment_id of this CreateOpensearchClusterPipelineDetails.
        The OCID for the compartment where the pipwline's subnet is located.


        :param subnet_compartment_id: The subnet_compartment_id of this CreateOpensearchClusterPipelineDetails.
        :type: str
        """
        self._subnet_compartment_id = subnet_compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOpensearchClusterPipelineDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOpensearchClusterPipelineDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOpensearchClusterPipelineDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOpensearchClusterPipelineDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOpensearchClusterPipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOpensearchClusterPipelineDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOpensearchClusterPipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOpensearchClusterPipelineDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateOpensearchClusterPipelineDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreateOpensearchClusterPipelineDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateOpensearchClusterPipelineDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreateOpensearchClusterPipelineDetails.
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
