# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .certificate_rule import CertificateRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateRenewalRule(CertificateRule):
    """
    A rule that imposes constraints on certificate renewal.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateRenewalRule object with values from keyword arguments. The default value of the :py:attr:`~oci.certificates_management.models.CertificateRenewalRule.rule_type` attribute
        of this class is ``CERTIFICATE_RENEWAL_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule_type:
            The value to assign to the rule_type property of this CertificateRenewalRule.
            Allowed values for this property are: "CERTIFICATE_RENEWAL_RULE"
        :type rule_type: str

        :param renewal_interval:
            The value to assign to the renewal_interval property of this CertificateRenewalRule.
        :type renewal_interval: str

        :param advance_renewal_period:
            The value to assign to the advance_renewal_period property of this CertificateRenewalRule.
        :type advance_renewal_period: str

        """
        self.swagger_types = {
            'rule_type': 'str',
            'renewal_interval': 'str',
            'advance_renewal_period': 'str'
        }

        self.attribute_map = {
            'rule_type': 'ruleType',
            'renewal_interval': 'renewalInterval',
            'advance_renewal_period': 'advanceRenewalPeriod'
        }

        self._rule_type = None
        self._renewal_interval = None
        self._advance_renewal_period = None
        self._rule_type = 'CERTIFICATE_RENEWAL_RULE'

    @property
    def renewal_interval(self):
        """
        **[Required]** Gets the renewal_interval of this CertificateRenewalRule.
        A property specifying how often, in days, a certificate should be renewed.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :return: The renewal_interval of this CertificateRenewalRule.
        :rtype: str
        """
        return self._renewal_interval

    @renewal_interval.setter
    def renewal_interval(self, renewal_interval):
        """
        Sets the renewal_interval of this CertificateRenewalRule.
        A property specifying how often, in days, a certificate should be renewed.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :param renewal_interval: The renewal_interval of this CertificateRenewalRule.
        :type: str
        """
        self._renewal_interval = renewal_interval

    @property
    def advance_renewal_period(self):
        """
        **[Required]** Gets the advance_renewal_period of this CertificateRenewalRule.
        A property specifying the period of time, in days, before the certificate's targeted renewal that the process should occur.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :return: The advance_renewal_period of this CertificateRenewalRule.
        :rtype: str
        """
        return self._advance_renewal_period

    @advance_renewal_period.setter
    def advance_renewal_period(self, advance_renewal_period):
        """
        Sets the advance_renewal_period of this CertificateRenewalRule.
        A property specifying the period of time, in days, before the certificate's targeted renewal that the process should occur.
        Expressed in `ISO 8601`__ format.

        __ https://en.wikipedia.org/wiki/ISO_8601#Time_intervals


        :param advance_renewal_period: The advance_renewal_period of this CertificateRenewalRule.
        :type: str
        """
        self._advance_renewal_period = advance_renewal_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
