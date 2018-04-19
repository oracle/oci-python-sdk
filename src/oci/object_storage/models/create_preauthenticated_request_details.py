# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePreauthenticatedRequestDetails(object):
    """
    CreatePreauthenticatedRequestDetails model.
    """

    #: A constant which can be used with the access_type property of a CreatePreauthenticatedRequestDetails.
    #: This constant has a value of "ObjectRead"
    ACCESS_TYPE_OBJECT_READ = "ObjectRead"

    #: A constant which can be used with the access_type property of a CreatePreauthenticatedRequestDetails.
    #: This constant has a value of "ObjectWrite"
    ACCESS_TYPE_OBJECT_WRITE = "ObjectWrite"

    #: A constant which can be used with the access_type property of a CreatePreauthenticatedRequestDetails.
    #: This constant has a value of "ObjectReadWrite"
    ACCESS_TYPE_OBJECT_READ_WRITE = "ObjectReadWrite"

    #: A constant which can be used with the access_type property of a CreatePreauthenticatedRequestDetails.
    #: This constant has a value of "AnyObjectWrite"
    ACCESS_TYPE_ANY_OBJECT_WRITE = "AnyObjectWrite"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePreauthenticatedRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreatePreauthenticatedRequestDetails.
        :type name: str

        :param object_name:
            The value to assign to the object_name property of this CreatePreauthenticatedRequestDetails.
        :type object_name: str

        :param access_type:
            The value to assign to the access_type property of this CreatePreauthenticatedRequestDetails.
            Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"
        :type access_type: str

        :param time_expires:
            The value to assign to the time_expires property of this CreatePreauthenticatedRequestDetails.
        :type time_expires: datetime

        """
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
        **[Required]** Gets the name of this CreatePreauthenticatedRequestDetails.
        A user-specified name for the pre-authenticated request. Helpful for management purposes.


        :return: The name of this CreatePreauthenticatedRequestDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePreauthenticatedRequestDetails.
        A user-specified name for the pre-authenticated request. Helpful for management purposes.


        :param name: The name of this CreatePreauthenticatedRequestDetails.
        :type: str
        """
        self._name = name

    @property
    def object_name(self):
        """
        Gets the object_name of this CreatePreauthenticatedRequestDetails.
        The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is, the pre-authenticated request grants access to the entire bucket.


        :return: The object_name of this CreatePreauthenticatedRequestDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this CreatePreauthenticatedRequestDetails.
        The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is, the pre-authenticated request grants access to the entire bucket.


        :param object_name: The object_name of this CreatePreauthenticatedRequestDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def access_type(self):
        """
        **[Required]** Gets the access_type of this CreatePreauthenticatedRequestDetails.
        The operation that can be performed on this resource.

        Allowed values for this property are: "ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"


        :return: The access_type of this CreatePreauthenticatedRequestDetails.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this CreatePreauthenticatedRequestDetails.
        The operation that can be performed on this resource.


        :param access_type: The access_type of this CreatePreauthenticatedRequestDetails.
        :type: str
        """
        allowed_values = ["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]
        if not value_allowed_none_or_none_sentinel(access_type, allowed_values):
            raise ValueError(
                "Invalid value for `access_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._access_type = access_type

    @property
    def time_expires(self):
        """
        **[Required]** Gets the time_expires of this CreatePreauthenticatedRequestDetails.
        The expiration date for the pre-authenticated request as per `RFC 3339`__. After this date the pre-authenticated request will no longer be valid.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_expires of this CreatePreauthenticatedRequestDetails.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this CreatePreauthenticatedRequestDetails.
        The expiration date for the pre-authenticated request as per `RFC 3339`__. After this date the pre-authenticated request will no longer be valid.

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
