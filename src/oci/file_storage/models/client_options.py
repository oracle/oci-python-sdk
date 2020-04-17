# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClientOptions(object):
    """
    NFS export options applied to a specified set of
    clients. Only governs access through the associated
    export. Access to the same file system through a different
    export (on the same or different mount target) will be governed
    by that export's export options.
    """

    #: A constant which can be used with the access property of a ClientOptions.
    #: This constant has a value of "READ_WRITE"
    ACCESS_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the access property of a ClientOptions.
    #: This constant has a value of "READ_ONLY"
    ACCESS_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the identity_squash property of a ClientOptions.
    #: This constant has a value of "NONE"
    IDENTITY_SQUASH_NONE = "NONE"

    #: A constant which can be used with the identity_squash property of a ClientOptions.
    #: This constant has a value of "ROOT"
    IDENTITY_SQUASH_ROOT = "ROOT"

    #: A constant which can be used with the identity_squash property of a ClientOptions.
    #: This constant has a value of "ALL"
    IDENTITY_SQUASH_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new ClientOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this ClientOptions.
        :type source: str

        :param require_privileged_source_port:
            The value to assign to the require_privileged_source_port property of this ClientOptions.
        :type require_privileged_source_port: bool

        :param access:
            The value to assign to the access property of this ClientOptions.
            Allowed values for this property are: "READ_WRITE", "READ_ONLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type access: str

        :param identity_squash:
            The value to assign to the identity_squash property of this ClientOptions.
            Allowed values for this property are: "NONE", "ROOT", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type identity_squash: str

        :param anonymous_uid:
            The value to assign to the anonymous_uid property of this ClientOptions.
        :type anonymous_uid: int

        :param anonymous_gid:
            The value to assign to the anonymous_gid property of this ClientOptions.
        :type anonymous_gid: int

        """
        self.swagger_types = {
            'source': 'str',
            'require_privileged_source_port': 'bool',
            'access': 'str',
            'identity_squash': 'str',
            'anonymous_uid': 'int',
            'anonymous_gid': 'int'
        }

        self.attribute_map = {
            'source': 'source',
            'require_privileged_source_port': 'requirePrivilegedSourcePort',
            'access': 'access',
            'identity_squash': 'identitySquash',
            'anonymous_uid': 'anonymousUid',
            'anonymous_gid': 'anonymousGid'
        }

        self._source = None
        self._require_privileged_source_port = None
        self._access = None
        self._identity_squash = None
        self._anonymous_uid = None
        self._anonymous_gid = None

    @property
    def source(self):
        """
        **[Required]** Gets the source of this ClientOptions.
        Clients these options should apply to. Must be a either
        single IPv4 address or single IPv4 CIDR block.

        **Note:** Access will also be limited by any applicable VCN
        security rules and the ability to route IP packets to the
        mount target. Mount targets do not have Internet-routable IP addresses.


        :return: The source of this ClientOptions.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ClientOptions.
        Clients these options should apply to. Must be a either
        single IPv4 address or single IPv4 CIDR block.

        **Note:** Access will also be limited by any applicable VCN
        security rules and the ability to route IP packets to the
        mount target. Mount targets do not have Internet-routable IP addresses.


        :param source: The source of this ClientOptions.
        :type: str
        """
        self._source = source

    @property
    def require_privileged_source_port(self):
        """
        Gets the require_privileged_source_port of this ClientOptions.
        If `true`, clients accessing the file system through this
        export must connect from a privileged source port. If
        unspecified, defaults to `true`.


        :return: The require_privileged_source_port of this ClientOptions.
        :rtype: bool
        """
        return self._require_privileged_source_port

    @require_privileged_source_port.setter
    def require_privileged_source_port(self, require_privileged_source_port):
        """
        Sets the require_privileged_source_port of this ClientOptions.
        If `true`, clients accessing the file system through this
        export must connect from a privileged source port. If
        unspecified, defaults to `true`.


        :param require_privileged_source_port: The require_privileged_source_port of this ClientOptions.
        :type: bool
        """
        self._require_privileged_source_port = require_privileged_source_port

    @property
    def access(self):
        """
        Gets the access of this ClientOptions.
        Type of access to grant clients using the file system
        through this export. If unspecified defaults to `READ_ONLY`.

        Allowed values for this property are: "READ_WRITE", "READ_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The access of this ClientOptions.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """
        Sets the access of this ClientOptions.
        Type of access to grant clients using the file system
        through this export. If unspecified defaults to `READ_ONLY`.


        :param access: The access of this ClientOptions.
        :type: str
        """
        allowed_values = ["READ_WRITE", "READ_ONLY"]
        if not value_allowed_none_or_none_sentinel(access, allowed_values):
            access = 'UNKNOWN_ENUM_VALUE'
        self._access = access

    @property
    def identity_squash(self):
        """
        Gets the identity_squash of this ClientOptions.
        Used when clients accessing the file system through this export
        have their UID and GID remapped to 'anonymousUid' and
        'anonymousGid'. If `ALL`, all users and groups are remapped;
        if `ROOT`, only the root user and group (UID/GID 0) are
        remapped; if `NONE`, no remapping is done. If unspecified,
        defaults to `ROOT`.

        Allowed values for this property are: "NONE", "ROOT", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The identity_squash of this ClientOptions.
        :rtype: str
        """
        return self._identity_squash

    @identity_squash.setter
    def identity_squash(self, identity_squash):
        """
        Sets the identity_squash of this ClientOptions.
        Used when clients accessing the file system through this export
        have their UID and GID remapped to 'anonymousUid' and
        'anonymousGid'. If `ALL`, all users and groups are remapped;
        if `ROOT`, only the root user and group (UID/GID 0) are
        remapped; if `NONE`, no remapping is done. If unspecified,
        defaults to `ROOT`.


        :param identity_squash: The identity_squash of this ClientOptions.
        :type: str
        """
        allowed_values = ["NONE", "ROOT", "ALL"]
        if not value_allowed_none_or_none_sentinel(identity_squash, allowed_values):
            identity_squash = 'UNKNOWN_ENUM_VALUE'
        self._identity_squash = identity_squash

    @property
    def anonymous_uid(self):
        """
        Gets the anonymous_uid of this ClientOptions.
        UID value to remap to when squashing a client UID (see
        identitySquash for more details.) If unspecified, defaults
        to `65534`.


        :return: The anonymous_uid of this ClientOptions.
        :rtype: int
        """
        return self._anonymous_uid

    @anonymous_uid.setter
    def anonymous_uid(self, anonymous_uid):
        """
        Sets the anonymous_uid of this ClientOptions.
        UID value to remap to when squashing a client UID (see
        identitySquash for more details.) If unspecified, defaults
        to `65534`.


        :param anonymous_uid: The anonymous_uid of this ClientOptions.
        :type: int
        """
        self._anonymous_uid = anonymous_uid

    @property
    def anonymous_gid(self):
        """
        Gets the anonymous_gid of this ClientOptions.
        GID value to remap to when squashing a client GID (see
        identitySquash for more details.) If unspecified defaults
        to `65534`.


        :return: The anonymous_gid of this ClientOptions.
        :rtype: int
        """
        return self._anonymous_gid

    @anonymous_gid.setter
    def anonymous_gid(self, anonymous_gid):
        """
        Sets the anonymous_gid of this ClientOptions.
        GID value to remap to when squashing a client GID (see
        identitySquash for more details.) If unspecified defaults
        to `65534`.


        :param anonymous_gid: The anonymous_gid of this ClientOptions.
        :type: int
        """
        self._anonymous_gid = anonymous_gid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
