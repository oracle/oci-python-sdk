# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PdbStatusDetails(object):
    """
    The number and status of PDBs in a Container Database.
    """

    #: A constant which can be used with the status property of a PdbStatusDetails.
    #: This constant has a value of "UP"
    STATUS_UP = "UP"

    #: A constant which can be used with the status property of a PdbStatusDetails.
    #: This constant has a value of "DOWN"
    STATUS_DOWN = "DOWN"

    #: A constant which can be used with the status property of a PdbStatusDetails.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new PdbStatusDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this PdbStatusDetails.
            Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param count:
            The value to assign to the count property of this PdbStatusDetails.
        :type count: int

        """
        self.swagger_types = {
            'status': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'status': 'status',
            'count': 'count'
        }

        self._status = None
        self._count = None

    @property
    def status(self):
        """
        Gets the status of this PdbStatusDetails.
        The status of the PDBs with this count.

        Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this PdbStatusDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PdbStatusDetails.
        The status of the PDBs with this count.


        :param status: The status of this PdbStatusDetails.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def count(self):
        """
        Gets the count of this PdbStatusDetails.
        The number of PDBs with this status.


        :return: The count of this PdbStatusDetails.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PdbStatusDetails.
        The number of PDBs with this status.


        :param count: The count of this PdbStatusDetails.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
