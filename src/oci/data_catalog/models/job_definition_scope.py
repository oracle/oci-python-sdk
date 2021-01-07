# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobDefinitionScope(object):
    """
    Defines the rules or criteria based on which the scope for job definition is circumscribed.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobDefinitionScope object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param folder_name:
            The value to assign to the folder_name property of this JobDefinitionScope.
        :type folder_name: str

        :param entity_name:
            The value to assign to the entity_name property of this JobDefinitionScope.
        :type entity_name: str

        :param folder_name_filter:
            The value to assign to the folder_name_filter property of this JobDefinitionScope.
        :type folder_name_filter: str

        :param entity_name_filter:
            The value to assign to the entity_name_filter property of this JobDefinitionScope.
        :type entity_name_filter: str

        :param is_sample_data_extracted:
            The value to assign to the is_sample_data_extracted property of this JobDefinitionScope.
        :type is_sample_data_extracted: bool

        :param sample_data_size_in_mbs:
            The value to assign to the sample_data_size_in_mbs property of this JobDefinitionScope.
        :type sample_data_size_in_mbs: int

        """
        self.swagger_types = {
            'folder_name': 'str',
            'entity_name': 'str',
            'folder_name_filter': 'str',
            'entity_name_filter': 'str',
            'is_sample_data_extracted': 'bool',
            'sample_data_size_in_mbs': 'int'
        }

        self.attribute_map = {
            'folder_name': 'folderName',
            'entity_name': 'entityName',
            'folder_name_filter': 'folderNameFilter',
            'entity_name_filter': 'entityNameFilter',
            'is_sample_data_extracted': 'isSampleDataExtracted',
            'sample_data_size_in_mbs': 'sampleDataSizeInMBs'
        }

        self._folder_name = None
        self._entity_name = None
        self._folder_name_filter = None
        self._entity_name_filter = None
        self._is_sample_data_extracted = None
        self._sample_data_size_in_mbs = None

    @property
    def folder_name(self):
        """
        Gets the folder_name of this JobDefinitionScope.
        Name of the folder or schema for this metadata harvest.


        :return: The folder_name of this JobDefinitionScope.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """
        Sets the folder_name of this JobDefinitionScope.
        Name of the folder or schema for this metadata harvest.


        :param folder_name: The folder_name of this JobDefinitionScope.
        :type: str
        """
        self._folder_name = folder_name

    @property
    def entity_name(self):
        """
        Gets the entity_name of this JobDefinitionScope.
        Name of the entity for this metadata harvest.


        :return: The entity_name of this JobDefinitionScope.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this JobDefinitionScope.
        Name of the entity for this metadata harvest.


        :param entity_name: The entity_name of this JobDefinitionScope.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def folder_name_filter(self):
        """
        Gets the folder_name_filter of this JobDefinitionScope.
        Filter rules with regular expression to specify folder names for this metadata harvest.


        :return: The folder_name_filter of this JobDefinitionScope.
        :rtype: str
        """
        return self._folder_name_filter

    @folder_name_filter.setter
    def folder_name_filter(self, folder_name_filter):
        """
        Sets the folder_name_filter of this JobDefinitionScope.
        Filter rules with regular expression to specify folder names for this metadata harvest.


        :param folder_name_filter: The folder_name_filter of this JobDefinitionScope.
        :type: str
        """
        self._folder_name_filter = folder_name_filter

    @property
    def entity_name_filter(self):
        """
        Gets the entity_name_filter of this JobDefinitionScope.
        Filter rules with regular expression to specify entity names for this metadata harvest.


        :return: The entity_name_filter of this JobDefinitionScope.
        :rtype: str
        """
        return self._entity_name_filter

    @entity_name_filter.setter
    def entity_name_filter(self, entity_name_filter):
        """
        Sets the entity_name_filter of this JobDefinitionScope.
        Filter rules with regular expression to specify entity names for this metadata harvest.


        :param entity_name_filter: The entity_name_filter of this JobDefinitionScope.
        :type: str
        """
        self._entity_name_filter = entity_name_filter

    @property
    def is_sample_data_extracted(self):
        """
        Gets the is_sample_data_extracted of this JobDefinitionScope.
        Specify if sample data to be extracted as part of this harvest.


        :return: The is_sample_data_extracted of this JobDefinitionScope.
        :rtype: bool
        """
        return self._is_sample_data_extracted

    @is_sample_data_extracted.setter
    def is_sample_data_extracted(self, is_sample_data_extracted):
        """
        Sets the is_sample_data_extracted of this JobDefinitionScope.
        Specify if sample data to be extracted as part of this harvest.


        :param is_sample_data_extracted: The is_sample_data_extracted of this JobDefinitionScope.
        :type: bool
        """
        self._is_sample_data_extracted = is_sample_data_extracted

    @property
    def sample_data_size_in_mbs(self):
        """
        Gets the sample_data_size_in_mbs of this JobDefinitionScope.
        Specify the sample data size in MB, specified as number of rows, for this metadata harvest.


        :return: The sample_data_size_in_mbs of this JobDefinitionScope.
        :rtype: int
        """
        return self._sample_data_size_in_mbs

    @sample_data_size_in_mbs.setter
    def sample_data_size_in_mbs(self, sample_data_size_in_mbs):
        """
        Sets the sample_data_size_in_mbs of this JobDefinitionScope.
        Specify the sample data size in MB, specified as number of rows, for this metadata harvest.


        :param sample_data_size_in_mbs: The sample_data_size_in_mbs of this JobDefinitionScope.
        :type: int
        """
        self._sample_data_size_in_mbs = sample_data_size_in_mbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
