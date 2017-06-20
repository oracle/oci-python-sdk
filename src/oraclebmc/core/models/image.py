# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class Image(object):

    def __init__(self):

        self.swagger_types = {
            'base_image_id': 'str',
            'compartment_id': 'str',
            'create_image_allowed': 'bool',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'operating_system': 'str',
            'operating_system_version': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'base_image_id': 'baseImageId',
            'compartment_id': 'compartmentId',
            'create_image_allowed': 'createImageAllowed',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'operating_system': 'operatingSystem',
            'operating_system_version': 'operatingSystemVersion',
            'time_created': 'timeCreated'
        }

        self._base_image_id = None
        self._compartment_id = None
        self._create_image_allowed = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._operating_system = None
        self._operating_system_version = None
        self._time_created = None

    @property
    def base_image_id(self):
        """
        Gets the base_image_id of this Image.
        The OCID of the image originally used to launch the instance.


        :return: The base_image_id of this Image.
        :rtype: str
        """
        return self._base_image_id

    @base_image_id.setter
    def base_image_id(self, base_image_id):
        """
        Sets the base_image_id of this Image.
        The OCID of the image originally used to launch the instance.


        :param base_image_id: The base_image_id of this Image.
        :type: str
        """
        self._base_image_id = base_image_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Image.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :return: The compartment_id of this Image.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Image.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :param compartment_id: The compartment_id of this Image.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def create_image_allowed(self):
        """
        Gets the create_image_allowed of this Image.
        Whether instances launched with this image can be used to create new images.
        For example, you cannot create an image of an Oracle Database instance.

        Example: `true`


        :return: The create_image_allowed of this Image.
        :rtype: bool
        """
        return self._create_image_allowed

    @create_image_allowed.setter
    def create_image_allowed(self, create_image_allowed):
        """
        Sets the create_image_allowed of this Image.
        Whether instances launched with this image can be used to create new images.
        For example, you cannot create an image of an Oracle Database instance.

        Example: `true`


        :param create_image_allowed: The create_image_allowed of this Image.
        :type: bool
        """
        self._create_image_allowed = create_image_allowed

    @property
    def display_name(self):
        """
        Gets the display_name of this Image.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My custom Oracle Linux image`


        :return: The display_name of this Image.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Image.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My custom Oracle Linux image`


        :param display_name: The display_name of this Image.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Image.
        The OCID of the image.


        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.
        The OCID of the image.


        :param id: The id of this Image.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Image.
        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "DISABLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Image.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Image.

        :param lifecycle_state: The lifecycle_state of this Image.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "DISABLED", "DELETED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def operating_system(self):
        """
        Gets the operating_system of this Image.
        The image's operating system.

        Example: `Oracle Linux`


        :return: The operating_system of this Image.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this Image.
        The image's operating system.

        Example: `Oracle Linux`


        :param operating_system: The operating_system of this Image.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def operating_system_version(self):
        """
        Gets the operating_system_version of this Image.
        The image's operating system version.

        Example: `7.2`


        :return: The operating_system_version of this Image.
        :rtype: str
        """
        return self._operating_system_version

    @operating_system_version.setter
    def operating_system_version(self, operating_system_version):
        """
        Sets the operating_system_version of this Image.
        The image's operating system version.

        Example: `7.2`


        :param operating_system_version: The operating_system_version of this Image.
        :type: str
        """
        self._operating_system_version = operating_system_version

    @property
    def time_created(self):
        """
        Gets the time_created of this Image.
        The date and time the image was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Image.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Image.
        The date and time the image was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Image.
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
