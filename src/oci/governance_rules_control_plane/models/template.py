# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Template(object):
    """
    Template object for the governance rule. It could be of type QUOTA, TAG or REGION_RESTRICTION.
    """

    #: A constant which can be used with the type property of a Template.
    #: This constant has a value of "QUOTA"
    TYPE_QUOTA = "QUOTA"

    #: A constant which can be used with the type property of a Template.
    #: This constant has a value of "TAG"
    TYPE_TAG = "TAG"

    #: A constant which can be used with the type property of a Template.
    #: This constant has a value of "ALLOWED_REGIONS"
    TYPE_ALLOWED_REGIONS = "ALLOWED_REGIONS"

    def __init__(self, **kwargs):
        """
        Initializes a new Template object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.governance_rules_control_plane.models.TagTemplate`
        * :class:`~oci.governance_rules_control_plane.models.QuotaTemplate`
        * :class:`~oci.governance_rules_control_plane.models.AllowedRegionsTemplate`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Template.
            Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
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

        if type == 'TAG':
            return 'TagTemplate'

        if type == 'QUOTA':
            return 'QuotaTemplate'

        if type == 'ALLOWED_REGIONS':
            return 'AllowedRegionsTemplate'
        else:
            return 'Template'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Template.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`

        Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Template.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Template.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`


        :param type: The type of this Template.
        :type: str
        """
        allowed_values = ["QUOTA", "TAG", "ALLOWED_REGIONS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
