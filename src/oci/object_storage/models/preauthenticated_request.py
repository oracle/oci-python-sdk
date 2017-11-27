# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreauthenticatedRequest(object):

    def __init__(self, **kwargs):
        """
        Initializes a new PreauthenticatedRequest object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PreauthenticatedRequest.
        :type id: str

        :param name:
            The value to assign to the name property of this PreauthenticatedRequest.
        :type name: str

        :param access_uri:
            The value to assign to the access_uri property of this PreauthenticatedRequest.
        :type access_uri: str

        :param object_name:
            The value to assign to the object_name property of this PreauthenticatedRequest.
        :type object_name: str

        :param access_type:
            The value to assign to the access_type property of this PreauthenticatedRequest.
            Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type access_type: str

        :param time_expires:
            The value to assign to the time_expires property of this PreauthenticatedRequest.
        :type time_expires: datetime

        :param time_created:
            The value to assign to the time_created property of this PreauthenticatedRequest.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'access_uri': 'str',
            'object_name': 'str',
            'access_type': 'str',
            'time_expires': 'datetime',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'access_uri': 'accessUri',
            'object_name': 'objectName',
            'access_type': 'accessType',
            'time_expires': 'timeExpires',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._name = None
        self._access_uri = None
        self._object_name = None
        self._access_type = None
        self._time_expires = None
        self._time_created = None

    @property
    def id(self):
        """
        Gets the id of this PreauthenticatedRequest.
        The unique identifier to use when directly addressing the pre-authenticated request.


        :return: The id of this PreauthenticatedRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PreauthenticatedRequest.
        The unique identifier to use when directly addressing the pre-authenticated request.


        :param id: The id of this PreauthenticatedRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PreauthenticatedRequest.
        The user-provided name of the pre-authenticated request.


        :return: The name of this PreauthenticatedRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PreauthenticatedRequest.
        The user-provided name of the pre-authenticated request.


        :param name: The name of this PreauthenticatedRequest.
        :type: str
        """
        self._name = name

    @property
    def access_uri(self):
        """
        Gets the access_uri of this PreauthenticatedRequest.
        The URI to embed in the URL when using the pre-authenticated request.


        :return: The access_uri of this PreauthenticatedRequest.
        :rtype: str
        """
        return self._access_uri

    @access_uri.setter
    def access_uri(self, access_uri):
        """
        Sets the access_uri of this PreauthenticatedRequest.
        The URI to embed in the URL when using the pre-authenticated request.


        :param access_uri: The access_uri of this PreauthenticatedRequest.
        :type: str
        """
        self._access_uri = access_uri

    @property
    def object_name(self):
        """
        Gets the object_name of this PreauthenticatedRequest.
        The name of the object that is being granted access to by the pre-authenticated request. This can be null and
        if so, the pre-authenticated request grants access to the entire bucket. Avoid entering confidential information.
        Example: test/object1.log


        :return: The object_name of this PreauthenticatedRequest.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this PreauthenticatedRequest.
        The name of the object that is being granted access to by the pre-authenticated request. This can be null and
        if so, the pre-authenticated request grants access to the entire bucket. Avoid entering confidential information.
        Example: test/object1.log


        :param object_name: The object_name of this PreauthenticatedRequest.
        :type: str
        """
        self._object_name = object_name

    @property
    def access_type(self):
        """
        Gets the access_type of this PreauthenticatedRequest.
        The operation that can be performed on this resource.

        Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The access_type of this PreauthenticatedRequest.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this PreauthenticatedRequest.
        The operation that can be performed on this resource.


        :param access_type: The access_type of this PreauthenticatedRequest.
        :type: str
        """
        allowed_values = ["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]
        if access_type not in allowed_values:
            access_type = 'UNKNOWN_ENUM_VALUE'
        self._access_type = access_type

    @property
    def time_expires(self):
        """
        Gets the time_expires of this PreauthenticatedRequest.
        The expiration date for the pre-authenticated request as per `RFC 3339`__. After this date the pre-authenticated request will no longer be valid.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_expires of this PreauthenticatedRequest.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this PreauthenticatedRequest.
        The expiration date for the pre-authenticated request as per `RFC 3339`__. After this date the pre-authenticated request will no longer be valid.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_expires: The time_expires of this PreauthenticatedRequest.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def time_created(self):
        """
        Gets the time_created of this PreauthenticatedRequest.
        The date when the pre-authenticated request was created as per specification
        `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this PreauthenticatedRequest.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PreauthenticatedRequest.
        The date when the pre-authenticated request was created as per specification
        `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this PreauthenticatedRequest.
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
