# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobDefinition(object):
    """
    Representation of a job definition resource. Job definitions define the harvest scope and includes the list
    of objects to be harvested along with a schedule. The list of objects is usually specified through a combination
    of object type, regular expressions, or specific names of objects and a sample size for the data harvested.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobDefinition.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this JobDefinition.
        :type display_name: str

        :param catalog_id:
            The value to assign to the catalog_id property of this JobDefinition.
        :type catalog_id: str

        :param job_type:
            The value to assign to the job_type property of this JobDefinition.
        :type job_type: str

        :param is_incremental:
            The value to assign to the is_incremental property of this JobDefinition.
        :type is_incremental: bool

        :param data_asset_key:
            The value to assign to the data_asset_key property of this JobDefinition.
        :type data_asset_key: str

        :param description:
            The value to assign to the description property of this JobDefinition.
        :type description: str

        :param connection_key:
            The value to assign to the connection_key property of this JobDefinition.
        :type connection_key: str

        :param internal_version:
            The value to assign to the internal_version property of this JobDefinition.
        :type internal_version: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobDefinition.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this JobDefinition.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JobDefinition.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this JobDefinition.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this JobDefinition.
        :type updated_by_id: str

        :param uri:
            The value to assign to the uri property of this JobDefinition.
        :type uri: str

        :param is_sample_data_extracted:
            The value to assign to the is_sample_data_extracted property of this JobDefinition.
        :type is_sample_data_extracted: bool

        :param sample_data_size_in_mbs:
            The value to assign to the sample_data_size_in_mbs property of this JobDefinition.
        :type sample_data_size_in_mbs: int

        :param properties:
            The value to assign to the properties property of this JobDefinition.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'catalog_id': 'str',
            'job_type': 'str',
            'is_incremental': 'bool',
            'data_asset_key': 'str',
            'description': 'str',
            'connection_key': 'str',
            'internal_version': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'uri': 'str',
            'is_sample_data_extracted': 'bool',
            'sample_data_size_in_mbs': 'int',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'catalog_id': 'catalogId',
            'job_type': 'jobType',
            'is_incremental': 'isIncremental',
            'data_asset_key': 'dataAssetKey',
            'description': 'description',
            'connection_key': 'connectionKey',
            'internal_version': 'internalVersion',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'uri': 'uri',
            'is_sample_data_extracted': 'isSampleDataExtracted',
            'sample_data_size_in_mbs': 'sampleDataSizeInMBs',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._catalog_id = None
        self._job_type = None
        self._is_incremental = None
        self._data_asset_key = None
        self._description = None
        self._connection_key = None
        self._internal_version = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._uri = None
        self._is_sample_data_extracted = None
        self._sample_data_size_in_mbs = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobDefinition.
        Unique key of the job definition resource that is immutable.


        :return: The key of this JobDefinition.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobDefinition.
        Unique key of the job definition resource that is immutable.


        :param key: The key of this JobDefinition.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this JobDefinition.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this JobDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobDefinition.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this JobDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this JobDefinition.
        The data catalog's OCID.


        :return: The catalog_id of this JobDefinition.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this JobDefinition.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this JobDefinition.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def job_type(self):
        """
        Gets the job_type of this JobDefinition.
        Type of the job definition.


        :return: The job_type of this JobDefinition.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this JobDefinition.
        Type of the job definition.


        :param job_type: The job_type of this JobDefinition.
        :type: str
        """
        self._job_type = job_type

    @property
    def is_incremental(self):
        """
        Gets the is_incremental of this JobDefinition.
        Specifies if the job definition is incremental or full.


        :return: The is_incremental of this JobDefinition.
        :rtype: bool
        """
        return self._is_incremental

    @is_incremental.setter
    def is_incremental(self, is_incremental):
        """
        Sets the is_incremental of this JobDefinition.
        Specifies if the job definition is incremental or full.


        :param is_incremental: The is_incremental of this JobDefinition.
        :type: bool
        """
        self._is_incremental = is_incremental

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this JobDefinition.
        The key of the data asset for which the job is defined.


        :return: The data_asset_key of this JobDefinition.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this JobDefinition.
        The key of the data asset for which the job is defined.


        :param data_asset_key: The data_asset_key of this JobDefinition.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def description(self):
        """
        Gets the description of this JobDefinition.
        Detailed description of the job definition.


        :return: The description of this JobDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JobDefinition.
        Detailed description of the job definition.


        :param description: The description of this JobDefinition.
        :type: str
        """
        self._description = description

    @property
    def connection_key(self):
        """
        Gets the connection_key of this JobDefinition.
        The key of the default connection resource to be used for harvest, sampling, profiling jobs.
        This may be overridden in each job instance.


        :return: The connection_key of this JobDefinition.
        :rtype: str
        """
        return self._connection_key

    @connection_key.setter
    def connection_key(self, connection_key):
        """
        Sets the connection_key of this JobDefinition.
        The key of the default connection resource to be used for harvest, sampling, profiling jobs.
        This may be overridden in each job instance.


        :param connection_key: The connection_key of this JobDefinition.
        :type: str
        """
        self._connection_key = connection_key

    @property
    def internal_version(self):
        """
        Gets the internal_version of this JobDefinition.
        Version of the job definition object. Used internally but can be visible to users.


        :return: The internal_version of this JobDefinition.
        :rtype: str
        """
        return self._internal_version

    @internal_version.setter
    def internal_version(self, internal_version):
        """
        Sets the internal_version of this JobDefinition.
        Version of the job definition object. Used internally but can be visible to users.


        :param internal_version: The internal_version of this JobDefinition.
        :type: str
        """
        self._internal_version = internal_version

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this JobDefinition.
        Lifecycle state of the job definition.


        :return: The lifecycle_state of this JobDefinition.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobDefinition.
        Lifecycle state of the job definition.


        :param lifecycle_state: The lifecycle_state of this JobDefinition.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this JobDefinition.
        The date and time the job definition was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobDefinition.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobDefinition.
        The date and time the job definition was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobDefinition.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this JobDefinition.
        The last time that any change was made to the data asset. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this JobDefinition.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JobDefinition.
        The last time that any change was made to the data asset. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this JobDefinition.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this JobDefinition.
        OCID of the user who created this job definition.


        :return: The created_by_id of this JobDefinition.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this JobDefinition.
        OCID of the user who created this job definition.


        :param created_by_id: The created_by_id of this JobDefinition.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this JobDefinition.
        OCID of the user who updated this job definition.


        :return: The updated_by_id of this JobDefinition.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this JobDefinition.
        OCID of the user who updated this job definition.


        :param updated_by_id: The updated_by_id of this JobDefinition.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def uri(self):
        """
        Gets the uri of this JobDefinition.
        URI to the job definition instance in the API.


        :return: The uri of this JobDefinition.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobDefinition.
        URI to the job definition instance in the API.


        :param uri: The uri of this JobDefinition.
        :type: str
        """
        self._uri = uri

    @property
    def is_sample_data_extracted(self):
        """
        Gets the is_sample_data_extracted of this JobDefinition.
        Specify if sample data to be extracted as part of this harvest.


        :return: The is_sample_data_extracted of this JobDefinition.
        :rtype: bool
        """
        return self._is_sample_data_extracted

    @is_sample_data_extracted.setter
    def is_sample_data_extracted(self, is_sample_data_extracted):
        """
        Sets the is_sample_data_extracted of this JobDefinition.
        Specify if sample data to be extracted as part of this harvest.


        :param is_sample_data_extracted: The is_sample_data_extracted of this JobDefinition.
        :type: bool
        """
        self._is_sample_data_extracted = is_sample_data_extracted

    @property
    def sample_data_size_in_mbs(self):
        """
        Gets the sample_data_size_in_mbs of this JobDefinition.
        Specify the sample data size in MB, specified as number of rows, for this metadata harvest.


        :return: The sample_data_size_in_mbs of this JobDefinition.
        :rtype: int
        """
        return self._sample_data_size_in_mbs

    @sample_data_size_in_mbs.setter
    def sample_data_size_in_mbs(self, sample_data_size_in_mbs):
        """
        Sets the sample_data_size_in_mbs of this JobDefinition.
        Specify the sample data size in MB, specified as number of rows, for this metadata harvest.


        :param sample_data_size_in_mbs: The sample_data_size_in_mbs of this JobDefinition.
        :type: int
        """
        self._sample_data_size_in_mbs = sample_data_size_in_mbs

    @property
    def properties(self):
        """
        Gets the properties of this JobDefinition.
        A map of maps that contains the properties which are specific to the job type. Each job type
        definition may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job definitions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this JobDefinition.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this JobDefinition.
        A map of maps that contains the properties which are specific to the job type. Each job type
        definition may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job definitions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this JobDefinition.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
