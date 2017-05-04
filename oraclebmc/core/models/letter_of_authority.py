# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class LetterOfAuthority(object):

    def __init__(self):

        self.swagger_types = {
            'circuit_type': 'str',
            'cross_connect_id': 'str',
            'facility_location': 'str',
            'port_name': 'str',
            'time_expires': 'datetime',
            'time_issued': 'datetime'
        }

        self.attribute_map = {
            'circuit_type': 'circuitType',
            'cross_connect_id': 'crossConnectId',
            'facility_location': 'facilityLocation',
            'port_name': 'portName',
            'time_expires': 'timeExpires',
            'time_issued': 'timeIssued'
        }

        self._circuit_type = None
        self._cross_connect_id = None
        self._facility_location = None
        self._port_name = None
        self._time_expires = None
        self._time_issued = None

    @property
    def circuit_type(self):
        """
        Gets the circuit_type of this LetterOfAuthority.
        The type of cross-connect fiber, termination, and optical specification.

        Allowed values for this property are: "Single_mode_LC", "Single_mode_SC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The circuit_type of this LetterOfAuthority.
        :rtype: str
        """
        return self._circuit_type

    @circuit_type.setter
    def circuit_type(self, circuit_type):
        """
        Sets the circuit_type of this LetterOfAuthority.
        The type of cross-connect fiber, termination, and optical specification.


        :param circuit_type: The circuit_type of this LetterOfAuthority.
        :type: str
        """
        allowed_values = ["Single_mode_LC", "Single_mode_SC"]
        if circuit_type not in allowed_values:
            circuit_type = 'UNKNOWN_ENUM_VALUE'
        self._circuit_type = circuit_type

    @property
    def cross_connect_id(self):
        """
        Gets the cross_connect_id of this LetterOfAuthority.
        The OCID of the cross-connect.


        :return: The cross_connect_id of this LetterOfAuthority.
        :rtype: str
        """
        return self._cross_connect_id

    @cross_connect_id.setter
    def cross_connect_id(self, cross_connect_id):
        """
        Sets the cross_connect_id of this LetterOfAuthority.
        The OCID of the cross-connect.


        :param cross_connect_id: The cross_connect_id of this LetterOfAuthority.
        :type: str
        """
        self._cross_connect_id = cross_connect_id

    @property
    def facility_location(self):
        """
        Gets the facility_location of this LetterOfAuthority.
        The address of the FastConnect location.


        :return: The facility_location of this LetterOfAuthority.
        :rtype: str
        """
        return self._facility_location

    @facility_location.setter
    def facility_location(self, facility_location):
        """
        Sets the facility_location of this LetterOfAuthority.
        The address of the FastConnect location.


        :param facility_location: The facility_location of this LetterOfAuthority.
        :type: str
        """
        self._facility_location = facility_location

    @property
    def port_name(self):
        """
        Gets the port_name of this LetterOfAuthority.
        The meet-me room port for this cross-connect.


        :return: The port_name of this LetterOfAuthority.
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """
        Sets the port_name of this LetterOfAuthority.
        The meet-me room port for this cross-connect.


        :param port_name: The port_name of this LetterOfAuthority.
        :type: str
        """
        self._port_name = port_name

    @property
    def time_expires(self):
        """
        Gets the time_expires of this LetterOfAuthority.
        The date and time when the Letter of Authority expires, in the format defined by RFC3339.


        :return: The time_expires of this LetterOfAuthority.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this LetterOfAuthority.
        The date and time when the Letter of Authority expires, in the format defined by RFC3339.


        :param time_expires: The time_expires of this LetterOfAuthority.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def time_issued(self):
        """
        Gets the time_issued of this LetterOfAuthority.
        The date and time the Letter of Authority was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_issued of this LetterOfAuthority.
        :rtype: datetime
        """
        return self._time_issued

    @time_issued.setter
    def time_issued(self, time_issued):
        """
        Sets the time_issued of this LetterOfAuthority.
        The date and time the Letter of Authority was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_issued: The time_issued of this LetterOfAuthority.
        :type: datetime
        """
        self._time_issued = time_issued

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
