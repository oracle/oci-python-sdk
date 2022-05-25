# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class User(object):
    """
    The summary of a specific user resource.
    """

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "OPEN"
    STATUS_OPEN = "OPEN"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED"
    STATUS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_GRACE"
    STATUS_EXPIRED_GRACE = "EXPIRED_GRACE"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "LOCKED"
    STATUS_LOCKED = "LOCKED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "LOCKED_TIMED"
    STATUS_LOCKED_TIMED = "LOCKED_TIMED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_AND_LOCKED"
    STATUS_EXPIRED_AND_LOCKED = "EXPIRED_AND_LOCKED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_GRACE_AND_LOCKED"
    STATUS_EXPIRED_GRACE_AND_LOCKED = "EXPIRED_GRACE_AND_LOCKED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_AND_LOCKED_TIMED"
    STATUS_EXPIRED_AND_LOCKED_TIMED = "EXPIRED_AND_LOCKED_TIMED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_GRACE_AND_LOCKED_TIMED"
    STATUS_EXPIRED_GRACE_AND_LOCKED_TIMED = "EXPIRED_GRACE_AND_LOCKED_TIMED"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "OPEN_AND_IN_ROLLOVER"
    STATUS_OPEN_AND_IN_ROLLOVER = "OPEN_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_AND_IN_ROLLOVER"
    STATUS_EXPIRED_AND_IN_ROLLOVER = "EXPIRED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "LOCKED_AND_IN_ROLLOVER"
    STATUS_LOCKED_AND_IN_ROLLOVER = "LOCKED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER"
    STATUS_EXPIRED_AND_LOCKED_AND_IN_ROLLOVER = "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "LOCKED_TIMED_AND_IN_ROLLOVER"
    STATUS_LOCKED_TIMED_AND_IN_ROLLOVER = "LOCKED_TIMED_AND_IN_ROLLOVER"

    #: A constant which can be used with the status property of a User.
    #: This constant has a value of "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL"
    STATUS_EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL = "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL"

    #: A constant which can be used with the editions_enabled property of a User.
    #: This constant has a value of "YES"
    EDITIONS_ENABLED_YES = "YES"

    #: A constant which can be used with the editions_enabled property of a User.
    #: This constant has a value of "NO"
    EDITIONS_ENABLED_NO = "NO"

    #: A constant which can be used with the authentication property of a User.
    #: This constant has a value of "NONE"
    AUTHENTICATION_NONE = "NONE"

    #: A constant which can be used with the authentication property of a User.
    #: This constant has a value of "EXTERNAL"
    AUTHENTICATION_EXTERNAL = "EXTERNAL"

    #: A constant which can be used with the authentication property of a User.
    #: This constant has a value of "GLOBAL"
    AUTHENTICATION_GLOBAL = "GLOBAL"

    #: A constant which can be used with the authentication property of a User.
    #: This constant has a value of "PASSWORD"
    AUTHENTICATION_PASSWORD = "PASSWORD"

    #: A constant which can be used with the proxy_connect property of a User.
    #: This constant has a value of "YES"
    PROXY_CONNECT_YES = "YES"

    #: A constant which can be used with the proxy_connect property of a User.
    #: This constant has a value of "NO"
    PROXY_CONNECT_NO = "NO"

    #: A constant which can be used with the common property of a User.
    #: This constant has a value of "YES"
    COMMON_YES = "YES"

    #: A constant which can be used with the common property of a User.
    #: This constant has a value of "NO"
    COMMON_NO = "NO"

    #: A constant which can be used with the oracle_maintained property of a User.
    #: This constant has a value of "YES"
    ORACLE_MAINTAINED_YES = "YES"

    #: A constant which can be used with the oracle_maintained property of a User.
    #: This constant has a value of "NO"
    ORACLE_MAINTAINED_NO = "NO"

    #: A constant which can be used with the inherited property of a User.
    #: This constant has a value of "YES"
    INHERITED_YES = "YES"

    #: A constant which can be used with the inherited property of a User.
    #: This constant has a value of "NO"
    INHERITED_NO = "NO"

    #: A constant which can be used with the implicit property of a User.
    #: This constant has a value of "YES"
    IMPLICIT_YES = "YES"

    #: A constant which can be used with the implicit property of a User.
    #: This constant has a value of "NO"
    IMPLICIT_NO = "NO"

    #: A constant which can be used with the all_shared property of a User.
    #: This constant has a value of "YES"
    ALL_SHARED_YES = "YES"

    #: A constant which can be used with the all_shared property of a User.
    #: This constant has a value of "NO"
    ALL_SHARED_NO = "NO"

    #: A constant which can be used with the external_shared property of a User.
    #: This constant has a value of "YES"
    EXTERNAL_SHARED_YES = "YES"

    #: A constant which can be used with the external_shared property of a User.
    #: This constant has a value of "NO"
    EXTERNAL_SHARED_NO = "NO"

    def __init__(self, **kwargs):
        """
        Initializes a new User object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this User.
        :type name: str

        :param status:
            The value to assign to the status property of this User.
            Allowed values for this property are: "OPEN", "EXPIRED", "EXPIRED_GRACE", "LOCKED", "LOCKED_TIMED", "EXPIRED_AND_LOCKED", "EXPIRED_GRACE_AND_LOCKED", "EXPIRED_AND_LOCKED_TIMED", "EXPIRED_GRACE_AND_LOCKED_TIMED", "OPEN_AND_IN_ROLLOVER", "EXPIRED_AND_IN_ROLLOVER", "LOCKED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER", "LOCKED_TIMED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_locked:
            The value to assign to the time_locked property of this User.
        :type time_locked: datetime

        :param time_expiring:
            The value to assign to the time_expiring property of this User.
        :type time_expiring: datetime

        :param default_tablespace:
            The value to assign to the default_tablespace property of this User.
        :type default_tablespace: str

        :param temp_tablespace:
            The value to assign to the temp_tablespace property of this User.
        :type temp_tablespace: str

        :param local_temp_tablespace:
            The value to assign to the local_temp_tablespace property of this User.
        :type local_temp_tablespace: str

        :param time_created:
            The value to assign to the time_created property of this User.
        :type time_created: datetime

        :param profile:
            The value to assign to the profile property of this User.
        :type profile: str

        :param consumer_group:
            The value to assign to the consumer_group property of this User.
        :type consumer_group: str

        :param external_name:
            The value to assign to the external_name property of this User.
        :type external_name: str

        :param password_versions:
            The value to assign to the password_versions property of this User.
        :type password_versions: str

        :param editions_enabled:
            The value to assign to the editions_enabled property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type editions_enabled: str

        :param authentication:
            The value to assign to the authentication property of this User.
            Allowed values for this property are: "NONE", "EXTERNAL", "GLOBAL", "PASSWORD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type authentication: str

        :param proxy_connect:
            The value to assign to the proxy_connect property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type proxy_connect: str

        :param common:
            The value to assign to the common property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type common: str

        :param time_last_login:
            The value to assign to the time_last_login property of this User.
        :type time_last_login: datetime

        :param oracle_maintained:
            The value to assign to the oracle_maintained property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type oracle_maintained: str

        :param inherited:
            The value to assign to the inherited property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type inherited: str

        :param default_collation:
            The value to assign to the default_collation property of this User.
        :type default_collation: str

        :param implicit:
            The value to assign to the implicit property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type implicit: str

        :param all_shared:
            The value to assign to the all_shared property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type all_shared: str

        :param external_shared:
            The value to assign to the external_shared property of this User.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type external_shared: str

        :param time_password_changed:
            The value to assign to the time_password_changed property of this User.
        :type time_password_changed: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'status': 'str',
            'time_locked': 'datetime',
            'time_expiring': 'datetime',
            'default_tablespace': 'str',
            'temp_tablespace': 'str',
            'local_temp_tablespace': 'str',
            'time_created': 'datetime',
            'profile': 'str',
            'consumer_group': 'str',
            'external_name': 'str',
            'password_versions': 'str',
            'editions_enabled': 'str',
            'authentication': 'str',
            'proxy_connect': 'str',
            'common': 'str',
            'time_last_login': 'datetime',
            'oracle_maintained': 'str',
            'inherited': 'str',
            'default_collation': 'str',
            'implicit': 'str',
            'all_shared': 'str',
            'external_shared': 'str',
            'time_password_changed': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'status': 'status',
            'time_locked': 'timeLocked',
            'time_expiring': 'timeExpiring',
            'default_tablespace': 'defaultTablespace',
            'temp_tablespace': 'tempTablespace',
            'local_temp_tablespace': 'localTempTablespace',
            'time_created': 'timeCreated',
            'profile': 'profile',
            'consumer_group': 'consumerGroup',
            'external_name': 'externalName',
            'password_versions': 'passwordVersions',
            'editions_enabled': 'editionsEnabled',
            'authentication': 'authentication',
            'proxy_connect': 'proxyConnect',
            'common': 'common',
            'time_last_login': 'timeLastLogin',
            'oracle_maintained': 'oracleMaintained',
            'inherited': 'inherited',
            'default_collation': 'defaultCollation',
            'implicit': 'implicit',
            'all_shared': 'allShared',
            'external_shared': 'externalShared',
            'time_password_changed': 'timePasswordChanged'
        }

        self._name = None
        self._status = None
        self._time_locked = None
        self._time_expiring = None
        self._default_tablespace = None
        self._temp_tablespace = None
        self._local_temp_tablespace = None
        self._time_created = None
        self._profile = None
        self._consumer_group = None
        self._external_name = None
        self._password_versions = None
        self._editions_enabled = None
        self._authentication = None
        self._proxy_connect = None
        self._common = None
        self._time_last_login = None
        self._oracle_maintained = None
        self._inherited = None
        self._default_collation = None
        self._implicit = None
        self._all_shared = None
        self._external_shared = None
        self._time_password_changed = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this User.
        The name of the User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.
        The name of the User.


        :param name: The name of this User.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this User.
        The status of the user account.

        Allowed values for this property are: "OPEN", "EXPIRED", "EXPIRED_GRACE", "LOCKED", "LOCKED_TIMED", "EXPIRED_AND_LOCKED", "EXPIRED_GRACE_AND_LOCKED", "EXPIRED_AND_LOCKED_TIMED", "EXPIRED_GRACE_AND_LOCKED_TIMED", "OPEN_AND_IN_ROLLOVER", "EXPIRED_AND_IN_ROLLOVER", "LOCKED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER", "LOCKED_TIMED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this User.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this User.
        The status of the user account.


        :param status: The status of this User.
        :type: str
        """
        allowed_values = ["OPEN", "EXPIRED", "EXPIRED_GRACE", "LOCKED", "LOCKED_TIMED", "EXPIRED_AND_LOCKED", "EXPIRED_GRACE_AND_LOCKED", "EXPIRED_AND_LOCKED_TIMED", "EXPIRED_GRACE_AND_LOCKED_TIMED", "OPEN_AND_IN_ROLLOVER", "EXPIRED_AND_IN_ROLLOVER", "LOCKED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_AND_IN_ROLLOVER", "LOCKED_TIMED_AND_IN_ROLLOVER", "EXPIRED_AND_LOCKED_TIMED_AND_IN_ROL"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_locked(self):
        """
        Gets the time_locked of this User.
        The date the account was locked, if the status of the account is LOCKED.


        :return: The time_locked of this User.
        :rtype: datetime
        """
        return self._time_locked

    @time_locked.setter
    def time_locked(self, time_locked):
        """
        Sets the time_locked of this User.
        The date the account was locked, if the status of the account is LOCKED.


        :param time_locked: The time_locked of this User.
        :type: datetime
        """
        self._time_locked = time_locked

    @property
    def time_expiring(self):
        """
        Gets the time_expiring of this User.
        The date and time of the expiration of the user account.


        :return: The time_expiring of this User.
        :rtype: datetime
        """
        return self._time_expiring

    @time_expiring.setter
    def time_expiring(self, time_expiring):
        """
        Sets the time_expiring of this User.
        The date and time of the expiration of the user account.


        :param time_expiring: The time_expiring of this User.
        :type: datetime
        """
        self._time_expiring = time_expiring

    @property
    def default_tablespace(self):
        """
        **[Required]** Gets the default_tablespace of this User.
        The default tablespace for data.


        :return: The default_tablespace of this User.
        :rtype: str
        """
        return self._default_tablespace

    @default_tablespace.setter
    def default_tablespace(self, default_tablespace):
        """
        Sets the default_tablespace of this User.
        The default tablespace for data.


        :param default_tablespace: The default_tablespace of this User.
        :type: str
        """
        self._default_tablespace = default_tablespace

    @property
    def temp_tablespace(self):
        """
        **[Required]** Gets the temp_tablespace of this User.
        The name of the default tablespace for temporary tables or the name of a tablespace group.


        :return: The temp_tablespace of this User.
        :rtype: str
        """
        return self._temp_tablespace

    @temp_tablespace.setter
    def temp_tablespace(self, temp_tablespace):
        """
        Sets the temp_tablespace of this User.
        The name of the default tablespace for temporary tables or the name of a tablespace group.


        :param temp_tablespace: The temp_tablespace of this User.
        :type: str
        """
        self._temp_tablespace = temp_tablespace

    @property
    def local_temp_tablespace(self):
        """
        Gets the local_temp_tablespace of this User.
        The default local temporary tablespace for the user.


        :return: The local_temp_tablespace of this User.
        :rtype: str
        """
        return self._local_temp_tablespace

    @local_temp_tablespace.setter
    def local_temp_tablespace(self, local_temp_tablespace):
        """
        Sets the local_temp_tablespace of this User.
        The default local temporary tablespace for the user.


        :param local_temp_tablespace: The local_temp_tablespace of this User.
        :type: str
        """
        self._local_temp_tablespace = local_temp_tablespace

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this User.
        The date and time the user was created.


        :return: The time_created of this User.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this User.
        The date and time the user was created.


        :param time_created: The time_created of this User.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def profile(self):
        """
        **[Required]** Gets the profile of this User.
        The profile name of the user.


        :return: The profile of this User.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this User.
        The profile name of the user.


        :param profile: The profile of this User.
        :type: str
        """
        self._profile = profile

    @property
    def consumer_group(self):
        """
        Gets the consumer_group of this User.
        The initial resource consumer group for the User.


        :return: The consumer_group of this User.
        :rtype: str
        """
        return self._consumer_group

    @consumer_group.setter
    def consumer_group(self, consumer_group):
        """
        Sets the consumer_group of this User.
        The initial resource consumer group for the User.


        :param consumer_group: The consumer_group of this User.
        :type: str
        """
        self._consumer_group = consumer_group

    @property
    def external_name(self):
        """
        Gets the external_name of this User.
        The external name of the user.


        :return: The external_name of this User.
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """
        Sets the external_name of this User.
        The external name of the user.


        :param external_name: The external_name of this User.
        :type: str
        """
        self._external_name = external_name

    @property
    def password_versions(self):
        """
        Gets the password_versions of this User.
        The list of existing versions of the password hashes (also known as \"verifiers\") for the account.


        :return: The password_versions of this User.
        :rtype: str
        """
        return self._password_versions

    @password_versions.setter
    def password_versions(self, password_versions):
        """
        Sets the password_versions of this User.
        The list of existing versions of the password hashes (also known as \"verifiers\") for the account.


        :param password_versions: The password_versions of this User.
        :type: str
        """
        self._password_versions = password_versions

    @property
    def editions_enabled(self):
        """
        Gets the editions_enabled of this User.
        Indicates whether editions have been enabled for the corresponding user (Y) or not (N).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The editions_enabled of this User.
        :rtype: str
        """
        return self._editions_enabled

    @editions_enabled.setter
    def editions_enabled(self, editions_enabled):
        """
        Sets the editions_enabled of this User.
        Indicates whether editions have been enabled for the corresponding user (Y) or not (N).


        :param editions_enabled: The editions_enabled of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(editions_enabled, allowed_values):
            editions_enabled = 'UNKNOWN_ENUM_VALUE'
        self._editions_enabled = editions_enabled

    @property
    def authentication(self):
        """
        Gets the authentication of this User.
        The authentication mechanism for the user.

        Allowed values for this property are: "NONE", "EXTERNAL", "GLOBAL", "PASSWORD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The authentication of this User.
        :rtype: str
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this User.
        The authentication mechanism for the user.


        :param authentication: The authentication of this User.
        :type: str
        """
        allowed_values = ["NONE", "EXTERNAL", "GLOBAL", "PASSWORD"]
        if not value_allowed_none_or_none_sentinel(authentication, allowed_values):
            authentication = 'UNKNOWN_ENUM_VALUE'
        self._authentication = authentication

    @property
    def proxy_connect(self):
        """
        Gets the proxy_connect of this User.
        Indicates whether a user can connect directly (N) or whether the account can only be proxied (Y) by users who have proxy privileges
        for this account (that is, by users who have been granted the \"connect through\" privilege for this account).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The proxy_connect of this User.
        :rtype: str
        """
        return self._proxy_connect

    @proxy_connect.setter
    def proxy_connect(self, proxy_connect):
        """
        Sets the proxy_connect of this User.
        Indicates whether a user can connect directly (N) or whether the account can only be proxied (Y) by users who have proxy privileges
        for this account (that is, by users who have been granted the \"connect through\" privilege for this account).


        :param proxy_connect: The proxy_connect of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(proxy_connect, allowed_values):
            proxy_connect = 'UNKNOWN_ENUM_VALUE'
        self._proxy_connect = proxy_connect

    @property
    def common(self):
        """
        Gets the common of this User.
        Indicates whether a given user is common(Y) or local(N).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The common of this User.
        :rtype: str
        """
        return self._common

    @common.setter
    def common(self, common):
        """
        Sets the common of this User.
        Indicates whether a given user is common(Y) or local(N).


        :param common: The common of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(common, allowed_values):
            common = 'UNKNOWN_ENUM_VALUE'
        self._common = common

    @property
    def time_last_login(self):
        """
        Gets the time_last_login of this User.
        The date and time of the last user login.
        This column is not populated when a user connects to the database with administrative privileges, that is, AS { SYSASM | SYSBACKUP | SYSDBA | SYSDG | SYSOPER | SYSRAC | SYSKM }.


        :return: The time_last_login of this User.
        :rtype: datetime
        """
        return self._time_last_login

    @time_last_login.setter
    def time_last_login(self, time_last_login):
        """
        Sets the time_last_login of this User.
        The date and time of the last user login.
        This column is not populated when a user connects to the database with administrative privileges, that is, AS { SYSASM | SYSBACKUP | SYSDBA | SYSDG | SYSOPER | SYSRAC | SYSKM }.


        :param time_last_login: The time_last_login of this User.
        :type: datetime
        """
        self._time_last_login = time_last_login

    @property
    def oracle_maintained(self):
        """
        Gets the oracle_maintained of this User.
        Indicates whether the user was created and is maintained by Oracle-supplied scripts (such as catalog.sql or catproc.sql).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The oracle_maintained of this User.
        :rtype: str
        """
        return self._oracle_maintained

    @oracle_maintained.setter
    def oracle_maintained(self, oracle_maintained):
        """
        Sets the oracle_maintained of this User.
        Indicates whether the user was created and is maintained by Oracle-supplied scripts (such as catalog.sql or catproc.sql).


        :param oracle_maintained: The oracle_maintained of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(oracle_maintained, allowed_values):
            oracle_maintained = 'UNKNOWN_ENUM_VALUE'
        self._oracle_maintained = oracle_maintained

    @property
    def inherited(self):
        """
        Gets the inherited of this User.
        Indicates whether the user definition is inherited from another container (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The inherited of this User.
        :rtype: str
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """
        Sets the inherited of this User.
        Indicates whether the user definition is inherited from another container (YES) or not (NO).


        :param inherited: The inherited of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(inherited, allowed_values):
            inherited = 'UNKNOWN_ENUM_VALUE'
        self._inherited = inherited

    @property
    def default_collation(self):
        """
        Gets the default_collation of this User.
        The default collation for the user schema.


        :return: The default_collation of this User.
        :rtype: str
        """
        return self._default_collation

    @default_collation.setter
    def default_collation(self, default_collation):
        """
        Sets the default_collation of this User.
        The default collation for the user schema.


        :param default_collation: The default_collation of this User.
        :type: str
        """
        self._default_collation = default_collation

    @property
    def implicit(self):
        """
        Gets the implicit of this User.
        Indicates whether the user is a common user created by an implicit application (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The implicit of this User.
        :rtype: str
        """
        return self._implicit

    @implicit.setter
    def implicit(self, implicit):
        """
        Sets the implicit of this User.
        Indicates whether the user is a common user created by an implicit application (YES) or not (NO).


        :param implicit: The implicit of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(implicit, allowed_values):
            implicit = 'UNKNOWN_ENUM_VALUE'
        self._implicit = implicit

    @property
    def all_shared(self):
        """
        Gets the all_shared of this User.
        In a sharded database, indicates whether the user is created with shard DDL enabled (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The all_shared of this User.
        :rtype: str
        """
        return self._all_shared

    @all_shared.setter
    def all_shared(self, all_shared):
        """
        Sets the all_shared of this User.
        In a sharded database, indicates whether the user is created with shard DDL enabled (YES) or not (NO).


        :param all_shared: The all_shared of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(all_shared, allowed_values):
            all_shared = 'UNKNOWN_ENUM_VALUE'
        self._all_shared = all_shared

    @property
    def external_shared(self):
        """
        Gets the external_shared of this User.
        In a federated sharded database, indicates whether the user is an external shard user (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The external_shared of this User.
        :rtype: str
        """
        return self._external_shared

    @external_shared.setter
    def external_shared(self, external_shared):
        """
        Sets the external_shared of this User.
        In a federated sharded database, indicates whether the user is an external shard user (YES) or not (NO).


        :param external_shared: The external_shared of this User.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(external_shared, allowed_values):
            external_shared = 'UNKNOWN_ENUM_VALUE'
        self._external_shared = external_shared

    @property
    def time_password_changed(self):
        """
        Gets the time_password_changed of this User.
        The date and time when the user password was last set.
        This column is populated only when the value of the AUTHENTICATION_TYPE column is PASSWORD. Otherwise, this column is null.


        :return: The time_password_changed of this User.
        :rtype: datetime
        """
        return self._time_password_changed

    @time_password_changed.setter
    def time_password_changed(self, time_password_changed):
        """
        Sets the time_password_changed of this User.
        The date and time when the user password was last set.
        This column is populated only when the value of the AUTHENTICATION_TYPE column is PASSWORD. Otherwise, this column is null.


        :param time_password_changed: The time_password_changed of this User.
        :type: datetime
        """
        self._time_password_changed = time_password_changed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
