# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbParameterChangeAggregation(object):
    """
    Change record for AWR database parameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbParameterChangeAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AddmDbParameterChangeAggregation.
        :type id: str

        :param time_begin:
            The value to assign to the time_begin property of this AddmDbParameterChangeAggregation.
        :type time_begin: datetime

        :param time_end:
            The value to assign to the time_end property of this AddmDbParameterChangeAggregation.
        :type time_end: datetime

        :param inst_num:
            The value to assign to the inst_num property of this AddmDbParameterChangeAggregation.
        :type inst_num: int

        :param previous_value:
            The value to assign to the previous_value property of this AddmDbParameterChangeAggregation.
        :type previous_value: str

        :param value:
            The value to assign to the value property of this AddmDbParameterChangeAggregation.
        :type value: str

        :param snapshot_id:
            The value to assign to the snapshot_id property of this AddmDbParameterChangeAggregation.
        :type snapshot_id: int

        """
        self.swagger_types = {
            'id': 'str',
            'time_begin': 'datetime',
            'time_end': 'datetime',
            'inst_num': 'int',
            'previous_value': 'str',
            'value': 'str',
            'snapshot_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'time_begin': 'timeBegin',
            'time_end': 'timeEnd',
            'inst_num': 'instNum',
            'previous_value': 'previousValue',
            'value': 'value',
            'snapshot_id': 'snapshotId'
        }

        self._id = None
        self._time_begin = None
        self._time_end = None
        self._inst_num = None
        self._previous_value = None
        self._value = None
        self._snapshot_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AddmDbParameterChangeAggregation.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this AddmDbParameterChangeAggregation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddmDbParameterChangeAggregation.
        The `OCID`__ of the Database insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this AddmDbParameterChangeAggregation.
        :type: str
        """
        self._id = id

    @property
    def time_begin(self):
        """
        **[Required]** Gets the time_begin of this AddmDbParameterChangeAggregation.
        Begin time of interval which includes change


        :return: The time_begin of this AddmDbParameterChangeAggregation.
        :rtype: datetime
        """
        return self._time_begin

    @time_begin.setter
    def time_begin(self, time_begin):
        """
        Sets the time_begin of this AddmDbParameterChangeAggregation.
        Begin time of interval which includes change


        :param time_begin: The time_begin of this AddmDbParameterChangeAggregation.
        :type: datetime
        """
        self._time_begin = time_begin

    @property
    def time_end(self):
        """
        **[Required]** Gets the time_end of this AddmDbParameterChangeAggregation.
        End time of interval which includes change


        :return: The time_end of this AddmDbParameterChangeAggregation.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this AddmDbParameterChangeAggregation.
        End time of interval which includes change


        :param time_end: The time_end of this AddmDbParameterChangeAggregation.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def inst_num(self):
        """
        **[Required]** Gets the inst_num of this AddmDbParameterChangeAggregation.
        Instance number


        :return: The inst_num of this AddmDbParameterChangeAggregation.
        :rtype: int
        """
        return self._inst_num

    @inst_num.setter
    def inst_num(self, inst_num):
        """
        Sets the inst_num of this AddmDbParameterChangeAggregation.
        Instance number


        :param inst_num: The inst_num of this AddmDbParameterChangeAggregation.
        :type: int
        """
        self._inst_num = inst_num

    @property
    def previous_value(self):
        """
        Gets the previous_value of this AddmDbParameterChangeAggregation.
        Previous value


        :return: The previous_value of this AddmDbParameterChangeAggregation.
        :rtype: str
        """
        return self._previous_value

    @previous_value.setter
    def previous_value(self, previous_value):
        """
        Sets the previous_value of this AddmDbParameterChangeAggregation.
        Previous value


        :param previous_value: The previous_value of this AddmDbParameterChangeAggregation.
        :type: str
        """
        self._previous_value = previous_value

    @property
    def value(self):
        """
        Gets the value of this AddmDbParameterChangeAggregation.
        Current value


        :return: The value of this AddmDbParameterChangeAggregation.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AddmDbParameterChangeAggregation.
        Current value


        :param value: The value of this AddmDbParameterChangeAggregation.
        :type: str
        """
        self._value = value

    @property
    def snapshot_id(self):
        """
        **[Required]** Gets the snapshot_id of this AddmDbParameterChangeAggregation.
        AWR snapshot id which includes the parameter value change


        :return: The snapshot_id of this AddmDbParameterChangeAggregation.
        :rtype: int
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """
        Sets the snapshot_id of this AddmDbParameterChangeAggregation.
        AWR snapshot id which includes the parameter value change


        :param snapshot_id: The snapshot_id of this AddmDbParameterChangeAggregation.
        :type: int
        """
        self._snapshot_id = snapshot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
