# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDeployStageDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDeployStageDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.UpdateOkeCanaryTrafficShiftDeployStageDetails`
        * :class:`~oci.devops.models.UpdateOkeCanaryDeployStageDetails`
        * :class:`~oci.devops.models.UpdateOkeHelmChartDeployStageDetails`
        * :class:`~oci.devops.models.UpdateComputeInstanceGroupDeployStageDetails`
        * :class:`~oci.devops.models.UpdateOkeCanaryApprovalDeployStageDetails`
        * :class:`~oci.devops.models.UpdateOkeDeployStageDetails`
        * :class:`~oci.devops.models.UpdateComputeInstanceGroupCanaryApprovalDeployStageDetails`
        * :class:`~oci.devops.models.UpdateLoadBalancerTrafficShiftDeployStageDetails`
        * :class:`~oci.devops.models.UpdateOkeBlueGreenDeployStageDetails`
        * :class:`~oci.devops.models.UpdateWaitDeployStageDetails`
        * :class:`~oci.devops.models.UpdateOkeBlueGreenTrafficShiftDeployStageDetails`
        * :class:`~oci.devops.models.UpdateManualApprovalDeployStageDetails`
        * :class:`~oci.devops.models.UpdateComputeInstanceGroupBlueGreenDeployStageDetails`
        * :class:`~oci.devops.models.UpdateComputeInstanceGroupCanaryDeployStageDetails`
        * :class:`~oci.devops.models.UpdateFunctionDeployStageDetails`
        * :class:`~oci.devops.models.UpdateComputeInstanceGroupBlueGreenTrafficShiftDeployStageDetails`
        * :class:`~oci.devops.models.UpdateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails`
        * :class:`~oci.devops.models.UpdateInvokeFunctionDeployStageDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deployStageType']

        if type == 'OKE_CANARY_TRAFFIC_SHIFT':
            return 'UpdateOkeCanaryTrafficShiftDeployStageDetails'

        if type == 'OKE_CANARY_DEPLOYMENT':
            return 'UpdateOkeCanaryDeployStageDetails'

        if type == 'OKE_HELM_CHART_DEPLOYMENT':
            return 'UpdateOkeHelmChartDeployStageDetails'

        if type == 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT':
            return 'UpdateComputeInstanceGroupDeployStageDetails'

        if type == 'OKE_CANARY_APPROVAL':
            return 'UpdateOkeCanaryApprovalDeployStageDetails'

        if type == 'OKE_DEPLOYMENT':
            return 'UpdateOkeDeployStageDetails'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL':
            return 'UpdateComputeInstanceGroupCanaryApprovalDeployStageDetails'

        if type == 'LOAD_BALANCER_TRAFFIC_SHIFT':
            return 'UpdateLoadBalancerTrafficShiftDeployStageDetails'

        if type == 'OKE_BLUE_GREEN_DEPLOYMENT':
            return 'UpdateOkeBlueGreenDeployStageDetails'

        if type == 'WAIT':
            return 'UpdateWaitDeployStageDetails'

        if type == 'OKE_BLUE_GREEN_TRAFFIC_SHIFT':
            return 'UpdateOkeBlueGreenTrafficShiftDeployStageDetails'

        if type == 'MANUAL_APPROVAL':
            return 'UpdateManualApprovalDeployStageDetails'

        if type == 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT':
            return 'UpdateComputeInstanceGroupBlueGreenDeployStageDetails'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT':
            return 'UpdateComputeInstanceGroupCanaryDeployStageDetails'

        if type == 'DEPLOY_FUNCTION':
            return 'UpdateFunctionDeployStageDetails'

        if type == 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT':
            return 'UpdateComputeInstanceGroupBlueGreenTrafficShiftDeployStageDetails'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT':
            return 'UpdateComputeInstanceGroupCanaryTrafficShiftDeployStageDetails'

        if type == 'INVOKE_FUNCTION':
            return 'UpdateInvokeFunctionDeployStageDetails'
        else:
            return 'UpdateDeployStageDetails'

    @property
    def description(self):
        """
        Gets the description of this UpdateDeployStageDetails.
        Optional description about the deployment stage.


        :return: The description of this UpdateDeployStageDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDeployStageDetails.
        Optional description about the deployment stage.


        :param description: The description of this UpdateDeployStageDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDeployStageDetails.
        Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this UpdateDeployStageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDeployStageDetails.
        Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDeployStageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def deploy_stage_type(self):
        """
        **[Required]** Gets the deploy_stage_type of this UpdateDeployStageDetails.
        Deployment stage type.


        :return: The deploy_stage_type of this UpdateDeployStageDetails.
        :rtype: str
        """
        return self._deploy_stage_type

    @deploy_stage_type.setter
    def deploy_stage_type(self, deploy_stage_type):
        """
        Sets the deploy_stage_type of this UpdateDeployStageDetails.
        Deployment stage type.


        :param deploy_stage_type: The deploy_stage_type of this UpdateDeployStageDetails.
        :type: str
        """
        self._deploy_stage_type = deploy_stage_type

    @property
    def deploy_stage_predecessor_collection(self):
        """
        Gets the deploy_stage_predecessor_collection of this UpdateDeployStageDetails.

        :return: The deploy_stage_predecessor_collection of this UpdateDeployStageDetails.
        :rtype: oci.devops.models.DeployStagePredecessorCollection
        """
        return self._deploy_stage_predecessor_collection

    @deploy_stage_predecessor_collection.setter
    def deploy_stage_predecessor_collection(self, deploy_stage_predecessor_collection):
        """
        Sets the deploy_stage_predecessor_collection of this UpdateDeployStageDetails.

        :param deploy_stage_predecessor_collection: The deploy_stage_predecessor_collection of this UpdateDeployStageDetails.
        :type: oci.devops.models.DeployStagePredecessorCollection
        """
        self._deploy_stage_predecessor_collection = deploy_stage_predecessor_collection

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDeployStageDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDeployStageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDeployStageDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDeployStageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDeployStageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDeployStageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDeployStageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDeployStageDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
