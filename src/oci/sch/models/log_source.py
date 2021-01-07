# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogSource(object):
    """
    The log source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogSource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this LogSource.
        :type compartment_id: str

        :param log_group_id:
            The value to assign to the log_group_id property of this LogSource.
        :type log_group_id: str

        :param log_id:
            The value to assign to the log_id property of this LogSource.
        :type log_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'log_group_id': 'str',
            'log_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'log_group_id': 'logGroupId',
            'log_id': 'logId'
        }

        self._compartment_id = None
        self._log_group_id = None
        self._log_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogSource.
        The `OCID`__ of the compartment containing the log source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogSource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogSource.
        The `OCID`__ of the compartment containing the log source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogSource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this LogSource.
        The `OCID`__ of the log group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The log_group_id of this LogSource.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this LogSource.
        The `OCID`__ of the log group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param log_group_id: The log_group_id of this LogSource.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_id(self):
        """
        Gets the log_id of this LogSource.
        The `OCID`__ of the log.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The log_id of this LogSource.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """
        Sets the log_id of this LogSource.
        The `OCID`__ of the log.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param log_id: The log_id of this LogSource.
        :type: str
        """
        self._log_id = log_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
