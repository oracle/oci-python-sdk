# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupPolicy(object):
    """
    The Backup policy for the DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this BackupPolicy.
        :type is_enabled: bool

        :param window_start_time:
            The value to assign to the window_start_time property of this BackupPolicy.
        :type window_start_time: str

        :param retention_in_days:
            The value to assign to the retention_in_days property of this BackupPolicy.
        :type retention_in_days: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BackupPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BackupPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param pitr_policy:
            The value to assign to the pitr_policy property of this BackupPolicy.
        :type pitr_policy: oci.mysql.models.PitrPolicy

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'window_start_time': 'str',
            'retention_in_days': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'pitr_policy': 'PitrPolicy'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'window_start_time': 'windowStartTime',
            'retention_in_days': 'retentionInDays',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'pitr_policy': 'pitrPolicy'
        }

        self._is_enabled = None
        self._window_start_time = None
        self._retention_in_days = None
        self._freeform_tags = None
        self._defined_tags = None
        self._pitr_policy = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this BackupPolicy.
        If automated backups are enabled or disabled.


        :return: The is_enabled of this BackupPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this BackupPolicy.
        If automated backups are enabled or disabled.


        :param is_enabled: The is_enabled of this BackupPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def window_start_time(self):
        """
        **[Required]** Gets the window_start_time of this BackupPolicy.
        The start of a 30-minute window of time in which daily, automated backups occur.

        This should be in the format of the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero.

        At some point in the window, the system may incur a brief service disruption as the backup is performed.

        If not defined, a window is selected from the following Region-based time-spans:
        - eu-frankfurt-1: 20:00 - 04:00 UTC
        - us-ashburn-1: 03:00 - 11:00 UTC
        - uk-london-1: 06:00 - 14:00 UTC
        - ap-tokyo-1: 13:00 - 21:00
        - us-phoenix-1: 06:00 - 14:00


        :return: The window_start_time of this BackupPolicy.
        :rtype: str
        """
        return self._window_start_time

    @window_start_time.setter
    def window_start_time(self, window_start_time):
        """
        Sets the window_start_time of this BackupPolicy.
        The start of a 30-minute window of time in which daily, automated backups occur.

        This should be in the format of the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero.

        At some point in the window, the system may incur a brief service disruption as the backup is performed.

        If not defined, a window is selected from the following Region-based time-spans:
        - eu-frankfurt-1: 20:00 - 04:00 UTC
        - us-ashburn-1: 03:00 - 11:00 UTC
        - uk-london-1: 06:00 - 14:00 UTC
        - ap-tokyo-1: 13:00 - 21:00
        - us-phoenix-1: 06:00 - 14:00


        :param window_start_time: The window_start_time of this BackupPolicy.
        :type: str
        """
        self._window_start_time = window_start_time

    @property
    def retention_in_days(self):
        """
        **[Required]** Gets the retention_in_days of this BackupPolicy.
        The number of days automated backups are retained.


        :return: The retention_in_days of this BackupPolicy.
        :rtype: int
        """
        return self._retention_in_days

    @retention_in_days.setter
    def retention_in_days(self, retention_in_days):
        """
        Sets the retention_in_days of this BackupPolicy.
        The number of days automated backups are retained.


        :param retention_in_days: The retention_in_days of this BackupPolicy.
        :type: int
        """
        self._retention_in_days = retention_in_days

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BackupPolicy.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.

        Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BackupPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BackupPolicy.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.

        Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BackupPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BackupPolicy.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.

        Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BackupPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BackupPolicy.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.

        Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BackupPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def pitr_policy(self):
        """
        Gets the pitr_policy of this BackupPolicy.

        :return: The pitr_policy of this BackupPolicy.
        :rtype: oci.mysql.models.PitrPolicy
        """
        return self._pitr_policy

    @pitr_policy.setter
    def pitr_policy(self, pitr_policy):
        """
        Sets the pitr_policy of this BackupPolicy.

        :param pitr_policy: The pitr_policy of this BackupPolicy.
        :type: oci.mysql.models.PitrPolicy
        """
        self._pitr_policy = pitr_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
