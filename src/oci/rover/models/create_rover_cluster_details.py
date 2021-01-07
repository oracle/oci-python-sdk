# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRoverClusterDetails(object):
    """
    The information required to create a RoverCluster.
    """

    #: A constant which can be used with the enclosure_type property of a CreateRoverClusterDetails.
    #: This constant has a value of "RUGGADIZED"
    ENCLOSURE_TYPE_RUGGADIZED = "RUGGADIZED"

    #: A constant which can be used with the enclosure_type property of a CreateRoverClusterDetails.
    #: This constant has a value of "NON_RUGGADIZED"
    ENCLOSURE_TYPE_NON_RUGGADIZED = "NON_RUGGADIZED"

    #: A constant which can be used with the shipping_preference property of a CreateRoverClusterDetails.
    #: This constant has a value of "ORACLE_SHIPPED"
    SHIPPING_PREFERENCE_ORACLE_SHIPPED = "ORACLE_SHIPPED"

    #: A constant which can be used with the shipping_preference property of a CreateRoverClusterDetails.
    #: This constant has a value of "CUSTOMER_PICKUP"
    SHIPPING_PREFERENCE_CUSTOMER_PICKUP = "CUSTOMER_PICKUP"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverClusterDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverClusterDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverClusterDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverClusterDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverClusterDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CreateRoverClusterDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRoverClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRoverClusterDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRoverClusterDetails.
        :type compartment_id: str

        :param cluster_size:
            The value to assign to the cluster_size property of this CreateRoverClusterDetails.
        :type cluster_size: int

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this CreateRoverClusterDetails.
        :type customer_shipping_address: oci.rover.models.ShippingAddress

        :param cluster_workloads:
            The value to assign to the cluster_workloads property of this CreateRoverClusterDetails.
        :type cluster_workloads: list[oci.rover.models.RoverWorkload]

        :param super_user_password:
            The value to assign to the super_user_password property of this CreateRoverClusterDetails.
        :type super_user_password: str

        :param enclosure_type:
            The value to assign to the enclosure_type property of this CreateRoverClusterDetails.
            Allowed values for this property are: "RUGGADIZED", "NON_RUGGADIZED"
        :type enclosure_type: str

        :param unlock_passphrase:
            The value to assign to the unlock_passphrase property of this CreateRoverClusterDetails.
        :type unlock_passphrase: str

        :param point_of_contact:
            The value to assign to the point_of_contact property of this CreateRoverClusterDetails.
        :type point_of_contact: str

        :param point_of_contact_phone_number:
            The value to assign to the point_of_contact_phone_number property of this CreateRoverClusterDetails.
        :type point_of_contact_phone_number: str

        :param shipping_preference:
            The value to assign to the shipping_preference property of this CreateRoverClusterDetails.
            Allowed values for this property are: "ORACLE_SHIPPED", "CUSTOMER_PICKUP"
        :type shipping_preference: str

        :param shipping_vendor:
            The value to assign to the shipping_vendor property of this CreateRoverClusterDetails.
        :type shipping_vendor: str

        :param time_pickup_expected:
            The value to assign to the time_pickup_expected property of this CreateRoverClusterDetails.
        :type time_pickup_expected: datetime

        :param oracle_shipping_tracking_url:
            The value to assign to the oracle_shipping_tracking_url property of this CreateRoverClusterDetails.
        :type oracle_shipping_tracking_url: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateRoverClusterDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this CreateRoverClusterDetails.
        :type lifecycle_state_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRoverClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRoverClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateRoverClusterDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'cluster_size': 'int',
            'customer_shipping_address': 'ShippingAddress',
            'cluster_workloads': 'list[RoverWorkload]',
            'super_user_password': 'str',
            'enclosure_type': 'str',
            'unlock_passphrase': 'str',
            'point_of_contact': 'str',
            'point_of_contact_phone_number': 'str',
            'shipping_preference': 'str',
            'shipping_vendor': 'str',
            'time_pickup_expected': 'datetime',
            'oracle_shipping_tracking_url': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'cluster_size': 'clusterSize',
            'customer_shipping_address': 'customerShippingAddress',
            'cluster_workloads': 'clusterWorkloads',
            'super_user_password': 'superUserPassword',
            'enclosure_type': 'enclosureType',
            'unlock_passphrase': 'unlockPassphrase',
            'point_of_contact': 'pointOfContact',
            'point_of_contact_phone_number': 'pointOfContactPhoneNumber',
            'shipping_preference': 'shippingPreference',
            'shipping_vendor': 'shippingVendor',
            'time_pickup_expected': 'timePickupExpected',
            'oracle_shipping_tracking_url': 'oracleShippingTrackingUrl',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._cluster_size = None
        self._customer_shipping_address = None
        self._cluster_workloads = None
        self._super_user_password = None
        self._enclosure_type = None
        self._unlock_passphrase = None
        self._point_of_contact = None
        self._point_of_contact_phone_number = None
        self._shipping_preference = None
        self._shipping_vendor = None
        self._time_pickup_expected = None
        self._oracle_shipping_tracking_url = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateRoverClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRoverClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRoverClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRoverClusterDetails.
        The OCID of the compartment containing the RoverCluster.


        :return: The compartment_id of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRoverClusterDetails.
        The OCID of the compartment containing the RoverCluster.


        :param compartment_id: The compartment_id of this CreateRoverClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cluster_size(self):
        """
        **[Required]** Gets the cluster_size of this CreateRoverClusterDetails.
        Number of nodes desired in the cluster, between 5 and 15.


        :return: The cluster_size of this CreateRoverClusterDetails.
        :rtype: int
        """
        return self._cluster_size

    @cluster_size.setter
    def cluster_size(self, cluster_size):
        """
        Sets the cluster_size of this CreateRoverClusterDetails.
        Number of nodes desired in the cluster, between 5 and 15.


        :param cluster_size: The cluster_size of this CreateRoverClusterDetails.
        :type: int
        """
        self._cluster_size = cluster_size

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this CreateRoverClusterDetails.

        :return: The customer_shipping_address of this CreateRoverClusterDetails.
        :rtype: oci.rover.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this CreateRoverClusterDetails.

        :param customer_shipping_address: The customer_shipping_address of this CreateRoverClusterDetails.
        :type: oci.rover.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def cluster_workloads(self):
        """
        Gets the cluster_workloads of this CreateRoverClusterDetails.
        List of existing workloads that should be provisioned on the nodes.


        :return: The cluster_workloads of this CreateRoverClusterDetails.
        :rtype: list[oci.rover.models.RoverWorkload]
        """
        return self._cluster_workloads

    @cluster_workloads.setter
    def cluster_workloads(self, cluster_workloads):
        """
        Sets the cluster_workloads of this CreateRoverClusterDetails.
        List of existing workloads that should be provisioned on the nodes.


        :param cluster_workloads: The cluster_workloads of this CreateRoverClusterDetails.
        :type: list[oci.rover.models.RoverWorkload]
        """
        self._cluster_workloads = cluster_workloads

    @property
    def super_user_password(self):
        """
        Gets the super_user_password of this CreateRoverClusterDetails.
        Root password for the rover cluster.


        :return: The super_user_password of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._super_user_password

    @super_user_password.setter
    def super_user_password(self, super_user_password):
        """
        Sets the super_user_password of this CreateRoverClusterDetails.
        Root password for the rover cluster.


        :param super_user_password: The super_user_password of this CreateRoverClusterDetails.
        :type: str
        """
        self._super_user_password = super_user_password

    @property
    def enclosure_type(self):
        """
        Gets the enclosure_type of this CreateRoverClusterDetails.
        The type of enclosure rover nodes in this cluster are shipped in.

        Allowed values for this property are: "RUGGADIZED", "NON_RUGGADIZED"


        :return: The enclosure_type of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._enclosure_type

    @enclosure_type.setter
    def enclosure_type(self, enclosure_type):
        """
        Sets the enclosure_type of this CreateRoverClusterDetails.
        The type of enclosure rover nodes in this cluster are shipped in.


        :param enclosure_type: The enclosure_type of this CreateRoverClusterDetails.
        :type: str
        """
        allowed_values = ["RUGGADIZED", "NON_RUGGADIZED"]
        if not value_allowed_none_or_none_sentinel(enclosure_type, allowed_values):
            raise ValueError(
                "Invalid value for `enclosure_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._enclosure_type = enclosure_type

    @property
    def unlock_passphrase(self):
        """
        Gets the unlock_passphrase of this CreateRoverClusterDetails.
        Password to unlock the rover cluster.


        :return: The unlock_passphrase of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._unlock_passphrase

    @unlock_passphrase.setter
    def unlock_passphrase(self, unlock_passphrase):
        """
        Sets the unlock_passphrase of this CreateRoverClusterDetails.
        Password to unlock the rover cluster.


        :param unlock_passphrase: The unlock_passphrase of this CreateRoverClusterDetails.
        :type: str
        """
        self._unlock_passphrase = unlock_passphrase

    @property
    def point_of_contact(self):
        """
        Gets the point_of_contact of this CreateRoverClusterDetails.
        Name of point of contact for this order if customer is picking up.


        :return: The point_of_contact of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._point_of_contact

    @point_of_contact.setter
    def point_of_contact(self, point_of_contact):
        """
        Sets the point_of_contact of this CreateRoverClusterDetails.
        Name of point of contact for this order if customer is picking up.


        :param point_of_contact: The point_of_contact of this CreateRoverClusterDetails.
        :type: str
        """
        self._point_of_contact = point_of_contact

    @property
    def point_of_contact_phone_number(self):
        """
        Gets the point_of_contact_phone_number of this CreateRoverClusterDetails.
        Phone number of point of contact for this order if customer is picking up.


        :return: The point_of_contact_phone_number of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._point_of_contact_phone_number

    @point_of_contact_phone_number.setter
    def point_of_contact_phone_number(self, point_of_contact_phone_number):
        """
        Sets the point_of_contact_phone_number of this CreateRoverClusterDetails.
        Phone number of point of contact for this order if customer is picking up.


        :param point_of_contact_phone_number: The point_of_contact_phone_number of this CreateRoverClusterDetails.
        :type: str
        """
        self._point_of_contact_phone_number = point_of_contact_phone_number

    @property
    def shipping_preference(self):
        """
        Gets the shipping_preference of this CreateRoverClusterDetails.
        Preference for device delivery.

        Allowed values for this property are: "ORACLE_SHIPPED", "CUSTOMER_PICKUP"


        :return: The shipping_preference of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._shipping_preference

    @shipping_preference.setter
    def shipping_preference(self, shipping_preference):
        """
        Sets the shipping_preference of this CreateRoverClusterDetails.
        Preference for device delivery.


        :param shipping_preference: The shipping_preference of this CreateRoverClusterDetails.
        :type: str
        """
        allowed_values = ["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]
        if not value_allowed_none_or_none_sentinel(shipping_preference, allowed_values):
            raise ValueError(
                "Invalid value for `shipping_preference`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._shipping_preference = shipping_preference

    @property
    def shipping_vendor(self):
        """
        Gets the shipping_vendor of this CreateRoverClusterDetails.
        Shipping vendor of choice for orace to customer shipping.


        :return: The shipping_vendor of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._shipping_vendor

    @shipping_vendor.setter
    def shipping_vendor(self, shipping_vendor):
        """
        Sets the shipping_vendor of this CreateRoverClusterDetails.
        Shipping vendor of choice for orace to customer shipping.


        :param shipping_vendor: The shipping_vendor of this CreateRoverClusterDetails.
        :type: str
        """
        self._shipping_vendor = shipping_vendor

    @property
    def time_pickup_expected(self):
        """
        Gets the time_pickup_expected of this CreateRoverClusterDetails.
        Expected date when customer wants to pickup the cluster if they chose customer pickup.


        :return: The time_pickup_expected of this CreateRoverClusterDetails.
        :rtype: datetime
        """
        return self._time_pickup_expected

    @time_pickup_expected.setter
    def time_pickup_expected(self, time_pickup_expected):
        """
        Sets the time_pickup_expected of this CreateRoverClusterDetails.
        Expected date when customer wants to pickup the cluster if they chose customer pickup.


        :param time_pickup_expected: The time_pickup_expected of this CreateRoverClusterDetails.
        :type: datetime
        """
        self._time_pickup_expected = time_pickup_expected

    @property
    def oracle_shipping_tracking_url(self):
        """
        Gets the oracle_shipping_tracking_url of this CreateRoverClusterDetails.
        Tracking Url for the shipped Rover Cluster.


        :return: The oracle_shipping_tracking_url of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._oracle_shipping_tracking_url

    @oracle_shipping_tracking_url.setter
    def oracle_shipping_tracking_url(self, oracle_shipping_tracking_url):
        """
        Sets the oracle_shipping_tracking_url of this CreateRoverClusterDetails.
        Tracking Url for the shipped Rover Cluster.


        :param oracle_shipping_tracking_url: The oracle_shipping_tracking_url of this CreateRoverClusterDetails.
        :type: str
        """
        self._oracle_shipping_tracking_url = oracle_shipping_tracking_url

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CreateRoverClusterDetails.
        The current state of the RoverCluster.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CreateRoverClusterDetails.
        The current state of the RoverCluster.


        :param lifecycle_state: The lifecycle_state of this CreateRoverClusterDetails.
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
        Gets the lifecycle_state_details of this CreateRoverClusterDetails.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this CreateRoverClusterDetails.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this CreateRoverClusterDetails.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this CreateRoverClusterDetails.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRoverClusterDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateRoverClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRoverClusterDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateRoverClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRoverClusterDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRoverClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRoverClusterDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRoverClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateRoverClusterDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this CreateRoverClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateRoverClusterDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this CreateRoverClusterDetails.
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
