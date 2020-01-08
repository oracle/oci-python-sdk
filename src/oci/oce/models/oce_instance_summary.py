# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OceInstanceSummary(object):
    """
    Summary of the OceInstance.
    """

    #: A constant which can be used with the lifecycle_state property of a OceInstanceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OceInstanceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OceInstanceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OceInstanceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OceInstanceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OceInstanceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OceInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OceInstanceSummary.
        :type id: str

        :param guid:
            The value to assign to the guid property of this OceInstanceSummary.
        :type guid: str

        :param description:
            The value to assign to the description property of this OceInstanceSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OceInstanceSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this OceInstanceSummary.
        :type name: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this OceInstanceSummary.
        :type tenancy_id: str

        :param idcs_tenancy:
            The value to assign to the idcs_tenancy property of this OceInstanceSummary.
        :type idcs_tenancy: str

        :param tenancy_name:
            The value to assign to the tenancy_name property of this OceInstanceSummary.
        :type tenancy_name: str

        :param object_storage_namespace:
            The value to assign to the object_storage_namespace property of this OceInstanceSummary.
        :type object_storage_namespace: str

        :param admin_email:
            The value to assign to the admin_email property of this OceInstanceSummary.
        :type admin_email: str

        :param time_created:
            The value to assign to the time_created property of this OceInstanceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OceInstanceSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OceInstanceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this OceInstanceSummary.
        :type state_message: str

        :param service:
            The value to assign to the service property of this OceInstanceSummary.
        :type service: dict(str, object)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OceInstanceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OceInstanceSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'guid': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'tenancy_id': 'str',
            'idcs_tenancy': 'str',
            'tenancy_name': 'str',
            'object_storage_namespace': 'str',
            'admin_email': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'state_message': 'str',
            'service': 'dict(str, object)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'guid': 'guid',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'tenancy_id': 'tenancyId',
            'idcs_tenancy': 'idcsTenancy',
            'tenancy_name': 'tenancyName',
            'object_storage_namespace': 'objectStorageNamespace',
            'admin_email': 'adminEmail',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage',
            'service': 'service',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._guid = None
        self._description = None
        self._compartment_id = None
        self._name = None
        self._tenancy_id = None
        self._idcs_tenancy = None
        self._tenancy_name = None
        self._object_storage_namespace = None
        self._admin_email = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._state_message = None
        self._service = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OceInstanceSummary.
        Unique identifier that is immutable on creation


        :return: The id of this OceInstanceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OceInstanceSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this OceInstanceSummary.
        :type: str
        """
        self._id = id

    @property
    def guid(self):
        """
        **[Required]** Gets the guid of this OceInstanceSummary.
        Unique GUID identifier that is immutable on creation


        :return: The guid of this OceInstanceSummary.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this OceInstanceSummary.
        Unique GUID identifier that is immutable on creation


        :param guid: The guid of this OceInstanceSummary.
        :type: str
        """
        self._guid = guid

    @property
    def description(self):
        """
        Gets the description of this OceInstanceSummary.
        OceInstance description, can be updated


        :return: The description of this OceInstanceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OceInstanceSummary.
        OceInstance description, can be updated


        :param description: The description of this OceInstanceSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OceInstanceSummary.
        Compartment Identifier


        :return: The compartment_id of this OceInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OceInstanceSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this OceInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OceInstanceSummary.
        OceInstance Name


        :return: The name of this OceInstanceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OceInstanceSummary.
        OceInstance Name


        :param name: The name of this OceInstanceSummary.
        :type: str
        """
        self._name = name

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this OceInstanceSummary.
        Tenancy Identifier


        :return: The tenancy_id of this OceInstanceSummary.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this OceInstanceSummary.
        Tenancy Identifier


        :param tenancy_id: The tenancy_id of this OceInstanceSummary.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def idcs_tenancy(self):
        """
        **[Required]** Gets the idcs_tenancy of this OceInstanceSummary.
        IDCS Tenancy Identifier


        :return: The idcs_tenancy of this OceInstanceSummary.
        :rtype: str
        """
        return self._idcs_tenancy

    @idcs_tenancy.setter
    def idcs_tenancy(self, idcs_tenancy):
        """
        Sets the idcs_tenancy of this OceInstanceSummary.
        IDCS Tenancy Identifier


        :param idcs_tenancy: The idcs_tenancy of this OceInstanceSummary.
        :type: str
        """
        self._idcs_tenancy = idcs_tenancy

    @property
    def tenancy_name(self):
        """
        **[Required]** Gets the tenancy_name of this OceInstanceSummary.
        Tenancy Name


        :return: The tenancy_name of this OceInstanceSummary.
        :rtype: str
        """
        return self._tenancy_name

    @tenancy_name.setter
    def tenancy_name(self, tenancy_name):
        """
        Sets the tenancy_name of this OceInstanceSummary.
        Tenancy Name


        :param tenancy_name: The tenancy_name of this OceInstanceSummary.
        :type: str
        """
        self._tenancy_name = tenancy_name

    @property
    def object_storage_namespace(self):
        """
        **[Required]** Gets the object_storage_namespace of this OceInstanceSummary.
        Object Storage Namespace of tenancy


        :return: The object_storage_namespace of this OceInstanceSummary.
        :rtype: str
        """
        return self._object_storage_namespace

    @object_storage_namespace.setter
    def object_storage_namespace(self, object_storage_namespace):
        """
        Sets the object_storage_namespace of this OceInstanceSummary.
        Object Storage Namespace of tenancy


        :param object_storage_namespace: The object_storage_namespace of this OceInstanceSummary.
        :type: str
        """
        self._object_storage_namespace = object_storage_namespace

    @property
    def admin_email(self):
        """
        **[Required]** Gets the admin_email of this OceInstanceSummary.
        Admin Email for Notification


        :return: The admin_email of this OceInstanceSummary.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this OceInstanceSummary.
        Admin Email for Notification


        :param admin_email: The admin_email of this OceInstanceSummary.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def time_created(self):
        """
        Gets the time_created of this OceInstanceSummary.
        The time the the OceInstance was created. An RFC3339 formatted datetime string


        :return: The time_created of this OceInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OceInstanceSummary.
        The time the the OceInstance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OceInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OceInstanceSummary.
        The time the OceInstance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this OceInstanceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OceInstanceSummary.
        The time the OceInstance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this OceInstanceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OceInstanceSummary.
        The current state of the file system.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OceInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OceInstanceSummary.
        The current state of the file system.


        :param lifecycle_state: The lifecycle_state of this OceInstanceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this OceInstanceSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this OceInstanceSummary.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this OceInstanceSummary.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this OceInstanceSummary.
        :type: str
        """
        self._state_message = state_message

    @property
    def service(self):
        """
        Gets the service of this OceInstanceSummary.
        SERVICE data.
        Example: `{\"service\": {\"IDCS\": \"value\"}}`


        :return: The service of this OceInstanceSummary.
        :rtype: dict(str, object)
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this OceInstanceSummary.
        SERVICE data.
        Example: `{\"service\": {\"IDCS\": \"value\"}}`


        :param service: The service of this OceInstanceSummary.
        :type: dict(str, object)
        """
        self._service = service

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OceInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OceInstanceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OceInstanceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OceInstanceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OceInstanceSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OceInstanceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OceInstanceSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OceInstanceSummary.
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
