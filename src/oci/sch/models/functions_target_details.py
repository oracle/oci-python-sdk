# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionsTargetDetails(TargetDetails):
    """
    The function used for the Functions target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionsTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.FunctionsTargetDetails.kind` attribute
        of this class is ``functions`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this FunctionsTargetDetails.
            Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming"
        :type kind: str

        :param function_id:
            The value to assign to the function_id property of this FunctionsTargetDetails.
        :type function_id: str

        """
        self.swagger_types = {
            'kind': 'str',
            'function_id': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'function_id': 'functionId'
        }

        self._kind = None
        self._function_id = None
        self._kind = 'functions'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this FunctionsTargetDetails.
        The `OCID`__ of the function.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The function_id of this FunctionsTargetDetails.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this FunctionsTargetDetails.
        The `OCID`__ of the function.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this FunctionsTargetDetails.
        :type: str
        """
        self._function_id = function_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
