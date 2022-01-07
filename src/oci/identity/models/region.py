# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Region(object):
    """
    A localized geographic area, such as Phoenix, AZ. Oracle Cloud Infrastructure is hosted in regions and Availability
    Domains. A region is composed of several Availability Domains. An Availability Domain is one or more data centers
    located within a region. For more information, see `Regions and Availability Domains`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Region object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Region.
        :type key: str

        :param name:
            The value to assign to the name property of this Region.
        :type name: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name'
        }

        self._key = None
        self._name = None

    @property
    def key(self):
        """
        Gets the key of this Region.
        The key of the region. See `Regions and Availability Domains`__ for
        the full list of supported 3-letter region codes.

        Example: `PHX`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The key of this Region.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Region.
        The key of the region. See `Regions and Availability Domains`__ for
        the full list of supported 3-letter region codes.

        Example: `PHX`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :param key: The key of this Region.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this Region.
        The name of the region. See `Regions and Availability Domains`__
        for the full list of supported region names.

        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The name of this Region.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Region.
        The name of the region. See `Regions and Availability Domains`__
        for the full list of supported region names.

        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :param name: The name of this Region.
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
