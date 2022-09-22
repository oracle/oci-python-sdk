# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveryJobSummary(object):
    """
    The Summary of DiscoveryJob details.
    """

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "WEBLOGIC_DOMAIN"
    RESOURCE_TYPE_WEBLOGIC_DOMAIN = "WEBLOGIC_DOMAIN"

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "EBS_INSTANCE"
    RESOURCE_TYPE_EBS_INSTANCE = "EBS_INSTANCE"

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "ORACLE_DATABASE"
    RESOURCE_TYPE_ORACLE_DATABASE = "ORACLE_DATABASE"

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "OCI_ORACLE_DB"
    RESOURCE_TYPE_OCI_ORACLE_DB = "OCI_ORACLE_DB"

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "OCI_ORACLE_CDB"
    RESOURCE_TYPE_OCI_ORACLE_CDB = "OCI_ORACLE_CDB"

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "OCI_ORACLE_PDB"
    RESOURCE_TYPE_OCI_ORACLE_PDB = "OCI_ORACLE_PDB"

    #: A constant which can be used with the resource_type property of a DiscoveryJobSummary.
    #: This constant has a value of "HOST"
    RESOURCE_TYPE_HOST = "HOST"

    #: A constant which can be used with the discovery_type property of a DiscoveryJobSummary.
    #: This constant has a value of "ADD"
    DISCOVERY_TYPE_ADD = "ADD"

    #: A constant which can be used with the discovery_type property of a DiscoveryJobSummary.
    #: This constant has a value of "ADD_WITH_RETRY"
    DISCOVERY_TYPE_ADD_WITH_RETRY = "ADD_WITH_RETRY"

    #: A constant which can be used with the discovery_type property of a DiscoveryJobSummary.
    #: This constant has a value of "REFRESH"
    DISCOVERY_TYPE_REFRESH = "REFRESH"

    #: A constant which can be used with the status property of a DiscoveryJobSummary.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the status property of a DiscoveryJobSummary.
    #: This constant has a value of "FAILURE"
    STATUS_FAILURE = "FAILURE"

    #: A constant which can be used with the status property of a DiscoveryJobSummary.
    #: This constant has a value of "INPROGRESS"
    STATUS_INPROGRESS = "INPROGRESS"

    #: A constant which can be used with the status property of a DiscoveryJobSummary.
    #: This constant has a value of "INACTIVE"
    STATUS_INACTIVE = "INACTIVE"

    #: A constant which can be used with the status property of a DiscoveryJobSummary.
    #: This constant has a value of "CREATED"
    STATUS_CREATED = "CREATED"

    #: A constant which can be used with the status property of a DiscoveryJobSummary.
    #: This constant has a value of "DELETED"
    STATUS_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJobSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJobSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJobSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJobSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJobSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DiscoveryJobSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveryJobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DiscoveryJobSummary.
        :type id: str

        :param resource_type:
            The value to assign to the resource_type property of this DiscoveryJobSummary.
            Allowed values for this property are: "WEBLOGIC_DOMAIN", "EBS_INSTANCE", "ORACLE_DATABASE", "OCI_ORACLE_DB", "OCI_ORACLE_CDB", "OCI_ORACLE_PDB", "HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param resource_name:
            The value to assign to the resource_name property of this DiscoveryJobSummary.
        :type resource_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DiscoveryJobSummary.
        :type compartment_id: str

        :param discovery_type:
            The value to assign to the discovery_type property of this DiscoveryJobSummary.
            Allowed values for this property are: "ADD", "ADD_WITH_RETRY", "REFRESH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type discovery_type: str

        :param status:
            The value to assign to the status property of this DiscoveryJobSummary.
            Allowed values for this property are: "SUCCESS", "FAILURE", "INPROGRESS", "INACTIVE", "CREATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_message:
            The value to assign to the status_message property of this DiscoveryJobSummary.
        :type status_message: str

        :param tenant_id:
            The value to assign to the tenant_id property of this DiscoveryJobSummary.
        :type tenant_id: str

        :param user_id:
            The value to assign to the user_id property of this DiscoveryJobSummary.
        :type user_id: str

        :param time_updated:
            The value to assign to the time_updated property of this DiscoveryJobSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DiscoveryJobSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DiscoveryJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DiscoveryJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DiscoveryJobSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'resource_type': 'str',
            'resource_name': 'str',
            'compartment_id': 'str',
            'discovery_type': 'str',
            'status': 'str',
            'status_message': 'str',
            'tenant_id': 'str',
            'user_id': 'str',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'resource_type': 'resourceType',
            'resource_name': 'resourceName',
            'compartment_id': 'compartmentId',
            'discovery_type': 'discoveryType',
            'status': 'status',
            'status_message': 'statusMessage',
            'tenant_id': 'tenantId',
            'user_id': 'userId',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._resource_type = None
        self._resource_name = None
        self._compartment_id = None
        self._discovery_type = None
        self._status = None
        self._status_message = None
        self._tenant_id = None
        self._user_id = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DiscoveryJobSummary.
        The OCID of Discovery job


        :return: The id of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DiscoveryJobSummary.
        The OCID of Discovery job


        :param id: The id of this DiscoveryJobSummary.
        :type: str
        """
        self._id = id

    @property
    def resource_type(self):
        """
        Gets the resource_type of this DiscoveryJobSummary.
        Resource Type

        Allowed values for this property are: "WEBLOGIC_DOMAIN", "EBS_INSTANCE", "ORACLE_DATABASE", "OCI_ORACLE_DB", "OCI_ORACLE_CDB", "OCI_ORACLE_PDB", "HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this DiscoveryJobSummary.
        Resource Type


        :param resource_type: The resource_type of this DiscoveryJobSummary.
        :type: str
        """
        allowed_values = ["WEBLOGIC_DOMAIN", "EBS_INSTANCE", "ORACLE_DATABASE", "OCI_ORACLE_DB", "OCI_ORACLE_CDB", "OCI_ORACLE_PDB", "HOST"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """
        Gets the resource_name of this DiscoveryJobSummary.
        The name of resource type


        :return: The resource_name of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this DiscoveryJobSummary.
        The name of resource type


        :param resource_name: The resource_name of this DiscoveryJobSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DiscoveryJobSummary.
        The OCID of the Compartment


        :return: The compartment_id of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DiscoveryJobSummary.
        The OCID of the Compartment


        :param compartment_id: The compartment_id of this DiscoveryJobSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def discovery_type(self):
        """
        Gets the discovery_type of this DiscoveryJobSummary.
        Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered resources.

        Allowed values for this property are: "ADD", "ADD_WITH_RETRY", "REFRESH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The discovery_type of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """
        Sets the discovery_type of this DiscoveryJobSummary.
        Add option submits new discovery Job. Add with retry option to re-submit failed discovery job. Refresh option refreshes the existing discovered resources.


        :param discovery_type: The discovery_type of this DiscoveryJobSummary.
        :type: str
        """
        allowed_values = ["ADD", "ADD_WITH_RETRY", "REFRESH"]
        if not value_allowed_none_or_none_sentinel(discovery_type, allowed_values):
            discovery_type = 'UNKNOWN_ENUM_VALUE'
        self._discovery_type = discovery_type

    @property
    def status(self):
        """
        Gets the status of this DiscoveryJobSummary.
        Specifies the status of the discovery job

        Allowed values for this property are: "SUCCESS", "FAILURE", "INPROGRESS", "INACTIVE", "CREATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DiscoveryJobSummary.
        Specifies the status of the discovery job


        :param status: The status of this DiscoveryJobSummary.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE", "INPROGRESS", "INACTIVE", "CREATED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_message(self):
        """
        Gets the status_message of this DiscoveryJobSummary.
        The short summary of the status of the discovery job


        :return: The status_message of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this DiscoveryJobSummary.
        The short summary of the status of the discovery job


        :param status_message: The status_message of this DiscoveryJobSummary.
        :type: str
        """
        self._status_message = status_message

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this DiscoveryJobSummary.
        The OCID of Tenant


        :return: The tenant_id of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this DiscoveryJobSummary.
        The OCID of Tenant


        :param tenant_id: The tenant_id of this DiscoveryJobSummary.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def user_id(self):
        """
        Gets the user_id of this DiscoveryJobSummary.
        The OCID of user in which the job is submitted


        :return: The user_id of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this DiscoveryJobSummary.
        The OCID of user in which the job is submitted


        :param user_id: The user_id of this DiscoveryJobSummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DiscoveryJobSummary.
        The time the discovery Job was updated.


        :return: The time_updated of this DiscoveryJobSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DiscoveryJobSummary.
        The time the discovery Job was updated.


        :param time_updated: The time_updated of this DiscoveryJobSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DiscoveryJobSummary.
        The current state of the DiscoveryJob Resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DiscoveryJobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DiscoveryJobSummary.
        The current state of the DiscoveryJob Resource.


        :param lifecycle_state: The lifecycle_state of this DiscoveryJobSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DiscoveryJobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DiscoveryJobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DiscoveryJobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DiscoveryJobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DiscoveryJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DiscoveryJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DiscoveryJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DiscoveryJobSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DiscoveryJobSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DiscoveryJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DiscoveryJobSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DiscoveryJobSummary.
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
