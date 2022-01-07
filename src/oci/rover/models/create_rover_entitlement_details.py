# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRoverEntitlementDetails(object):
    """
    Information required to create a RoverEntitlement.
    """

    #: A constant which can be used with the lifecycle_state property of a CreateRoverEntitlementDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverEntitlementDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverEntitlementDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverEntitlementDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverEntitlementDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverEntitlementDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRoverEntitlementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRoverEntitlementDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateRoverEntitlementDetails.
        :type display_name: str

        :param requestor_name:
            The value to assign to the requestor_name property of this CreateRoverEntitlementDetails.
        :type requestor_name: str

        :param requestor_email:
            The value to assign to the requestor_email property of this CreateRoverEntitlementDetails.
        :type requestor_email: str

        :param entitlement_details:
            The value to assign to the entitlement_details property of this CreateRoverEntitlementDetails.
        :type entitlement_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateRoverEntitlementDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this CreateRoverEntitlementDetails.
        :type lifecycle_state_details: str

        :param tenant_id:
            The value to assign to the tenant_id property of this CreateRoverEntitlementDetails.
        :type tenant_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRoverEntitlementDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRoverEntitlementDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateRoverEntitlementDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'requestor_name': 'str',
            'requestor_email': 'str',
            'entitlement_details': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'tenant_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'requestor_name': 'requestorName',
            'requestor_email': 'requestorEmail',
            'entitlement_details': 'entitlementDetails',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'tenant_id': 'tenantId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._requestor_name = None
        self._requestor_email = None
        self._entitlement_details = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._tenant_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRoverEntitlementDetails.
        The OCID of the compartment containing the RoverEntitlement.


        :return: The compartment_id of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRoverEntitlementDetails.
        The OCID of the compartment containing the RoverEntitlement.


        :param compartment_id: The compartment_id of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRoverEntitlementDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRoverEntitlementDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def requestor_name(self):
        """
        **[Required]** Gets the requestor_name of this CreateRoverEntitlementDetails.
        Requestor name for the entitlement.


        :return: The requestor_name of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._requestor_name

    @requestor_name.setter
    def requestor_name(self, requestor_name):
        """
        Sets the requestor_name of this CreateRoverEntitlementDetails.
        Requestor name for the entitlement.


        :param requestor_name: The requestor_name of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._requestor_name = requestor_name

    @property
    def requestor_email(self):
        """
        **[Required]** Gets the requestor_email of this CreateRoverEntitlementDetails.
        Requestor email for the entitlement.


        :return: The requestor_email of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._requestor_email

    @requestor_email.setter
    def requestor_email(self, requestor_email):
        """
        Sets the requestor_email of this CreateRoverEntitlementDetails.
        Requestor email for the entitlement.


        :param requestor_email: The requestor_email of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._requestor_email = requestor_email

    @property
    def entitlement_details(self):
        """
        Gets the entitlement_details of this CreateRoverEntitlementDetails.
        Details about the entitlement.


        :return: The entitlement_details of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._entitlement_details

    @entitlement_details.setter
    def entitlement_details(self, entitlement_details):
        """
        Sets the entitlement_details of this CreateRoverEntitlementDetails.
        Details about the entitlement.


        :param entitlement_details: The entitlement_details of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._entitlement_details = entitlement_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CreateRoverEntitlementDetails.
        The current state of the RoverNode.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CreateRoverEntitlementDetails.
        The current state of the RoverNode.


        :param lifecycle_state: The lifecycle_state of this CreateRoverEntitlementDetails.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this CreateRoverEntitlementDetails.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this CreateRoverEntitlementDetails.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this CreateRoverEntitlementDetails.
        tenant Id.


        :return: The tenant_id of this CreateRoverEntitlementDetails.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this CreateRoverEntitlementDetails.
        tenant Id.


        :param tenant_id: The tenant_id of this CreateRoverEntitlementDetails.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRoverEntitlementDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateRoverEntitlementDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRoverEntitlementDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateRoverEntitlementDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRoverEntitlementDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRoverEntitlementDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRoverEntitlementDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRoverEntitlementDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateRoverEntitlementDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this CreateRoverEntitlementDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateRoverEntitlementDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this CreateRoverEntitlementDetails.
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
