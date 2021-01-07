# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileSystem(object):
    """
    An NFS file system. To allow access to a file system, add it
    to an export set and associate the export set with a mount
    target. The same file system can be in multiple export sets and
    associated with multiple mount targets.

    To use any of the API operations, you must be authorized in an
    IAM policy. If you're not authorized, talk to an
    administrator. If you're an administrator who needs to write
    policies to give users access, see `Getting Started with
    Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FileSystem.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new FileSystem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this FileSystem.
        :type availability_domain: str

        :param metered_bytes:
            The value to assign to the metered_bytes property of this FileSystem.
        :type metered_bytes: int

        :param compartment_id:
            The value to assign to the compartment_id property of this FileSystem.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this FileSystem.
        :type display_name: str

        :param id:
            The value to assign to the id property of this FileSystem.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FileSystem.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this FileSystem.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FileSystem.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FileSystem.
        :type defined_tags: dict(str, dict(str, object))

        :param kms_key_id:
            The value to assign to the kms_key_id property of this FileSystem.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'metered_bytes': 'int',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'metered_bytes': 'meteredBytes',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'kms_key_id': 'kmsKeyId'
        }

        self._availability_domain = None
        self._metered_bytes = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None
        self._kms_key_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this FileSystem.
        The availability domain the file system is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this FileSystem.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this FileSystem.
        The availability domain the file system is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this FileSystem.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def metered_bytes(self):
        """
        **[Required]** Gets the metered_bytes of this FileSystem.
        The number of bytes consumed by the file system, including
        any snapshots. This number reflects the metered size of the file
        system and is updated asynchronously with respect to
        updates to the file system.


        :return: The metered_bytes of this FileSystem.
        :rtype: int
        """
        return self._metered_bytes

    @metered_bytes.setter
    def metered_bytes(self, metered_bytes):
        """
        Sets the metered_bytes of this FileSystem.
        The number of bytes consumed by the file system, including
        any snapshots. This number reflects the metered size of the file
        system and is updated asynchronously with respect to
        updates to the file system.


        :param metered_bytes: The metered_bytes of this FileSystem.
        :type: int
        """
        self._metered_bytes = metered_bytes

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FileSystem.
        The OCID of the compartment that contains the file system.


        :return: The compartment_id of this FileSystem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FileSystem.
        The OCID of the compartment that contains the file system.


        :param compartment_id: The compartment_id of this FileSystem.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FileSystem.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :return: The display_name of this FileSystem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FileSystem.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My file system`


        :param display_name: The display_name of this FileSystem.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FileSystem.
        The OCID of the file system.


        :return: The id of this FileSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FileSystem.
        The OCID of the file system.


        :param id: The id of this FileSystem.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FileSystem.
        The current state of the file system.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FileSystem.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FileSystem.
        The current state of the file system.


        :param lifecycle_state: The lifecycle_state of this FileSystem.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FileSystem.
        The date and time the file system was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this FileSystem.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FileSystem.
        The date and time the file system was created, expressed in
        `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this FileSystem.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FileSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this FileSystem.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FileSystem.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this FileSystem.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FileSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this FileSystem.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FileSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this FileSystem.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this FileSystem.
        The OCID of the KMS key which is the master encryption key for the file system.


        :return: The kms_key_id of this FileSystem.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this FileSystem.
        The OCID of the KMS key which is the master encryption key for the file system.


        :param kms_key_id: The kms_key_id of this FileSystem.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
