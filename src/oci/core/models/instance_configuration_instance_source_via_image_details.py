# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .instance_configuration_instance_source_details import InstanceConfigurationInstanceSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationInstanceSourceViaImageDetails(InstanceConfigurationInstanceSourceDetails):
    """
    InstanceConfigurationInstanceSourceViaImageDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationInstanceSourceViaImageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationInstanceSourceViaImageDetails.source_type` attribute
        of this class is ``image`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type source_type: str

        :param image_id:
            The value to assign to the image_id property of this InstanceConfigurationInstanceSourceViaImageDetails.
        :type image_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'image_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'image_id': 'imageId'
        }

        self._source_type = None
        self._image_id = None
        self._source_type = 'image'

    @property
    def image_id(self):
        """
        Gets the image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        The OCID of the image used to boot the instance.


        :return: The image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
        The OCID of the image used to boot the instance.


        :param image_id: The image_id of this InstanceConfigurationInstanceSourceViaImageDetails.
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
