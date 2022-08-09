# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaArtifact(object):
    """
    Information about a binary artifact of Java.
    """

    #: A constant which can be used with the artifact_content_type property of a JavaArtifact.
    #: This constant has a value of "JDK"
    ARTIFACT_CONTENT_TYPE_JDK = "JDK"

    #: A constant which can be used with the artifact_content_type property of a JavaArtifact.
    #: This constant has a value of "JRE"
    ARTIFACT_CONTENT_TYPE_JRE = "JRE"

    #: A constant which can be used with the artifact_content_type property of a JavaArtifact.
    #: This constant has a value of "SERVER_JRE"
    ARTIFACT_CONTENT_TYPE_SERVER_JRE = "SERVER_JRE"

    def __init__(self, **kwargs):
        """
        Initializes a new JavaArtifact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param artifact_id:
            The value to assign to the artifact_id property of this JavaArtifact.
        :type artifact_id: int

        :param artifact_description:
            The value to assign to the artifact_description property of this JavaArtifact.
        :type artifact_description: str

        :param artifact_content_type:
            The value to assign to the artifact_content_type property of this JavaArtifact.
            Allowed values for this property are: "JDK", "JRE", "SERVER_JRE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type artifact_content_type: str

        :param approximate_file_size_in_bytes:
            The value to assign to the approximate_file_size_in_bytes property of this JavaArtifact.
        :type approximate_file_size_in_bytes: int

        :param sha256:
            The value to assign to the sha256 property of this JavaArtifact.
        :type sha256: str

        """
        self.swagger_types = {
            'artifact_id': 'int',
            'artifact_description': 'str',
            'artifact_content_type': 'str',
            'approximate_file_size_in_bytes': 'int',
            'sha256': 'str'
        }

        self.attribute_map = {
            'artifact_id': 'artifactId',
            'artifact_description': 'artifactDescription',
            'artifact_content_type': 'artifactContentType',
            'approximate_file_size_in_bytes': 'approximateFileSizeInBytes',
            'sha256': 'sha256'
        }

        self._artifact_id = None
        self._artifact_description = None
        self._artifact_content_type = None
        self._approximate_file_size_in_bytes = None
        self._sha256 = None

    @property
    def artifact_id(self):
        """
        **[Required]** Gets the artifact_id of this JavaArtifact.
        Unique identifier for the artifact.


        :return: The artifact_id of this JavaArtifact.
        :rtype: int
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this JavaArtifact.
        Unique identifier for the artifact.


        :param artifact_id: The artifact_id of this JavaArtifact.
        :type: int
        """
        self._artifact_id = artifact_id

    @property
    def artifact_description(self):
        """
        **[Required]** Gets the artifact_description of this JavaArtifact.
        Description of the binary artifact. Typically includes the OS, architecture, and installer type.


        :return: The artifact_description of this JavaArtifact.
        :rtype: str
        """
        return self._artifact_description

    @artifact_description.setter
    def artifact_description(self, artifact_description):
        """
        Sets the artifact_description of this JavaArtifact.
        Description of the binary artifact. Typically includes the OS, architecture, and installer type.


        :param artifact_description: The artifact_description of this JavaArtifact.
        :type: str
        """
        self._artifact_description = artifact_description

    @property
    def artifact_content_type(self):
        """
        **[Required]** Gets the artifact_content_type of this JavaArtifact.
        Product content type of this artifact.

        Allowed values for this property are: "JDK", "JRE", "SERVER_JRE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The artifact_content_type of this JavaArtifact.
        :rtype: str
        """
        return self._artifact_content_type

    @artifact_content_type.setter
    def artifact_content_type(self, artifact_content_type):
        """
        Sets the artifact_content_type of this JavaArtifact.
        Product content type of this artifact.


        :param artifact_content_type: The artifact_content_type of this JavaArtifact.
        :type: str
        """
        allowed_values = ["JDK", "JRE", "SERVER_JRE"]
        if not value_allowed_none_or_none_sentinel(artifact_content_type, allowed_values):
            artifact_content_type = 'UNKNOWN_ENUM_VALUE'
        self._artifact_content_type = artifact_content_type

    @property
    def approximate_file_size_in_bytes(self):
        """
        **[Required]** Gets the approximate_file_size_in_bytes of this JavaArtifact.
        Approximate compressed file size in bytes.


        :return: The approximate_file_size_in_bytes of this JavaArtifact.
        :rtype: int
        """
        return self._approximate_file_size_in_bytes

    @approximate_file_size_in_bytes.setter
    def approximate_file_size_in_bytes(self, approximate_file_size_in_bytes):
        """
        Sets the approximate_file_size_in_bytes of this JavaArtifact.
        Approximate compressed file size in bytes.


        :param approximate_file_size_in_bytes: The approximate_file_size_in_bytes of this JavaArtifact.
        :type: int
        """
        self._approximate_file_size_in_bytes = approximate_file_size_in_bytes

    @property
    def sha256(self):
        """
        **[Required]** Gets the sha256 of this JavaArtifact.
        SHA256 checksum of the artifact.


        :return: The sha256 of this JavaArtifact.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """
        Sets the sha256 of this JavaArtifact.
        SHA256 checksum of the artifact.


        :param sha256: The sha256 of this JavaArtifact.
        :type: str
        """
        self._sha256 = sha256

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
