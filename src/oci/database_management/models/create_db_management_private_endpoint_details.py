# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbManagementPrivateEndpointDetails(object):
    """
    The details used to create a new Database Management private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbManagementPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateDbManagementPrivateEndpointDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDbManagementPrivateEndpointDetails.
        :type compartment_id: str

        :param is_cluster:
            The value to assign to the is_cluster property of this CreateDbManagementPrivateEndpointDetails.
        :type is_cluster: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDbManagementPrivateEndpointDetails.
        :type subnet_id: str

        :param description:
            The value to assign to the description property of this CreateDbManagementPrivateEndpointDetails.
        :type description: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateDbManagementPrivateEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'is_cluster': 'bool',
            'subnet_id': 'str',
            'description': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'is_cluster': 'isCluster',
            'subnet_id': 'subnetId',
            'description': 'description',
            'nsg_ids': 'nsgIds'
        }

        self._name = None
        self._compartment_id = None
        self._is_cluster = None
        self._subnet_id = None
        self._description = None
        self._nsg_ids = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDbManagementPrivateEndpointDetails.
        The display name of the Database Management private endpoint.


        :return: The name of this CreateDbManagementPrivateEndpointDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDbManagementPrivateEndpointDetails.
        The display name of the Database Management private endpoint.


        :param name: The name of this CreateDbManagementPrivateEndpointDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDbManagementPrivateEndpointDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDbManagementPrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDbManagementPrivateEndpointDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDbManagementPrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this CreateDbManagementPrivateEndpointDetails.
        Specifies whether the Database Management private endpoint will be used for Oracle Databases in a cluster.


        :return: The is_cluster of this CreateDbManagementPrivateEndpointDetails.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this CreateDbManagementPrivateEndpointDetails.
        Specifies whether the Database Management private endpoint will be used for Oracle Databases in a cluster.


        :param is_cluster: The is_cluster of this CreateDbManagementPrivateEndpointDetails.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateDbManagementPrivateEndpointDetails.
        The `OCID`__ of the subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateDbManagementPrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDbManagementPrivateEndpointDetails.
        The `OCID`__ of the subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateDbManagementPrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def description(self):
        """
        Gets the description of this CreateDbManagementPrivateEndpointDetails.
        The description of the private endpoint.


        :return: The description of this CreateDbManagementPrivateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDbManagementPrivateEndpointDetails.
        The description of the private endpoint.


        :param description: The description of this CreateDbManagementPrivateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateDbManagementPrivateEndpointDetails.
        The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.


        :return: The nsg_ids of this CreateDbManagementPrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateDbManagementPrivateEndpointDetails.
        The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.


        :param nsg_ids: The nsg_ids of this CreateDbManagementPrivateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
