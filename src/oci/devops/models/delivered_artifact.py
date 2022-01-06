# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeliveredArtifact(object):
    """
    Details of the artifacts delivered through the Deliver Artifacts stage.
    """

    #: A constant which can be used with the artifact_type property of a DeliveredArtifact.
    #: This constant has a value of "GENERIC_ARTIFACT"
    ARTIFACT_TYPE_GENERIC_ARTIFACT = "GENERIC_ARTIFACT"

    #: A constant which can be used with the artifact_type property of a DeliveredArtifact.
    #: This constant has a value of "OCIR"
    ARTIFACT_TYPE_OCIR = "OCIR"

    def __init__(self, **kwargs):
        """
        Initializes a new DeliveredArtifact object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ContainerRegistryDeliveredArtifact`
        * :class:`~oci.devops.models.GenericDeliveredArtifact`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_id:
            The value to assign to the deploy_artifact_id property of this DeliveredArtifact.
        :type deploy_artifact_id: str

        :param output_artifact_name:
            The value to assign to the output_artifact_name property of this DeliveredArtifact.
        :type output_artifact_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this DeliveredArtifact.
            Allowed values for this property are: "GENERIC_ARTIFACT", "OCIR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type artifact_type: str

        """
        self.swagger_types = {
            'deploy_artifact_id': 'str',
            'output_artifact_name': 'str',
            'artifact_type': 'str'
        }

        self.attribute_map = {
            'deploy_artifact_id': 'deployArtifactId',
            'output_artifact_name': 'outputArtifactName',
            'artifact_type': 'artifactType'
        }

        self._deploy_artifact_id = None
        self._output_artifact_name = None
        self._artifact_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['artifactType']

        if type == 'OCIR':
            return 'ContainerRegistryDeliveredArtifact'

        if type == 'GENERIC_ARTIFACT':
            return 'GenericDeliveredArtifact'
        else:
            return 'DeliveredArtifact'

    @property
    def deploy_artifact_id(self):
        """
        **[Required]** Gets the deploy_artifact_id of this DeliveredArtifact.
        The OCID of the deployment artifact definition.


        :return: The deploy_artifact_id of this DeliveredArtifact.
        :rtype: str
        """
        return self._deploy_artifact_id

    @deploy_artifact_id.setter
    def deploy_artifact_id(self, deploy_artifact_id):
        """
        Sets the deploy_artifact_id of this DeliveredArtifact.
        The OCID of the deployment artifact definition.


        :param deploy_artifact_id: The deploy_artifact_id of this DeliveredArtifact.
        :type: str
        """
        self._deploy_artifact_id = deploy_artifact_id

    @property
    def output_artifact_name(self):
        """
        **[Required]** Gets the output_artifact_name of this DeliveredArtifact.
        Name of the output artifact defined in the build specification file.


        :return: The output_artifact_name of this DeliveredArtifact.
        :rtype: str
        """
        return self._output_artifact_name

    @output_artifact_name.setter
    def output_artifact_name(self, output_artifact_name):
        """
        Sets the output_artifact_name of this DeliveredArtifact.
        Name of the output artifact defined in the build specification file.


        :param output_artifact_name: The output_artifact_name of this DeliveredArtifact.
        :type: str
        """
        self._output_artifact_name = output_artifact_name

    @property
    def artifact_type(self):
        """
        **[Required]** Gets the artifact_type of this DeliveredArtifact.
        Type of artifact delivered.

        Allowed values for this property are: "GENERIC_ARTIFACT", "OCIR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The artifact_type of this DeliveredArtifact.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """
        Sets the artifact_type of this DeliveredArtifact.
        Type of artifact delivered.


        :param artifact_type: The artifact_type of this DeliveredArtifact.
        :type: str
        """
        allowed_values = ["GENERIC_ARTIFACT", "OCIR"]
        if not value_allowed_none_or_none_sentinel(artifact_type, allowed_values):
            artifact_type = 'UNKNOWN_ENUM_VALUE'
        self._artifact_type = artifact_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
