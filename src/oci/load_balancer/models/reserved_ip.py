# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReservedIP(object):
    """
    ReservedIP model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReservedIP object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ReservedIP.
        :type id: str

        """
        self.swagger_types = {
            'id': 'str'
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = None

    @property
    def id(self):
        """
        Gets the id of this ReservedIP.

        :return: The id of this ReservedIP.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReservedIP.

        :param id: The id of this ReservedIP.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
