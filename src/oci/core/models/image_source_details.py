# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageSourceDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new ImageSourceDetails object with values from values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.ImageSourceViaObjectStorageTupleDetails`
        * :class:`~oci.core.models.ImageSourceViaObjectStorageUriDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this ImageSourceDetails.
        :type source_type: str

        """
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
        bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.


        :return: The source_type of this ImageSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this ImageSourceDetails.
        The source type for the image. Use `objectStorageTuple` when specifying the namespace,
        bucket name, and object name. Use `objectStorageUri` when specifying the Object Storage URL.


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
