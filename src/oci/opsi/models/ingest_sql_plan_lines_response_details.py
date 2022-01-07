# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngestSqlPlanLinesResponseDetails(object):
    """
    The response object returned from IngestSqlPlanLines operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngestSqlPlanLinesResponseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this IngestSqlPlanLinesResponseDetails.
        :type message: str

        """
        self.swagger_types = {
            'message': 'str'
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = None

    @property
    def message(self):
        """
        **[Required]** Gets the message of this IngestSqlPlanLinesResponseDetails.
        Success message returned as a result of the upload.


        :return: The message of this IngestSqlPlanLinesResponseDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this IngestSqlPlanLinesResponseDetails.
        Success message returned as a result of the upload.


        :param message: The message of this IngestSqlPlanLinesResponseDetails.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
