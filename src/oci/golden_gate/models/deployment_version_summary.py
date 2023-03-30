# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentVersionSummary(object):
    """
    The summary data of a specific deployment version.
    """

    #: A constant which can be used with the deployment_type property of a DeploymentVersionSummary.
    #: This constant has a value of "OGG"
    DEPLOYMENT_TYPE_OGG = "OGG"

    #: A constant which can be used with the deployment_type property of a DeploymentVersionSummary.
    #: This constant has a value of "DATABASE_ORACLE"
    DEPLOYMENT_TYPE_DATABASE_ORACLE = "DATABASE_ORACLE"

    #: A constant which can be used with the deployment_type property of a DeploymentVersionSummary.
    #: This constant has a value of "BIGDATA"
    DEPLOYMENT_TYPE_BIGDATA = "BIGDATA"

    #: A constant which can be used with the deployment_type property of a DeploymentVersionSummary.
    #: This constant has a value of "DATABASE_MICROSOFT_SQLSERVER"
    DEPLOYMENT_TYPE_DATABASE_MICROSOFT_SQLSERVER = "DATABASE_MICROSOFT_SQLSERVER"

    #: A constant which can be used with the deployment_type property of a DeploymentVersionSummary.
    #: This constant has a value of "DATABASE_MYSQL"
    DEPLOYMENT_TYPE_DATABASE_MYSQL = "DATABASE_MYSQL"

    #: A constant which can be used with the deployment_type property of a DeploymentVersionSummary.
    #: This constant has a value of "DATABASE_POSTGRESQL"
    DEPLOYMENT_TYPE_DATABASE_POSTGRESQL = "DATABASE_POSTGRESQL"

    #: A constant which can be used with the release_type property of a DeploymentVersionSummary.
    #: This constant has a value of "MAJOR"
    RELEASE_TYPE_MAJOR = "MAJOR"

    #: A constant which can be used with the release_type property of a DeploymentVersionSummary.
    #: This constant has a value of "BUNDLE"
    RELEASE_TYPE_BUNDLE = "BUNDLE"

    #: A constant which can be used with the release_type property of a DeploymentVersionSummary.
    #: This constant has a value of "MINOR"
    RELEASE_TYPE_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ogg_version:
            The value to assign to the ogg_version property of this DeploymentVersionSummary.
        :type ogg_version: str

        :param deployment_type:
            The value to assign to the deployment_type property of this DeploymentVersionSummary.
            Allowed values for this property are: "OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MICROSOFT_SQLSERVER", "DATABASE_MYSQL", "DATABASE_POSTGRESQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param time_released:
            The value to assign to the time_released property of this DeploymentVersionSummary.
        :type time_released: datetime

        :param release_type:
            The value to assign to the release_type property of this DeploymentVersionSummary.
            Allowed values for this property are: "MAJOR", "BUNDLE", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type release_type: str

        :param is_security_fix:
            The value to assign to the is_security_fix property of this DeploymentVersionSummary.
        :type is_security_fix: bool

        """
        self.swagger_types = {
            'ogg_version': 'str',
            'deployment_type': 'str',
            'time_released': 'datetime',
            'release_type': 'str',
            'is_security_fix': 'bool'
        }

        self.attribute_map = {
            'ogg_version': 'oggVersion',
            'deployment_type': 'deploymentType',
            'time_released': 'timeReleased',
            'release_type': 'releaseType',
            'is_security_fix': 'isSecurityFix'
        }

        self._ogg_version = None
        self._deployment_type = None
        self._time_released = None
        self._release_type = None
        self._is_security_fix = None

    @property
    def ogg_version(self):
        """
        **[Required]** Gets the ogg_version of this DeploymentVersionSummary.
        Version of OGG


        :return: The ogg_version of this DeploymentVersionSummary.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this DeploymentVersionSummary.
        Version of OGG


        :param ogg_version: The ogg_version of this DeploymentVersionSummary.
        :type: str
        """
        self._ogg_version = ogg_version

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this DeploymentVersionSummary.
        The type of deployment, which can be any one of the Allowed values.
        NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
            Its use is discouraged in favor of 'DATABASE_ORACLE'.

        Allowed values for this property are: "OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MICROSOFT_SQLSERVER", "DATABASE_MYSQL", "DATABASE_POSTGRESQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this DeploymentVersionSummary.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this DeploymentVersionSummary.
        The type of deployment, which can be any one of the Allowed values.
        NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.
            Its use is discouraged in favor of 'DATABASE_ORACLE'.


        :param deployment_type: The deployment_type of this DeploymentVersionSummary.
        :type: str
        """
        allowed_values = ["OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MICROSOFT_SQLSERVER", "DATABASE_MYSQL", "DATABASE_POSTGRESQL"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def time_released(self):
        """
        Gets the time_released of this DeploymentVersionSummary.
        The time the resource was released. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_released of this DeploymentVersionSummary.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this DeploymentVersionSummary.
        The time the resource was released. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_released: The time_released of this DeploymentVersionSummary.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def release_type(self):
        """
        Gets the release_type of this DeploymentVersionSummary.
        The type of release.

        Allowed values for this property are: "MAJOR", "BUNDLE", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The release_type of this DeploymentVersionSummary.
        :rtype: str
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """
        Sets the release_type of this DeploymentVersionSummary.
        The type of release.


        :param release_type: The release_type of this DeploymentVersionSummary.
        :type: str
        """
        allowed_values = ["MAJOR", "BUNDLE", "MINOR"]
        if not value_allowed_none_or_none_sentinel(release_type, allowed_values):
            release_type = 'UNKNOWN_ENUM_VALUE'
        self._release_type = release_type

    @property
    def is_security_fix(self):
        """
        Gets the is_security_fix of this DeploymentVersionSummary.
        Indicates if OGG release contains security fix.


        :return: The is_security_fix of this DeploymentVersionSummary.
        :rtype: bool
        """
        return self._is_security_fix

    @is_security_fix.setter
    def is_security_fix(self, is_security_fix):
        """
        Sets the is_security_fix of this DeploymentVersionSummary.
        Indicates if OGG release contains security fix.


        :param is_security_fix: The is_security_fix of this DeploymentVersionSummary.
        :type: bool
        """
        self._is_security_fix = is_security_fix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other