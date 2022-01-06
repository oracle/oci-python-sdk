# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SupportedVmwareSoftwareVersionSummary(object):
    """
    A specific version of bundled VMware software supported by the Oracle Cloud
    VMware Solution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SupportedVmwareSoftwareVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this SupportedVmwareSoftwareVersionSummary.
        :type version: str

        :param description:
            The value to assign to the description property of this SupportedVmwareSoftwareVersionSummary.
        :type description: str

        """
        self.swagger_types = {
            'version': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'description': 'description'
        }

        self._version = None
        self._description = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this SupportedVmwareSoftwareVersionSummary.
        A short, unique string that identifies the version of bundled software.


        :return: The version of this SupportedVmwareSoftwareVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SupportedVmwareSoftwareVersionSummary.
        A short, unique string that identifies the version of bundled software.


        :param version: The version of this SupportedVmwareSoftwareVersionSummary.
        :type: str
        """
        self._version = version

    @property
    def description(self):
        """
        **[Required]** Gets the description of this SupportedVmwareSoftwareVersionSummary.
        A description of the software in the bundle.


        :return: The description of this SupportedVmwareSoftwareVersionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SupportedVmwareSoftwareVersionSummary.
        A description of the software in the bundle.


        :param description: The description of this SupportedVmwareSoftwareVersionSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
