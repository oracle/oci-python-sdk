# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Server(object):
    """
    The server object that is returned by the API to get a specific server in a WebLogic domain.
    """

    #: A constant which can be used with the latest_patches_status property of a Server.
    #: This constant has a value of "ON_LATEST_PATCHES"
    LATEST_PATCHES_STATUS_ON_LATEST_PATCHES = "ON_LATEST_PATCHES"

    #: A constant which can be used with the latest_patches_status property of a Server.
    #: This constant has a value of "PATCHING_REQUIRED"
    LATEST_PATCHES_STATUS_PATCHING_REQUIRED = "PATCHING_REQUIRED"

    #: A constant which can be used with the latest_patches_status property of a Server.
    #: This constant has a value of "UNKNOWN"
    LATEST_PATCHES_STATUS_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the patch_readiness_status property of a Server.
    #: This constant has a value of "OK"
    PATCH_READINESS_STATUS_OK = "OK"

    #: A constant which can be used with the patch_readiness_status property of a Server.
    #: This constant has a value of "WARNING"
    PATCH_READINESS_STATUS_WARNING = "WARNING"

    #: A constant which can be used with the patch_readiness_status property of a Server.
    #: This constant has a value of "ERROR"
    PATCH_READINESS_STATUS_ERROR = "ERROR"

    #: A constant which can be used with the patch_readiness_status property of a Server.
    #: This constant has a value of "UNKNOWN"
    PATCH_READINESS_STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new Server object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Server.
        :type id: str

        :param name:
            The value to assign to the name property of this Server.
        :type name: str

        :param is_admin:
            The value to assign to the is_admin property of this Server.
        :type is_admin: bool

        :param status:
            The value to assign to the status property of this Server.
        :type status: str

        :param restart_order:
            The value to assign to the restart_order property of this Server.
        :type restart_order: int

        :param middleware_path:
            The value to assign to the middleware_path property of this Server.
        :type middleware_path: str

        :param middleware_type:
            The value to assign to the middleware_type property of this Server.
        :type middleware_type: str

        :param weblogic_version:
            The value to assign to the weblogic_version property of this Server.
        :type weblogic_version: str

        :param jdk_path:
            The value to assign to the jdk_path property of this Server.
        :type jdk_path: str

        :param jdk_version:
            The value to assign to the jdk_version property of this Server.
        :type jdk_version: str

        :param wls_domain_name:
            The value to assign to the wls_domain_name property of this Server.
        :type wls_domain_name: str

        :param wls_domain_id:
            The value to assign to the wls_domain_id property of this Server.
        :type wls_domain_id: str

        :param wls_domain_path:
            The value to assign to the wls_domain_path property of this Server.
        :type wls_domain_path: str

        :param latest_patches_status:
            The value to assign to the latest_patches_status property of this Server.
            Allowed values for this property are: "ON_LATEST_PATCHES", "PATCHING_REQUIRED", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type latest_patches_status: str

        :param patch_readiness_status:
            The value to assign to the patch_readiness_status property of this Server.
            Allowed values for this property are: "OK", "WARNING", "ERROR", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type patch_readiness_status: str

        :param host_name:
            The value to assign to the host_name property of this Server.
        :type host_name: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this Server.
        :type managed_instance_id: str

        :param time_created:
            The value to assign to the time_created property of this Server.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Server.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'is_admin': 'bool',
            'status': 'str',
            'restart_order': 'int',
            'middleware_path': 'str',
            'middleware_type': 'str',
            'weblogic_version': 'str',
            'jdk_path': 'str',
            'jdk_version': 'str',
            'wls_domain_name': 'str',
            'wls_domain_id': 'str',
            'wls_domain_path': 'str',
            'latest_patches_status': 'str',
            'patch_readiness_status': 'str',
            'host_name': 'str',
            'managed_instance_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'is_admin': 'isAdmin',
            'status': 'status',
            'restart_order': 'restartOrder',
            'middleware_path': 'middlewarePath',
            'middleware_type': 'middlewareType',
            'weblogic_version': 'weblogicVersion',
            'jdk_path': 'jdkPath',
            'jdk_version': 'jdkVersion',
            'wls_domain_name': 'wlsDomainName',
            'wls_domain_id': 'wlsDomainId',
            'wls_domain_path': 'wlsDomainPath',
            'latest_patches_status': 'latestPatchesStatus',
            'patch_readiness_status': 'patchReadinessStatus',
            'host_name': 'hostName',
            'managed_instance_id': 'managedInstanceId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._id = None
        self._name = None
        self._is_admin = None
        self._status = None
        self._restart_order = None
        self._middleware_path = None
        self._middleware_type = None
        self._weblogic_version = None
        self._jdk_path = None
        self._jdk_version = None
        self._wls_domain_name = None
        self._wls_domain_id = None
        self._wls_domain_path = None
        self._latest_patches_status = None
        self._patch_readiness_status = None
        self._host_name = None
        self._managed_instance_id = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        Gets the id of this Server.
        The unique identifier of the server.

        **Note:** Not an `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Server.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Server.
        The unique identifier of the server.

        **Note:** Not an `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Server.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Server.
        The name of the server.


        :return: The name of this Server.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Server.
        The name of the server.


        :param name: The name of this Server.
        :type: str
        """
        self._name = name

    @property
    def is_admin(self):
        """
        **[Required]** Gets the is_admin of this Server.
        Whether or not the server is an admin node.


        :return: The is_admin of this Server.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this Server.
        Whether or not the server is an admin node.


        :param is_admin: The is_admin of this Server.
        :type: bool
        """
        self._is_admin = is_admin

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Server.
        The status of the server.


        :return: The status of this Server.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Server.
        The status of the server.


        :param status: The status of this Server.
        :type: str
        """
        self._status = status

    @property
    def restart_order(self):
        """
        Gets the restart_order of this Server.
        The restart order assigned to the server.


        :return: The restart_order of this Server.
        :rtype: int
        """
        return self._restart_order

    @restart_order.setter
    def restart_order(self, restart_order):
        """
        Sets the restart_order of this Server.
        The restart order assigned to the server.


        :param restart_order: The restart_order of this Server.
        :type: int
        """
        self._restart_order = restart_order

    @property
    def middleware_path(self):
        """
        Gets the middleware_path of this Server.
        The middleware path on the server.


        :return: The middleware_path of this Server.
        :rtype: str
        """
        return self._middleware_path

    @middleware_path.setter
    def middleware_path(self, middleware_path):
        """
        Sets the middleware_path of this Server.
        The middleware path on the server.


        :param middleware_path: The middleware_path of this Server.
        :type: str
        """
        self._middleware_path = middleware_path

    @property
    def middleware_type(self):
        """
        Gets the middleware_type of this Server.
        The middleware type on the server.


        :return: The middleware_type of this Server.
        :rtype: str
        """
        return self._middleware_type

    @middleware_type.setter
    def middleware_type(self, middleware_type):
        """
        Sets the middleware_type of this Server.
        The middleware type on the server.


        :param middleware_type: The middleware_type of this Server.
        :type: str
        """
        self._middleware_type = middleware_type

    @property
    def weblogic_version(self):
        """
        Gets the weblogic_version of this Server.
        The version of the WebLogic domain of the server


        :return: The weblogic_version of this Server.
        :rtype: str
        """
        return self._weblogic_version

    @weblogic_version.setter
    def weblogic_version(self, weblogic_version):
        """
        Sets the weblogic_version of this Server.
        The version of the WebLogic domain of the server


        :param weblogic_version: The weblogic_version of this Server.
        :type: str
        """
        self._weblogic_version = weblogic_version

    @property
    def jdk_path(self):
        """
        Gets the jdk_path of this Server.
        The JDK path on the server.


        :return: The jdk_path of this Server.
        :rtype: str
        """
        return self._jdk_path

    @jdk_path.setter
    def jdk_path(self, jdk_path):
        """
        Sets the jdk_path of this Server.
        The JDK path on the server.


        :param jdk_path: The jdk_path of this Server.
        :type: str
        """
        self._jdk_path = jdk_path

    @property
    def jdk_version(self):
        """
        Gets the jdk_version of this Server.
        The JDK version on the server.


        :return: The jdk_version of this Server.
        :rtype: str
        """
        return self._jdk_version

    @jdk_version.setter
    def jdk_version(self, jdk_version):
        """
        Sets the jdk_version of this Server.
        The JDK version on the server.


        :param jdk_version: The jdk_version of this Server.
        :type: str
        """
        self._jdk_version = jdk_version

    @property
    def wls_domain_name(self):
        """
        Gets the wls_domain_name of this Server.
        The name of the WebLogic domain to which the server belongs.


        :return: The wls_domain_name of this Server.
        :rtype: str
        """
        return self._wls_domain_name

    @wls_domain_name.setter
    def wls_domain_name(self, wls_domain_name):
        """
        Sets the wls_domain_name of this Server.
        The name of the WebLogic domain to which the server belongs.


        :param wls_domain_name: The wls_domain_name of this Server.
        :type: str
        """
        self._wls_domain_name = wls_domain_name

    @property
    def wls_domain_id(self):
        """
        Gets the wls_domain_id of this Server.
        The ID of the WebLogic domain to which the server belongs.


        :return: The wls_domain_id of this Server.
        :rtype: str
        """
        return self._wls_domain_id

    @wls_domain_id.setter
    def wls_domain_id(self, wls_domain_id):
        """
        Sets the wls_domain_id of this Server.
        The ID of the WebLogic domain to which the server belongs.


        :param wls_domain_id: The wls_domain_id of this Server.
        :type: str
        """
        self._wls_domain_id = wls_domain_id

    @property
    def wls_domain_path(self):
        """
        Gets the wls_domain_path of this Server.
        The path of the WebLogic domain to which the server belongs.


        :return: The wls_domain_path of this Server.
        :rtype: str
        """
        return self._wls_domain_path

    @wls_domain_path.setter
    def wls_domain_path(self, wls_domain_path):
        """
        Sets the wls_domain_path of this Server.
        The path of the WebLogic domain to which the server belongs.


        :param wls_domain_path: The wls_domain_path of this Server.
        :type: str
        """
        self._wls_domain_path = wls_domain_path

    @property
    def latest_patches_status(self):
        """
        Gets the latest_patches_status of this Server.
        Whether or not the server has installed the latest patches.

        Allowed values for this property are: "ON_LATEST_PATCHES", "PATCHING_REQUIRED", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The latest_patches_status of this Server.
        :rtype: str
        """
        return self._latest_patches_status

    @latest_patches_status.setter
    def latest_patches_status(self, latest_patches_status):
        """
        Sets the latest_patches_status of this Server.
        Whether or not the server has installed the latest patches.


        :param latest_patches_status: The latest_patches_status of this Server.
        :type: str
        """
        allowed_values = ["ON_LATEST_PATCHES", "PATCHING_REQUIRED", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(latest_patches_status, allowed_values):
            latest_patches_status = 'UNKNOWN_ENUM_VALUE'
        self._latest_patches_status = latest_patches_status

    @property
    def patch_readiness_status(self):
        """
        Gets the patch_readiness_status of this Server.
        The patch readiness status of the server.

        Allowed values for this property are: "OK", "WARNING", "ERROR", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The patch_readiness_status of this Server.
        :rtype: str
        """
        return self._patch_readiness_status

    @patch_readiness_status.setter
    def patch_readiness_status(self, patch_readiness_status):
        """
        Sets the patch_readiness_status of this Server.
        The patch readiness status of the server.


        :param patch_readiness_status: The patch_readiness_status of this Server.
        :type: str
        """
        allowed_values = ["OK", "WARNING", "ERROR", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(patch_readiness_status, allowed_values):
            patch_readiness_status = 'UNKNOWN_ENUM_VALUE'
        self._patch_readiness_status = patch_readiness_status

    @property
    def host_name(self):
        """
        Gets the host_name of this Server.
        The name of the server.


        :return: The host_name of this Server.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this Server.
        The name of the server.


        :param host_name: The host_name of this Server.
        :type: str
        """
        self._host_name = host_name

    @property
    def managed_instance_id(self):
        """
        Gets the managed_instance_id of this Server.
        The managed instance ID of the server.


        :return: The managed_instance_id of this Server.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this Server.
        The managed instance ID of the server.


        :param managed_instance_id: The managed_instance_id of this Server.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Server.
        The date and time the server was first reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Server.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Server.
        The date and time the server was first reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Server.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Server.
        The date and time the server was last reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this Server.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Server.
        The date and time the server was last reported (in `RFC 3339`__ format).

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this Server.
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
