# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetadataRemap(object):
    """
    Defines remapping to be applied to objects as they are processed.
    Refer to `METADATA_REMAP Procedure `__

    __ https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D
    """

    #: A constant which can be used with the type property of a MetadataRemap.
    #: This constant has a value of "SCHEMA"
    TYPE_SCHEMA = "SCHEMA"

    #: A constant which can be used with the type property of a MetadataRemap.
    #: This constant has a value of "TABLESPACE"
    TYPE_TABLESPACE = "TABLESPACE"

    #: A constant which can be used with the type property of a MetadataRemap.
    #: This constant has a value of "DATAFILE"
    TYPE_DATAFILE = "DATAFILE"

    #: A constant which can be used with the type property of a MetadataRemap.
    #: This constant has a value of "TABLE"
    TYPE_TABLE = "TABLE"

    def __init__(self, **kwargs):
        """
        Initializes a new MetadataRemap object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this MetadataRemap.
            Allowed values for this property are: "SCHEMA", "TABLESPACE", "DATAFILE", "TABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param old_value:
            The value to assign to the old_value property of this MetadataRemap.
        :type old_value: str

        :param new_value:
            The value to assign to the new_value property of this MetadataRemap.
        :type new_value: str

        """
        self.swagger_types = {
            'type': 'str',
            'old_value': 'str',
            'new_value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'old_value': 'oldValue',
            'new_value': 'newValue'
        }

        self._type = None
        self._old_value = None
        self._new_value = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MetadataRemap.
        Type of remap. Refer to `METADATA_REMAP Procedure `__

        __ https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D

        Allowed values for this property are: "SCHEMA", "TABLESPACE", "DATAFILE", "TABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MetadataRemap.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MetadataRemap.
        Type of remap. Refer to `METADATA_REMAP Procedure `__

        __ https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D


        :param type: The type of this MetadataRemap.
        :type: str
        """
        allowed_values = ["SCHEMA", "TABLESPACE", "DATAFILE", "TABLE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def old_value(self):
        """
        **[Required]** Gets the old_value of this MetadataRemap.
        Specifies the value which needs to be reset.


        :return: The old_value of this MetadataRemap.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """
        Sets the old_value of this MetadataRemap.
        Specifies the value which needs to be reset.


        :param old_value: The old_value of this MetadataRemap.
        :type: str
        """
        self._old_value = old_value

    @property
    def new_value(self):
        """
        **[Required]** Gets the new_value of this MetadataRemap.
        Specifies the new value that oldValue should be translated into.


        :return: The new_value of this MetadataRemap.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """
        Sets the new_value of this MetadataRemap.
        Specifies the new value that oldValue should be translated into.


        :param new_value: The new_value of this MetadataRemap.
        :type: str
        """
        self._new_value = new_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
