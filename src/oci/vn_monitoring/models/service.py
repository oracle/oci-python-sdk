# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Service(object):
    """
    An object that represents one or multiple Oracle services that you can enable for a
    :class:`ServiceGateway`. In the User Guide topic
    `Access to Oracle Services: Service Gateway`__, the
    term *service CIDR label* is used to refer to the string that represents the regional public
    IP address ranges of the Oracle service or services covered by a given `Service` object. That
    unique string is the value of the `Service` object's `cidrBlock` attribute.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm
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
        A string that represents the regional public IP address ranges for the Oracle service or
        services covered by this `Service` object. Also known as the `Service` object's *service
        CIDR label*.

        When you set up a route rule to route traffic to the service gateway, use this value as the
        rule's destination. See :class:`RouteTable`. Also, when you set up
        a security list rule to cover traffic with the service gateway, use the `cidrBlock` value
        as the rule's destination (for an egress rule) or the source (for an ingress rule).
        See :class:`SecurityList`.

        Example: `oci-phx-objectstorage`


        :return: The cidr_block of this Service.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Service.
        A string that represents the regional public IP address ranges for the Oracle service or
        services covered by this `Service` object. Also known as the `Service` object's *service
        CIDR label*.

        When you set up a route rule to route traffic to the service gateway, use this value as the
        rule's destination. See :class:`RouteTable`. Also, when you set up
        a security list rule to cover traffic with the service gateway, use the `cidrBlock` value
        as the rule's destination (for an egress rule) or the source (for an ingress rule).
        See :class:`SecurityList`.

        Example: `oci-phx-objectstorage`


        :param cidr_block: The cidr_block of this Service.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Service.
        Description of the Oracle service or services covered by this `Service` object.

        Example: `OCI PHX Object Storage`


        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Service.
        Description of the Oracle service or services covered by this `Service` object.

        Example: `OCI PHX Object Storage`


        :param description: The description of this Service.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Service.
        The `Service` object's `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Service.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Service.
        The `Service` object's `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Service.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Service.
        Name of the `Service` object. This name can change and is not guaranteed to be unique.

        Example: `OCI PHX Object Storage`


        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Service.
        Name of the `Service` object. This name can change and is not guaranteed to be unique.

        Example: `OCI PHX Object Storage`


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
