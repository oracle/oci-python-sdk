# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .image_source_details import ImageSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageSourceViaObjectStorageUriDetails(ImageSourceDetails):
    """
    ImageSourceViaObjectStorageUriDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageSourceViaObjectStorageUriDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.ImageSourceViaObjectStorageUriDetails.source_type` attribute
        of this class is ``objectStorageUri`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_image_type:
            The value to assign to the source_image_type property of this ImageSourceViaObjectStorageUriDetails.
            Allowed values for this property are: "QCOW2", "VMDK"
        :type source_image_type: str

        :param source_type:
            The value to assign to the source_type property of this ImageSourceViaObjectStorageUriDetails.
        :type source_type: str

        :param source_uri:
            The value to assign to the source_uri property of this ImageSourceViaObjectStorageUriDetails.
        :type source_uri: str

        """
        self.swagger_types = {
            'source_image_type': 'str',
            'source_type': 'str',
            'source_uri': 'str'
        }

        self.attribute_map = {
            'source_image_type': 'sourceImageType',
            'source_type': 'sourceType',
            'source_uri': 'sourceUri'
        }

        self._source_image_type = None
        self._source_type = None
        self._source_uri = None
        self._source_type = 'objectStorageUri'

    @property
    def source_uri(self):
        """
        **[Required]** Gets the source_uri of this ImageSourceViaObjectStorageUriDetails.
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
