# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceCategory(object):
    """
    Incident Classifier details
    """

    #: A constant which can be used with the scope property of a ServiceCategory.
    #: This constant has a value of "AD"
    SCOPE_AD = "AD"

    #: A constant which can be used with the scope property of a ServiceCategory.
    #: This constant has a value of "REGION"
    SCOPE_REGION = "REGION"

    #: A constant which can be used with the scope property of a ServiceCategory.
    #: This constant has a value of "TENANCY"
    SCOPE_TENANCY = "TENANCY"

    #: A constant which can be used with the scope property of a ServiceCategory.
    #: This constant has a value of "NONE"
    SCOPE_NONE = "NONE"

    #: A constant which can be used with the unit property of a ServiceCategory.
    #: This constant has a value of "COUNT"
    UNIT_COUNT = "COUNT"

    #: A constant which can be used with the unit property of a ServiceCategory.
    #: This constant has a value of "GB"
    UNIT_GB = "GB"

    #: A constant which can be used with the unit property of a ServiceCategory.
    #: This constant has a value of "NONE"
    UNIT_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceCategory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ServiceCategory.
        :type key: str

        :param name:
            The value to assign to the name property of this ServiceCategory.
        :type name: str

        :param label:
            The value to assign to the label property of this ServiceCategory.
        :type label: str

        :param description:
            The value to assign to the description property of this ServiceCategory.
        :type description: str

        :param issue_type_list:
            The value to assign to the issue_type_list property of this ServiceCategory.
        :type issue_type_list: list[IssueType]

        :param scope:
            The value to assign to the scope property of this ServiceCategory.
            Allowed values for this property are: "AD", "REGION", "TENANCY", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param unit:
            The value to assign to the unit property of this ServiceCategory.
            Allowed values for this property are: "COUNT", "GB", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        :param limit_id:
            The value to assign to the limit_id property of this ServiceCategory.
        :type limit_id: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'label': 'str',
            'description': 'str',
            'issue_type_list': 'list[IssueType]',
            'scope': 'str',
            'unit': 'str',
            'limit_id': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'label': 'label',
            'description': 'description',
            'issue_type_list': 'issueTypeList',
            'scope': 'scope',
            'unit': 'unit',
            'limit_id': 'limitId'
        }

        self._key = None
        self._name = None
        self._label = None
        self._description = None
        self._issue_type_list = None
        self._scope = None
        self._unit = None
        self._limit_id = None

    @property
    def key(self):
        """
        Gets the key of this ServiceCategory.
        Unique ID that identifies a classifier


        :return: The key of this ServiceCategory.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ServiceCategory.
        Unique ID that identifies a classifier


        :param key: The key of this ServiceCategory.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this ServiceCategory.
        Name of classifier. eg: LIMIT Increase


        :return: The name of this ServiceCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServiceCategory.
        Name of classifier. eg: LIMIT Increase


        :param name: The name of this ServiceCategory.
        :type: str
        """
        self._name = name

    @property
    def label(self):
        """
        Gets the label of this ServiceCategory.
        Label of classifier


        :return: The label of this ServiceCategory.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this ServiceCategory.
        Label of classifier


        :param label: The label of this ServiceCategory.
        :type: str
        """
        self._label = label

    @property
    def description(self):
        """
        Gets the description of this ServiceCategory.
        Description of classifier


        :return: The description of this ServiceCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServiceCategory.
        Description of classifier


        :param description: The description of this ServiceCategory.
        :type: str
        """
        self._description = description

    @property
    def issue_type_list(self):
        """
        Gets the issue_type_list of this ServiceCategory.
        List of Issues


        :return: The issue_type_list of this ServiceCategory.
        :rtype: list[IssueType]
        """
        return self._issue_type_list

    @issue_type_list.setter
    def issue_type_list(self, issue_type_list):
        """
        Sets the issue_type_list of this ServiceCategory.
        List of Issues


        :param issue_type_list: The issue_type_list of this ServiceCategory.
        :type: list[IssueType]
        """
        self._issue_type_list = issue_type_list

    @property
    def scope(self):
        """
        Gets the scope of this ServiceCategory.
        List of Scope

        Allowed values for this property are: "AD", "REGION", "TENANCY", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this ServiceCategory.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this ServiceCategory.
        List of Scope


        :param scope: The scope of this ServiceCategory.
        :type: str
        """
        allowed_values = ["AD", "REGION", "TENANCY", "NONE"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def unit(self):
        """
        Gets the unit of this ServiceCategory.
        List of Units

        Allowed values for this property are: "COUNT", "GB", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this ServiceCategory.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this ServiceCategory.
        List of Units


        :param unit: The unit of this ServiceCategory.
        :type: str
        """
        allowed_values = ["COUNT", "GB", "NONE"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    @property
    def limit_id(self):
        """
        Gets the limit_id of this ServiceCategory.
        Limit's unique id


        :return: The limit_id of this ServiceCategory.
        :rtype: str
        """
        return self._limit_id

    @limit_id.setter
    def limit_id(self, limit_id):
        """
        Sets the limit_id of this ServiceCategory.
        Limit's unique id


        :param limit_id: The limit_id of this ServiceCategory.
        :type: str
        """
        self._limit_id = limit_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
