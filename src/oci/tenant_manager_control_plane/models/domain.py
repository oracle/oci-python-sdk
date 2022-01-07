# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Domain(object):
    """
    The domain model that is associated with a tenancy.
    """

    #: A constant which can be used with the lifecycle_state property of a Domain.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Domain.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Domain.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "RELEASING"
    STATUS_RELEASING = "RELEASING"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "RELEASED"
    STATUS_RELEASED = "RELEASED"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "EXPIRING"
    STATUS_EXPIRING = "EXPIRING"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "REVOKING"
    STATUS_REVOKING = "REVOKING"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "REVOKED"
    STATUS_REVOKED = "REVOKED"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a Domain.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Domain object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Domain.
        :type id: str

        :param domain_name:
            The value to assign to the domain_name property of this Domain.
        :type domain_name: str

        :param owner_id:
            The value to assign to the owner_id property of this Domain.
        :type owner_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Domain.
            Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param status:
            The value to assign to the status property of this Domain.
            Allowed values for this property are: "PENDING", "RELEASING", "RELEASED", "EXPIRING", "REVOKING", "REVOKED", "ACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param txt_record:
            The value to assign to the txt_record property of this Domain.
        :type txt_record: str

        :param time_created:
            The value to assign to the time_created property of this Domain.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Domain.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Domain.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Domain.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Domain.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'domain_name': 'str',
            'owner_id': 'str',
            'lifecycle_state': 'str',
            'status': 'str',
            'txt_record': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'domain_name': 'domainName',
            'owner_id': 'ownerId',
            'lifecycle_state': 'lifecycleState',
            'status': 'status',
            'txt_record': 'txtRecord',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._domain_name = None
        self._owner_id = None
        self._lifecycle_state = None
        self._status = None
        self._txt_record = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Domain.
        The OCID of the domain.


        :return: The id of this Domain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Domain.
        The OCID of the domain.


        :param id: The id of this Domain.
        :type: str
        """
        self._id = id

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this Domain.
        The domain name.


        :return: The domain_name of this Domain.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this Domain.
        The domain name.


        :param domain_name: The domain_name of this Domain.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def owner_id(self):
        """
        **[Required]** Gets the owner_id of this Domain.
        The OCID of the tenancy that has started the registration process for this domain.


        :return: The owner_id of this Domain.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this Domain.
        The OCID of the tenancy that has started the registration process for this domain.


        :param owner_id: The owner_id of this Domain.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Domain.
        Lifecycle state of the domain.

        Allowed values for this property are: "ACTIVE", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Domain.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Domain.
        Lifecycle state of the domain.


        :param lifecycle_state: The lifecycle_state of this Domain.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Domain.
        Status of the domain.

        Allowed values for this property are: "PENDING", "RELEASING", "RELEASED", "EXPIRING", "REVOKING", "REVOKED", "ACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Domain.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Domain.
        Status of the domain.


        :param status: The status of this Domain.
        :type: str
        """
        allowed_values = ["PENDING", "RELEASING", "RELEASED", "EXPIRING", "REVOKING", "REVOKED", "ACTIVE", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def txt_record(self):
        """
        **[Required]** Gets the txt_record of this Domain.
        The code that the owner of the domain will need to add as a TXT record to their domain.


        :return: The txt_record of this Domain.
        :rtype: str
        """
        return self._txt_record

    @txt_record.setter
    def txt_record(self, txt_record):
        """
        Sets the txt_record of this Domain.
        The code that the owner of the domain will need to add as a TXT record to their domain.


        :param txt_record: The txt_record of this Domain.
        :type: str
        """
        self._txt_record = txt_record

    @property
    def time_created(self):
        """
        Gets the time_created of this Domain.
        Date-time when this domain was created. An RFC 3339-formatted date and time string.


        :return: The time_created of this Domain.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Domain.
        Date-time when this domain was created. An RFC 3339-formatted date and time string.


        :param time_created: The time_created of this Domain.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Domain.
        Date-time when this domain was last updated. An RFC 3339-formatted date and time string.


        :return: The time_updated of this Domain.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Domain.
        Date-time when this domain was last updated. An RFC 3339-formatted date and time string.


        :param time_updated: The time_updated of this Domain.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Domain.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Domain.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Domain.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Domain.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Domain.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Domain.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Domain.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Domain.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Domain.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Domain.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Domain.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Domain.
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
