# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessPolicyRule(object):
    """
    Access policy rule.
    """

    #: A constant which can be used with the action property of a AccessPolicyRule.
    #: This constant has a value of "ALLOW"
    ACTION_ALLOW = "ALLOW"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessPolicyRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this AccessPolicyRule.
            Allowed values for this property are: "ALLOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param source:
            The value to assign to the source property of this AccessPolicyRule.
        :type source: oci.service_mesh.models.AccessPolicyTarget

        :param destination:
            The value to assign to the destination property of this AccessPolicyRule.
        :type destination: oci.service_mesh.models.AccessPolicyTarget

        """
        self.swagger_types = {
            'action': 'str',
            'source': 'AccessPolicyTarget',
            'destination': 'AccessPolicyTarget'
        }

        self.attribute_map = {
            'action': 'action',
            'source': 'source',
            'destination': 'destination'
        }

        self._action = None
        self._source = None
        self._destination = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this AccessPolicyRule.
        Action for the traffic between the source and the destination.

        Allowed values for this property are: "ALLOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this AccessPolicyRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AccessPolicyRule.
        Action for the traffic between the source and the destination.


        :param action: The action of this AccessPolicyRule.
        :type: str
        """
        allowed_values = ["ALLOW"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def source(self):
        """
        **[Required]** Gets the source of this AccessPolicyRule.

        :return: The source of this AccessPolicyRule.
        :rtype: oci.service_mesh.models.AccessPolicyTarget
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this AccessPolicyRule.

        :param source: The source of this AccessPolicyRule.
        :type: oci.service_mesh.models.AccessPolicyTarget
        """
        self._source = source

    @property
    def destination(self):
        """
        **[Required]** Gets the destination of this AccessPolicyRule.

        :return: The destination of this AccessPolicyRule.
        :rtype: oci.service_mesh.models.AccessPolicyTarget
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this AccessPolicyRule.

        :param destination: The destination of this AccessPolicyRule.
        :type: oci.service_mesh.models.AccessPolicyTarget
        """
        self._destination = destination

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
