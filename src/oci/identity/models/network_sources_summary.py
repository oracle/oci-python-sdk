# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkSourcesSummary(object):
    """
    A network source specifies a list of source IP addresses that are allowed to make authorization requests.
    Use the network source in policy statements to restrict access to only requests that come from the specified IPs.
    For more information, see `Managing Network Sources`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Tasks/managingnetworksources.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkSourcesSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NetworkSourcesSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NetworkSourcesSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this NetworkSourcesSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this NetworkSourcesSummary.
        :type description: str

        :param public_source_list:
            The value to assign to the public_source_list property of this NetworkSourcesSummary.
        :type public_source_list: list[str]

        :param virtual_source_list:
            The value to assign to the virtual_source_list property of this NetworkSourcesSummary.
        :type virtual_source_list: list[NetworkSourcesVirtualSourceList]

        :param services:
            The value to assign to the services property of this NetworkSourcesSummary.
        :type services: list[str]

        :param time_created:
            The value to assign to the time_created property of this NetworkSourcesSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'public_source_list': 'list[str]',
            'virtual_source_list': 'list[NetworkSourcesVirtualSourceList]',
            'services': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'public_source_list': 'publicSourceList',
            'virtual_source_list': 'virtualSourceList',
            'services': 'services',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._public_source_list = None
        self._virtual_source_list = None
        self._services = None
        self._time_created = None

    @property
    def id(self):
        """
        Gets the id of this NetworkSourcesSummary.
        The OCID of the network source.


        :return: The id of this NetworkSourcesSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NetworkSourcesSummary.
        The OCID of the network source.


        :param id: The id of this NetworkSourcesSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this NetworkSourcesSummary.
        The OCID of the tenancy (root compartment) containing the network source.


        :return: The compartment_id of this NetworkSourcesSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NetworkSourcesSummary.
        The OCID of the tenancy (root compartment) containing the network source.


        :param compartment_id: The compartment_id of this NetworkSourcesSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this NetworkSourcesSummary.
        The name you assign to the network source during creation. The name must be unique across
        the tenancy and cannot be changed.


        :return: The name of this NetworkSourcesSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NetworkSourcesSummary.
        The name you assign to the network source during creation. The name must be unique across
        the tenancy and cannot be changed.


        :param name: The name of this NetworkSourcesSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this NetworkSourcesSummary.
        The description you assign to the network source. Does not have to be unique, and it's changeable.


        :return: The description of this NetworkSourcesSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NetworkSourcesSummary.
        The description you assign to the network source. Does not have to be unique, and it's changeable.


        :param description: The description of this NetworkSourcesSummary.
        :type: str
        """
        self._description = description

    @property
    def public_source_list(self):
        """
        Gets the public_source_list of this NetworkSourcesSummary.
        A list of allowed public IP addresses and CIDR ranges.


        :return: The public_source_list of this NetworkSourcesSummary.
        :rtype: list[str]
        """
        return self._public_source_list

    @public_source_list.setter
    def public_source_list(self, public_source_list):
        """
        Sets the public_source_list of this NetworkSourcesSummary.
        A list of allowed public IP addresses and CIDR ranges.


        :param public_source_list: The public_source_list of this NetworkSourcesSummary.
        :type: list[str]
        """
        self._public_source_list = public_source_list

    @property
    def virtual_source_list(self):
        """
        Gets the virtual_source_list of this NetworkSourcesSummary.
        A list of allowed VCN OCID and IP range pairs.
        Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`


        :return: The virtual_source_list of this NetworkSourcesSummary.
        :rtype: list[NetworkSourcesVirtualSourceList]
        """
        return self._virtual_source_list

    @virtual_source_list.setter
    def virtual_source_list(self, virtual_source_list):
        """
        Sets the virtual_source_list of this NetworkSourcesSummary.
        A list of allowed VCN OCID and IP range pairs.
        Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`


        :param virtual_source_list: The virtual_source_list of this NetworkSourcesSummary.
        :type: list[NetworkSourcesVirtualSourceList]
        """
        self._virtual_source_list = virtual_source_list

    @property
    def services(self):
        """
        Gets the services of this NetworkSourcesSummary.
        A list of services allowed to make on-behalf-of requests. These requests can have different source IPs than
        those specified in the network source. Currently, only `all` and `none` are supported. The default is `all`.


        :return: The services of this NetworkSourcesSummary.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this NetworkSourcesSummary.
        A list of services allowed to make on-behalf-of requests. These requests can have different source IPs than
        those specified in the network source. Currently, only `all` and `none` are supported. The default is `all`.


        :param services: The services of this NetworkSourcesSummary.
        :type: list[str]
        """
        self._services = services

    @property
    def time_created(self):
        """
        Gets the time_created of this NetworkSourcesSummary.
        Date and time the group was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this NetworkSourcesSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NetworkSourcesSummary.
        Date and time the group was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this NetworkSourcesSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
