# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisableAutoAssociationDetail(object):
    """
    The information required to disable log source auto-association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DisableAutoAssociationDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param delete_existing_associations:
            The value to assign to the delete_existing_associations property of this DisableAutoAssociationDetail.
        :type delete_existing_associations: bool

        """
        self.swagger_types = {
            'delete_existing_associations': 'bool'
        }

        self.attribute_map = {
            'delete_existing_associations': 'deleteExistingAssociations'
        }

        self._delete_existing_associations = None

    @property
    def delete_existing_associations(self):
        """
        Gets the delete_existing_associations of this DisableAutoAssociationDetail.
        A flag indicating whether or not to delete all the existing associations of the log source.


        :return: The delete_existing_associations of this DisableAutoAssociationDetail.
        :rtype: bool
        """
        return self._delete_existing_associations

    @delete_existing_associations.setter
    def delete_existing_associations(self, delete_existing_associations):
        """
        Sets the delete_existing_associations of this DisableAutoAssociationDetail.
        A flag indicating whether or not to delete all the existing associations of the log source.


        :param delete_existing_associations: The delete_existing_associations of this DisableAutoAssociationDetail.
        :type: bool
        """
        self._delete_existing_associations = delete_existing_associations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
