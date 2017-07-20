# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class ImageSourceDetails(object):

    def __init__(self):

        self.swagger_types = {
            'source_type': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType'
        }

        self._source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sourceType']

        if type == 'objectStorageTuple':
            return 'ImageSourceViaObjectStorageTupleDetails'

        if type == 'objectStorageUri':
            return 'ImageSourceViaObjectStorageUriDetails'
        else:
            return 'ImageSourceDetails'

    @property
    def source_type(self):
        """
        Gets the source_type of this ImageSourceDetails.
        The source type for the image. Use `objectStorageTuple` when specifying the namespace,
        bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage Service URL.


        :return: The source_type of this ImageSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this ImageSourceDetails.
        The source type for the image. Use `objectStorageTuple` when specifying the namespace,
        bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage Service URL.


        :param source_type: The source_type of this ImageSourceDetails.
        :type: str
        """
        self._source_type = source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
