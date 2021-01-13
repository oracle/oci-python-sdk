# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLogAnalyticsEntityDetails(object):
    """
    Details for new log analytics entity to be added.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLogAnalyticsEntityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateLogAnalyticsEntityDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLogAnalyticsEntityDetails.
        :type compartment_id: str

        :param entity_type_name:
            The value to assign to the entity_type_name property of this CreateLogAnalyticsEntityDetails.
        :type entity_type_name: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this CreateLogAnalyticsEntityDetails.
        :type management_agent_id: str

        :param cloud_resource_id:
            The value to assign to the cloud_resource_id property of this CreateLogAnalyticsEntityDetails.
        :type cloud_resource_id: str

        :param timezone_region:
            The value to assign to the timezone_region property of this CreateLogAnalyticsEntityDetails.
        :type timezone_region: str

        :param hostname:
            The value to assign to the hostname property of this CreateLogAnalyticsEntityDetails.
        :type hostname: str

        :param source_id:
            The value to assign to the source_id property of this CreateLogAnalyticsEntityDetails.
        :type source_id: str

        :param properties:
            The value to assign to the properties property of this CreateLogAnalyticsEntityDetails.
        :type properties: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLogAnalyticsEntityDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLogAnalyticsEntityDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'entity_type_name': 'str',
            'management_agent_id': 'str',
            'cloud_resource_id': 'str',
            'timezone_region': 'str',
            'hostname': 'str',
            'source_id': 'str',
            'properties': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'entity_type_name': 'entityTypeName',
            'management_agent_id': 'managementAgentId',
            'cloud_resource_id': 'cloudResourceId',
            'timezone_region': 'timezoneRegion',
            'hostname': 'hostname',
            'source_id': 'sourceId',
            'properties': 'properties',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._compartment_id = None
        self._entity_type_name = None
        self._management_agent_id = None
        self._cloud_resource_id = None
        self._timezone_region = None
        self._hostname = None
        self._source_id = None
        self._properties = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateLogAnalyticsEntityDetails.
        Log analytics entity name.


        :return: The name of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateLogAnalyticsEntityDetails.
        Log analytics entity name.


        :param name: The name of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateLogAnalyticsEntityDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateLogAnalyticsEntityDetails.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def entity_type_name(self):
        """
        **[Required]** Gets the entity_type_name of this CreateLogAnalyticsEntityDetails.
        Log analytics entity type name.


        :return: The entity_type_name of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._entity_type_name

    @entity_type_name.setter
    def entity_type_name(self, entity_type_name):
        """
        Sets the entity_type_name of this CreateLogAnalyticsEntityDetails.
        Log analytics entity type name.


        :param entity_type_name: The entity_type_name of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._entity_type_name = entity_type_name

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this CreateLogAnalyticsEntityDetails.
        The OCID of the Management Agent.


        :return: The management_agent_id of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this CreateLogAnalyticsEntityDetails.
        The OCID of the Management Agent.


        :param management_agent_id: The management_agent_id of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def cloud_resource_id(self):
        """
        Gets the cloud_resource_id of this CreateLogAnalyticsEntityDetails.
        The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
        represents a non-cloud resource that the customer may have on their premises.


        :return: The cloud_resource_id of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._cloud_resource_id

    @cloud_resource_id.setter
    def cloud_resource_id(self, cloud_resource_id):
        """
        Sets the cloud_resource_id of this CreateLogAnalyticsEntityDetails.
        The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
        represents a non-cloud resource that the customer may have on their premises.


        :param cloud_resource_id: The cloud_resource_id of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._cloud_resource_id = cloud_resource_id

    @property
    def timezone_region(self):
        """
        Gets the timezone_region of this CreateLogAnalyticsEntityDetails.
        The timezone region of the log analytics entity.


        :return: The timezone_region of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._timezone_region

    @timezone_region.setter
    def timezone_region(self, timezone_region):
        """
        Sets the timezone_region of this CreateLogAnalyticsEntityDetails.
        The timezone region of the log analytics entity.


        :param timezone_region: The timezone_region of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._timezone_region = timezone_region

    @property
    def hostname(self):
        """
        Gets the hostname of this CreateLogAnalyticsEntityDetails.
        The hostname where the entity represented here is actually present. This would be the output one would get if
        they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
        management agents host since logs may be collected remotely.


        :return: The hostname of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateLogAnalyticsEntityDetails.
        The hostname where the entity represented here is actually present. This would be the output one would get if
        they run `echo $HOSTNAME` on Linux or an equivalent OS command. This may be different from
        management agents host since logs may be collected remotely.


        :param hostname: The hostname of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def source_id(self):
        """
        Gets the source_id of this CreateLogAnalyticsEntityDetails.
        This indicates the type of source. It is primarily for Enterprise Manager Repository ID.


        :return: The source_id of this CreateLogAnalyticsEntityDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this CreateLogAnalyticsEntityDetails.
        This indicates the type of source. It is primarily for Enterprise Manager Repository ID.


        :param source_id: The source_id of this CreateLogAnalyticsEntityDetails.
        :type: str
        """
        self._source_id = source_id

    @property
    def properties(self):
        """
        Gets the properties of this CreateLogAnalyticsEntityDetails.
        The name/value pairs for parameter values to be used in file patterns specified in log sources.


        :return: The properties of this CreateLogAnalyticsEntityDetails.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateLogAnalyticsEntityDetails.
        The name/value pairs for parameter values to be used in file patterns specified in log sources.


        :param properties: The properties of this CreateLogAnalyticsEntityDetails.
        :type: dict(str, str)
        """
        self._properties = properties

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateLogAnalyticsEntityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateLogAnalyticsEntityDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateLogAnalyticsEntityDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateLogAnalyticsEntityDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateLogAnalyticsEntityDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateLogAnalyticsEntityDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateLogAnalyticsEntityDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateLogAnalyticsEntityDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
