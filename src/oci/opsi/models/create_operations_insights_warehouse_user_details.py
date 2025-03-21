# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOperationsInsightsWarehouseUserDetails(object):
    """
    The information about a Operations Insights Warehouse User to be created. Input compartmentId MUST be the root compartment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOperationsInsightsWarehouseUserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operations_insights_warehouse_id:
            The value to assign to the operations_insights_warehouse_id property of this CreateOperationsInsightsWarehouseUserDetails.
        :type operations_insights_warehouse_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOperationsInsightsWarehouseUserDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateOperationsInsightsWarehouseUserDetails.
        :type name: str

        :param connection_password:
            The value to assign to the connection_password property of this CreateOperationsInsightsWarehouseUserDetails.
        :type connection_password: str

        :param is_awr_data_access:
            The value to assign to the is_awr_data_access property of this CreateOperationsInsightsWarehouseUserDetails.
        :type is_awr_data_access: bool

        :param is_em_data_access:
            The value to assign to the is_em_data_access property of this CreateOperationsInsightsWarehouseUserDetails.
        :type is_em_data_access: bool

        :param is_opsi_data_access:
            The value to assign to the is_opsi_data_access property of this CreateOperationsInsightsWarehouseUserDetails.
        :type is_opsi_data_access: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOperationsInsightsWarehouseUserDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOperationsInsightsWarehouseUserDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'operations_insights_warehouse_id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'connection_password': 'str',
            'is_awr_data_access': 'bool',
            'is_em_data_access': 'bool',
            'is_opsi_data_access': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'operations_insights_warehouse_id': 'operationsInsightsWarehouseId',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'connection_password': 'connectionPassword',
            'is_awr_data_access': 'isAwrDataAccess',
            'is_em_data_access': 'isEmDataAccess',
            'is_opsi_data_access': 'isOpsiDataAccess',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._operations_insights_warehouse_id = None
        self._compartment_id = None
        self._name = None
        self._connection_password = None
        self._is_awr_data_access = None
        self._is_em_data_access = None
        self._is_opsi_data_access = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def operations_insights_warehouse_id(self):
        """
        **[Required]** Gets the operations_insights_warehouse_id of this CreateOperationsInsightsWarehouseUserDetails.
        OPSI Warehouse OCID


        :return: The operations_insights_warehouse_id of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: str
        """
        return self._operations_insights_warehouse_id

    @operations_insights_warehouse_id.setter
    def operations_insights_warehouse_id(self, operations_insights_warehouse_id):
        """
        Sets the operations_insights_warehouse_id of this CreateOperationsInsightsWarehouseUserDetails.
        OPSI Warehouse OCID


        :param operations_insights_warehouse_id: The operations_insights_warehouse_id of this CreateOperationsInsightsWarehouseUserDetails.
        :type: str
        """
        self._operations_insights_warehouse_id = operations_insights_warehouse_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOperationsInsightsWarehouseUserDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOperationsInsightsWarehouseUserDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateOperationsInsightsWarehouseUserDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateOperationsInsightsWarehouseUserDetails.
        Username for schema which would have access to AWR Data,  Enterprise Manager Data and Ops Insights OPSI Hub.


        :return: The name of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateOperationsInsightsWarehouseUserDetails.
        Username for schema which would have access to AWR Data,  Enterprise Manager Data and Ops Insights OPSI Hub.


        :param name: The name of this CreateOperationsInsightsWarehouseUserDetails.
        :type: str
        """
        self._name = name

    @property
    def connection_password(self):
        """
        **[Required]** Gets the connection_password of this CreateOperationsInsightsWarehouseUserDetails.
        User provided connection password for the AWR Data,  Enterprise Manager Data and Ops Insights OPSI Hub.


        :return: The connection_password of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: str
        """
        return self._connection_password

    @connection_password.setter
    def connection_password(self, connection_password):
        """
        Sets the connection_password of this CreateOperationsInsightsWarehouseUserDetails.
        User provided connection password for the AWR Data,  Enterprise Manager Data and Ops Insights OPSI Hub.


        :param connection_password: The connection_password of this CreateOperationsInsightsWarehouseUserDetails.
        :type: str
        """
        self._connection_password = connection_password

    @property
    def is_awr_data_access(self):
        """
        **[Required]** Gets the is_awr_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to AWR data.


        :return: The is_awr_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: bool
        """
        return self._is_awr_data_access

    @is_awr_data_access.setter
    def is_awr_data_access(self, is_awr_data_access):
        """
        Sets the is_awr_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to AWR data.


        :param is_awr_data_access: The is_awr_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        :type: bool
        """
        self._is_awr_data_access = is_awr_data_access

    @property
    def is_em_data_access(self):
        """
        Gets the is_em_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to EM data.


        :return: The is_em_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: bool
        """
        return self._is_em_data_access

    @is_em_data_access.setter
    def is_em_data_access(self, is_em_data_access):
        """
        Sets the is_em_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to EM data.


        :param is_em_data_access: The is_em_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        :type: bool
        """
        self._is_em_data_access = is_em_data_access

    @property
    def is_opsi_data_access(self):
        """
        Gets the is_opsi_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to OPSI data.


        :return: The is_opsi_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: bool
        """
        return self._is_opsi_data_access

    @is_opsi_data_access.setter
    def is_opsi_data_access(self, is_opsi_data_access):
        """
        Sets the is_opsi_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to OPSI data.


        :param is_opsi_data_access: The is_opsi_data_access of this CreateOperationsInsightsWarehouseUserDetails.
        :type: bool
        """
        self._is_opsi_data_access = is_opsi_data_access

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOperationsInsightsWarehouseUserDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOperationsInsightsWarehouseUserDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOperationsInsightsWarehouseUserDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOperationsInsightsWarehouseUserDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOperationsInsightsWarehouseUserDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOperationsInsightsWarehouseUserDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOperationsInsightsWarehouseUserDetails.
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
