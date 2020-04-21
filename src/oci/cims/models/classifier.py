# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Classifier(object):
    """
    Incident Classifier details
    """

    #: A constant which can be used with the scope property of a Classifier.
    #: This constant has a value of "AD"
    SCOPE_AD = "AD"

    #: A constant which can be used with the scope property of a Classifier.
    #: This constant has a value of "REGION"
    SCOPE_REGION = "REGION"

    #: A constant which can be used with the scope property of a Classifier.
    #: This constant has a value of "TENANCY"
    SCOPE_TENANCY = "TENANCY"

    #: A constant which can be used with the scope property of a Classifier.
    #: This constant has a value of "NONE"
    SCOPE_NONE = "NONE"

    #: A constant which can be used with the unit property of a Classifier.
    #: This constant has a value of "COUNT"
    UNIT_COUNT = "COUNT"

    #: A constant which can be used with the unit property of a Classifier.
    #: This constant has a value of "GB"
    UNIT_GB = "GB"

    #: A constant which can be used with the unit property of a Classifier.
    #: This constant has a value of "NONE"
    UNIT_NONE = "NONE"

    def __init__(self, **kwargs):
        """
        Initializes a new Classifier object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Classifier.
        :type id: str

        :param name:
            The value to assign to the name property of this Classifier.
        :type name: str

        :param label:
            The value to assign to the label property of this Classifier.
        :type label: str

        :param description:
            The value to assign to the description property of this Classifier.
        :type description: str

        :param issue_type_list:
            The value to assign to the issue_type_list property of this Classifier.
        :type issue_type_list: list[IssueType]

        :param scope:
            The value to assign to the scope property of this Classifier.
            Allowed values for this property are: "AD", "REGION", "TENANCY", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scope: str

        :param unit:
            The value to assign to the unit property of this Classifier.
            Allowed values for this property are: "COUNT", "GB", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'label': 'str',
            'description': 'str',
            'issue_type_list': 'list[IssueType]',
            'scope': 'str',
            'unit': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'label': 'label',
            'description': 'description',
            'issue_type_list': 'issueTypeList',
            'scope': 'scope',
            'unit': 'unit'
        }

        self._id = None
        self._name = None
        self._label = None
        self._description = None
        self._issue_type_list = None
        self._scope = None
        self._unit = None

    @property
    def id(self):
        """
        Gets the id of this Classifier.
        Unique ID that identifies a classifier


        :return: The id of this Classifier.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Classifier.
        Unique ID that identifies a classifier


        :param id: The id of this Classifier.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Classifier.
        Name of classifier. eg: LIMIT Increase


        :return: The name of this Classifier.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Classifier.
        Name of classifier. eg: LIMIT Increase


        :param name: The name of this Classifier.
        :type: str
        """
        self._name = name

    @property
    def label(self):
        """
        Gets the label of this Classifier.
        Label of classifier


        :return: The label of this Classifier.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Classifier.
        Label of classifier


        :param label: The label of this Classifier.
        :type: str
        """
        self._label = label

    @property
    def description(self):
        """
        Gets the description of this Classifier.
        Description of classifier


        :return: The description of this Classifier.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Classifier.
        Description of classifier


        :param description: The description of this Classifier.
        :type: str
        """
        self._description = description

    @property
    def issue_type_list(self):
        """
        Gets the issue_type_list of this Classifier.
        List of Issues


        :return: The issue_type_list of this Classifier.
        :rtype: list[IssueType]
        """
        return self._issue_type_list

    @issue_type_list.setter
    def issue_type_list(self, issue_type_list):
        """
        Sets the issue_type_list of this Classifier.
        List of Issues


        :param issue_type_list: The issue_type_list of this Classifier.
        :type: list[IssueType]
        """
        self._issue_type_list = issue_type_list

    @property
    def scope(self):
        """
        Gets the scope of this Classifier.
        Scope of Service category/resource

        Allowed values for this property are: "AD", "REGION", "TENANCY", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scope of this Classifier.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this Classifier.
        Scope of Service category/resource


        :param scope: The scope of this Classifier.
        :type: str
        """
        allowed_values = ["AD", "REGION", "TENANCY", "NONE"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            scope = 'UNKNOWN_ENUM_VALUE'
        self._scope = scope

    @property
    def unit(self):
        """
        Gets the unit of this Classifier.
        Unit to measure Service category/ resource

        Allowed values for this property are: "COUNT", "GB", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this Classifier.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this Classifier.
        Unit to measure Service category/ resource


        :param unit: The unit of this Classifier.
        :type: str
        """
        allowed_values = ["COUNT", "GB", "NONE"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
