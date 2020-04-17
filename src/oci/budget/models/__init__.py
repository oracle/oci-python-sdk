# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
