# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateImageDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'instance_id': 'instanceId'
        }

        self._compartment_id = None
        self._display_name = None
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
        A user-friendly name for the image. It does not have to be unique, and it's changeable. You cannot use an
        Oracle-provided image name as a custom image name.

        Example: `My Oracle Linux image`


        :return: The display_name of this CreateImageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable. You cannot use an
        Oracle-provided image name as a custom image name.

        Example: `My Oracle Linux image`


        :param display_name: The display_name of this CreateImageDetails.
        :type: str
        """
        self._display_name = display_name

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
