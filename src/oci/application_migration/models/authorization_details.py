# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthorizationDetails(object):
    """
    Details of the source environment from which you want to migrate applications to Oracle Cloud Infrastructure. It also contains access
    credentials.
    """

    #: A constant which can be used with the type property of a AuthorizationDetails.
    #: This constant has a value of "OCIC"
    TYPE_OCIC = "OCIC"

    #: A constant which can be used with the type property of a AuthorizationDetails.
    #: This constant has a value of "INTERNAL_COMPUTE"
    TYPE_INTERNAL_COMPUTE = "INTERNAL_COMPUTE"

    #: A constant which can be used with the type property of a AuthorizationDetails.
    #: This constant has a value of "OCC"
    TYPE_OCC = "OCC"

    #: A constant which can be used with the type property of a AuthorizationDetails.
    #: This constant has a value of "OCIC_IDCS"
    TYPE_OCIC_IDCS = "OCIC_IDCS"

    #: A constant which can be used with the type property of a AuthorizationDetails.
    #: This constant has a value of "IMPORT"
    TYPE_IMPORT = "IMPORT"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthorizationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.application_migration.models.OccAuthorizationDetails`
        * :class:`~oci.application_migration.models.InternalAuthorizationDetails`
        * :class:`~oci.application_migration.models.OcicAuthorizationTokenDetails`
        * :class:`~oci.application_migration.models.OcicAuthorizationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AuthorizationDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS", "IMPORT"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'OCC':
            return 'OccAuthorizationDetails'

        if type == 'INTERNAL_COMPUTE':
            return 'InternalAuthorizationDetails'

        if type == 'OCIC_IDCS':
            return 'OcicAuthorizationTokenDetails'

        if type == 'OCIC':
            return 'OcicAuthorizationDetails'
        else:
            return 'AuthorizationDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AuthorizationDetails.
        Type of the source environment from which you are migrating applications to Oracle Cloud Infrastructure.

        Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS", "IMPORT"


        :return: The type of this AuthorizationDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AuthorizationDetails.
        Type of the source environment from which you are migrating applications to Oracle Cloud Infrastructure.


        :param type: The type of this AuthorizationDetails.
        :type: str
        """
        allowed_values = ["OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS", "IMPORT"]
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
