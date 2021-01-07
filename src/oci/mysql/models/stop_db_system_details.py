# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StopDbSystemDetails(object):
    """
    DB System shutdown parameters.
    """

    #: A constant which can be used with the shutdown_type property of a StopDbSystemDetails.
    #: This constant has a value of "IMMEDIATE"
    SHUTDOWN_TYPE_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the shutdown_type property of a StopDbSystemDetails.
    #: This constant has a value of "FAST"
    SHUTDOWN_TYPE_FAST = "FAST"

    #: A constant which can be used with the shutdown_type property of a StopDbSystemDetails.
    #: This constant has a value of "SLOW"
    SHUTDOWN_TYPE_SLOW = "SLOW"

    def __init__(self, **kwargs):
        """
        Initializes a new StopDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shutdown_type:
            The value to assign to the shutdown_type property of this StopDbSystemDetails.
            Allowed values for this property are: "IMMEDIATE", "FAST", "SLOW"
        :type shutdown_type: str

        """
        self.swagger_types = {
            'shutdown_type': 'str'
        }

        self.attribute_map = {
            'shutdown_type': 'shutdownType'
        }

        self._shutdown_type = None

    @property
    def shutdown_type(self):
        """
        **[Required]** Gets the shutdown_type of this StopDbSystemDetails.
        The InnoDB shutdown mode to use, following the option
        \"`innodb_fast_shutdown`__\".

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_fast_shutdown

        Allowed values for this property are: "IMMEDIATE", "FAST", "SLOW"


        :return: The shutdown_type of this StopDbSystemDetails.
        :rtype: str
        """
        return self._shutdown_type

    @shutdown_type.setter
    def shutdown_type(self, shutdown_type):
        """
        Sets the shutdown_type of this StopDbSystemDetails.
        The InnoDB shutdown mode to use, following the option
        \"`innodb_fast_shutdown`__\".

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_fast_shutdown


        :param shutdown_type: The shutdown_type of this StopDbSystemDetails.
        :type: str
        """
        allowed_values = ["IMMEDIATE", "FAST", "SLOW"]
        if not value_allowed_none_or_none_sentinel(shutdown_type, allowed_values):
            raise ValueError(
                "Invalid value for `shutdown_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._shutdown_type = shutdown_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
