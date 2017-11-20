# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .image_source_details import ImageSourceDetails
from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageSourceViaObjectStorageUriDetails(ImageSourceDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new ImageSourceViaObjectStorageUriDetails object with values from values from keyword arguments. The
        following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this ImageSourceViaObjectStorageUriDetails.
        :type source_type: str

        :param source_uri:
            The value to assign to the source_uri property of this ImageSourceViaObjectStorageUriDetails.
        :type source_uri: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'source_uri': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'source_uri': 'sourceUri'
        }

        self._source_type = None
        self._source_uri = None
        self._source_type = 'objectStorageUri'

    @property
    def source_uri(self):
        """
        Gets the source_uri of this ImageSourceViaObjectStorageUriDetails.
        The Object Storage URL for the image.


        :return: The source_uri of this ImageSourceViaObjectStorageUriDetails.
        :rtype: str
        """
        return self._source_uri

    @source_uri.setter
    def source_uri(self, source_uri):
        """
        Sets the source_uri of this ImageSourceViaObjectStorageUriDetails.
        The Object Storage URL for the image.


        :param source_uri: The source_uri of this ImageSourceViaObjectStorageUriDetails.
        :type: str
        """
        self._source_uri = source_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
