# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .node_source_option import NodeSourceOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeSourceViaImageOption(NodeSourceOption):
    """
    An image can be specified as the source of nodes when launching a node pool using the `nodeSourceDetails` object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeSourceViaImageOption object with values from keyword arguments. The default value of the :py:attr:`~oci.container_engine.models.NodeSourceViaImageOption.source_type` attribute
        of this class is ``IMAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this NodeSourceViaImageOption.
            Allowed values for this property are: "IMAGE"
        :type source_type: str

        :param source_name:
            The value to assign to the source_name property of this NodeSourceViaImageOption.
        :type source_name: str

        :param image_id:
            The value to assign to the image_id property of this NodeSourceViaImageOption.
        :type image_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'source_name': 'str',
            'image_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'source_name': 'sourceName',
            'image_id': 'imageId'
        }

        self._source_type = None
        self._source_name = None
        self._image_id = None
        self._source_type = 'IMAGE'

    @property
    def image_id(self):
        """
        Gets the image_id of this NodeSourceViaImageOption.
        The OCID of the image.


        :return: The image_id of this NodeSourceViaImageOption.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this NodeSourceViaImageOption.
        The OCID of the image.


        :param image_id: The image_id of this NodeSourceViaImageOption.
        :type: str
        """
        self._image_id = image_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
