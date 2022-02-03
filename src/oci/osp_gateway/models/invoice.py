# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Invoice(object):
    """
    Invoice details
    """

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "HARDWARE"
    INVOICE_TYPE_HARDWARE = "HARDWARE"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "SUBSCRIPTION"
    INVOICE_TYPE_SUBSCRIPTION = "SUBSCRIPTION"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "SUPPORT"
    INVOICE_TYPE_SUPPORT = "SUPPORT"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "LICENSE"
    INVOICE_TYPE_LICENSE = "LICENSE"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "EDUCATION"
    INVOICE_TYPE_EDUCATION = "EDUCATION"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "CONSULTING"
    INVOICE_TYPE_CONSULTING = "CONSULTING"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "SERVICE"
    INVOICE_TYPE_SERVICE = "SERVICE"

    #: A constant which can be used with the invoice_type property of a Invoice.
    #: This constant has a value of "USAGE"
    INVOICE_TYPE_USAGE = "USAGE"

    #: A constant which can be used with the invoice_status property of a Invoice.
    #: This constant has a value of "OPEN"
    INVOICE_STATUS_OPEN = "OPEN"

    #: A constant which can be used with the invoice_status property of a Invoice.
    #: This constant has a value of "PAST_DUE"
    INVOICE_STATUS_PAST_DUE = "PAST_DUE"

    #: A constant which can be used with the invoice_status property of a Invoice.
    #: This constant has a value of "PAYMENT_SUBMITTED"
    INVOICE_STATUS_PAYMENT_SUBMITTED = "PAYMENT_SUBMITTED"

    #: A constant which can be used with the invoice_status property of a Invoice.
    #: This constant has a value of "CLOSED"
    INVOICE_STATUS_CLOSED = "CLOSED"

    def __init__(self, **kwargs):
        """
        Initializes a new Invoice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param invoice_id:
            The value to assign to the invoice_id property of this Invoice.
        :type invoice_id: str

        :param invoice_number:
            The value to assign to the invoice_number property of this Invoice.
        :type invoice_number: str

        :param internal_invoice_id:
            The value to assign to the internal_invoice_id property of this Invoice.
        :type internal_invoice_id: str

        :param is_credit_card_payable:
            The value to assign to the is_credit_card_payable property of this Invoice.
        :type is_credit_card_payable: bool

        :param time_invoice:
            The value to assign to the time_invoice property of this Invoice.
        :type time_invoice: datetime

        :param tax:
            The value to assign to the tax property of this Invoice.
        :type tax: float

        :param invoice_amount:
            The value to assign to the invoice_amount property of this Invoice.
        :type invoice_amount: float

        :param invoice_amount_due:
            The value to assign to the invoice_amount_due property of this Invoice.
        :type invoice_amount_due: float

        :param invoice_amount_credited:
            The value to assign to the invoice_amount_credited property of this Invoice.
        :type invoice_amount_credited: float

        :param invoice_amount_adjusted:
            The value to assign to the invoice_amount_adjusted property of this Invoice.
        :type invoice_amount_adjusted: float

        :param invoice_amount_applied:
            The value to assign to the invoice_amount_applied property of this Invoice.
        :type invoice_amount_applied: float

        :param currency:
            The value to assign to the currency property of this Invoice.
        :type currency: oci.osp_gateway.models.Currency

        :param invoice_type:
            The value to assign to the invoice_type property of this Invoice.
            Allowed values for this property are: "HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type invoice_type: str

        :param time_invoice_due:
            The value to assign to the time_invoice_due property of this Invoice.
        :type time_invoice_due: datetime

        :param invoice_ref_number:
            The value to assign to the invoice_ref_number property of this Invoice.
        :type invoice_ref_number: str

        :param invoice_po_number:
            The value to assign to the invoice_po_number property of this Invoice.
        :type invoice_po_number: str

        :param invoice_status:
            The value to assign to the invoice_status property of this Invoice.
            Allowed values for this property are: "OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type invoice_status: str

        :param preferred_email:
            The value to assign to the preferred_email property of this Invoice.
        :type preferred_email: str

        :param is_pdf_email_available:
            The value to assign to the is_pdf_email_available property of this Invoice.
        :type is_pdf_email_available: bool

        :param is_display_download_pdf:
            The value to assign to the is_display_download_pdf property of this Invoice.
        :type is_display_download_pdf: bool

        :param is_payable:
            The value to assign to the is_payable property of this Invoice.
        :type is_payable: bool

        :param payment_terms:
            The value to assign to the payment_terms property of this Invoice.
        :type payment_terms: str

        :param last_payment_detail:
            The value to assign to the last_payment_detail property of this Invoice.
        :type last_payment_detail: oci.osp_gateway.models.PaymentDetail

        :param bill_to_address:
            The value to assign to the bill_to_address property of this Invoice.
        :type bill_to_address: oci.osp_gateway.models.BillToAddress

        :param subscription_ids:
            The value to assign to the subscription_ids property of this Invoice.
        :type subscription_ids: list[str]

        """
        self.swagger_types = {
            'invoice_id': 'str',
            'invoice_number': 'str',
            'internal_invoice_id': 'str',
            'is_credit_card_payable': 'bool',
            'time_invoice': 'datetime',
            'tax': 'float',
            'invoice_amount': 'float',
            'invoice_amount_due': 'float',
            'invoice_amount_credited': 'float',
            'invoice_amount_adjusted': 'float',
            'invoice_amount_applied': 'float',
            'currency': 'Currency',
            'invoice_type': 'str',
            'time_invoice_due': 'datetime',
            'invoice_ref_number': 'str',
            'invoice_po_number': 'str',
            'invoice_status': 'str',
            'preferred_email': 'str',
            'is_pdf_email_available': 'bool',
            'is_display_download_pdf': 'bool',
            'is_payable': 'bool',
            'payment_terms': 'str',
            'last_payment_detail': 'PaymentDetail',
            'bill_to_address': 'BillToAddress',
            'subscription_ids': 'list[str]'
        }

        self.attribute_map = {
            'invoice_id': 'invoiceId',
            'invoice_number': 'invoiceNumber',
            'internal_invoice_id': 'internalInvoiceId',
            'is_credit_card_payable': 'isCreditCardPayable',
            'time_invoice': 'timeInvoice',
            'tax': 'tax',
            'invoice_amount': 'invoiceAmount',
            'invoice_amount_due': 'invoiceAmountDue',
            'invoice_amount_credited': 'invoiceAmountCredited',
            'invoice_amount_adjusted': 'invoiceAmountAdjusted',
            'invoice_amount_applied': 'invoiceAmountApplied',
            'currency': 'currency',
            'invoice_type': 'invoiceType',
            'time_invoice_due': 'timeInvoiceDue',
            'invoice_ref_number': 'invoiceRefNumber',
            'invoice_po_number': 'invoicePoNumber',
            'invoice_status': 'invoiceStatus',
            'preferred_email': 'preferredEmail',
            'is_pdf_email_available': 'isPdfEmailAvailable',
            'is_display_download_pdf': 'isDisplayDownloadPdf',
            'is_payable': 'isPayable',
            'payment_terms': 'paymentTerms',
            'last_payment_detail': 'lastPaymentDetail',
            'bill_to_address': 'billToAddress',
            'subscription_ids': 'subscriptionIds'
        }

        self._invoice_id = None
        self._invoice_number = None
        self._internal_invoice_id = None
        self._is_credit_card_payable = None
        self._time_invoice = None
        self._tax = None
        self._invoice_amount = None
        self._invoice_amount_due = None
        self._invoice_amount_credited = None
        self._invoice_amount_adjusted = None
        self._invoice_amount_applied = None
        self._currency = None
        self._invoice_type = None
        self._time_invoice_due = None
        self._invoice_ref_number = None
        self._invoice_po_number = None
        self._invoice_status = None
        self._preferred_email = None
        self._is_pdf_email_available = None
        self._is_display_download_pdf = None
        self._is_payable = None
        self._payment_terms = None
        self._last_payment_detail = None
        self._bill_to_address = None
        self._subscription_ids = None

    @property
    def invoice_id(self):
        """
        **[Required]** Gets the invoice_id of this Invoice.
        Invoice identifier which is generated on the on-premise sie. Pls note this is not an OCID


        :return: The invoice_id of this Invoice.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this Invoice.
        Invoice identifier which is generated on the on-premise sie. Pls note this is not an OCID


        :param invoice_id: The invoice_id of this Invoice.
        :type: str
        """
        self._invoice_id = invoice_id

    @property
    def invoice_number(self):
        """
        Gets the invoice_number of this Invoice.
        Invoice external reference


        :return: The invoice_number of this Invoice.
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """
        Sets the invoice_number of this Invoice.
        Invoice external reference


        :param invoice_number: The invoice_number of this Invoice.
        :type: str
        """
        self._invoice_number = invoice_number

    @property
    def internal_invoice_id(self):
        """
        Gets the internal_invoice_id of this Invoice.
        Transaction identifier


        :return: The internal_invoice_id of this Invoice.
        :rtype: str
        """
        return self._internal_invoice_id

    @internal_invoice_id.setter
    def internal_invoice_id(self, internal_invoice_id):
        """
        Sets the internal_invoice_id of this Invoice.
        Transaction identifier


        :param internal_invoice_id: The internal_invoice_id of this Invoice.
        :type: str
        """
        self._internal_invoice_id = internal_invoice_id

    @property
    def is_credit_card_payable(self):
        """
        Gets the is_credit_card_payable of this Invoice.
        Is credit card payment eligible


        :return: The is_credit_card_payable of this Invoice.
        :rtype: bool
        """
        return self._is_credit_card_payable

    @is_credit_card_payable.setter
    def is_credit_card_payable(self, is_credit_card_payable):
        """
        Sets the is_credit_card_payable of this Invoice.
        Is credit card payment eligible


        :param is_credit_card_payable: The is_credit_card_payable of this Invoice.
        :type: bool
        """
        self._is_credit_card_payable = is_credit_card_payable

    @property
    def time_invoice(self):
        """
        Gets the time_invoice of this Invoice.
        Date of invoice


        :return: The time_invoice of this Invoice.
        :rtype: datetime
        """
        return self._time_invoice

    @time_invoice.setter
    def time_invoice(self, time_invoice):
        """
        Sets the time_invoice of this Invoice.
        Date of invoice


        :param time_invoice: The time_invoice of this Invoice.
        :type: datetime
        """
        self._time_invoice = time_invoice

    @property
    def tax(self):
        """
        Gets the tax of this Invoice.
        Tax of invoice amount


        :return: The tax of this Invoice.
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this Invoice.
        Tax of invoice amount


        :param tax: The tax of this Invoice.
        :type: float
        """
        self._tax = tax

    @property
    def invoice_amount(self):
        """
        Gets the invoice_amount of this Invoice.
        Total amount of invoice


        :return: The invoice_amount of this Invoice.
        :rtype: float
        """
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, invoice_amount):
        """
        Sets the invoice_amount of this Invoice.
        Total amount of invoice


        :param invoice_amount: The invoice_amount of this Invoice.
        :type: float
        """
        self._invoice_amount = invoice_amount

    @property
    def invoice_amount_due(self):
        """
        Gets the invoice_amount_due of this Invoice.
        Balance of invoice


        :return: The invoice_amount_due of this Invoice.
        :rtype: float
        """
        return self._invoice_amount_due

    @invoice_amount_due.setter
    def invoice_amount_due(self, invoice_amount_due):
        """
        Sets the invoice_amount_due of this Invoice.
        Balance of invoice


        :param invoice_amount_due: The invoice_amount_due of this Invoice.
        :type: float
        """
        self._invoice_amount_due = invoice_amount_due

    @property
    def invoice_amount_credited(self):
        """
        Gets the invoice_amount_credited of this Invoice.
        Invoice amount credit


        :return: The invoice_amount_credited of this Invoice.
        :rtype: float
        """
        return self._invoice_amount_credited

    @invoice_amount_credited.setter
    def invoice_amount_credited(self, invoice_amount_credited):
        """
        Sets the invoice_amount_credited of this Invoice.
        Invoice amount credit


        :param invoice_amount_credited: The invoice_amount_credited of this Invoice.
        :type: float
        """
        self._invoice_amount_credited = invoice_amount_credited

    @property
    def invoice_amount_adjusted(self):
        """
        Gets the invoice_amount_adjusted of this Invoice.
        Invoice amount adjust


        :return: The invoice_amount_adjusted of this Invoice.
        :rtype: float
        """
        return self._invoice_amount_adjusted

    @invoice_amount_adjusted.setter
    def invoice_amount_adjusted(self, invoice_amount_adjusted):
        """
        Sets the invoice_amount_adjusted of this Invoice.
        Invoice amount adjust


        :param invoice_amount_adjusted: The invoice_amount_adjusted of this Invoice.
        :type: float
        """
        self._invoice_amount_adjusted = invoice_amount_adjusted

    @property
    def invoice_amount_applied(self):
        """
        Gets the invoice_amount_applied of this Invoice.
        Invoice amount applied


        :return: The invoice_amount_applied of this Invoice.
        :rtype: float
        """
        return self._invoice_amount_applied

    @invoice_amount_applied.setter
    def invoice_amount_applied(self, invoice_amount_applied):
        """
        Sets the invoice_amount_applied of this Invoice.
        Invoice amount applied


        :param invoice_amount_applied: The invoice_amount_applied of this Invoice.
        :type: float
        """
        self._invoice_amount_applied = invoice_amount_applied

    @property
    def currency(self):
        """
        Gets the currency of this Invoice.

        :return: The currency of this Invoice.
        :rtype: oci.osp_gateway.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Invoice.

        :param currency: The currency of this Invoice.
        :type: oci.osp_gateway.models.Currency
        """
        self._currency = currency

    @property
    def invoice_type(self):
        """
        Gets the invoice_type of this Invoice.
        Type of invoice

        Allowed values for this property are: "HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The invoice_type of this Invoice.
        :rtype: str
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """
        Sets the invoice_type of this Invoice.
        Type of invoice


        :param invoice_type: The invoice_type of this Invoice.
        :type: str
        """
        allowed_values = ["HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE"]
        if not value_allowed_none_or_none_sentinel(invoice_type, allowed_values):
            invoice_type = 'UNKNOWN_ENUM_VALUE'
        self._invoice_type = invoice_type

    @property
    def time_invoice_due(self):
        """
        Gets the time_invoice_due of this Invoice.
        Due date of invoice


        :return: The time_invoice_due of this Invoice.
        :rtype: datetime
        """
        return self._time_invoice_due

    @time_invoice_due.setter
    def time_invoice_due(self, time_invoice_due):
        """
        Sets the time_invoice_due of this Invoice.
        Due date of invoice


        :param time_invoice_due: The time_invoice_due of this Invoice.
        :type: datetime
        """
        self._time_invoice_due = time_invoice_due

    @property
    def invoice_ref_number(self):
        """
        Gets the invoice_ref_number of this Invoice.
        Invoice reference number


        :return: The invoice_ref_number of this Invoice.
        :rtype: str
        """
        return self._invoice_ref_number

    @invoice_ref_number.setter
    def invoice_ref_number(self, invoice_ref_number):
        """
        Sets the invoice_ref_number of this Invoice.
        Invoice reference number


        :param invoice_ref_number: The invoice_ref_number of this Invoice.
        :type: str
        """
        self._invoice_ref_number = invoice_ref_number

    @property
    def invoice_po_number(self):
        """
        Gets the invoice_po_number of this Invoice.
        Invoice PO number


        :return: The invoice_po_number of this Invoice.
        :rtype: str
        """
        return self._invoice_po_number

    @invoice_po_number.setter
    def invoice_po_number(self, invoice_po_number):
        """
        Sets the invoice_po_number of this Invoice.
        Invoice PO number


        :param invoice_po_number: The invoice_po_number of this Invoice.
        :type: str
        """
        self._invoice_po_number = invoice_po_number

    @property
    def invoice_status(self):
        """
        Gets the invoice_status of this Invoice.
        Invoice status

        Allowed values for this property are: "OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The invoice_status of this Invoice.
        :rtype: str
        """
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, invoice_status):
        """
        Sets the invoice_status of this Invoice.
        Invoice status


        :param invoice_status: The invoice_status of this Invoice.
        :type: str
        """
        allowed_values = ["OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(invoice_status, allowed_values):
            invoice_status = 'UNKNOWN_ENUM_VALUE'
        self._invoice_status = invoice_status

    @property
    def preferred_email(self):
        """
        Gets the preferred_email of this Invoice.
        Preferred Email on the invoice


        :return: The preferred_email of this Invoice.
        :rtype: str
        """
        return self._preferred_email

    @preferred_email.setter
    def preferred_email(self, preferred_email):
        """
        Sets the preferred_email of this Invoice.
        Preferred Email on the invoice


        :param preferred_email: The preferred_email of this Invoice.
        :type: str
        """
        self._preferred_email = preferred_email

    @property
    def is_pdf_email_available(self):
        """
        Gets the is_pdf_email_available of this Invoice.
        Is emailing pdf allowed


        :return: The is_pdf_email_available of this Invoice.
        :rtype: bool
        """
        return self._is_pdf_email_available

    @is_pdf_email_available.setter
    def is_pdf_email_available(self, is_pdf_email_available):
        """
        Sets the is_pdf_email_available of this Invoice.
        Is emailing pdf allowed


        :param is_pdf_email_available: The is_pdf_email_available of this Invoice.
        :type: bool
        """
        self._is_pdf_email_available = is_pdf_email_available

    @property
    def is_display_download_pdf(self):
        """
        Gets the is_display_download_pdf of this Invoice.
        Is pdf download access allowed


        :return: The is_display_download_pdf of this Invoice.
        :rtype: bool
        """
        return self._is_display_download_pdf

    @is_display_download_pdf.setter
    def is_display_download_pdf(self, is_display_download_pdf):
        """
        Sets the is_display_download_pdf of this Invoice.
        Is pdf download access allowed


        :param is_display_download_pdf: The is_display_download_pdf of this Invoice.
        :type: bool
        """
        self._is_display_download_pdf = is_display_download_pdf

    @property
    def is_payable(self):
        """
        Gets the is_payable of this Invoice.
        Whether invoice can be payed


        :return: The is_payable of this Invoice.
        :rtype: bool
        """
        return self._is_payable

    @is_payable.setter
    def is_payable(self, is_payable):
        """
        Sets the is_payable of this Invoice.
        Whether invoice can be payed


        :param is_payable: The is_payable of this Invoice.
        :type: bool
        """
        self._is_payable = is_payable

    @property
    def payment_terms(self):
        """
        Gets the payment_terms of this Invoice.
        Payment terms


        :return: The payment_terms of this Invoice.
        :rtype: str
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """
        Sets the payment_terms of this Invoice.
        Payment terms


        :param payment_terms: The payment_terms of this Invoice.
        :type: str
        """
        self._payment_terms = payment_terms

    @property
    def last_payment_detail(self):
        """
        Gets the last_payment_detail of this Invoice.

        :return: The last_payment_detail of this Invoice.
        :rtype: oci.osp_gateway.models.PaymentDetail
        """
        return self._last_payment_detail

    @last_payment_detail.setter
    def last_payment_detail(self, last_payment_detail):
        """
        Sets the last_payment_detail of this Invoice.

        :param last_payment_detail: The last_payment_detail of this Invoice.
        :type: oci.osp_gateway.models.PaymentDetail
        """
        self._last_payment_detail = last_payment_detail

    @property
    def bill_to_address(self):
        """
        Gets the bill_to_address of this Invoice.

        :return: The bill_to_address of this Invoice.
        :rtype: oci.osp_gateway.models.BillToAddress
        """
        return self._bill_to_address

    @bill_to_address.setter
    def bill_to_address(self, bill_to_address):
        """
        Sets the bill_to_address of this Invoice.

        :param bill_to_address: The bill_to_address of this Invoice.
        :type: oci.osp_gateway.models.BillToAddress
        """
        self._bill_to_address = bill_to_address

    @property
    def subscription_ids(self):
        """
        Gets the subscription_ids of this Invoice.
        List of subscription identifiers


        :return: The subscription_ids of this Invoice.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """
        Sets the subscription_ids of this Invoice.
        List of subscription identifiers


        :param subscription_ids: The subscription_ids of this Invoice.
        :type: list[str]
        """
        self._subscription_ids = subscription_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
