# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFolderDetails(object):
    """
    Properties used in folder update operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFolderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateFolderDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateFolderDetails.
        :type description: str

        :param parent_folder_key:
            The value to assign to the parent_folder_key property of this UpdateFolderDetails.
        :type parent_folder_key: str

        :param properties:
            The value to assign to the properties property of this UpdateFolderDetails.
        :type properties: dict(str, dict(str, str))

        :param time_external:
            The value to assign to the time_external property of this UpdateFolderDetails.
        :type time_external: datetime

        :param harvest_status:
            The value to assign to the harvest_status property of this UpdateFolderDetails.
        :type harvest_status: str

        :param last_job_key:
            The value to assign to the last_job_key property of this UpdateFolderDetails.
        :type last_job_key: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'parent_folder_key': 'str',
            'properties': 'dict(str, dict(str, str))',
            'time_external': 'datetime',
            'harvest_status': 'str',
            'last_job_key': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'parent_folder_key': 'parentFolderKey',
            'properties': 'properties',
            'time_external': 'timeExternal',
            'harvest_status': 'harvestStatus',
            'last_job_key': 'lastJobKey'
        }

        self._display_name = None
        self._description = None
        self._parent_folder_key = None
        self._properties = None
        self._time_external = None
        self._harvest_status = None
        self._last_job_key = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateFolderDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateFolderDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateFolderDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateFolderDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateFolderDetails.
        Detailed description of a folder.


        :return: The description of this UpdateFolderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateFolderDetails.
        Detailed description of a folder.


        :param description: The description of this UpdateFolderDetails.
        :type: str
        """
        self._description = description

    @property
    def parent_folder_key(self):
        """
        Gets the parent_folder_key of this UpdateFolderDetails.
        The key of the containing folder.


        :return: The parent_folder_key of this UpdateFolderDetails.
        :rtype: str
        """
        return self._parent_folder_key

    @parent_folder_key.setter
    def parent_folder_key(self, parent_folder_key):
        """
        Sets the parent_folder_key of this UpdateFolderDetails.
        The key of the containing folder.


        :param parent_folder_key: The parent_folder_key of this UpdateFolderDetails.
        :type: str
        """
        self._parent_folder_key = parent_folder_key

    @property
    def properties(self):
        """
        Gets the properties of this UpdateFolderDetails.
        A map of maps that contains the properties which are specific to the folder type. Each folder type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        folders have required properties within the \"default\" category. To determine the set of optional and
        required properties for a folder type, a query can be done on '/types?type=folder' that returns a
        collection of all folder types. The appropriate folder type, which includes definitions of all of
        it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :return: The properties of this UpdateFolderDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateFolderDetails.
        A map of maps that contains the properties which are specific to the folder type. Each folder type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        folders have required properties within the \"default\" category. To determine the set of optional and
        required properties for a folder type, a query can be done on '/types?type=folder' that returns a
        collection of all folder types. The appropriate folder type, which includes definitions of all of
        it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`


        :param properties: The properties of this UpdateFolderDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    @property
    def time_external(self):
        """
        Gets the time_external of this UpdateFolderDetails.
        Last modified timestamp of this object in the external system.


        :return: The time_external of this UpdateFolderDetails.
        :rtype: datetime
        """
        return self._time_external

    @time_external.setter
    def time_external(self, time_external):
        """
        Sets the time_external of this UpdateFolderDetails.
        Last modified timestamp of this object in the external system.


        :param time_external: The time_external of this UpdateFolderDetails.
        :type: datetime
        """
        self._time_external = time_external

    @property
    def harvest_status(self):
        """
        Gets the harvest_status of this UpdateFolderDetails.
        Harvest status of the folder.


        :return: The harvest_status of this UpdateFolderDetails.
        :rtype: str
        """
        return self._harvest_status

    @harvest_status.setter
    def harvest_status(self, harvest_status):
        """
        Sets the harvest_status of this UpdateFolderDetails.
        Harvest status of the folder.


        :param harvest_status: The harvest_status of this UpdateFolderDetails.
        :type: str
        """
        self._harvest_status = harvest_status

    @property
    def last_job_key(self):
        """
        Gets the last_job_key of this UpdateFolderDetails.
        The key of the last harvest process to update the metadata of this object.


        :return: The last_job_key of this UpdateFolderDetails.
        :rtype: str
        """
        return self._last_job_key

    @last_job_key.setter
    def last_job_key(self, last_job_key):
        """
        Sets the last_job_key of this UpdateFolderDetails.
        The key of the last harvest process to update the metadata of this object.


        :param last_job_key: The last_job_key of this UpdateFolderDetails.
        :type: str
        """
        self._last_job_key = last_job_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
