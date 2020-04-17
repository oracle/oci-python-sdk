# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FullyQualifiedScope(object):
    """
    FullyQualifiedScope model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FullyQualifiedScope object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audience:
            The value to assign to the audience property of this FullyQualifiedScope.
        :type audience: str

        :param scope:
            The value to assign to the scope property of this FullyQualifiedScope.
        :type scope: str

        """
        self.swagger_types = {
            'audience': 'str',
            'scope': 'str'
        }

        self.attribute_map = {
            'audience': 'audience',
            'scope': 'scope'
        }

        self._audience = None
        self._scope = None

    @property
    def audience(self):
        """
        **[Required]** Gets the audience of this FullyQualifiedScope.
        Audience for the given scope context.


        :return: The audience of this FullyQualifiedScope.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """
        Sets the audience of this FullyQualifiedScope.
        Audience for the given scope context.


        :param audience: The audience of this FullyQualifiedScope.
        :type: str
        """
        self._audience = audience

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this FullyQualifiedScope.
        Allowed permission scope for the given context.


        :return: The scope of this FullyQualifiedScope.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this FullyQualifiedScope.
        Allowed permission scope for the given context.


        :param scope: The scope of this FullyQualifiedScope.
        :type: str
        """
        self._scope = scope

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
