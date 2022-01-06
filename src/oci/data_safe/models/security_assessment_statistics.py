# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAssessmentStatistics(object):
    """
    Statistics showing the number of findings for each category grouped by risk levels for all
    the targets in the specified security assessment.

    The categories include Auditing, Authorization Control, Data Encryption, Database Configuration,
    Fine-Grained Access Control, Privileges and Roles, and User Accounts.
    The risk levels include High Risk, Medium Risk, Low Risk, Advisory, Evaluate, and Pass.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAssessmentStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets_count:
            The value to assign to the targets_count property of this SecurityAssessmentStatistics.
        :type targets_count: int

        :param high_risk:
            The value to assign to the high_risk property of this SecurityAssessmentStatistics.
        :type high_risk: oci.data_safe.models.SectionStatistics

        :param medium_risk:
            The value to assign to the medium_risk property of this SecurityAssessmentStatistics.
        :type medium_risk: oci.data_safe.models.SectionStatistics

        :param low_risk:
            The value to assign to the low_risk property of this SecurityAssessmentStatistics.
        :type low_risk: oci.data_safe.models.SectionStatistics

        :param advisory:
            The value to assign to the advisory property of this SecurityAssessmentStatistics.
        :type advisory: oci.data_safe.models.SectionStatistics

        :param evaluate:
            The value to assign to the evaluate property of this SecurityAssessmentStatistics.
        :type evaluate: oci.data_safe.models.SectionStatistics

        :param _pass:
            The value to assign to the _pass property of this SecurityAssessmentStatistics.
        :type _pass: oci.data_safe.models.SectionStatistics

        """
        self.swagger_types = {
            'targets_count': 'int',
            'high_risk': 'SectionStatistics',
            'medium_risk': 'SectionStatistics',
            'low_risk': 'SectionStatistics',
            'advisory': 'SectionStatistics',
            'evaluate': 'SectionStatistics',
            '_pass': 'SectionStatistics'
        }

        self.attribute_map = {
            'targets_count': 'targetsCount',
            'high_risk': 'highRisk',
            'medium_risk': 'mediumRisk',
            'low_risk': 'lowRisk',
            'advisory': 'advisory',
            'evaluate': 'evaluate',
            '_pass': 'pass'
        }

        self._targets_count = None
        self._high_risk = None
        self._medium_risk = None
        self._low_risk = None
        self._advisory = None
        self._evaluate = None
        self.__pass = None

    @property
    def targets_count(self):
        """
        Gets the targets_count of this SecurityAssessmentStatistics.
        The total number of targets in this security assessment.


        :return: The targets_count of this SecurityAssessmentStatistics.
        :rtype: int
        """
        return self._targets_count

    @targets_count.setter
    def targets_count(self, targets_count):
        """
        Sets the targets_count of this SecurityAssessmentStatistics.
        The total number of targets in this security assessment.


        :param targets_count: The targets_count of this SecurityAssessmentStatistics.
        :type: int
        """
        self._targets_count = targets_count

    @property
    def high_risk(self):
        """
        Gets the high_risk of this SecurityAssessmentStatistics.

        :return: The high_risk of this SecurityAssessmentStatistics.
        :rtype: oci.data_safe.models.SectionStatistics
        """
        return self._high_risk

    @high_risk.setter
    def high_risk(self, high_risk):
        """
        Sets the high_risk of this SecurityAssessmentStatistics.

        :param high_risk: The high_risk of this SecurityAssessmentStatistics.
        :type: oci.data_safe.models.SectionStatistics
        """
        self._high_risk = high_risk

    @property
    def medium_risk(self):
        """
        Gets the medium_risk of this SecurityAssessmentStatistics.

        :return: The medium_risk of this SecurityAssessmentStatistics.
        :rtype: oci.data_safe.models.SectionStatistics
        """
        return self._medium_risk

    @medium_risk.setter
    def medium_risk(self, medium_risk):
        """
        Sets the medium_risk of this SecurityAssessmentStatistics.

        :param medium_risk: The medium_risk of this SecurityAssessmentStatistics.
        :type: oci.data_safe.models.SectionStatistics
        """
        self._medium_risk = medium_risk

    @property
    def low_risk(self):
        """
        Gets the low_risk of this SecurityAssessmentStatistics.

        :return: The low_risk of this SecurityAssessmentStatistics.
        :rtype: oci.data_safe.models.SectionStatistics
        """
        return self._low_risk

    @low_risk.setter
    def low_risk(self, low_risk):
        """
        Sets the low_risk of this SecurityAssessmentStatistics.

        :param low_risk: The low_risk of this SecurityAssessmentStatistics.
        :type: oci.data_safe.models.SectionStatistics
        """
        self._low_risk = low_risk

    @property
    def advisory(self):
        """
        Gets the advisory of this SecurityAssessmentStatistics.

        :return: The advisory of this SecurityAssessmentStatistics.
        :rtype: oci.data_safe.models.SectionStatistics
        """
        return self._advisory

    @advisory.setter
    def advisory(self, advisory):
        """
        Sets the advisory of this SecurityAssessmentStatistics.

        :param advisory: The advisory of this SecurityAssessmentStatistics.
        :type: oci.data_safe.models.SectionStatistics
        """
        self._advisory = advisory

    @property
    def evaluate(self):
        """
        Gets the evaluate of this SecurityAssessmentStatistics.

        :return: The evaluate of this SecurityAssessmentStatistics.
        :rtype: oci.data_safe.models.SectionStatistics
        """
        return self._evaluate

    @evaluate.setter
    def evaluate(self, evaluate):
        """
        Sets the evaluate of this SecurityAssessmentStatistics.

        :param evaluate: The evaluate of this SecurityAssessmentStatistics.
        :type: oci.data_safe.models.SectionStatistics
        """
        self._evaluate = evaluate

    @property
    def _pass(self):
        """
        Gets the _pass of this SecurityAssessmentStatistics.

        :return: The _pass of this SecurityAssessmentStatistics.
        :rtype: oci.data_safe.models.SectionStatistics
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """
        Sets the _pass of this SecurityAssessmentStatistics.

        :param _pass: The _pass of this SecurityAssessmentStatistics.
        :type: oci.data_safe.models.SectionStatistics
        """
        self.__pass = _pass

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
