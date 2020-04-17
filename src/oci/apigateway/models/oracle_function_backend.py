# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .api_specification_route_backend import ApiSpecificationRouteBackend
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleFunctionBackend(ApiSpecificationRouteBackend):
    """
    Send the request to an Oracle Functions function.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleFunctionBackend object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.OracleFunctionBackend.type` attribute
        of this class is ``ORACLE_FUNCTIONS_BACKEND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OracleFunctionBackend.
            Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND"
        :type type: str

        :param function_id:
            The value to assign to the function_id property of this OracleFunctionBackend.
        :type function_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'function_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'function_id': 'functionId'
        }

        self._type = None
        self._function_id = None
        self._type = 'ORACLE_FUNCTIONS_BACKEND'

    @property
    def function_id(self):
        """
        **[Required]** Gets the function_id of this OracleFunctionBackend.
        The `OCID`__ of the Oracle Functions function resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The function_id of this OracleFunctionBackend.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this OracleFunctionBackend.
        The `OCID`__ of the Oracle Functions function resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param function_id: The function_id of this OracleFunctionBackend.
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
