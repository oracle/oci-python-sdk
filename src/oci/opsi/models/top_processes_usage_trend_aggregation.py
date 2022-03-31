# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopProcessesUsageTrendAggregation(object):
    """
    Usage data per host top process
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopProcessesUsageTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param command:
            The value to assign to the command property of this TopProcessesUsageTrendAggregation.
        :type command: str

        :param usage_data:
            The value to assign to the usage_data property of this TopProcessesUsageTrendAggregation.
        :type usage_data: list[oci.opsi.models.TopProcessesUsageTrend]

        """
        self.swagger_types = {
            'command': 'str',
            'usage_data': 'list[TopProcessesUsageTrend]'
        }

        self.attribute_map = {
            'command': 'command',
            'usage_data': 'usageData'
        }

        self._command = None
        self._usage_data = None

    @property
    def command(self):
        """
        **[Required]** Gets the command of this TopProcessesUsageTrendAggregation.
        Command line and arguments used to launch process


        :return: The command of this TopProcessesUsageTrendAggregation.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this TopProcessesUsageTrendAggregation.
        Command line and arguments used to launch process


        :param command: The command of this TopProcessesUsageTrendAggregation.
        :type: str
        """
        self._command = command

    @property
    def usage_data(self):
        """
        **[Required]** Gets the usage_data of this TopProcessesUsageTrendAggregation.
        List of usage data samples for a top process


        :return: The usage_data of this TopProcessesUsageTrendAggregation.
        :rtype: list[oci.opsi.models.TopProcessesUsageTrend]
        """
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """
        Sets the usage_data of this TopProcessesUsageTrendAggregation.
        List of usage data samples for a top process


        :param usage_data: The usage_data of this TopProcessesUsageTrendAggregation.
        :type: list[oci.opsi.models.TopProcessesUsageTrend]
        """
        self._usage_data = usage_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
