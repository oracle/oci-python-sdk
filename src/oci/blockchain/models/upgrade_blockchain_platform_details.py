# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpgradeBlockchainPlatformDetails(object):
    """
    Input payload to upgrade the blockchain platform.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpgradeBlockchainPlatformDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patch_id:
            The value to assign to the patch_id property of this UpgradeBlockchainPlatformDetails.
        :type patch_id: str

        """
        self.swagger_types = {
            'patch_id': 'str'
        }

        self.attribute_map = {
            'patch_id': 'patchId'
        }

        self._patch_id = None

    @property
    def patch_id(self):
        """
        **[Required]** Gets the patch_id of this UpgradeBlockchainPlatformDetails.
        The patch ID corresponding to the version to which platform will be upgraded.


        :return: The patch_id of this UpgradeBlockchainPlatformDetails.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this UpgradeBlockchainPlatformDetails.
        The patch ID corresponding to the version to which platform will be upgraded.


        :param patch_id: The patch_id of this UpgradeBlockchainPlatformDetails.
        :type: str
        """
        self._patch_id = patch_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
