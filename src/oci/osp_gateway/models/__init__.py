# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .address import Address
from .country import Country
from .credit_card_payment_detail import CreditCardPaymentDetail
from .currency import Currency
from .invoice import Invoice
from .invoice_collection import InvoiceCollection
from .invoice_line_collection import InvoiceLineCollection
from .invoice_line_summary import InvoiceLineSummary
from .invoice_summary import InvoiceSummary
from .other_payment_detail import OtherPaymentDetail
from .pay_invoice_details import PayInvoiceDetails
from .pay_invoice_receipt import PayInvoiceReceipt
from .payment_detail import PaymentDetail
from .paypal_payment_detail import PaypalPaymentDetail

# Maps type names to classes for osp_gateway services.
osp_gateway_type_mapping = {
    "Address": Address,
    "Country": Country,
    "CreditCardPaymentDetail": CreditCardPaymentDetail,
    "Currency": Currency,
    "Invoice": Invoice,
    "InvoiceCollection": InvoiceCollection,
    "InvoiceLineCollection": InvoiceLineCollection,
    "InvoiceLineSummary": InvoiceLineSummary,
    "InvoiceSummary": InvoiceSummary,
    "OtherPaymentDetail": OtherPaymentDetail,
    "PayInvoiceDetails": PayInvoiceDetails,
    "PayInvoiceReceipt": PayInvoiceReceipt,
    "PaymentDetail": PaymentDetail,
    "PaypalPaymentDetail": PaypalPaymentDetail
}
