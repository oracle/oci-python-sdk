# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreatePreauthenticatedRequestDetails(object):

    def __init__(self):

        self.swagger_types = {
            'name': 'str',
            'object_name': 'str',
            'access_type': 'str',
            'time_expires': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'object_name': 'objectName',
            'access_type': 'accessType',
            'time_expires': 'timeExpires'
        }

        self._name = None
        self._object_name = None
        self._access_type = None
        self._time_expires = None

    @property
    def name(self):
        """
        Gets the name of this CreatePreauthenticatedRequestDetails.
        user specified name for pre-authenticated request. Helpful for management purposes.


        :return: The name of this CreatePreauthenticatedRequestDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePreauthenticatedRequestDetails.
        user specified name for pre-authenticated request. Helpful for management purposes.


        :param name: The name of this CreatePreauthenticatedRequestDetails.
        :type: str
        """
        self._name = name

    @property
    def object_name(self):
        """
        Gets the object_name of this CreatePreauthenticatedRequestDetails.
        Name of object that is being granted access to by the pre-authenticated request. This can be null and that would mean that the pre-authenticated request is granting access to the entire bucket


        :return: The object_name of this CreatePreauthenticatedRequestDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this CreatePreauthenticatedRequestDetails.
        Name of object that is being granted access to by the pre-authenticated request. This can be null and that would mean that the pre-authenticated request is granting access to the entire bucket


        :param object_name: The object_name of this CreatePreauthenticatedRequestDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def access_type(self):
        """
        Gets the access_type of this CreatePreauthenticatedRequestDetails.
        the operation that can be performed on this resource e.g PUT or GET.

        Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"


        :return: The access_type of this CreatePreauthenticatedRequestDetails.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this CreatePreauthenticatedRequestDetails.
        the operation that can be performed on this resource e.g PUT or GET.


        :param access_type: The access_type of this CreatePreauthenticatedRequestDetails.
        :type: str
        """
        allowed_values = ["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]
        if access_type not in allowed_values:
            raise ValueError(
                "Invalid value for `access_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._access_type = access_type

    @property
    def time_expires(self):
        """
        Gets the time_expires of this CreatePreauthenticatedRequestDetails.
        The expiration date after which the pre-authenticated request will no longer be valid per spec
        `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_expires of this CreatePreauthenticatedRequestDetails.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this CreatePreauthenticatedRequestDetails.
        The expiration date after which the pre-authenticated request will no longer be valid per spec
        `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_expires: The time_expires of this CreatePreauthenticatedRequestDetails.
        :type: datetime
        """
        self._time_expires = time_expires

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
