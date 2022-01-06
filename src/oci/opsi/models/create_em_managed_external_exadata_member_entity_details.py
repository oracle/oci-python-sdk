# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEmManagedExternalExadataMemberEntityDetails(object):
    """
    Compartment `OCID`__ of the Enterprise Manager member entity (e.g. databases and hosts) associated with an Exadata system.

    __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEmManagedExternalExadataMemberEntityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this CreateEmManagedExternalExadataMemberEntityDetails.
        :type enterprise_manager_entity_identifier: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEmManagedExternalExadataMemberEntityDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'enterprise_manager_entity_identifier': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'compartment_id': 'compartmentId'
        }

        self._enterprise_manager_entity_identifier = None
        self._compartment_id = None

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataMemberEntityDetails.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataMemberEntityDetails.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataMemberEntityDetails.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this CreateEmManagedExternalExadataMemberEntityDetails.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateEmManagedExternalExadataMemberEntityDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateEmManagedExternalExadataMemberEntityDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateEmManagedExternalExadataMemberEntityDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateEmManagedExternalExadataMemberEntityDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
