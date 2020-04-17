# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateJobDefinitionDetails(object):
    """
    Update information for a job definition resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateJobDefinitionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateJobDefinitionDetails.
        :type display_name: str

        :param is_incremental:
            The value to assign to the is_incremental property of this UpdateJobDefinitionDetails.
        :type is_incremental: bool

        :param data_asset_key:
            The value to assign to the data_asset_key property of this UpdateJobDefinitionDetails.
        :type data_asset_key: str

        :param description:
            The value to assign to the description property of this UpdateJobDefinitionDetails.
        :type description: str

        :param connection_key:
            The value to assign to the connection_key property of this UpdateJobDefinitionDetails.
        :type connection_key: str

        :param is_sample_data_extracted:
            The value to assign to the is_sample_data_extracted property of this UpdateJobDefinitionDetails.
        :type is_sample_data_extracted: bool

        :param sample_data_size_in_mbs:
            The value to assign to the sample_data_size_in_mbs property of this UpdateJobDefinitionDetails.
        :type sample_data_size_in_mbs: int

        :param properties:
            The value to assign to the properties property of this UpdateJobDefinitionDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_incremental': 'bool',
            'data_asset_key': 'str',
            'description': 'str',
            'connection_key': 'str',
            'is_sample_data_extracted': 'bool',
            'sample_data_size_in_mbs': 'int',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_incremental': 'isIncremental',
            'data_asset_key': 'dataAssetKey',
            'description': 'description',
            'connection_key': 'connectionKey',
            'is_sample_data_extracted': 'isSampleDataExtracted',
            'sample_data_size_in_mbs': 'sampleDataSizeInMBs',
            'properties': 'properties'
        }

        self._display_name = None
        self._is_incremental = None
        self._data_asset_key = None
        self._description = None
        self._connection_key = None
        self._is_sample_data_extracted = None
        self._sample_data_size_in_mbs = None
        self._properties = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateJobDefinitionDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateJobDefinitionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateJobDefinitionDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateJobDefinitionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_incremental(self):
        """
        Gets the is_incremental of this UpdateJobDefinitionDetails.
        Specifies if the job definition is incremental or full.


        :return: The is_incremental of this UpdateJobDefinitionDetails.
        :rtype: bool
        """
        return self._is_incremental

    @is_incremental.setter
    def is_incremental(self, is_incremental):
        """
        Sets the is_incremental of this UpdateJobDefinitionDetails.
        Specifies if the job definition is incremental or full.


        :param is_incremental: The is_incremental of this UpdateJobDefinitionDetails.
        :type: bool
        """
        self._is_incremental = is_incremental

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this UpdateJobDefinitionDetails.
        The key of the data asset for which the job is defined.


        :return: The data_asset_key of this UpdateJobDefinitionDetails.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this UpdateJobDefinitionDetails.
        The key of the data asset for which the job is defined.


        :param data_asset_key: The data_asset_key of this UpdateJobDefinitionDetails.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def description(self):
        """
        Gets the description of this UpdateJobDefinitionDetails.
        Detailed description of the job definition.


        :return: The description of this UpdateJobDefinitionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateJobDefinitionDetails.
        Detailed description of the job definition.


        :param description: The description of this UpdateJobDefinitionDetails.
        :type: str
        """
        self._description = description

    @property
    def connection_key(self):
        """
        Gets the connection_key of this UpdateJobDefinitionDetails.
        The key of the connection resource to be used for harvest, sampling, profiling jobs.


        :return: The connection_key of this UpdateJobDefinitionDetails.
        :rtype: str
        """
        return self._connection_key

    @connection_key.setter
    def connection_key(self, connection_key):
        """
        Sets the connection_key of this UpdateJobDefinitionDetails.
        The key of the connection resource to be used for harvest, sampling, profiling jobs.


        :param connection_key: The connection_key of this UpdateJobDefinitionDetails.
        :type: str
        """
        self._connection_key = connection_key

    @property
    def is_sample_data_extracted(self):
        """
        Gets the is_sample_data_extracted of this UpdateJobDefinitionDetails.
        Specify if sample data to be extracted as part of this harvest.


        :return: The is_sample_data_extracted of this UpdateJobDefinitionDetails.
        :rtype: bool
        """
        return self._is_sample_data_extracted

    @is_sample_data_extracted.setter
    def is_sample_data_extracted(self, is_sample_data_extracted):
        """
        Sets the is_sample_data_extracted of this UpdateJobDefinitionDetails.
        Specify if sample data to be extracted as part of this harvest.


        :param is_sample_data_extracted: The is_sample_data_extracted of this UpdateJobDefinitionDetails.
        :type: bool
        """
        self._is_sample_data_extracted = is_sample_data_extracted

    @property
    def sample_data_size_in_mbs(self):
        """
        Gets the sample_data_size_in_mbs of this UpdateJobDefinitionDetails.
        Specify the sample data size in MB, specified as number of rows, for this metadata harvest.


        :return: The sample_data_size_in_mbs of this UpdateJobDefinitionDetails.
        :rtype: int
        """
        return self._sample_data_size_in_mbs

    @sample_data_size_in_mbs.setter
    def sample_data_size_in_mbs(self, sample_data_size_in_mbs):
        """
        Sets the sample_data_size_in_mbs of this UpdateJobDefinitionDetails.
        Specify the sample data size in MB, specified as number of rows, for this metadata harvest.


        :param sample_data_size_in_mbs: The sample_data_size_in_mbs of this UpdateJobDefinitionDetails.
        :type: int
        """
        self._sample_data_size_in_mbs = sample_data_size_in_mbs

    @property
    def properties(self):
        """
        Gets the properties of this UpdateJobDefinitionDetails.
        A map of maps that contains the properties which are specific to the job type. Each job type
        definition may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job definitions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this UpdateJobDefinitionDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateJobDefinitionDetails.
        A map of maps that contains the properties which are specific to the job type. Each job type
        definition may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job definitions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this UpdateJobDefinitionDetails.
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
