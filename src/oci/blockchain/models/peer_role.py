# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeerRole(object):
    """
    Peer role
    """

    #: A constant which can be used with the role property of a PeerRole.
    #: This constant has a value of "MEMBER"
    ROLE_MEMBER = "MEMBER"

    #: A constant which can be used with the role property of a PeerRole.
    #: This constant has a value of "ADMIN"
    ROLE_ADMIN = "ADMIN"

    def __init__(self, **kwargs):
        """
        Initializes a new PeerRole object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this PeerRole.
            Allowed values for this property are: "MEMBER", "ADMIN"
        :type role: str

        """
        self.swagger_types = {
            'role': 'str'
        }

        self.attribute_map = {
            'role': 'role'
        }

        self._role = None

    @property
    def role(self):
        """
        Gets the role of this PeerRole.
        Peer role names

        Allowed values for this property are: "MEMBER", "ADMIN"


        :return: The role of this PeerRole.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this PeerRole.
        Peer role names


        :param role: The role of this PeerRole.
        :type: str
        """
        allowed_values = ["MEMBER", "ADMIN"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                "Invalid value for `role`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
