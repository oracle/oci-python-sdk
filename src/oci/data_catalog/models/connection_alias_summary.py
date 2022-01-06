# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionAliasSummary(object):
    """
    Summary representation of database aliases parsed from the file metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionAliasSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param alias_name:
            The value to assign to the alias_name property of this ConnectionAliasSummary.
        :type alias_name: str

        :param alias_details:
            The value to assign to the alias_details property of this ConnectionAliasSummary.
        :type alias_details: str

        """
        self.swagger_types = {
            'alias_name': 'str',
            'alias_details': 'str'
        }

        self.attribute_map = {
            'alias_name': 'aliasName',
            'alias_details': 'aliasDetails'
        }

        self._alias_name = None
        self._alias_details = None

    @property
    def alias_name(self):
        """
        **[Required]** Gets the alias_name of this ConnectionAliasSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The alias_name of this ConnectionAliasSummary.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """
        Sets the alias_name of this ConnectionAliasSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param alias_name: The alias_name of this ConnectionAliasSummary.
        :type: str
        """
        self._alias_name = alias_name

    @property
    def alias_details(self):
        """
        Gets the alias_details of this ConnectionAliasSummary.
        The description about the database alias parsed from the file metadata.


        :return: The alias_details of this ConnectionAliasSummary.
        :rtype: str
        """
        return self._alias_details

    @alias_details.setter
    def alias_details(self, alias_details):
        """
        Sets the alias_details of this ConnectionAliasSummary.
        The description about the database alias parsed from the file metadata.


        :param alias_details: The alias_details of this ConnectionAliasSummary.
        :type: str
        """
        self._alias_details = alias_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
