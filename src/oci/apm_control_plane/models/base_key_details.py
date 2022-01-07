# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseKeyDetails(object):
    """
    The information about a Data Key.
    """

    #: A constant which can be used with the type property of a BaseKeyDetails.
    #: This constant has a value of "PRIVATE"
    TYPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the type property of a BaseKeyDetails.
    #: This constant has a value of "PUBLIC"
    TYPE_PUBLIC = "PUBLIC"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this BaseKeyDetails.
        :type name: str

        :param type:
            The value to assign to the type property of this BaseKeyDetails.
            Allowed values for this property are: "PRIVATE", "PUBLIC"
        :type type: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type'
        }

        self._name = None
        self._type = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BaseKeyDetails.
        Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.


        :return: The name of this BaseKeyDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BaseKeyDetails.
        Name of the Data Key. The name uniquely identifies a Data Key within an APM domain.


        :param name: The name of this BaseKeyDetails.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this BaseKeyDetails.
        Type of the Data Key.

        Allowed values for this property are: "PRIVATE", "PUBLIC"


        :return: The type of this BaseKeyDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BaseKeyDetails.
        Type of the Data Key.


        :param type: The type of this BaseKeyDetails.
        :type: str
        """
        allowed_values = ["PRIVATE", "PUBLIC"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
