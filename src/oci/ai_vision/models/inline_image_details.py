# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .image_details import ImageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InlineImageDetails(ImageDetails):
    """
    Image incorporated in the request payload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InlineImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.InlineImageDetails.source` attribute
        of this class is ``INLINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this InlineImageDetails.
            Allowed values for this property are: "INLINE", "OBJECT_STORAGE"
        :type source: str

        :param data:
            The value to assign to the data property of this InlineImageDetails.
        :type data: str

        """
        self.swagger_types = {
            'source': 'str',
            'data': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'data': 'data'
        }

        self._source = None
        self._data = None
        self._source = 'INLINE'

    @property
    def data(self):
        """
        **[Required]** Gets the data of this InlineImageDetails.
        Image raw data.


        :return: The data of this InlineImageDetails.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this InlineImageDetails.
        Image raw data.


        :param data: The data of this InlineImageDetails.
        :type: str
        """
        self._data = data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
