# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OceInstance(object):
    """
    Details of OceInstance.
    """

    #: A constant which can be used with the upgrade_schedule property of a OceInstance.
    #: This constant has a value of "UPGRADE_IMMEDIATELY"
    UPGRADE_SCHEDULE_UPGRADE_IMMEDIATELY = "UPGRADE_IMMEDIATELY"

    #: A constant which can be used with the upgrade_schedule property of a OceInstance.
    #: This constant has a value of "DELAYED_UPGRADE"
    UPGRADE_SCHEDULE_DELAYED_UPGRADE = "DELAYED_UPGRADE"

    #: A constant which can be used with the instance_usage_type property of a OceInstance.
    #: This constant has a value of "PRIMARY"
    INSTANCE_USAGE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the instance_usage_type property of a OceInstance.
    #: This constant has a value of "NONPRIMARY"
    INSTANCE_USAGE_TYPE_NONPRIMARY = "NONPRIMARY"

    #: A constant which can be used with the instance_access_type property of a OceInstance.
    #: This constant has a value of "PUBLIC"
    INSTANCE_ACCESS_TYPE_PUBLIC = "PUBLIC"

    #: A constant which can be used with the instance_access_type property of a OceInstance.
    #: This constant has a value of "PRIVATE"
    INSTANCE_ACCESS_TYPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the instance_license_type property of a OceInstance.
    #: This constant has a value of "NEW"
    INSTANCE_LICENSE_TYPE_NEW = "NEW"

    #: A constant which can be used with the instance_license_type property of a OceInstance.
    #: This constant has a value of "BYOL"
    INSTANCE_LICENSE_TYPE_BYOL = "BYOL"

    #: A constant which can be used with the instance_license_type property of a OceInstance.
    #: This constant has a value of "PREMIUM"
    INSTANCE_LICENSE_TYPE_PREMIUM = "PREMIUM"

    #: A constant which can be used with the instance_license_type property of a OceInstance.
    #: This constant has a value of "STARTER"
    INSTANCE_LICENSE_TYPE_STARTER = "STARTER"

    #: A constant which can be used with the lifecycle_state property of a OceInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OceInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OceInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OceInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OceInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OceInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a OceInstance.
    #: This constant has a value of "STANDBY"
    LIFECYCLE_DETAILS_STANDBY = "STANDBY"

    #: A constant which can be used with the lifecycle_details property of a OceInstance.
    #: This constant has a value of "FAILOVER"
    LIFECYCLE_DETAILS_FAILOVER = "FAILOVER"

    #: A constant which can be used with the lifecycle_details property of a OceInstance.
    #: This constant has a value of "DOWN"
    LIFECYCLE_DETAILS_DOWN = "DOWN"

    #: A constant which can be used with the lifecycle_details property of a OceInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_DETAILS_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new OceInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OceInstance.
        :type id: str

        :param guid:
            The value to assign to the guid property of this OceInstance.
        :type guid: str

        :param description:
            The value to assign to the description property of this OceInstance.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OceInstance.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this OceInstance.
        :type name: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this OceInstance.
        :type tenancy_id: str

        :param idcs_tenancy:
            The value to assign to the idcs_tenancy property of this OceInstance.
        :type idcs_tenancy: str

        :param tenancy_name:
            The value to assign to the tenancy_name property of this OceInstance.
        :type tenancy_name: str

        :param upgrade_schedule:
            The value to assign to the upgrade_schedule property of this OceInstance.
            Allowed values for this property are: "UPGRADE_IMMEDIATELY", "DELAYED_UPGRADE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type upgrade_schedule: str

        :param identity_stripe:
            The value to assign to the identity_stripe property of this OceInstance.
        :type identity_stripe: oci.oce.models.IdentityStripeDetails

        :param instance_usage_type:
            The value to assign to the instance_usage_type property of this OceInstance.
            Allowed values for this property are: "PRIMARY", "NONPRIMARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type instance_usage_type: str

        :param add_on_features:
            The value to assign to the add_on_features property of this OceInstance.
        :type add_on_features: list[str]

        :param object_storage_namespace:
            The value to assign to the object_storage_namespace property of this OceInstance.
        :type object_storage_namespace: str

        :param admin_email:
            The value to assign to the admin_email property of this OceInstance.
        :type admin_email: str

        :param waf_primary_domain:
            The value to assign to the waf_primary_domain property of this OceInstance.
        :type waf_primary_domain: str

        :param instance_access_type:
            The value to assign to the instance_access_type property of this OceInstance.
            Allowed values for this property are: "PUBLIC", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type instance_access_type: str

        :param instance_license_type:
            The value to assign to the instance_license_type property of this OceInstance.
            Allowed values for this property are: "NEW", "BYOL", "PREMIUM", "STARTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type instance_license_type: str

        :param time_created:
            The value to assign to the time_created property of this OceInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OceInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OceInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OceInstance.
            Allowed values for this property are: "STANDBY", "FAILOVER", "DOWN", "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param state_message:
            The value to assign to the state_message property of this OceInstance.
        :type state_message: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OceInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OceInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OceInstance.
        :type system_tags: dict(str, dict(str, object))

        :param service:
            The value to assign to the service property of this OceInstance.
        :type service: dict(str, object)

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
            'upgrade_schedule': 'str',
            'identity_stripe': 'IdentityStripeDetails',
            'instance_usage_type': 'str',
            'add_on_features': 'list[str]',
            'object_storage_namespace': 'str',
            'admin_email': 'str',
            'waf_primary_domain': 'str',
            'instance_access_type': 'str',
            'instance_license_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'state_message': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'service': 'dict(str, object)'
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
            'upgrade_schedule': 'upgradeSchedule',
            'identity_stripe': 'identityStripe',
            'instance_usage_type': 'instanceUsageType',
            'add_on_features': 'addOnFeatures',
            'object_storage_namespace': 'objectStorageNamespace',
            'admin_email': 'adminEmail',
            'waf_primary_domain': 'wafPrimaryDomain',
            'instance_access_type': 'instanceAccessType',
            'instance_license_type': 'instanceLicenseType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'state_message': 'stateMessage',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'service': 'service'
        }

        self._id = None
        self._guid = None
        self._description = None
        self._compartment_id = None
        self._name = None
        self._tenancy_id = None
        self._idcs_tenancy = None
        self._tenancy_name = None
        self._upgrade_schedule = None
        self._identity_stripe = None
        self._instance_usage_type = None
        self._add_on_features = None
        self._object_storage_namespace = None
        self._admin_email = None
        self._waf_primary_domain = None
        self._instance_access_type = None
        self._instance_license_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._state_message = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._service = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OceInstance.
        Unique identifier that is immutable on creation


        :return: The id of this OceInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OceInstance.
        Unique identifier that is immutable on creation


        :param id: The id of this OceInstance.
        :type: str
        """
        self._id = id

    @property
    def guid(self):
        """
        **[Required]** Gets the guid of this OceInstance.
        Unique GUID identifier that is immutable on creation


        :return: The guid of this OceInstance.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this OceInstance.
        Unique GUID identifier that is immutable on creation


        :param guid: The guid of this OceInstance.
        :type: str
        """
        self._guid = guid

    @property
    def description(self):
        """
        Gets the description of this OceInstance.
        OceInstance description, can be updated


        :return: The description of this OceInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OceInstance.
        OceInstance description, can be updated


        :param description: The description of this OceInstance.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OceInstance.
        Compartment Identifier


        :return: The compartment_id of this OceInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OceInstance.
        Compartment Identifier


        :param compartment_id: The compartment_id of this OceInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OceInstance.
        OceInstance Name


        :return: The name of this OceInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OceInstance.
        OceInstance Name


        :param name: The name of this OceInstance.
        :type: str
        """
        self._name = name

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this OceInstance.
        Tenancy Identifier


        :return: The tenancy_id of this OceInstance.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this OceInstance.
        Tenancy Identifier


        :param tenancy_id: The tenancy_id of this OceInstance.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def idcs_tenancy(self):
        """
        **[Required]** Gets the idcs_tenancy of this OceInstance.
        IDCS Tenancy Identifier


        :return: The idcs_tenancy of this OceInstance.
        :rtype: str
        """
        return self._idcs_tenancy

    @idcs_tenancy.setter
    def idcs_tenancy(self, idcs_tenancy):
        """
        Sets the idcs_tenancy of this OceInstance.
        IDCS Tenancy Identifier


        :param idcs_tenancy: The idcs_tenancy of this OceInstance.
        :type: str
        """
        self._idcs_tenancy = idcs_tenancy

    @property
    def tenancy_name(self):
        """
        **[Required]** Gets the tenancy_name of this OceInstance.
        Tenancy Name


        :return: The tenancy_name of this OceInstance.
        :rtype: str
        """
        return self._tenancy_name

    @tenancy_name.setter
    def tenancy_name(self, tenancy_name):
        """
        Sets the tenancy_name of this OceInstance.
        Tenancy Name


        :param tenancy_name: The tenancy_name of this OceInstance.
        :type: str
        """
        self._tenancy_name = tenancy_name

    @property
    def upgrade_schedule(self):
        """
        Gets the upgrade_schedule of this OceInstance.
        Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
        or delay upgrade of the service to previous released version

        Allowed values for this property are: "UPGRADE_IMMEDIATELY", "DELAYED_UPGRADE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The upgrade_schedule of this OceInstance.
        :rtype: str
        """
        return self._upgrade_schedule

    @upgrade_schedule.setter
    def upgrade_schedule(self, upgrade_schedule):
        """
        Sets the upgrade_schedule of this OceInstance.
        Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
        or delay upgrade of the service to previous released version


        :param upgrade_schedule: The upgrade_schedule of this OceInstance.
        :type: str
        """
        allowed_values = ["UPGRADE_IMMEDIATELY", "DELAYED_UPGRADE"]
        if not value_allowed_none_or_none_sentinel(upgrade_schedule, allowed_values):
            upgrade_schedule = 'UNKNOWN_ENUM_VALUE'
        self._upgrade_schedule = upgrade_schedule

    @property
    def identity_stripe(self):
        """
        Gets the identity_stripe of this OceInstance.

        :return: The identity_stripe of this OceInstance.
        :rtype: oci.oce.models.IdentityStripeDetails
        """
        return self._identity_stripe

    @identity_stripe.setter
    def identity_stripe(self, identity_stripe):
        """
        Sets the identity_stripe of this OceInstance.

        :param identity_stripe: The identity_stripe of this OceInstance.
        :type: oci.oce.models.IdentityStripeDetails
        """
        self._identity_stripe = identity_stripe

    @property
    def instance_usage_type(self):
        """
        Gets the instance_usage_type of this OceInstance.
        Instance type based on its usage

        Allowed values for this property are: "PRIMARY", "NONPRIMARY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The instance_usage_type of this OceInstance.
        :rtype: str
        """
        return self._instance_usage_type

    @instance_usage_type.setter
    def instance_usage_type(self, instance_usage_type):
        """
        Sets the instance_usage_type of this OceInstance.
        Instance type based on its usage


        :param instance_usage_type: The instance_usage_type of this OceInstance.
        :type: str
        """
        allowed_values = ["PRIMARY", "NONPRIMARY"]
        if not value_allowed_none_or_none_sentinel(instance_usage_type, allowed_values):
            instance_usage_type = 'UNKNOWN_ENUM_VALUE'
        self._instance_usage_type = instance_usage_type

    @property
    def add_on_features(self):
        """
        Gets the add_on_features of this OceInstance.
        a list of add-on features for the ocm instance


        :return: The add_on_features of this OceInstance.
        :rtype: list[str]
        """
        return self._add_on_features

    @add_on_features.setter
    def add_on_features(self, add_on_features):
        """
        Sets the add_on_features of this OceInstance.
        a list of add-on features for the ocm instance


        :param add_on_features: The add_on_features of this OceInstance.
        :type: list[str]
        """
        self._add_on_features = add_on_features

    @property
    def object_storage_namespace(self):
        """
        **[Required]** Gets the object_storage_namespace of this OceInstance.
        Object Storage Namespace of tenancy


        :return: The object_storage_namespace of this OceInstance.
        :rtype: str
        """
        return self._object_storage_namespace

    @object_storage_namespace.setter
    def object_storage_namespace(self, object_storage_namespace):
        """
        Sets the object_storage_namespace of this OceInstance.
        Object Storage Namespace of tenancy


        :param object_storage_namespace: The object_storage_namespace of this OceInstance.
        :type: str
        """
        self._object_storage_namespace = object_storage_namespace

    @property
    def admin_email(self):
        """
        **[Required]** Gets the admin_email of this OceInstance.
        Admin Email for Notification


        :return: The admin_email of this OceInstance.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this OceInstance.
        Admin Email for Notification


        :param admin_email: The admin_email of this OceInstance.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def waf_primary_domain(self):
        """
        Gets the waf_primary_domain of this OceInstance.
        Web Application Firewall(WAF) primary domain


        :return: The waf_primary_domain of this OceInstance.
        :rtype: str
        """
        return self._waf_primary_domain

    @waf_primary_domain.setter
    def waf_primary_domain(self, waf_primary_domain):
        """
        Sets the waf_primary_domain of this OceInstance.
        Web Application Firewall(WAF) primary domain


        :param waf_primary_domain: The waf_primary_domain of this OceInstance.
        :type: str
        """
        self._waf_primary_domain = waf_primary_domain

    @property
    def instance_access_type(self):
        """
        Gets the instance_access_type of this OceInstance.
        Flag indicating whether the instance access is private or public

        Allowed values for this property are: "PUBLIC", "PRIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The instance_access_type of this OceInstance.
        :rtype: str
        """
        return self._instance_access_type

    @instance_access_type.setter
    def instance_access_type(self, instance_access_type):
        """
        Sets the instance_access_type of this OceInstance.
        Flag indicating whether the instance access is private or public


        :param instance_access_type: The instance_access_type of this OceInstance.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(instance_access_type, allowed_values):
            instance_access_type = 'UNKNOWN_ENUM_VALUE'
        self._instance_access_type = instance_access_type

    @property
    def instance_license_type(self):
        """
        Gets the instance_license_type of this OceInstance.
        Flag indicating whether the instance license is new cloud or bring your own license

        Allowed values for this property are: "NEW", "BYOL", "PREMIUM", "STARTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The instance_license_type of this OceInstance.
        :rtype: str
        """
        return self._instance_license_type

    @instance_license_type.setter
    def instance_license_type(self, instance_license_type):
        """
        Sets the instance_license_type of this OceInstance.
        Flag indicating whether the instance license is new cloud or bring your own license


        :param instance_license_type: The instance_license_type of this OceInstance.
        :type: str
        """
        allowed_values = ["NEW", "BYOL", "PREMIUM", "STARTER"]
        if not value_allowed_none_or_none_sentinel(instance_license_type, allowed_values):
            instance_license_type = 'UNKNOWN_ENUM_VALUE'
        self._instance_license_type = instance_license_type

    @property
    def time_created(self):
        """
        Gets the time_created of this OceInstance.
        The time the the OceInstance was created. An RFC3339 formatted datetime string


        :return: The time_created of this OceInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OceInstance.
        The time the the OceInstance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OceInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OceInstance.
        The time the OceInstance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this OceInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OceInstance.
        The time the OceInstance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this OceInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OceInstance.
        The current state of the instance lifecycle.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OceInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OceInstance.
        The current state of the instance lifecycle.


        :param lifecycle_state: The lifecycle_state of this OceInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OceInstance.
        Details of the current state of the instance lifecycle

        Allowed values for this property are: "STANDBY", "FAILOVER", "DOWN", "ACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this OceInstance.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OceInstance.
        Details of the current state of the instance lifecycle


        :param lifecycle_details: The lifecycle_details of this OceInstance.
        :type: str
        """
        allowed_values = ["STANDBY", "FAILOVER", "DOWN", "ACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def state_message(self):
        """
        Gets the state_message of this OceInstance.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this OceInstance.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this OceInstance.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this OceInstance.
        :type: str
        """
        self._state_message = state_message

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OceInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OceInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OceInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OceInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OceInstance.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OceInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OceInstance.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OceInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OceInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OceInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OceInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OceInstance.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def service(self):
        """
        Gets the service of this OceInstance.
        SERVICE data.
        Example: `{\"service\": {\"IDCS\": \"value\"}}`


        :return: The service of this OceInstance.
        :rtype: dict(str, object)
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this OceInstance.
        SERVICE data.
        Example: `{\"service\": {\"IDCS\": \"value\"}}`


        :param service: The service of this OceInstance.
        :type: dict(str, object)
        """
        self._service = service

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
