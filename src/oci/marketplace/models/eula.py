# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Eula(object):
    """
    A base object for all types of End User Licenses
    """

    #: A constant which can be used with the eula_type property of a Eula.
    #: This constant has a value of "TEXT"
    EULA_TYPE_TEXT = "TEXT"

    def __init__(self, **kwargs):
        """
        Initializes a new Eula object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace.models.TextBasedEula`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param eula_type:
            The value to assign to the eula_type property of this Eula.
            Allowed values for this property are: "TEXT"
        :type eula_type: str

        """
        self.swagger_types = {
            'eula_type': 'str'
        }

        self.attribute_map = {
            'eula_type': 'eulaType'
        }

        self._eula_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['eulaType']

        if type == 'TEXT':
            return 'TextBasedEula'
        else:
            return 'Eula'

    @property
    def eula_type(self):
        """
        **[Required]** Gets the eula_type of this Eula.
        the specified eula's type

        Allowed values for this property are: "TEXT"


        :return: The eula_type of this Eula.
        :rtype: str
        """
        return self._eula_type

    @eula_type.setter
    def eula_type(self, eula_type):
        """
        Sets the eula_type of this Eula.
        the specified eula's type


        :param eula_type: The eula_type of this Eula.
        :type: str
        """
        allowed_values = ["TEXT"]
        if not value_allowed_none_or_none_sentinel(eula_type, allowed_values):
            raise ValueError(
                "Invalid value for `eula_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._eula_type = eula_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
