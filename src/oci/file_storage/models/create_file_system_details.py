# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFileSystemDetails(object):
    """
    CreateFileSystemDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFileSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateFileSystemDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateFileSystemDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateFileSystemDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateFileSystemDetails.
        The availability domain to create the file system in.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateFileSystemDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateFileSystemDetails.
        The availability domain to create the file system in.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateFileSystemDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateFileSystemDetails.
        The OCID of the compartment to create the file system in.


        :return: The compartment_id of this CreateFileSystemDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateFileSystemDetails.
        The OCID of the compartment to create the file system in.


        :param compartment_id: The compartment_id of this CreateFileSystemDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateFileSystemDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :return: The display_name of this CreateFileSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateFileSystemDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :param display_name: The display_name of this CreateFileSystemDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
