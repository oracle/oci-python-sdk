# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoiceSummary(object):
    """
    Invoice list elements
    """

    #: A constant which can be used with the invoice_status property of a InvoiceSummary.
    #: This constant has a value of "OPEN"
    INVOICE_STATUS_OPEN = "OPEN"

    #: A constant which can be used with the invoice_status property of a InvoiceSummary.
    #: This constant has a value of "PAST_DUE"
    INVOICE_STATUS_PAST_DUE = "PAST_DUE"

    #: A constant which can be used with the invoice_status property of a InvoiceSummary.
    #: This constant has a value of "PAYMENT_SUBMITTED"
    INVOICE_STATUS_PAYMENT_SUBMITTED = "PAYMENT_SUBMITTED"

    #: A constant which can be used with the invoice_status property of a InvoiceSummary.
    #: This constant has a value of "CLOSED"
    INVOICE_STATUS_CLOSED = "CLOSED"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "HARDWARE"
    INVOICE_TYPE_HARDWARE = "HARDWARE"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "SUBSCRIPTION"
    INVOICE_TYPE_SUBSCRIPTION = "SUBSCRIPTION"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "SUPPORT"
    INVOICE_TYPE_SUPPORT = "SUPPORT"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "LICENSE"
    INVOICE_TYPE_LICENSE = "LICENSE"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "EDUCATION"
    INVOICE_TYPE_EDUCATION = "EDUCATION"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "CONSULTING"
    INVOICE_TYPE_CONSULTING = "CONSULTING"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "SERVICE"
    INVOICE_TYPE_SERVICE = "SERVICE"

    #: A constant which can be used with the invoice_type property of a InvoiceSummary.
    #: This constant has a value of "USAGE"
    INVOICE_TYPE_USAGE = "USAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new InvoiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param invoice_id:
            The value to assign to the invoice_id property of this InvoiceSummary.
        :type invoice_id: str

        :param invoice_number:
            The value to assign to the invoice_number property of this InvoiceSummary.
        :type invoice_number: str

        :param internal_invoice_id:
            The value to assign to the internal_invoice_id property of this InvoiceSummary.
        :type internal_invoice_id: str

        :param is_credit_card_payable:
            The value to assign to the is_credit_card_payable property of this InvoiceSummary.
        :type is_credit_card_payable: bool

        :param invoice_status:
            The value to assign to the invoice_status property of this InvoiceSummary.
            Allowed values for this property are: "OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type invoice_status: str

        :param invoice_type:
            The value to assign to the invoice_type property of this InvoiceSummary.
            Allowed values for this property are: "HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type invoice_type: str

        :param is_paid:
            The value to assign to the is_paid property of this InvoiceSummary.
        :type is_paid: bool

        :param is_payable:
            The value to assign to the is_payable property of this InvoiceSummary.
        :type is_payable: bool

        :param invoice_amount:
            The value to assign to the invoice_amount property of this InvoiceSummary.
        :type invoice_amount: float

        :param invoice_amount_due:
            The value to assign to the invoice_amount_due property of this InvoiceSummary.
        :type invoice_amount_due: float

        :param invoice_amount_credited:
            The value to assign to the invoice_amount_credited property of this InvoiceSummary.
        :type invoice_amount_credited: float

        :param invoice_amount_adjusted:
            The value to assign to the invoice_amount_adjusted property of this InvoiceSummary.
        :type invoice_amount_adjusted: float

        :param invoice_amount_applied:
            The value to assign to the invoice_amount_applied property of this InvoiceSummary.
        :type invoice_amount_applied: float

        :param time_invoice_due:
            The value to assign to the time_invoice_due property of this InvoiceSummary.
        :type time_invoice_due: datetime

        :param is_payment_failed:
            The value to assign to the is_payment_failed property of this InvoiceSummary.
        :type is_payment_failed: bool

        :param invoice_amount_in_dispute:
            The value to assign to the invoice_amount_in_dispute property of this InvoiceSummary.
        :type invoice_amount_in_dispute: float

        :param invoice_ref_number:
            The value to assign to the invoice_ref_number property of this InvoiceSummary.
        :type invoice_ref_number: str

        :param invoice_po_number:
            The value to assign to the invoice_po_number property of this InvoiceSummary.
        :type invoice_po_number: str

        :param time_invoice:
            The value to assign to the time_invoice property of this InvoiceSummary.
        :type time_invoice: datetime

        :param currency:
            The value to assign to the currency property of this InvoiceSummary.
        :type currency: oci.osp_gateway.models.Currency

        :param is_pdf_email_available:
            The value to assign to the is_pdf_email_available property of this InvoiceSummary.
        :type is_pdf_email_available: bool

        :param is_display_view_pdf:
            The value to assign to the is_display_view_pdf property of this InvoiceSummary.
        :type is_display_view_pdf: bool

        :param is_display_download_pdf:
            The value to assign to the is_display_download_pdf property of this InvoiceSummary.
        :type is_display_download_pdf: bool

        :param last_payment_detail:
            The value to assign to the last_payment_detail property of this InvoiceSummary.
        :type last_payment_detail: oci.osp_gateway.models.PaymentDetail

        :param party_name:
            The value to assign to the party_name property of this InvoiceSummary.
        :type party_name: str

        :param subscription_ids:
            The value to assign to the subscription_ids property of this InvoiceSummary.
        :type subscription_ids: list[str]

        """
        self.swagger_types = {
            'invoice_id': 'str',
            'invoice_number': 'str',
            'internal_invoice_id': 'str',
            'is_credit_card_payable': 'bool',
            'invoice_status': 'str',
            'invoice_type': 'str',
            'is_paid': 'bool',
            'is_payable': 'bool',
            'invoice_amount': 'float',
            'invoice_amount_due': 'float',
            'invoice_amount_credited': 'float',
            'invoice_amount_adjusted': 'float',
            'invoice_amount_applied': 'float',
            'time_invoice_due': 'datetime',
            'is_payment_failed': 'bool',
            'invoice_amount_in_dispute': 'float',
            'invoice_ref_number': 'str',
            'invoice_po_number': 'str',
            'time_invoice': 'datetime',
            'currency': 'Currency',
            'is_pdf_email_available': 'bool',
            'is_display_view_pdf': 'bool',
            'is_display_download_pdf': 'bool',
            'last_payment_detail': 'PaymentDetail',
            'party_name': 'str',
            'subscription_ids': 'list[str]'
        }

        self.attribute_map = {
            'invoice_id': 'invoiceId',
            'invoice_number': 'invoiceNumber',
            'internal_invoice_id': 'internalInvoiceId',
            'is_credit_card_payable': 'isCreditCardPayable',
            'invoice_status': 'invoiceStatus',
            'invoice_type': 'invoiceType',
            'is_paid': 'isPaid',
            'is_payable': 'isPayable',
            'invoice_amount': 'invoiceAmount',
            'invoice_amount_due': 'invoiceAmountDue',
            'invoice_amount_credited': 'invoiceAmountCredited',
            'invoice_amount_adjusted': 'invoiceAmountAdjusted',
            'invoice_amount_applied': 'invoiceAmountApplied',
            'time_invoice_due': 'timeInvoiceDue',
            'is_payment_failed': 'isPaymentFailed',
            'invoice_amount_in_dispute': 'invoiceAmountInDispute',
            'invoice_ref_number': 'invoiceRefNumber',
            'invoice_po_number': 'invoicePoNumber',
            'time_invoice': 'timeInvoice',
            'currency': 'currency',
            'is_pdf_email_available': 'isPdfEmailAvailable',
            'is_display_view_pdf': 'isDisplayViewPdf',
            'is_display_download_pdf': 'isDisplayDownloadPdf',
            'last_payment_detail': 'lastPaymentDetail',
            'party_name': 'partyName',
            'subscription_ids': 'subscriptionIds'
        }

        self._invoice_id = None
        self._invoice_number = None
        self._internal_invoice_id = None
        self._is_credit_card_payable = None
        self._invoice_status = None
        self._invoice_type = None
        self._is_paid = None
        self._is_payable = None
        self._invoice_amount = None
        self._invoice_amount_due = None
        self._invoice_amount_credited = None
        self._invoice_amount_adjusted = None
        self._invoice_amount_applied = None
        self._time_invoice_due = None
        self._is_payment_failed = None
        self._invoice_amount_in_dispute = None
        self._invoice_ref_number = None
        self._invoice_po_number = None
        self._time_invoice = None
        self._currency = None
        self._is_pdf_email_available = None
        self._is_display_view_pdf = None
        self._is_display_download_pdf = None
        self._last_payment_detail = None
        self._party_name = None
        self._subscription_ids = None

    @property
    def invoice_id(self):
        """
        **[Required]** Gets the invoice_id of this InvoiceSummary.
        Invoice identifier


        :return: The invoice_id of this InvoiceSummary.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this InvoiceSummary.
        Invoice identifier


        :param invoice_id: The invoice_id of this InvoiceSummary.
        :type: str
        """
        self._invoice_id = invoice_id

    @property
    def invoice_number(self):
        """
        Gets the invoice_number of this InvoiceSummary.
        Invoice external reference


        :return: The invoice_number of this InvoiceSummary.
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """
        Sets the invoice_number of this InvoiceSummary.
        Invoice external reference


        :param invoice_number: The invoice_number of this InvoiceSummary.
        :type: str
        """
        self._invoice_number = invoice_number

    @property
    def internal_invoice_id(self):
        """
        Gets the internal_invoice_id of this InvoiceSummary.
        PC invoice identifier


        :return: The internal_invoice_id of this InvoiceSummary.
        :rtype: str
        """
        return self._internal_invoice_id

    @internal_invoice_id.setter
    def internal_invoice_id(self, internal_invoice_id):
        """
        Sets the internal_invoice_id of this InvoiceSummary.
        PC invoice identifier


        :param internal_invoice_id: The internal_invoice_id of this InvoiceSummary.
        :type: str
        """
        self._internal_invoice_id = internal_invoice_id

    @property
    def is_credit_card_payable(self):
        """
        Gets the is_credit_card_payable of this InvoiceSummary.
        Is credit card payment eligible


        :return: The is_credit_card_payable of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_credit_card_payable

    @is_credit_card_payable.setter
    def is_credit_card_payable(self, is_credit_card_payable):
        """
        Sets the is_credit_card_payable of this InvoiceSummary.
        Is credit card payment eligible


        :param is_credit_card_payable: The is_credit_card_payable of this InvoiceSummary.
        :type: bool
        """
        self._is_credit_card_payable = is_credit_card_payable

    @property
    def invoice_status(self):
        """
        Gets the invoice_status of this InvoiceSummary.
        Invoice status

        Allowed values for this property are: "OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The invoice_status of this InvoiceSummary.
        :rtype: str
        """
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, invoice_status):
        """
        Sets the invoice_status of this InvoiceSummary.
        Invoice status


        :param invoice_status: The invoice_status of this InvoiceSummary.
        :type: str
        """
        allowed_values = ["OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED"]
        if not value_allowed_none_or_none_sentinel(invoice_status, allowed_values):
            invoice_status = 'UNKNOWN_ENUM_VALUE'
        self._invoice_status = invoice_status

    @property
    def invoice_type(self):
        """
        Gets the invoice_type of this InvoiceSummary.
        Type of invoice

        Allowed values for this property are: "HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The invoice_type of this InvoiceSummary.
        :rtype: str
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """
        Sets the invoice_type of this InvoiceSummary.
        Type of invoice


        :param invoice_type: The invoice_type of this InvoiceSummary.
        :type: str
        """
        allowed_values = ["HARDWARE", "SUBSCRIPTION", "SUPPORT", "LICENSE", "EDUCATION", "CONSULTING", "SERVICE", "USAGE"]
        if not value_allowed_none_or_none_sentinel(invoice_type, allowed_values):
            invoice_type = 'UNKNOWN_ENUM_VALUE'
        self._invoice_type = invoice_type

    @property
    def is_paid(self):
        """
        Gets the is_paid of this InvoiceSummary.
        Is the invoice has been already payed


        :return: The is_paid of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_paid

    @is_paid.setter
    def is_paid(self, is_paid):
        """
        Sets the is_paid of this InvoiceSummary.
        Is the invoice has been already payed


        :param is_paid: The is_paid of this InvoiceSummary.
        :type: bool
        """
        self._is_paid = is_paid

    @property
    def is_payable(self):
        """
        Gets the is_payable of this InvoiceSummary.
        Whether invoice can be payed


        :return: The is_payable of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_payable

    @is_payable.setter
    def is_payable(self, is_payable):
        """
        Sets the is_payable of this InvoiceSummary.
        Whether invoice can be payed


        :param is_payable: The is_payable of this InvoiceSummary.
        :type: bool
        """
        self._is_payable = is_payable

    @property
    def invoice_amount(self):
        """
        Gets the invoice_amount of this InvoiceSummary.
        Invoice amount


        :return: The invoice_amount of this InvoiceSummary.
        :rtype: float
        """
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, invoice_amount):
        """
        Sets the invoice_amount of this InvoiceSummary.
        Invoice amount


        :param invoice_amount: The invoice_amount of this InvoiceSummary.
        :type: float
        """
        self._invoice_amount = invoice_amount

    @property
    def invoice_amount_due(self):
        """
        Gets the invoice_amount_due of this InvoiceSummary.
        Invoice amount due


        :return: The invoice_amount_due of this InvoiceSummary.
        :rtype: float
        """
        return self._invoice_amount_due

    @invoice_amount_due.setter
    def invoice_amount_due(self, invoice_amount_due):
        """
        Sets the invoice_amount_due of this InvoiceSummary.
        Invoice amount due


        :param invoice_amount_due: The invoice_amount_due of this InvoiceSummary.
        :type: float
        """
        self._invoice_amount_due = invoice_amount_due

    @property
    def invoice_amount_credited(self):
        """
        Gets the invoice_amount_credited of this InvoiceSummary.
        Invoice amount credit


        :return: The invoice_amount_credited of this InvoiceSummary.
        :rtype: float
        """
        return self._invoice_amount_credited

    @invoice_amount_credited.setter
    def invoice_amount_credited(self, invoice_amount_credited):
        """
        Sets the invoice_amount_credited of this InvoiceSummary.
        Invoice amount credit


        :param invoice_amount_credited: The invoice_amount_credited of this InvoiceSummary.
        :type: float
        """
        self._invoice_amount_credited = invoice_amount_credited

    @property
    def invoice_amount_adjusted(self):
        """
        Gets the invoice_amount_adjusted of this InvoiceSummary.
        Invoice amount adjust


        :return: The invoice_amount_adjusted of this InvoiceSummary.
        :rtype: float
        """
        return self._invoice_amount_adjusted

    @invoice_amount_adjusted.setter
    def invoice_amount_adjusted(self, invoice_amount_adjusted):
        """
        Sets the invoice_amount_adjusted of this InvoiceSummary.
        Invoice amount adjust


        :param invoice_amount_adjusted: The invoice_amount_adjusted of this InvoiceSummary.
        :type: float
        """
        self._invoice_amount_adjusted = invoice_amount_adjusted

    @property
    def invoice_amount_applied(self):
        """
        Gets the invoice_amount_applied of this InvoiceSummary.
        Invoice amount applied


        :return: The invoice_amount_applied of this InvoiceSummary.
        :rtype: float
        """
        return self._invoice_amount_applied

    @invoice_amount_applied.setter
    def invoice_amount_applied(self, invoice_amount_applied):
        """
        Sets the invoice_amount_applied of this InvoiceSummary.
        Invoice amount applied


        :param invoice_amount_applied: The invoice_amount_applied of this InvoiceSummary.
        :type: float
        """
        self._invoice_amount_applied = invoice_amount_applied

    @property
    def time_invoice_due(self):
        """
        Gets the time_invoice_due of this InvoiceSummary.
        Due date of invoice amount


        :return: The time_invoice_due of this InvoiceSummary.
        :rtype: datetime
        """
        return self._time_invoice_due

    @time_invoice_due.setter
    def time_invoice_due(self, time_invoice_due):
        """
        Sets the time_invoice_due of this InvoiceSummary.
        Due date of invoice amount


        :param time_invoice_due: The time_invoice_due of this InvoiceSummary.
        :type: datetime
        """
        self._time_invoice_due = time_invoice_due

    @property
    def is_payment_failed(self):
        """
        Gets the is_payment_failed of this InvoiceSummary.
        Is the last payment failed


        :return: The is_payment_failed of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_payment_failed

    @is_payment_failed.setter
    def is_payment_failed(self, is_payment_failed):
        """
        Sets the is_payment_failed of this InvoiceSummary.
        Is the last payment failed


        :param is_payment_failed: The is_payment_failed of this InvoiceSummary.
        :type: bool
        """
        self._is_payment_failed = is_payment_failed

    @property
    def invoice_amount_in_dispute(self):
        """
        Gets the invoice_amount_in_dispute of this InvoiceSummary.
        Invoice amount in dispute


        :return: The invoice_amount_in_dispute of this InvoiceSummary.
        :rtype: float
        """
        return self._invoice_amount_in_dispute

    @invoice_amount_in_dispute.setter
    def invoice_amount_in_dispute(self, invoice_amount_in_dispute):
        """
        Sets the invoice_amount_in_dispute of this InvoiceSummary.
        Invoice amount in dispute


        :param invoice_amount_in_dispute: The invoice_amount_in_dispute of this InvoiceSummary.
        :type: float
        """
        self._invoice_amount_in_dispute = invoice_amount_in_dispute

    @property
    def invoice_ref_number(self):
        """
        Gets the invoice_ref_number of this InvoiceSummary.
        Invoice reference number


        :return: The invoice_ref_number of this InvoiceSummary.
        :rtype: str
        """
        return self._invoice_ref_number

    @invoice_ref_number.setter
    def invoice_ref_number(self, invoice_ref_number):
        """
        Sets the invoice_ref_number of this InvoiceSummary.
        Invoice reference number


        :param invoice_ref_number: The invoice_ref_number of this InvoiceSummary.
        :type: str
        """
        self._invoice_ref_number = invoice_ref_number

    @property
    def invoice_po_number(self):
        """
        Gets the invoice_po_number of this InvoiceSummary.
        Invoice PO number


        :return: The invoice_po_number of this InvoiceSummary.
        :rtype: str
        """
        return self._invoice_po_number

    @invoice_po_number.setter
    def invoice_po_number(self, invoice_po_number):
        """
        Sets the invoice_po_number of this InvoiceSummary.
        Invoice PO number


        :param invoice_po_number: The invoice_po_number of this InvoiceSummary.
        :type: str
        """
        self._invoice_po_number = invoice_po_number

    @property
    def time_invoice(self):
        """
        Gets the time_invoice of this InvoiceSummary.
        Date of invoice


        :return: The time_invoice of this InvoiceSummary.
        :rtype: datetime
        """
        return self._time_invoice

    @time_invoice.setter
    def time_invoice(self, time_invoice):
        """
        Sets the time_invoice of this InvoiceSummary.
        Date of invoice


        :param time_invoice: The time_invoice of this InvoiceSummary.
        :type: datetime
        """
        self._time_invoice = time_invoice

    @property
    def currency(self):
        """
        Gets the currency of this InvoiceSummary.

        :return: The currency of this InvoiceSummary.
        :rtype: oci.osp_gateway.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this InvoiceSummary.

        :param currency: The currency of this InvoiceSummary.
        :type: oci.osp_gateway.models.Currency
        """
        self._currency = currency

    @property
    def is_pdf_email_available(self):
        """
        Gets the is_pdf_email_available of this InvoiceSummary.
        Is emailing pdf allowed


        :return: The is_pdf_email_available of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_pdf_email_available

    @is_pdf_email_available.setter
    def is_pdf_email_available(self, is_pdf_email_available):
        """
        Sets the is_pdf_email_available of this InvoiceSummary.
        Is emailing pdf allowed


        :param is_pdf_email_available: The is_pdf_email_available of this InvoiceSummary.
        :type: bool
        """
        self._is_pdf_email_available = is_pdf_email_available

    @property
    def is_display_view_pdf(self):
        """
        Gets the is_display_view_pdf of this InvoiceSummary.
        Is view access allowed


        :return: The is_display_view_pdf of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_display_view_pdf

    @is_display_view_pdf.setter
    def is_display_view_pdf(self, is_display_view_pdf):
        """
        Sets the is_display_view_pdf of this InvoiceSummary.
        Is view access allowed


        :param is_display_view_pdf: The is_display_view_pdf of this InvoiceSummary.
        :type: bool
        """
        self._is_display_view_pdf = is_display_view_pdf

    @property
    def is_display_download_pdf(self):
        """
        Gets the is_display_download_pdf of this InvoiceSummary.
        Is pdf download access allowed


        :return: The is_display_download_pdf of this InvoiceSummary.
        :rtype: bool
        """
        return self._is_display_download_pdf

    @is_display_download_pdf.setter
    def is_display_download_pdf(self, is_display_download_pdf):
        """
        Sets the is_display_download_pdf of this InvoiceSummary.
        Is pdf download access allowed


        :param is_display_download_pdf: The is_display_download_pdf of this InvoiceSummary.
        :type: bool
        """
        self._is_display_download_pdf = is_display_download_pdf

    @property
    def last_payment_detail(self):
        """
        Gets the last_payment_detail of this InvoiceSummary.

        :return: The last_payment_detail of this InvoiceSummary.
        :rtype: oci.osp_gateway.models.PaymentDetail
        """
        return self._last_payment_detail

    @last_payment_detail.setter
    def last_payment_detail(self, last_payment_detail):
        """
        Sets the last_payment_detail of this InvoiceSummary.

        :param last_payment_detail: The last_payment_detail of this InvoiceSummary.
        :type: oci.osp_gateway.models.PaymentDetail
        """
        self._last_payment_detail = last_payment_detail

    @property
    def party_name(self):
        """
        Gets the party_name of this InvoiceSummary.
        Name of the bill to customer


        :return: The party_name of this InvoiceSummary.
        :rtype: str
        """
        return self._party_name

    @party_name.setter
    def party_name(self, party_name):
        """
        Sets the party_name of this InvoiceSummary.
        Name of the bill to customer


        :param party_name: The party_name of this InvoiceSummary.
        :type: str
        """
        self._party_name = party_name

    @property
    def subscription_ids(self):
        """
        Gets the subscription_ids of this InvoiceSummary.
        List of subscription identifiers


        :return: The subscription_ids of this InvoiceSummary.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """
        Sets the subscription_ids of this InvoiceSummary.
        List of subscription identifiers


        :param subscription_ids: The subscription_ids of this InvoiceSummary.
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
