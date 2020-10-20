# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseInsightSummary(object):
    """
    Partial definition of the database insight resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseInsightSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_id:
            The value to assign to the database_id property of this DatabaseInsightSummary.
        :type database_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseInsightSummary.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this DatabaseInsightSummary.
        :type database_name: str

        :param database_display_name:
            The value to assign to the database_display_name property of this DatabaseInsightSummary.
        :type database_display_name: str

        :param database_type:
            The value to assign to the database_type property of this DatabaseInsightSummary.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this DatabaseInsightSummary.
        :type database_version: str

        :param database_host_names:
            The value to assign to the database_host_names property of this DatabaseInsightSummary.
        :type database_host_names: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'database_id': 'str',
            'compartment_id': 'str',
            'database_name': 'str',
            'database_display_name': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'database_host_names': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'database_id': 'databaseId',
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_display_name': 'databaseDisplayName',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'database_host_names': 'databaseHostNames',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._database_id = None
        self._compartment_id = None
        self._database_name = None
        self._database_display_name = None
        self._database_type = None
        self._database_version = None
        self._database_host_names = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this DatabaseInsightSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DatabaseInsightSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DatabaseInsightSummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DatabaseInsightSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DatabaseInsightSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseInsightSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseInsightSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseInsightSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_name(self):
        """
        Gets the database_name of this DatabaseInsightSummary.
        The database name. The database name is unique within the tenancy.


        :return: The database_name of this DatabaseInsightSummary.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this DatabaseInsightSummary.
        The database name. The database name is unique within the tenancy.


        :param database_name: The database_name of this DatabaseInsightSummary.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_display_name(self):
        """
        Gets the database_display_name of this DatabaseInsightSummary.
        The user-friendly name for the database. The name does not have to be unique.


        :return: The database_display_name of this DatabaseInsightSummary.
        :rtype: str
        """
        return self._database_display_name

    @database_display_name.setter
    def database_display_name(self, database_display_name):
        """
        Sets the database_display_name of this DatabaseInsightSummary.
        The user-friendly name for the database. The name does not have to be unique.


        :param database_display_name: The database_display_name of this DatabaseInsightSummary.
        :type: str
        """
        self._database_display_name = database_display_name

    @property
    def database_type(self):
        """
        Gets the database_type of this DatabaseInsightSummary.
        Operations Insights internal representation of the database type.


        :return: The database_type of this DatabaseInsightSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseInsightSummary.
        Operations Insights internal representation of the database type.


        :param database_type: The database_type of this DatabaseInsightSummary.
        :type: str
        """
        self._database_type = database_type

    @property
    def database_version(self):
        """
        Gets the database_version of this DatabaseInsightSummary.
        The version of the database.


        :return: The database_version of this DatabaseInsightSummary.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this DatabaseInsightSummary.
        The version of the database.


        :param database_version: The database_version of this DatabaseInsightSummary.
        :type: str
        """
        self._database_version = database_version

    @property
    def database_host_names(self):
        """
        Gets the database_host_names of this DatabaseInsightSummary.
        The hostnames for the database.


        :return: The database_host_names of this DatabaseInsightSummary.
        :rtype: list[str]
        """
        return self._database_host_names

    @database_host_names.setter
    def database_host_names(self, database_host_names):
        """
        Sets the database_host_names of this DatabaseInsightSummary.
        The hostnames for the database.


        :param database_host_names: The database_host_names of this DatabaseInsightSummary.
        :type: list[str]
        """
        self._database_host_names = database_host_names

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatabaseInsightSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseInsightSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseInsightSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseInsightSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatabaseInsightSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseInsightSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseInsightSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseInsightSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatabaseInsightSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DatabaseInsightSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatabaseInsightSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DatabaseInsightSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
