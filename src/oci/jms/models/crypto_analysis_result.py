# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CryptoAnalysisResult(object):
    """
    Metadata of a Crypto Event Analysis result. The analysis result is stored as the Object Storage object.
    """

    #: A constant which can be used with the aggregation_mode property of a CryptoAnalysisResult.
    #: This constant has a value of "JFR"
    AGGREGATION_MODE_JFR = "JFR"

    #: A constant which can be used with the aggregation_mode property of a CryptoAnalysisResult.
    #: This constant has a value of "MANAGED_INSTANCE"
    AGGREGATION_MODE_MANAGED_INSTANCE = "MANAGED_INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CryptoAnalysisResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CryptoAnalysisResult.
        :type id: str

        :param work_request_id:
            The value to assign to the work_request_id property of this CryptoAnalysisResult.
        :type work_request_id: str

        :param aggregation_mode:
            The value to assign to the aggregation_mode property of this CryptoAnalysisResult.
            Allowed values for this property are: "JFR", "MANAGED_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type aggregation_mode: str

        :param fleet_id:
            The value to assign to the fleet_id property of this CryptoAnalysisResult.
        :type fleet_id: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this CryptoAnalysisResult.
        :type managed_instance_id: str

        :param host_name:
            The value to assign to the host_name property of this CryptoAnalysisResult.
        :type host_name: str

        :param time_first_event:
            The value to assign to the time_first_event property of this CryptoAnalysisResult.
        :type time_first_event: datetime

        :param time_last_event:
            The value to assign to the time_last_event property of this CryptoAnalysisResult.
        :type time_last_event: datetime

        :param total_event_count:
            The value to assign to the total_event_count property of this CryptoAnalysisResult.
        :type total_event_count: int

        :param summarized_event_count:
            The value to assign to the summarized_event_count property of this CryptoAnalysisResult.
        :type summarized_event_count: int

        :param finding_count:
            The value to assign to the finding_count property of this CryptoAnalysisResult.
        :type finding_count: int

        :param non_compliant_finding_count:
            The value to assign to the non_compliant_finding_count property of this CryptoAnalysisResult.
        :type non_compliant_finding_count: int

        :param time_created:
            The value to assign to the time_created property of this CryptoAnalysisResult.
        :type time_created: datetime

        :param crypto_roadmap_version:
            The value to assign to the crypto_roadmap_version property of this CryptoAnalysisResult.
        :type crypto_roadmap_version: str

        :param namespace:
            The value to assign to the namespace property of this CryptoAnalysisResult.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CryptoAnalysisResult.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this CryptoAnalysisResult.
        :type object_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'work_request_id': 'str',
            'aggregation_mode': 'str',
            'fleet_id': 'str',
            'managed_instance_id': 'str',
            'host_name': 'str',
            'time_first_event': 'datetime',
            'time_last_event': 'datetime',
            'total_event_count': 'int',
            'summarized_event_count': 'int',
            'finding_count': 'int',
            'non_compliant_finding_count': 'int',
            'time_created': 'datetime',
            'crypto_roadmap_version': 'str',
            'namespace': 'str',
            'bucket_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'work_request_id': 'workRequestId',
            'aggregation_mode': 'aggregationMode',
            'fleet_id': 'fleetId',
            'managed_instance_id': 'managedInstanceId',
            'host_name': 'hostName',
            'time_first_event': 'timeFirstEvent',
            'time_last_event': 'timeLastEvent',
            'total_event_count': 'totalEventCount',
            'summarized_event_count': 'summarizedEventCount',
            'finding_count': 'findingCount',
            'non_compliant_finding_count': 'nonCompliantFindingCount',
            'time_created': 'timeCreated',
            'crypto_roadmap_version': 'cryptoRoadmapVersion',
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'object_name': 'objectName'
        }

        self._id = None
        self._work_request_id = None
        self._aggregation_mode = None
        self._fleet_id = None
        self._managed_instance_id = None
        self._host_name = None
        self._time_first_event = None
        self._time_last_event = None
        self._total_event_count = None
        self._summarized_event_count = None
        self._finding_count = None
        self._non_compliant_finding_count = None
        self._time_created = None
        self._crypto_roadmap_version = None
        self._namespace = None
        self._bucket_name = None
        self._object_name = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CryptoAnalysisResult.
        The OCID to identify this analysis results.


        :return: The id of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CryptoAnalysisResult.
        The OCID to identify this analysis results.


        :param id: The id of this CryptoAnalysisResult.
        :type: str
        """
        self._id = id

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this CryptoAnalysisResult.
        The OCID of the work request to start the analysis.


        :return: The work_request_id of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this CryptoAnalysisResult.
        The OCID of the work request to start the analysis.


        :param work_request_id: The work_request_id of this CryptoAnalysisResult.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def aggregation_mode(self):
        """
        **[Required]** Gets the aggregation_mode of this CryptoAnalysisResult.
        The result aggregation mode

        Allowed values for this property are: "JFR", "MANAGED_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The aggregation_mode of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._aggregation_mode

    @aggregation_mode.setter
    def aggregation_mode(self, aggregation_mode):
        """
        Sets the aggregation_mode of this CryptoAnalysisResult.
        The result aggregation mode


        :param aggregation_mode: The aggregation_mode of this CryptoAnalysisResult.
        :type: str
        """
        allowed_values = ["JFR", "MANAGED_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(aggregation_mode, allowed_values):
            aggregation_mode = 'UNKNOWN_ENUM_VALUE'
        self._aggregation_mode = aggregation_mode

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this CryptoAnalysisResult.
        The fleet OCID.


        :return: The fleet_id of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this CryptoAnalysisResult.
        The fleet OCID.


        :param fleet_id: The fleet_id of this CryptoAnalysisResult.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def managed_instance_id(self):
        """
        Gets the managed_instance_id of this CryptoAnalysisResult.
        The managed instance OCID.


        :return: The managed_instance_id of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this CryptoAnalysisResult.
        The managed instance OCID.


        :param managed_instance_id: The managed_instance_id of this CryptoAnalysisResult.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def host_name(self):
        """
        Gets the host_name of this CryptoAnalysisResult.
        The hostname of the managed instance.


        :return: The host_name of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this CryptoAnalysisResult.
        The hostname of the managed instance.


        :param host_name: The host_name of this CryptoAnalysisResult.
        :type: str
        """
        self._host_name = host_name

    @property
    def time_first_event(self):
        """
        Gets the time_first_event of this CryptoAnalysisResult.
        Time of the first event in the analysis.


        :return: The time_first_event of this CryptoAnalysisResult.
        :rtype: datetime
        """
        return self._time_first_event

    @time_first_event.setter
    def time_first_event(self, time_first_event):
        """
        Sets the time_first_event of this CryptoAnalysisResult.
        Time of the first event in the analysis.


        :param time_first_event: The time_first_event of this CryptoAnalysisResult.
        :type: datetime
        """
        self._time_first_event = time_first_event

    @property
    def time_last_event(self):
        """
        Gets the time_last_event of this CryptoAnalysisResult.
        Time of the last event in the analysis.


        :return: The time_last_event of this CryptoAnalysisResult.
        :rtype: datetime
        """
        return self._time_last_event

    @time_last_event.setter
    def time_last_event(self, time_last_event):
        """
        Sets the time_last_event of this CryptoAnalysisResult.
        Time of the last event in the analysis.


        :param time_last_event: The time_last_event of this CryptoAnalysisResult.
        :type: datetime
        """
        self._time_last_event = time_last_event

    @property
    def total_event_count(self):
        """
        **[Required]** Gets the total_event_count of this CryptoAnalysisResult.
        Total number of events in the analysis.


        :return: The total_event_count of this CryptoAnalysisResult.
        :rtype: int
        """
        return self._total_event_count

    @total_event_count.setter
    def total_event_count(self, total_event_count):
        """
        Sets the total_event_count of this CryptoAnalysisResult.
        Total number of events in the analysis.


        :param total_event_count: The total_event_count of this CryptoAnalysisResult.
        :type: int
        """
        self._total_event_count = total_event_count

    @property
    def summarized_event_count(self):
        """
        **[Required]** Gets the summarized_event_count of this CryptoAnalysisResult.
        Total number of summarized events. Summarized events are deduplicated events of interest.


        :return: The summarized_event_count of this CryptoAnalysisResult.
        :rtype: int
        """
        return self._summarized_event_count

    @summarized_event_count.setter
    def summarized_event_count(self, summarized_event_count):
        """
        Sets the summarized_event_count of this CryptoAnalysisResult.
        Total number of summarized events. Summarized events are deduplicated events of interest.


        :param summarized_event_count: The summarized_event_count of this CryptoAnalysisResult.
        :type: int
        """
        self._summarized_event_count = summarized_event_count

    @property
    def finding_count(self):
        """
        **[Required]** Gets the finding_count of this CryptoAnalysisResult.
        Total number of findings with the analysis.


        :return: The finding_count of this CryptoAnalysisResult.
        :rtype: int
        """
        return self._finding_count

    @finding_count.setter
    def finding_count(self, finding_count):
        """
        Sets the finding_count of this CryptoAnalysisResult.
        Total number of findings with the analysis.


        :param finding_count: The finding_count of this CryptoAnalysisResult.
        :type: int
        """
        self._finding_count = finding_count

    @property
    def non_compliant_finding_count(self):
        """
        **[Required]** Gets the non_compliant_finding_count of this CryptoAnalysisResult.
        Total number of non-compliant findings with the analysis. A non-compliant finding means the
        application won't work properly with the changes introduced by the crypto roadmap version
        used the the analysis.


        :return: The non_compliant_finding_count of this CryptoAnalysisResult.
        :rtype: int
        """
        return self._non_compliant_finding_count

    @non_compliant_finding_count.setter
    def non_compliant_finding_count(self, non_compliant_finding_count):
        """
        Sets the non_compliant_finding_count of this CryptoAnalysisResult.
        Total number of non-compliant findings with the analysis. A non-compliant finding means the
        application won't work properly with the changes introduced by the crypto roadmap version
        used the the analysis.


        :param non_compliant_finding_count: The non_compliant_finding_count of this CryptoAnalysisResult.
        :type: int
        """
        self._non_compliant_finding_count = non_compliant_finding_count

    @property
    def time_created(self):
        """
        Gets the time_created of this CryptoAnalysisResult.
        The time the result is compiled.


        :return: The time_created of this CryptoAnalysisResult.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CryptoAnalysisResult.
        The time the result is compiled.


        :param time_created: The time_created of this CryptoAnalysisResult.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def crypto_roadmap_version(self):
        """
        **[Required]** Gets the crypto_roadmap_version of this CryptoAnalysisResult.
        The Crypto Roadmap version used to perform the analysis.


        :return: The crypto_roadmap_version of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._crypto_roadmap_version

    @crypto_roadmap_version.setter
    def crypto_roadmap_version(self, crypto_roadmap_version):
        """
        Sets the crypto_roadmap_version of this CryptoAnalysisResult.
        The Crypto Roadmap version used to perform the analysis.


        :param crypto_roadmap_version: The crypto_roadmap_version of this CryptoAnalysisResult.
        :type: str
        """
        self._crypto_roadmap_version = crypto_roadmap_version

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this CryptoAnalysisResult.
        The Object Storage namespace of this analysis result.


        :return: The namespace of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this CryptoAnalysisResult.
        The Object Storage namespace of this analysis result.


        :param namespace: The namespace of this CryptoAnalysisResult.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CryptoAnalysisResult.
        The Object Storage bucket name of this analysis result.


        :return: The bucket_name of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CryptoAnalysisResult.
        The Object Storage bucket name of this analysis result.


        :param bucket_name: The bucket_name of this CryptoAnalysisResult.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this CryptoAnalysisResult.
        The Object Storage object name of this analysis result.


        :return: The object_name of this CryptoAnalysisResult.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this CryptoAnalysisResult.
        The Object Storage object name of this analysis result.


        :param object_name: The object_name of this CryptoAnalysisResult.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
