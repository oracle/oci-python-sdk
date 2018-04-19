# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportImageDetails(object):
    """
    The destination details for the image export.

    Set `destinationType` to `objectStorageTuple`
    and use :func:`export_image_via_object_storage_tuple_details`
    when specifying the namespace, bucket name, and object name.

    Set `destinationType` to `objectStorageUri` and
    use :func:`export_image_via_object_storage_uri_details`
    when specifying the Object Storage URL.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportImageDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.ExportImageViaObjectStorageUriDetails`
        * :class:`~oci.core.models.ExportImageViaObjectStorageTupleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_type:
            The value to assign to the destination_type property of this ExportImageDetails.
        :type destination_type: str

        """
        self.swagger_types = {
            'destination_type': 'str'
        }

        self.attribute_map = {
            'destination_type': 'destinationType'
        }

        self._destination_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['destinationType']

        if type == 'objectStorageUri':
            return 'ExportImageViaObjectStorageUriDetails'

        if type == 'objectStorageTuple':
            return 'ExportImageViaObjectStorageTupleDetails'
        else:
            return 'ExportImageDetails'

    @property
    def destination_type(self):
        """
        **[Required]** Gets the destination_type of this ExportImageDetails.
        The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
        Use `objectStorageUri` when specifying the Object Storage URL.


        :return: The destination_type of this ExportImageDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this ExportImageDetails.
        The destination type. Use `objectStorageTuple` when specifying the namespace, bucket name, and object name.
        Use `objectStorageUri` when specifying the Object Storage URL.


        :param destination_type: The destination_type of this ExportImageDetails.
        :type: str
        """
        self._destination_type = destination_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
