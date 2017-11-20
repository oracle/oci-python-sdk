# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceSourceDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceSourceDetails object with values from values from keyword arguments. The
        following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceSourceDetails.
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

        if type == 'image':
            return 'InstanceSourceViaImageDetails'

        if type == 'bootVolume':
            return 'InstanceSourceViaBootVolumeDetails'
        else:
            return 'InstanceSourceDetails'

    @property
    def source_type(self):
        """
        Gets the source_type of this InstanceSourceDetails.
        The source type for the instance.
        Use `image` when specifying the image OCID. Use `bootVolume` when specifying
        the boot volume OCID.


        :return: The source_type of this InstanceSourceDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this InstanceSourceDetails.
        The source type for the instance.
        Use `image` when specifying the image OCID. Use `bootVolume` when specifying
        the boot volume OCID.


        :param source_type: The source_type of this InstanceSourceDetails.
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
