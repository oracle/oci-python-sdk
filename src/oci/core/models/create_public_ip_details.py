# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePublicIpDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePublicIpDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePublicIpDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreatePublicIpDetails.
        :type display_name: str

        :param lifetime:
            The value to assign to the lifetime property of this CreatePublicIpDetails.
            Allowed values for this property are: "EPHEMERAL", "RESERVED"
        :type lifetime: str

        :param private_ip_id:
            The value to assign to the private_ip_id property of this CreatePublicIpDetails.
        :type private_ip_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'lifetime': 'str',
            'private_ip_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifetime': 'lifetime',
            'private_ip_id': 'privateIpId'
        }

        self._compartment_id = None
        self._display_name = None
        self._lifetime = None
        self._private_ip_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePublicIpDetails.
        The OCID of the compartment to contain the public IP. For ephemeral public IPs,
        you must set this to the private IP's compartment OCID.


        :return: The compartment_id of this CreatePublicIpDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePublicIpDetails.
        The OCID of the compartment to contain the public IP. For ephemeral public IPs,
        you must set this to the private IP's compartment OCID.


        :param compartment_id: The compartment_id of this CreatePublicIpDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreatePublicIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this CreatePublicIpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePublicIpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this CreatePublicIpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifetime(self):
        """
        **[Required]** Gets the lifetime of this CreatePublicIpDetails.
        Defines when the public IP is deleted and released back to the Oracle Cloud
        Infrastructure public IP pool. For more information, see
        `Public IP Addresses`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingpublicIPs.htm

        Allowed values for this property are: "EPHEMERAL", "RESERVED"


        :return: The lifetime of this CreatePublicIpDetails.
        :rtype: str
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """
        Sets the lifetime of this CreatePublicIpDetails.
        Defines when the public IP is deleted and released back to the Oracle Cloud
        Infrastructure public IP pool. For more information, see
        `Public IP Addresses`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingpublicIPs.htm


        :param lifetime: The lifetime of this CreatePublicIpDetails.
        :type: str
        """
        allowed_values = ["EPHEMERAL", "RESERVED"]
        if not value_allowed_none_or_none_sentinel(lifetime, allowed_values):
            raise ValueError(
                "Invalid value for `lifetime`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifetime = lifetime

    @property
    def private_ip_id(self):
        """
        Gets the private_ip_id of this CreatePublicIpDetails.
        The OCID of the private IP to assign the public IP to.

        Required for an ephemeral public IP because it must always be assigned to a private IP
        (specifically a *primary* private IP).

        Optional for a reserved public IP. If you don't provide it, the public IP is created but not
        assigned to a private IP. You can later assign the public IP with
        :func:`update_public_ip`.


        :return: The private_ip_id of this CreatePublicIpDetails.
        :rtype: str
        """
        return self._private_ip_id

    @private_ip_id.setter
    def private_ip_id(self, private_ip_id):
        """
        Sets the private_ip_id of this CreatePublicIpDetails.
        The OCID of the private IP to assign the public IP to.

        Required for an ephemeral public IP because it must always be assigned to a private IP
        (specifically a *primary* private IP).

        Optional for a reserved public IP. If you don't provide it, the public IP is created but not
        assigned to a private IP. You can later assign the public IP with
        :func:`update_public_ip`.


        :param private_ip_id: The private_ip_id of this CreatePublicIpDetails.
        :type: str
        """
        self._private_ip_id = private_ip_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
