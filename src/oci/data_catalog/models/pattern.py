# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Pattern(object):
    """
    A pattern is a data selector or filter which can provide a singular,
    logical entity view aggregating multiple physical data artifacts for ease of use.
    """

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Pattern.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new Pattern object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Pattern.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this Pattern.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Pattern.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this Pattern.
        :type catalog_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Pattern.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Pattern.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Pattern.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this Pattern.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this Pattern.
        :type updated_by_id: str

        :param expression:
            The value to assign to the expression property of this Pattern.
        :type expression: str

        :param file_path_prefix:
            The value to assign to the file_path_prefix property of this Pattern.
        :type file_path_prefix: str

        :param check_file_path_list:
            The value to assign to the check_file_path_list property of this Pattern.
        :type check_file_path_list: list[str]

        :param is_enable_check_failure_limit:
            The value to assign to the is_enable_check_failure_limit property of this Pattern.
        :type is_enable_check_failure_limit: bool

        :param check_failure_limit:
            The value to assign to the check_failure_limit property of this Pattern.
        :type check_failure_limit: int

        :param properties:
            The value to assign to the properties property of this Pattern.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'expression': 'str',
            'file_path_prefix': 'str',
            'check_file_path_list': 'list[str]',
            'is_enable_check_failure_limit': 'bool',
            'check_failure_limit': 'int',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'catalog_id': 'catalogId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'expression': 'expression',
            'file_path_prefix': 'filePathPrefix',
            'check_file_path_list': 'checkFilePathList',
            'is_enable_check_failure_limit': 'isEnableCheckFailureLimit',
            'check_failure_limit': 'checkFailureLimit',
            'properties': 'properties'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._catalog_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._expression = None
        self._file_path_prefix = None
        self._check_file_path_list = None
        self._is_enable_check_failure_limit = None
        self._check_failure_limit = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Pattern.
        Unique pattern key that is immutable.


        :return: The key of this Pattern.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Pattern.
        Unique pattern key that is immutable.


        :param key: The key of this Pattern.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this Pattern.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Pattern.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Pattern.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Pattern.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Pattern.
        Detailed description of the pattern.


        :return: The description of this Pattern.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Pattern.
        Detailed description of the pattern.


        :param description: The description of this Pattern.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this Pattern.
        The data catalog's OCID.


        :return: The catalog_id of this Pattern.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this Pattern.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this Pattern.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Pattern.
        The current state of the pattern.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Pattern.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Pattern.
        The current state of the pattern.


        :param lifecycle_state: The lifecycle_state of this Pattern.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Pattern.
        The date and time the pattern was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Pattern.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Pattern.
        The date and time the pattern was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Pattern.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Pattern.
        The last time that any change was made to the pattern. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Pattern.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Pattern.
        The last time that any change was made to the pattern. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Pattern.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this Pattern.
        OCID of the user who created the pattern.


        :return: The created_by_id of this Pattern.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this Pattern.
        OCID of the user who created the pattern.


        :param created_by_id: The created_by_id of this Pattern.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this Pattern.
        OCID of the user who last modified the pattern.


        :return: The updated_by_id of this Pattern.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this Pattern.
        OCID of the user who last modified the pattern.


        :param updated_by_id: The updated_by_id of this Pattern.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def expression(self):
        """
        Gets the expression of this Pattern.
        Input string which drives the selection process, allowing for fine-grained control using qualifiers.
        Refer to the user documentation for details of the format and examples. A pattern cannot include both
        a prefix and an expression.


        :return: The expression of this Pattern.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this Pattern.
        Input string which drives the selection process, allowing for fine-grained control using qualifiers.
        Refer to the user documentation for details of the format and examples. A pattern cannot include both
        a prefix and an expression.


        :param expression: The expression of this Pattern.
        :type: str
        """
        self._expression = expression

    @property
    def file_path_prefix(self):
        """
        Gets the file_path_prefix of this Pattern.
        Input string which drives the selection process.
        Refer to the user documentation for details of the format and examples. A pattern cannot include both
        a prefix and an expression.


        :return: The file_path_prefix of this Pattern.
        :rtype: str
        """
        return self._file_path_prefix

    @file_path_prefix.setter
    def file_path_prefix(self, file_path_prefix):
        """
        Sets the file_path_prefix of this Pattern.
        Input string which drives the selection process.
        Refer to the user documentation for details of the format and examples. A pattern cannot include both
        a prefix and an expression.


        :param file_path_prefix: The file_path_prefix of this Pattern.
        :type: str
        """
        self._file_path_prefix = file_path_prefix

    @property
    def check_file_path_list(self):
        """
        Gets the check_file_path_list of this Pattern.
        List of file paths against which the pattern can be tried, as a check. This documents, for reference
        purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true,
        this will be run as a validation during the request, such that if the check fails the request fails. If
        isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even
        if the check fails, with a lifecycleState of FAILED.


        :return: The check_file_path_list of this Pattern.
        :rtype: list[str]
        """
        return self._check_file_path_list

    @check_file_path_list.setter
    def check_file_path_list(self, check_file_path_list):
        """
        Sets the check_file_path_list of this Pattern.
        List of file paths against which the pattern can be tried, as a check. This documents, for reference
        purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true,
        this will be run as a validation during the request, such that if the check fails the request fails. If
        isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even
        if the check fails, with a lifecycleState of FAILED.


        :param check_file_path_list: The check_file_path_list of this Pattern.
        :type: list[str]
        """
        self._check_file_path_list = check_file_path_list

    @property
    def is_enable_check_failure_limit(self):
        """
        Gets the is_enable_check_failure_limit of this Pattern.
        Indicates whether the pattern check, against the checkFilePathList, will fail the request if the count of
        UNMATCHED files is above the checkFailureLimit.


        :return: The is_enable_check_failure_limit of this Pattern.
        :rtype: bool
        """
        return self._is_enable_check_failure_limit

    @is_enable_check_failure_limit.setter
    def is_enable_check_failure_limit(self, is_enable_check_failure_limit):
        """
        Sets the is_enable_check_failure_limit of this Pattern.
        Indicates whether the pattern check, against the checkFilePathList, will fail the request if the count of
        UNMATCHED files is above the checkFailureLimit.


        :param is_enable_check_failure_limit: The is_enable_check_failure_limit of this Pattern.
        :type: bool
        """
        self._is_enable_check_failure_limit = is_enable_check_failure_limit

    @property
    def check_failure_limit(self):
        """
        Gets the check_failure_limit of this Pattern.
        The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if
        checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.


        :return: The check_failure_limit of this Pattern.
        :rtype: int
        """
        return self._check_failure_limit

    @check_failure_limit.setter
    def check_failure_limit(self, check_failure_limit):
        """
        Sets the check_failure_limit of this Pattern.
        The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if
        checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.


        :param check_failure_limit: The check_failure_limit of this Pattern.
        :type: int
        """
        self._check_failure_limit = check_failure_limit

    @property
    def properties(self):
        """
        Gets the properties of this Pattern.
        A map of maps that contains the properties which are specific to the pattern type. Each pattern type
        definition defines it's set of required and optional properties.
        Example: `{\"properties\": { \"default\": { \"tbd\"}}}`


        :return: The properties of this Pattern.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Pattern.
        A map of maps that contains the properties which are specific to the pattern type. Each pattern type
        definition defines it's set of required and optional properties.
        Example: `{\"properties\": { \"default\": { \"tbd\"}}}`


        :param properties: The properties of this Pattern.
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
