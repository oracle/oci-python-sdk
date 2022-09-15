# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduleDetails(object):
    """
    Details for updating the custom table.
    """

    #: A constant which can be used with the output_file_format property of a UpdateScheduleDetails.
    #: This constant has a value of "CSV"
    OUTPUT_FILE_FORMAT_CSV = "CSV"

    #: A constant which can be used with the output_file_format property of a UpdateScheduleDetails.
    #: This constant has a value of "PDF"
    OUTPUT_FILE_FORMAT_PDF = "PDF"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateScheduleDetails.
        :type description: str

        :param output_file_format:
            The value to assign to the output_file_format property of this UpdateScheduleDetails.
            Allowed values for this property are: "CSV", "PDF"
        :type output_file_format: str

        :param result_location:
            The value to assign to the result_location property of this UpdateScheduleDetails.
        :type result_location: oci.usage_api.models.ResultLocation

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateScheduleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateScheduleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'output_file_format': 'str',
            'result_location': 'ResultLocation',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'output_file_format': 'outputFileFormat',
            'result_location': 'resultLocation',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._output_file_format = None
        self._result_location = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateScheduleDetails.
        The description of the schedule.


        :return: The description of this UpdateScheduleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateScheduleDetails.
        The description of the schedule.


        :param description: The description of this UpdateScheduleDetails.
        :type: str
        """
        self._description = description

    @property
    def output_file_format(self):
        """
        Gets the output_file_format of this UpdateScheduleDetails.
        Specifies supported output file format.

        Allowed values for this property are: "CSV", "PDF"


        :return: The output_file_format of this UpdateScheduleDetails.
        :rtype: str
        """
        return self._output_file_format

    @output_file_format.setter
    def output_file_format(self, output_file_format):
        """
        Sets the output_file_format of this UpdateScheduleDetails.
        Specifies supported output file format.


        :param output_file_format: The output_file_format of this UpdateScheduleDetails.
        :type: str
        """
        allowed_values = ["CSV", "PDF"]
        if not value_allowed_none_or_none_sentinel(output_file_format, allowed_values):
            raise ValueError(
                "Invalid value for `output_file_format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._output_file_format = output_file_format

    @property
    def result_location(self):
        """
        Gets the result_location of this UpdateScheduleDetails.

        :return: The result_location of this UpdateScheduleDetails.
        :rtype: oci.usage_api.models.ResultLocation
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """
        Sets the result_location of this UpdateScheduleDetails.

        :param result_location: The result_location of this UpdateScheduleDetails.
        :type: oci.usage_api.models.ResultLocation
        """
        self._result_location = result_location

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateScheduleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateScheduleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateScheduleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateScheduleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateScheduleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateScheduleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateScheduleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateScheduleDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
