# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoiceLineSummary(object):
    """
    Invoice Line
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvoiceLineSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InvoiceLineSummary.
        :type id: str

        :param product:
            The value to assign to the product property of this InvoiceLineSummary.
        :type product: oci.onesubscription.models.InvoicingProduct

        :param ar_invoice_number:
            The value to assign to the ar_invoice_number property of this InvoiceLineSummary.
        :type ar_invoice_number: str

        :param data_center:
            The value to assign to the data_center property of this InvoiceLineSummary.
        :type data_center: str

        :param time_start:
            The value to assign to the time_start property of this InvoiceLineSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this InvoiceLineSummary.
        :type time_end: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'product': 'InvoicingProduct',
            'ar_invoice_number': 'str',
            'data_center': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'product': 'product',
            'ar_invoice_number': 'arInvoiceNumber',
            'data_center': 'dataCenter',
            'time_start': 'timeStart',
            'time_end': 'timeEnd'
        }

        self._id = None
        self._product = None
        self._ar_invoice_number = None
        self._data_center = None
        self._time_start = None
        self._time_end = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InvoiceLineSummary.
        SPM Invoice Line internal identifier


        :return: The id of this InvoiceLineSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InvoiceLineSummary.
        SPM Invoice Line internal identifier


        :param id: The id of this InvoiceLineSummary.
        :type: str
        """
        self._id = id

    @property
    def product(self):
        """
        **[Required]** Gets the product of this InvoiceLineSummary.

        :return: The product of this InvoiceLineSummary.
        :rtype: oci.onesubscription.models.InvoicingProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this InvoiceLineSummary.

        :param product: The product of this InvoiceLineSummary.
        :type: oci.onesubscription.models.InvoicingProduct
        """
        self._product = product

    @property
    def ar_invoice_number(self):
        """
        Gets the ar_invoice_number of this InvoiceLineSummary.
        AR Invoice Number for Invoice Line


        :return: The ar_invoice_number of this InvoiceLineSummary.
        :rtype: str
        """
        return self._ar_invoice_number

    @ar_invoice_number.setter
    def ar_invoice_number(self, ar_invoice_number):
        """
        Sets the ar_invoice_number of this InvoiceLineSummary.
        AR Invoice Number for Invoice Line


        :param ar_invoice_number: The ar_invoice_number of this InvoiceLineSummary.
        :type: str
        """
        self._ar_invoice_number = ar_invoice_number

    @property
    def data_center(self):
        """
        **[Required]** Gets the data_center of this InvoiceLineSummary.
        Data Center Attribute.


        :return: The data_center of this InvoiceLineSummary.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """
        Sets the data_center of this InvoiceLineSummary.
        Data Center Attribute.


        :param data_center: The data_center of this InvoiceLineSummary.
        :type: str
        """
        self._data_center = data_center

    @property
    def time_start(self):
        """
        **[Required]** Gets the time_start of this InvoiceLineSummary.
        Usage start time


        :return: The time_start of this InvoiceLineSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this InvoiceLineSummary.
        Usage start time


        :param time_start: The time_start of this InvoiceLineSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        **[Required]** Gets the time_end of this InvoiceLineSummary.
        Usage end time


        :return: The time_end of this InvoiceLineSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this InvoiceLineSummary.
        Usage end time


        :param time_end: The time_end of this InvoiceLineSummary.
        :type: datetime
        """
        self._time_end = time_end

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
