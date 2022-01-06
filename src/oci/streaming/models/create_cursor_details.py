# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCursorDetails(object):
    """
    Object used to create a cursor to consume messages in a stream.
    """

    #: A constant which can be used with the type property of a CreateCursorDetails.
    #: This constant has a value of "AFTER_OFFSET"
    TYPE_AFTER_OFFSET = "AFTER_OFFSET"

    #: A constant which can be used with the type property of a CreateCursorDetails.
    #: This constant has a value of "AT_OFFSET"
    TYPE_AT_OFFSET = "AT_OFFSET"

    #: A constant which can be used with the type property of a CreateCursorDetails.
    #: This constant has a value of "AT_TIME"
    TYPE_AT_TIME = "AT_TIME"

    #: A constant which can be used with the type property of a CreateCursorDetails.
    #: This constant has a value of "LATEST"
    TYPE_LATEST = "LATEST"

    #: A constant which can be used with the type property of a CreateCursorDetails.
    #: This constant has a value of "TRIM_HORIZON"
    TYPE_TRIM_HORIZON = "TRIM_HORIZON"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCursorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param partition:
            The value to assign to the partition property of this CreateCursorDetails.
        :type partition: str

        :param type:
            The value to assign to the type property of this CreateCursorDetails.
            Allowed values for this property are: "AFTER_OFFSET", "AT_OFFSET", "AT_TIME", "LATEST", "TRIM_HORIZON"
        :type type: str

        :param offset:
            The value to assign to the offset property of this CreateCursorDetails.
        :type offset: int

        :param time:
            The value to assign to the time property of this CreateCursorDetails.
        :type time: datetime

        """
        self.swagger_types = {
            'partition': 'str',
            'type': 'str',
            'offset': 'int',
            'time': 'datetime'
        }

        self.attribute_map = {
            'partition': 'partition',
            'type': 'type',
            'offset': 'offset',
            'time': 'time'
        }

        self._partition = None
        self._type = None
        self._offset = None
        self._time = None

    @property
    def partition(self):
        """
        **[Required]** Gets the partition of this CreateCursorDetails.
        The partition to get messages from.


        :return: The partition of this CreateCursorDetails.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this CreateCursorDetails.
        The partition to get messages from.


        :param partition: The partition of this CreateCursorDetails.
        :type: str
        """
        self._partition = partition

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateCursorDetails.
        The type of cursor, which determines the starting point from which the stream will be consumed:

        - `AFTER_OFFSET:` The partition position immediately following the offset you specify. (Offsets are assigned when you successfully append a message to a partition in a stream.)
        - `AT_OFFSET:` The exact partition position indicated by the offset you specify.
        - `AT_TIME:` A specific point in time.
        - `LATEST:` The most recent message in the partition that was added after the cursor was created.
        - `TRIM_HORIZON:` The oldest message in the partition that is within the retention period window.

        Allowed values for this property are: "AFTER_OFFSET", "AT_OFFSET", "AT_TIME", "LATEST", "TRIM_HORIZON"


        :return: The type of this CreateCursorDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateCursorDetails.
        The type of cursor, which determines the starting point from which the stream will be consumed:

        - `AFTER_OFFSET:` The partition position immediately following the offset you specify. (Offsets are assigned when you successfully append a message to a partition in a stream.)
        - `AT_OFFSET:` The exact partition position indicated by the offset you specify.
        - `AT_TIME:` A specific point in time.
        - `LATEST:` The most recent message in the partition that was added after the cursor was created.
        - `TRIM_HORIZON:` The oldest message in the partition that is within the retention period window.


        :param type: The type of this CreateCursorDetails.
        :type: str
        """
        allowed_values = ["AFTER_OFFSET", "AT_OFFSET", "AT_TIME", "LATEST", "TRIM_HORIZON"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def offset(self):
        """
        Gets the offset of this CreateCursorDetails.
        The offset to consume from if the cursor type is `AT_OFFSET` or `AFTER_OFFSET`.


        :return: The offset of this CreateCursorDetails.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this CreateCursorDetails.
        The offset to consume from if the cursor type is `AT_OFFSET` or `AFTER_OFFSET`.


        :param offset: The offset of this CreateCursorDetails.
        :type: int
        """
        self._offset = offset

    @property
    def time(self):
        """
        Gets the time of this CreateCursorDetails.
        The time to consume from if the cursor type is `AT_TIME`, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time of this CreateCursorDetails.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this CreateCursorDetails.
        The time to consume from if the cursor type is `AT_TIME`, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time: The time of this CreateCursorDetails.
        :type: datetime
        """
        self._time = time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
