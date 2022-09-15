# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceSourceDetails(object):
    """
    InstanceSourceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_migrations.models.InstanceSourceViaImageDetails`
        * :class:`~oci.cloud_migrations.models.InstanceSourceViaBootVolumeDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

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
        **[Required]** Gets the source_type of this InstanceSourceDetails.
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
