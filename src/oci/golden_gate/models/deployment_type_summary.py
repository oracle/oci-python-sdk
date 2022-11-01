# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentTypeSummary(object):
    """
    The meta-data specific on particular deployment type represented by deploymentType field.
    """

    #: A constant which can be used with the category property of a DeploymentTypeSummary.
    #: This constant has a value of "DATA_REPLICATION"
    CATEGORY_DATA_REPLICATION = "DATA_REPLICATION"

    #: A constant which can be used with the category property of a DeploymentTypeSummary.
    #: This constant has a value of "STREAM_ANALYTICS"
    CATEGORY_STREAM_ANALYTICS = "STREAM_ANALYTICS"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "OGG"
    DEPLOYMENT_TYPE_OGG = "OGG"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_ORACLE"
    DEPLOYMENT_TYPE_DATABASE_ORACLE = "DATABASE_ORACLE"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "BIGDATA"
    DEPLOYMENT_TYPE_BIGDATA = "BIGDATA"

    #: A constant which can be used with the deployment_type property of a DeploymentTypeSummary.
    #: This constant has a value of "DATABASE_MYSQL"
    DEPLOYMENT_TYPE_DATABASE_MYSQL = "DATABASE_MYSQL"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "GOLDENGATE"
    CONNECTION_TYPES_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "KAFKA"
    CONNECTION_TYPES_KAFKA = "KAFKA"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "MYSQL"
    CONNECTION_TYPES_MYSQL = "MYSQL"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    CONNECTION_TYPES_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the connection_types property of a DeploymentTypeSummary.
    #: This constant has a value of "ORACLE"
    CONNECTION_TYPES_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param category:
            The value to assign to the category property of this DeploymentTypeSummary.
            Allowed values for this property are: "DATA_REPLICATION", "STREAM_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        :param display_name:
            The value to assign to the display_name property of this DeploymentTypeSummary.
        :type display_name: str

        :param deployment_type:
            The value to assign to the deployment_type property of this DeploymentTypeSummary.
            Allowed values for this property are: "OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MYSQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param connection_types:
            The value to assign to the connection_types property of this DeploymentTypeSummary.
            Allowed values for items in this list are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_types: list[str]

        :param source_technologies:
            The value to assign to the source_technologies property of this DeploymentTypeSummary.
        :type source_technologies: list[str]

        :param target_technologies:
            The value to assign to the target_technologies property of this DeploymentTypeSummary.
        :type target_technologies: list[str]

        """
        self.swagger_types = {
            'category': 'str',
            'display_name': 'str',
            'deployment_type': 'str',
            'connection_types': 'list[str]',
            'source_technologies': 'list[str]',
            'target_technologies': 'list[str]'
        }

        self.attribute_map = {
            'category': 'category',
            'display_name': 'displayName',
            'deployment_type': 'deploymentType',
            'connection_types': 'connectionTypes',
            'source_technologies': 'sourceTechnologies',
            'target_technologies': 'targetTechnologies'
        }

        self._category = None
        self._display_name = None
        self._deployment_type = None
        self._connection_types = None
        self._source_technologies = None
        self._target_technologies = None

    @property
    def category(self):
        """
        **[Required]** Gets the category of this DeploymentTypeSummary.
        The deployment category defines the broad separation of the deployment type into categories.  Currently
        the separation is 'DATA_REPLICATION' and 'STREAM_ANALYTICS'.

        Allowed values for this property are: "DATA_REPLICATION", "STREAM_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this DeploymentTypeSummary.
        The deployment category defines the broad separation of the deployment type into categories.  Currently
        the separation is 'DATA_REPLICATION' and 'STREAM_ANALYTICS'.


        :param category: The category of this DeploymentTypeSummary.
        :type: str
        """
        allowed_values = ["DATA_REPLICATION", "STREAM_ANALYTICS"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DeploymentTypeSummary.
        An object's Display Name.


        :return: The display_name of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeploymentTypeSummary.
        An object's Display Name.


        :param display_name: The display_name of this DeploymentTypeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this DeploymentTypeSummary.
        The type of deployment, the value determines the exact 'type' of service executed in the Deployment.
        NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.  Its use is discouraged
              in favor of the equivalent 'DATABASE_ORACLE' value.

        Allowed values for this property are: "OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MYSQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this DeploymentTypeSummary.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this DeploymentTypeSummary.
        The type of deployment, the value determines the exact 'type' of service executed in the Deployment.
        NOTE: Use of the value 'OGG' is maintained for backward compatibility purposes.  Its use is discouraged
              in favor of the equivalent 'DATABASE_ORACLE' value.


        :param deployment_type: The deployment_type of this DeploymentTypeSummary.
        :type: str
        """
        allowed_values = ["OGG", "DATABASE_ORACLE", "BIGDATA", "DATABASE_MYSQL"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def connection_types(self):
        """
        Gets the connection_types of this DeploymentTypeSummary.
        An array of connectionTypes.

        Allowed values for items in this list are: "GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_types of this DeploymentTypeSummary.
        :rtype: list[str]
        """
        return self._connection_types

    @connection_types.setter
    def connection_types(self, connection_types):
        """
        Sets the connection_types of this DeploymentTypeSummary.
        An array of connectionTypes.


        :param connection_types: The connection_types of this DeploymentTypeSummary.
        :type: list[str]
        """
        allowed_values = ["GOLDENGATE", "KAFKA", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE"]
        if connection_types:
            connection_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in connection_types]
        self._connection_types = connection_types

    @property
    def source_technologies(self):
        """
        Gets the source_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :return: The source_technologies of this DeploymentTypeSummary.
        :rtype: list[str]
        """
        return self._source_technologies

    @source_technologies.setter
    def source_technologies(self, source_technologies):
        """
        Sets the source_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :param source_technologies: The source_technologies of this DeploymentTypeSummary.
        :type: list[str]
        """
        self._source_technologies = source_technologies

    @property
    def target_technologies(self):
        """
        Gets the target_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :return: The target_technologies of this DeploymentTypeSummary.
        :rtype: list[str]
        """
        return self._target_technologies

    @target_technologies.setter
    def target_technologies(self, target_technologies):
        """
        Sets the target_technologies of this DeploymentTypeSummary.
        List of the supported technologies generally.  The value is a freeform text string generally consisting
        of a description of the technology and optionally the speific version(s) support.  For example,
        [ \"Oracle Database 19c\", \"Oracle Exadata\", \"OCI Streaming\" ]


        :param target_technologies: The target_technologies of this DeploymentTypeSummary.
        :type: list[str]
        """
        self._target_technologies = target_technologies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
