# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportableEnterpriseManagerEntity(object):
    """
    An Enterprise Manager entity that can be imported into Operations Insights.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportableEnterpriseManagerEntity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param enterprise_manager_identifier:
            The value to assign to the enterprise_manager_identifier property of this ImportableEnterpriseManagerEntity.
        :type enterprise_manager_identifier: str

        :param enterprise_manager_entity_name:
            The value to assign to the enterprise_manager_entity_name property of this ImportableEnterpriseManagerEntity.
        :type enterprise_manager_entity_name: str

        :param enterprise_manager_entity_type:
            The value to assign to the enterprise_manager_entity_type property of this ImportableEnterpriseManagerEntity.
        :type enterprise_manager_entity_type: str

        :param enterprise_manager_entity_identifier:
            The value to assign to the enterprise_manager_entity_identifier property of this ImportableEnterpriseManagerEntity.
        :type enterprise_manager_entity_identifier: str

        :param opsi_entity_type:
            The value to assign to the opsi_entity_type property of this ImportableEnterpriseManagerEntity.
        :type opsi_entity_type: str

        """
        self.swagger_types = {
            'enterprise_manager_identifier': 'str',
            'enterprise_manager_entity_name': 'str',
            'enterprise_manager_entity_type': 'str',
            'enterprise_manager_entity_identifier': 'str',
            'opsi_entity_type': 'str'
        }

        self.attribute_map = {
            'enterprise_manager_identifier': 'enterpriseManagerIdentifier',
            'enterprise_manager_entity_name': 'enterpriseManagerEntityName',
            'enterprise_manager_entity_type': 'enterpriseManagerEntityType',
            'enterprise_manager_entity_identifier': 'enterpriseManagerEntityIdentifier',
            'opsi_entity_type': 'opsiEntityType'
        }

        self._enterprise_manager_identifier = None
        self._enterprise_manager_entity_name = None
        self._enterprise_manager_entity_type = None
        self._enterprise_manager_entity_identifier = None
        self._opsi_entity_type = None

    @property
    def enterprise_manager_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_identifier of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Unique Identifier


        :return: The enterprise_manager_identifier of this ImportableEnterpriseManagerEntity.
        :rtype: str
        """
        return self._enterprise_manager_identifier

    @enterprise_manager_identifier.setter
    def enterprise_manager_identifier(self, enterprise_manager_identifier):
        """
        Sets the enterprise_manager_identifier of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Unique Identifier


        :param enterprise_manager_identifier: The enterprise_manager_identifier of this ImportableEnterpriseManagerEntity.
        :type: str
        """
        self._enterprise_manager_identifier = enterprise_manager_identifier

    @property
    def enterprise_manager_entity_name(self):
        """
        **[Required]** Gets the enterprise_manager_entity_name of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Entity Name


        :return: The enterprise_manager_entity_name of this ImportableEnterpriseManagerEntity.
        :rtype: str
        """
        return self._enterprise_manager_entity_name

    @enterprise_manager_entity_name.setter
    def enterprise_manager_entity_name(self, enterprise_manager_entity_name):
        """
        Sets the enterprise_manager_entity_name of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Entity Name


        :param enterprise_manager_entity_name: The enterprise_manager_entity_name of this ImportableEnterpriseManagerEntity.
        :type: str
        """
        self._enterprise_manager_entity_name = enterprise_manager_entity_name

    @property
    def enterprise_manager_entity_type(self):
        """
        **[Required]** Gets the enterprise_manager_entity_type of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Entity Type


        :return: The enterprise_manager_entity_type of this ImportableEnterpriseManagerEntity.
        :rtype: str
        """
        return self._enterprise_manager_entity_type

    @enterprise_manager_entity_type.setter
    def enterprise_manager_entity_type(self, enterprise_manager_entity_type):
        """
        Sets the enterprise_manager_entity_type of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Entity Type


        :param enterprise_manager_entity_type: The enterprise_manager_entity_type of this ImportableEnterpriseManagerEntity.
        :type: str
        """
        self._enterprise_manager_entity_type = enterprise_manager_entity_type

    @property
    def enterprise_manager_entity_identifier(self):
        """
        **[Required]** Gets the enterprise_manager_entity_identifier of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Entity Unique Identifier


        :return: The enterprise_manager_entity_identifier of this ImportableEnterpriseManagerEntity.
        :rtype: str
        """
        return self._enterprise_manager_entity_identifier

    @enterprise_manager_entity_identifier.setter
    def enterprise_manager_entity_identifier(self, enterprise_manager_entity_identifier):
        """
        Sets the enterprise_manager_entity_identifier of this ImportableEnterpriseManagerEntity.
        Enterprise Manager Entity Unique Identifier


        :param enterprise_manager_entity_identifier: The enterprise_manager_entity_identifier of this ImportableEnterpriseManagerEntity.
        :type: str
        """
        self._enterprise_manager_entity_identifier = enterprise_manager_entity_identifier

    @property
    def opsi_entity_type(self):
        """
        Gets the opsi_entity_type of this ImportableEnterpriseManagerEntity.
        Operations Insights internal representation of the resource type.


        :return: The opsi_entity_type of this ImportableEnterpriseManagerEntity.
        :rtype: str
        """
        return self._opsi_entity_type

    @opsi_entity_type.setter
    def opsi_entity_type(self, opsi_entity_type):
        """
        Sets the opsi_entity_type of this ImportableEnterpriseManagerEntity.
        Operations Insights internal representation of the resource type.


        :param opsi_entity_type: The opsi_entity_type of this ImportableEnterpriseManagerEntity.
        :type: str
        """
        self._opsi_entity_type = opsi_entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
