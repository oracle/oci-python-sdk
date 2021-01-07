# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .api_specification_route_backend import ApiSpecificationRouteBackend
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StockResponseBackend(ApiSpecificationRouteBackend):
    """
    Send the request to a mock backend.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StockResponseBackend object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.StockResponseBackend.type` attribute
        of this class is ``STOCK_RESPONSE_BACKEND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StockResponseBackend.
            Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND"
        :type type: str

        :param body:
            The value to assign to the body property of this StockResponseBackend.
        :type body: str

        :param status:
            The value to assign to the status property of this StockResponseBackend.
        :type status: int

        :param headers:
            The value to assign to the headers property of this StockResponseBackend.
        :type headers: list[oci.apigateway.models.HeaderFieldSpecification]

        """
        self.swagger_types = {
            'type': 'str',
            'body': 'str',
            'status': 'int',
            'headers': 'list[HeaderFieldSpecification]'
        }

        self.attribute_map = {
            'type': 'type',
            'body': 'body',
            'status': 'status',
            'headers': 'headers'
        }

        self._type = None
        self._body = None
        self._status = None
        self._headers = None
        self._type = 'STOCK_RESPONSE_BACKEND'

    @property
    def body(self):
        """
        Gets the body of this StockResponseBackend.
        The body of the stock response from the mock backend.


        :return: The body of this StockResponseBackend.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this StockResponseBackend.
        The body of the stock response from the mock backend.


        :param body: The body of this StockResponseBackend.
        :type: str
        """
        self._body = body

    @property
    def status(self):
        """
        **[Required]** Gets the status of this StockResponseBackend.
        The status code of the stock response from the mock backend.


        :return: The status of this StockResponseBackend.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StockResponseBackend.
        The status code of the stock response from the mock backend.


        :param status: The status of this StockResponseBackend.
        :type: int
        """
        self._status = status

    @property
    def headers(self):
        """
        Gets the headers of this StockResponseBackend.
        The headers of the stock response from the mock backend.


        :return: The headers of this StockResponseBackend.
        :rtype: list[oci.apigateway.models.HeaderFieldSpecification]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this StockResponseBackend.
        The headers of the stock response from the mock backend.


        :param headers: The headers of this StockResponseBackend.
        :type: list[oci.apigateway.models.HeaderFieldSpecification]
        """
        self._headers = headers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
