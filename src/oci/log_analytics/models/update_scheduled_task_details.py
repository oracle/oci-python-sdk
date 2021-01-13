# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateScheduledTaskDetails(object):
    """
    The details for updating a schedule task.
    """

    #: A constant which can be used with the kind property of a UpdateScheduledTaskDetails.
    #: This constant has a value of "ACCELERATION"
    KIND_ACCELERATION = "ACCELERATION"

    #: A constant which can be used with the kind property of a UpdateScheduledTaskDetails.
    #: This constant has a value of "STANDARD"
    KIND_STANDARD = "STANDARD"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateScheduledTaskDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.log_analytics.models.UpdateStandardTaskDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this UpdateScheduledTaskDetails.
            Allowed values for this property are: "ACCELERATION", "STANDARD"
        :type kind: str

        :param display_name:
            The value to assign to the display_name property of this UpdateScheduledTaskDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateScheduledTaskDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateScheduledTaskDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param schedules:
            The value to assign to the schedules property of this UpdateScheduledTaskDetails.
        :type schedules: list[oci.log_analytics.models.Schedule]

        """
        self.swagger_types = {
            'kind': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'schedules': 'list[Schedule]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'schedules': 'schedules'
        }

        self._kind = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._schedules = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'STANDARD':
            return 'UpdateStandardTaskDetails'
        else:
            return 'UpdateScheduledTaskDetails'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this UpdateScheduledTaskDetails.
        Discriminator.

        Allowed values for this property are: "ACCELERATION", "STANDARD"


        :return: The kind of this UpdateScheduledTaskDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this UpdateScheduledTaskDetails.
        Discriminator.


        :param kind: The kind of this UpdateScheduledTaskDetails.
        :type: str
        """
        allowed_values = ["ACCELERATION", "STANDARD"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            raise ValueError(
                "Invalid value for `kind`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._kind = kind

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateScheduledTaskDetails.
        A user-friendly name that is changeable and that does not have to be unique.
        Format: a leading alphanumeric, followed by zero or more
        alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
        No trailing spaces allowed.


        :return: The display_name of this UpdateScheduledTaskDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateScheduledTaskDetails.
        A user-friendly name that is changeable and that does not have to be unique.
        Format: a leading alphanumeric, followed by zero or more
        alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
        No trailing spaces allowed.


        :param display_name: The display_name of this UpdateScheduledTaskDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateScheduledTaskDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateScheduledTaskDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateScheduledTaskDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateScheduledTaskDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateScheduledTaskDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateScheduledTaskDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateScheduledTaskDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateScheduledTaskDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def schedules(self):
        """
        Gets the schedules of this UpdateScheduledTaskDetails.
        Schedules may be updated for task types SAVED_SEARCH and PURGE.
        Note there may only be a single schedule for SAVED_SEARCH and PURGE scheduled tasks.


        :return: The schedules of this UpdateScheduledTaskDetails.
        :rtype: list[oci.log_analytics.models.Schedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this UpdateScheduledTaskDetails.
        Schedules may be updated for task types SAVED_SEARCH and PURGE.
        Note there may only be a single schedule for SAVED_SEARCH and PURGE scheduled tasks.


        :param schedules: The schedules of this UpdateScheduledTaskDetails.
        :type: list[oci.log_analytics.models.Schedule]
        """
        self._schedules = schedules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
