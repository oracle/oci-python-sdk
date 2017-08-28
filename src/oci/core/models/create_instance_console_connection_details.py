# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateInstanceConsoleConnectionDetails(object):

    def __init__(self):

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
        The host instance OCID


        :return: The instance_id of this CreateInstanceConsoleConnectionDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateInstanceConsoleConnectionDetails.
        The host instance OCID


        :param instance_id: The instance_id of this CreateInstanceConsoleConnectionDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def public_key(self):
        """
        Gets the public_key of this CreateInstanceConsoleConnectionDetails.
        An ssh public key that will be used to authenticate the console connection.


        :return: The public_key of this CreateInstanceConsoleConnectionDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this CreateInstanceConsoleConnectionDetails.
        An ssh public key that will be used to authenticate the console connection.


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
