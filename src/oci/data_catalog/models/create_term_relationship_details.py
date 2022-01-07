# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTermRelationshipDetails(object):
    """
    Properties used in term relationship create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTermRelationshipDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateTermRelationshipDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateTermRelationshipDetails.
        :type description: str

        :param related_term_key:
            The value to assign to the related_term_key property of this CreateTermRelationshipDetails.
        :type related_term_key: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'related_term_key': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'related_term_key': 'relatedTermKey'
        }

        self._display_name = None
        self._description = None
        self._related_term_key = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateTermRelationshipDetails.
        A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey'
        must be unique. Avoid entering confidential information. This is the same as 'relationshipType' for 'termRelationship'.


        :return: The display_name of this CreateTermRelationshipDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTermRelationshipDetails.
        A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey'
        must be unique. Avoid entering confidential information. This is the same as 'relationshipType' for 'termRelationship'.


        :param display_name: The display_name of this CreateTermRelationshipDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateTermRelationshipDetails.
        Detailed description of the term relationship usually defined at the time of creation.


        :return: The description of this CreateTermRelationshipDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTermRelationshipDetails.
        Detailed description of the term relationship usually defined at the time of creation.


        :param description: The description of this CreateTermRelationshipDetails.
        :type: str
        """
        self._description = description

    @property
    def related_term_key(self):
        """
        **[Required]** Gets the related_term_key of this CreateTermRelationshipDetails.
        Unique id of the related term.


        :return: The related_term_key of this CreateTermRelationshipDetails.
        :rtype: str
        """
        return self._related_term_key

    @related_term_key.setter
    def related_term_key(self, related_term_key):
        """
        Sets the related_term_key of this CreateTermRelationshipDetails.
        Unique id of the related term.


        :param related_term_key: The related_term_key of this CreateTermRelationshipDetails.
        :type: str
        """
        self._related_term_key = related_term_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
