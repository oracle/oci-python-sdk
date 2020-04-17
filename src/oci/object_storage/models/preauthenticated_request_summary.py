# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreauthenticatedRequestSummary(object):
    """
    Get summary information about pre-authenticated requests.
    """

    #: A constant which can be used with the access_type property of a PreauthenticatedRequestSummary.
    #: This constant has a value of "ObjectRead"
    ACCESS_TYPE_OBJECT_READ = "ObjectRead"

    #: A constant which can be used with the access_type property of a PreauthenticatedRequestSummary.
    #: This constant has a value of "ObjectWrite"
    ACCESS_TYPE_OBJECT_WRITE = "ObjectWrite"

    #: A constant which can be used with the access_type property of a PreauthenticatedRequestSummary.
    #: This constant has a value of "ObjectReadWrite"
    ACCESS_TYPE_OBJECT_READ_WRITE = "ObjectReadWrite"

    #: A constant which can be used with the access_type property of a PreauthenticatedRequestSummary.
    #: This constant has a value of "AnyObjectWrite"
    ACCESS_TYPE_ANY_OBJECT_WRITE = "AnyObjectWrite"

    def __init__(self, **kwargs):
        """
        Initializes a new PreauthenticatedRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PreauthenticatedRequestSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this PreauthenticatedRequestSummary.
        :type name: str

        :param object_name:
            The value to assign to the object_name property of this PreauthenticatedRequestSummary.
        :type object_name: str

        :param access_type:
            The value to assign to the access_type property of this PreauthenticatedRequestSummary.
            Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type access_type: str

        :param time_expires:
            The value to assign to the time_expires property of this PreauthenticatedRequestSummary.
        :type time_expires: datetime

        :param time_created:
            The value to assign to the time_created property of this PreauthenticatedRequestSummary.
        :type time_created: datetime

        """
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
        **[Required]** Gets the id of this PreauthenticatedRequestSummary.
        The unique identifier to use when directly addressing the pre-authenticated request.


        :return: The id of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PreauthenticatedRequestSummary.
        The unique identifier to use when directly addressing the pre-authenticated request.


        :param id: The id of this PreauthenticatedRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PreauthenticatedRequestSummary.
        The user-provided name of the pre-authenticated request.


        :return: The name of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PreauthenticatedRequestSummary.
        The user-provided name of the pre-authenticated request.


        :param name: The name of this PreauthenticatedRequestSummary.
        :type: str
        """
        self._name = name

    @property
    def object_name(self):
        """
        Gets the object_name of this PreauthenticatedRequestSummary.
        The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is,
        the pre-authenticated request grants access to the entire bucket.


        :return: The object_name of this PreauthenticatedRequestSummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this PreauthenticatedRequestSummary.
        The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is,
        the pre-authenticated request grants access to the entire bucket.


        :param object_name: The object_name of this PreauthenticatedRequestSummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def access_type(self):
        """
        **[Required]** Gets the access_type of this PreauthenticatedRequestSummary.
        The operation that can be performed on this resource.

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
        The operation that can be performed on this resource.


        :param access_type: The access_type of this PreauthenticatedRequestSummary.
        :type: str
        """
        allowed_values = ["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]
        if not value_allowed_none_or_none_sentinel(access_type, allowed_values):
            access_type = 'UNKNOWN_ENUM_VALUE'
        self._access_type = access_type

    @property
    def time_expires(self):
        """
        **[Required]** Gets the time_expires of this PreauthenticatedRequestSummary.
        The expiration date for the pre-authenticated request as per `RFC 3339`__. After this date the pre-authenticated request will no longer be valid.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_expires of this PreauthenticatedRequestSummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this PreauthenticatedRequestSummary.
        The expiration date for the pre-authenticated request as per `RFC 3339`__. After this date the pre-authenticated request will no longer be valid.

        __ https://tools.ietf.org/html/rfc3339


        :param time_expires: The time_expires of this PreauthenticatedRequestSummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PreauthenticatedRequestSummary.
        The date when the pre-authenticated request was created as per `RFC 3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PreauthenticatedRequestSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PreauthenticatedRequestSummary.
        The date when the pre-authenticated request was created as per `RFC 3339`__.

        __ https://tools.ietf.org/html/rfc3339


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
