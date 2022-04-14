# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceAssociation(object):
    """
    Association between two monitored resources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceAssociation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param association_type:
            The value to assign to the association_type property of this MonitoredResourceAssociation.
        :type association_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredResourceAssociation.
        :type compartment_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this MonitoredResourceAssociation.
        :type tenant_id: str

        :param source_resource_id:
            The value to assign to the source_resource_id property of this MonitoredResourceAssociation.
        :type source_resource_id: str

        :param destination_resource_id:
            The value to assign to the destination_resource_id property of this MonitoredResourceAssociation.
        :type destination_resource_id: str

        :param source_resource_details:
            The value to assign to the source_resource_details property of this MonitoredResourceAssociation.
        :type source_resource_details: oci.stack_monitoring.models.AssociationResourceDetails

        :param destination_resource_details:
            The value to assign to the destination_resource_details property of this MonitoredResourceAssociation.
        :type destination_resource_details: oci.stack_monitoring.models.AssociationResourceDetails

        :param time_created:
            The value to assign to the time_created property of this MonitoredResourceAssociation.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoredResourceAssociation.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoredResourceAssociation.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoredResourceAssociation.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'association_type': 'str',
            'compartment_id': 'str',
            'tenant_id': 'str',
            'source_resource_id': 'str',
            'destination_resource_id': 'str',
            'source_resource_details': 'AssociationResourceDetails',
            'destination_resource_details': 'AssociationResourceDetails',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'association_type': 'associationType',
            'compartment_id': 'compartmentId',
            'tenant_id': 'tenantId',
            'source_resource_id': 'sourceResourceId',
            'destination_resource_id': 'destinationResourceId',
            'source_resource_details': 'sourceResourceDetails',
            'destination_resource_details': 'destinationResourceDetails',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._association_type = None
        self._compartment_id = None
        self._tenant_id = None
        self._source_resource_id = None
        self._destination_resource_id = None
        self._source_resource_details = None
        self._destination_resource_details = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def association_type(self):
        """
        **[Required]** Gets the association_type of this MonitoredResourceAssociation.
        Association Type


        :return: The association_type of this MonitoredResourceAssociation.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """
        Sets the association_type of this MonitoredResourceAssociation.
        Association Type


        :param association_type: The association_type of this MonitoredResourceAssociation.
        :type: str
        """
        self._association_type = association_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoredResourceAssociation.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredResourceAssociation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredResourceAssociation.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredResourceAssociation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this MonitoredResourceAssociation.
        Tenancy Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenant_id of this MonitoredResourceAssociation.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MonitoredResourceAssociation.
        Tenancy Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenant_id: The tenant_id of this MonitoredResourceAssociation.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def source_resource_id(self):
        """
        **[Required]** Gets the source_resource_id of this MonitoredResourceAssociation.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_resource_id of this MonitoredResourceAssociation.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        """
        Sets the source_resource_id of this MonitoredResourceAssociation.
        Source Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_resource_id: The source_resource_id of this MonitoredResourceAssociation.
        :type: str
        """
        self._source_resource_id = source_resource_id

    @property
    def destination_resource_id(self):
        """
        **[Required]** Gets the destination_resource_id of this MonitoredResourceAssociation.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The destination_resource_id of this MonitoredResourceAssociation.
        :rtype: str
        """
        return self._destination_resource_id

    @destination_resource_id.setter
    def destination_resource_id(self, destination_resource_id):
        """
        Sets the destination_resource_id of this MonitoredResourceAssociation.
        Destination Monitored Resource Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param destination_resource_id: The destination_resource_id of this MonitoredResourceAssociation.
        :type: str
        """
        self._destination_resource_id = destination_resource_id

    @property
    def source_resource_details(self):
        """
        Gets the source_resource_details of this MonitoredResourceAssociation.

        :return: The source_resource_details of this MonitoredResourceAssociation.
        :rtype: oci.stack_monitoring.models.AssociationResourceDetails
        """
        return self._source_resource_details

    @source_resource_details.setter
    def source_resource_details(self, source_resource_details):
        """
        Sets the source_resource_details of this MonitoredResourceAssociation.

        :param source_resource_details: The source_resource_details of this MonitoredResourceAssociation.
        :type: oci.stack_monitoring.models.AssociationResourceDetails
        """
        self._source_resource_details = source_resource_details

    @property
    def destination_resource_details(self):
        """
        Gets the destination_resource_details of this MonitoredResourceAssociation.

        :return: The destination_resource_details of this MonitoredResourceAssociation.
        :rtype: oci.stack_monitoring.models.AssociationResourceDetails
        """
        return self._destination_resource_details

    @destination_resource_details.setter
    def destination_resource_details(self, destination_resource_details):
        """
        Sets the destination_resource_details of this MonitoredResourceAssociation.

        :param destination_resource_details: The destination_resource_details of this MonitoredResourceAssociation.
        :type: oci.stack_monitoring.models.AssociationResourceDetails
        """
        self._destination_resource_details = destination_resource_details

    @property
    def time_created(self):
        """
        Gets the time_created of this MonitoredResourceAssociation.
        The time when the association was created. An RFC3339 formatted datetime string


        :return: The time_created of this MonitoredResourceAssociation.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoredResourceAssociation.
        The time when the association was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MonitoredResourceAssociation.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoredResourceAssociation.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoredResourceAssociation.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoredResourceAssociation.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoredResourceAssociation.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoredResourceAssociation.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoredResourceAssociation.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoredResourceAssociation.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoredResourceAssociation.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoredResourceAssociation.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoredResourceAssociation.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoredResourceAssociation.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoredResourceAssociation.
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
