# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStackDetails(object):
    """
    Stack details required to update a Stack artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStackDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_stack_id:
            The value to assign to the source_stack_id property of this UpdateStackDetails.
        :type source_stack_id: str

        :param image_listing_ids:
            The value to assign to the image_listing_ids property of this UpdateStackDetails.
        :type image_listing_ids: list[str]

        """
        self.swagger_types = {
            'source_stack_id': 'str',
            'image_listing_ids': 'list[str]'
        }
        self.attribute_map = {
            'source_stack_id': 'sourceStackId',
            'image_listing_ids': 'imageListingIds'
        }
        self._source_stack_id = None
        self._image_listing_ids = None

    @property
    def source_stack_id(self):
        """
        Gets the source_stack_id of this UpdateStackDetails.
        The source stack OCID.


        :return: The source_stack_id of this UpdateStackDetails.
        :rtype: str
        """
        return self._source_stack_id

    @source_stack_id.setter
    def source_stack_id(self, source_stack_id):
        """
        Sets the source_stack_id of this UpdateStackDetails.
        The source stack OCID.


        :param source_stack_id: The source_stack_id of this UpdateStackDetails.
        :type: str
        """
        self._source_stack_id = source_stack_id

    @property
    def image_listing_ids(self):
        """
        Gets the image_listing_ids of this UpdateStackDetails.
        Image listing OCIDs that are referred in the Stack.


        :return: The image_listing_ids of this UpdateStackDetails.
        :rtype: list[str]
        """
        return self._image_listing_ids

    @image_listing_ids.setter
    def image_listing_ids(self, image_listing_ids):
        """
        Sets the image_listing_ids of this UpdateStackDetails.
        Image listing OCIDs that are referred in the Stack.


        :param image_listing_ids: The image_listing_ids of this UpdateStackDetails.
        :type: list[str]
        """
        self._image_listing_ids = image_listing_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
