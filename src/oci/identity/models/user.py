# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class User(object):
    """
    An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure
    resources. Users might need to launch instances, manage remote disks, work with your cloud network, etc. Users
    have one or more IAM Service credentials (:class:`ApiKey`,
    :class:`UIPassword`, :class:`SwiftPassword` and
    :class:`AuthToken`).
    For more information, see `User Credentials`__). End users of your
    application are not typically IAM Service users, but for tenancies that have identity domains, they might be.
    For conceptual information about users and other IAM Service components, see `Overview of IAM`__.

    These users are created directly within the Oracle Cloud Infrastructure system, via the IAM service.
    They are different from *federated users*, who authenticate themselves to the Oracle Cloud Infrastructure
    Console via an identity provider. For more information, see
    `Identity Providers and Federation`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access,
    see `Get Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values
    using the API.

    __ https://docs.cloud.oracle.com/Content/Identity/usercred/usercredentials.htm
    __ https://docs.cloud.oracle.com/Content/Identity/getstarted/identity-domains.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/federation.htm
    __ https://docs.cloud.oracle.com/Content/Identity/policiesgs/get-started-with-policies.htm
    """

    #: A constant which can be used with the lifecycle_state property of a User.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a User.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a User.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a User.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a User.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new User object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this User.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this User.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this User.
        :type name: str

        :param description:
            The value to assign to the description property of this User.
        :type description: str

        :param email:
            The value to assign to the email property of this User.
        :type email: str

        :param email_verified:
            The value to assign to the email_verified property of this User.
        :type email_verified: bool

        :param db_user_name:
            The value to assign to the db_user_name property of this User.
        :type db_user_name: str

        :param identity_provider_id:
            The value to assign to the identity_provider_id property of this User.
        :type identity_provider_id: str

        :param external_identifier:
            The value to assign to the external_identifier property of this User.
        :type external_identifier: str

        :param time_created:
            The value to assign to the time_created property of this User.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this User.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this User.
        :type inactive_status: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this User.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this User.
        :type defined_tags: dict(str, dict(str, object))

        :param capabilities:
            The value to assign to the capabilities property of this User.
        :type capabilities: oci.identity.models.UserCapabilities

        :param is_mfa_activated:
            The value to assign to the is_mfa_activated property of this User.
        :type is_mfa_activated: bool

        :param last_successful_login_time:
            The value to assign to the last_successful_login_time property of this User.
        :type last_successful_login_time: datetime

        :param previous_successful_login_time:
            The value to assign to the previous_successful_login_time property of this User.
        :type previous_successful_login_time: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'email': 'str',
            'email_verified': 'bool',
            'db_user_name': 'str',
            'identity_provider_id': 'str',
            'external_identifier': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'capabilities': 'UserCapabilities',
            'is_mfa_activated': 'bool',
            'last_successful_login_time': 'datetime',
            'previous_successful_login_time': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'email': 'email',
            'email_verified': 'emailVerified',
            'db_user_name': 'dbUserName',
            'identity_provider_id': 'identityProviderId',
            'external_identifier': 'externalIdentifier',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'capabilities': 'capabilities',
            'is_mfa_activated': 'isMfaActivated',
            'last_successful_login_time': 'lastSuccessfulLoginTime',
            'previous_successful_login_time': 'previousSuccessfulLoginTime'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._email = None
        self._email_verified = None
        self._db_user_name = None
        self._identity_provider_id = None
        self._external_identifier = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._freeform_tags = None
        self._defined_tags = None
        self._capabilities = None
        self._is_mfa_activated = None
        self._last_successful_login_time = None
        self._previous_successful_login_time = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this User.
        The OCID of the user.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        The OCID of the user.


        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this User.
        The OCID of the tenancy containing the user.


        :return: The compartment_id of this User.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this User.
        The OCID of the tenancy containing the user.


        :param compartment_id: The compartment_id of this User.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this User.
        The name you assign to the user during creation. This is the user's login for the Console.
        The name must be unique across all users in the tenancy and cannot be changed.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.
        The name you assign to the user during creation. This is the user's login for the Console.
        The name must be unique across all users in the tenancy and cannot be changed.


        :param name: The name of this User.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this User.
        The description you assign to the user. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this User.
        The description you assign to the user. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :param description: The description of this User.
        :type: str
        """
        self._description = description

    @property
    def email(self):
        """
        Gets the email of this User.
        The email address you assign to the user.
        The email address must be unique across all users in the tenancy.

        (For tenancies that support identity domains) The email address is required unless the requirement is disabled at the tenancy level.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        The email address you assign to the user.
        The email address must be unique across all users in the tenancy.

        (For tenancies that support identity domains) The email address is required unless the requirement is disabled at the tenancy level.


        :param email: The email of this User.
        :type: str
        """
        self._email = email

    @property
    def email_verified(self):
        """
        Gets the email_verified of this User.
        Whether the email address has been validated.


        :return: The email_verified of this User.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """
        Sets the email_verified of this User.
        Whether the email address has been validated.


        :param email_verified: The email_verified of this User.
        :type: bool
        """
        self._email_verified = email_verified

    @property
    def db_user_name(self):
        """
        Gets the db_user_name of this User.
        DB username of the DB credential. Has to be unique across the tenancy.


        :return: The db_user_name of this User.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """
        Sets the db_user_name of this User.
        DB username of the DB credential. Has to be unique across the tenancy.


        :param db_user_name: The db_user_name of this User.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def identity_provider_id(self):
        """
        Gets the identity_provider_id of this User.
        The OCID of the `IdentityProvider` this user belongs to.


        :return: The identity_provider_id of this User.
        :rtype: str
        """
        return self._identity_provider_id

    @identity_provider_id.setter
    def identity_provider_id(self, identity_provider_id):
        """
        Sets the identity_provider_id of this User.
        The OCID of the `IdentityProvider` this user belongs to.


        :param identity_provider_id: The identity_provider_id of this User.
        :type: str
        """
        self._identity_provider_id = identity_provider_id

    @property
    def external_identifier(self):
        """
        Gets the external_identifier of this User.
        Identifier of the user in the identity provider


        :return: The external_identifier of this User.
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """
        Sets the external_identifier of this User.
        Identifier of the user in the identity provider


        :param external_identifier: The external_identifier of this User.
        :type: str
        """
        self._external_identifier = external_identifier

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this User.
        Date and time the user was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this User.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this User.
        Date and time the user was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this User.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this User.
        The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to
        ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this User.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this User.
        The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to
        ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this User.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this User.
        Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user
        is inactive:

        - bit 0: SUSPENDED (reserved for future use)
        - bit 1: DISABLED (reserved for future use)
        - bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)


        :return: The inactive_status of this User.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this User.
        Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user
        is inactive:

        - bit 0: SUSPENDED (reserved for future use)
        - bit 1: DISABLED (reserved for future use)
        - bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)


        :param inactive_status: The inactive_status of this User.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this User.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this User.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this User.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this User.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this User.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this User.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this User.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this User.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def capabilities(self):
        """
        Gets the capabilities of this User.

        :return: The capabilities of this User.
        :rtype: oci.identity.models.UserCapabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this User.

        :param capabilities: The capabilities of this User.
        :type: oci.identity.models.UserCapabilities
        """
        self._capabilities = capabilities

    @property
    def is_mfa_activated(self):
        """
        **[Required]** Gets the is_mfa_activated of this User.
        Flag indicates if MFA has been activated for the user.


        :return: The is_mfa_activated of this User.
        :rtype: bool
        """
        return self._is_mfa_activated

    @is_mfa_activated.setter
    def is_mfa_activated(self, is_mfa_activated):
        """
        Sets the is_mfa_activated of this User.
        Flag indicates if MFA has been activated for the user.


        :param is_mfa_activated: The is_mfa_activated of this User.
        :type: bool
        """
        self._is_mfa_activated = is_mfa_activated

    @property
    def last_successful_login_time(self):
        """
        Gets the last_successful_login_time of this User.
        The date and time of when the user most recently logged in the
        format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
        If there is no login history, this field is null.

        For illustrative purposes, suppose we have a user who has logged in
        at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
        They then login again on July 2nd, 2020 at 1500 PST.

        Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.

        Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.


        :return: The last_successful_login_time of this User.
        :rtype: datetime
        """
        return self._last_successful_login_time

    @last_successful_login_time.setter
    def last_successful_login_time(self, last_successful_login_time):
        """
        Sets the last_successful_login_time of this User.
        The date and time of when the user most recently logged in the
        format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
        If there is no login history, this field is null.

        For illustrative purposes, suppose we have a user who has logged in
        at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
        They then login again on July 2nd, 2020 at 1500 PST.

        Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.

        Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.


        :param last_successful_login_time: The last_successful_login_time of this User.
        :type: datetime
        """
        self._last_successful_login_time = last_successful_login_time

    @property
    def previous_successful_login_time(self):
        """
        Gets the previous_successful_login_time of this User.
        The date and time of when the user most recently logged in the
        format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
        If there is no login history, this field is null.

        For illustrative purposes, suppose we have a user who has logged in
        at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
        They then login again on July 2nd, 2020 at 1500 PST.

        Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.

        Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.


        :return: The previous_successful_login_time of this User.
        :rtype: datetime
        """
        return self._previous_successful_login_time

    @previous_successful_login_time.setter
    def previous_successful_login_time(self, previous_successful_login_time):
        """
        Sets the previous_successful_login_time of this User.
        The date and time of when the user most recently logged in the
        format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
        If there is no login history, this field is null.

        For illustrative purposes, suppose we have a user who has logged in
        at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
        They then login again on July 2nd, 2020 at 1500 PST.

        Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.

        Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.


        :param previous_successful_login_time: The previous_successful_login_time of this User.
        :type: datetime
        """
        self._previous_successful_login_time = previous_successful_login_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
