# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DistributedDbConnectionString(object):
    """
    Details of Globally distributed database connection String.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DistributedDbConnectionString object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param all_connection_strings:
            The value to assign to the all_connection_strings property of this DistributedDbConnectionString.
        :type all_connection_strings: dict(str, str)

        """
        self.swagger_types = {
            'all_connection_strings': 'dict(str, str)'
        }
        self.attribute_map = {
            'all_connection_strings': 'allConnectionStrings'
        }
        self._all_connection_strings = None

    @property
    def all_connection_strings(self):
        """
        **[Required]** Gets the all_connection_strings of this DistributedDbConnectionString.
        Collection of connection strings.


        :return: The all_connection_strings of this DistributedDbConnectionString.
        :rtype: dict(str, str)
        """
        return self._all_connection_strings

    @all_connection_strings.setter
    def all_connection_strings(self, all_connection_strings):
        """
        Sets the all_connection_strings of this DistributedDbConnectionString.
        Collection of connection strings.


        :param all_connection_strings: The all_connection_strings of this DistributedDbConnectionString.
        :type: dict(str, str)
        """
        self._all_connection_strings = all_connection_strings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
