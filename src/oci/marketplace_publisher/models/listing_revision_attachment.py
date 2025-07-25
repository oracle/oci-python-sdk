# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListingRevisionAttachment(object):
    """
    A attachment for the listing revision. User can provide an external URL/upload a file
    """

    #: A constant which can be used with the attachment_type property of a ListingRevisionAttachment.
    #: This constant has a value of "RELATED_DOCUMENT"
    ATTACHMENT_TYPE_RELATED_DOCUMENT = "RELATED_DOCUMENT"

    #: A constant which can be used with the attachment_type property of a ListingRevisionAttachment.
    #: This constant has a value of "SCREENSHOT"
    ATTACHMENT_TYPE_SCREENSHOT = "SCREENSHOT"

    #: A constant which can be used with the attachment_type property of a ListingRevisionAttachment.
    #: This constant has a value of "VIDEO"
    ATTACHMENT_TYPE_VIDEO = "VIDEO"

    #: A constant which can be used with the attachment_type property of a ListingRevisionAttachment.
    #: This constant has a value of "REVIEW_SUPPORT_DOCUMENT"
    ATTACHMENT_TYPE_REVIEW_SUPPORT_DOCUMENT = "REVIEW_SUPPORT_DOCUMENT"

    #: A constant which can be used with the attachment_type property of a ListingRevisionAttachment.
    #: This constant has a value of "CUSTOMER_SUCCESS"
    ATTACHMENT_TYPE_CUSTOMER_SUCCESS = "CUSTOMER_SUCCESS"

    #: A constant which can be used with the attachment_type property of a ListingRevisionAttachment.
    #: This constant has a value of "SUPPORTED_SERVICES"
    ATTACHMENT_TYPE_SUPPORTED_SERVICES = "SUPPORTED_SERVICES"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionAttachment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionAttachment.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ListingRevisionAttachment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ListingRevisionAttachment object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace_publisher.models.RelatedDocumentAttachment`
        * :class:`~oci.marketplace_publisher.models.ScreenShotAttachment`
        * :class:`~oci.marketplace_publisher.models.ReviewSupportDocumentAttachment`
        * :class:`~oci.marketplace_publisher.models.SupportedServiceAttachment`
        * :class:`~oci.marketplace_publisher.models.VideoAttachment`
        * :class:`~oci.marketplace_publisher.models.CustomerSuccessAttachment`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ListingRevisionAttachment.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ListingRevisionAttachment.
        :type compartment_id: str

        :param listing_revision_id:
            The value to assign to the listing_revision_id property of this ListingRevisionAttachment.
        :type listing_revision_id: str

        :param display_name:
            The value to assign to the display_name property of this ListingRevisionAttachment.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ListingRevisionAttachment.
        :type description: str

        :param attachment_type:
            The value to assign to the attachment_type property of this ListingRevisionAttachment.
            Allowed values for this property are: "RELATED_DOCUMENT", "SCREENSHOT", "VIDEO", "REVIEW_SUPPORT_DOCUMENT", "CUSTOMER_SUCCESS", "SUPPORTED_SERVICES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attachment_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ListingRevisionAttachment.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ListingRevisionAttachment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ListingRevisionAttachment.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ListingRevisionAttachment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ListingRevisionAttachment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ListingRevisionAttachment.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'listing_revision_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'attachment_type': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'listing_revision_id': 'listingRevisionId',
            'display_name': 'displayName',
            'description': 'description',
            'attachment_type': 'attachmentType',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._listing_revision_id = None
        self._display_name = None
        self._description = None
        self._attachment_type = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['attachmentType']

        if type == 'RELATED_DOCUMENT':
            return 'RelatedDocumentAttachment'

        if type == 'SCREENSHOT':
            return 'ScreenShotAttachment'

        if type == 'REVIEW_SUPPORT_DOCUMENT':
            return 'ReviewSupportDocumentAttachment'

        if type == 'SUPPORTED_SERVICES':
            return 'SupportedServiceAttachment'

        if type == 'VIDEO':
            return 'VideoAttachment'

        if type == 'CUSTOMER_SUCCESS':
            return 'CustomerSuccessAttachment'
        else:
            return 'ListingRevisionAttachment'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ListingRevisionAttachment.
        Unique OCID identifier for the listing revision attachment.


        :return: The id of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ListingRevisionAttachment.
        Unique OCID identifier for the listing revision attachment.


        :param id: The id of this ListingRevisionAttachment.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ListingRevisionAttachment.
        The unique identifier for the compartment.


        :return: The compartment_id of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ListingRevisionAttachment.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this ListingRevisionAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def listing_revision_id(self):
        """
        **[Required]** Gets the listing_revision_id of this ListingRevisionAttachment.
        The unique identifier of the listing revision that the specified attachment belongs to.


        :return: The listing_revision_id of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._listing_revision_id

    @listing_revision_id.setter
    def listing_revision_id(self, listing_revision_id):
        """
        Sets the listing_revision_id of this ListingRevisionAttachment.
        The unique identifier of the listing revision that the specified attachment belongs to.


        :param listing_revision_id: The listing_revision_id of this ListingRevisionAttachment.
        :type: str
        """
        self._listing_revision_id = listing_revision_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ListingRevisionAttachment.
        Name of the listing revision attachment.


        :return: The display_name of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ListingRevisionAttachment.
        Name of the listing revision attachment.


        :param display_name: The display_name of this ListingRevisionAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ListingRevisionAttachment.
        Description of the listing revision attachment.


        :return: The description of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ListingRevisionAttachment.
        Description of the listing revision attachment.


        :param description: The description of this ListingRevisionAttachment.
        :type: str
        """
        self._description = description

    @property
    def attachment_type(self):
        """
        **[Required]** Gets the attachment_type of this ListingRevisionAttachment.
        Possible values for the publisher listing revision attachments. The attachment type informs the type of attachment for the listing revision.

        Allowed values for this property are: "RELATED_DOCUMENT", "SCREENSHOT", "VIDEO", "REVIEW_SUPPORT_DOCUMENT", "CUSTOMER_SUCCESS", "SUPPORTED_SERVICES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attachment_type of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """
        Sets the attachment_type of this ListingRevisionAttachment.
        Possible values for the publisher listing revision attachments. The attachment type informs the type of attachment for the listing revision.


        :param attachment_type: The attachment_type of this ListingRevisionAttachment.
        :type: str
        """
        allowed_values = ["RELATED_DOCUMENT", "SCREENSHOT", "VIDEO", "REVIEW_SUPPORT_DOCUMENT", "CUSTOMER_SUCCESS", "SUPPORTED_SERVICES"]
        if not value_allowed_none_or_none_sentinel(attachment_type, allowed_values):
            attachment_type = 'UNKNOWN_ENUM_VALUE'
        self._attachment_type = attachment_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ListingRevisionAttachment.
        The current state of the attachment.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ListingRevisionAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ListingRevisionAttachment.
        The current state of the attachment.


        :param lifecycle_state: The lifecycle_state of this ListingRevisionAttachment.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ListingRevisionAttachment.
        The time the attachment was created. An RFC3339 formatted datetime string.


        :return: The time_created of this ListingRevisionAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ListingRevisionAttachment.
        The time the attachment was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ListingRevisionAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ListingRevisionAttachment.
        The time the attachment was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this ListingRevisionAttachment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ListingRevisionAttachment.
        The time the attachment was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ListingRevisionAttachment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ListingRevisionAttachment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ListingRevisionAttachment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ListingRevisionAttachment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ListingRevisionAttachment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ListingRevisionAttachment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ListingRevisionAttachment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ListingRevisionAttachment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ListingRevisionAttachment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ListingRevisionAttachment.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ListingRevisionAttachment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ListingRevisionAttachment.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ListingRevisionAttachment.
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
