# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveEntityAssociationsDetails(object):
    """
    Information about the associations to be deleted between source entity and other existing destination entities.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveEntityAssociationsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param association_entities:
            The value to assign to the association_entities property of this RemoveEntityAssociationsDetails.
        :type association_entities: list[str]

        """
        self.swagger_types = {
            'association_entities': 'list[str]'
        }

        self.attribute_map = {
            'association_entities': 'associationEntities'
        }

        self._association_entities = None

    @property
    def association_entities(self):
        """
        **[Required]** Gets the association_entities of this RemoveEntityAssociationsDetails.
        Destination entities OCIDs with which associations are to be deleted


        :return: The association_entities of this RemoveEntityAssociationsDetails.
        :rtype: list[str]
        """
        return self._association_entities

    @association_entities.setter
    def association_entities(self, association_entities):
        """
        Sets the association_entities of this RemoveEntityAssociationsDetails.
        Destination entities OCIDs with which associations are to be deleted


        :param association_entities: The association_entities of this RemoveEntityAssociationsDetails.
        :type: list[str]
        """
        self._association_entities = association_entities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
