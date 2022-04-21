# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallPatchDetails(object):
    """
    The reqeust body while installing a patch to a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallPatchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this InstallPatchDetails.
        :type version: str

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this InstallPatchDetails.
        :type cluster_admin_password: str

        """
        self.swagger_types = {
            'version': 'str',
            'cluster_admin_password': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'cluster_admin_password': 'clusterAdminPassword'
        }

        self._version = None
        self._cluster_admin_password = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this InstallPatchDetails.
        The version of the patch to be installed.


        :return: The version of this InstallPatchDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InstallPatchDetails.
        The version of the patch to be installed.


        :param version: The version of this InstallPatchDetails.
        :type: str
        """
        self._version = version

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this InstallPatchDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this InstallPatchDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this InstallPatchDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this InstallPatchDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
