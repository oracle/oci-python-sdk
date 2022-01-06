# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CostTrackingTag(object):
    """
    CostTrackingTag model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CostTrackingTag object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tag_namespace_id:
            The value to assign to the tag_namespace_id property of this CostTrackingTag.
        :type tag_namespace_id: str

        :param tag_namespace_name:
            The value to assign to the tag_namespace_name property of this CostTrackingTag.
        :type tag_namespace_name: str

        :param tag_definition_id:
            The value to assign to the tag_definition_id property of this CostTrackingTag.
        :type tag_definition_id: str

        :param tag_definition_name:
            The value to assign to the tag_definition_name property of this CostTrackingTag.
        :type tag_definition_name: str

        """
        self.swagger_types = {
            'tag_namespace_id': 'str',
            'tag_namespace_name': 'str',
            'tag_definition_id': 'str',
            'tag_definition_name': 'str'
        }

        self.attribute_map = {
            'tag_namespace_id': 'Tag_Namespace_Id',
            'tag_namespace_name': 'Tag_Namespace_Name',
            'tag_definition_id': 'Tag_Definition_Id',
            'tag_definition_name': 'Tag_Definition_Name'
        }

        self._tag_namespace_id = None
        self._tag_namespace_name = None
        self._tag_definition_id = None
        self._tag_definition_name = None

    @property
    def tag_namespace_id(self):
        """
        **[Required]** Gets the tag_namespace_id of this CostTrackingTag.
        The tag namespace id.


        :return: The tag_namespace_id of this CostTrackingTag.
        :rtype: str
        """
        return self._tag_namespace_id

    @tag_namespace_id.setter
    def tag_namespace_id(self, tag_namespace_id):
        """
        Sets the tag_namespace_id of this CostTrackingTag.
        The tag namespace id.


        :param tag_namespace_id: The tag_namespace_id of this CostTrackingTag.
        :type: str
        """
        self._tag_namespace_id = tag_namespace_id

    @property
    def tag_namespace_name(self):
        """
        **[Required]** Gets the tag_namespace_name of this CostTrackingTag.
        The tag namespace name.


        :return: The tag_namespace_name of this CostTrackingTag.
        :rtype: str
        """
        return self._tag_namespace_name

    @tag_namespace_name.setter
    def tag_namespace_name(self, tag_namespace_name):
        """
        Sets the tag_namespace_name of this CostTrackingTag.
        The tag namespace name.


        :param tag_namespace_name: The tag_namespace_name of this CostTrackingTag.
        :type: str
        """
        self._tag_namespace_name = tag_namespace_name

    @property
    def tag_definition_id(self):
        """
        **[Required]** Gets the tag_definition_id of this CostTrackingTag.
        The tag definition id.


        :return: The tag_definition_id of this CostTrackingTag.
        :rtype: str
        """
        return self._tag_definition_id

    @tag_definition_id.setter
    def tag_definition_id(self, tag_definition_id):
        """
        Sets the tag_definition_id of this CostTrackingTag.
        The tag definition id.


        :param tag_definition_id: The tag_definition_id of this CostTrackingTag.
        :type: str
        """
        self._tag_definition_id = tag_definition_id

    @property
    def tag_definition_name(self):
        """
        **[Required]** Gets the tag_definition_name of this CostTrackingTag.
        The tag definition name.


        :return: The tag_definition_name of this CostTrackingTag.
        :rtype: str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """
        Sets the tag_definition_name of this CostTrackingTag.
        The tag definition name.


        :param tag_definition_name: The tag_definition_name of this CostTrackingTag.
        :type: str
        """
        self._tag_definition_name = tag_definition_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
