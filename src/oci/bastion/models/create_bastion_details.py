# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBastionDetails(object):
    """
    The configuration details for a new bastion. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBastionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bastion_type:
            The value to assign to the bastion_type property of this CreateBastionDetails.
        :type bastion_type: str

        :param name:
            The value to assign to the name property of this CreateBastionDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBastionDetails.
        :type compartment_id: str

        :param target_subnet_id:
            The value to assign to the target_subnet_id property of this CreateBastionDetails.
        :type target_subnet_id: str

        :param phone_book_entry:
            The value to assign to the phone_book_entry property of this CreateBastionDetails.
        :type phone_book_entry: str

        :param static_jump_host_ip_addresses:
            The value to assign to the static_jump_host_ip_addresses property of this CreateBastionDetails.
        :type static_jump_host_ip_addresses: list[str]

        :param client_cidr_block_allow_list:
            The value to assign to the client_cidr_block_allow_list property of this CreateBastionDetails.
        :type client_cidr_block_allow_list: list[str]

        :param max_session_ttl_in_seconds:
            The value to assign to the max_session_ttl_in_seconds property of this CreateBastionDetails.
        :type max_session_ttl_in_seconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBastionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBastionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'bastion_type': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'target_subnet_id': 'str',
            'phone_book_entry': 'str',
            'static_jump_host_ip_addresses': 'list[str]',
            'client_cidr_block_allow_list': 'list[str]',
            'max_session_ttl_in_seconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'bastion_type': 'bastionType',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'target_subnet_id': 'targetSubnetId',
            'phone_book_entry': 'phoneBookEntry',
            'static_jump_host_ip_addresses': 'staticJumpHostIpAddresses',
            'client_cidr_block_allow_list': 'clientCidrBlockAllowList',
            'max_session_ttl_in_seconds': 'maxSessionTtlInSeconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._bastion_type = None
        self._name = None
        self._compartment_id = None
        self._target_subnet_id = None
        self._phone_book_entry = None
        self._static_jump_host_ip_addresses = None
        self._client_cidr_block_allow_list = None
        self._max_session_ttl_in_seconds = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def bastion_type(self):
        """
        **[Required]** Gets the bastion_type of this CreateBastionDetails.
        The type of bastion. Use `standard`.


        :return: The bastion_type of this CreateBastionDetails.
        :rtype: str
        """
        return self._bastion_type

    @bastion_type.setter
    def bastion_type(self, bastion_type):
        """
        Sets the bastion_type of this CreateBastionDetails.
        The type of bastion. Use `standard`.


        :param bastion_type: The bastion_type of this CreateBastionDetails.
        :type: str
        """
        self._bastion_type = bastion_type

    @property
    def name(self):
        """
        Gets the name of this CreateBastionDetails.
        The name of the bastion, which can't be changed after creation.


        :return: The name of this CreateBastionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateBastionDetails.
        The name of the bastion, which can't be changed after creation.


        :param name: The name of this CreateBastionDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateBastionDetails.
        The unique identifier (OCID) of the compartment where the bastion is located.


        :return: The compartment_id of this CreateBastionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBastionDetails.
        The unique identifier (OCID) of the compartment where the bastion is located.


        :param compartment_id: The compartment_id of this CreateBastionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_subnet_id(self):
        """
        **[Required]** Gets the target_subnet_id of this CreateBastionDetails.
        The unique identifier (OCID) of the subnet that the bastion connects to.


        :return: The target_subnet_id of this CreateBastionDetails.
        :rtype: str
        """
        return self._target_subnet_id

    @target_subnet_id.setter
    def target_subnet_id(self, target_subnet_id):
        """
        Sets the target_subnet_id of this CreateBastionDetails.
        The unique identifier (OCID) of the subnet that the bastion connects to.


        :param target_subnet_id: The target_subnet_id of this CreateBastionDetails.
        :type: str
        """
        self._target_subnet_id = target_subnet_id

    @property
    def phone_book_entry(self):
        """
        Gets the phone_book_entry of this CreateBastionDetails.
        The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.


        :return: The phone_book_entry of this CreateBastionDetails.
        :rtype: str
        """
        return self._phone_book_entry

    @phone_book_entry.setter
    def phone_book_entry(self, phone_book_entry):
        """
        Sets the phone_book_entry of this CreateBastionDetails.
        The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.


        :param phone_book_entry: The phone_book_entry of this CreateBastionDetails.
        :type: str
        """
        self._phone_book_entry = phone_book_entry

    @property
    def static_jump_host_ip_addresses(self):
        """
        Gets the static_jump_host_ip_addresses of this CreateBastionDetails.
        A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.


        :return: The static_jump_host_ip_addresses of this CreateBastionDetails.
        :rtype: list[str]
        """
        return self._static_jump_host_ip_addresses

    @static_jump_host_ip_addresses.setter
    def static_jump_host_ip_addresses(self, static_jump_host_ip_addresses):
        """
        Sets the static_jump_host_ip_addresses of this CreateBastionDetails.
        A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.


        :param static_jump_host_ip_addresses: The static_jump_host_ip_addresses of this CreateBastionDetails.
        :type: list[str]
        """
        self._static_jump_host_ip_addresses = static_jump_host_ip_addresses

    @property
    def client_cidr_block_allow_list(self):
        """
        Gets the client_cidr_block_allow_list of this CreateBastionDetails.
        A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.


        :return: The client_cidr_block_allow_list of this CreateBastionDetails.
        :rtype: list[str]
        """
        return self._client_cidr_block_allow_list

    @client_cidr_block_allow_list.setter
    def client_cidr_block_allow_list(self, client_cidr_block_allow_list):
        """
        Sets the client_cidr_block_allow_list of this CreateBastionDetails.
        A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.


        :param client_cidr_block_allow_list: The client_cidr_block_allow_list of this CreateBastionDetails.
        :type: list[str]
        """
        self._client_cidr_block_allow_list = client_cidr_block_allow_list

    @property
    def max_session_ttl_in_seconds(self):
        """
        Gets the max_session_ttl_in_seconds of this CreateBastionDetails.
        The maximum amount of time that any session on the bastion can remain active.


        :return: The max_session_ttl_in_seconds of this CreateBastionDetails.
        :rtype: int
        """
        return self._max_session_ttl_in_seconds

    @max_session_ttl_in_seconds.setter
    def max_session_ttl_in_seconds(self, max_session_ttl_in_seconds):
        """
        Sets the max_session_ttl_in_seconds of this CreateBastionDetails.
        The maximum amount of time that any session on the bastion can remain active.


        :param max_session_ttl_in_seconds: The max_session_ttl_in_seconds of this CreateBastionDetails.
        :type: int
        """
        self._max_session_ttl_in_seconds = max_session_ttl_in_seconds

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBastionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateBastionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBastionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateBastionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBastionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateBastionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBastionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateBastionDetails.
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
