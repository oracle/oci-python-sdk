# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataMemberSummary(object):
    """
    Lists name, display name and type of exadata member.
    """

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "DATABASE"
    ENTITY_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "ILOM_SERVER"
    ENTITY_TYPE_ILOM_SERVER = "ILOM_SERVER"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "PDU"
    ENTITY_TYPE_PDU = "PDU"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "STORAGE_SERVER"
    ENTITY_TYPE_STORAGE_SERVER = "STORAGE_SERVER"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "CLUSTER_ASM"
    ENTITY_TYPE_CLUSTER_ASM = "CLUSTER_ASM"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "INFINIBAND_SWITCH"
    ENTITY_TYPE_INFINIBAND_SWITCH = "INFINIBAND_SWITCH"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "ETHERNET_SWITCH"
    ENTITY_TYPE_ETHERNET_SWITCH = "ETHERNET_SWITCH"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "HOST"
    ENTITY_TYPE_HOST = "HOST"

    #: A constant which can be used with the entity_type property of a ExadataMemberSummary.
    #: This constant has a value of "VM_CLUSTER"
    ENTITY_TYPE_VM_CLUSTER = "VM_CLUSTER"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataMemberSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ExadataMemberSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this ExadataMemberSummary.
        :type display_name: str

        :param entity_type:
            The value to assign to the entity_type property of this ExadataMemberSummary.
            Allowed values for this property are: "DATABASE", "ILOM_SERVER", "PDU", "STORAGE_SERVER", "CLUSTER_ASM", "INFINIBAND_SWITCH", "ETHERNET_SWITCH", "HOST", "VM_CLUSTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'entity_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'entity_type': 'entityType'
        }

        self._name = None
        self._display_name = None
        self._entity_type = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ExadataMemberSummary.
        Name of exadata member target


        :return: The name of this ExadataMemberSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExadataMemberSummary.
        Name of exadata member target


        :param name: The name of this ExadataMemberSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExadataMemberSummary.
        Display Name of exadata member target


        :return: The display_name of this ExadataMemberSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExadataMemberSummary.
        Display Name of exadata member target


        :param display_name: The display_name of this ExadataMemberSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this ExadataMemberSummary.
        Entity type of exadata member target

        Allowed values for this property are: "DATABASE", "ILOM_SERVER", "PDU", "STORAGE_SERVER", "CLUSTER_ASM", "INFINIBAND_SWITCH", "ETHERNET_SWITCH", "HOST", "VM_CLUSTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this ExadataMemberSummary.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ExadataMemberSummary.
        Entity type of exadata member target


        :param entity_type: The entity_type of this ExadataMemberSummary.
        :type: str
        """
        allowed_values = ["DATABASE", "ILOM_SERVER", "PDU", "STORAGE_SERVER", "CLUSTER_ASM", "INFINIBAND_SWITCH", "ETHERNET_SWITCH", "HOST", "VM_CLUSTER"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
