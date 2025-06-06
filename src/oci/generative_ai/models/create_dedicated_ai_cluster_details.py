# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDedicatedAiClusterDetails(object):
    """
    The data to create a dedicated AI cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDedicatedAiClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDedicatedAiClusterDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDedicatedAiClusterDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateDedicatedAiClusterDetails.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDedicatedAiClusterDetails.
        :type compartment_id: str

        :param unit_count:
            The value to assign to the unit_count property of this CreateDedicatedAiClusterDetails.
        :type unit_count: int

        :param unit_shape:
            The value to assign to the unit_shape property of this CreateDedicatedAiClusterDetails.
        :type unit_shape: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDedicatedAiClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDedicatedAiClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'unit_count': 'int',
            'unit_shape': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'unit_count': 'unitCount',
            'unit_shape': 'unitShape',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._description = None
        self._type = None
        self._compartment_id = None
        self._unit_count = None
        self._unit_shape = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDedicatedAiClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateDedicatedAiClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDedicatedAiClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateDedicatedAiClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDedicatedAiClusterDetails.
        An optional description of the dedicated AI cluster.


        :return: The description of this CreateDedicatedAiClusterDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDedicatedAiClusterDetails.
        An optional description of the dedicated AI cluster.


        :param description: The description of this CreateDedicatedAiClusterDetails.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateDedicatedAiClusterDetails.
        The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.

        Allowed values are:
        - HOSTING
        - FINE_TUNING


        :return: The type of this CreateDedicatedAiClusterDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateDedicatedAiClusterDetails.
        The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.

        Allowed values are:
        - HOSTING
        - FINE_TUNING


        :param type: The type of this CreateDedicatedAiClusterDetails.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDedicatedAiClusterDetails.
        The compartment OCID to create the dedicated AI cluster in.


        :return: The compartment_id of this CreateDedicatedAiClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDedicatedAiClusterDetails.
        The compartment OCID to create the dedicated AI cluster in.


        :param compartment_id: The compartment_id of this CreateDedicatedAiClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def unit_count(self):
        """
        **[Required]** Gets the unit_count of this CreateDedicatedAiClusterDetails.
        The number of dedicated units in this AI cluster.


        :return: The unit_count of this CreateDedicatedAiClusterDetails.
        :rtype: int
        """
        return self._unit_count

    @unit_count.setter
    def unit_count(self, unit_count):
        """
        Sets the unit_count of this CreateDedicatedAiClusterDetails.
        The number of dedicated units in this AI cluster.


        :param unit_count: The unit_count of this CreateDedicatedAiClusterDetails.
        :type: int
        """
        self._unit_count = unit_count

    @property
    def unit_shape(self):
        """
        **[Required]** Gets the unit_shape of this CreateDedicatedAiClusterDetails.
        The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

        Allowed values are:
        - LARGE_COHERE
        - LARGE_COHERE_V2
        - SMALL_COHERE
        - SMALL_COHERE_V2
        - SMALL_COHERE_4
        - EMBED_COHERE
        - LLAMA2_70
        - LARGE_GENERIC
        - LARGE_COHERE_V2_2
        - LARGE_GENERIC_4
        - SMALL_GENERIC_V2
        - LARGE_GENERIC_2
        - LARGE_COHERE_V3
        - RERANK_COHERE


        :return: The unit_shape of this CreateDedicatedAiClusterDetails.
        :rtype: str
        """
        return self._unit_shape

    @unit_shape.setter
    def unit_shape(self, unit_shape):
        """
        Sets the unit_shape of this CreateDedicatedAiClusterDetails.
        The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

        Allowed values are:
        - LARGE_COHERE
        - LARGE_COHERE_V2
        - SMALL_COHERE
        - SMALL_COHERE_V2
        - SMALL_COHERE_4
        - EMBED_COHERE
        - LLAMA2_70
        - LARGE_GENERIC
        - LARGE_COHERE_V2_2
        - LARGE_GENERIC_4
        - SMALL_GENERIC_V2
        - LARGE_GENERIC_2
        - LARGE_COHERE_V3
        - RERANK_COHERE


        :param unit_shape: The unit_shape of this CreateDedicatedAiClusterDetails.
        :type: str
        """
        self._unit_shape = unit_shape

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDedicatedAiClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDedicatedAiClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDedicatedAiClusterDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDedicatedAiClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDedicatedAiClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDedicatedAiClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDedicatedAiClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDedicatedAiClusterDetails.
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
