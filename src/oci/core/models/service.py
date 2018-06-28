# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Service(object):
    """
    Information about a service that is accessible through a service gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Service object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this Service.
        :type cidr_block: str

        :param description:
            The value to assign to the description property of this Service.
        :type description: str

        :param id:
            The value to assign to the id property of this Service.
        :type id: str

        :param name:
            The value to assign to the name property of this Service.
        :type name: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'description': 'str',
            'id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'description': 'description',
            'id': 'id',
            'name': 'name'
        }

        self._cidr_block = None
        self._description = None
        self._id = None
        self._name = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this Service.
        A string that represents the public endpoints for the service. When you set up a route rule
        to route traffic to the service gateway, use this value as the destination CIDR block for
        the rule. See :class:`RouteTable`.


        :return: The cidr_block of this Service.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Service.
        A string that represents the public endpoints for the service. When you set up a route rule
        to route traffic to the service gateway, use this value as the destination CIDR block for
        the rule. See :class:`RouteTable`.


        :param cidr_block: The cidr_block of this Service.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Service.
        Description of the service.


        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Service.
        Description of the service.


        :param description: The description of this Service.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Service.
        The service's `OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Service.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Service.
        The service's `OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Service.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Service.
        Name of the service.


        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Service.
        Name of the service.


        :param name: The name of this Service.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
