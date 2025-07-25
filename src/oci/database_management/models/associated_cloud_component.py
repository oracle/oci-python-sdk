# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociatedCloudComponent(object):
    """
    The details of the associated component.
    """

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "ASM"
    COMPONENT_TYPE_ASM = "ASM"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "ASM_INSTANCE"
    COMPONENT_TYPE_ASM_INSTANCE = "ASM_INSTANCE"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "CLUSTER"
    COMPONENT_TYPE_CLUSTER = "CLUSTER"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "CLUSTER_INSTANCE"
    COMPONENT_TYPE_CLUSTER_INSTANCE = "CLUSTER_INSTANCE"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "DATABASE"
    COMPONENT_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "DATABASE_INSTANCE"
    COMPONENT_TYPE_DATABASE_INSTANCE = "DATABASE_INSTANCE"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "DATABASE_HOME"
    COMPONENT_TYPE_DATABASE_HOME = "DATABASE_HOME"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "DATABASE_NODE"
    COMPONENT_TYPE_DATABASE_NODE = "DATABASE_NODE"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "DBSYSTEM"
    COMPONENT_TYPE_DBSYSTEM = "DBSYSTEM"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "LISTENER"
    COMPONENT_TYPE_LISTENER = "LISTENER"

    #: A constant which can be used with the component_type property of a AssociatedCloudComponent.
    #: This constant has a value of "PLUGGABLE_DATABASE"
    COMPONENT_TYPE_PLUGGABLE_DATABASE = "PLUGGABLE_DATABASE"

    #: A constant which can be used with the association_type property of a AssociatedCloudComponent.
    #: This constant has a value of "CONTAINS"
    ASSOCIATION_TYPE_CONTAINS = "CONTAINS"

    #: A constant which can be used with the association_type property of a AssociatedCloudComponent.
    #: This constant has a value of "USES"
    ASSOCIATION_TYPE_USES = "USES"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociatedCloudComponent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_id:
            The value to assign to the component_id property of this AssociatedCloudComponent.
        :type component_id: str

        :param component_type:
            The value to assign to the component_type property of this AssociatedCloudComponent.
            Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type component_type: str

        :param association_type:
            The value to assign to the association_type property of this AssociatedCloudComponent.
            Allowed values for this property are: "CONTAINS", "USES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type association_type: str

        """
        self.swagger_types = {
            'component_id': 'str',
            'component_type': 'str',
            'association_type': 'str'
        }
        self.attribute_map = {
            'component_id': 'componentId',
            'component_type': 'componentType',
            'association_type': 'associationType'
        }
        self._component_id = None
        self._component_type = None
        self._association_type = None

    @property
    def component_id(self):
        """
        **[Required]** Gets the component_id of this AssociatedCloudComponent.
        The identifier of the associated component.


        :return: The component_id of this AssociatedCloudComponent.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """
        Sets the component_id of this AssociatedCloudComponent.
        The identifier of the associated component.


        :param component_id: The component_id of this AssociatedCloudComponent.
        :type: str
        """
        self._component_id = component_id

    @property
    def component_type(self):
        """
        Gets the component_type of this AssociatedCloudComponent.
        The type of associated component.

        Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The component_type of this AssociatedCloudComponent.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this AssociatedCloudComponent.
        The type of associated component.


        :param component_type: The component_type of this AssociatedCloudComponent.
        :type: str
        """
        allowed_values = ["ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE"]
        if not value_allowed_none_or_none_sentinel(component_type, allowed_values):
            component_type = 'UNKNOWN_ENUM_VALUE'
        self._component_type = component_type

    @property
    def association_type(self):
        """
        **[Required]** Gets the association_type of this AssociatedCloudComponent.
        The association type.

        Allowed values for this property are: "CONTAINS", "USES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The association_type of this AssociatedCloudComponent.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """
        Sets the association_type of this AssociatedCloudComponent.
        The association type.


        :param association_type: The association_type of this AssociatedCloudComponent.
        :type: str
        """
        allowed_values = ["CONTAINS", "USES"]
        if not value_allowed_none_or_none_sentinel(association_type, allowed_values):
            association_type = 'UNKNOWN_ENUM_VALUE'
        self._association_type = association_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
