# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetDetails(object):
    """
    Details of target member of a Exadata Fleet Update Collection.
    """

    #: A constant which can be used with the entity_type property of a TargetDetails.
    #: This constant has a value of "DATABASE"
    ENTITY_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the entity_type property of a TargetDetails.
    #: This constant has a value of "VMCLUSTER"
    ENTITY_TYPE_VMCLUSTER = "VMCLUSTER"

    #: A constant which can be used with the entity_type property of a TargetDetails.
    #: This constant has a value of "CLOUDVMCLUSTER"
    ENTITY_TYPE_CLOUDVMCLUSTER = "CLOUDVMCLUSTER"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.VmClusterTargetSummary`
        * :class:`~oci.fleet_software_update.models.CloudVmClusterTargetSummary`
        * :class:`~oci.fleet_software_update.models.DatabaseTargetSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this TargetDetails.
            Allowed values for this property are: "DATABASE", "VMCLUSTER", "CLOUDVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param id:
            The value to assign to the id property of this TargetDetails.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'entity_type': 'str',
            'id': 'str',
            'compartment_id': 'str'
        }
        self.attribute_map = {
            'entity_type': 'entityType',
            'id': 'id',
            'compartment_id': 'compartmentId'
        }
        self._entity_type = None
        self._id = None
        self._compartment_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entityType']

        if type == 'VMCLUSTER':
            return 'VmClusterTargetSummary'

        if type == 'CLOUDVMCLUSTER':
            return 'CloudVmClusterTargetSummary'

        if type == 'DATABASE':
            return 'DatabaseTargetSummary'
        else:
            return 'TargetDetails'

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this TargetDetails.
        Resource EntityType for the target in the Exadata Fleet Update Collection.

        Allowed values for this property are: "DATABASE", "VMCLUSTER", "CLOUDVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this TargetDetails.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this TargetDetails.
        Resource EntityType for the target in the Exadata Fleet Update Collection.


        :param entity_type: The entity_type of this TargetDetails.
        :type: str
        """
        allowed_values = ["DATABASE", "VMCLUSTER", "CLOUDVMCLUSTER"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def id(self):
        """
        Gets the id of this TargetDetails.
        OCID of the target resource in the Exadata Fleet Update Collection.


        :return: The id of this TargetDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetDetails.
        OCID of the target resource in the Exadata Fleet Update Collection.


        :param id: The id of this TargetDetails.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TargetDetails.
        Compartment identifier of the target.


        :return: The compartment_id of this TargetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetDetails.
        Compartment identifier of the target.


        :param compartment_id: The compartment_id of this TargetDetails.
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
