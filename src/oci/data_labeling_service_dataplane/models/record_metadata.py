# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecordMetadata(object):
    """
    Collection of record's metadata.  This can be, for example, the height, width or depth of image for an image record.
    """

    #: A constant which can be used with the record_type property of a RecordMetadata.
    #: This constant has a value of "IMAGE_METADATA"
    RECORD_TYPE_IMAGE_METADATA = "IMAGE_METADATA"

    #: A constant which can be used with the record_type property of a RecordMetadata.
    #: This constant has a value of "TEXT_METADATA"
    RECORD_TYPE_TEXT_METADATA = "TEXT_METADATA"

    #: A constant which can be used with the record_type property of a RecordMetadata.
    #: This constant has a value of "DOCUMENT_METADATA"
    RECORD_TYPE_DOCUMENT_METADATA = "DOCUMENT_METADATA"

    def __init__(self, **kwargs):
        """
        Initializes a new RecordMetadata object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_labeling_service_dataplane.models.DocumentMetadata`
        * :class:`~oci.data_labeling_service_dataplane.models.ImageMetadata`
        * :class:`~oci.data_labeling_service_dataplane.models.TextMetadata`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param record_type:
            The value to assign to the record_type property of this RecordMetadata.
            Allowed values for this property are: "IMAGE_METADATA", "TEXT_METADATA", "DOCUMENT_METADATA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type record_type: str

        """
        self.swagger_types = {
            'record_type': 'str'
        }

        self.attribute_map = {
            'record_type': 'recordType'
        }

        self._record_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['recordType']

        if type == 'DOCUMENT_METADATA':
            return 'DocumentMetadata'

        if type == 'IMAGE_METADATA':
            return 'ImageMetadata'

        if type == 'TEXT_METADATA':
            return 'TextMetadata'
        else:
            return 'RecordMetadata'

    @property
    def record_type(self):
        """
        Gets the record_type of this RecordMetadata.
        The record type based on dataset format details.
        IMAGE_METADATA  - Collection of metadata related to image record.
        TEXT_METADATA - Collection of metadata related to text record.
        DOCUMENT_METADATA - Collection of metadata related to document record.

        Allowed values for this property are: "IMAGE_METADATA", "TEXT_METADATA", "DOCUMENT_METADATA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The record_type of this RecordMetadata.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """
        Sets the record_type of this RecordMetadata.
        The record type based on dataset format details.
        IMAGE_METADATA  - Collection of metadata related to image record.
        TEXT_METADATA - Collection of metadata related to text record.
        DOCUMENT_METADATA - Collection of metadata related to document record.


        :param record_type: The record_type of this RecordMetadata.
        :type: str
        """
        allowed_values = ["IMAGE_METADATA", "TEXT_METADATA", "DOCUMENT_METADATA"]
        if not value_allowed_none_or_none_sentinel(record_type, allowed_values):
            record_type = 'UNKNOWN_ENUM_VALUE'
        self._record_type = record_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
