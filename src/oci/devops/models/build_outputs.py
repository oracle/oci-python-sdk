# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildOutputs(object):
    """
    Outputs from the build.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BuildOutputs object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exported_variables:
            The value to assign to the exported_variables property of this BuildOutputs.
        :type exported_variables: oci.devops.models.ExportedVariableCollection

        :param delivered_artifacts:
            The value to assign to the delivered_artifacts property of this BuildOutputs.
        :type delivered_artifacts: oci.devops.models.DeliveredArtifactCollection

        :param artifact_override_parameters:
            The value to assign to the artifact_override_parameters property of this BuildOutputs.
        :type artifact_override_parameters: oci.devops.models.DeployArtifactOverrideArgumentCollection

        """
        self.swagger_types = {
            'exported_variables': 'ExportedVariableCollection',
            'delivered_artifacts': 'DeliveredArtifactCollection',
            'artifact_override_parameters': 'DeployArtifactOverrideArgumentCollection'
        }

        self.attribute_map = {
            'exported_variables': 'exportedVariables',
            'delivered_artifacts': 'deliveredArtifacts',
            'artifact_override_parameters': 'artifactOverrideParameters'
        }

        self._exported_variables = None
        self._delivered_artifacts = None
        self._artifact_override_parameters = None

    @property
    def exported_variables(self):
        """
        Gets the exported_variables of this BuildOutputs.

        :return: The exported_variables of this BuildOutputs.
        :rtype: oci.devops.models.ExportedVariableCollection
        """
        return self._exported_variables

    @exported_variables.setter
    def exported_variables(self, exported_variables):
        """
        Sets the exported_variables of this BuildOutputs.

        :param exported_variables: The exported_variables of this BuildOutputs.
        :type: oci.devops.models.ExportedVariableCollection
        """
        self._exported_variables = exported_variables

    @property
    def delivered_artifacts(self):
        """
        Gets the delivered_artifacts of this BuildOutputs.

        :return: The delivered_artifacts of this BuildOutputs.
        :rtype: oci.devops.models.DeliveredArtifactCollection
        """
        return self._delivered_artifacts

    @delivered_artifacts.setter
    def delivered_artifacts(self, delivered_artifacts):
        """
        Sets the delivered_artifacts of this BuildOutputs.

        :param delivered_artifacts: The delivered_artifacts of this BuildOutputs.
        :type: oci.devops.models.DeliveredArtifactCollection
        """
        self._delivered_artifacts = delivered_artifacts

    @property
    def artifact_override_parameters(self):
        """
        Gets the artifact_override_parameters of this BuildOutputs.

        :return: The artifact_override_parameters of this BuildOutputs.
        :rtype: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        return self._artifact_override_parameters

    @artifact_override_parameters.setter
    def artifact_override_parameters(self, artifact_override_parameters):
        """
        Sets the artifact_override_parameters of this BuildOutputs.

        :param artifact_override_parameters: The artifact_override_parameters of this BuildOutputs.
        :type: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        self._artifact_override_parameters = artifact_override_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
