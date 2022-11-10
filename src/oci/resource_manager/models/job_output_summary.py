# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobOutputSummary(object):
    """
    Terraform output associated with a job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobOutputSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_name:
            The value to assign to the output_name property of this JobOutputSummary.
        :type output_name: str

        :param output_type:
            The value to assign to the output_type property of this JobOutputSummary.
        :type output_type: str

        :param output_value:
            The value to assign to the output_value property of this JobOutputSummary.
        :type output_value: str

        :param is_sensitive:
            The value to assign to the is_sensitive property of this JobOutputSummary.
        :type is_sensitive: bool

        :param description:
            The value to assign to the description property of this JobOutputSummary.
        :type description: str

        """
        self.swagger_types = {
            'output_name': 'str',
            'output_type': 'str',
            'output_value': 'str',
            'is_sensitive': 'bool',
            'description': 'str'
        }

        self.attribute_map = {
            'output_name': 'outputName',
            'output_type': 'outputType',
            'output_value': 'outputValue',
            'is_sensitive': 'isSensitive',
            'description': 'description'
        }

        self._output_name = None
        self._output_type = None
        self._output_value = None
        self._is_sensitive = None
        self._description = None

    @property
    def output_name(self):
        """
        Gets the output_name of this JobOutputSummary.
        Name of the output.


        :return: The output_name of this JobOutputSummary.
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        """
        Sets the output_name of this JobOutputSummary.
        Name of the output.


        :param output_name: The output_name of this JobOutputSummary.
        :type: str
        """
        self._output_name = output_name

    @property
    def output_type(self):
        """
        Gets the output_type of this JobOutputSummary.
        Output resource type.


        :return: The output_type of this JobOutputSummary.
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """
        Sets the output_type of this JobOutputSummary.
        Output resource type.


        :param output_type: The output_type of this JobOutputSummary.
        :type: str
        """
        self._output_type = output_type

    @property
    def output_value(self):
        """
        Gets the output_value of this JobOutputSummary.
        Value of the Terraform output.


        :return: The output_value of this JobOutputSummary.
        :rtype: str
        """
        return self._output_value

    @output_value.setter
    def output_value(self, output_value):
        """
        Sets the output_value of this JobOutputSummary.
        Value of the Terraform output.


        :param output_value: The output_value of this JobOutputSummary.
        :type: str
        """
        self._output_value = output_value

    @property
    def is_sensitive(self):
        """
        Gets the is_sensitive of this JobOutputSummary.
        When `true`, output is sensitive.


        :return: The is_sensitive of this JobOutputSummary.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """
        Sets the is_sensitive of this JobOutputSummary.
        When `true`, output is sensitive.


        :param is_sensitive: The is_sensitive of this JobOutputSummary.
        :type: bool
        """
        self._is_sensitive = is_sensitive

    @property
    def description(self):
        """
        Gets the description of this JobOutputSummary.
        Description of the output.


        :return: The description of this JobOutputSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JobOutputSummary.
        Description of the output.


        :param description: The description of this JobOutputSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
