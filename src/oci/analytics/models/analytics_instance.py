# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyticsInstance(object):
    """
    Analytics Instance metadata.
    """

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the feature_set property of a AnalyticsInstance.
    #: This constant has a value of "SELF_SERVICE_ANALYTICS"
    FEATURE_SET_SELF_SERVICE_ANALYTICS = "SELF_SERVICE_ANALYTICS"

    #: A constant which can be used with the feature_set property of a AnalyticsInstance.
    #: This constant has a value of "ENTERPRISE_ANALYTICS"
    FEATURE_SET_ENTERPRISE_ANALYTICS = "ENTERPRISE_ANALYTICS"

    #: A constant which can be used with the license_type property of a AnalyticsInstance.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_TYPE_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_type property of a AnalyticsInstance.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyticsInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AnalyticsInstance.
        :type id: str

        :param name:
            The value to assign to the name property of this AnalyticsInstance.
        :type name: str

        :param description:
            The value to assign to the description property of this AnalyticsInstance.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AnalyticsInstance.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnalyticsInstance.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param feature_set:
            The value to assign to the feature_set property of this AnalyticsInstance.
            Allowed values for this property are: "SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type feature_set: str

        :param capacity:
            The value to assign to the capacity property of this AnalyticsInstance.
        :type capacity: oci.analytics.models.Capacity

        :param license_type:
            The value to assign to the license_type property of this AnalyticsInstance.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_type: str

        :param email_notification:
            The value to assign to the email_notification property of this AnalyticsInstance.
        :type email_notification: str

        :param network_endpoint_details:
            The value to assign to the network_endpoint_details property of this AnalyticsInstance.
        :type network_endpoint_details: oci.analytics.models.NetworkEndpointDetails

        :param private_access_channels:
            The value to assign to the private_access_channels property of this AnalyticsInstance.
        :type private_access_channels: dict(str, PrivateAccessChannel)

        :param vanity_url_details:
            The value to assign to the vanity_url_details property of this AnalyticsInstance.
        :type vanity_url_details: dict(str, VanityUrlDetails)

        :param service_url:
            The value to assign to the service_url property of this AnalyticsInstance.
        :type service_url: str

        :param defined_tags:
            The value to assign to the defined_tags property of this AnalyticsInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AnalyticsInstance.
        :type freeform_tags: dict(str, str)

        :param kms_key_id:
            The value to assign to the kms_key_id property of this AnalyticsInstance.
        :type kms_key_id: str

        :param time_created:
            The value to assign to the time_created property of this AnalyticsInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnalyticsInstance.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'feature_set': 'str',
            'capacity': 'Capacity',
            'license_type': 'str',
            'email_notification': 'str',
            'network_endpoint_details': 'NetworkEndpointDetails',
            'private_access_channels': 'dict(str, PrivateAccessChannel)',
            'vanity_url_details': 'dict(str, VanityUrlDetails)',
            'service_url': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'kms_key_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'feature_set': 'featureSet',
            'capacity': 'capacity',
            'license_type': 'licenseType',
            'email_notification': 'emailNotification',
            'network_endpoint_details': 'networkEndpointDetails',
            'private_access_channels': 'privateAccessChannels',
            'vanity_url_details': 'vanityUrlDetails',
            'service_url': 'serviceUrl',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'kms_key_id': 'kmsKeyId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._name = None
        self._description = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._feature_set = None
        self._capacity = None
        self._license_type = None
        self._email_notification = None
        self._network_endpoint_details = None
        self._private_access_channels = None
        self._vanity_url_details = None
        self._service_url = None
        self._defined_tags = None
        self._freeform_tags = None
        self._kms_key_id = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AnalyticsInstance.
        The resource OCID.


        :return: The id of this AnalyticsInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AnalyticsInstance.
        The resource OCID.


        :param id: The id of this AnalyticsInstance.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AnalyticsInstance.
        The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.


        :return: The name of this AnalyticsInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AnalyticsInstance.
        The name of the Analytics instance. This name must be unique in the tenancy and cannot be changed.


        :param name: The name of this AnalyticsInstance.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this AnalyticsInstance.
        Optional description.


        :return: The description of this AnalyticsInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AnalyticsInstance.
        Optional description.


        :param description: The description of this AnalyticsInstance.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AnalyticsInstance.
        The OCID of the compartment.


        :return: The compartment_id of this AnalyticsInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AnalyticsInstance.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this AnalyticsInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AnalyticsInstance.
        The current state of an instance.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AnalyticsInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnalyticsInstance.
        The current state of an instance.


        :param lifecycle_state: The lifecycle_state of this AnalyticsInstance.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "INACTIVE", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def feature_set(self):
        """
        **[Required]** Gets the feature_set of this AnalyticsInstance.
        Analytics feature set.

        Allowed values for this property are: "SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The feature_set of this AnalyticsInstance.
        :rtype: str
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        """
        Sets the feature_set of this AnalyticsInstance.
        Analytics feature set.


        :param feature_set: The feature_set of this AnalyticsInstance.
        :type: str
        """
        allowed_values = ["SELF_SERVICE_ANALYTICS", "ENTERPRISE_ANALYTICS"]
        if not value_allowed_none_or_none_sentinel(feature_set, allowed_values):
            feature_set = 'UNKNOWN_ENUM_VALUE'
        self._feature_set = feature_set

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this AnalyticsInstance.

        :return: The capacity of this AnalyticsInstance.
        :rtype: oci.analytics.models.Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this AnalyticsInstance.

        :param capacity: The capacity of this AnalyticsInstance.
        :type: oci.analytics.models.Capacity
        """
        self._capacity = capacity

    @property
    def license_type(self):
        """
        Gets the license_type of this AnalyticsInstance.
        The license used for the service.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_type of this AnalyticsInstance.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this AnalyticsInstance.
        The license used for the service.


        :param license_type: The license_type of this AnalyticsInstance.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            license_type = 'UNKNOWN_ENUM_VALUE'
        self._license_type = license_type

    @property
    def email_notification(self):
        """
        Gets the email_notification of this AnalyticsInstance.
        Email address receiving notifications.


        :return: The email_notification of this AnalyticsInstance.
        :rtype: str
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """
        Sets the email_notification of this AnalyticsInstance.
        Email address receiving notifications.


        :param email_notification: The email_notification of this AnalyticsInstance.
        :type: str
        """
        self._email_notification = email_notification

    @property
    def network_endpoint_details(self):
        """
        **[Required]** Gets the network_endpoint_details of this AnalyticsInstance.

        :return: The network_endpoint_details of this AnalyticsInstance.
        :rtype: oci.analytics.models.NetworkEndpointDetails
        """
        return self._network_endpoint_details

    @network_endpoint_details.setter
    def network_endpoint_details(self, network_endpoint_details):
        """
        Sets the network_endpoint_details of this AnalyticsInstance.

        :param network_endpoint_details: The network_endpoint_details of this AnalyticsInstance.
        :type: oci.analytics.models.NetworkEndpointDetails
        """
        self._network_endpoint_details = network_endpoint_details

    @property
    def private_access_channels(self):
        """
        Gets the private_access_channels of this AnalyticsInstance.
        Map of PrivateAccessChannel unique identifier key as KEY and PrivateAccessChannel Object as VALUE.


        :return: The private_access_channels of this AnalyticsInstance.
        :rtype: dict(str, PrivateAccessChannel)
        """
        return self._private_access_channels

    @private_access_channels.setter
    def private_access_channels(self, private_access_channels):
        """
        Sets the private_access_channels of this AnalyticsInstance.
        Map of PrivateAccessChannel unique identifier key as KEY and PrivateAccessChannel Object as VALUE.


        :param private_access_channels: The private_access_channels of this AnalyticsInstance.
        :type: dict(str, PrivateAccessChannel)
        """
        self._private_access_channels = private_access_channels

    @property
    def vanity_url_details(self):
        """
        Gets the vanity_url_details of this AnalyticsInstance.
        Map of VanityUrl unique identifier key as KEY and VanityUrl Object as VALUE.


        :return: The vanity_url_details of this AnalyticsInstance.
        :rtype: dict(str, VanityUrlDetails)
        """
        return self._vanity_url_details

    @vanity_url_details.setter
    def vanity_url_details(self, vanity_url_details):
        """
        Sets the vanity_url_details of this AnalyticsInstance.
        Map of VanityUrl unique identifier key as KEY and VanityUrl Object as VALUE.


        :param vanity_url_details: The vanity_url_details of this AnalyticsInstance.
        :type: dict(str, VanityUrlDetails)
        """
        self._vanity_url_details = vanity_url_details

    @property
    def service_url(self):
        """
        Gets the service_url of this AnalyticsInstance.
        URL of the Analytics service.


        :return: The service_url of this AnalyticsInstance.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """
        Sets the service_url of this AnalyticsInstance.
        URL of the Analytics service.


        :param service_url: The service_url of this AnalyticsInstance.
        :type: str
        """
        self._service_url = service_url

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AnalyticsInstance.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AnalyticsInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AnalyticsInstance.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AnalyticsInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AnalyticsInstance.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AnalyticsInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AnalyticsInstance.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AnalyticsInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this AnalyticsInstance.
        The `OCID`__ of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this AnalyticsInstance.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this AnalyticsInstance.
        The `OCID`__ of the OCI Vault Key encrypting the customer data stored in this Analytics instance. A null value indicates Oracle managed default encryption.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this AnalyticsInstance.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AnalyticsInstance.
        The date and time the instance was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this AnalyticsInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AnalyticsInstance.
        The date and time the instance was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this AnalyticsInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AnalyticsInstance.
        The date and time the instance was last updated (in the format defined by RFC3339).
        This timestamp represents updates made through this API. External events do not
        influence it.


        :return: The time_updated of this AnalyticsInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AnalyticsInstance.
        The date and time the instance was last updated (in the format defined by RFC3339).
        This timestamp represents updates made through this API. External events do not
        influence it.


        :param time_updated: The time_updated of this AnalyticsInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
