# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockchainPlatformPatchSummary(object):
    """
    Patch Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BlockchainPlatformPatchSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BlockchainPlatformPatchSummary.
        :type id: str

        :param service_version:
            The value to assign to the service_version property of this BlockchainPlatformPatchSummary.
        :type service_version: str

        :param patch_info_url:
            The value to assign to the patch_info_url property of this BlockchainPlatformPatchSummary.
        :type patch_info_url: str

        :param time_patch_due:
            The value to assign to the time_patch_due property of this BlockchainPlatformPatchSummary.
        :type time_patch_due: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'service_version': 'str',
            'patch_info_url': 'str',
            'time_patch_due': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'service_version': 'serviceVersion',
            'patch_info_url': 'patchInfoUrl',
            'time_patch_due': 'timePatchDue'
        }

        self._id = None
        self._service_version = None
        self._patch_info_url = None
        self._time_patch_due = None

    @property
    def id(self):
        """
        Gets the id of this BlockchainPlatformPatchSummary.
        patch id


        :return: The id of this BlockchainPlatformPatchSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlockchainPlatformPatchSummary.
        patch id


        :param id: The id of this BlockchainPlatformPatchSummary.
        :type: str
        """
        self._id = id

    @property
    def service_version(self):
        """
        Gets the service_version of this BlockchainPlatformPatchSummary.
        patch service version


        :return: The service_version of this BlockchainPlatformPatchSummary.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """
        Sets the service_version of this BlockchainPlatformPatchSummary.
        patch service version


        :param service_version: The service_version of this BlockchainPlatformPatchSummary.
        :type: str
        """
        self._service_version = service_version

    @property
    def patch_info_url(self):
        """
        Gets the patch_info_url of this BlockchainPlatformPatchSummary.
        A URL for the patch specific documentation


        :return: The patch_info_url of this BlockchainPlatformPatchSummary.
        :rtype: str
        """
        return self._patch_info_url

    @patch_info_url.setter
    def patch_info_url(self, patch_info_url):
        """
        Sets the patch_info_url of this BlockchainPlatformPatchSummary.
        A URL for the patch specific documentation


        :param patch_info_url: The patch_info_url of this BlockchainPlatformPatchSummary.
        :type: str
        """
        self._patch_info_url = patch_info_url

    @property
    def time_patch_due(self):
        """
        Gets the time_patch_due of this BlockchainPlatformPatchSummary.
        patch due date for customer initiated patching


        :return: The time_patch_due of this BlockchainPlatformPatchSummary.
        :rtype: datetime
        """
        return self._time_patch_due

    @time_patch_due.setter
    def time_patch_due(self, time_patch_due):
        """
        Sets the time_patch_due of this BlockchainPlatformPatchSummary.
        patch due date for customer initiated patching


        :param time_patch_due: The time_patch_due of this BlockchainPlatformPatchSummary.
        :type: datetime
        """
        self._time_patch_due = time_patch_due

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
