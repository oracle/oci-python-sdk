# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GoldenGateHub(object):
    """
    Details about Oracle GoldenGate Microservices.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GoldenGateHub object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rest_admin_credentials:
            The value to assign to the rest_admin_credentials property of this GoldenGateHub.
        :type rest_admin_credentials: oci.database_migration.models.AdminCredentials

        :param source_db_admin_credentials:
            The value to assign to the source_db_admin_credentials property of this GoldenGateHub.
        :type source_db_admin_credentials: oci.database_migration.models.AdminCredentials

        :param source_container_db_admin_credentials:
            The value to assign to the source_container_db_admin_credentials property of this GoldenGateHub.
        :type source_container_db_admin_credentials: oci.database_migration.models.AdminCredentials

        :param target_db_admin_credentials:
            The value to assign to the target_db_admin_credentials property of this GoldenGateHub.
        :type target_db_admin_credentials: oci.database_migration.models.AdminCredentials

        :param url:
            The value to assign to the url property of this GoldenGateHub.
        :type url: str

        :param source_microservices_deployment_name:
            The value to assign to the source_microservices_deployment_name property of this GoldenGateHub.
        :type source_microservices_deployment_name: str

        :param target_microservices_deployment_name:
            The value to assign to the target_microservices_deployment_name property of this GoldenGateHub.
        :type target_microservices_deployment_name: str

        :param compute_id:
            The value to assign to the compute_id property of this GoldenGateHub.
        :type compute_id: str

        """
        self.swagger_types = {
            'rest_admin_credentials': 'AdminCredentials',
            'source_db_admin_credentials': 'AdminCredentials',
            'source_container_db_admin_credentials': 'AdminCredentials',
            'target_db_admin_credentials': 'AdminCredentials',
            'url': 'str',
            'source_microservices_deployment_name': 'str',
            'target_microservices_deployment_name': 'str',
            'compute_id': 'str'
        }

        self.attribute_map = {
            'rest_admin_credentials': 'restAdminCredentials',
            'source_db_admin_credentials': 'sourceDbAdminCredentials',
            'source_container_db_admin_credentials': 'sourceContainerDbAdminCredentials',
            'target_db_admin_credentials': 'targetDbAdminCredentials',
            'url': 'url',
            'source_microservices_deployment_name': 'sourceMicroservicesDeploymentName',
            'target_microservices_deployment_name': 'targetMicroservicesDeploymentName',
            'compute_id': 'computeId'
        }

        self._rest_admin_credentials = None
        self._source_db_admin_credentials = None
        self._source_container_db_admin_credentials = None
        self._target_db_admin_credentials = None
        self._url = None
        self._source_microservices_deployment_name = None
        self._target_microservices_deployment_name = None
        self._compute_id = None

    @property
    def rest_admin_credentials(self):
        """
        **[Required]** Gets the rest_admin_credentials of this GoldenGateHub.

        :return: The rest_admin_credentials of this GoldenGateHub.
        :rtype: oci.database_migration.models.AdminCredentials
        """
        return self._rest_admin_credentials

    @rest_admin_credentials.setter
    def rest_admin_credentials(self, rest_admin_credentials):
        """
        Sets the rest_admin_credentials of this GoldenGateHub.

        :param rest_admin_credentials: The rest_admin_credentials of this GoldenGateHub.
        :type: oci.database_migration.models.AdminCredentials
        """
        self._rest_admin_credentials = rest_admin_credentials

    @property
    def source_db_admin_credentials(self):
        """
        **[Required]** Gets the source_db_admin_credentials of this GoldenGateHub.

        :return: The source_db_admin_credentials of this GoldenGateHub.
        :rtype: oci.database_migration.models.AdminCredentials
        """
        return self._source_db_admin_credentials

    @source_db_admin_credentials.setter
    def source_db_admin_credentials(self, source_db_admin_credentials):
        """
        Sets the source_db_admin_credentials of this GoldenGateHub.

        :param source_db_admin_credentials: The source_db_admin_credentials of this GoldenGateHub.
        :type: oci.database_migration.models.AdminCredentials
        """
        self._source_db_admin_credentials = source_db_admin_credentials

    @property
    def source_container_db_admin_credentials(self):
        """
        Gets the source_container_db_admin_credentials of this GoldenGateHub.

        :return: The source_container_db_admin_credentials of this GoldenGateHub.
        :rtype: oci.database_migration.models.AdminCredentials
        """
        return self._source_container_db_admin_credentials

    @source_container_db_admin_credentials.setter
    def source_container_db_admin_credentials(self, source_container_db_admin_credentials):
        """
        Sets the source_container_db_admin_credentials of this GoldenGateHub.

        :param source_container_db_admin_credentials: The source_container_db_admin_credentials of this GoldenGateHub.
        :type: oci.database_migration.models.AdminCredentials
        """
        self._source_container_db_admin_credentials = source_container_db_admin_credentials

    @property
    def target_db_admin_credentials(self):
        """
        **[Required]** Gets the target_db_admin_credentials of this GoldenGateHub.

        :return: The target_db_admin_credentials of this GoldenGateHub.
        :rtype: oci.database_migration.models.AdminCredentials
        """
        return self._target_db_admin_credentials

    @target_db_admin_credentials.setter
    def target_db_admin_credentials(self, target_db_admin_credentials):
        """
        Sets the target_db_admin_credentials of this GoldenGateHub.

        :param target_db_admin_credentials: The target_db_admin_credentials of this GoldenGateHub.
        :type: oci.database_migration.models.AdminCredentials
        """
        self._target_db_admin_credentials = target_db_admin_credentials

    @property
    def url(self):
        """
        **[Required]** Gets the url of this GoldenGateHub.
        Oracle GoldenGate hub's REST endpoint.
        Refer to https://docs.oracle.com/en/middleware/goldengate/core/19.1/securing/network.html#GUID-A709DA55-111D-455E-8942-C9BDD1E38CAA


        :return: The url of this GoldenGateHub.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this GoldenGateHub.
        Oracle GoldenGate hub's REST endpoint.
        Refer to https://docs.oracle.com/en/middleware/goldengate/core/19.1/securing/network.html#GUID-A709DA55-111D-455E-8942-C9BDD1E38CAA


        :param url: The url of this GoldenGateHub.
        :type: str
        """
        self._url = url

    @property
    def source_microservices_deployment_name(self):
        """
        **[Required]** Gets the source_microservices_deployment_name of this GoldenGateHub.
        Name of GoldenGate deployment to operate on source database


        :return: The source_microservices_deployment_name of this GoldenGateHub.
        :rtype: str
        """
        return self._source_microservices_deployment_name

    @source_microservices_deployment_name.setter
    def source_microservices_deployment_name(self, source_microservices_deployment_name):
        """
        Sets the source_microservices_deployment_name of this GoldenGateHub.
        Name of GoldenGate deployment to operate on source database


        :param source_microservices_deployment_name: The source_microservices_deployment_name of this GoldenGateHub.
        :type: str
        """
        self._source_microservices_deployment_name = source_microservices_deployment_name

    @property
    def target_microservices_deployment_name(self):
        """
        **[Required]** Gets the target_microservices_deployment_name of this GoldenGateHub.
        Name of GoldenGate deployment to operate on target database


        :return: The target_microservices_deployment_name of this GoldenGateHub.
        :rtype: str
        """
        return self._target_microservices_deployment_name

    @target_microservices_deployment_name.setter
    def target_microservices_deployment_name(self, target_microservices_deployment_name):
        """
        Sets the target_microservices_deployment_name of this GoldenGateHub.
        Name of GoldenGate deployment to operate on target database


        :param target_microservices_deployment_name: The target_microservices_deployment_name of this GoldenGateHub.
        :type: str
        """
        self._target_microservices_deployment_name = target_microservices_deployment_name

    @property
    def compute_id(self):
        """
        Gets the compute_id of this GoldenGateHub.
        OCID of GoldenGate compute instance.


        :return: The compute_id of this GoldenGateHub.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        """
        Sets the compute_id of this GoldenGateHub.
        OCID of GoldenGate compute instance.


        :param compute_id: The compute_id of this GoldenGateHub.
        :type: str
        """
        self._compute_id = compute_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
