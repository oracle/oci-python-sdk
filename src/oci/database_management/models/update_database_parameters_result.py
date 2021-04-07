# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDatabaseParametersResult(object):
    """
    The results of database parameter update.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDatabaseParametersResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateDatabaseParametersResult.
        :type status: dict(str, DatabaseParameterUpdateStatus)

        """
        self.swagger_types = {
            'status': 'dict(str, DatabaseParameterUpdateStatus)'
        }

        self.attribute_map = {
            'status': 'status'
        }

        self._status = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateDatabaseParametersResult.
        A map with the parameter name as key and its update status as value.


        :return: The status of this UpdateDatabaseParametersResult.
        :rtype: dict(str, DatabaseParameterUpdateStatus)
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateDatabaseParametersResult.
        A map with the parameter name as key and its update status as value.


        :param status: The status of this UpdateDatabaseParametersResult.
        :type: dict(str, DatabaseParameterUpdateStatus)
        """
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
