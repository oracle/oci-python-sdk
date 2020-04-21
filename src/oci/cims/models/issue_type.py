# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IssueType(object):
    """
    Details Issue Type of the incident
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IssueType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param issue_type_key:
            The value to assign to the issue_type_key property of this IssueType.
        :type issue_type_key: str

        :param label:
            The value to assign to the label property of this IssueType.
        :type label: str

        """
        self.swagger_types = {
            'issue_type_key': 'str',
            'label': 'str'
        }

        self.attribute_map = {
            'issue_type_key': 'issueTypeKey',
            'label': 'label'
        }

        self._issue_type_key = None
        self._label = None

    @property
    def issue_type_key(self):
        """
        Gets the issue_type_key of this IssueType.
        Unique ID that identifies an Issue Type


        :return: The issue_type_key of this IssueType.
        :rtype: str
        """
        return self._issue_type_key

    @issue_type_key.setter
    def issue_type_key(self, issue_type_key):
        """
        Sets the issue_type_key of this IssueType.
        Unique ID that identifies an Issue Type


        :param issue_type_key: The issue_type_key of this IssueType.
        :type: str
        """
        self._issue_type_key = issue_type_key

    @property
    def label(self):
        """
        Gets the label of this IssueType.
        Label of issue type. eg: Instance Performance


        :return: The label of this IssueType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this IssueType.
        Label of issue type. eg: Instance Performance


        :param label: The label of this IssueType.
        :type: str
        """
        self._label = label

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
