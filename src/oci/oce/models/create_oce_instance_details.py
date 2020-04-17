# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOceInstanceDetails(object):
    """
    The information about new OceInstance.
    """

    #: A constant which can be used with the instance_usage_type property of a CreateOceInstanceDetails.
    #: This constant has a value of "PRIMARY"
    INSTANCE_USAGE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the instance_usage_type property of a CreateOceInstanceDetails.
    #: This constant has a value of "NONPRIMARY"
    INSTANCE_USAGE_TYPE_NONPRIMARY = "NONPRIMARY"

    #: A constant which can be used with the instance_access_type property of a CreateOceInstanceDetails.
    #: This constant has a value of "PUBLIC"
    INSTANCE_ACCESS_TYPE_PUBLIC = "PUBLIC"

    #: A constant which can be used with the instance_access_type property of a CreateOceInstanceDetails.
    #: This constant has a value of "PRIVATE"
    INSTANCE_ACCESS_TYPE_PRIVATE = "PRIVATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOceInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateOceInstanceDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOceInstanceDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateOceInstanceDetails.
        :type name: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this CreateOceInstanceDetails.
        :type tenancy_id: str

        :param idcs_access_token:
            The value to assign to the idcs_access_token property of this CreateOceInstanceDetails.
        :type idcs_access_token: str

        :param identity_stripe:
            The value to assign to the identity_stripe property of this CreateOceInstanceDetails.
        :type identity_stripe: IdentityStripeDetails

        :param tenancy_name:
            The value to assign to the tenancy_name property of this CreateOceInstanceDetails.
        :type tenancy_name: str

        :param instance_usage_type:
            The value to assign to the instance_usage_type property of this CreateOceInstanceDetails.
            Allowed values for this property are: "PRIMARY", "NONPRIMARY"
        :type instance_usage_type: str

        :param object_storage_namespace:
            The value to assign to the object_storage_namespace property of this CreateOceInstanceDetails.
        :type object_storage_namespace: str

        :param admin_email:
            The value to assign to the admin_email property of this CreateOceInstanceDetails.
        :type admin_email: str

        :param upgrade_schedule:
            The value to assign to the upgrade_schedule property of this CreateOceInstanceDetails.
        :type upgrade_schedule: str

        :param waf_primary_domain:
            The value to assign to the waf_primary_domain property of this CreateOceInstanceDetails.
        :type waf_primary_domain: str

        :param instance_access_type:
            The value to assign to the instance_access_type property of this CreateOceInstanceDetails.
            Allowed values for this property are: "PUBLIC", "PRIVATE"
        :type instance_access_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOceInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOceInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'tenancy_id': 'str',
            'idcs_access_token': 'str',
            'identity_stripe': 'IdentityStripeDetails',
            'tenancy_name': 'str',
            'instance_usage_type': 'str',
            'object_storage_namespace': 'str',
            'admin_email': 'str',
            'upgrade_schedule': 'str',
            'waf_primary_domain': 'str',
            'instance_access_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'tenancy_id': 'tenancyId',
            'idcs_access_token': 'idcsAccessToken',
            'identity_stripe': 'identityStripe',
            'tenancy_name': 'tenancyName',
            'instance_usage_type': 'instanceUsageType',
            'object_storage_namespace': 'objectStorageNamespace',
            'admin_email': 'adminEmail',
            'upgrade_schedule': 'upgradeSchedule',
            'waf_primary_domain': 'wafPrimaryDomain',
            'instance_access_type': 'instanceAccessType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._compartment_id = None
        self._name = None
        self._tenancy_id = None
        self._idcs_access_token = None
        self._identity_stripe = None
        self._tenancy_name = None
        self._instance_usage_type = None
        self._object_storage_namespace = None
        self._admin_email = None
        self._upgrade_schedule = None
        self._waf_primary_domain = None
        self._instance_access_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this CreateOceInstanceDetails.
        OceInstance description


        :return: The description of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOceInstanceDetails.
        OceInstance description


        :param description: The description of this CreateOceInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOceInstanceDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOceInstanceDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateOceInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateOceInstanceDetails.
        OceInstance Name


        :return: The name of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateOceInstanceDetails.
        OceInstance Name


        :param name: The name of this CreateOceInstanceDetails.
        :type: str
        """
        self._name = name

    @property
    def tenancy_id(self):
        """
        **[Required]** Gets the tenancy_id of this CreateOceInstanceDetails.
        Tenancy Identifier


        :return: The tenancy_id of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this CreateOceInstanceDetails.
        Tenancy Identifier


        :param tenancy_id: The tenancy_id of this CreateOceInstanceDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def idcs_access_token(self):
        """
        **[Required]** Gets the idcs_access_token of this CreateOceInstanceDetails.
        Identity Cloud Service access token identifying a stripe and service administrator user


        :return: The idcs_access_token of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._idcs_access_token

    @idcs_access_token.setter
    def idcs_access_token(self, idcs_access_token):
        """
        Sets the idcs_access_token of this CreateOceInstanceDetails.
        Identity Cloud Service access token identifying a stripe and service administrator user


        :param idcs_access_token: The idcs_access_token of this CreateOceInstanceDetails.
        :type: str
        """
        self._idcs_access_token = idcs_access_token

    @property
    def identity_stripe(self):
        """
        Gets the identity_stripe of this CreateOceInstanceDetails.

        :return: The identity_stripe of this CreateOceInstanceDetails.
        :rtype: IdentityStripeDetails
        """
        return self._identity_stripe

    @identity_stripe.setter
    def identity_stripe(self, identity_stripe):
        """
        Sets the identity_stripe of this CreateOceInstanceDetails.

        :param identity_stripe: The identity_stripe of this CreateOceInstanceDetails.
        :type: IdentityStripeDetails
        """
        self._identity_stripe = identity_stripe

    @property
    def tenancy_name(self):
        """
        **[Required]** Gets the tenancy_name of this CreateOceInstanceDetails.
        Tenancy Name


        :return: The tenancy_name of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._tenancy_name

    @tenancy_name.setter
    def tenancy_name(self, tenancy_name):
        """
        Sets the tenancy_name of this CreateOceInstanceDetails.
        Tenancy Name


        :param tenancy_name: The tenancy_name of this CreateOceInstanceDetails.
        :type: str
        """
        self._tenancy_name = tenancy_name

    @property
    def instance_usage_type(self):
        """
        Gets the instance_usage_type of this CreateOceInstanceDetails.
        Instance type based on its usage

        Allowed values for this property are: "PRIMARY", "NONPRIMARY"


        :return: The instance_usage_type of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._instance_usage_type

    @instance_usage_type.setter
    def instance_usage_type(self, instance_usage_type):
        """
        Sets the instance_usage_type of this CreateOceInstanceDetails.
        Instance type based on its usage


        :param instance_usage_type: The instance_usage_type of this CreateOceInstanceDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "NONPRIMARY"]
        if not value_allowed_none_or_none_sentinel(instance_usage_type, allowed_values):
            raise ValueError(
                "Invalid value for `instance_usage_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._instance_usage_type = instance_usage_type

    @property
    def object_storage_namespace(self):
        """
        **[Required]** Gets the object_storage_namespace of this CreateOceInstanceDetails.
        Object Storage Namespace of Tenancy


        :return: The object_storage_namespace of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._object_storage_namespace

    @object_storage_namespace.setter
    def object_storage_namespace(self, object_storage_namespace):
        """
        Sets the object_storage_namespace of this CreateOceInstanceDetails.
        Object Storage Namespace of Tenancy


        :param object_storage_namespace: The object_storage_namespace of this CreateOceInstanceDetails.
        :type: str
        """
        self._object_storage_namespace = object_storage_namespace

    @property
    def admin_email(self):
        """
        **[Required]** Gets the admin_email of this CreateOceInstanceDetails.
        Admin Email for Notification


        :return: The admin_email of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this CreateOceInstanceDetails.
        Admin Email for Notification


        :param admin_email: The admin_email of this CreateOceInstanceDetails.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def upgrade_schedule(self):
        """
        Gets the upgrade_schedule of this CreateOceInstanceDetails.
        Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
        or delay upgrade of the service to previous released version


        :return: The upgrade_schedule of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._upgrade_schedule

    @upgrade_schedule.setter
    def upgrade_schedule(self, upgrade_schedule):
        """
        Sets the upgrade_schedule of this CreateOceInstanceDetails.
        Upgrade schedule type representing service to be upgraded immediately whenever latest version is released
        or delay upgrade of the service to previous released version


        :param upgrade_schedule: The upgrade_schedule of this CreateOceInstanceDetails.
        :type: str
        """
        self._upgrade_schedule = upgrade_schedule

    @property
    def waf_primary_domain(self):
        """
        Gets the waf_primary_domain of this CreateOceInstanceDetails.
        Web Application Firewall(WAF) primary domain


        :return: The waf_primary_domain of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._waf_primary_domain

    @waf_primary_domain.setter
    def waf_primary_domain(self, waf_primary_domain):
        """
        Sets the waf_primary_domain of this CreateOceInstanceDetails.
        Web Application Firewall(WAF) primary domain


        :param waf_primary_domain: The waf_primary_domain of this CreateOceInstanceDetails.
        :type: str
        """
        self._waf_primary_domain = waf_primary_domain

    @property
    def instance_access_type(self):
        """
        Gets the instance_access_type of this CreateOceInstanceDetails.
        Flag indicating whether the instance access is private or public

        Allowed values for this property are: "PUBLIC", "PRIVATE"


        :return: The instance_access_type of this CreateOceInstanceDetails.
        :rtype: str
        """
        return self._instance_access_type

    @instance_access_type.setter
    def instance_access_type(self, instance_access_type):
        """
        Sets the instance_access_type of this CreateOceInstanceDetails.
        Flag indicating whether the instance access is private or public


        :param instance_access_type: The instance_access_type of this CreateOceInstanceDetails.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(instance_access_type, allowed_values):
            raise ValueError(
                "Invalid value for `instance_access_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._instance_access_type = instance_access_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOceInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateOceInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOceInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateOceInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOceInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateOceInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOceInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateOceInstanceDetails.
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
