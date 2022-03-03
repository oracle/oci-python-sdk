# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationObjectSummary(object):
    """
    Database objects to include or exclude from migration
    """

    #: A constant which can be used with the object_status property of a MigrationObjectSummary.
    #: This constant has a value of "EXCLUDE"
    OBJECT_STATUS_EXCLUDE = "EXCLUDE"

    #: A constant which can be used with the object_status property of a MigrationObjectSummary.
    #: This constant has a value of "INCLUDE"
    OBJECT_STATUS_INCLUDE = "INCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationObjectSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param owner:
            The value to assign to the owner property of this MigrationObjectSummary.
        :type owner: str

        :param object_name:
            The value to assign to the object_name property of this MigrationObjectSummary.
        :type object_name: str

        :param type:
            The value to assign to the type property of this MigrationObjectSummary.
        :type type: str

        :param object_status:
            The value to assign to the object_status property of this MigrationObjectSummary.
            Allowed values for this property are: "EXCLUDE", "INCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type object_status: str

        """
        self.swagger_types = {
            'owner': 'str',
            'object_name': 'str',
            'type': 'str',
            'object_status': 'str'
        }

        self.attribute_map = {
            'owner': 'owner',
            'object_name': 'objectName',
            'type': 'type',
            'object_status': 'objectStatus'
        }

        self._owner = None
        self._object_name = None
        self._type = None
        self._object_status = None

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this MigrationObjectSummary.
        Owner of the object (regular expression is allowed)


        :return: The owner of this MigrationObjectSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this MigrationObjectSummary.
        Owner of the object (regular expression is allowed)


        :param owner: The owner of this MigrationObjectSummary.
        :type: str
        """
        self._owner = owner

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this MigrationObjectSummary.
        Name of the object (regular expression is allowed)


        :return: The object_name of this MigrationObjectSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this MigrationObjectSummary.
        Name of the object (regular expression is allowed)


        :param object_name: The object_name of this MigrationObjectSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def type(self):
        """
        Gets the type of this MigrationObjectSummary.
        Type of object to exclude.
        If not specified, matching owners and object names of type TABLE would be excluded.


        :return: The type of this MigrationObjectSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MigrationObjectSummary.
        Type of object to exclude.
        If not specified, matching owners and object names of type TABLE would be excluded.


        :param type: The type of this MigrationObjectSummary.
        :type: str
        """
        self._type = type

    @property
    def object_status(self):
        """
        Gets the object_status of this MigrationObjectSummary.
        Object status.

        Allowed values for this property are: "EXCLUDE", "INCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The object_status of this MigrationObjectSummary.
        :rtype: str
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this MigrationObjectSummary.
        Object status.


        :param object_status: The object_status of this MigrationObjectSummary.
        :type: str
        """
        allowed_values = ["EXCLUDE", "INCLUDE"]
        if not value_allowed_none_or_none_sentinel(object_status, allowed_values):
            object_status = 'UNKNOWN_ENUM_VALUE'
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
