# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployArtifactOverrideArgument(object):
    """
    Values for artifact parameters to be supplied at the time of deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployArtifactOverrideArgument object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this DeployArtifactOverrideArgument.
        :type deploy_artifact_id: str

        :param name:
            The value to assign to the name property of this DeployArtifactOverrideArgument.
        :type name: str

        :param value:
            The value to assign to the value property of this DeployArtifactOverrideArgument.
        :type value: str

        """
        self.swagger_types = {
            'deploy_artifact_id': 'str',
            'name': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_id': 'deployArtifactId',
            'name': 'name',
            'value': 'value'
        }

        self._deploy_artifact_id = None
        self._name = None
        self._value = None

    @property
    def deploy_artifact_id(self):
        """
        **[Required]** Gets the deploy_artifact_id of this DeployArtifactOverrideArgument.
        The OCID of the artifact to which this parameter applies.


        :return: The deploy_artifact_id of this DeployArtifactOverrideArgument.
        :rtype: str
        """
        return self._deploy_artifact_id

    @deploy_artifact_id.setter
    def deploy_artifact_id(self, deploy_artifact_id):
        """
        Sets the deploy_artifact_id of this DeployArtifactOverrideArgument.
        The OCID of the artifact to which this parameter applies.


        :param deploy_artifact_id: The deploy_artifact_id of this DeployArtifactOverrideArgument.
        :type: str
        """
        self._deploy_artifact_id = deploy_artifact_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DeployArtifactOverrideArgument.
        Name of the parameter (case-sensitive).


        :return: The name of this DeployArtifactOverrideArgument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeployArtifactOverrideArgument.
        Name of the parameter (case-sensitive).


        :param name: The name of this DeployArtifactOverrideArgument.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this DeployArtifactOverrideArgument.
        Value of the parameter.


        :return: The value of this DeployArtifactOverrideArgument.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DeployArtifactOverrideArgument.
        Value of the parameter.


        :param value: The value of this DeployArtifactOverrideArgument.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
