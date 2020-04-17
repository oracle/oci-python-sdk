# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplianceExportJob(object):
    """
    ApplianceExportJob model.
    """

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "INPROGRESS"
    LIFECYCLE_STATE_INPROGRESS = "INPROGRESS"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJob.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplianceExportJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApplianceExportJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ApplianceExportJob.
        :type compartment_id: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ApplianceExportJob.
        :type bucket_name: str

        :param display_name:
            The value to assign to the display_name property of this ApplianceExportJob.
        :type display_name: str

        :param creation_time:
            The value to assign to the creation_time property of this ApplianceExportJob.
        :type creation_time: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApplianceExportJob.
            Allowed values for this property are: "CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this ApplianceExportJob.
        :type lifecycle_state_details: str

        :param appliance_serial_number:
            The value to assign to the appliance_serial_number property of this ApplianceExportJob.
        :type appliance_serial_number: str

        :param appliance_decryption_passphrase:
            The value to assign to the appliance_decryption_passphrase property of this ApplianceExportJob.
        :type appliance_decryption_passphrase: str

        :param appliance_delivery_vendor:
            The value to assign to the appliance_delivery_vendor property of this ApplianceExportJob.
        :type appliance_delivery_vendor: str

        :param appliance_delivery_tracking_number:
            The value to assign to the appliance_delivery_tracking_number property of this ApplianceExportJob.
        :type appliance_delivery_tracking_number: str

        :param appliance_return_delivery_tracking_number:
            The value to assign to the appliance_return_delivery_tracking_number property of this ApplianceExportJob.
        :type appliance_return_delivery_tracking_number: str

        :param sending_security_tie:
            The value to assign to the sending_security_tie property of this ApplianceExportJob.
        :type sending_security_tie: str

        :param receiving_security_tie:
            The value to assign to the receiving_security_tie property of this ApplianceExportJob.
        :type receiving_security_tie: str

        :param prefix:
            The value to assign to the prefix property of this ApplianceExportJob.
        :type prefix: str

        :param range_start:
            The value to assign to the range_start property of this ApplianceExportJob.
        :type range_start: str

        :param range_end:
            The value to assign to the range_end property of this ApplianceExportJob.
        :type range_end: str

        :param number_of_objects:
            The value to assign to the number_of_objects property of this ApplianceExportJob.
        :type number_of_objects: str

        :param total_size_in_bytes:
            The value to assign to the total_size_in_bytes property of this ApplianceExportJob.
        :type total_size_in_bytes: str

        :param first_object:
            The value to assign to the first_object property of this ApplianceExportJob.
        :type first_object: str

        :param last_object:
            The value to assign to the last_object property of this ApplianceExportJob.
        :type last_object: str

        :param next_object:
            The value to assign to the next_object property of this ApplianceExportJob.
        :type next_object: str

        :param manifest_file:
            The value to assign to the manifest_file property of this ApplianceExportJob.
        :type manifest_file: str

        :param manifest_md5:
            The value to assign to the manifest_md5 property of this ApplianceExportJob.
        :type manifest_md5: str

        :param bucket_access_policies:
            The value to assign to the bucket_access_policies property of this ApplianceExportJob.
        :type bucket_access_policies: list[str]

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this ApplianceExportJob.
        :type customer_shipping_address: ShippingAddress

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApplianceExportJob.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApplianceExportJob.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'bucket_name': 'str',
            'display_name': 'str',
            'creation_time': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'appliance_serial_number': 'str',
            'appliance_decryption_passphrase': 'str',
            'appliance_delivery_vendor': 'str',
            'appliance_delivery_tracking_number': 'str',
            'appliance_return_delivery_tracking_number': 'str',
            'sending_security_tie': 'str',
            'receiving_security_tie': 'str',
            'prefix': 'str',
            'range_start': 'str',
            'range_end': 'str',
            'number_of_objects': 'str',
            'total_size_in_bytes': 'str',
            'first_object': 'str',
            'last_object': 'str',
            'next_object': 'str',
            'manifest_file': 'str',
            'manifest_md5': 'str',
            'bucket_access_policies': 'list[str]',
            'customer_shipping_address': 'ShippingAddress',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'bucket_name': 'bucketName',
            'display_name': 'displayName',
            'creation_time': 'creationTime',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'appliance_serial_number': 'applianceSerialNumber',
            'appliance_decryption_passphrase': 'applianceDecryptionPassphrase',
            'appliance_delivery_vendor': 'applianceDeliveryVendor',
            'appliance_delivery_tracking_number': 'applianceDeliveryTrackingNumber',
            'appliance_return_delivery_tracking_number': 'applianceReturnDeliveryTrackingNumber',
            'sending_security_tie': 'sendingSecurityTie',
            'receiving_security_tie': 'receivingSecurityTie',
            'prefix': 'prefix',
            'range_start': 'rangeStart',
            'range_end': 'rangeEnd',
            'number_of_objects': 'numberOfObjects',
            'total_size_in_bytes': 'totalSizeInBytes',
            'first_object': 'firstObject',
            'last_object': 'lastObject',
            'next_object': 'nextObject',
            'manifest_file': 'manifestFile',
            'manifest_md5': 'manifestMd5',
            'bucket_access_policies': 'bucketAccessPolicies',
            'customer_shipping_address': 'customerShippingAddress',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._bucket_name = None
        self._display_name = None
        self._creation_time = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._appliance_serial_number = None
        self._appliance_decryption_passphrase = None
        self._appliance_delivery_vendor = None
        self._appliance_delivery_tracking_number = None
        self._appliance_return_delivery_tracking_number = None
        self._sending_security_tie = None
        self._receiving_security_tie = None
        self._prefix = None
        self._range_start = None
        self._range_end = None
        self._number_of_objects = None
        self._total_size_in_bytes = None
        self._first_object = None
        self._last_object = None
        self._next_object = None
        self._manifest_file = None
        self._manifest_md5 = None
        self._bucket_access_policies = None
        self._customer_shipping_address = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApplianceExportJob.

        :return: The id of this ApplianceExportJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApplianceExportJob.

        :param id: The id of this ApplianceExportJob.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ApplianceExportJob.

        :return: The compartment_id of this ApplianceExportJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ApplianceExportJob.

        :param compartment_id: The compartment_id of this ApplianceExportJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ApplianceExportJob.

        :return: The bucket_name of this ApplianceExportJob.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ApplianceExportJob.

        :param bucket_name: The bucket_name of this ApplianceExportJob.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def display_name(self):
        """
        Gets the display_name of this ApplianceExportJob.

        :return: The display_name of this ApplianceExportJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplianceExportJob.

        :param display_name: The display_name of this ApplianceExportJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def creation_time(self):
        """
        Gets the creation_time of this ApplianceExportJob.

        :return: The creation_time of this ApplianceExportJob.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this ApplianceExportJob.

        :param creation_time: The creation_time of this ApplianceExportJob.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApplianceExportJob.
        Allowed values for this property are: "CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ApplianceExportJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApplianceExportJob.

        :param lifecycle_state: The lifecycle_state of this ApplianceExportJob.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this ApplianceExportJob.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this ApplianceExportJob.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this ApplianceExportJob.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this ApplianceExportJob.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def appliance_serial_number(self):
        """
        Gets the appliance_serial_number of this ApplianceExportJob.
        Serial Number of the Appliance associated with this Export Job.


        :return: The appliance_serial_number of this ApplianceExportJob.
        :rtype: str
        """
        return self._appliance_serial_number

    @appliance_serial_number.setter
    def appliance_serial_number(self, appliance_serial_number):
        """
        Sets the appliance_serial_number of this ApplianceExportJob.
        Serial Number of the Appliance associated with this Export Job.


        :param appliance_serial_number: The appliance_serial_number of this ApplianceExportJob.
        :type: str
        """
        self._appliance_serial_number = appliance_serial_number

    @property
    def appliance_decryption_passphrase(self):
        """
        Gets the appliance_decryption_passphrase of this ApplianceExportJob.
        Passphrase associated with the Appliance.


        :return: The appliance_decryption_passphrase of this ApplianceExportJob.
        :rtype: str
        """
        return self._appliance_decryption_passphrase

    @appliance_decryption_passphrase.setter
    def appliance_decryption_passphrase(self, appliance_decryption_passphrase):
        """
        Sets the appliance_decryption_passphrase of this ApplianceExportJob.
        Passphrase associated with the Appliance.


        :param appliance_decryption_passphrase: The appliance_decryption_passphrase of this ApplianceExportJob.
        :type: str
        """
        self._appliance_decryption_passphrase = appliance_decryption_passphrase

    @property
    def appliance_delivery_vendor(self):
        """
        Gets the appliance_delivery_vendor of this ApplianceExportJob.
        Shipping Vendor selected to ship the Appliance associated with this job.


        :return: The appliance_delivery_vendor of this ApplianceExportJob.
        :rtype: str
        """
        return self._appliance_delivery_vendor

    @appliance_delivery_vendor.setter
    def appliance_delivery_vendor(self, appliance_delivery_vendor):
        """
        Sets the appliance_delivery_vendor of this ApplianceExportJob.
        Shipping Vendor selected to ship the Appliance associated with this job.


        :param appliance_delivery_vendor: The appliance_delivery_vendor of this ApplianceExportJob.
        :type: str
        """
        self._appliance_delivery_vendor = appliance_delivery_vendor

    @property
    def appliance_delivery_tracking_number(self):
        """
        Gets the appliance_delivery_tracking_number of this ApplianceExportJob.
        Tracking number associated with the shipment while shipping the Appliance to Customer.


        :return: The appliance_delivery_tracking_number of this ApplianceExportJob.
        :rtype: str
        """
        return self._appliance_delivery_tracking_number

    @appliance_delivery_tracking_number.setter
    def appliance_delivery_tracking_number(self, appliance_delivery_tracking_number):
        """
        Sets the appliance_delivery_tracking_number of this ApplianceExportJob.
        Tracking number associated with the shipment while shipping the Appliance to Customer.


        :param appliance_delivery_tracking_number: The appliance_delivery_tracking_number of this ApplianceExportJob.
        :type: str
        """
        self._appliance_delivery_tracking_number = appliance_delivery_tracking_number

    @property
    def appliance_return_delivery_tracking_number(self):
        """
        Gets the appliance_return_delivery_tracking_number of this ApplianceExportJob.
        Tracking number associated with the shipment while shipping the Appliance back to Oracle.


        :return: The appliance_return_delivery_tracking_number of this ApplianceExportJob.
        :rtype: str
        """
        return self._appliance_return_delivery_tracking_number

    @appliance_return_delivery_tracking_number.setter
    def appliance_return_delivery_tracking_number(self, appliance_return_delivery_tracking_number):
        """
        Sets the appliance_return_delivery_tracking_number of this ApplianceExportJob.
        Tracking number associated with the shipment while shipping the Appliance back to Oracle.


        :param appliance_return_delivery_tracking_number: The appliance_return_delivery_tracking_number of this ApplianceExportJob.
        :type: str
        """
        self._appliance_return_delivery_tracking_number = appliance_return_delivery_tracking_number

    @property
    def sending_security_tie(self):
        """
        Gets the sending_security_tie of this ApplianceExportJob.
        Unique number associated with the security tie used to seal the Appliance case.


        :return: The sending_security_tie of this ApplianceExportJob.
        :rtype: str
        """
        return self._sending_security_tie

    @sending_security_tie.setter
    def sending_security_tie(self, sending_security_tie):
        """
        Sets the sending_security_tie of this ApplianceExportJob.
        Unique number associated with the security tie used to seal the Appliance case.


        :param sending_security_tie: The sending_security_tie of this ApplianceExportJob.
        :type: str
        """
        self._sending_security_tie = sending_security_tie

    @property
    def receiving_security_tie(self):
        """
        Gets the receiving_security_tie of this ApplianceExportJob.
        Unique number associated with the return security tie used to seal the Appliance case.


        :return: The receiving_security_tie of this ApplianceExportJob.
        :rtype: str
        """
        return self._receiving_security_tie

    @receiving_security_tie.setter
    def receiving_security_tie(self, receiving_security_tie):
        """
        Sets the receiving_security_tie of this ApplianceExportJob.
        Unique number associated with the return security tie used to seal the Appliance case.


        :param receiving_security_tie: The receiving_security_tie of this ApplianceExportJob.
        :type: str
        """
        self._receiving_security_tie = receiving_security_tie

    @property
    def prefix(self):
        """
        Gets the prefix of this ApplianceExportJob.
        List of objects with names matching this prefix would be part of this export job.


        :return: The prefix of this ApplianceExportJob.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this ApplianceExportJob.
        List of objects with names matching this prefix would be part of this export job.


        :param prefix: The prefix of this ApplianceExportJob.
        :type: str
        """
        self._prefix = prefix

    @property
    def range_start(self):
        """
        Gets the range_start of this ApplianceExportJob.
        The name of the first object in the range of objects that are expected to be part of this export job.


        :return: The range_start of this ApplianceExportJob.
        :rtype: str
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """
        Sets the range_start of this ApplianceExportJob.
        The name of the first object in the range of objects that are expected to be part of this export job.


        :param range_start: The range_start of this ApplianceExportJob.
        :type: str
        """
        self._range_start = range_start

    @property
    def range_end(self):
        """
        Gets the range_end of this ApplianceExportJob.
        The name of the last object in the range of objects that are expected to be part of this export job.


        :return: The range_end of this ApplianceExportJob.
        :rtype: str
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """
        Sets the range_end of this ApplianceExportJob.
        The name of the last object in the range of objects that are expected to be part of this export job.


        :param range_end: The range_end of this ApplianceExportJob.
        :type: str
        """
        self._range_end = range_end

    @property
    def number_of_objects(self):
        """
        Gets the number_of_objects of this ApplianceExportJob.
        Total number of objects that are exported in this job.


        :return: The number_of_objects of this ApplianceExportJob.
        :rtype: str
        """
        return self._number_of_objects

    @number_of_objects.setter
    def number_of_objects(self, number_of_objects):
        """
        Sets the number_of_objects of this ApplianceExportJob.
        Total number of objects that are exported in this job.


        :param number_of_objects: The number_of_objects of this ApplianceExportJob.
        :type: str
        """
        self._number_of_objects = number_of_objects

    @property
    def total_size_in_bytes(self):
        """
        Gets the total_size_in_bytes of this ApplianceExportJob.
        Total size of objects in Bytes that are exported in this job.


        :return: The total_size_in_bytes of this ApplianceExportJob.
        :rtype: str
        """
        return self._total_size_in_bytes

    @total_size_in_bytes.setter
    def total_size_in_bytes(self, total_size_in_bytes):
        """
        Sets the total_size_in_bytes of this ApplianceExportJob.
        Total size of objects in Bytes that are exported in this job.


        :param total_size_in_bytes: The total_size_in_bytes of this ApplianceExportJob.
        :type: str
        """
        self._total_size_in_bytes = total_size_in_bytes

    @property
    def first_object(self):
        """
        Gets the first_object of this ApplianceExportJob.
        First object in the list of objects that are exported in this job.


        :return: The first_object of this ApplianceExportJob.
        :rtype: str
        """
        return self._first_object

    @first_object.setter
    def first_object(self, first_object):
        """
        Sets the first_object of this ApplianceExportJob.
        First object in the list of objects that are exported in this job.


        :param first_object: The first_object of this ApplianceExportJob.
        :type: str
        """
        self._first_object = first_object

    @property
    def last_object(self):
        """
        Gets the last_object of this ApplianceExportJob.
        Last object in the list of objects that are exported in this job.


        :return: The last_object of this ApplianceExportJob.
        :rtype: str
        """
        return self._last_object

    @last_object.setter
    def last_object(self, last_object):
        """
        Sets the last_object of this ApplianceExportJob.
        Last object in the list of objects that are exported in this job.


        :param last_object: The last_object of this ApplianceExportJob.
        :type: str
        """
        self._last_object = last_object

    @property
    def next_object(self):
        """
        Gets the next_object of this ApplianceExportJob.
        First object from which the next potential export job could start.


        :return: The next_object of this ApplianceExportJob.
        :rtype: str
        """
        return self._next_object

    @next_object.setter
    def next_object(self, next_object):
        """
        Sets the next_object of this ApplianceExportJob.
        First object from which the next potential export job could start.


        :param next_object: The next_object of this ApplianceExportJob.
        :type: str
        """
        self._next_object = next_object

    @property
    def manifest_file(self):
        """
        Gets the manifest_file of this ApplianceExportJob.
        Url of the Manifest File associated with this export job.


        :return: The manifest_file of this ApplianceExportJob.
        :rtype: str
        """
        return self._manifest_file

    @manifest_file.setter
    def manifest_file(self, manifest_file):
        """
        Sets the manifest_file of this ApplianceExportJob.
        Url of the Manifest File associated with this export job.


        :param manifest_file: The manifest_file of this ApplianceExportJob.
        :type: str
        """
        self._manifest_file = manifest_file

    @property
    def manifest_md5(self):
        """
        Gets the manifest_md5 of this ApplianceExportJob.
        md5 digest of the manifest file.


        :return: The manifest_md5 of this ApplianceExportJob.
        :rtype: str
        """
        return self._manifest_md5

    @manifest_md5.setter
    def manifest_md5(self, manifest_md5):
        """
        Sets the manifest_md5 of this ApplianceExportJob.
        md5 digest of the manifest file.


        :param manifest_md5: The manifest_md5 of this ApplianceExportJob.
        :type: str
        """
        self._manifest_md5 = manifest_md5

    @property
    def bucket_access_policies(self):
        """
        Gets the bucket_access_policies of this ApplianceExportJob.
        Polices to grant Data Transfer Service to access objects in the Bucket


        :return: The bucket_access_policies of this ApplianceExportJob.
        :rtype: list[str]
        """
        return self._bucket_access_policies

    @bucket_access_policies.setter
    def bucket_access_policies(self, bucket_access_policies):
        """
        Sets the bucket_access_policies of this ApplianceExportJob.
        Polices to grant Data Transfer Service to access objects in the Bucket


        :param bucket_access_policies: The bucket_access_policies of this ApplianceExportJob.
        :type: list[str]
        """
        self._bucket_access_policies = bucket_access_policies

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this ApplianceExportJob.

        :return: The customer_shipping_address of this ApplianceExportJob.
        :rtype: ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this ApplianceExportJob.

        :param customer_shipping_address: The customer_shipping_address of this ApplianceExportJob.
        :type: ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ApplianceExportJob.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ApplianceExportJob.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApplianceExportJob.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ApplianceExportJob.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ApplianceExportJob.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ApplianceExportJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApplianceExportJob.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ApplianceExportJob.
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
