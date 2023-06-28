# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportableComputeEntitySummary(object):
    """
    A compute entity that can be imported into Operations Insights.
    """

    #: A constant which can be used with the entity_source property of a ImportableComputeEntitySummary.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_HOST = "MACS_MANAGED_EXTERNAL_HOST"

    #: A constant which can be used with the entity_source property of a ImportableComputeEntitySummary.
    #: This constant has a value of "MACS_MANAGED_CLOUD_HOST"
    ENTITY_SOURCE_MACS_MANAGED_CLOUD_HOST = "MACS_MANAGED_CLOUD_HOST"

    def __init__(self, **kwargs):
        """
        Initializes a new ImportableComputeEntitySummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.CloudImportableComputeEntitySummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this ImportableComputeEntitySummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "MACS_MANAGED_CLOUD_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param compute_id:
            The value to assign to the compute_id property of this ImportableComputeEntitySummary.
        :type compute_id: str

        :param compute_display_name:
            The value to assign to the compute_display_name property of this ImportableComputeEntitySummary.
        :type compute_display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ImportableComputeEntitySummary.
        :type compartment_id: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compute_id': 'str',
            'compute_display_name': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'compute_id': 'computeId',
            'compute_display_name': 'computeDisplayName',
            'compartment_id': 'compartmentId'
        }

        self._entity_source = None
        self._compute_id = None
        self._compute_display_name = None
        self._compartment_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'MACS_MANAGED_CLOUD_HOST':
            return 'CloudImportableComputeEntitySummary'
        else:
            return 'ImportableComputeEntitySummary'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this ImportableComputeEntitySummary.
        Source of the importable agent entity.

        Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "MACS_MANAGED_CLOUD_HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this ImportableComputeEntitySummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this ImportableComputeEntitySummary.
        Source of the importable agent entity.


        :param entity_source: The entity_source of this ImportableComputeEntitySummary.
        :type: str
        """
        allowed_values = ["MACS_MANAGED_EXTERNAL_HOST", "MACS_MANAGED_CLOUD_HOST"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def compute_id(self):
        """
        **[Required]** Gets the compute_id of this ImportableComputeEntitySummary.
        The `OCID`__ of the Compute Instance

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compute_id of this ImportableComputeEntitySummary.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        """
        Sets the compute_id of this ImportableComputeEntitySummary.
        The `OCID`__ of the Compute Instance

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compute_id: The compute_id of this ImportableComputeEntitySummary.
        :type: str
        """
        self._compute_id = compute_id

    @property
    def compute_display_name(self):
        """
        **[Required]** Gets the compute_display_name of this ImportableComputeEntitySummary.
        The `Display Name`__ of the Compute Instance

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display


        :return: The compute_display_name of this ImportableComputeEntitySummary.
        :rtype: str
        """
        return self._compute_display_name

    @compute_display_name.setter
    def compute_display_name(self, compute_display_name):
        """
        Sets the compute_display_name of this ImportableComputeEntitySummary.
        The `Display Name`__ of the Compute Instance

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display


        :param compute_display_name: The compute_display_name of this ImportableComputeEntitySummary.
        :type: str
        """
        self._compute_display_name = compute_display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ImportableComputeEntitySummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ImportableComputeEntitySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ImportableComputeEntitySummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ImportableComputeEntitySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
