# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbFleetDiscoveryFilter(object):
    """
    Possible Discovery filters for Database targets.
    """

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "COMPARTMENT_ID"
    TYPE_COMPARTMENT_ID = "COMPARTMENT_ID"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "VERSION"
    TYPE_VERSION = "VERSION"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "DB_NAME"
    TYPE_DB_NAME = "DB_NAME"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "DB_UNIQUE_NAME"
    TYPE_DB_UNIQUE_NAME = "DB_UNIQUE_NAME"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "DB_HOME_NAME"
    TYPE_DB_HOME_NAME = "DB_HOME_NAME"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "FREEFORM_TAG"
    TYPE_FREEFORM_TAG = "FREEFORM_TAG"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "DEFINED_TAG"
    TYPE_DEFINED_TAG = "DEFINED_TAG"

    #: A constant which can be used with the type property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "RESOURCE_ID"
    TYPE_RESOURCE_ID = "RESOURCE_ID"

    #: A constant which can be used with the mode property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "INCLUDE"
    MODE_INCLUDE = "INCLUDE"

    #: A constant which can be used with the mode property of a DbFleetDiscoveryFilter.
    #: This constant has a value of "EXCLUDE"
    MODE_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new DbFleetDiscoveryFilter object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.DbDefinedTagsFilter`
        * :class:`~oci.fleet_software_update.models.DbUniqueNameFilter`
        * :class:`~oci.fleet_software_update.models.DbVersionFilter`
        * :class:`~oci.fleet_software_update.models.DbResourceIdFilter`
        * :class:`~oci.fleet_software_update.models.DbHomeNameFilter`
        * :class:`~oci.fleet_software_update.models.DbCompartmentIdFilter`
        * :class:`~oci.fleet_software_update.models.DbNameFilter`
        * :class:`~oci.fleet_software_update.models.DbFreeformTagsFilter`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DbFleetDiscoveryFilter.
            Allowed values for this property are: "COMPARTMENT_ID", "VERSION", "DB_NAME", "DB_UNIQUE_NAME", "DB_HOME_NAME", "FREEFORM_TAG", "DEFINED_TAG", "RESOURCE_ID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param mode:
            The value to assign to the mode property of this DbFleetDiscoveryFilter.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        """
        self.swagger_types = {
            'type': 'str',
            'mode': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'mode': 'mode'
        }
        self._type = None
        self._mode = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'DEFINED_TAG':
            return 'DbDefinedTagsFilter'

        if type == 'DB_UNIQUE_NAME':
            return 'DbUniqueNameFilter'

        if type == 'VERSION':
            return 'DbVersionFilter'

        if type == 'RESOURCE_ID':
            return 'DbResourceIdFilter'

        if type == 'DB_HOME_NAME':
            return 'DbHomeNameFilter'

        if type == 'COMPARTMENT_ID':
            return 'DbCompartmentIdFilter'

        if type == 'DB_NAME':
            return 'DbNameFilter'

        if type == 'FREEFORM_TAG':
            return 'DbFreeformTagsFilter'
        else:
            return 'DbFleetDiscoveryFilter'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DbFleetDiscoveryFilter.
        Type of filters supported for Database targets discovery.

        Allowed values for this property are: "COMPARTMENT_ID", "VERSION", "DB_NAME", "DB_UNIQUE_NAME", "DB_HOME_NAME", "FREEFORM_TAG", "DEFINED_TAG", "RESOURCE_ID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DbFleetDiscoveryFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DbFleetDiscoveryFilter.
        Type of filters supported for Database targets discovery.


        :param type: The type of this DbFleetDiscoveryFilter.
        :type: str
        """
        allowed_values = ["COMPARTMENT_ID", "VERSION", "DB_NAME", "DB_UNIQUE_NAME", "DB_HOME_NAME", "FREEFORM_TAG", "DEFINED_TAG", "RESOURCE_ID"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def mode(self):
        """
        Gets the mode of this DbFleetDiscoveryFilter.
        INCLUDE or EXCLUDE the filter results in the discovery for DB targets.
        Supported for 'FSUCOLLECTION' RESOURCE_ID filter only.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this DbFleetDiscoveryFilter.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this DbFleetDiscoveryFilter.
        INCLUDE or EXCLUDE the filter results in the discovery for DB targets.
        Supported for 'FSUCOLLECTION' RESOURCE_ID filter only.


        :param mode: The mode of this DbFleetDiscoveryFilter.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
