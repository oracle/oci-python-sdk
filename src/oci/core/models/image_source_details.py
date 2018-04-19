# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageSourceDetails(object):
    """
    ImageSourceDetails model.
    """

    #: A constant which can be used with the source_image_type property of a ImageSourceDetails.
    #: This constant has a value of "QCOW2"
    SOURCE_IMAGE_TYPE_QCOW2 = "QCOW2"

    #: A constant which can be used with the source_image_type property of a ImageSourceDetails.
    #: This constant has a value of "VMDK"
    SOURCE_IMAGE_TYPE_VMDK = "VMDK"

    def __init__(self, **kwargs):
        """
        Initializes a new ImageSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.ImageSourceViaObjectStorageTupleDetails`
        * :class:`~oci.core.models.ImageSourceViaObjectStorageUriDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_image_type:
            The value to assign to the source_image_type property of this ImageSourceDetails.
            Allowed values for this property are: "QCOW2", "VMDK"
        :type source_image_type: str

        :param source_type:
            The value to assign to the source_type property of this ImageSourceDetails.
        :type source_type: str

        """
        self.swagger_types = {
            'source_image_type': 'str',
            'source_type': 'str'
        }

        self.attribute_map = {
            'source_image_type': 'sourceImageType',
            'source_type': 'sourceType'
        }

        self._source_image_type = None
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
    def source_image_type(self):
        """
        Gets the source_image_type of this ImageSourceDetails.
        The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic
        images are supported.

        Allowed values for this property are: "QCOW2", "VMDK"


        :return: The source_image_type of this ImageSourceDetails.
        :rtype: str
        """
        return self._source_image_type

    @source_image_type.setter
    def source_image_type(self, source_image_type):
        """
        Sets the source_image_type of this ImageSourceDetails.
        The format of the image to be imported.  Exported Oracle images are QCOW2.  Only monolithic
        images are supported.


        :param source_image_type: The source_image_type of this ImageSourceDetails.
        :type: str
        """
        allowed_values = ["QCOW2", "VMDK"]
        if not value_allowed_none_or_none_sentinel(source_image_type, allowed_values):
            raise ValueError(
                "Invalid value for `source_image_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source_image_type = source_image_type

    @property
    def source_type(self):
        """
        **[Required]** Gets the source_type of this ImageSourceDetails.
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
