# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInclusionCriterionDetails(object):
    """
    Request object for Createinclusion criterion operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInclusionCriterionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param governance_rule_id:
            The value to assign to the governance_rule_id property of this CreateInclusionCriterionDetails.
        :type governance_rule_id: str

        :param type:
            The value to assign to the type property of this CreateInclusionCriterionDetails.
        :type type: str

        :param association:
            The value to assign to the association property of this CreateInclusionCriterionDetails.
        :type association: oci.governance_rules_control_plane.models.Association

        """
        self.swagger_types = {
            'governance_rule_id': 'str',
            'type': 'str',
            'association': 'Association'
        }

        self.attribute_map = {
            'governance_rule_id': 'governanceRuleId',
            'type': 'type',
            'association': 'association'
        }

        self._governance_rule_id = None
        self._type = None
        self._association = None

    @property
    def governance_rule_id(self):
        """
        **[Required]** Gets the governance_rule_id of this CreateInclusionCriterionDetails.
        The Oracle ID (`OCID`__) of the governance rule. Every inclusion criterion is associated with a governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The governance_rule_id of this CreateInclusionCriterionDetails.
        :rtype: str
        """
        return self._governance_rule_id

    @governance_rule_id.setter
    def governance_rule_id(self, governance_rule_id):
        """
        Sets the governance_rule_id of this CreateInclusionCriterionDetails.
        The Oracle ID (`OCID`__) of the governance rule. Every inclusion criterion is associated with a governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param governance_rule_id: The governance_rule_id of this CreateInclusionCriterionDetails.
        :type: str
        """
        self._governance_rule_id = governance_rule_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateInclusionCriterionDetails.
        Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.


        :return: The type of this CreateInclusionCriterionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateInclusionCriterionDetails.
        Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.


        :param type: The type of this CreateInclusionCriterionDetails.
        :type: str
        """
        self._type = type

    @property
    def association(self):
        """
        Gets the association of this CreateInclusionCriterionDetails.

        :return: The association of this CreateInclusionCriterionDetails.
        :rtype: oci.governance_rules_control_plane.models.Association
        """
        return self._association

    @association.setter
    def association(self, association):
        """
        Sets the association of this CreateInclusionCriterionDetails.

        :param association: The association of this CreateInclusionCriterionDetails.
        :type: oci.governance_rules_control_plane.models.Association
        """
        self._association = association

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
