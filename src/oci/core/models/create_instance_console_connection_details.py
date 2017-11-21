# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceConsoleConnectionDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceConsoleConnectionDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_id:
            The value to assign to the instance_id property of this CreateInstanceConsoleConnectionDetails.
        :type instance_id: str

        :param public_key:
            The value to assign to the public_key property of this CreateInstanceConsoleConnectionDetails.
        :type public_key: str

        """
        self.swagger_types = {
            'instance_id': 'str',
            'public_key': 'str'
        }

        self.attribute_map = {
            'instance_id': 'instanceId',
            'public_key': 'publicKey'
        }

        self._instance_id = None
        self._public_key = None

    @property
    def instance_id(self):
        """
        Gets the instance_id of this CreateInstanceConsoleConnectionDetails.
        The OCID of the instance to create the console connection to.


        :return: The instance_id of this CreateInstanceConsoleConnectionDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateInstanceConsoleConnectionDetails.
        The OCID of the instance to create the console connection to.


        :param instance_id: The instance_id of this CreateInstanceConsoleConnectionDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def public_key(self):
        """
        Gets the public_key of this CreateInstanceConsoleConnectionDetails.
        The SSH public key used to authenticate the console connection.


        :return: The public_key of this CreateInstanceConsoleConnectionDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this CreateInstanceConsoleConnectionDetails.
        The SSH public key used to authenticate the console connection.


        :param public_key: The public_key of this CreateInstanceConsoleConnectionDetails.
        :type: str
        """
        self._public_key = public_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
