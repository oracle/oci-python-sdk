# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaInstanceAttachment(object):
    """
    Description of an ODA instance attachment.
    """

    #: A constant which can be used with the attachment_type property of a OdaInstanceAttachment.
    #: This constant has a value of "FUSION"
    ATTACHMENT_TYPE_FUSION = "FUSION"

    #: A constant which can be used with the lifecycle_state property of a OdaInstanceAttachment.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstanceAttachment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaInstanceAttachment.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a OdaInstanceAttachment.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaInstanceAttachment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OdaInstanceAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OdaInstanceAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this OdaInstanceAttachment.
        :type instance_id: str

        :param attach_to_id:
            The value to assign to the attach_to_id property of this OdaInstanceAttachment.
        :type attach_to_id: str

        :param attachment_type:
            The value to assign to the attachment_type property of this OdaInstanceAttachment.
            Allowed values for this property are: "FUSION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attachment_type: str

        :param attachment_metadata:
            The value to assign to the attachment_metadata property of this OdaInstanceAttachment.
        :type attachment_metadata: str

        :param restricted_operations:
            The value to assign to the restricted_operations property of this OdaInstanceAttachment.
        :type restricted_operations: list[str]

        :param owner:
            The value to assign to the owner property of this OdaInstanceAttachment.
        :type owner: oci.oda.models.OdaInstanceOwner

        :param time_created:
            The value to assign to the time_created property of this OdaInstanceAttachment.
        :type time_created: datetime

        :param time_last_update:
            The value to assign to the time_last_update property of this OdaInstanceAttachment.
        :type time_last_update: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OdaInstanceAttachment.
            Allowed values for this property are: "ATTACHING", "ACTIVE", "DETACHING", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OdaInstanceAttachment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OdaInstanceAttachment.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'instance_id': 'str',
            'attach_to_id': 'str',
            'attachment_type': 'str',
            'attachment_metadata': 'str',
            'restricted_operations': 'list[str]',
            'owner': 'OdaInstanceOwner',
            'time_created': 'datetime',
            'time_last_update': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_id': 'instanceId',
            'attach_to_id': 'attachToId',
            'attachment_type': 'attachmentType',
            'attachment_metadata': 'attachmentMetadata',
            'restricted_operations': 'restrictedOperations',
            'owner': 'owner',
            'time_created': 'timeCreated',
            'time_last_update': 'timeLastUpdate',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._instance_id = None
        self._attach_to_id = None
        self._attachment_type = None
        self._attachment_metadata = None
        self._restricted_operations = None
        self._owner = None
        self._time_created = None
        self._time_last_update = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OdaInstanceAttachment.
        Unique immutable identifier that was assigned when the ODA instance attachment was created.


        :return: The id of this OdaInstanceAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OdaInstanceAttachment.
        Unique immutable identifier that was assigned when the ODA instance attachment was created.


        :param id: The id of this OdaInstanceAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this OdaInstanceAttachment.
        The OCID of the ODA instance to which the attachment applies.


        :return: The instance_id of this OdaInstanceAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this OdaInstanceAttachment.
        The OCID of the ODA instance to which the attachment applies.


        :param instance_id: The instance_id of this OdaInstanceAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def attach_to_id(self):
        """
        **[Required]** Gets the attach_to_id of this OdaInstanceAttachment.
        The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which the ODA instance is or is being attached.


        :return: The attach_to_id of this OdaInstanceAttachment.
        :rtype: str
        """
        return self._attach_to_id

    @attach_to_id.setter
    def attach_to_id(self, attach_to_id):
        """
        Sets the attach_to_id of this OdaInstanceAttachment.
        The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which the ODA instance is or is being attached.


        :param attach_to_id: The attach_to_id of this OdaInstanceAttachment.
        :type: str
        """
        self._attach_to_id = attach_to_id

    @property
    def attachment_type(self):
        """
        **[Required]** Gets the attachment_type of this OdaInstanceAttachment.
        The type of attachment defined as an enum.

        Allowed values for this property are: "FUSION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attachment_type of this OdaInstanceAttachment.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """
        Sets the attachment_type of this OdaInstanceAttachment.
        The type of attachment defined as an enum.


        :param attachment_type: The attachment_type of this OdaInstanceAttachment.
        :type: str
        """
        allowed_values = ["FUSION"]
        if not value_allowed_none_or_none_sentinel(attachment_type, allowed_values):
            attachment_type = 'UNKNOWN_ENUM_VALUE'
        self._attachment_type = attachment_type

    @property
    def attachment_metadata(self):
        """
        Gets the attachment_metadata of this OdaInstanceAttachment.
        Attachment-specific metadata, defined by the target service.


        :return: The attachment_metadata of this OdaInstanceAttachment.
        :rtype: str
        """
        return self._attachment_metadata

    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata):
        """
        Sets the attachment_metadata of this OdaInstanceAttachment.
        Attachment-specific metadata, defined by the target service.


        :param attachment_metadata: The attachment_metadata of this OdaInstanceAttachment.
        :type: str
        """
        self._attachment_metadata = attachment_metadata

    @property
    def restricted_operations(self):
        """
        Gets the restricted_operations of this OdaInstanceAttachment.
        List of operation names that are restricted while this ODA instance is attached.


        :return: The restricted_operations of this OdaInstanceAttachment.
        :rtype: list[str]
        """
        return self._restricted_operations

    @restricted_operations.setter
    def restricted_operations(self, restricted_operations):
        """
        Sets the restricted_operations of this OdaInstanceAttachment.
        List of operation names that are restricted while this ODA instance is attached.


        :param restricted_operations: The restricted_operations of this OdaInstanceAttachment.
        :type: list[str]
        """
        self._restricted_operations = restricted_operations

    @property
    def owner(self):
        """
        Gets the owner of this OdaInstanceAttachment.

        :return: The owner of this OdaInstanceAttachment.
        :rtype: oci.oda.models.OdaInstanceOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this OdaInstanceAttachment.

        :param owner: The owner of this OdaInstanceAttachment.
        :type: oci.oda.models.OdaInstanceOwner
        """
        self._owner = owner

    @property
    def time_created(self):
        """
        Gets the time_created of this OdaInstanceAttachment.
        The time the attachment was created. An RFC3339 formatted datetime string


        :return: The time_created of this OdaInstanceAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OdaInstanceAttachment.
        The time the attachment was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OdaInstanceAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_update(self):
        """
        Gets the time_last_update of this OdaInstanceAttachment.
        The time the attachment was last modified. An RFC3339 formatted datetime string


        :return: The time_last_update of this OdaInstanceAttachment.
        :rtype: datetime
        """
        return self._time_last_update

    @time_last_update.setter
    def time_last_update(self, time_last_update):
        """
        Sets the time_last_update of this OdaInstanceAttachment.
        The time the attachment was last modified. An RFC3339 formatted datetime string


        :param time_last_update: The time_last_update of this OdaInstanceAttachment.
        :type: datetime
        """
        self._time_last_update = time_last_update

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OdaInstanceAttachment.
        The current state of the attachment.

        Allowed values for this property are: "ATTACHING", "ACTIVE", "DETACHING", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OdaInstanceAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OdaInstanceAttachment.
        The current state of the attachment.


        :param lifecycle_state: The lifecycle_state of this OdaInstanceAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ACTIVE", "DETACHING", "INACTIVE", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OdaInstanceAttachment.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OdaInstanceAttachment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OdaInstanceAttachment.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OdaInstanceAttachment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OdaInstanceAttachment.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OdaInstanceAttachment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OdaInstanceAttachment.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OdaInstanceAttachment.
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
