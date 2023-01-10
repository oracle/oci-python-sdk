# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetAdvancedFeatureConfiguration(object):
    """
    Advanced feature metadata for the fleet
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FleetAdvancedFeatureConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param analytic_namespace:
            The value to assign to the analytic_namespace property of this FleetAdvancedFeatureConfiguration.
        :type analytic_namespace: str

        :param analytic_bucket_name:
            The value to assign to the analytic_bucket_name property of this FleetAdvancedFeatureConfiguration.
        :type analytic_bucket_name: str

        :param lcm:
            The value to assign to the lcm property of this FleetAdvancedFeatureConfiguration.
        :type lcm: oci.jms.models.Lcm

        :param crypto_event_analysis:
            The value to assign to the crypto_event_analysis property of this FleetAdvancedFeatureConfiguration.
        :type crypto_event_analysis: oci.jms.models.CryptoEventAnalysis

        :param advanced_usage_tracking:
            The value to assign to the advanced_usage_tracking property of this FleetAdvancedFeatureConfiguration.
        :type advanced_usage_tracking: oci.jms.models.AdvancedUsageTracking

        :param jfr_recording:
            The value to assign to the jfr_recording property of this FleetAdvancedFeatureConfiguration.
        :type jfr_recording: oci.jms.models.JfrRecording

        :param time_last_modified:
            The value to assign to the time_last_modified property of this FleetAdvancedFeatureConfiguration.
        :type time_last_modified: datetime

        """
        self.swagger_types = {
            'analytic_namespace': 'str',
            'analytic_bucket_name': 'str',
            'lcm': 'Lcm',
            'crypto_event_analysis': 'CryptoEventAnalysis',
            'advanced_usage_tracking': 'AdvancedUsageTracking',
            'jfr_recording': 'JfrRecording',
            'time_last_modified': 'datetime'
        }

        self.attribute_map = {
            'analytic_namespace': 'analyticNamespace',
            'analytic_bucket_name': 'analyticBucketName',
            'lcm': 'lcm',
            'crypto_event_analysis': 'cryptoEventAnalysis',
            'advanced_usage_tracking': 'advancedUsageTracking',
            'jfr_recording': 'jfrRecording',
            'time_last_modified': 'timeLastModified'
        }

        self._analytic_namespace = None
        self._analytic_bucket_name = None
        self._lcm = None
        self._crypto_event_analysis = None
        self._advanced_usage_tracking = None
        self._jfr_recording = None
        self._time_last_modified = None

    @property
    def analytic_namespace(self):
        """
        **[Required]** Gets the analytic_namespace of this FleetAdvancedFeatureConfiguration.
        Namespace for the fleet advanced feature


        :return: The analytic_namespace of this FleetAdvancedFeatureConfiguration.
        :rtype: str
        """
        return self._analytic_namespace

    @analytic_namespace.setter
    def analytic_namespace(self, analytic_namespace):
        """
        Sets the analytic_namespace of this FleetAdvancedFeatureConfiguration.
        Namespace for the fleet advanced feature


        :param analytic_namespace: The analytic_namespace of this FleetAdvancedFeatureConfiguration.
        :type: str
        """
        self._analytic_namespace = analytic_namespace

    @property
    def analytic_bucket_name(self):
        """
        **[Required]** Gets the analytic_bucket_name of this FleetAdvancedFeatureConfiguration.
        Bucket name required to store jfr and related data


        :return: The analytic_bucket_name of this FleetAdvancedFeatureConfiguration.
        :rtype: str
        """
        return self._analytic_bucket_name

    @analytic_bucket_name.setter
    def analytic_bucket_name(self, analytic_bucket_name):
        """
        Sets the analytic_bucket_name of this FleetAdvancedFeatureConfiguration.
        Bucket name required to store jfr and related data


        :param analytic_bucket_name: The analytic_bucket_name of this FleetAdvancedFeatureConfiguration.
        :type: str
        """
        self._analytic_bucket_name = analytic_bucket_name

    @property
    def lcm(self):
        """
        **[Required]** Gets the lcm of this FleetAdvancedFeatureConfiguration.

        :return: The lcm of this FleetAdvancedFeatureConfiguration.
        :rtype: oci.jms.models.Lcm
        """
        return self._lcm

    @lcm.setter
    def lcm(self, lcm):
        """
        Sets the lcm of this FleetAdvancedFeatureConfiguration.

        :param lcm: The lcm of this FleetAdvancedFeatureConfiguration.
        :type: oci.jms.models.Lcm
        """
        self._lcm = lcm

    @property
    def crypto_event_analysis(self):
        """
        **[Required]** Gets the crypto_event_analysis of this FleetAdvancedFeatureConfiguration.

        :return: The crypto_event_analysis of this FleetAdvancedFeatureConfiguration.
        :rtype: oci.jms.models.CryptoEventAnalysis
        """
        return self._crypto_event_analysis

    @crypto_event_analysis.setter
    def crypto_event_analysis(self, crypto_event_analysis):
        """
        Sets the crypto_event_analysis of this FleetAdvancedFeatureConfiguration.

        :param crypto_event_analysis: The crypto_event_analysis of this FleetAdvancedFeatureConfiguration.
        :type: oci.jms.models.CryptoEventAnalysis
        """
        self._crypto_event_analysis = crypto_event_analysis

    @property
    def advanced_usage_tracking(self):
        """
        **[Required]** Gets the advanced_usage_tracking of this FleetAdvancedFeatureConfiguration.

        :return: The advanced_usage_tracking of this FleetAdvancedFeatureConfiguration.
        :rtype: oci.jms.models.AdvancedUsageTracking
        """
        return self._advanced_usage_tracking

    @advanced_usage_tracking.setter
    def advanced_usage_tracking(self, advanced_usage_tracking):
        """
        Sets the advanced_usage_tracking of this FleetAdvancedFeatureConfiguration.

        :param advanced_usage_tracking: The advanced_usage_tracking of this FleetAdvancedFeatureConfiguration.
        :type: oci.jms.models.AdvancedUsageTracking
        """
        self._advanced_usage_tracking = advanced_usage_tracking

    @property
    def jfr_recording(self):
        """
        **[Required]** Gets the jfr_recording of this FleetAdvancedFeatureConfiguration.

        :return: The jfr_recording of this FleetAdvancedFeatureConfiguration.
        :rtype: oci.jms.models.JfrRecording
        """
        return self._jfr_recording

    @jfr_recording.setter
    def jfr_recording(self, jfr_recording):
        """
        Sets the jfr_recording of this FleetAdvancedFeatureConfiguration.

        :param jfr_recording: The jfr_recording of this FleetAdvancedFeatureConfiguration.
        :type: oci.jms.models.JfrRecording
        """
        self._jfr_recording = jfr_recording

    @property
    def time_last_modified(self):
        """
        **[Required]** Gets the time_last_modified of this FleetAdvancedFeatureConfiguration.
        The date and time of the last modification to the Fleet Agent Configuration (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_last_modified of this FleetAdvancedFeatureConfiguration.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this FleetAdvancedFeatureConfiguration.
        The date and time of the last modification to the Fleet Agent Configuration (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_last_modified: The time_last_modified of this FleetAdvancedFeatureConfiguration.
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
