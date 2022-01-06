# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BdsMetastoreConfiguration(object):
    """
    The metastore configuration information.
    """

    #: A constant which can be used with the metastore_type property of a BdsMetastoreConfiguration.
    #: This constant has a value of "LOCAL"
    METASTORE_TYPE_LOCAL = "LOCAL"

    #: A constant which can be used with the metastore_type property of a BdsMetastoreConfiguration.
    #: This constant has a value of "EXTERNAL"
    METASTORE_TYPE_EXTERNAL = "EXTERNAL"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_STATE_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a BdsMetastoreConfiguration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new BdsMetastoreConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BdsMetastoreConfiguration.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BdsMetastoreConfiguration.
        :type display_name: str

        :param metastore_type:
            The value to assign to the metastore_type property of this BdsMetastoreConfiguration.
            Allowed values for this property are: "LOCAL", "EXTERNAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type metastore_type: str

        :param metastore_id:
            The value to assign to the metastore_id property of this BdsMetastoreConfiguration.
        :type metastore_id: str

        :param bds_api_key_id:
            The value to assign to the bds_api_key_id property of this BdsMetastoreConfiguration.
        :type bds_api_key_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BdsMetastoreConfiguration.
            Allowed values for this property are: "CREATING", "ACTIVATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this BdsMetastoreConfiguration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BdsMetastoreConfiguration.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'metastore_type': 'str',
            'metastore_id': 'str',
            'bds_api_key_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'metastore_type': 'metastoreType',
            'metastore_id': 'metastoreId',
            'bds_api_key_id': 'bdsApiKeyId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._display_name = None
        self._metastore_type = None
        self._metastore_id = None
        self._bds_api_key_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BdsMetastoreConfiguration.
        The ID of the metastore configuration


        :return: The id of this BdsMetastoreConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BdsMetastoreConfiguration.
        The ID of the metastore configuration


        :param id: The id of this BdsMetastoreConfiguration.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BdsMetastoreConfiguration.
        The display name of metastore configuration


        :return: The display_name of this BdsMetastoreConfiguration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BdsMetastoreConfiguration.
        The display name of metastore configuration


        :param display_name: The display_name of this BdsMetastoreConfiguration.
        :type: str
        """
        self._display_name = display_name

    @property
    def metastore_type(self):
        """
        **[Required]** Gets the metastore_type of this BdsMetastoreConfiguration.
        The type of the metastore in the metastore configuration.

        Allowed values for this property are: "LOCAL", "EXTERNAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The metastore_type of this BdsMetastoreConfiguration.
        :rtype: str
        """
        return self._metastore_type

    @metastore_type.setter
    def metastore_type(self, metastore_type):
        """
        Sets the metastore_type of this BdsMetastoreConfiguration.
        The type of the metastore in the metastore configuration.


        :param metastore_type: The metastore_type of this BdsMetastoreConfiguration.
        :type: str
        """
        allowed_values = ["LOCAL", "EXTERNAL"]
        if not value_allowed_none_or_none_sentinel(metastore_type, allowed_values):
            metastore_type = 'UNKNOWN_ENUM_VALUE'
        self._metastore_type = metastore_type

    @property
    def metastore_id(self):
        """
        Gets the metastore_id of this BdsMetastoreConfiguration.
        The OCID of the Data Catalog metastore. Set only if metastore's type is EXTERNAL.


        :return: The metastore_id of this BdsMetastoreConfiguration.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        """
        Sets the metastore_id of this BdsMetastoreConfiguration.
        The OCID of the Data Catalog metastore. Set only if metastore's type is EXTERNAL.


        :param metastore_id: The metastore_id of this BdsMetastoreConfiguration.
        :type: str
        """
        self._metastore_id = metastore_id

    @property
    def bds_api_key_id(self):
        """
        Gets the bds_api_key_id of this BdsMetastoreConfiguration.
        The ID of BDS API Key used for metastore configuration. Set only if metastore's type is EXTERNAL.


        :return: The bds_api_key_id of this BdsMetastoreConfiguration.
        :rtype: str
        """
        return self._bds_api_key_id

    @bds_api_key_id.setter
    def bds_api_key_id(self, bds_api_key_id):
        """
        Sets the bds_api_key_id of this BdsMetastoreConfiguration.
        The ID of BDS API Key used for metastore configuration. Set only if metastore's type is EXTERNAL.


        :param bds_api_key_id: The bds_api_key_id of this BdsMetastoreConfiguration.
        :type: str
        """
        self._bds_api_key_id = bds_api_key_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BdsMetastoreConfiguration.
        the lifecycle state of the metastore configuration.

        Allowed values for this property are: "CREATING", "ACTIVATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BdsMetastoreConfiguration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BdsMetastoreConfiguration.
        the lifecycle state of the metastore configuration.


        :param lifecycle_state: The lifecycle_state of this BdsMetastoreConfiguration.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BdsMetastoreConfiguration.
        The time when the configuration was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this BdsMetastoreConfiguration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BdsMetastoreConfiguration.
        The time when the configuration was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this BdsMetastoreConfiguration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BdsMetastoreConfiguration.
        The time when the configuration was updated, shown as an RFC 3339 formatted datetime string.


        :return: The time_updated of this BdsMetastoreConfiguration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BdsMetastoreConfiguration.
        The time when the configuration was updated, shown as an RFC 3339 formatted datetime string.


        :param time_updated: The time_updated of this BdsMetastoreConfiguration.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
