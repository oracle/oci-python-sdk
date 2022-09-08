# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ArtifactExportDetails(object):
    """
    Details of Artifact source
    """

    #: A constant which can be used with the artifact_source_type property of a ArtifactExportDetails.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE"
    ARTIFACT_SOURCE_TYPE_ORACLE_OBJECT_STORAGE = "ORACLE_OBJECT_STORAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ArtifactExportDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.ArtifactExportDetailsObjectStorage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param artifact_source_type:
            The value to assign to the artifact_source_type property of this ArtifactExportDetails.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE"
        :type artifact_source_type: str

        """
        self.swagger_types = {
            'artifact_source_type': 'str'
        }

        self.attribute_map = {
            'artifact_source_type': 'artifactSourceType'
        }

        self._artifact_source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['artifactSourceType']

        if type == 'ORACLE_OBJECT_STORAGE':
            return 'ArtifactExportDetailsObjectStorage'
        else:
            return 'ArtifactExportDetails'

    @property
    def artifact_source_type(self):
        """
        **[Required]** Gets the artifact_source_type of this ArtifactExportDetails.
        Source type where actually artifact is being stored

        Allowed values for this property are: "ORACLE_OBJECT_STORAGE"


        :return: The artifact_source_type of this ArtifactExportDetails.
        :rtype: str
        """
        return self._artifact_source_type

    @artifact_source_type.setter
    def artifact_source_type(self, artifact_source_type):
        """
        Sets the artifact_source_type of this ArtifactExportDetails.
        Source type where actually artifact is being stored


        :param artifact_source_type: The artifact_source_type of this ArtifactExportDetails.
        :type: str
        """
        allowed_values = ["ORACLE_OBJECT_STORAGE"]
        if not value_allowed_none_or_none_sentinel(artifact_source_type, allowed_values):
            raise ValueError(
                "Invalid value for `artifact_source_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._artifact_source_type = artifact_source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
