# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkDeleteTagsDetails(object):
    """
    Properties for deleting tags in bulk
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkDeleteTagsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tag_definition_ids:
            The value to assign to the tag_definition_ids property of this BulkDeleteTagsDetails.
        :type tag_definition_ids: list[str]

        """
        self.swagger_types = {
            'tag_definition_ids': 'list[str]'
        }

        self.attribute_map = {
            'tag_definition_ids': 'tagDefinitionIds'
        }

        self._tag_definition_ids = None

    @property
    def tag_definition_ids(self):
        """
        **[Required]** Gets the tag_definition_ids of this BulkDeleteTagsDetails.
        The OCIDs of the tag definitions to delete


        :return: The tag_definition_ids of this BulkDeleteTagsDetails.
        :rtype: list[str]
        """
        return self._tag_definition_ids

    @tag_definition_ids.setter
    def tag_definition_ids(self, tag_definition_ids):
        """
        Sets the tag_definition_ids of this BulkDeleteTagsDetails.
        The OCIDs of the tag definitions to delete


        :param tag_definition_ids: The tag_definition_ids of this BulkDeleteTagsDetails.
        :type: list[str]
        """
        self._tag_definition_ids = tag_definition_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
