# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscribedService(object):
    """
    Subscribed service contract details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscribedService object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SubscribedService.
        :type id: str

        :param type:
            The value to assign to the type property of this SubscribedService.
        :type type: str

        :param serial_number:
            The value to assign to the serial_number property of this SubscribedService.
        :type serial_number: str

        :param subscription_id:
            The value to assign to the subscription_id property of this SubscribedService.
        :type subscription_id: str

        :param product:
            The value to assign to the product property of this SubscribedService.
        :type product: oci.onesubscription.models.RateCardProduct

        :param time_start:
            The value to assign to the time_start property of this SubscribedService.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this SubscribedService.
        :type time_end: datetime

        :param quantity:
            The value to assign to the quantity property of this SubscribedService.
        :type quantity: str

        :param status:
            The value to assign to the status property of this SubscribedService.
        :type status: str

        :param operation_type:
            The value to assign to the operation_type property of this SubscribedService.
        :type operation_type: str

        :param net_unit_price:
            The value to assign to the net_unit_price property of this SubscribedService.
        :type net_unit_price: str

        :param price_period:
            The value to assign to the price_period property of this SubscribedService.
        :type price_period: str

        :param line_net_amount:
            The value to assign to the line_net_amount property of this SubscribedService.
        :type line_net_amount: str

        :param is_variable_commitment:
            The value to assign to the is_variable_commitment property of this SubscribedService.
        :type is_variable_commitment: bool

        :param is_allowance:
            The value to assign to the is_allowance property of this SubscribedService.
        :type is_allowance: bool

        :param used_amount:
            The value to assign to the used_amount property of this SubscribedService.
        :type used_amount: str

        :param available_amount:
            The value to assign to the available_amount property of this SubscribedService.
        :type available_amount: str

        :param funded_allocation_value:
            The value to assign to the funded_allocation_value property of this SubscribedService.
        :type funded_allocation_value: str

        :param is_having_usage:
            The value to assign to the is_having_usage property of this SubscribedService.
        :type is_having_usage: bool

        :param is_cap_to_price_list:
            The value to assign to the is_cap_to_price_list property of this SubscribedService.
        :type is_cap_to_price_list: bool

        :param credit_percentage:
            The value to assign to the credit_percentage property of this SubscribedService.
        :type credit_percentage: str

        :param partner_transaction_type:
            The value to assign to the partner_transaction_type property of this SubscribedService.
        :type partner_transaction_type: str

        :param is_credit_enabled:
            The value to assign to the is_credit_enabled property of this SubscribedService.
        :type is_credit_enabled: bool

        :param overage_policy:
            The value to assign to the overage_policy property of this SubscribedService.
        :type overage_policy: str

        :param overage_bill_to:
            The value to assign to the overage_bill_to property of this SubscribedService.
        :type overage_bill_to: str

        :param payg_policy:
            The value to assign to the payg_policy property of this SubscribedService.
        :type payg_policy: str

        :param promo_order_line_id:
            The value to assign to the promo_order_line_id property of this SubscribedService.
        :type promo_order_line_id: int

        :param promotion_pricing_type:
            The value to assign to the promotion_pricing_type property of this SubscribedService.
        :type promotion_pricing_type: str

        :param rate_card_discount_percentage:
            The value to assign to the rate_card_discount_percentage property of this SubscribedService.
        :type rate_card_discount_percentage: str

        :param overage_discount_percentage:
            The value to assign to the overage_discount_percentage property of this SubscribedService.
        :type overage_discount_percentage: str

        :param bill_to_customer:
            The value to assign to the bill_to_customer property of this SubscribedService.
        :type bill_to_customer: oci.onesubscription.models.SubscribedServiceBusinessPartner

        :param bill_to_contact:
            The value to assign to the bill_to_contact property of this SubscribedService.
        :type bill_to_contact: oci.onesubscription.models.SubscribedServiceUser

        :param bill_to_address:
            The value to assign to the bill_to_address property of this SubscribedService.
        :type bill_to_address: oci.onesubscription.models.SubscribedServiceAddress

        :param payment_number:
            The value to assign to the payment_number property of this SubscribedService.
        :type payment_number: str

        :param time_payment_expiry:
            The value to assign to the time_payment_expiry property of this SubscribedService.
        :type time_payment_expiry: datetime

        :param payment_term:
            The value to assign to the payment_term property of this SubscribedService.
        :type payment_term: oci.onesubscription.models.SubscribedServicePaymentTerm

        :param payment_method:
            The value to assign to the payment_method property of this SubscribedService.
        :type payment_method: str

        :param transaction_extension_id:
            The value to assign to the transaction_extension_id property of this SubscribedService.
        :type transaction_extension_id: int

        :param sales_channel:
            The value to assign to the sales_channel property of this SubscribedService.
        :type sales_channel: str

        :param eligible_to_renew:
            The value to assign to the eligible_to_renew property of this SubscribedService.
        :type eligible_to_renew: str

        :param renewed_subscribed_service_id:
            The value to assign to the renewed_subscribed_service_id property of this SubscribedService.
        :type renewed_subscribed_service_id: str

        :param term_value:
            The value to assign to the term_value property of this SubscribedService.
        :type term_value: int

        :param term_value_uom:
            The value to assign to the term_value_uom property of this SubscribedService.
        :type term_value_uom: str

        :param renewal_opty_id:
            The value to assign to the renewal_opty_id property of this SubscribedService.
        :type renewal_opty_id: int

        :param renewal_opty_number:
            The value to assign to the renewal_opty_number property of this SubscribedService.
        :type renewal_opty_number: str

        :param renewal_opty_type:
            The value to assign to the renewal_opty_type property of this SubscribedService.
        :type renewal_opty_type: str

        :param booking_opty_number:
            The value to assign to the booking_opty_number property of this SubscribedService.
        :type booking_opty_number: str

        :param revenue_line_id:
            The value to assign to the revenue_line_id property of this SubscribedService.
        :type revenue_line_id: int

        :param revenue_line_number:
            The value to assign to the revenue_line_number property of this SubscribedService.
        :type revenue_line_number: str

        :param major_set:
            The value to assign to the major_set property of this SubscribedService.
        :type major_set: int

        :param time_majorset_start:
            The value to assign to the time_majorset_start property of this SubscribedService.
        :type time_majorset_start: datetime

        :param time_majorset_end:
            The value to assign to the time_majorset_end property of this SubscribedService.
        :type time_majorset_end: datetime

        :param system_arr_in_lc:
            The value to assign to the system_arr_in_lc property of this SubscribedService.
        :type system_arr_in_lc: str

        :param system_arr_in_sc:
            The value to assign to the system_arr_in_sc property of this SubscribedService.
        :type system_arr_in_sc: str

        :param system_atr_arr_in_lc:
            The value to assign to the system_atr_arr_in_lc property of this SubscribedService.
        :type system_atr_arr_in_lc: str

        :param system_atr_arr_in_sc:
            The value to assign to the system_atr_arr_in_sc property of this SubscribedService.
        :type system_atr_arr_in_sc: str

        :param revised_arr_in_lc:
            The value to assign to the revised_arr_in_lc property of this SubscribedService.
        :type revised_arr_in_lc: str

        :param revised_arr_in_sc:
            The value to assign to the revised_arr_in_sc property of this SubscribedService.
        :type revised_arr_in_sc: str

        :param total_value:
            The value to assign to the total_value property of this SubscribedService.
        :type total_value: str

        :param original_promo_amount:
            The value to assign to the original_promo_amount property of this SubscribedService.
        :type original_promo_amount: str

        :param order_header_id:
            The value to assign to the order_header_id property of this SubscribedService.
        :type order_header_id: int

        :param order_number:
            The value to assign to the order_number property of this SubscribedService.
        :type order_number: int

        :param order_type:
            The value to assign to the order_type property of this SubscribedService.
        :type order_type: str

        :param order_line_id:
            The value to assign to the order_line_id property of this SubscribedService.
        :type order_line_id: int

        :param order_line_number:
            The value to assign to the order_line_number property of this SubscribedService.
        :type order_line_number: int

        :param commitment_schedule_id:
            The value to assign to the commitment_schedule_id property of this SubscribedService.
        :type commitment_schedule_id: str

        :param sales_account_party_id:
            The value to assign to the sales_account_party_id property of this SubscribedService.
        :type sales_account_party_id: int

        :param data_center:
            The value to assign to the data_center property of this SubscribedService.
        :type data_center: str

        :param data_center_region:
            The value to assign to the data_center_region property of this SubscribedService.
        :type data_center_region: str

        :param admin_email:
            The value to assign to the admin_email property of this SubscribedService.
        :type admin_email: str

        :param buyer_email:
            The value to assign to the buyer_email property of this SubscribedService.
        :type buyer_email: str

        :param subscription_source:
            The value to assign to the subscription_source property of this SubscribedService.
        :type subscription_source: str

        :param provisioning_source:
            The value to assign to the provisioning_source property of this SubscribedService.
        :type provisioning_source: str

        :param fulfillment_set:
            The value to assign to the fulfillment_set property of this SubscribedService.
        :type fulfillment_set: str

        :param is_intent_to_pay:
            The value to assign to the is_intent_to_pay property of this SubscribedService.
        :type is_intent_to_pay: bool

        :param is_payg:
            The value to assign to the is_payg property of this SubscribedService.
        :type is_payg: bool

        :param pricing_model:
            The value to assign to the pricing_model property of this SubscribedService.
        :type pricing_model: str

        :param program_type:
            The value to assign to the program_type property of this SubscribedService.
        :type program_type: str

        :param start_date_type:
            The value to assign to the start_date_type property of this SubscribedService.
        :type start_date_type: str

        :param time_provisioned:
            The value to assign to the time_provisioned property of this SubscribedService.
        :type time_provisioned: datetime

        :param promo_type:
            The value to assign to the promo_type property of this SubscribedService.
        :type promo_type: str

        :param service_to_customer:
            The value to assign to the service_to_customer property of this SubscribedService.
        :type service_to_customer: oci.onesubscription.models.SubscribedServiceBusinessPartner

        :param service_to_contact:
            The value to assign to the service_to_contact property of this SubscribedService.
        :type service_to_contact: oci.onesubscription.models.SubscribedServiceUser

        :param service_to_address:
            The value to assign to the service_to_address property of this SubscribedService.
        :type service_to_address: oci.onesubscription.models.SubscribedServiceAddress

        :param sold_to_customer:
            The value to assign to the sold_to_customer property of this SubscribedService.
        :type sold_to_customer: oci.onesubscription.models.SubscribedServiceBusinessPartner

        :param sold_to_contact:
            The value to assign to the sold_to_contact property of this SubscribedService.
        :type sold_to_contact: oci.onesubscription.models.SubscribedServiceUser

        :param end_user_customer:
            The value to assign to the end_user_customer property of this SubscribedService.
        :type end_user_customer: oci.onesubscription.models.SubscribedServiceBusinessPartner

        :param end_user_contact:
            The value to assign to the end_user_contact property of this SubscribedService.
        :type end_user_contact: oci.onesubscription.models.SubscribedServiceUser

        :param end_user_address:
            The value to assign to the end_user_address property of this SubscribedService.
        :type end_user_address: oci.onesubscription.models.SubscribedServiceAddress

        :param reseller_customer:
            The value to assign to the reseller_customer property of this SubscribedService.
        :type reseller_customer: oci.onesubscription.models.SubscribedServiceBusinessPartner

        :param reseller_contact:
            The value to assign to the reseller_contact property of this SubscribedService.
        :type reseller_contact: oci.onesubscription.models.SubscribedServiceUser

        :param reseller_address:
            The value to assign to the reseller_address property of this SubscribedService.
        :type reseller_address: oci.onesubscription.models.SubscribedServiceAddress

        :param csi:
            The value to assign to the csi property of this SubscribedService.
        :type csi: int

        :param customer_transaction_reference:
            The value to assign to the customer_transaction_reference property of this SubscribedService.
        :type customer_transaction_reference: str

        :param partner_credit_amount:
            The value to assign to the partner_credit_amount property of this SubscribedService.
        :type partner_credit_amount: str

        :param is_single_rate_card:
            The value to assign to the is_single_rate_card property of this SubscribedService.
        :type is_single_rate_card: bool

        :param agreement_id:
            The value to assign to the agreement_id property of this SubscribedService.
        :type agreement_id: int

        :param agreement_name:
            The value to assign to the agreement_name property of this SubscribedService.
        :type agreement_name: str

        :param agreement_type:
            The value to assign to the agreement_type property of this SubscribedService.
        :type agreement_type: str

        :param billing_frequency:
            The value to assign to the billing_frequency property of this SubscribedService.
        :type billing_frequency: str

        :param time_welcome_email_sent:
            The value to assign to the time_welcome_email_sent property of this SubscribedService.
        :type time_welcome_email_sent: datetime

        :param time_service_configuration_email_sent:
            The value to assign to the time_service_configuration_email_sent property of this SubscribedService.
        :type time_service_configuration_email_sent: datetime

        :param time_customer_config:
            The value to assign to the time_customer_config property of this SubscribedService.
        :type time_customer_config: datetime

        :param time_agreement_end:
            The value to assign to the time_agreement_end property of this SubscribedService.
        :type time_agreement_end: datetime

        :param commitment_services:
            The value to assign to the commitment_services property of this SubscribedService.
        :type commitment_services: list[oci.onesubscription.models.CommitmentService]

        :param rate_cards:
            The value to assign to the rate_cards property of this SubscribedService.
        :type rate_cards: list[oci.onesubscription.models.RateCardSummary]

        :param time_created:
            The value to assign to the time_created property of this SubscribedService.
        :type time_created: datetime

        :param created_by:
            The value to assign to the created_by property of this SubscribedService.
        :type created_by: str

        :param time_updated:
            The value to assign to the time_updated property of this SubscribedService.
        :type time_updated: datetime

        :param updated_by:
            The value to assign to the updated_by property of this SubscribedService.
        :type updated_by: str

        :param ratecard_type:
            The value to assign to the ratecard_type property of this SubscribedService.
        :type ratecard_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'serial_number': 'str',
            'subscription_id': 'str',
            'product': 'RateCardProduct',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'quantity': 'str',
            'status': 'str',
            'operation_type': 'str',
            'net_unit_price': 'str',
            'price_period': 'str',
            'line_net_amount': 'str',
            'is_variable_commitment': 'bool',
            'is_allowance': 'bool',
            'used_amount': 'str',
            'available_amount': 'str',
            'funded_allocation_value': 'str',
            'is_having_usage': 'bool',
            'is_cap_to_price_list': 'bool',
            'credit_percentage': 'str',
            'partner_transaction_type': 'str',
            'is_credit_enabled': 'bool',
            'overage_policy': 'str',
            'overage_bill_to': 'str',
            'payg_policy': 'str',
            'promo_order_line_id': 'int',
            'promotion_pricing_type': 'str',
            'rate_card_discount_percentage': 'str',
            'overage_discount_percentage': 'str',
            'bill_to_customer': 'SubscribedServiceBusinessPartner',
            'bill_to_contact': 'SubscribedServiceUser',
            'bill_to_address': 'SubscribedServiceAddress',
            'payment_number': 'str',
            'time_payment_expiry': 'datetime',
            'payment_term': 'SubscribedServicePaymentTerm',
            'payment_method': 'str',
            'transaction_extension_id': 'int',
            'sales_channel': 'str',
            'eligible_to_renew': 'str',
            'renewed_subscribed_service_id': 'str',
            'term_value': 'int',
            'term_value_uom': 'str',
            'renewal_opty_id': 'int',
            'renewal_opty_number': 'str',
            'renewal_opty_type': 'str',
            'booking_opty_number': 'str',
            'revenue_line_id': 'int',
            'revenue_line_number': 'str',
            'major_set': 'int',
            'time_majorset_start': 'datetime',
            'time_majorset_end': 'datetime',
            'system_arr_in_lc': 'str',
            'system_arr_in_sc': 'str',
            'system_atr_arr_in_lc': 'str',
            'system_atr_arr_in_sc': 'str',
            'revised_arr_in_lc': 'str',
            'revised_arr_in_sc': 'str',
            'total_value': 'str',
            'original_promo_amount': 'str',
            'order_header_id': 'int',
            'order_number': 'int',
            'order_type': 'str',
            'order_line_id': 'int',
            'order_line_number': 'int',
            'commitment_schedule_id': 'str',
            'sales_account_party_id': 'int',
            'data_center': 'str',
            'data_center_region': 'str',
            'admin_email': 'str',
            'buyer_email': 'str',
            'subscription_source': 'str',
            'provisioning_source': 'str',
            'fulfillment_set': 'str',
            'is_intent_to_pay': 'bool',
            'is_payg': 'bool',
            'pricing_model': 'str',
            'program_type': 'str',
            'start_date_type': 'str',
            'time_provisioned': 'datetime',
            'promo_type': 'str',
            'service_to_customer': 'SubscribedServiceBusinessPartner',
            'service_to_contact': 'SubscribedServiceUser',
            'service_to_address': 'SubscribedServiceAddress',
            'sold_to_customer': 'SubscribedServiceBusinessPartner',
            'sold_to_contact': 'SubscribedServiceUser',
            'end_user_customer': 'SubscribedServiceBusinessPartner',
            'end_user_contact': 'SubscribedServiceUser',
            'end_user_address': 'SubscribedServiceAddress',
            'reseller_customer': 'SubscribedServiceBusinessPartner',
            'reseller_contact': 'SubscribedServiceUser',
            'reseller_address': 'SubscribedServiceAddress',
            'csi': 'int',
            'customer_transaction_reference': 'str',
            'partner_credit_amount': 'str',
            'is_single_rate_card': 'bool',
            'agreement_id': 'int',
            'agreement_name': 'str',
            'agreement_type': 'str',
            'billing_frequency': 'str',
            'time_welcome_email_sent': 'datetime',
            'time_service_configuration_email_sent': 'datetime',
            'time_customer_config': 'datetime',
            'time_agreement_end': 'datetime',
            'commitment_services': 'list[CommitmentService]',
            'rate_cards': 'list[RateCardSummary]',
            'time_created': 'datetime',
            'created_by': 'str',
            'time_updated': 'datetime',
            'updated_by': 'str',
            'ratecard_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'serial_number': 'serialNumber',
            'subscription_id': 'subscriptionId',
            'product': 'product',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'quantity': 'quantity',
            'status': 'status',
            'operation_type': 'operationType',
            'net_unit_price': 'netUnitPrice',
            'price_period': 'pricePeriod',
            'line_net_amount': 'lineNetAmount',
            'is_variable_commitment': 'isVariableCommitment',
            'is_allowance': 'isAllowance',
            'used_amount': 'usedAmount',
            'available_amount': 'availableAmount',
            'funded_allocation_value': 'fundedAllocationValue',
            'is_having_usage': 'isHavingUsage',
            'is_cap_to_price_list': 'isCapToPriceList',
            'credit_percentage': 'creditPercentage',
            'partner_transaction_type': 'partnerTransactionType',
            'is_credit_enabled': 'isCreditEnabled',
            'overage_policy': 'overagePolicy',
            'overage_bill_to': 'overageBillTo',
            'payg_policy': 'paygPolicy',
            'promo_order_line_id': 'promoOrderLineId',
            'promotion_pricing_type': 'promotionPricingType',
            'rate_card_discount_percentage': 'rateCardDiscountPercentage',
            'overage_discount_percentage': 'overageDiscountPercentage',
            'bill_to_customer': 'billToCustomer',
            'bill_to_contact': 'billToContact',
            'bill_to_address': 'billToAddress',
            'payment_number': 'paymentNumber',
            'time_payment_expiry': 'timePaymentExpiry',
            'payment_term': 'paymentTerm',
            'payment_method': 'paymentMethod',
            'transaction_extension_id': 'transactionExtensionId',
            'sales_channel': 'salesChannel',
            'eligible_to_renew': 'eligibleToRenew',
            'renewed_subscribed_service_id': 'renewedSubscribedServiceId',
            'term_value': 'termValue',
            'term_value_uom': 'termValueUom',
            'renewal_opty_id': 'renewalOptyId',
            'renewal_opty_number': 'renewalOptyNumber',
            'renewal_opty_type': 'renewalOptyType',
            'booking_opty_number': 'bookingOptyNumber',
            'revenue_line_id': 'revenueLineId',
            'revenue_line_number': 'revenueLineNumber',
            'major_set': 'majorSet',
            'time_majorset_start': 'timeMajorsetStart',
            'time_majorset_end': 'timeMajorsetEnd',
            'system_arr_in_lc': 'systemArrInLc',
            'system_arr_in_sc': 'systemArrInSc',
            'system_atr_arr_in_lc': 'systemAtrArrInLc',
            'system_atr_arr_in_sc': 'systemAtrArrInSc',
            'revised_arr_in_lc': 'revisedArrInLc',
            'revised_arr_in_sc': 'revisedArrInSc',
            'total_value': 'totalValue',
            'original_promo_amount': 'originalPromoAmount',
            'order_header_id': 'orderHeaderId',
            'order_number': 'orderNumber',
            'order_type': 'orderType',
            'order_line_id': 'orderLineId',
            'order_line_number': 'orderLineNumber',
            'commitment_schedule_id': 'commitmentScheduleId',
            'sales_account_party_id': 'salesAccountPartyId',
            'data_center': 'dataCenter',
            'data_center_region': 'dataCenterRegion',
            'admin_email': 'adminEmail',
            'buyer_email': 'buyerEmail',
            'subscription_source': 'subscriptionSource',
            'provisioning_source': 'provisioningSource',
            'fulfillment_set': 'fulfillmentSet',
            'is_intent_to_pay': 'isIntentToPay',
            'is_payg': 'isPayg',
            'pricing_model': 'pricingModel',
            'program_type': 'programType',
            'start_date_type': 'startDateType',
            'time_provisioned': 'timeProvisioned',
            'promo_type': 'promoType',
            'service_to_customer': 'serviceToCustomer',
            'service_to_contact': 'serviceToContact',
            'service_to_address': 'serviceToAddress',
            'sold_to_customer': 'soldToCustomer',
            'sold_to_contact': 'soldToContact',
            'end_user_customer': 'endUserCustomer',
            'end_user_contact': 'endUserContact',
            'end_user_address': 'endUserAddress',
            'reseller_customer': 'resellerCustomer',
            'reseller_contact': 'resellerContact',
            'reseller_address': 'resellerAddress',
            'csi': 'csi',
            'customer_transaction_reference': 'customerTransactionReference',
            'partner_credit_amount': 'partnerCreditAmount',
            'is_single_rate_card': 'isSingleRateCard',
            'agreement_id': 'agreementId',
            'agreement_name': 'agreementName',
            'agreement_type': 'agreementType',
            'billing_frequency': 'billingFrequency',
            'time_welcome_email_sent': 'timeWelcomeEmailSent',
            'time_service_configuration_email_sent': 'timeServiceConfigurationEmailSent',
            'time_customer_config': 'timeCustomerConfig',
            'time_agreement_end': 'timeAgreementEnd',
            'commitment_services': 'commitmentServices',
            'rate_cards': 'rateCards',
            'time_created': 'timeCreated',
            'created_by': 'createdBy',
            'time_updated': 'timeUpdated',
            'updated_by': 'updatedBy',
            'ratecard_type': 'ratecardType'
        }

        self._id = None
        self._type = None
        self._serial_number = None
        self._subscription_id = None
        self._product = None
        self._time_start = None
        self._time_end = None
        self._quantity = None
        self._status = None
        self._operation_type = None
        self._net_unit_price = None
        self._price_period = None
        self._line_net_amount = None
        self._is_variable_commitment = None
        self._is_allowance = None
        self._used_amount = None
        self._available_amount = None
        self._funded_allocation_value = None
        self._is_having_usage = None
        self._is_cap_to_price_list = None
        self._credit_percentage = None
        self._partner_transaction_type = None
        self._is_credit_enabled = None
        self._overage_policy = None
        self._overage_bill_to = None
        self._payg_policy = None
        self._promo_order_line_id = None
        self._promotion_pricing_type = None
        self._rate_card_discount_percentage = None
        self._overage_discount_percentage = None
        self._bill_to_customer = None
        self._bill_to_contact = None
        self._bill_to_address = None
        self._payment_number = None
        self._time_payment_expiry = None
        self._payment_term = None
        self._payment_method = None
        self._transaction_extension_id = None
        self._sales_channel = None
        self._eligible_to_renew = None
        self._renewed_subscribed_service_id = None
        self._term_value = None
        self._term_value_uom = None
        self._renewal_opty_id = None
        self._renewal_opty_number = None
        self._renewal_opty_type = None
        self._booking_opty_number = None
        self._revenue_line_id = None
        self._revenue_line_number = None
        self._major_set = None
        self._time_majorset_start = None
        self._time_majorset_end = None
        self._system_arr_in_lc = None
        self._system_arr_in_sc = None
        self._system_atr_arr_in_lc = None
        self._system_atr_arr_in_sc = None
        self._revised_arr_in_lc = None
        self._revised_arr_in_sc = None
        self._total_value = None
        self._original_promo_amount = None
        self._order_header_id = None
        self._order_number = None
        self._order_type = None
        self._order_line_id = None
        self._order_line_number = None
        self._commitment_schedule_id = None
        self._sales_account_party_id = None
        self._data_center = None
        self._data_center_region = None
        self._admin_email = None
        self._buyer_email = None
        self._subscription_source = None
        self._provisioning_source = None
        self._fulfillment_set = None
        self._is_intent_to_pay = None
        self._is_payg = None
        self._pricing_model = None
        self._program_type = None
        self._start_date_type = None
        self._time_provisioned = None
        self._promo_type = None
        self._service_to_customer = None
        self._service_to_contact = None
        self._service_to_address = None
        self._sold_to_customer = None
        self._sold_to_contact = None
        self._end_user_customer = None
        self._end_user_contact = None
        self._end_user_address = None
        self._reseller_customer = None
        self._reseller_contact = None
        self._reseller_address = None
        self._csi = None
        self._customer_transaction_reference = None
        self._partner_credit_amount = None
        self._is_single_rate_card = None
        self._agreement_id = None
        self._agreement_name = None
        self._agreement_type = None
        self._billing_frequency = None
        self._time_welcome_email_sent = None
        self._time_service_configuration_email_sent = None
        self._time_customer_config = None
        self._time_agreement_end = None
        self._commitment_services = None
        self._rate_cards = None
        self._time_created = None
        self._created_by = None
        self._time_updated = None
        self._updated_by = None
        self._ratecard_type = None

    @property
    def id(self):
        """
        Gets the id of this SubscribedService.
        SPM internal Subscribed Service ID


        :return: The id of this SubscribedService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscribedService.
        SPM internal Subscribed Service ID


        :param id: The id of this SubscribedService.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this SubscribedService.
        Subscribed Service line type


        :return: The type of this SubscribedService.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SubscribedService.
        Subscribed Service line type


        :param type: The type of this SubscribedService.
        :type: str
        """
        self._type = type

    @property
    def serial_number(self):
        """
        Gets the serial_number of this SubscribedService.
        Subscribed service line number


        :return: The serial_number of this SubscribedService.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this SubscribedService.
        Subscribed service line number


        :param serial_number: The serial_number of this SubscribedService.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this SubscribedService.
        Subscription ID associated to the subscribed service


        :return: The subscription_id of this SubscribedService.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this SubscribedService.
        Subscription ID associated to the subscribed service


        :param subscription_id: The subscription_id of this SubscribedService.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def product(self):
        """
        Gets the product of this SubscribedService.

        :return: The product of this SubscribedService.
        :rtype: oci.onesubscription.models.RateCardProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this SubscribedService.

        :param product: The product of this SubscribedService.
        :type: oci.onesubscription.models.RateCardProduct
        """
        self._product = product

    @property
    def time_start(self):
        """
        Gets the time_start of this SubscribedService.
        Subscribed service start date


        :return: The time_start of this SubscribedService.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this SubscribedService.
        Subscribed service start date


        :param time_start: The time_start of this SubscribedService.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this SubscribedService.
        Subscribed service end date


        :return: The time_end of this SubscribedService.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this SubscribedService.
        Subscribed service end date


        :param time_end: The time_end of this SubscribedService.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def quantity(self):
        """
        Gets the quantity of this SubscribedService.
        Subscribed service quantity


        :return: The quantity of this SubscribedService.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this SubscribedService.
        Subscribed service quantity


        :param quantity: The quantity of this SubscribedService.
        :type: str
        """
        self._quantity = quantity

    @property
    def status(self):
        """
        Gets the status of this SubscribedService.
        Subscribed service status


        :return: The status of this SubscribedService.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SubscribedService.
        Subscribed service status


        :param status: The status of this SubscribedService.
        :type: str
        """
        self._status = status

    @property
    def operation_type(self):
        """
        Gets the operation_type of this SubscribedService.
        Subscribed service operation type


        :return: The operation_type of this SubscribedService.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this SubscribedService.
        Subscribed service operation type


        :param operation_type: The operation_type of this SubscribedService.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def net_unit_price(self):
        """
        Gets the net_unit_price of this SubscribedService.
        Subscribed service net unit price


        :return: The net_unit_price of this SubscribedService.
        :rtype: str
        """
        return self._net_unit_price

    @net_unit_price.setter
    def net_unit_price(self, net_unit_price):
        """
        Sets the net_unit_price of this SubscribedService.
        Subscribed service net unit price


        :param net_unit_price: The net_unit_price of this SubscribedService.
        :type: str
        """
        self._net_unit_price = net_unit_price

    @property
    def price_period(self):
        """
        Gets the price_period of this SubscribedService.
        Indicates the period for which the commitment amount can be utilised exceeding which the amount lapses. Also used in calculation of total contract line value


        :return: The price_period of this SubscribedService.
        :rtype: str
        """
        return self._price_period

    @price_period.setter
    def price_period(self, price_period):
        """
        Sets the price_period of this SubscribedService.
        Indicates the period for which the commitment amount can be utilised exceeding which the amount lapses. Also used in calculation of total contract line value


        :param price_period: The price_period of this SubscribedService.
        :type: str
        """
        self._price_period = price_period

    @property
    def line_net_amount(self):
        """
        Gets the line_net_amount of this SubscribedService.
        Subscribed service line net amount


        :return: The line_net_amount of this SubscribedService.
        :rtype: str
        """
        return self._line_net_amount

    @line_net_amount.setter
    def line_net_amount(self, line_net_amount):
        """
        Sets the line_net_amount of this SubscribedService.
        Subscribed service line net amount


        :param line_net_amount: The line_net_amount of this SubscribedService.
        :type: str
        """
        self._line_net_amount = line_net_amount

    @property
    def is_variable_commitment(self):
        """
        Gets the is_variable_commitment of this SubscribedService.
        Indicates if the commitment lines can have different quantities


        :return: The is_variable_commitment of this SubscribedService.
        :rtype: bool
        """
        return self._is_variable_commitment

    @is_variable_commitment.setter
    def is_variable_commitment(self, is_variable_commitment):
        """
        Sets the is_variable_commitment of this SubscribedService.
        Indicates if the commitment lines can have different quantities


        :param is_variable_commitment: The is_variable_commitment of this SubscribedService.
        :type: bool
        """
        self._is_variable_commitment = is_variable_commitment

    @property
    def is_allowance(self):
        """
        Gets the is_allowance of this SubscribedService.
        Indicates if a service can recieve usages and consequently have available amounts computed


        :return: The is_allowance of this SubscribedService.
        :rtype: bool
        """
        return self._is_allowance

    @is_allowance.setter
    def is_allowance(self, is_allowance):
        """
        Sets the is_allowance of this SubscribedService.
        Indicates if a service can recieve usages and consequently have available amounts computed


        :param is_allowance: The is_allowance of this SubscribedService.
        :type: bool
        """
        self._is_allowance = is_allowance

    @property
    def used_amount(self):
        """
        Gets the used_amount of this SubscribedService.
        Subscribed service used amount


        :return: The used_amount of this SubscribedService.
        :rtype: str
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """
        Sets the used_amount of this SubscribedService.
        Subscribed service used amount


        :param used_amount: The used_amount of this SubscribedService.
        :type: str
        """
        self._used_amount = used_amount

    @property
    def available_amount(self):
        """
        Gets the available_amount of this SubscribedService.
        Subscribed sercice available or remaining amount


        :return: The available_amount of this SubscribedService.
        :rtype: str
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """
        Sets the available_amount of this SubscribedService.
        Subscribed sercice available or remaining amount


        :param available_amount: The available_amount of this SubscribedService.
        :type: str
        """
        self._available_amount = available_amount

    @property
    def funded_allocation_value(self):
        """
        Gets the funded_allocation_value of this SubscribedService.
        Funded Allocation line value
        example: 12000.00


        :return: The funded_allocation_value of this SubscribedService.
        :rtype: str
        """
        return self._funded_allocation_value

    @funded_allocation_value.setter
    def funded_allocation_value(self, funded_allocation_value):
        """
        Sets the funded_allocation_value of this SubscribedService.
        Funded Allocation line value
        example: 12000.00


        :param funded_allocation_value: The funded_allocation_value of this SubscribedService.
        :type: str
        """
        self._funded_allocation_value = funded_allocation_value

    @property
    def is_having_usage(self):
        """
        Gets the is_having_usage of this SubscribedService.
        Indicator on whether or not there has been usage for the subscribed service


        :return: The is_having_usage of this SubscribedService.
        :rtype: bool
        """
        return self._is_having_usage

    @is_having_usage.setter
    def is_having_usage(self, is_having_usage):
        """
        Sets the is_having_usage of this SubscribedService.
        Indicator on whether or not there has been usage for the subscribed service


        :param is_having_usage: The is_having_usage of this SubscribedService.
        :type: bool
        """
        self._is_having_usage = is_having_usage

    @property
    def is_cap_to_price_list(self):
        """
        Gets the is_cap_to_price_list of this SubscribedService.
        If true compares rate between ratecard and the active pricelist and minimum rate would be fetched


        :return: The is_cap_to_price_list of this SubscribedService.
        :rtype: bool
        """
        return self._is_cap_to_price_list

    @is_cap_to_price_list.setter
    def is_cap_to_price_list(self, is_cap_to_price_list):
        """
        Sets the is_cap_to_price_list of this SubscribedService.
        If true compares rate between ratecard and the active pricelist and minimum rate would be fetched


        :param is_cap_to_price_list: The is_cap_to_price_list of this SubscribedService.
        :type: bool
        """
        self._is_cap_to_price_list = is_cap_to_price_list

    @property
    def credit_percentage(self):
        """
        Gets the credit_percentage of this SubscribedService.
        Subscribed service credit percentage


        :return: The credit_percentage of this SubscribedService.
        :rtype: str
        """
        return self._credit_percentage

    @credit_percentage.setter
    def credit_percentage(self, credit_percentage):
        """
        Sets the credit_percentage of this SubscribedService.
        Subscribed service credit percentage


        :param credit_percentage: The credit_percentage of this SubscribedService.
        :type: str
        """
        self._credit_percentage = credit_percentage

    @property
    def partner_transaction_type(self):
        """
        Gets the partner_transaction_type of this SubscribedService.
        This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ


        :return: The partner_transaction_type of this SubscribedService.
        :rtype: str
        """
        return self._partner_transaction_type

    @partner_transaction_type.setter
    def partner_transaction_type(self, partner_transaction_type):
        """
        Sets the partner_transaction_type of this SubscribedService.
        This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ


        :param partner_transaction_type: The partner_transaction_type of this SubscribedService.
        :type: str
        """
        self._partner_transaction_type = partner_transaction_type

    @property
    def is_credit_enabled(self):
        """
        Gets the is_credit_enabled of this SubscribedService.
        Used in context of service credit lines


        :return: The is_credit_enabled of this SubscribedService.
        :rtype: bool
        """
        return self._is_credit_enabled

    @is_credit_enabled.setter
    def is_credit_enabled(self, is_credit_enabled):
        """
        Sets the is_credit_enabled of this SubscribedService.
        Used in context of service credit lines


        :param is_credit_enabled: The is_credit_enabled of this SubscribedService.
        :type: bool
        """
        self._is_credit_enabled = is_credit_enabled

    @property
    def overage_policy(self):
        """
        Gets the overage_policy of this SubscribedService.
        Overage Policy of Subscribed Service


        :return: The overage_policy of this SubscribedService.
        :rtype: str
        """
        return self._overage_policy

    @overage_policy.setter
    def overage_policy(self, overage_policy):
        """
        Sets the overage_policy of this SubscribedService.
        Overage Policy of Subscribed Service


        :param overage_policy: The overage_policy of this SubscribedService.
        :type: str
        """
        self._overage_policy = overage_policy

    @property
    def overage_bill_to(self):
        """
        Gets the overage_bill_to of this SubscribedService.
        Overage Bill To of Subscribed Service


        :return: The overage_bill_to of this SubscribedService.
        :rtype: str
        """
        return self._overage_bill_to

    @overage_bill_to.setter
    def overage_bill_to(self, overage_bill_to):
        """
        Sets the overage_bill_to of this SubscribedService.
        Overage Bill To of Subscribed Service


        :param overage_bill_to: The overage_bill_to of this SubscribedService.
        :type: str
        """
        self._overage_bill_to = overage_bill_to

    @property
    def payg_policy(self):
        """
        Gets the payg_policy of this SubscribedService.
        Pay As You Go policy of Subscribed Service (Can be null - indicating no payg policy)


        :return: The payg_policy of this SubscribedService.
        :rtype: str
        """
        return self._payg_policy

    @payg_policy.setter
    def payg_policy(self, payg_policy):
        """
        Sets the payg_policy of this SubscribedService.
        Pay As You Go policy of Subscribed Service (Can be null - indicating no payg policy)


        :param payg_policy: The payg_policy of this SubscribedService.
        :type: str
        """
        self._payg_policy = payg_policy

    @property
    def promo_order_line_id(self):
        """
        Gets the promo_order_line_id of this SubscribedService.
        Not null if this service has an associated promotion line in SPM. Contains the line identifier from Order Management of
        the associated promo line.


        :return: The promo_order_line_id of this SubscribedService.
        :rtype: int
        """
        return self._promo_order_line_id

    @promo_order_line_id.setter
    def promo_order_line_id(self, promo_order_line_id):
        """
        Sets the promo_order_line_id of this SubscribedService.
        Not null if this service has an associated promotion line in SPM. Contains the line identifier from Order Management of
        the associated promo line.


        :param promo_order_line_id: The promo_order_line_id of this SubscribedService.
        :type: int
        """
        self._promo_order_line_id = promo_order_line_id

    @property
    def promotion_pricing_type(self):
        """
        Gets the promotion_pricing_type of this SubscribedService.
        Promotion Pricing Type of Subscribed Service (Can be null - indicating no promotion pricing)


        :return: The promotion_pricing_type of this SubscribedService.
        :rtype: str
        """
        return self._promotion_pricing_type

    @promotion_pricing_type.setter
    def promotion_pricing_type(self, promotion_pricing_type):
        """
        Sets the promotion_pricing_type of this SubscribedService.
        Promotion Pricing Type of Subscribed Service (Can be null - indicating no promotion pricing)


        :param promotion_pricing_type: The promotion_pricing_type of this SubscribedService.
        :type: str
        """
        self._promotion_pricing_type = promotion_pricing_type

    @property
    def rate_card_discount_percentage(self):
        """
        Gets the rate_card_discount_percentage of this SubscribedService.
        Subscribed service Rate Card Discount Percentage


        :return: The rate_card_discount_percentage of this SubscribedService.
        :rtype: str
        """
        return self._rate_card_discount_percentage

    @rate_card_discount_percentage.setter
    def rate_card_discount_percentage(self, rate_card_discount_percentage):
        """
        Sets the rate_card_discount_percentage of this SubscribedService.
        Subscribed service Rate Card Discount Percentage


        :param rate_card_discount_percentage: The rate_card_discount_percentage of this SubscribedService.
        :type: str
        """
        self._rate_card_discount_percentage = rate_card_discount_percentage

    @property
    def overage_discount_percentage(self):
        """
        Gets the overage_discount_percentage of this SubscribedService.
        Subscribed service Overage Discount Percentage


        :return: The overage_discount_percentage of this SubscribedService.
        :rtype: str
        """
        return self._overage_discount_percentage

    @overage_discount_percentage.setter
    def overage_discount_percentage(self, overage_discount_percentage):
        """
        Sets the overage_discount_percentage of this SubscribedService.
        Subscribed service Overage Discount Percentage


        :param overage_discount_percentage: The overage_discount_percentage of this SubscribedService.
        :type: str
        """
        self._overage_discount_percentage = overage_discount_percentage

    @property
    def bill_to_customer(self):
        """
        Gets the bill_to_customer of this SubscribedService.

        :return: The bill_to_customer of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        return self._bill_to_customer

    @bill_to_customer.setter
    def bill_to_customer(self, bill_to_customer):
        """
        Sets the bill_to_customer of this SubscribedService.

        :param bill_to_customer: The bill_to_customer of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        self._bill_to_customer = bill_to_customer

    @property
    def bill_to_contact(self):
        """
        Gets the bill_to_contact of this SubscribedService.

        :return: The bill_to_contact of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceUser
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """
        Sets the bill_to_contact of this SubscribedService.

        :param bill_to_contact: The bill_to_contact of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceUser
        """
        self._bill_to_contact = bill_to_contact

    @property
    def bill_to_address(self):
        """
        Gets the bill_to_address of this SubscribedService.

        :return: The bill_to_address of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceAddress
        """
        return self._bill_to_address

    @bill_to_address.setter
    def bill_to_address(self, bill_to_address):
        """
        Sets the bill_to_address of this SubscribedService.

        :param bill_to_address: The bill_to_address of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceAddress
        """
        self._bill_to_address = bill_to_address

    @property
    def payment_number(self):
        """
        Gets the payment_number of this SubscribedService.
        Payment Number of Subscribed Service


        :return: The payment_number of this SubscribedService.
        :rtype: str
        """
        return self._payment_number

    @payment_number.setter
    def payment_number(self, payment_number):
        """
        Sets the payment_number of this SubscribedService.
        Payment Number of Subscribed Service


        :param payment_number: The payment_number of this SubscribedService.
        :type: str
        """
        self._payment_number = payment_number

    @property
    def time_payment_expiry(self):
        """
        Gets the time_payment_expiry of this SubscribedService.
        Subscribed service payment expiry date


        :return: The time_payment_expiry of this SubscribedService.
        :rtype: datetime
        """
        return self._time_payment_expiry

    @time_payment_expiry.setter
    def time_payment_expiry(self, time_payment_expiry):
        """
        Sets the time_payment_expiry of this SubscribedService.
        Subscribed service payment expiry date


        :param time_payment_expiry: The time_payment_expiry of this SubscribedService.
        :type: datetime
        """
        self._time_payment_expiry = time_payment_expiry

    @property
    def payment_term(self):
        """
        Gets the payment_term of this SubscribedService.

        :return: The payment_term of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServicePaymentTerm
        """
        return self._payment_term

    @payment_term.setter
    def payment_term(self, payment_term):
        """
        Sets the payment_term of this SubscribedService.

        :param payment_term: The payment_term of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServicePaymentTerm
        """
        self._payment_term = payment_term

    @property
    def payment_method(self):
        """
        Gets the payment_method of this SubscribedService.
        Payment Method of Subscribed Service


        :return: The payment_method of this SubscribedService.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this SubscribedService.
        Payment Method of Subscribed Service


        :param payment_method: The payment_method of this SubscribedService.
        :type: str
        """
        self._payment_method = payment_method

    @property
    def transaction_extension_id(self):
        """
        Gets the transaction_extension_id of this SubscribedService.
        Subscribed service Transaction Extension Id


        :return: The transaction_extension_id of this SubscribedService.
        :rtype: int
        """
        return self._transaction_extension_id

    @transaction_extension_id.setter
    def transaction_extension_id(self, transaction_extension_id):
        """
        Sets the transaction_extension_id of this SubscribedService.
        Subscribed service Transaction Extension Id


        :param transaction_extension_id: The transaction_extension_id of this SubscribedService.
        :type: int
        """
        self._transaction_extension_id = transaction_extension_id

    @property
    def sales_channel(self):
        """
        Gets the sales_channel of this SubscribedService.
        Sales Channel of Subscribed Service


        :return: The sales_channel of this SubscribedService.
        :rtype: str
        """
        return self._sales_channel

    @sales_channel.setter
    def sales_channel(self, sales_channel):
        """
        Sets the sales_channel of this SubscribedService.
        Sales Channel of Subscribed Service


        :param sales_channel: The sales_channel of this SubscribedService.
        :type: str
        """
        self._sales_channel = sales_channel

    @property
    def eligible_to_renew(self):
        """
        Gets the eligible_to_renew of this SubscribedService.
        Subscribed service eligible to renew field


        :return: The eligible_to_renew of this SubscribedService.
        :rtype: str
        """
        return self._eligible_to_renew

    @eligible_to_renew.setter
    def eligible_to_renew(self, eligible_to_renew):
        """
        Sets the eligible_to_renew of this SubscribedService.
        Subscribed service eligible to renew field


        :param eligible_to_renew: The eligible_to_renew of this SubscribedService.
        :type: str
        """
        self._eligible_to_renew = eligible_to_renew

    @property
    def renewed_subscribed_service_id(self):
        """
        Gets the renewed_subscribed_service_id of this SubscribedService.
        SPM renewed Subscription ID


        :return: The renewed_subscribed_service_id of this SubscribedService.
        :rtype: str
        """
        return self._renewed_subscribed_service_id

    @renewed_subscribed_service_id.setter
    def renewed_subscribed_service_id(self, renewed_subscribed_service_id):
        """
        Sets the renewed_subscribed_service_id of this SubscribedService.
        SPM renewed Subscription ID


        :param renewed_subscribed_service_id: The renewed_subscribed_service_id of this SubscribedService.
        :type: str
        """
        self._renewed_subscribed_service_id = renewed_subscribed_service_id

    @property
    def term_value(self):
        """
        Gets the term_value of this SubscribedService.
        Term value in Months


        :return: The term_value of this SubscribedService.
        :rtype: int
        """
        return self._term_value

    @term_value.setter
    def term_value(self, term_value):
        """
        Sets the term_value of this SubscribedService.
        Term value in Months


        :param term_value: The term_value of this SubscribedService.
        :type: int
        """
        self._term_value = term_value

    @property
    def term_value_uom(self):
        """
        Gets the term_value_uom of this SubscribedService.
        Term value UOM


        :return: The term_value_uom of this SubscribedService.
        :rtype: str
        """
        return self._term_value_uom

    @term_value_uom.setter
    def term_value_uom(self, term_value_uom):
        """
        Sets the term_value_uom of this SubscribedService.
        Term value UOM


        :param term_value_uom: The term_value_uom of this SubscribedService.
        :type: str
        """
        self._term_value_uom = term_value_uom

    @property
    def renewal_opty_id(self):
        """
        Gets the renewal_opty_id of this SubscribedService.
        Subscribed service Opportunity Id


        :return: The renewal_opty_id of this SubscribedService.
        :rtype: int
        """
        return self._renewal_opty_id

    @renewal_opty_id.setter
    def renewal_opty_id(self, renewal_opty_id):
        """
        Sets the renewal_opty_id of this SubscribedService.
        Subscribed service Opportunity Id


        :param renewal_opty_id: The renewal_opty_id of this SubscribedService.
        :type: int
        """
        self._renewal_opty_id = renewal_opty_id

    @property
    def renewal_opty_number(self):
        """
        Gets the renewal_opty_number of this SubscribedService.
        Renewal Opportunity Number of Subscribed Service


        :return: The renewal_opty_number of this SubscribedService.
        :rtype: str
        """
        return self._renewal_opty_number

    @renewal_opty_number.setter
    def renewal_opty_number(self, renewal_opty_number):
        """
        Sets the renewal_opty_number of this SubscribedService.
        Renewal Opportunity Number of Subscribed Service


        :param renewal_opty_number: The renewal_opty_number of this SubscribedService.
        :type: str
        """
        self._renewal_opty_number = renewal_opty_number

    @property
    def renewal_opty_type(self):
        """
        Gets the renewal_opty_type of this SubscribedService.
        Renewal Opportunity Type of Subscribed Service


        :return: The renewal_opty_type of this SubscribedService.
        :rtype: str
        """
        return self._renewal_opty_type

    @renewal_opty_type.setter
    def renewal_opty_type(self, renewal_opty_type):
        """
        Sets the renewal_opty_type of this SubscribedService.
        Renewal Opportunity Type of Subscribed Service


        :param renewal_opty_type: The renewal_opty_type of this SubscribedService.
        :type: str
        """
        self._renewal_opty_type = renewal_opty_type

    @property
    def booking_opty_number(self):
        """
        Gets the booking_opty_number of this SubscribedService.
        Booking Opportunity Number of Subscribed Service


        :return: The booking_opty_number of this SubscribedService.
        :rtype: str
        """
        return self._booking_opty_number

    @booking_opty_number.setter
    def booking_opty_number(self, booking_opty_number):
        """
        Sets the booking_opty_number of this SubscribedService.
        Booking Opportunity Number of Subscribed Service


        :param booking_opty_number: The booking_opty_number of this SubscribedService.
        :type: str
        """
        self._booking_opty_number = booking_opty_number

    @property
    def revenue_line_id(self):
        """
        Gets the revenue_line_id of this SubscribedService.
        Subscribed service Revenue Line Id


        :return: The revenue_line_id of this SubscribedService.
        :rtype: int
        """
        return self._revenue_line_id

    @revenue_line_id.setter
    def revenue_line_id(self, revenue_line_id):
        """
        Sets the revenue_line_id of this SubscribedService.
        Subscribed service Revenue Line Id


        :param revenue_line_id: The revenue_line_id of this SubscribedService.
        :type: int
        """
        self._revenue_line_id = revenue_line_id

    @property
    def revenue_line_number(self):
        """
        Gets the revenue_line_number of this SubscribedService.
        Revenue Line NUmber of Subscribed Service


        :return: The revenue_line_number of this SubscribedService.
        :rtype: str
        """
        return self._revenue_line_number

    @revenue_line_number.setter
    def revenue_line_number(self, revenue_line_number):
        """
        Sets the revenue_line_number of this SubscribedService.
        Revenue Line NUmber of Subscribed Service


        :param revenue_line_number: The revenue_line_number of this SubscribedService.
        :type: str
        """
        self._revenue_line_number = revenue_line_number

    @property
    def major_set(self):
        """
        Gets the major_set of this SubscribedService.
        Subscribed service Major Set


        :return: The major_set of this SubscribedService.
        :rtype: int
        """
        return self._major_set

    @major_set.setter
    def major_set(self, major_set):
        """
        Sets the major_set of this SubscribedService.
        Subscribed service Major Set


        :param major_set: The major_set of this SubscribedService.
        :type: int
        """
        self._major_set = major_set

    @property
    def time_majorset_start(self):
        """
        Gets the time_majorset_start of this SubscribedService.
        Subscribed service Major Set Start date


        :return: The time_majorset_start of this SubscribedService.
        :rtype: datetime
        """
        return self._time_majorset_start

    @time_majorset_start.setter
    def time_majorset_start(self, time_majorset_start):
        """
        Sets the time_majorset_start of this SubscribedService.
        Subscribed service Major Set Start date


        :param time_majorset_start: The time_majorset_start of this SubscribedService.
        :type: datetime
        """
        self._time_majorset_start = time_majorset_start

    @property
    def time_majorset_end(self):
        """
        Gets the time_majorset_end of this SubscribedService.
        Subscribed service Major Set End date


        :return: The time_majorset_end of this SubscribedService.
        :rtype: datetime
        """
        return self._time_majorset_end

    @time_majorset_end.setter
    def time_majorset_end(self, time_majorset_end):
        """
        Sets the time_majorset_end of this SubscribedService.
        Subscribed service Major Set End date


        :param time_majorset_end: The time_majorset_end of this SubscribedService.
        :type: datetime
        """
        self._time_majorset_end = time_majorset_end

    @property
    def system_arr_in_lc(self):
        """
        Gets the system_arr_in_lc of this SubscribedService.
        Subscribed service System ARR


        :return: The system_arr_in_lc of this SubscribedService.
        :rtype: str
        """
        return self._system_arr_in_lc

    @system_arr_in_lc.setter
    def system_arr_in_lc(self, system_arr_in_lc):
        """
        Sets the system_arr_in_lc of this SubscribedService.
        Subscribed service System ARR


        :param system_arr_in_lc: The system_arr_in_lc of this SubscribedService.
        :type: str
        """
        self._system_arr_in_lc = system_arr_in_lc

    @property
    def system_arr_in_sc(self):
        """
        Gets the system_arr_in_sc of this SubscribedService.
        Subscribed service System ARR in Standard Currency


        :return: The system_arr_in_sc of this SubscribedService.
        :rtype: str
        """
        return self._system_arr_in_sc

    @system_arr_in_sc.setter
    def system_arr_in_sc(self, system_arr_in_sc):
        """
        Sets the system_arr_in_sc of this SubscribedService.
        Subscribed service System ARR in Standard Currency


        :param system_arr_in_sc: The system_arr_in_sc of this SubscribedService.
        :type: str
        """
        self._system_arr_in_sc = system_arr_in_sc

    @property
    def system_atr_arr_in_lc(self):
        """
        Gets the system_atr_arr_in_lc of this SubscribedService.
        Subscribed service System ATR-ARR


        :return: The system_atr_arr_in_lc of this SubscribedService.
        :rtype: str
        """
        return self._system_atr_arr_in_lc

    @system_atr_arr_in_lc.setter
    def system_atr_arr_in_lc(self, system_atr_arr_in_lc):
        """
        Sets the system_atr_arr_in_lc of this SubscribedService.
        Subscribed service System ATR-ARR


        :param system_atr_arr_in_lc: The system_atr_arr_in_lc of this SubscribedService.
        :type: str
        """
        self._system_atr_arr_in_lc = system_atr_arr_in_lc

    @property
    def system_atr_arr_in_sc(self):
        """
        Gets the system_atr_arr_in_sc of this SubscribedService.
        Subscribed service System ATR-ARR in Standard Currency


        :return: The system_atr_arr_in_sc of this SubscribedService.
        :rtype: str
        """
        return self._system_atr_arr_in_sc

    @system_atr_arr_in_sc.setter
    def system_atr_arr_in_sc(self, system_atr_arr_in_sc):
        """
        Sets the system_atr_arr_in_sc of this SubscribedService.
        Subscribed service System ATR-ARR in Standard Currency


        :param system_atr_arr_in_sc: The system_atr_arr_in_sc of this SubscribedService.
        :type: str
        """
        self._system_atr_arr_in_sc = system_atr_arr_in_sc

    @property
    def revised_arr_in_lc(self):
        """
        Gets the revised_arr_in_lc of this SubscribedService.
        Subscribed service Revised ARR


        :return: The revised_arr_in_lc of this SubscribedService.
        :rtype: str
        """
        return self._revised_arr_in_lc

    @revised_arr_in_lc.setter
    def revised_arr_in_lc(self, revised_arr_in_lc):
        """
        Sets the revised_arr_in_lc of this SubscribedService.
        Subscribed service Revised ARR


        :param revised_arr_in_lc: The revised_arr_in_lc of this SubscribedService.
        :type: str
        """
        self._revised_arr_in_lc = revised_arr_in_lc

    @property
    def revised_arr_in_sc(self):
        """
        Gets the revised_arr_in_sc of this SubscribedService.
        Subscribed service Revised ARR in Standard Currency


        :return: The revised_arr_in_sc of this SubscribedService.
        :rtype: str
        """
        return self._revised_arr_in_sc

    @revised_arr_in_sc.setter
    def revised_arr_in_sc(self, revised_arr_in_sc):
        """
        Sets the revised_arr_in_sc of this SubscribedService.
        Subscribed service Revised ARR in Standard Currency


        :param revised_arr_in_sc: The revised_arr_in_sc of this SubscribedService.
        :type: str
        """
        self._revised_arr_in_sc = revised_arr_in_sc

    @property
    def total_value(self):
        """
        Gets the total_value of this SubscribedService.
        Subscribed service total value


        :return: The total_value of this SubscribedService.
        :rtype: str
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        """
        Sets the total_value of this SubscribedService.
        Subscribed service total value


        :param total_value: The total_value of this SubscribedService.
        :type: str
        """
        self._total_value = total_value

    @property
    def original_promo_amount(self):
        """
        Gets the original_promo_amount of this SubscribedService.
        Subscribed service Promotion Amount


        :return: The original_promo_amount of this SubscribedService.
        :rtype: str
        """
        return self._original_promo_amount

    @original_promo_amount.setter
    def original_promo_amount(self, original_promo_amount):
        """
        Sets the original_promo_amount of this SubscribedService.
        Subscribed service Promotion Amount


        :param original_promo_amount: The original_promo_amount of this SubscribedService.
        :type: str
        """
        self._original_promo_amount = original_promo_amount

    @property
    def order_header_id(self):
        """
        Gets the order_header_id of this SubscribedService.
        Sales Order Header associated to the subscribed service


        :return: The order_header_id of this SubscribedService.
        :rtype: int
        """
        return self._order_header_id

    @order_header_id.setter
    def order_header_id(self, order_header_id):
        """
        Sets the order_header_id of this SubscribedService.
        Sales Order Header associated to the subscribed service


        :param order_header_id: The order_header_id of this SubscribedService.
        :type: int
        """
        self._order_header_id = order_header_id

    @property
    def order_number(self):
        """
        Gets the order_number of this SubscribedService.
        Sales Order Number associated to the subscribed service


        :return: The order_number of this SubscribedService.
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """
        Sets the order_number of this SubscribedService.
        Sales Order Number associated to the subscribed service


        :param order_number: The order_number of this SubscribedService.
        :type: int
        """
        self._order_number = order_number

    @property
    def order_type(self):
        """
        Gets the order_type of this SubscribedService.
        Order Type of Subscribed Service


        :return: The order_type of this SubscribedService.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """
        Sets the order_type of this SubscribedService.
        Order Type of Subscribed Service


        :param order_type: The order_type of this SubscribedService.
        :type: str
        """
        self._order_type = order_type

    @property
    def order_line_id(self):
        """
        Gets the order_line_id of this SubscribedService.
        Sales Order Line Id associated to the subscribed service


        :return: The order_line_id of this SubscribedService.
        :rtype: int
        """
        return self._order_line_id

    @order_line_id.setter
    def order_line_id(self, order_line_id):
        """
        Sets the order_line_id of this SubscribedService.
        Sales Order Line Id associated to the subscribed service


        :param order_line_id: The order_line_id of this SubscribedService.
        :type: int
        """
        self._order_line_id = order_line_id

    @property
    def order_line_number(self):
        """
        Gets the order_line_number of this SubscribedService.
        Sales Order Line Number associated to the subscribed service


        :return: The order_line_number of this SubscribedService.
        :rtype: int
        """
        return self._order_line_number

    @order_line_number.setter
    def order_line_number(self, order_line_number):
        """
        Sets the order_line_number of this SubscribedService.
        Sales Order Line Number associated to the subscribed service


        :param order_line_number: The order_line_number of this SubscribedService.
        :type: int
        """
        self._order_line_number = order_line_number

    @property
    def commitment_schedule_id(self):
        """
        Gets the commitment_schedule_id of this SubscribedService.
        Subscribed service commitment schedule Id


        :return: The commitment_schedule_id of this SubscribedService.
        :rtype: str
        """
        return self._commitment_schedule_id

    @commitment_schedule_id.setter
    def commitment_schedule_id(self, commitment_schedule_id):
        """
        Sets the commitment_schedule_id of this SubscribedService.
        Subscribed service commitment schedule Id


        :param commitment_schedule_id: The commitment_schedule_id of this SubscribedService.
        :type: str
        """
        self._commitment_schedule_id = commitment_schedule_id

    @property
    def sales_account_party_id(self):
        """
        Gets the sales_account_party_id of this SubscribedService.
        Subscribed service sales account party id


        :return: The sales_account_party_id of this SubscribedService.
        :rtype: int
        """
        return self._sales_account_party_id

    @sales_account_party_id.setter
    def sales_account_party_id(self, sales_account_party_id):
        """
        Sets the sales_account_party_id of this SubscribedService.
        Subscribed service sales account party id


        :param sales_account_party_id: The sales_account_party_id of this SubscribedService.
        :type: int
        """
        self._sales_account_party_id = sales_account_party_id

    @property
    def data_center(self):
        """
        Gets the data_center of this SubscribedService.
        Subscribed service data center


        :return: The data_center of this SubscribedService.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """
        Sets the data_center of this SubscribedService.
        Subscribed service data center


        :param data_center: The data_center of this SubscribedService.
        :type: str
        """
        self._data_center = data_center

    @property
    def data_center_region(self):
        """
        Gets the data_center_region of this SubscribedService.
        Subscribed service data center region


        :return: The data_center_region of this SubscribedService.
        :rtype: str
        """
        return self._data_center_region

    @data_center_region.setter
    def data_center_region(self, data_center_region):
        """
        Sets the data_center_region of this SubscribedService.
        Subscribed service data center region


        :param data_center_region: The data_center_region of this SubscribedService.
        :type: str
        """
        self._data_center_region = data_center_region

    @property
    def admin_email(self):
        """
        Gets the admin_email of this SubscribedService.
        Subscribed service admin email id


        :return: The admin_email of this SubscribedService.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this SubscribedService.
        Subscribed service admin email id


        :param admin_email: The admin_email of this SubscribedService.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def buyer_email(self):
        """
        Gets the buyer_email of this SubscribedService.
        Subscribed service buyer email id


        :return: The buyer_email of this SubscribedService.
        :rtype: str
        """
        return self._buyer_email

    @buyer_email.setter
    def buyer_email(self, buyer_email):
        """
        Sets the buyer_email of this SubscribedService.
        Subscribed service buyer email id


        :param buyer_email: The buyer_email of this SubscribedService.
        :type: str
        """
        self._buyer_email = buyer_email

    @property
    def subscription_source(self):
        """
        Gets the subscription_source of this SubscribedService.
        Subscribed service source


        :return: The subscription_source of this SubscribedService.
        :rtype: str
        """
        return self._subscription_source

    @subscription_source.setter
    def subscription_source(self, subscription_source):
        """
        Sets the subscription_source of this SubscribedService.
        Subscribed service source


        :param subscription_source: The subscription_source of this SubscribedService.
        :type: str
        """
        self._subscription_source = subscription_source

    @property
    def provisioning_source(self):
        """
        Gets the provisioning_source of this SubscribedService.
        Subscribed service provisioning source


        :return: The provisioning_source of this SubscribedService.
        :rtype: str
        """
        return self._provisioning_source

    @provisioning_source.setter
    def provisioning_source(self, provisioning_source):
        """
        Sets the provisioning_source of this SubscribedService.
        Subscribed service provisioning source


        :param provisioning_source: The provisioning_source of this SubscribedService.
        :type: str
        """
        self._provisioning_source = provisioning_source

    @property
    def fulfillment_set(self):
        """
        Gets the fulfillment_set of this SubscribedService.
        Subscribed service fulfillment set


        :return: The fulfillment_set of this SubscribedService.
        :rtype: str
        """
        return self._fulfillment_set

    @fulfillment_set.setter
    def fulfillment_set(self, fulfillment_set):
        """
        Sets the fulfillment_set of this SubscribedService.
        Subscribed service fulfillment set


        :param fulfillment_set: The fulfillment_set of this SubscribedService.
        :type: str
        """
        self._fulfillment_set = fulfillment_set

    @property
    def is_intent_to_pay(self):
        """
        Gets the is_intent_to_pay of this SubscribedService.
        Subscribed service intent to pay flag


        :return: The is_intent_to_pay of this SubscribedService.
        :rtype: bool
        """
        return self._is_intent_to_pay

    @is_intent_to_pay.setter
    def is_intent_to_pay(self, is_intent_to_pay):
        """
        Sets the is_intent_to_pay of this SubscribedService.
        Subscribed service intent to pay flag


        :param is_intent_to_pay: The is_intent_to_pay of this SubscribedService.
        :type: bool
        """
        self._is_intent_to_pay = is_intent_to_pay

    @property
    def is_payg(self):
        """
        Gets the is_payg of this SubscribedService.
        Subscribed service payg flag


        :return: The is_payg of this SubscribedService.
        :rtype: bool
        """
        return self._is_payg

    @is_payg.setter
    def is_payg(self, is_payg):
        """
        Sets the is_payg of this SubscribedService.
        Subscribed service payg flag


        :param is_payg: The is_payg of this SubscribedService.
        :type: bool
        """
        self._is_payg = is_payg

    @property
    def pricing_model(self):
        """
        Gets the pricing_model of this SubscribedService.
        Subscribed service pricing model


        :return: The pricing_model of this SubscribedService.
        :rtype: str
        """
        return self._pricing_model

    @pricing_model.setter
    def pricing_model(self, pricing_model):
        """
        Sets the pricing_model of this SubscribedService.
        Subscribed service pricing model


        :param pricing_model: The pricing_model of this SubscribedService.
        :type: str
        """
        self._pricing_model = pricing_model

    @property
    def program_type(self):
        """
        Gets the program_type of this SubscribedService.
        Subscribed service program type


        :return: The program_type of this SubscribedService.
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type):
        """
        Sets the program_type of this SubscribedService.
        Subscribed service program type


        :param program_type: The program_type of this SubscribedService.
        :type: str
        """
        self._program_type = program_type

    @property
    def start_date_type(self):
        """
        Gets the start_date_type of this SubscribedService.
        Subscribed service start date type


        :return: The start_date_type of this SubscribedService.
        :rtype: str
        """
        return self._start_date_type

    @start_date_type.setter
    def start_date_type(self, start_date_type):
        """
        Sets the start_date_type of this SubscribedService.
        Subscribed service start date type


        :param start_date_type: The start_date_type of this SubscribedService.
        :type: str
        """
        self._start_date_type = start_date_type

    @property
    def time_provisioned(self):
        """
        Gets the time_provisioned of this SubscribedService.
        Subscribed service provisioning date


        :return: The time_provisioned of this SubscribedService.
        :rtype: datetime
        """
        return self._time_provisioned

    @time_provisioned.setter
    def time_provisioned(self, time_provisioned):
        """
        Sets the time_provisioned of this SubscribedService.
        Subscribed service provisioning date


        :param time_provisioned: The time_provisioned of this SubscribedService.
        :type: datetime
        """
        self._time_provisioned = time_provisioned

    @property
    def promo_type(self):
        """
        Gets the promo_type of this SubscribedService.
        Subscribed service promotion type


        :return: The promo_type of this SubscribedService.
        :rtype: str
        """
        return self._promo_type

    @promo_type.setter
    def promo_type(self, promo_type):
        """
        Sets the promo_type of this SubscribedService.
        Subscribed service promotion type


        :param promo_type: The promo_type of this SubscribedService.
        :type: str
        """
        self._promo_type = promo_type

    @property
    def service_to_customer(self):
        """
        Gets the service_to_customer of this SubscribedService.

        :return: The service_to_customer of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        return self._service_to_customer

    @service_to_customer.setter
    def service_to_customer(self, service_to_customer):
        """
        Sets the service_to_customer of this SubscribedService.

        :param service_to_customer: The service_to_customer of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        self._service_to_customer = service_to_customer

    @property
    def service_to_contact(self):
        """
        Gets the service_to_contact of this SubscribedService.

        :return: The service_to_contact of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceUser
        """
        return self._service_to_contact

    @service_to_contact.setter
    def service_to_contact(self, service_to_contact):
        """
        Sets the service_to_contact of this SubscribedService.

        :param service_to_contact: The service_to_contact of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceUser
        """
        self._service_to_contact = service_to_contact

    @property
    def service_to_address(self):
        """
        Gets the service_to_address of this SubscribedService.

        :return: The service_to_address of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceAddress
        """
        return self._service_to_address

    @service_to_address.setter
    def service_to_address(self, service_to_address):
        """
        Sets the service_to_address of this SubscribedService.

        :param service_to_address: The service_to_address of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceAddress
        """
        self._service_to_address = service_to_address

    @property
    def sold_to_customer(self):
        """
        Gets the sold_to_customer of this SubscribedService.

        :return: The sold_to_customer of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        return self._sold_to_customer

    @sold_to_customer.setter
    def sold_to_customer(self, sold_to_customer):
        """
        Sets the sold_to_customer of this SubscribedService.

        :param sold_to_customer: The sold_to_customer of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        self._sold_to_customer = sold_to_customer

    @property
    def sold_to_contact(self):
        """
        Gets the sold_to_contact of this SubscribedService.

        :return: The sold_to_contact of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceUser
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """
        Sets the sold_to_contact of this SubscribedService.

        :param sold_to_contact: The sold_to_contact of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceUser
        """
        self._sold_to_contact = sold_to_contact

    @property
    def end_user_customer(self):
        """
        Gets the end_user_customer of this SubscribedService.

        :return: The end_user_customer of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        return self._end_user_customer

    @end_user_customer.setter
    def end_user_customer(self, end_user_customer):
        """
        Sets the end_user_customer of this SubscribedService.

        :param end_user_customer: The end_user_customer of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        self._end_user_customer = end_user_customer

    @property
    def end_user_contact(self):
        """
        Gets the end_user_contact of this SubscribedService.

        :return: The end_user_contact of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceUser
        """
        return self._end_user_contact

    @end_user_contact.setter
    def end_user_contact(self, end_user_contact):
        """
        Sets the end_user_contact of this SubscribedService.

        :param end_user_contact: The end_user_contact of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceUser
        """
        self._end_user_contact = end_user_contact

    @property
    def end_user_address(self):
        """
        Gets the end_user_address of this SubscribedService.

        :return: The end_user_address of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceAddress
        """
        return self._end_user_address

    @end_user_address.setter
    def end_user_address(self, end_user_address):
        """
        Sets the end_user_address of this SubscribedService.

        :param end_user_address: The end_user_address of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceAddress
        """
        self._end_user_address = end_user_address

    @property
    def reseller_customer(self):
        """
        Gets the reseller_customer of this SubscribedService.

        :return: The reseller_customer of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        return self._reseller_customer

    @reseller_customer.setter
    def reseller_customer(self, reseller_customer):
        """
        Sets the reseller_customer of this SubscribedService.

        :param reseller_customer: The reseller_customer of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceBusinessPartner
        """
        self._reseller_customer = reseller_customer

    @property
    def reseller_contact(self):
        """
        Gets the reseller_contact of this SubscribedService.

        :return: The reseller_contact of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceUser
        """
        return self._reseller_contact

    @reseller_contact.setter
    def reseller_contact(self, reseller_contact):
        """
        Sets the reseller_contact of this SubscribedService.

        :param reseller_contact: The reseller_contact of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceUser
        """
        self._reseller_contact = reseller_contact

    @property
    def reseller_address(self):
        """
        Gets the reseller_address of this SubscribedService.

        :return: The reseller_address of this SubscribedService.
        :rtype: oci.onesubscription.models.SubscribedServiceAddress
        """
        return self._reseller_address

    @reseller_address.setter
    def reseller_address(self, reseller_address):
        """
        Sets the reseller_address of this SubscribedService.

        :param reseller_address: The reseller_address of this SubscribedService.
        :type: oci.onesubscription.models.SubscribedServiceAddress
        """
        self._reseller_address = reseller_address

    @property
    def csi(self):
        """
        Gets the csi of this SubscribedService.
        Subscribed service CSI number


        :return: The csi of this SubscribedService.
        :rtype: int
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """
        Sets the csi of this SubscribedService.
        Subscribed service CSI number


        :param csi: The csi of this SubscribedService.
        :type: int
        """
        self._csi = csi

    @property
    def customer_transaction_reference(self):
        """
        Gets the customer_transaction_reference of this SubscribedService.
        Identifier for a customer's transactions for purchase of ay oracle services


        :return: The customer_transaction_reference of this SubscribedService.
        :rtype: str
        """
        return self._customer_transaction_reference

    @customer_transaction_reference.setter
    def customer_transaction_reference(self, customer_transaction_reference):
        """
        Sets the customer_transaction_reference of this SubscribedService.
        Identifier for a customer's transactions for purchase of ay oracle services


        :param customer_transaction_reference: The customer_transaction_reference of this SubscribedService.
        :type: str
        """
        self._customer_transaction_reference = customer_transaction_reference

    @property
    def partner_credit_amount(self):
        """
        Gets the partner_credit_amount of this SubscribedService.
        Subscribed service partner credit amount


        :return: The partner_credit_amount of this SubscribedService.
        :rtype: str
        """
        return self._partner_credit_amount

    @partner_credit_amount.setter
    def partner_credit_amount(self, partner_credit_amount):
        """
        Sets the partner_credit_amount of this SubscribedService.
        Subscribed service partner credit amount


        :param partner_credit_amount: The partner_credit_amount of this SubscribedService.
        :type: str
        """
        self._partner_credit_amount = partner_credit_amount

    @property
    def is_single_rate_card(self):
        """
        Gets the is_single_rate_card of this SubscribedService.
        Indicates if the Subscribed service has a single ratecard


        :return: The is_single_rate_card of this SubscribedService.
        :rtype: bool
        """
        return self._is_single_rate_card

    @is_single_rate_card.setter
    def is_single_rate_card(self, is_single_rate_card):
        """
        Sets the is_single_rate_card of this SubscribedService.
        Indicates if the Subscribed service has a single ratecard


        :param is_single_rate_card: The is_single_rate_card of this SubscribedService.
        :type: bool
        """
        self._is_single_rate_card = is_single_rate_card

    @property
    def agreement_id(self):
        """
        Gets the agreement_id of this SubscribedService.
        Subscribed service agreement ID


        :return: The agreement_id of this SubscribedService.
        :rtype: int
        """
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, agreement_id):
        """
        Sets the agreement_id of this SubscribedService.
        Subscribed service agreement ID


        :param agreement_id: The agreement_id of this SubscribedService.
        :type: int
        """
        self._agreement_id = agreement_id

    @property
    def agreement_name(self):
        """
        Gets the agreement_name of this SubscribedService.
        Subscribed service agrrement name


        :return: The agreement_name of this SubscribedService.
        :rtype: str
        """
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, agreement_name):
        """
        Sets the agreement_name of this SubscribedService.
        Subscribed service agrrement name


        :param agreement_name: The agreement_name of this SubscribedService.
        :type: str
        """
        self._agreement_name = agreement_name

    @property
    def agreement_type(self):
        """
        Gets the agreement_type of this SubscribedService.
        Subscribed service agrrement type


        :return: The agreement_type of this SubscribedService.
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        """
        Sets the agreement_type of this SubscribedService.
        Subscribed service agrrement type


        :param agreement_type: The agreement_type of this SubscribedService.
        :type: str
        """
        self._agreement_type = agreement_type

    @property
    def billing_frequency(self):
        """
        Gets the billing_frequency of this SubscribedService.
        Subscribed service invoice frequency


        :return: The billing_frequency of this SubscribedService.
        :rtype: str
        """
        return self._billing_frequency

    @billing_frequency.setter
    def billing_frequency(self, billing_frequency):
        """
        Sets the billing_frequency of this SubscribedService.
        Subscribed service invoice frequency


        :param billing_frequency: The billing_frequency of this SubscribedService.
        :type: str
        """
        self._billing_frequency = billing_frequency

    @property
    def time_welcome_email_sent(self):
        """
        Gets the time_welcome_email_sent of this SubscribedService.
        Subscribed service welcome email sent date


        :return: The time_welcome_email_sent of this SubscribedService.
        :rtype: datetime
        """
        return self._time_welcome_email_sent

    @time_welcome_email_sent.setter
    def time_welcome_email_sent(self, time_welcome_email_sent):
        """
        Sets the time_welcome_email_sent of this SubscribedService.
        Subscribed service welcome email sent date


        :param time_welcome_email_sent: The time_welcome_email_sent of this SubscribedService.
        :type: datetime
        """
        self._time_welcome_email_sent = time_welcome_email_sent

    @property
    def time_service_configuration_email_sent(self):
        """
        Gets the time_service_configuration_email_sent of this SubscribedService.
        Subscribed service service configuration email sent date


        :return: The time_service_configuration_email_sent of this SubscribedService.
        :rtype: datetime
        """
        return self._time_service_configuration_email_sent

    @time_service_configuration_email_sent.setter
    def time_service_configuration_email_sent(self, time_service_configuration_email_sent):
        """
        Sets the time_service_configuration_email_sent of this SubscribedService.
        Subscribed service service configuration email sent date


        :param time_service_configuration_email_sent: The time_service_configuration_email_sent of this SubscribedService.
        :type: datetime
        """
        self._time_service_configuration_email_sent = time_service_configuration_email_sent

    @property
    def time_customer_config(self):
        """
        Gets the time_customer_config of this SubscribedService.
        Subscribed service customer config date


        :return: The time_customer_config of this SubscribedService.
        :rtype: datetime
        """
        return self._time_customer_config

    @time_customer_config.setter
    def time_customer_config(self, time_customer_config):
        """
        Sets the time_customer_config of this SubscribedService.
        Subscribed service customer config date


        :param time_customer_config: The time_customer_config of this SubscribedService.
        :type: datetime
        """
        self._time_customer_config = time_customer_config

    @property
    def time_agreement_end(self):
        """
        Gets the time_agreement_end of this SubscribedService.
        Subscribed service agrrement end date


        :return: The time_agreement_end of this SubscribedService.
        :rtype: datetime
        """
        return self._time_agreement_end

    @time_agreement_end.setter
    def time_agreement_end(self, time_agreement_end):
        """
        Sets the time_agreement_end of this SubscribedService.
        Subscribed service agrrement end date


        :param time_agreement_end: The time_agreement_end of this SubscribedService.
        :type: datetime
        """
        self._time_agreement_end = time_agreement_end

    @property
    def commitment_services(self):
        """
        Gets the commitment_services of this SubscribedService.
        List of Commitment services of a line


        :return: The commitment_services of this SubscribedService.
        :rtype: list[oci.onesubscription.models.CommitmentService]
        """
        return self._commitment_services

    @commitment_services.setter
    def commitment_services(self, commitment_services):
        """
        Sets the commitment_services of this SubscribedService.
        List of Commitment services of a line


        :param commitment_services: The commitment_services of this SubscribedService.
        :type: list[oci.onesubscription.models.CommitmentService]
        """
        self._commitment_services = commitment_services

    @property
    def rate_cards(self):
        """
        Gets the rate_cards of this SubscribedService.
        List of Rate Cards of a Subscribed Service


        :return: The rate_cards of this SubscribedService.
        :rtype: list[oci.onesubscription.models.RateCardSummary]
        """
        return self._rate_cards

    @rate_cards.setter
    def rate_cards(self, rate_cards):
        """
        Sets the rate_cards of this SubscribedService.
        List of Rate Cards of a Subscribed Service


        :param rate_cards: The rate_cards of this SubscribedService.
        :type: list[oci.onesubscription.models.RateCardSummary]
        """
        self._rate_cards = rate_cards

    @property
    def time_created(self):
        """
        Gets the time_created of this SubscribedService.
        Subscribed service creation date


        :return: The time_created of this SubscribedService.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SubscribedService.
        Subscribed service creation date


        :param time_created: The time_created of this SubscribedService.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def created_by(self):
        """
        Gets the created_by of this SubscribedService.
        User that created the subscribed service


        :return: The created_by of this SubscribedService.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this SubscribedService.
        User that created the subscribed service


        :param created_by: The created_by of this SubscribedService.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SubscribedService.
        Subscribed service last update date


        :return: The time_updated of this SubscribedService.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SubscribedService.
        Subscribed service last update date


        :param time_updated: The time_updated of this SubscribedService.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def updated_by(self):
        """
        Gets the updated_by of this SubscribedService.
        User that updated the subscribed service


        :return: The updated_by of this SubscribedService.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this SubscribedService.
        User that updated the subscribed service


        :param updated_by: The updated_by of this SubscribedService.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def ratecard_type(self):
        """
        Gets the ratecard_type of this SubscribedService.
        SPM Ratecard Type


        :return: The ratecard_type of this SubscribedService.
        :rtype: str
        """
        return self._ratecard_type

    @ratecard_type.setter
    def ratecard_type(self, ratecard_type):
        """
        Sets the ratecard_type of this SubscribedService.
        SPM Ratecard Type


        :param ratecard_type: The ratecard_type of this SubscribedService.
        :type: str
        """
        self._ratecard_type = ratecard_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
