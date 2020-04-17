# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwarePackageSummary(object):
    """
    Summary information for a software package
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwarePackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this SoftwarePackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this SoftwarePackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this SoftwarePackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this SoftwarePackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this SoftwarePackageSummary.
        :type architecture: str

        :param checksum:
            The value to assign to the checksum property of this SoftwarePackageSummary.
        :type checksum: str

        :param checksum_type:
            The value to assign to the checksum_type property of this SoftwarePackageSummary.
        :type checksum_type: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'checksum': 'str',
            'checksum_type': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'checksum': 'checksum',
            'checksum_type': 'checksumType'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._checksum = None
        self._checksum_type = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwarePackageSummary.
        Package name


        :return: The display_name of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwarePackageSummary.
        Package name


        :param display_name: The display_name of this SoftwarePackageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SoftwarePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID


        :return: The name of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SoftwarePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID


        :param name: The name of this SoftwarePackageSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SoftwarePackageSummary.
        Type of the package


        :return: The type of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SoftwarePackageSummary.
        Type of the package


        :param type: The type of this SoftwarePackageSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SoftwarePackageSummary.
        Version of the package


        :return: The version of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SoftwarePackageSummary.
        Version of the package


        :param version: The version of this SoftwarePackageSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this SoftwarePackageSummary.
        the architecture for which this software was built


        :return: The architecture of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this SoftwarePackageSummary.
        the architecture for which this software was built


        :param architecture: The architecture of this SoftwarePackageSummary.
        :type: str
        """
        self._architecture = architecture

    @property
    def checksum(self):
        """
        Gets the checksum of this SoftwarePackageSummary.
        checksum of the package


        :return: The checksum of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this SoftwarePackageSummary.
        checksum of the package


        :param checksum: The checksum of this SoftwarePackageSummary.
        :type: str
        """
        self._checksum = checksum

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this SoftwarePackageSummary.
        type of the checksum


        :return: The checksum_type of this SoftwarePackageSummary.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this SoftwarePackageSummary.
        type of the checksum


        :param checksum_type: The checksum_type of this SoftwarePackageSummary.
        :type: str
        """
        self._checksum_type = checksum_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
