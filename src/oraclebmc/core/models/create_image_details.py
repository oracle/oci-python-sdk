# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateImageDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'image_source_details': 'ImageSourceDetails',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'image_source_details': 'imageSourceDetails',
            'instance_id': 'instanceId'
        }

        self._compartment_id = None
        self._display_name = None
        self._image_source_details = None
        self._instance_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateImageDetails.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :return: The compartment_id of this CreateImageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateImageDetails.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :param compartment_id: The compartment_id of this CreateImageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My Oracle Linux image`


        :return: The display_name of this CreateImageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My Oracle Linux image`


        :param display_name: The display_name of this CreateImageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def image_source_details(self):
        """
        Gets the image_source_details of this CreateImageDetails.
        Details for creating an image through import


        :return: The image_source_details of this CreateImageDetails.
        :rtype: ImageSourceDetails
        """
        return self._image_source_details

    @image_source_details.setter
    def image_source_details(self, image_source_details):
        """
        Sets the image_source_details of this CreateImageDetails.
        Details for creating an image through import


        :param image_source_details: The image_source_details of this CreateImageDetails.
        :type: ImageSourceDetails
        """
        self._image_source_details = image_source_details

    @property
    def instance_id(self):
        """
        Gets the instance_id of this CreateImageDetails.
        The OCID of the instance you want to use as the basis for the image.


        :return: The instance_id of this CreateImageDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateImageDetails.
        The OCID of the instance you want to use as the basis for the image.


        :param instance_id: The instance_id of this CreateImageDetails.
        :type: str
        """
        self._instance_id = instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
