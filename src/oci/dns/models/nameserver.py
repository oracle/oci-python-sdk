# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Nameserver(object):
    """
    A server that has been set up to answer DNS queries for a zone.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Nameserver object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this Nameserver.
        :type hostname: str

        """
        self.swagger_types = {
            'hostname': 'str'
        }

        self.attribute_map = {
            'hostname': 'hostname'
        }

        self._hostname = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this Nameserver.
        The hostname of the nameserver.


        :return: The hostname of this Nameserver.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this Nameserver.
        The hostname of the nameserver.


        :param hostname: The hostname of this Nameserver.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
