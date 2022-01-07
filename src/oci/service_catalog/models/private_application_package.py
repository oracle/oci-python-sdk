# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateApplicationPackage(object):
    """
    A base object for all types of private application packages.
    """

    #: A constant which can be used with the package_type property of a PrivateApplicationPackage.
    #: This constant has a value of "STACK"
    PACKAGE_TYPE_STACK = "STACK"

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateApplicationPackage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_catalog.models.PrivateApplicationStackPackage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PrivateApplicationPackage.
        :type id: str

        :param private_application_id:
            The value to assign to the private_application_id property of this PrivateApplicationPackage.
        :type private_application_id: str

        :param display_name:
            The value to assign to the display_name property of this PrivateApplicationPackage.
        :type display_name: str

        :param version:
            The value to assign to the version property of this PrivateApplicationPackage.
        :type version: str

        :param package_type:
            The value to assign to the package_type property of this PrivateApplicationPackage.
            Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param time_created:
            The value to assign to the time_created property of this PrivateApplicationPackage.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'private_application_id': 'str',
            'display_name': 'str',
            'version': 'str',
            'package_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'private_application_id': 'privateApplicationId',
            'display_name': 'displayName',
            'version': 'version',
            'package_type': 'packageType',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._private_application_id = None
        self._display_name = None
        self._version = None
        self._package_type = None
        self._time_created = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageType']

        if type == 'STACK':
            return 'PrivateApplicationStackPackage'
        else:
            return 'PrivateApplicationPackage'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PrivateApplicationPackage.
        The `OCID`__ of the private application package.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PrivateApplicationPackage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateApplicationPackage.
        The `OCID`__ of the private application package.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PrivateApplicationPackage.
        :type: str
        """
        self._id = id

    @property
    def private_application_id(self):
        """
        **[Required]** Gets the private_application_id of this PrivateApplicationPackage.
        The `OCID`__ of the private application where the package is hosted.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_application_id of this PrivateApplicationPackage.
        :rtype: str
        """
        return self._private_application_id

    @private_application_id.setter
    def private_application_id(self, private_application_id):
        """
        Sets the private_application_id of this PrivateApplicationPackage.
        The `OCID`__ of the private application where the package is hosted.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_application_id: The private_application_id of this PrivateApplicationPackage.
        :type: str
        """
        self._private_application_id = private_application_id

    @property
    def display_name(self):
        """
        Gets the display_name of this PrivateApplicationPackage.
        The display name of the package.


        :return: The display_name of this PrivateApplicationPackage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateApplicationPackage.
        The display name of the package.


        :param display_name: The display_name of this PrivateApplicationPackage.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this PrivateApplicationPackage.
        The package version.


        :return: The version of this PrivateApplicationPackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PrivateApplicationPackage.
        The package version.


        :param version: The version of this PrivateApplicationPackage.
        :type: str
        """
        self._version = version

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this PrivateApplicationPackage.
        The specified package's type.

        Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this PrivateApplicationPackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PrivateApplicationPackage.
        The specified package's type.


        :param package_type: The package_type of this PrivateApplicationPackage.
        :type: str
        """
        allowed_values = ["STACK"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PrivateApplicationPackage.
        The date and time the private application package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-27T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PrivateApplicationPackage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateApplicationPackage.
        The date and time the private application package was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-27T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PrivateApplicationPackage.
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
