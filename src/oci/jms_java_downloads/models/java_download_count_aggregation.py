# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaDownloadCountAggregation(object):
    """
    Count of Java downloads aggregated by the specified type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JavaDownloadCountAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param download_count:
            The value to assign to the download_count property of this JavaDownloadCountAggregation.
        :type download_count: int

        :param family_version:
            The value to assign to the family_version property of this JavaDownloadCountAggregation.
        :type family_version: str

        :param family_display_name:
            The value to assign to the family_display_name property of this JavaDownloadCountAggregation.
        :type family_display_name: str

        :param release_version:
            The value to assign to the release_version property of this JavaDownloadCountAggregation.
        :type release_version: str

        :param os_family:
            The value to assign to the os_family property of this JavaDownloadCountAggregation.
        :type os_family: str

        :param architecture:
            The value to assign to the architecture property of this JavaDownloadCountAggregation.
        :type architecture: str

        :param package_type:
            The value to assign to the package_type property of this JavaDownloadCountAggregation.
        :type package_type: str

        :param package_type_detail:
            The value to assign to the package_type_detail property of this JavaDownloadCountAggregation.
        :type package_type_detail: str

        """
        self.swagger_types = {
            'download_count': 'int',
            'family_version': 'str',
            'family_display_name': 'str',
            'release_version': 'str',
            'os_family': 'str',
            'architecture': 'str',
            'package_type': 'str',
            'package_type_detail': 'str'
        }
        self.attribute_map = {
            'download_count': 'downloadCount',
            'family_version': 'familyVersion',
            'family_display_name': 'familyDisplayName',
            'release_version': 'releaseVersion',
            'os_family': 'osFamily',
            'architecture': 'architecture',
            'package_type': 'packageType',
            'package_type_detail': 'packageTypeDetail'
        }
        self._download_count = None
        self._family_version = None
        self._family_display_name = None
        self._release_version = None
        self._os_family = None
        self._architecture = None
        self._package_type = None
        self._package_type_detail = None

    @property
    def download_count(self):
        """
        **[Required]** Gets the download_count of this JavaDownloadCountAggregation.
        Count of Java downloads.


        :return: The download_count of this JavaDownloadCountAggregation.
        :rtype: int
        """
        return self._download_count

    @download_count.setter
    def download_count(self, download_count):
        """
        Sets the download_count of this JavaDownloadCountAggregation.
        Count of Java downloads.


        :param download_count: The download_count of this JavaDownloadCountAggregation.
        :type: int
        """
        self._download_count = download_count

    @property
    def family_version(self):
        """
        Gets the family_version of this JavaDownloadCountAggregation.
        The Java family version.


        :return: The family_version of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._family_version

    @family_version.setter
    def family_version(self, family_version):
        """
        Sets the family_version of this JavaDownloadCountAggregation.
        The Java family version.


        :param family_version: The family_version of this JavaDownloadCountAggregation.
        :type: str
        """
        self._family_version = family_version

    @property
    def family_display_name(self):
        """
        Gets the family_display_name of this JavaDownloadCountAggregation.
        The Java family display name.


        :return: The family_display_name of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._family_display_name

    @family_display_name.setter
    def family_display_name(self, family_display_name):
        """
        Sets the family_display_name of this JavaDownloadCountAggregation.
        The Java family display name.


        :param family_display_name: The family_display_name of this JavaDownloadCountAggregation.
        :type: str
        """
        self._family_display_name = family_display_name

    @property
    def release_version(self):
        """
        Gets the release_version of this JavaDownloadCountAggregation.
        The Java release version. Applicable only to `JAVA_RELEASE` aggregationType.


        :return: The release_version of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """
        Sets the release_version of this JavaDownloadCountAggregation.
        The Java release version. Applicable only to `JAVA_RELEASE` aggregationType.


        :param release_version: The release_version of this JavaDownloadCountAggregation.
        :type: str
        """
        self._release_version = release_version

    @property
    def os_family(self):
        """
        Gets the os_family of this JavaDownloadCountAggregation.
        The target Operating System family for the artifact. Applicable only to `PLATFORM` aggregationType.


        :return: The os_family of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this JavaDownloadCountAggregation.
        The target Operating System family for the artifact. Applicable only to `PLATFORM` aggregationType.


        :param os_family: The os_family of this JavaDownloadCountAggregation.
        :type: str
        """
        self._os_family = os_family

    @property
    def architecture(self):
        """
        Gets the architecture of this JavaDownloadCountAggregation.
        The target Operating System architecture for the artifact. Applicable only to `PLATFORM` aggregationType.


        :return: The architecture of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this JavaDownloadCountAggregation.
        The target Operating System architecture for the artifact. Applicable only to `PLATFORM` aggregationType.


        :param architecture: The architecture of this JavaDownloadCountAggregation.
        :type: str
        """
        self._architecture = architecture

    @property
    def package_type(self):
        """
        Gets the package_type of this JavaDownloadCountAggregation.
        The package type (typically the file extension) of the artifact. Applicable only to `PLATFORM` aggregationType.


        :return: The package_type of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this JavaDownloadCountAggregation.
        The package type (typically the file extension) of the artifact. Applicable only to `PLATFORM` aggregationType.


        :param package_type: The package_type of this JavaDownloadCountAggregation.
        :type: str
        """
        self._package_type = package_type

    @property
    def package_type_detail(self):
        """
        Gets the package_type_detail of this JavaDownloadCountAggregation.
        Additional information about the package type. Applicable only to `PLATFORM` aggregationType.


        :return: The package_type_detail of this JavaDownloadCountAggregation.
        :rtype: str
        """
        return self._package_type_detail

    @package_type_detail.setter
    def package_type_detail(self, package_type_detail):
        """
        Sets the package_type_detail of this JavaDownloadCountAggregation.
        Additional information about the package type. Applicable only to `PLATFORM` aggregationType.


        :param package_type_detail: The package_type_detail of this JavaDownloadCountAggregation.
        :type: str
        """
        self._package_type_detail = package_type_detail

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
