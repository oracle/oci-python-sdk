# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .upgrade_deployment_details import UpgradeDeploymentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpgradeDeploymentSpecificReleaseDetails(UpgradeDeploymentDetails):
    """
    Definition of the additional attributes for a Specific Release upgrade.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpgradeDeploymentSpecificReleaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpgradeDeploymentSpecificReleaseDetails.type` attribute
        of this class is ``SPECIFIC_RELEASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpgradeDeploymentSpecificReleaseDetails.
            Allowed values for this property are: "CURRENT_RELEASE", "SPECIFIC_RELEASE"
        :type type: str

        :param ogg_version:
            The value to assign to the ogg_version property of this UpgradeDeploymentSpecificReleaseDetails.
        :type ogg_version: str

        """
        self.swagger_types = {
            'type': 'str',
            'ogg_version': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'ogg_version': 'oggVersion'
        }

        self._type = None
        self._ogg_version = None
        self._type = 'SPECIFIC_RELEASE'

    @property
    def ogg_version(self):
        """
        **[Required]** Gets the ogg_version of this UpgradeDeploymentSpecificReleaseDetails.
        Version of OGG


        :return: The ogg_version of this UpgradeDeploymentSpecificReleaseDetails.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this UpgradeDeploymentSpecificReleaseDetails.
        Version of OGG


        :param ogg_version: The ogg_version of this UpgradeDeploymentSpecificReleaseDetails.
        :type: str
        """
        self._ogg_version = ogg_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
