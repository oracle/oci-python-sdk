# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class ExportImageDetails(object):

    def __init__(self):

        self.swagger_types = {
            'destination_type': 'str'
        }

        self.attribute_map = {
            'destination_type': 'destinationType'
        }

        self._destination_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['destinationType']

        if type == 'objectStorageUri':
            return 'ExportImageViaObjectStorageUriDetails'

        if type == 'objectStorageTuple':
            return 'ExportImageViaObjectStorageTupleDetails'
        else:
            return 'ExportImageDetails'

    @property
    def destination_type(self):
        """
        Gets the destination_type of this ExportImageDetails.
        The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
        Use `objectStorageUri` when specifying the Object Storage Service URL.


        :return: The destination_type of this ExportImageDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this ExportImageDetails.
        The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
        Use `objectStorageUri` when specifying the Object Storage Service URL.


        :param destination_type: The destination_type of this ExportImageDetails.
        :type: str
        """
        self._destination_type = destination_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
