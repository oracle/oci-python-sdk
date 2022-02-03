# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaxInfo(object):
    """
    Tax details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaxInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tax_payer_id:
            The value to assign to the tax_payer_id property of this TaxInfo.
        :type tax_payer_id: str

        :param tax_reg_number:
            The value to assign to the tax_reg_number property of this TaxInfo.
        :type tax_reg_number: str

        :param no_tax_reason_code:
            The value to assign to the no_tax_reason_code property of this TaxInfo.
        :type no_tax_reason_code: str

        :param no_tax_reason_code_details:
            The value to assign to the no_tax_reason_code_details property of this TaxInfo.
        :type no_tax_reason_code_details: str

        :param tax_cnpj:
            The value to assign to the tax_cnpj property of this TaxInfo.
        :type tax_cnpj: str

        """
        self.swagger_types = {
            'tax_payer_id': 'str',
            'tax_reg_number': 'str',
            'no_tax_reason_code': 'str',
            'no_tax_reason_code_details': 'str',
            'tax_cnpj': 'str'
        }

        self.attribute_map = {
            'tax_payer_id': 'taxPayerId',
            'tax_reg_number': 'taxRegNumber',
            'no_tax_reason_code': 'noTaxReasonCode',
            'no_tax_reason_code_details': 'noTaxReasonCodeDetails',
            'tax_cnpj': 'taxCnpj'
        }

        self._tax_payer_id = None
        self._tax_reg_number = None
        self._no_tax_reason_code = None
        self._no_tax_reason_code_details = None
        self._tax_cnpj = None

    @property
    def tax_payer_id(self):
        """
        Gets the tax_payer_id of this TaxInfo.
        Tay payer identifier.


        :return: The tax_payer_id of this TaxInfo.
        :rtype: str
        """
        return self._tax_payer_id

    @tax_payer_id.setter
    def tax_payer_id(self, tax_payer_id):
        """
        Sets the tax_payer_id of this TaxInfo.
        Tay payer identifier.


        :param tax_payer_id: The tax_payer_id of this TaxInfo.
        :type: str
        """
        self._tax_payer_id = tax_payer_id

    @property
    def tax_reg_number(self):
        """
        Gets the tax_reg_number of this TaxInfo.
        Tax registration number.


        :return: The tax_reg_number of this TaxInfo.
        :rtype: str
        """
        return self._tax_reg_number

    @tax_reg_number.setter
    def tax_reg_number(self, tax_reg_number):
        """
        Sets the tax_reg_number of this TaxInfo.
        Tax registration number.


        :param tax_reg_number: The tax_reg_number of this TaxInfo.
        :type: str
        """
        self._tax_reg_number = tax_reg_number

    @property
    def no_tax_reason_code(self):
        """
        Gets the no_tax_reason_code of this TaxInfo.
        Tax exemption reason code.


        :return: The no_tax_reason_code of this TaxInfo.
        :rtype: str
        """
        return self._no_tax_reason_code

    @no_tax_reason_code.setter
    def no_tax_reason_code(self, no_tax_reason_code):
        """
        Sets the no_tax_reason_code of this TaxInfo.
        Tax exemption reason code.


        :param no_tax_reason_code: The no_tax_reason_code of this TaxInfo.
        :type: str
        """
        self._no_tax_reason_code = no_tax_reason_code

    @property
    def no_tax_reason_code_details(self):
        """
        Gets the no_tax_reason_code_details of this TaxInfo.
        Tax exemption reason description.


        :return: The no_tax_reason_code_details of this TaxInfo.
        :rtype: str
        """
        return self._no_tax_reason_code_details

    @no_tax_reason_code_details.setter
    def no_tax_reason_code_details(self, no_tax_reason_code_details):
        """
        Sets the no_tax_reason_code_details of this TaxInfo.
        Tax exemption reason description.


        :param no_tax_reason_code_details: The no_tax_reason_code_details of this TaxInfo.
        :type: str
        """
        self._no_tax_reason_code_details = no_tax_reason_code_details

    @property
    def tax_cnpj(self):
        """
        Gets the tax_cnpj of this TaxInfo.
        Brazilian companies' CNPJ number.


        :return: The tax_cnpj of this TaxInfo.
        :rtype: str
        """
        return self._tax_cnpj

    @tax_cnpj.setter
    def tax_cnpj(self, tax_cnpj):
        """
        Sets the tax_cnpj of this TaxInfo.
        Brazilian companies' CNPJ number.


        :param tax_cnpj: The tax_cnpj of this TaxInfo.
        :type: str
        """
        self._tax_cnpj = tax_cnpj

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
