# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .alert_rule import AlertRule
from .alert_rule_summary import AlertRuleSummary
from .budget import Budget
from .budget_summary import BudgetSummary
from .create_alert_rule_details import CreateAlertRuleDetails
from .create_budget_details import CreateBudgetDetails
from .update_alert_rule_details import UpdateAlertRuleDetails
from .update_budget_details import UpdateBudgetDetails

# Maps type names to classes for budget services.
budget_type_mapping = {
    "AlertRule": AlertRule,
    "AlertRuleSummary": AlertRuleSummary,
    "Budget": Budget,
    "BudgetSummary": BudgetSummary,
    "CreateAlertRuleDetails": CreateAlertRuleDetails,
    "CreateBudgetDetails": CreateBudgetDetails,
    "UpdateAlertRuleDetails": UpdateAlertRuleDetails,
    "UpdateBudgetDetails": UpdateBudgetDetails
}
