# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NewInstallationSite(object):
    """
    The properties of a new Java installation site.
    """

    #: A constant which can be used with the artifact_content_type property of a NewInstallationSite.
    #: This constant has a value of "JDK"
    ARTIFACT_CONTENT_TYPE_JDK = "JDK"

    #: A constant which can be used with the artifact_content_type property of a NewInstallationSite.
    #: This constant has a value of "JRE"
    ARTIFACT_CONTENT_TYPE_JRE = "JRE"

    #: A constant which can be used with the artifact_content_type property of a NewInstallationSite.
    #: This constant has a value of "SERVER_JRE"
    ARTIFACT_CONTENT_TYPE_SERVER_JRE = "SERVER_JRE"

    def __init__(self, **kwargs):
        """
        Initializes a new NewInstallationSite object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this NewInstallationSite.
        :type managed_instance_id: str

        :param release_version:
            The value to assign to the release_version property of this NewInstallationSite.
        :type release_version: str

        :param artifact_content_type:
            The value to assign to the artifact_content_type property of this NewInstallationSite.
            Allowed values for this property are: "JDK", "JRE", "SERVER_JRE"
        :type artifact_content_type: str

        """
        self.swagger_types = {
            'managed_instance_id': 'str',
            'release_version': 'str',
            'artifact_content_type': 'str'
        }

        self.attribute_map = {
            'managed_instance_id': 'managedInstanceId',
            'release_version': 'releaseVersion',
            'artifact_content_type': 'artifactContentType'
        }

        self._managed_instance_id = None
        self._release_version = None
        self._artifact_content_type = None

    @property
    def managed_instance_id(self):
        """
        **[Required]** Gets the managed_instance_id of this NewInstallationSite.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_id of this NewInstallationSite.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this NewInstallationSite.
        The `OCID`__ of the related managed instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_id: The managed_instance_id of this NewInstallationSite.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def release_version(self):
        """
        **[Required]** Gets the release_version of this NewInstallationSite.
        The release version of the Java Runtime.


        :return: The release_version of this NewInstallationSite.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """
        Sets the release_version of this NewInstallationSite.
        The release version of the Java Runtime.


        :param release_version: The release_version of this NewInstallationSite.
        :type: str
        """
        self._release_version = release_version

    @property
    def artifact_content_type(self):
        """
        Gets the artifact_content_type of this NewInstallationSite.
        Artifact content type for the Java version.

        Allowed values for this property are: "JDK", "JRE", "SERVER_JRE"


        :return: The artifact_content_type of this NewInstallationSite.
        :rtype: str
        """
        return self._artifact_content_type

    @artifact_content_type.setter
    def artifact_content_type(self, artifact_content_type):
        """
        Sets the artifact_content_type of this NewInstallationSite.
        Artifact content type for the Java version.


        :param artifact_content_type: The artifact_content_type of this NewInstallationSite.
        :type: str
        """
        allowed_values = ["JDK", "JRE", "SERVER_JRE"]
        if not value_allowed_none_or_none_sentinel(artifact_content_type, allowed_values):
            raise ValueError(
                "Invalid value for `artifact_content_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._artifact_content_type = artifact_content_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
