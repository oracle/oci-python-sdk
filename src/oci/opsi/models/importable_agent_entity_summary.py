# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportableAgentEntitySummary(object):
    """
    An agent entity that can be imported into Operations Insights.
    """

    #: A constant which can be used with the entity_source property of a ImportableAgentEntitySummary.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_HOST = "MACS_MANAGED_EXTERNAL_HOST"

    def __init__(self, **kwargs):
        """
        Initializes a new ImportableAgentEntitySummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.HostImportableAgentEntitySummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this ImportableAgentEntitySummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this ImportableAgentEntitySummary.
        :type management_agent_id: str

        :param management_agent_display_name:
            The value to assign to the management_agent_display_name property of this ImportableAgentEntitySummary.
        :type management_agent_display_name: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'management_agent_id': 'str',
            'management_agent_display_name': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'management_agent_id': 'managementAgentId',
            'management_agent_display_name': 'managementAgentDisplayName'
        }

        self._entity_source = None
        self._management_agent_id = None
        self._management_agent_display_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'MACS_MANAGED_EXTERNAL_HOST':
            return 'HostImportableAgentEntitySummary'
        else:
            return 'ImportableAgentEntitySummary'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this ImportableAgentEntitySummary.
        Source of the importable agent entity.

        Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this ImportableAgentEntitySummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this ImportableAgentEntitySummary.
        Source of the importable agent entity.


        :param entity_source: The entity_source of this ImportableAgentEntitySummary.
        :type: str
        """
        allowed_values = ["MACS_MANAGED_EXTERNAL_HOST"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def management_agent_id(self):
        """
        **[Required]** Gets the management_agent_id of this ImportableAgentEntitySummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this ImportableAgentEntitySummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this ImportableAgentEntitySummary.
        The `OCID`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this ImportableAgentEntitySummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def management_agent_display_name(self):
        """
        **[Required]** Gets the management_agent_display_name of this ImportableAgentEntitySummary.
        The `Display Name`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display


        :return: The management_agent_display_name of this ImportableAgentEntitySummary.
        :rtype: str
        """
        return self._management_agent_display_name

    @management_agent_display_name.setter
    def management_agent_display_name(self, management_agent_display_name):
        """
        Sets the management_agent_display_name of this ImportableAgentEntitySummary.
        The `Display Name`__ of the Management Agent

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Display


        :param management_agent_display_name: The management_agent_display_name of this ImportableAgentEntitySummary.
        :type: str
        """
        self._management_agent_display_name = management_agent_display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
