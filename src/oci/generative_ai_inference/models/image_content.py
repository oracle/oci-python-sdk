# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130

from .chat_content import ChatContent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageContent(ChatContent):
    """
    Represents a single instance of chat image content.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageContent object with values from keyword arguments. The default value of the :py:attr:`~oci.generative_ai_inference.models.ImageContent.type` attribute
        of this class is ``IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ImageContent.
            Allowed values for this property are: "TEXT", "IMAGE"
        :type type: str

        :param image_url:
            The value to assign to the image_url property of this ImageContent.
        :type image_url: oci.generative_ai_inference.models.ImageUrl

        """
        self.swagger_types = {
            'type': 'str',
            'image_url': 'ImageUrl'
        }
        self.attribute_map = {
            'type': 'type',
            'image_url': 'imageUrl'
        }
        self._type = None
        self._image_url = None
        self._type = 'IMAGE'

    @property
    def image_url(self):
        """
        Gets the image_url of this ImageContent.

        :return: The image_url of this ImageContent.
        :rtype: oci.generative_ai_inference.models.ImageUrl
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this ImageContent.

        :param image_url: The image_url of this ImageContent.
        :type: oci.generative_ai_inference.models.ImageUrl
        """
        self._image_url = image_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
