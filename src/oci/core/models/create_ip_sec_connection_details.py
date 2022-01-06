# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIPSecConnectionDetails(object):
    """
    CreateIPSecConnectionDetails model.
    """

    #: A constant which can be used with the cpe_local_identifier_type property of a CreateIPSecConnectionDetails.
    #: This constant has a value of "IP_ADDRESS"
    CPE_LOCAL_IDENTIFIER_TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the cpe_local_identifier_type property of a CreateIPSecConnectionDetails.
    #: This constant has a value of "HOSTNAME"
    CPE_LOCAL_IDENTIFIER_TYPE_HOSTNAME = "HOSTNAME"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIPSecConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIPSecConnectionDetails.
        :type compartment_id: str

        :param cpe_id:
            The value to assign to the cpe_id property of this CreateIPSecConnectionDetails.
        :type cpe_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIPSecConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateIPSecConnectionDetails.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this CreateIPSecConnectionDetails.
        :type drg_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIPSecConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param cpe_local_identifier:
            The value to assign to the cpe_local_identifier property of this CreateIPSecConnectionDetails.
        :type cpe_local_identifier: str

        :param cpe_local_identifier_type:
            The value to assign to the cpe_local_identifier_type property of this CreateIPSecConnectionDetails.
            Allowed values for this property are: "IP_ADDRESS", "HOSTNAME"
        :type cpe_local_identifier_type: str

        :param static_routes:
            The value to assign to the static_routes property of this CreateIPSecConnectionDetails.
        :type static_routes: list[str]

        :param tunnel_configuration:
            The value to assign to the tunnel_configuration property of this CreateIPSecConnectionDetails.
        :type tunnel_configuration: list[oci.core.models.CreateIPSecConnectionTunnelDetails]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cpe_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'drg_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'cpe_local_identifier': 'str',
            'cpe_local_identifier_type': 'str',
            'static_routes': 'list[str]',
            'tunnel_configuration': 'list[CreateIPSecConnectionTunnelDetails]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cpe_id': 'cpeId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'freeform_tags': 'freeformTags',
            'cpe_local_identifier': 'cpeLocalIdentifier',
            'cpe_local_identifier_type': 'cpeLocalIdentifierType',
            'static_routes': 'staticRoutes',
            'tunnel_configuration': 'tunnelConfiguration'
        }

        self._compartment_id = None
        self._cpe_id = None
        self._defined_tags = None
        self._display_name = None
        self._drg_id = None
        self._freeform_tags = None
        self._cpe_local_identifier = None
        self._cpe_local_identifier_type = None
        self._static_routes = None
        self._tunnel_configuration = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateIPSecConnectionDetails.
        The `OCID`__ of the compartment to contain the IPSec connection.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIPSecConnectionDetails.
        The `OCID`__ of the compartment to contain the IPSec connection.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpe_id(self):
        """
        **[Required]** Gets the cpe_id of this CreateIPSecConnectionDetails.
        The `OCID`__ of the :class:`Cpe` object.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The cpe_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._cpe_id

    @cpe_id.setter
    def cpe_id(self, cpe_id):
        """
        Sets the cpe_id of this CreateIPSecConnectionDetails.
        The `OCID`__ of the :class:`Cpe` object.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param cpe_id: The cpe_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._cpe_id = cpe_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateIPSecConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateIPSecConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateIPSecConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateIPSecConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateIPSecConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateIPSecConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this CreateIPSecConnectionDetails.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateIPSecConnectionDetails.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_id: The drg_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateIPSecConnectionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateIPSecConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateIPSecConnectionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateIPSecConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def cpe_local_identifier(self):
        """
        Gets the cpe_local_identifier of this CreateIPSecConnectionDetails.
        Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the
        fully qualified domain name (FQDN)). The type of identifier you provide here must correspond
        to the value for `cpeLocalIdentifierType`.

        If you don't provide a value, the `ipAddress` attribute for the :class:`Cpe`
        object specified by `cpeId` is used as the `cpeLocalIdentifier`.

        For information about why you'd provide this value, see
        `If Your CPE Is Behind a NAT Device`__.

        Example IP address: `10.0.3.3`

        Example hostname: `cpe.example.com`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat


        :return: The cpe_local_identifier of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._cpe_local_identifier

    @cpe_local_identifier.setter
    def cpe_local_identifier(self, cpe_local_identifier):
        """
        Sets the cpe_local_identifier of this CreateIPSecConnectionDetails.
        Your identifier for your CPE device. Can be either an IP address or a hostname (specifically, the
        fully qualified domain name (FQDN)). The type of identifier you provide here must correspond
        to the value for `cpeLocalIdentifierType`.

        If you don't provide a value, the `ipAddress` attribute for the :class:`Cpe`
        object specified by `cpeId` is used as the `cpeLocalIdentifier`.

        For information about why you'd provide this value, see
        `If Your CPE Is Behind a NAT Device`__.

        Example IP address: `10.0.3.3`

        Example hostname: `cpe.example.com`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm#nat


        :param cpe_local_identifier: The cpe_local_identifier of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._cpe_local_identifier = cpe_local_identifier

    @property
    def cpe_local_identifier_type(self):
        """
        Gets the cpe_local_identifier_type of this CreateIPSecConnectionDetails.
        The type of identifier for your CPE device. The value you provide here must correspond to the value
        for `cpeLocalIdentifier`.

        Allowed values for this property are: "IP_ADDRESS", "HOSTNAME"


        :return: The cpe_local_identifier_type of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._cpe_local_identifier_type

    @cpe_local_identifier_type.setter
    def cpe_local_identifier_type(self, cpe_local_identifier_type):
        """
        Sets the cpe_local_identifier_type of this CreateIPSecConnectionDetails.
        The type of identifier for your CPE device. The value you provide here must correspond to the value
        for `cpeLocalIdentifier`.


        :param cpe_local_identifier_type: The cpe_local_identifier_type of this CreateIPSecConnectionDetails.
        :type: str
        """
        allowed_values = ["IP_ADDRESS", "HOSTNAME"]
        if not value_allowed_none_or_none_sentinel(cpe_local_identifier_type, allowed_values):
            raise ValueError(
                "Invalid value for `cpe_local_identifier_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._cpe_local_identifier_type = cpe_local_identifier_type

    @property
    def static_routes(self):
        """
        **[Required]** Gets the static_routes of this CreateIPSecConnectionDetails.
        Static routes to the CPE. A static route's CIDR must not be a
        multicast address or class E address.

        Used for routing a given IPSec tunnel's traffic only if the tunnel
        is using static routing. If you configure at least one tunnel to use static routing, then
        you must provide at least one valid static route. If you configure both
        tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
        For more information, see the important note in :class:`IPSecConnection`.

        The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions.
        See `IPv6 Addresses`__.

        Example: `10.0.1.0/24`

        Example: `2001:db8::/32`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The static_routes of this CreateIPSecConnectionDetails.
        :rtype: list[str]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this CreateIPSecConnectionDetails.
        Static routes to the CPE. A static route's CIDR must not be a
        multicast address or class E address.

        Used for routing a given IPSec tunnel's traffic only if the tunnel
        is using static routing. If you configure at least one tunnel to use static routing, then
        you must provide at least one valid static route. If you configure both
        tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.
        For more information, see the important note in :class:`IPSecConnection`.

        The CIDR can be either IPv4 or IPv6. IPv6 addressing is supported for all commercial and government regions.
        See `IPv6 Addresses`__.

        Example: `10.0.1.0/24`

        Example: `2001:db8::/32`

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param static_routes: The static_routes of this CreateIPSecConnectionDetails.
        :type: list[str]
        """
        self._static_routes = static_routes

    @property
    def tunnel_configuration(self):
        """
        Gets the tunnel_configuration of this CreateIPSecConnectionDetails.
        Information for creating the individual tunnels in the IPSec connection. You can provide a
        maximum of 2 `tunnelConfiguration` objects in the array (one for each of the
        two tunnels).


        :return: The tunnel_configuration of this CreateIPSecConnectionDetails.
        :rtype: list[oci.core.models.CreateIPSecConnectionTunnelDetails]
        """
        return self._tunnel_configuration

    @tunnel_configuration.setter
    def tunnel_configuration(self, tunnel_configuration):
        """
        Sets the tunnel_configuration of this CreateIPSecConnectionDetails.
        Information for creating the individual tunnels in the IPSec connection. You can provide a
        maximum of 2 `tunnelConfiguration` objects in the array (one for each of the
        two tunnels).


        :param tunnel_configuration: The tunnel_configuration of this CreateIPSecConnectionDetails.
        :type: list[oci.core.models.CreateIPSecConnectionTunnelDetails]
        """
        self._tunnel_configuration = tunnel_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
