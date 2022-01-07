# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNode(object):
    """
    Information about a RoverNode.
    """

    #: A constant which can be used with the node_type property of a RoverNode.
    #: This constant has a value of "STANDALONE"
    NODE_TYPE_STANDALONE = "STANDALONE"

    #: A constant which can be used with the node_type property of a RoverNode.
    #: This constant has a value of "CLUSTERED"
    NODE_TYPE_CLUSTERED = "CLUSTERED"

    #: A constant which can be used with the enclosure_type property of a RoverNode.
    #: This constant has a value of "RUGGADIZED"
    ENCLOSURE_TYPE_RUGGADIZED = "RUGGADIZED"

    #: A constant which can be used with the enclosure_type property of a RoverNode.
    #: This constant has a value of "NON_RUGGADIZED"
    ENCLOSURE_TYPE_NON_RUGGADIZED = "NON_RUGGADIZED"

    #: A constant which can be used with the lifecycle_state property of a RoverNode.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RoverNode.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RoverNode.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RoverNode.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RoverNode.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a RoverNode.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the shipping_preference property of a RoverNode.
    #: This constant has a value of "ORACLE_SHIPPED"
    SHIPPING_PREFERENCE_ORACLE_SHIPPED = "ORACLE_SHIPPED"

    #: A constant which can be used with the shipping_preference property of a RoverNode.
    #: This constant has a value of "CUSTOMER_PICKUP"
    SHIPPING_PREFERENCE_CUSTOMER_PICKUP = "CUSTOMER_PICKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RoverNode.
        :type id: str

        :param cluster_id:
            The value to assign to the cluster_id property of this RoverNode.
        :type cluster_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RoverNode.
        :type compartment_id: str

        :param node_type:
            The value to assign to the node_type property of this RoverNode.
            Allowed values for this property are: "STANDALONE", "CLUSTERED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type node_type: str

        :param enclosure_type:
            The value to assign to the enclosure_type property of this RoverNode.
            Allowed values for this property are: "RUGGADIZED", "NON_RUGGADIZED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type enclosure_type: str

        :param serial_number:
            The value to assign to the serial_number property of this RoverNode.
        :type serial_number: str

        :param display_name:
            The value to assign to the display_name property of this RoverNode.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this RoverNode.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RoverNode.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this RoverNode.
        :type lifecycle_state_details: str

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this RoverNode.
        :type customer_shipping_address: oci.rover.models.ShippingAddress

        :param node_workloads:
            The value to assign to the node_workloads property of this RoverNode.
        :type node_workloads: list[oci.rover.models.RoverWorkload]

        :param time_customer_receieved:
            The value to assign to the time_customer_receieved property of this RoverNode.
        :type time_customer_receieved: datetime

        :param time_customer_returned:
            The value to assign to the time_customer_returned property of this RoverNode.
        :type time_customer_returned: datetime

        :param delivery_tracking_info:
            The value to assign to the delivery_tracking_info property of this RoverNode.
        :type delivery_tracking_info: str

        :param super_user_password:
            The value to assign to the super_user_password property of this RoverNode.
        :type super_user_password: str

        :param unlock_passphrase:
            The value to assign to the unlock_passphrase property of this RoverNode.
        :type unlock_passphrase: str

        :param point_of_contact:
            The value to assign to the point_of_contact property of this RoverNode.
        :type point_of_contact: str

        :param point_of_contact_phone_number:
            The value to assign to the point_of_contact_phone_number property of this RoverNode.
        :type point_of_contact_phone_number: str

        :param shipping_preference:
            The value to assign to the shipping_preference property of this RoverNode.
            Allowed values for this property are: "ORACLE_SHIPPED", "CUSTOMER_PICKUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shipping_preference: str

        :param shipping_vendor:
            The value to assign to the shipping_vendor property of this RoverNode.
        :type shipping_vendor: str

        :param time_pickup_expected:
            The value to assign to the time_pickup_expected property of this RoverNode.
        :type time_pickup_expected: datetime

        :param time_return_window_starts:
            The value to assign to the time_return_window_starts property of this RoverNode.
        :type time_return_window_starts: datetime

        :param oracle_shipping_tracking_url:
            The value to assign to the oracle_shipping_tracking_url property of this RoverNode.
        :type oracle_shipping_tracking_url: str

        :param time_return_window_ends:
            The value to assign to the time_return_window_ends property of this RoverNode.
        :type time_return_window_ends: datetime

        :param return_shipping_label_uri:
            The value to assign to the return_shipping_label_uri property of this RoverNode.
        :type return_shipping_label_uri: str

        :param is_import_requested:
            The value to assign to the is_import_requested property of this RoverNode.
        :type is_import_requested: bool

        :param import_compartment_id:
            The value to assign to the import_compartment_id property of this RoverNode.
        :type import_compartment_id: str

        :param import_file_bucket:
            The value to assign to the import_file_bucket property of this RoverNode.
        :type import_file_bucket: str

        :param data_validation_code:
            The value to assign to the data_validation_code property of this RoverNode.
        :type data_validation_code: str

        :param public_key:
            The value to assign to the public_key property of this RoverNode.
        :type public_key: str

        :param image_export_par:
            The value to assign to the image_export_par property of this RoverNode.
        :type image_export_par: str

        :param tags:
            The value to assign to the tags property of this RoverNode.
        :type tags: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RoverNode.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RoverNode.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RoverNode.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'cluster_id': 'str',
            'compartment_id': 'str',
            'node_type': 'str',
            'enclosure_type': 'str',
            'serial_number': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'customer_shipping_address': 'ShippingAddress',
            'node_workloads': 'list[RoverWorkload]',
            'time_customer_receieved': 'datetime',
            'time_customer_returned': 'datetime',
            'delivery_tracking_info': 'str',
            'super_user_password': 'str',
            'unlock_passphrase': 'str',
            'point_of_contact': 'str',
            'point_of_contact_phone_number': 'str',
            'shipping_preference': 'str',
            'shipping_vendor': 'str',
            'time_pickup_expected': 'datetime',
            'time_return_window_starts': 'datetime',
            'oracle_shipping_tracking_url': 'str',
            'time_return_window_ends': 'datetime',
            'return_shipping_label_uri': 'str',
            'is_import_requested': 'bool',
            'import_compartment_id': 'str',
            'import_file_bucket': 'str',
            'data_validation_code': 'str',
            'public_key': 'str',
            'image_export_par': 'str',
            'tags': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'cluster_id': 'clusterId',
            'compartment_id': 'compartmentId',
            'node_type': 'nodeType',
            'enclosure_type': 'enclosureType',
            'serial_number': 'serialNumber',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'customer_shipping_address': 'customerShippingAddress',
            'node_workloads': 'nodeWorkloads',
            'time_customer_receieved': 'timeCustomerReceieved',
            'time_customer_returned': 'timeCustomerReturned',
            'delivery_tracking_info': 'deliveryTrackingInfo',
            'super_user_password': 'superUserPassword',
            'unlock_passphrase': 'unlockPassphrase',
            'point_of_contact': 'pointOfContact',
            'point_of_contact_phone_number': 'pointOfContactPhoneNumber',
            'shipping_preference': 'shippingPreference',
            'shipping_vendor': 'shippingVendor',
            'time_pickup_expected': 'timePickupExpected',
            'time_return_window_starts': 'timeReturnWindowStarts',
            'oracle_shipping_tracking_url': 'oracleShippingTrackingUrl',
            'time_return_window_ends': 'timeReturnWindowEnds',
            'return_shipping_label_uri': 'returnShippingLabelUri',
            'is_import_requested': 'isImportRequested',
            'import_compartment_id': 'importCompartmentId',
            'import_file_bucket': 'importFileBucket',
            'data_validation_code': 'dataValidationCode',
            'public_key': 'publicKey',
            'image_export_par': 'imageExportPar',
            'tags': 'tags',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._cluster_id = None
        self._compartment_id = None
        self._node_type = None
        self._enclosure_type = None
        self._serial_number = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._customer_shipping_address = None
        self._node_workloads = None
        self._time_customer_receieved = None
        self._time_customer_returned = None
        self._delivery_tracking_info = None
        self._super_user_password = None
        self._unlock_passphrase = None
        self._point_of_contact = None
        self._point_of_contact_phone_number = None
        self._shipping_preference = None
        self._shipping_vendor = None
        self._time_pickup_expected = None
        self._time_return_window_starts = None
        self._oracle_shipping_tracking_url = None
        self._time_return_window_ends = None
        self._return_shipping_label_uri = None
        self._is_import_requested = None
        self._import_compartment_id = None
        self._import_file_bucket = None
        self._data_validation_code = None
        self._public_key = None
        self._image_export_par = None
        self._tags = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RoverNode.
        The OCID of RoverNode.


        :return: The id of this RoverNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RoverNode.
        The OCID of RoverNode.


        :param id: The id of this RoverNode.
        :type: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this RoverNode.
        The cluster ID if the node is part of a cluster.


        :return: The cluster_id of this RoverNode.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this RoverNode.
        The cluster ID if the node is part of a cluster.


        :param cluster_id: The cluster_id of this RoverNode.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RoverNode.
        The OCID of the compartment containing the RoverNode.


        :return: The compartment_id of this RoverNode.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RoverNode.
        The OCID of the compartment containing the RoverNode.


        :param compartment_id: The compartment_id of this RoverNode.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def node_type(self):
        """
        Gets the node_type of this RoverNode.
        The type of node indicating if it belongs to a cluster

        Allowed values for this property are: "STANDALONE", "CLUSTERED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The node_type of this RoverNode.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this RoverNode.
        The type of node indicating if it belongs to a cluster


        :param node_type: The node_type of this RoverNode.
        :type: str
        """
        allowed_values = ["STANDALONE", "CLUSTERED"]
        if not value_allowed_none_or_none_sentinel(node_type, allowed_values):
            node_type = 'UNKNOWN_ENUM_VALUE'
        self._node_type = node_type

    @property
    def enclosure_type(self):
        """
        Gets the enclosure_type of this RoverNode.
        The type of enclosure rover node is shipped in.

        Allowed values for this property are: "RUGGADIZED", "NON_RUGGADIZED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The enclosure_type of this RoverNode.
        :rtype: str
        """
        return self._enclosure_type

    @enclosure_type.setter
    def enclosure_type(self, enclosure_type):
        """
        Sets the enclosure_type of this RoverNode.
        The type of enclosure rover node is shipped in.


        :param enclosure_type: The enclosure_type of this RoverNode.
        :type: str
        """
        allowed_values = ["RUGGADIZED", "NON_RUGGADIZED"]
        if not value_allowed_none_or_none_sentinel(enclosure_type, allowed_values):
            enclosure_type = 'UNKNOWN_ENUM_VALUE'
        self._enclosure_type = enclosure_type

    @property
    def serial_number(self):
        """
        Gets the serial_number of this RoverNode.
        Serial number of the node.


        :return: The serial_number of this RoverNode.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this RoverNode.
        Serial number of the node.


        :param serial_number: The serial_number of this RoverNode.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RoverNode.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this RoverNode.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RoverNode.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this RoverNode.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this RoverNode.
        The time the the RoverNode was created. An RFC3339 formatted datetime string


        :return: The time_created of this RoverNode.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RoverNode.
        The time the the RoverNode was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this RoverNode.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RoverNode.
        The current state of the RoverNode.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RoverNode.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RoverNode.
        The current state of the RoverNode.


        :param lifecycle_state: The lifecycle_state of this RoverNode.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this RoverNode.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this RoverNode.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this RoverNode.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this RoverNode.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this RoverNode.

        :return: The customer_shipping_address of this RoverNode.
        :rtype: oci.rover.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this RoverNode.

        :param customer_shipping_address: The customer_shipping_address of this RoverNode.
        :type: oci.rover.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def node_workloads(self):
        """
        Gets the node_workloads of this RoverNode.
        List of existing workloads that should be provisioned on the node.


        :return: The node_workloads of this RoverNode.
        :rtype: list[oci.rover.models.RoverWorkload]
        """
        return self._node_workloads

    @node_workloads.setter
    def node_workloads(self, node_workloads):
        """
        Sets the node_workloads of this RoverNode.
        List of existing workloads that should be provisioned on the node.


        :param node_workloads: The node_workloads of this RoverNode.
        :type: list[oci.rover.models.RoverWorkload]
        """
        self._node_workloads = node_workloads

    @property
    def time_customer_receieved(self):
        """
        Gets the time_customer_receieved of this RoverNode.
        Date and time when customer received tne node.


        :return: The time_customer_receieved of this RoverNode.
        :rtype: datetime
        """
        return self._time_customer_receieved

    @time_customer_receieved.setter
    def time_customer_receieved(self, time_customer_receieved):
        """
        Sets the time_customer_receieved of this RoverNode.
        Date and time when customer received tne node.


        :param time_customer_receieved: The time_customer_receieved of this RoverNode.
        :type: datetime
        """
        self._time_customer_receieved = time_customer_receieved

    @property
    def time_customer_returned(self):
        """
        Gets the time_customer_returned of this RoverNode.
        Date and time when customer returned the node.


        :return: The time_customer_returned of this RoverNode.
        :rtype: datetime
        """
        return self._time_customer_returned

    @time_customer_returned.setter
    def time_customer_returned(self, time_customer_returned):
        """
        Sets the time_customer_returned of this RoverNode.
        Date and time when customer returned the node.


        :param time_customer_returned: The time_customer_returned of this RoverNode.
        :type: datetime
        """
        self._time_customer_returned = time_customer_returned

    @property
    def delivery_tracking_info(self):
        """
        Gets the delivery_tracking_info of this RoverNode.
        Tracking information for device shipping.


        :return: The delivery_tracking_info of this RoverNode.
        :rtype: str
        """
        return self._delivery_tracking_info

    @delivery_tracking_info.setter
    def delivery_tracking_info(self, delivery_tracking_info):
        """
        Sets the delivery_tracking_info of this RoverNode.
        Tracking information for device shipping.


        :param delivery_tracking_info: The delivery_tracking_info of this RoverNode.
        :type: str
        """
        self._delivery_tracking_info = delivery_tracking_info

    @property
    def super_user_password(self):
        """
        Gets the super_user_password of this RoverNode.
        Root password for the rover node.


        :return: The super_user_password of this RoverNode.
        :rtype: str
        """
        return self._super_user_password

    @super_user_password.setter
    def super_user_password(self, super_user_password):
        """
        Sets the super_user_password of this RoverNode.
        Root password for the rover node.


        :param super_user_password: The super_user_password of this RoverNode.
        :type: str
        """
        self._super_user_password = super_user_password

    @property
    def unlock_passphrase(self):
        """
        Gets the unlock_passphrase of this RoverNode.
        Password to unlock the rover node.


        :return: The unlock_passphrase of this RoverNode.
        :rtype: str
        """
        return self._unlock_passphrase

    @unlock_passphrase.setter
    def unlock_passphrase(self, unlock_passphrase):
        """
        Sets the unlock_passphrase of this RoverNode.
        Password to unlock the rover node.


        :param unlock_passphrase: The unlock_passphrase of this RoverNode.
        :type: str
        """
        self._unlock_passphrase = unlock_passphrase

    @property
    def point_of_contact(self):
        """
        Gets the point_of_contact of this RoverNode.
        Name of point of contact for this order if customer is picking up.


        :return: The point_of_contact of this RoverNode.
        :rtype: str
        """
        return self._point_of_contact

    @point_of_contact.setter
    def point_of_contact(self, point_of_contact):
        """
        Sets the point_of_contact of this RoverNode.
        Name of point of contact for this order if customer is picking up.


        :param point_of_contact: The point_of_contact of this RoverNode.
        :type: str
        """
        self._point_of_contact = point_of_contact

    @property
    def point_of_contact_phone_number(self):
        """
        Gets the point_of_contact_phone_number of this RoverNode.
        Phone number of point of contact for this order if customer is picking up.


        :return: The point_of_contact_phone_number of this RoverNode.
        :rtype: str
        """
        return self._point_of_contact_phone_number

    @point_of_contact_phone_number.setter
    def point_of_contact_phone_number(self, point_of_contact_phone_number):
        """
        Sets the point_of_contact_phone_number of this RoverNode.
        Phone number of point of contact for this order if customer is picking up.


        :param point_of_contact_phone_number: The point_of_contact_phone_number of this RoverNode.
        :type: str
        """
        self._point_of_contact_phone_number = point_of_contact_phone_number

    @property
    def shipping_preference(self):
        """
        Gets the shipping_preference of this RoverNode.
        Preference for device delivery.

        Allowed values for this property are: "ORACLE_SHIPPED", "CUSTOMER_PICKUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shipping_preference of this RoverNode.
        :rtype: str
        """
        return self._shipping_preference

    @shipping_preference.setter
    def shipping_preference(self, shipping_preference):
        """
        Sets the shipping_preference of this RoverNode.
        Preference for device delivery.


        :param shipping_preference: The shipping_preference of this RoverNode.
        :type: str
        """
        allowed_values = ["ORACLE_SHIPPED", "CUSTOMER_PICKUP"]
        if not value_allowed_none_or_none_sentinel(shipping_preference, allowed_values):
            shipping_preference = 'UNKNOWN_ENUM_VALUE'
        self._shipping_preference = shipping_preference

    @property
    def shipping_vendor(self):
        """
        Gets the shipping_vendor of this RoverNode.
        Shipping vendor of choice for orace to customer shipping.


        :return: The shipping_vendor of this RoverNode.
        :rtype: str
        """
        return self._shipping_vendor

    @shipping_vendor.setter
    def shipping_vendor(self, shipping_vendor):
        """
        Sets the shipping_vendor of this RoverNode.
        Shipping vendor of choice for orace to customer shipping.


        :param shipping_vendor: The shipping_vendor of this RoverNode.
        :type: str
        """
        self._shipping_vendor = shipping_vendor

    @property
    def time_pickup_expected(self):
        """
        Gets the time_pickup_expected of this RoverNode.
        Expected date when customer wants to pickup the device if they chose customer pickup.


        :return: The time_pickup_expected of this RoverNode.
        :rtype: datetime
        """
        return self._time_pickup_expected

    @time_pickup_expected.setter
    def time_pickup_expected(self, time_pickup_expected):
        """
        Sets the time_pickup_expected of this RoverNode.
        Expected date when customer wants to pickup the device if they chose customer pickup.


        :param time_pickup_expected: The time_pickup_expected of this RoverNode.
        :type: datetime
        """
        self._time_pickup_expected = time_pickup_expected

    @property
    def time_return_window_starts(self):
        """
        Gets the time_return_window_starts of this RoverNode.
        Start time for the window to pickup the device from customer.


        :return: The time_return_window_starts of this RoverNode.
        :rtype: datetime
        """
        return self._time_return_window_starts

    @time_return_window_starts.setter
    def time_return_window_starts(self, time_return_window_starts):
        """
        Sets the time_return_window_starts of this RoverNode.
        Start time for the window to pickup the device from customer.


        :param time_return_window_starts: The time_return_window_starts of this RoverNode.
        :type: datetime
        """
        self._time_return_window_starts = time_return_window_starts

    @property
    def oracle_shipping_tracking_url(self):
        """
        Gets the oracle_shipping_tracking_url of this RoverNode.
        Tracking Url for the shipped RoverNode.


        :return: The oracle_shipping_tracking_url of this RoverNode.
        :rtype: str
        """
        return self._oracle_shipping_tracking_url

    @oracle_shipping_tracking_url.setter
    def oracle_shipping_tracking_url(self, oracle_shipping_tracking_url):
        """
        Sets the oracle_shipping_tracking_url of this RoverNode.
        Tracking Url for the shipped RoverNode.


        :param oracle_shipping_tracking_url: The oracle_shipping_tracking_url of this RoverNode.
        :type: str
        """
        self._oracle_shipping_tracking_url = oracle_shipping_tracking_url

    @property
    def time_return_window_ends(self):
        """
        Gets the time_return_window_ends of this RoverNode.
        End time for the window to pickup the device from customer.


        :return: The time_return_window_ends of this RoverNode.
        :rtype: datetime
        """
        return self._time_return_window_ends

    @time_return_window_ends.setter
    def time_return_window_ends(self, time_return_window_ends):
        """
        Sets the time_return_window_ends of this RoverNode.
        End time for the window to pickup the device from customer.


        :param time_return_window_ends: The time_return_window_ends of this RoverNode.
        :type: datetime
        """
        self._time_return_window_ends = time_return_window_ends

    @property
    def return_shipping_label_uri(self):
        """
        Gets the return_shipping_label_uri of this RoverNode.
        Uri to download return shipping label.


        :return: The return_shipping_label_uri of this RoverNode.
        :rtype: str
        """
        return self._return_shipping_label_uri

    @return_shipping_label_uri.setter
    def return_shipping_label_uri(self, return_shipping_label_uri):
        """
        Sets the return_shipping_label_uri of this RoverNode.
        Uri to download return shipping label.


        :param return_shipping_label_uri: The return_shipping_label_uri of this RoverNode.
        :type: str
        """
        self._return_shipping_label_uri = return_shipping_label_uri

    @property
    def is_import_requested(self):
        """
        Gets the is_import_requested of this RoverNode.
        The flag indicating that customer requests data to be imported to OCI upon Rover node return.


        :return: The is_import_requested of this RoverNode.
        :rtype: bool
        """
        return self._is_import_requested

    @is_import_requested.setter
    def is_import_requested(self, is_import_requested):
        """
        Sets the is_import_requested of this RoverNode.
        The flag indicating that customer requests data to be imported to OCI upon Rover node return.


        :param is_import_requested: The is_import_requested of this RoverNode.
        :type: bool
        """
        self._is_import_requested = is_import_requested

    @property
    def import_compartment_id(self):
        """
        Gets the import_compartment_id of this RoverNode.
        An OCID of a compartment where data will be imported to upon Rover node return.


        :return: The import_compartment_id of this RoverNode.
        :rtype: str
        """
        return self._import_compartment_id

    @import_compartment_id.setter
    def import_compartment_id(self, import_compartment_id):
        """
        Sets the import_compartment_id of this RoverNode.
        An OCID of a compartment where data will be imported to upon Rover node return.


        :param import_compartment_id: The import_compartment_id of this RoverNode.
        :type: str
        """
        self._import_compartment_id = import_compartment_id

    @property
    def import_file_bucket(self):
        """
        Gets the import_file_bucket of this RoverNode.
        Name of a bucket where files from NFS share will be imported to upon Rover node return.


        :return: The import_file_bucket of this RoverNode.
        :rtype: str
        """
        return self._import_file_bucket

    @import_file_bucket.setter
    def import_file_bucket(self, import_file_bucket):
        """
        Sets the import_file_bucket of this RoverNode.
        Name of a bucket where files from NFS share will be imported to upon Rover node return.


        :param import_file_bucket: The import_file_bucket of this RoverNode.
        :type: str
        """
        self._import_file_bucket = import_file_bucket

    @property
    def data_validation_code(self):
        """
        Gets the data_validation_code of this RoverNode.
        Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.


        :return: The data_validation_code of this RoverNode.
        :rtype: str
        """
        return self._data_validation_code

    @data_validation_code.setter
    def data_validation_code(self, data_validation_code):
        """
        Sets the data_validation_code of this RoverNode.
        Validation code returned by data validation tool. Required for return shipping label generation if data import was requested.


        :param data_validation_code: The data_validation_code of this RoverNode.
        :type: str
        """
        self._data_validation_code = data_validation_code

    @property
    def public_key(self):
        """
        Gets the public_key of this RoverNode.
        The public key of the resource principal


        :return: The public_key of this RoverNode.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this RoverNode.
        The public key of the resource principal


        :param public_key: The public_key of this RoverNode.
        :type: str
        """
        self._public_key = public_key

    @property
    def image_export_par(self):
        """
        Gets the image_export_par of this RoverNode.
        The link to pre-authenticated request for a bucket where image workloads are moved.


        :return: The image_export_par of this RoverNode.
        :rtype: str
        """
        return self._image_export_par

    @image_export_par.setter
    def image_export_par(self, image_export_par):
        """
        Sets the image_export_par of this RoverNode.
        The link to pre-authenticated request for a bucket where image workloads are moved.


        :param image_export_par: The image_export_par of this RoverNode.
        :type: str
        """
        self._image_export_par = image_export_par

    @property
    def tags(self):
        """
        Gets the tags of this RoverNode.
        The tags associated with tagSlug.


        :return: The tags of this RoverNode.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this RoverNode.
        The tags associated with tagSlug.


        :param tags: The tags of this RoverNode.
        :type: str
        """
        self._tags = tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RoverNode.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RoverNode.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RoverNode.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RoverNode.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RoverNode.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RoverNode.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RoverNode.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RoverNode.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RoverNode.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this RoverNode.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RoverNode.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this RoverNode.
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
