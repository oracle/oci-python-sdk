# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Entity(object):
    """
    An entity allows the labeler to identify an object in the record to label.  This can be, for example, a snippet of text, an entire image, or a bounding box within an image.  All entity types have an array of labels that are indexed. If more than one label is provided, but the annotationType on the corresponding dataset is for a single class, the API rejects the create annotation request.
    """

    #: A constant which can be used with the entity_type property of a Entity.
    #: This constant has a value of "GENERIC"
    ENTITY_TYPE_GENERIC = "GENERIC"

    #: A constant which can be used with the entity_type property of a Entity.
    #: This constant has a value of "IMAGEOBJECTSELECTION"
    ENTITY_TYPE_IMAGEOBJECTSELECTION = "IMAGEOBJECTSELECTION"

    #: A constant which can be used with the entity_type property of a Entity.
    #: This constant has a value of "TEXTSELECTION"
    ENTITY_TYPE_TEXTSELECTION = "TEXTSELECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new Entity object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_labeling_service_dataplane.models.ImageObjectSelectionEntity`
        * :class:`~oci.data_labeling_service_dataplane.models.GenericEntity`
        * :class:`~oci.data_labeling_service_dataplane.models.TextSelectionEntity`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this Entity.
            Allowed values for this property are: "GENERIC", "IMAGEOBJECTSELECTION", "TEXTSELECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        """
        self.swagger_types = {
            'entity_type': 'str'
        }

        self.attribute_map = {
            'entity_type': 'entityType'
        }

        self._entity_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entityType']

        if type == 'IMAGEOBJECTSELECTION':
            return 'ImageObjectSelectionEntity'

        if type == 'GENERIC':
            return 'GenericEntity'

        if type == 'TEXTSELECTION':
            return 'TextSelectionEntity'
        else:
            return 'Entity'

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this Entity.
        The entity type described in the annotation.
        GENERIC  - An extensible entity type that is the base entity type for some annotation formats.
        IMAGEOBJECTSELECTION- - This allows the labeler to use specify a bounding polygon on the image to represent an object and apply labels to it.
        TEXTSELECTION - This allows the labeler to highlight text, by specifying an offset and a length, and apply labels to it.

        Allowed values for this property are: "GENERIC", "IMAGEOBJECTSELECTION", "TEXTSELECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this Entity.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Entity.
        The entity type described in the annotation.
        GENERIC  - An extensible entity type that is the base entity type for some annotation formats.
        IMAGEOBJECTSELECTION- - This allows the labeler to use specify a bounding polygon on the image to represent an object and apply labels to it.
        TEXTSELECTION - This allows the labeler to highlight text, by specifying an offset and a length, and apply labels to it.


        :param entity_type: The entity_type of this Entity.
        :type: str
        """
        allowed_values = ["GENERIC", "IMAGEOBJECTSELECTION", "TEXTSELECTION"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
