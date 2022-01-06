# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBastionDetails(object):
    """
    The configuration to update on an existing bastion.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBastionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param max_session_ttl_in_seconds:
            The value to assign to the max_session_ttl_in_seconds property of this UpdateBastionDetails.
        :type max_session_ttl_in_seconds: int

        :param static_jump_host_ip_addresses:
            The value to assign to the static_jump_host_ip_addresses property of this UpdateBastionDetails.
        :type static_jump_host_ip_addresses: list[str]

        :param client_cidr_block_allow_list:
            The value to assign to the client_cidr_block_allow_list property of this UpdateBastionDetails.
        :type client_cidr_block_allow_list: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBastionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBastionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'max_session_ttl_in_seconds': 'int',
            'static_jump_host_ip_addresses': 'list[str]',
            'client_cidr_block_allow_list': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'max_session_ttl_in_seconds': 'maxSessionTtlInSeconds',
            'static_jump_host_ip_addresses': 'staticJumpHostIpAddresses',
            'client_cidr_block_allow_list': 'clientCidrBlockAllowList',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._max_session_ttl_in_seconds = None
        self._static_jump_host_ip_addresses = None
        self._client_cidr_block_allow_list = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def max_session_ttl_in_seconds(self):
        """
        Gets the max_session_ttl_in_seconds of this UpdateBastionDetails.
        The maximum amount of time that any session on the bastion can remain active.


        :return: The max_session_ttl_in_seconds of this UpdateBastionDetails.
        :rtype: int
        """
        return self._max_session_ttl_in_seconds

    @max_session_ttl_in_seconds.setter
    def max_session_ttl_in_seconds(self, max_session_ttl_in_seconds):
        """
        Sets the max_session_ttl_in_seconds of this UpdateBastionDetails.
        The maximum amount of time that any session on the bastion can remain active.


        :param max_session_ttl_in_seconds: The max_session_ttl_in_seconds of this UpdateBastionDetails.
        :type: int
        """
        self._max_session_ttl_in_seconds = max_session_ttl_in_seconds

    @property
    def static_jump_host_ip_addresses(self):
        """
        Gets the static_jump_host_ip_addresses of this UpdateBastionDetails.
        A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.


        :return: The static_jump_host_ip_addresses of this UpdateBastionDetails.
        :rtype: list[str]
        """
        return self._static_jump_host_ip_addresses

    @static_jump_host_ip_addresses.setter
    def static_jump_host_ip_addresses(self, static_jump_host_ip_addresses):
        """
        Sets the static_jump_host_ip_addresses of this UpdateBastionDetails.
        A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.


        :param static_jump_host_ip_addresses: The static_jump_host_ip_addresses of this UpdateBastionDetails.
        :type: list[str]
        """
        self._static_jump_host_ip_addresses = static_jump_host_ip_addresses

    @property
    def client_cidr_block_allow_list(self):
        """
        Gets the client_cidr_block_allow_list of this UpdateBastionDetails.
        A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.


        :return: The client_cidr_block_allow_list of this UpdateBastionDetails.
        :rtype: list[str]
        """
        return self._client_cidr_block_allow_list

    @client_cidr_block_allow_list.setter
    def client_cidr_block_allow_list(self, client_cidr_block_allow_list):
        """
        Sets the client_cidr_block_allow_list of this UpdateBastionDetails.
        A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.


        :param client_cidr_block_allow_list: The client_cidr_block_allow_list of this UpdateBastionDetails.
        :type: list[str]
        """
        self._client_cidr_block_allow_list = client_cidr_block_allow_list

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBastionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateBastionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBastionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateBastionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBastionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateBastionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBastionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateBastionDetails.
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
