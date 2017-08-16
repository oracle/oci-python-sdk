# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class PreauthenticatedRequestSummary(object):

    def __init__(self):

        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'object_name': 'str',
            'access_type': 'str',
            'time_expires': 'datetime',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'object_name': 'objectName',
            'access_type': 'accessType',
            'time_expires': 'timeExpires',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._name = None
        self._object_name = None
        self._access_type = None
        self._time_expires = None
        self._time_created = None

    @property
    def id(self):
        """
        Gets the id of this PreauthenticatedRequestSummary.
        the unique identifier to use when directly addressing the pre-authenticated request


        :return: The id of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PreauthenticatedRequestSummary.
        the unique identifier to use when directly addressing the pre-authenticated request


        :param id: The id of this PreauthenticatedRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PreauthenticatedRequestSummary.
        the user supplied name of the pre-authenticated request


        :return: The name of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PreauthenticatedRequestSummary.
        the user supplied name of the pre-authenticated request


        :param name: The name of this PreauthenticatedRequestSummary.
        :type: str
        """
        self._name = name

    @property
    def object_name(self):
        """
        Gets the object_name of this PreauthenticatedRequestSummary.
        Name of object that is being granted access to by the pre-authenticated request. This can be null and that would mean that the pre-authenticated request is granting access to the entire bucket


        :return: The object_name of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this PreauthenticatedRequestSummary.
        Name of object that is being granted access to by the pre-authenticated request. This can be null and that would mean that the pre-authenticated request is granting access to the entire bucket


        :param object_name: The object_name of this PreauthenticatedRequestSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def access_type(self):
        """
        Gets the access_type of this PreauthenticatedRequestSummary.
        the operation that can be performed on this resource e.g PUT or GET.

        Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The access_type of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this PreauthenticatedRequestSummary.
        the operation that can be performed on this resource e.g PUT or GET.


        :param access_type: The access_type of this PreauthenticatedRequestSummary.
        :type: str
        """
        allowed_values = ["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]
        if access_type not in allowed_values:
            access_type = 'UNKNOWN_ENUM_VALUE'
        self._access_type = access_type

    @property
    def time_expires(self):
        """
        Gets the time_expires of this PreauthenticatedRequestSummary.
        the expiration date after which the pre authenticated request will no longer be valid as per spec
        `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_expires of this PreauthenticatedRequestSummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this PreauthenticatedRequestSummary.
        the expiration date after which the pre authenticated request will no longer be valid as per spec
        `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_expires: The time_expires of this PreauthenticatedRequestSummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def time_created(self):
        """
        Gets the time_created of this PreauthenticatedRequestSummary.
        the date when the pre-authenticated request was created as per spec
        `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this PreauthenticatedRequestSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PreauthenticatedRequestSummary.
        the date when the pre-authenticated request was created as per spec
        `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this PreauthenticatedRequestSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
