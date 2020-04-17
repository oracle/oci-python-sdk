# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePublicIpDetails(object):
    """
    CreatePublicIpDetails model.
    """

    #: A constant which can be used with the lifetime property of a CreatePublicIpDetails.
    #: This constant has a value of "EPHEMERAL"
    LIFETIME_EPHEMERAL = "EPHEMERAL"

    #: A constant which can be used with the lifetime property of a CreatePublicIpDetails.
    #: This constant has a value of "RESERVED"
    LIFETIME_RESERVED = "RESERVED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePublicIpDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePublicIpDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePublicIpDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreatePublicIpDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePublicIpDetails.
        :type freeform_tags: dict(str, str)

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
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'lifetime': 'str',
            'private_ip_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'lifetime': 'lifetime',
            'private_ip_id': 'privateIpId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
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
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePublicIpDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreatePublicIpDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePublicIpDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreatePublicIpDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

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
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePublicIpDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreatePublicIpDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePublicIpDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreatePublicIpDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def lifetime(self):
        """
        **[Required]** Gets the lifetime of this CreatePublicIpDetails.
        Defines when the public IP is deleted and released back to the Oracle Cloud
        Infrastructure public IP pool. For more information, see
        `Public IP Addresses`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm

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

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingpublicIPs.htm


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
