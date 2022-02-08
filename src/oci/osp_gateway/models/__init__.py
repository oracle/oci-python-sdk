# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .authorize_subscription_payment_details import AuthorizeSubscriptionPaymentDetails
from .authorize_subscription_payment_receipt import AuthorizeSubscriptionPaymentReceipt
from .bill_to_address import BillToAddress
from .billing_address import BillingAddress
from .country import Country
from .credit_card_payment_detail import CreditCardPaymentDetail
from .credit_card_payment_option import CreditCardPaymentOption
from .currency import Currency
from .invoice import Invoice
from .invoice_collection import InvoiceCollection
from .invoice_line_collection import InvoiceLineCollection
from .invoice_line_summary import InvoiceLineSummary
from .invoice_summary import InvoiceSummary
from .merchant_defined_data import MerchantDefinedData
from .other_payment_detail import OtherPaymentDetail
from .pay_invoice_details import PayInvoiceDetails
from .pay_invoice_receipt import PayInvoiceReceipt
from .pay_subscription_details import PaySubscriptionDetails
from .pay_subscription_receipt import PaySubscriptionReceipt
from .payment_detail import PaymentDetail
from .payment_gateway import PaymentGateway
from .payment_option import PaymentOption
from .paypal_payment_detail import PaypalPaymentDetail
from .paypal_payment_option import PaypalPaymentOption
from .subscription import Subscription
from .subscription_collection import SubscriptionCollection
from .subscription_summary import SubscriptionSummary
from .tax_info import TaxInfo
from .update_subscription_details import UpdateSubscriptionDetails

# Maps type names to classes for osp_gateway services.
osp_gateway_type_mapping = {
    "AuthorizeSubscriptionPaymentDetails": AuthorizeSubscriptionPaymentDetails,
    "AuthorizeSubscriptionPaymentReceipt": AuthorizeSubscriptionPaymentReceipt,
    "BillToAddress": BillToAddress,
    "BillingAddress": BillingAddress,
    "Country": Country,
    "CreditCardPaymentDetail": CreditCardPaymentDetail,
    "CreditCardPaymentOption": CreditCardPaymentOption,
    "Currency": Currency,
    "Invoice": Invoice,
    "InvoiceCollection": InvoiceCollection,
    "InvoiceLineCollection": InvoiceLineCollection,
    "InvoiceLineSummary": InvoiceLineSummary,
    "InvoiceSummary": InvoiceSummary,
    "MerchantDefinedData": MerchantDefinedData,
    "OtherPaymentDetail": OtherPaymentDetail,
    "PayInvoiceDetails": PayInvoiceDetails,
    "PayInvoiceReceipt": PayInvoiceReceipt,
    "PaySubscriptionDetails": PaySubscriptionDetails,
    "PaySubscriptionReceipt": PaySubscriptionReceipt,
    "PaymentDetail": PaymentDetail,
    "PaymentGateway": PaymentGateway,
    "PaymentOption": PaymentOption,
    "PaypalPaymentDetail": PaypalPaymentDetail,
    "PaypalPaymentOption": PaypalPaymentOption,
    "Subscription": Subscription,
    "SubscriptionCollection": SubscriptionCollection,
    "SubscriptionSummary": SubscriptionSummary,
    "TaxInfo": TaxInfo,
    "UpdateSubscriptionDetails": UpdateSubscriptionDetails
}
