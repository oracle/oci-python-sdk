# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deploy_stage_details import UpdateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInvokeFunctionDeployStageDetails(UpdateDeployStageDetails):
    """
    Specifies Invoke Function stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInvokeFunctionDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateInvokeFunctionDeployStageDetails.deploy_stage_type` attribute
        of this class is ``INVOKE_FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateInvokeFunctionDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateInvokeFunctionDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateInvokeFunctionDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateInvokeFunctionDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateInvokeFunctionDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateInvokeFunctionDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param function_deploy_environment_id:
            The value to assign to the function_deploy_environment_id property of this UpdateInvokeFunctionDeployStageDetails.
        :type function_deploy_environment_id: str

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this UpdateInvokeFunctionDeployStageDetails.
        :type deploy_artifact_id: str

        :param is_async:
            The value to assign to the is_async property of this UpdateInvokeFunctionDeployStageDetails.
        :type is_async: bool

        :param is_validation_enabled:
            The value to assign to the is_validation_enabled property of this UpdateInvokeFunctionDeployStageDetails.
        :type is_validation_enabled: bool

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'function_deploy_environment_id': 'str',
            'deploy_artifact_id': 'str',
            'is_async': 'bool',
            'is_validation_enabled': 'bool'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'function_deploy_environment_id': 'functionDeployEnvironmentId',
            'deploy_artifact_id': 'deployArtifactId',
            'is_async': 'isAsync',
            'is_validation_enabled': 'isValidationEnabled'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._function_deploy_environment_id = None
        self._deploy_artifact_id = None
        self._is_async = None
        self._is_validation_enabled = None
        self._deploy_stage_type = 'INVOKE_FUNCTION'

    @property
    def function_deploy_environment_id(self):
        """
        Gets the function_deploy_environment_id of this UpdateInvokeFunctionDeployStageDetails.
        Function environment OCID.


        :return: The function_deploy_environment_id of this UpdateInvokeFunctionDeployStageDetails.
        :rtype: str
        """
        return self._function_deploy_environment_id

    @function_deploy_environment_id.setter
    def function_deploy_environment_id(self, function_deploy_environment_id):
        """
        Sets the function_deploy_environment_id of this UpdateInvokeFunctionDeployStageDetails.
        Function environment OCID.


        :param function_deploy_environment_id: The function_deploy_environment_id of this UpdateInvokeFunctionDeployStageDetails.
        :type: str
        """
        self._function_deploy_environment_id = function_deploy_environment_id

    @property
    def deploy_artifact_id(self):
        """
        Gets the deploy_artifact_id of this UpdateInvokeFunctionDeployStageDetails.
        Optional binary artifact OCID user may provide to this stage.


        :return: The deploy_artifact_id of this UpdateInvokeFunctionDeployStageDetails.
        :rtype: str
        """
        return self._deploy_artifact_id

    @deploy_artifact_id.setter
    def deploy_artifact_id(self, deploy_artifact_id):
        """
        Sets the deploy_artifact_id of this UpdateInvokeFunctionDeployStageDetails.
        Optional binary artifact OCID user may provide to this stage.


        :param deploy_artifact_id: The deploy_artifact_id of this UpdateInvokeFunctionDeployStageDetails.
        :type: str
        """
        self._deploy_artifact_id = deploy_artifact_id

    @property
    def is_async(self):
        """
        Gets the is_async of this UpdateInvokeFunctionDeployStageDetails.
        A boolean flag specifies whether this stage executes asynchronously.


        :return: The is_async of this UpdateInvokeFunctionDeployStageDetails.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """
        Sets the is_async of this UpdateInvokeFunctionDeployStageDetails.
        A boolean flag specifies whether this stage executes asynchronously.


        :param is_async: The is_async of this UpdateInvokeFunctionDeployStageDetails.
        :type: bool
        """
        self._is_async = is_async

    @property
    def is_validation_enabled(self):
        """
        Gets the is_validation_enabled of this UpdateInvokeFunctionDeployStageDetails.
        A boolean flag specifies whether the invoked function must be validated.


        :return: The is_validation_enabled of this UpdateInvokeFunctionDeployStageDetails.
        :rtype: bool
        """
        return self._is_validation_enabled

    @is_validation_enabled.setter
    def is_validation_enabled(self, is_validation_enabled):
        """
        Sets the is_validation_enabled of this UpdateInvokeFunctionDeployStageDetails.
        A boolean flag specifies whether the invoked function must be validated.


        :param is_validation_enabled: The is_validation_enabled of this UpdateInvokeFunctionDeployStageDetails.
        :type: bool
        """
        self._is_validation_enabled = is_validation_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
