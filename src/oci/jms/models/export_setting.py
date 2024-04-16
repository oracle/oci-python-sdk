# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportSetting(object):
    """
    An export settings for JMS fleets.
    """

    #: A constant which can be used with the export_duration property of a ExportSetting.
    #: This constant has a value of "LAST_30_DAYS"
    EXPORT_DURATION_LAST_30_DAYS = "LAST_30_DAYS"

    #: A constant which can be used with the export_duration property of a ExportSetting.
    #: This constant has a value of "LAST_60_DAYS"
    EXPORT_DURATION_LAST_60_DAYS = "LAST_60_DAYS"

    #: A constant which can be used with the export_duration property of a ExportSetting.
    #: This constant has a value of "LAST_90_DAYS"
    EXPORT_DURATION_LAST_90_DAYS = "LAST_90_DAYS"

    #: A constant which can be used with the export_resources property of a ExportSetting.
    #: This constant has a value of "MANAGED_INSTANCE"
    EXPORT_RESOURCES_MANAGED_INSTANCE = "MANAGED_INSTANCE"

    #: A constant which can be used with the export_resources property of a ExportSetting.
    #: This constant has a value of "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME"
    EXPORT_RESOURCES_MANAGED_INSTANCE_PLUS_JAVA_RUNTIME = "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME"

    #: A constant which can be used with the export_resources property of a ExportSetting.
    #: This constant has a value of "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION"
    EXPORT_RESOURCES_MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION = "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION"

    #: A constant which can be used with the export_frequency property of a ExportSetting.
    #: This constant has a value of "DAILY"
    EXPORT_FREQUENCY_DAILY = "DAILY"

    #: A constant which can be used with the export_frequency property of a ExportSetting.
    #: This constant has a value of "WEEKLY"
    EXPORT_FREQUENCY_WEEKLY = "WEEKLY"

    #: A constant which can be used with the export_frequency property of a ExportSetting.
    #: This constant has a value of "MONTHLY"
    EXPORT_FREQUENCY_MONTHLY = "MONTHLY"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportSetting object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_setting_key:
            The value to assign to the export_setting_key property of this ExportSetting.
        :type export_setting_key: str

        :param fleet_id:
            The value to assign to the fleet_id property of this ExportSetting.
        :type fleet_id: str

        :param export_duration:
            The value to assign to the export_duration property of this ExportSetting.
            Allowed values for this property are: "LAST_30_DAYS", "LAST_60_DAYS", "LAST_90_DAYS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type export_duration: str

        :param export_resources:
            The value to assign to the export_resources property of this ExportSetting.
            Allowed values for this property are: "MANAGED_INSTANCE", "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME", "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type export_resources: str

        :param is_cross_region_acknowledged:
            The value to assign to the is_cross_region_acknowledged property of this ExportSetting.
        :type is_cross_region_acknowledged: bool

        :param target_bucket_name:
            The value to assign to the target_bucket_name property of this ExportSetting.
        :type target_bucket_name: str

        :param target_bucket_namespace:
            The value to assign to the target_bucket_namespace property of this ExportSetting.
        :type target_bucket_namespace: str

        :param target_bucket_region:
            The value to assign to the target_bucket_region property of this ExportSetting.
        :type target_bucket_region: str

        :param export_frequency:
            The value to assign to the export_frequency property of this ExportSetting.
            Allowed values for this property are: "DAILY", "WEEKLY", "MONTHLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type export_frequency: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ExportSetting.
        :type is_enabled: bool

        :param time_created:
            The value to assign to the time_created property of this ExportSetting.
        :type time_created: datetime

        :param time_last_modified:
            The value to assign to the time_last_modified property of this ExportSetting.
        :type time_last_modified: datetime

        """
        self.swagger_types = {
            'export_setting_key': 'str',
            'fleet_id': 'str',
            'export_duration': 'str',
            'export_resources': 'str',
            'is_cross_region_acknowledged': 'bool',
            'target_bucket_name': 'str',
            'target_bucket_namespace': 'str',
            'target_bucket_region': 'str',
            'export_frequency': 'str',
            'is_enabled': 'bool',
            'time_created': 'datetime',
            'time_last_modified': 'datetime'
        }

        self.attribute_map = {
            'export_setting_key': 'exportSettingKey',
            'fleet_id': 'fleetId',
            'export_duration': 'exportDuration',
            'export_resources': 'exportResources',
            'is_cross_region_acknowledged': 'isCrossRegionAcknowledged',
            'target_bucket_name': 'targetBucketName',
            'target_bucket_namespace': 'targetBucketNamespace',
            'target_bucket_region': 'targetBucketRegion',
            'export_frequency': 'exportFrequency',
            'is_enabled': 'isEnabled',
            'time_created': 'timeCreated',
            'time_last_modified': 'timeLastModified'
        }

        self._export_setting_key = None
        self._fleet_id = None
        self._export_duration = None
        self._export_resources = None
        self._is_cross_region_acknowledged = None
        self._target_bucket_name = None
        self._target_bucket_namespace = None
        self._target_bucket_region = None
        self._export_frequency = None
        self._is_enabled = None
        self._time_created = None
        self._time_last_modified = None

    @property
    def export_setting_key(self):
        """
        Gets the export_setting_key of this ExportSetting.
        The internal identifier of the export setting.


        :return: The export_setting_key of this ExportSetting.
        :rtype: str
        """
        return self._export_setting_key

    @export_setting_key.setter
    def export_setting_key(self, export_setting_key):
        """
        Sets the export_setting_key of this ExportSetting.
        The internal identifier of the export setting.


        :param export_setting_key: The export_setting_key of this ExportSetting.
        :type: str
        """
        self._export_setting_key = export_setting_key

    @property
    def fleet_id(self):
        """
        Gets the fleet_id of this ExportSetting.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this ExportSetting.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this ExportSetting.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this ExportSetting.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def export_duration(self):
        """
        Gets the export_duration of this ExportSetting.
        The duration of data to be exported for fleets.

        Allowed values for this property are: "LAST_30_DAYS", "LAST_60_DAYS", "LAST_90_DAYS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The export_duration of this ExportSetting.
        :rtype: str
        """
        return self._export_duration

    @export_duration.setter
    def export_duration(self, export_duration):
        """
        Sets the export_duration of this ExportSetting.
        The duration of data to be exported for fleets.


        :param export_duration: The export_duration of this ExportSetting.
        :type: str
        """
        allowed_values = ["LAST_30_DAYS", "LAST_60_DAYS", "LAST_90_DAYS"]
        if not value_allowed_none_or_none_sentinel(export_duration, allowed_values):
            export_duration = 'UNKNOWN_ENUM_VALUE'
        self._export_duration = export_duration

    @property
    def export_resources(self):
        """
        Gets the export_resources of this ExportSetting.
        Resource to export data associated from the fleets.

        Allowed values for this property are: "MANAGED_INSTANCE", "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME", "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The export_resources of this ExportSetting.
        :rtype: str
        """
        return self._export_resources

    @export_resources.setter
    def export_resources(self, export_resources):
        """
        Sets the export_resources of this ExportSetting.
        Resource to export data associated from the fleets.


        :param export_resources: The export_resources of this ExportSetting.
        :type: str
        """
        allowed_values = ["MANAGED_INSTANCE", "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME", "MANAGED_INSTANCE_PLUS_JAVA_RUNTIME_PLUS_APPLICATION"]
        if not value_allowed_none_or_none_sentinel(export_resources, allowed_values):
            export_resources = 'UNKNOWN_ENUM_VALUE'
        self._export_resources = export_resources

    @property
    def is_cross_region_acknowledged(self):
        """
        Gets the is_cross_region_acknowledged of this ExportSetting.
        Acknowledgement for cross region target bucket configuration.


        :return: The is_cross_region_acknowledged of this ExportSetting.
        :rtype: bool
        """
        return self._is_cross_region_acknowledged

    @is_cross_region_acknowledged.setter
    def is_cross_region_acknowledged(self, is_cross_region_acknowledged):
        """
        Sets the is_cross_region_acknowledged of this ExportSetting.
        Acknowledgement for cross region target bucket configuration.


        :param is_cross_region_acknowledged: The is_cross_region_acknowledged of this ExportSetting.
        :type: bool
        """
        self._is_cross_region_acknowledged = is_cross_region_acknowledged

    @property
    def target_bucket_name(self):
        """
        Gets the target_bucket_name of this ExportSetting.
        The name of the bucket where data will be exported.


        :return: The target_bucket_name of this ExportSetting.
        :rtype: str
        """
        return self._target_bucket_name

    @target_bucket_name.setter
    def target_bucket_name(self, target_bucket_name):
        """
        Sets the target_bucket_name of this ExportSetting.
        The name of the bucket where data will be exported.


        :param target_bucket_name: The target_bucket_name of this ExportSetting.
        :type: str
        """
        self._target_bucket_name = target_bucket_name

    @property
    def target_bucket_namespace(self):
        """
        Gets the target_bucket_namespace of this ExportSetting.
        The namespace of the bucket where data will be exported.


        :return: The target_bucket_namespace of this ExportSetting.
        :rtype: str
        """
        return self._target_bucket_namespace

    @target_bucket_namespace.setter
    def target_bucket_namespace(self, target_bucket_namespace):
        """
        Sets the target_bucket_namespace of this ExportSetting.
        The namespace of the bucket where data will be exported.


        :param target_bucket_namespace: The target_bucket_namespace of this ExportSetting.
        :type: str
        """
        self._target_bucket_namespace = target_bucket_namespace

    @property
    def target_bucket_region(self):
        """
        Gets the target_bucket_region of this ExportSetting.
        The namespace of the bucket where data will be exported.


        :return: The target_bucket_region of this ExportSetting.
        :rtype: str
        """
        return self._target_bucket_region

    @target_bucket_region.setter
    def target_bucket_region(self, target_bucket_region):
        """
        Sets the target_bucket_region of this ExportSetting.
        The namespace of the bucket where data will be exported.


        :param target_bucket_region: The target_bucket_region of this ExportSetting.
        :type: str
        """
        self._target_bucket_region = target_bucket_region

    @property
    def export_frequency(self):
        """
        Gets the export_frequency of this ExportSetting.
        Schedule at which data will be exported.

        Allowed values for this property are: "DAILY", "WEEKLY", "MONTHLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The export_frequency of this ExportSetting.
        :rtype: str
        """
        return self._export_frequency

    @export_frequency.setter
    def export_frequency(self, export_frequency):
        """
        Sets the export_frequency of this ExportSetting.
        Schedule at which data will be exported.


        :param export_frequency: The export_frequency of this ExportSetting.
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY", "MONTHLY"]
        if not value_allowed_none_or_none_sentinel(export_frequency, allowed_values):
            export_frequency = 'UNKNOWN_ENUM_VALUE'
        self._export_frequency = export_frequency

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ExportSetting.
        ExportSetting flag to store enabled or disabled status.


        :return: The is_enabled of this ExportSetting.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ExportSetting.
        ExportSetting flag to store enabled or disabled status.


        :param is_enabled: The is_enabled of this ExportSetting.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def time_created(self):
        """
        Gets the time_created of this ExportSetting.
        The creation date and time of the export setting (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this ExportSetting.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExportSetting.
        The creation date and time of the export setting (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this ExportSetting.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this ExportSetting.
        The update date and time of the export setting (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_last_modified of this ExportSetting.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this ExportSetting.
        The update date and time of the export setting (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_last_modified: The time_last_modified of this ExportSetting.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other