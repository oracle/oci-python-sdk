# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeDatabaseParameterDetails(object):
    """
    The value of a database parameter to change.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeDatabaseParameterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ChangeDatabaseParameterDetails.
        :type name: str

        :param value:
            The value to assign to the value property of this ChangeDatabaseParameterDetails.
        :type value: str

        :param update_comment:
            The value to assign to the update_comment property of this ChangeDatabaseParameterDetails.
        :type update_comment: str

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'update_comment': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'update_comment': 'updateComment'
        }

        self._name = None
        self._value = None
        self._update_comment = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ChangeDatabaseParameterDetails.
        The parameter name.


        :return: The name of this ChangeDatabaseParameterDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ChangeDatabaseParameterDetails.
        The parameter name.


        :param name: The name of this ChangeDatabaseParameterDetails.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ChangeDatabaseParameterDetails.
        The parameter value.


        :return: The value of this ChangeDatabaseParameterDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ChangeDatabaseParameterDetails.
        The parameter value.


        :param value: The value of this ChangeDatabaseParameterDetails.
        :type: str
        """
        self._value = value

    @property
    def update_comment(self):
        """
        Gets the update_comment of this ChangeDatabaseParameterDetails.
        A comment string to associate with the change in parameter value.
        It cannot contain control characters or a line break.


        :return: The update_comment of this ChangeDatabaseParameterDetails.
        :rtype: str
        """
        return self._update_comment

    @update_comment.setter
    def update_comment(self, update_comment):
        """
        Sets the update_comment of this ChangeDatabaseParameterDetails.
        A comment string to associate with the change in parameter value.
        It cannot contain control characters or a line break.


        :param update_comment: The update_comment of this ChangeDatabaseParameterDetails.
        :type: str
        """
        self._update_comment = update_comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
