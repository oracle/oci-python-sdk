# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbVersionSummary(object):
    """
    The Oracle Database software version.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this DbVersionSummary.
        :type version: str

        :param is_latest_for_major_version:
            The value to assign to the is_latest_for_major_version property of this DbVersionSummary.
        :type is_latest_for_major_version: bool

        :param supports_pdb:
            The value to assign to the supports_pdb property of this DbVersionSummary.
        :type supports_pdb: bool

        :param is_preview_db_version:
            The value to assign to the is_preview_db_version property of this DbVersionSummary.
        :type is_preview_db_version: bool

        :param is_upgrade_supported:
            The value to assign to the is_upgrade_supported property of this DbVersionSummary.
        :type is_upgrade_supported: bool

        """
        self.swagger_types = {
            'version': 'str',
            'is_latest_for_major_version': 'bool',
            'supports_pdb': 'bool',
            'is_preview_db_version': 'bool',
            'is_upgrade_supported': 'bool'
        }

        self.attribute_map = {
            'version': 'version',
            'is_latest_for_major_version': 'isLatestForMajorVersion',
            'supports_pdb': 'supportsPdb',
            'is_preview_db_version': 'isPreviewDbVersion',
            'is_upgrade_supported': 'isUpgradeSupported'
        }

        self._version = None
        self._is_latest_for_major_version = None
        self._supports_pdb = None
        self._is_preview_db_version = None
        self._is_upgrade_supported = None

    @property
    def version(self):
        """
        **[Required]** Gets the version of this DbVersionSummary.
        A valid Oracle Database version.


        :return: The version of this DbVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DbVersionSummary.
        A valid Oracle Database version.


        :param version: The version of this DbVersionSummary.
        :type: str
        """
        self._version = version

    @property
    def is_latest_for_major_version(self):
        """
        Gets the is_latest_for_major_version of this DbVersionSummary.
        True if this version of the Oracle Database software is the latest version for a release.


        :return: The is_latest_for_major_version of this DbVersionSummary.
        :rtype: bool
        """
        return self._is_latest_for_major_version

    @is_latest_for_major_version.setter
    def is_latest_for_major_version(self, is_latest_for_major_version):
        """
        Sets the is_latest_for_major_version of this DbVersionSummary.
        True if this version of the Oracle Database software is the latest version for a release.


        :param is_latest_for_major_version: The is_latest_for_major_version of this DbVersionSummary.
        :type: bool
        """
        self._is_latest_for_major_version = is_latest_for_major_version

    @property
    def supports_pdb(self):
        """
        Gets the supports_pdb of this DbVersionSummary.
        True if this version of the Oracle Database software supports pluggable databases.


        :return: The supports_pdb of this DbVersionSummary.
        :rtype: bool
        """
        return self._supports_pdb

    @supports_pdb.setter
    def supports_pdb(self, supports_pdb):
        """
        Sets the supports_pdb of this DbVersionSummary.
        True if this version of the Oracle Database software supports pluggable databases.


        :param supports_pdb: The supports_pdb of this DbVersionSummary.
        :type: bool
        """
        self._supports_pdb = supports_pdb

    @property
    def is_preview_db_version(self):
        """
        Gets the is_preview_db_version of this DbVersionSummary.
        True if this version of the Oracle Database software is the preview version.


        :return: The is_preview_db_version of this DbVersionSummary.
        :rtype: bool
        """
        return self._is_preview_db_version

    @is_preview_db_version.setter
    def is_preview_db_version(self, is_preview_db_version):
        """
        Sets the is_preview_db_version of this DbVersionSummary.
        True if this version of the Oracle Database software is the preview version.


        :param is_preview_db_version: The is_preview_db_version of this DbVersionSummary.
        :type: bool
        """
        self._is_preview_db_version = is_preview_db_version

    @property
    def is_upgrade_supported(self):
        """
        Gets the is_upgrade_supported of this DbVersionSummary.
        True if this version of the Oracle Database software is supported for Upgrade.


        :return: The is_upgrade_supported of this DbVersionSummary.
        :rtype: bool
        """
        return self._is_upgrade_supported

    @is_upgrade_supported.setter
    def is_upgrade_supported(self, is_upgrade_supported):
        """
        Sets the is_upgrade_supported of this DbVersionSummary.
        True if this version of the Oracle Database software is supported for Upgrade.


        :param is_upgrade_supported: The is_upgrade_supported of this DbVersionSummary.
        :type: bool
        """
        self._is_upgrade_supported = is_upgrade_supported

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
