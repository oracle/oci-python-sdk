# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .add_exadata_insight_members_details import AddExadataInsightMembersDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddEmManagedExternalExadataInsightMembersDetails(AddExadataInsightMembersDetails):
    """
    The information about the members of Exadata system to be added. If memberEntityDetails is not specified, the the Enterprise Manager entity (e.g. databases and hosts) associated with an Exadata system will be placed in the same compartment as the Exadata system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddEmManagedExternalExadataInsightMembersDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.AddEmManagedExternalExadataInsightMembersDetails.entity_source` attribute
        of this class is ``EM_MANAGED_EXTERNAL_EXADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this AddEmManagedExternalExadataInsightMembersDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_EXADATA"
        :type entity_source: str

        :param member_entity_details:
            The value to assign to the member_entity_details property of this AddEmManagedExternalExadataInsightMembersDetails.
        :type member_entity_details: list[oci.opsi.models.CreateEmManagedExternalExadataMemberEntityDetails]

        """
        self.swagger_types = {
            'entity_source': 'str',
            'member_entity_details': 'list[CreateEmManagedExternalExadataMemberEntityDetails]'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'member_entity_details': 'memberEntityDetails'
        }

        self._entity_source = None
        self._member_entity_details = None
        self._entity_source = 'EM_MANAGED_EXTERNAL_EXADATA'

    @property
    def member_entity_details(self):
        """
        Gets the member_entity_details of this AddEmManagedExternalExadataInsightMembersDetails.

        :return: The member_entity_details of this AddEmManagedExternalExadataInsightMembersDetails.
        :rtype: list[oci.opsi.models.CreateEmManagedExternalExadataMemberEntityDetails]
        """
        return self._member_entity_details

    @member_entity_details.setter
    def member_entity_details(self, member_entity_details):
        """
        Sets the member_entity_details of this AddEmManagedExternalExadataInsightMembersDetails.

        :param member_entity_details: The member_entity_details of this AddEmManagedExternalExadataInsightMembersDetails.
        :type: list[oci.opsi.models.CreateEmManagedExternalExadataMemberEntityDetails]
        """
        self._member_entity_details = member_entity_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
