# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to you can create a budget and an alert rule on the budget.
# It then shows how to perform updates, reads, and deletes. It will:
#
#   * Create a budget
#   * List budgets in the compartment
#   * Get a single budget (the one that was created above)
#   * Create an alert rule on the budget to trigger when forecast spend reaches 100% of the budget amount, specifically:
#       type: FORECAST
#       threshold: 100
#       thresholdType: PERCENTAGE
#   * List alert rules in the budget
#   * Get a single alert rule (the one that was created above)
#   * Update the budget amount
#   * Update the alert rule threshold
#   * Delete the alert rule
#   * Delete the budget
#
# This script accepts five arguments:
#
#   * The ocid of the compartment for the budget, which should be the tenancy root compartment
#   * The target type of the budget, which should be COMPARTMENT or TAG.
#   * The target for the budget.
#       For COMPARTMENT budget, this should be the target compartment OCID;
#       For TAG budget, this should be the target tag in String format 'TagNamespace.TagDefinition.TagValue'.
#   * The amount for the budget, which should an unformatted number.
#   * An email address to be used as the budget alert rule recipient.
#

import oci
import sys

# Default config file and profile
config = oci.config.from_file()
budget_client = oci.budget.BudgetClient(config)

if len(sys.argv) != 6:
    raise RuntimeError('This example expects 5 arguments: compartment OCID, target type (COMPARTMENT or TAG), target (compartment OCID or cost tracking tag in String format \'TagNamespace.TagDefinition.TagValue\', budget amount, alert rule recipient')

# The first argument is the name of the script, so start the index at 1
compartment_id = sys.argv[1]
target_type = sys.argv[2]
target = sys.argv[3]
amount = sys.argv[4]
recipient = sys.argv[5]

# create a budget
create_budget_response = budget_client.create_budget(
    oci.budget.models.CreateBudgetDetails(
        compartment_id=compartment_id,
        target_type=target_type,
        targets=[target],
        amount=float(amount),
        reset_period="MONTHLY"
    )
)
print('Created budget:')
print(create_budget_response.data)

budget_id = create_budget_response.data.id

# list all budgets
budgets = oci.pagination.list_call_get_all_results(
    budget_client.list_budgets,
    compartment_id
).data
print('ListBudgets for compartment with OCID: {}'.format(compartment_id))
for budget in budgets:
    print(budget)

# get a single budget
get_budget_response = budget_client.get_budget(
    budget_id
)
print('GetBudget with OCID: {}'.format(get_budget_response.data.id))
print(get_budget_response.data)

# create alert rule on the budget
create_alert_rule_response = budget_client.create_alert_rule(
    budget_id,
    oci.budget.models.CreateAlertRuleDetails(
        type="FORECAST",
        threshold=float(100),
        threshold_type="PERCENTAGE",
        recipients=recipient
    )
)
print('Created AlertRule:')
print(create_alert_rule_response.data)

alert_rule_id = create_alert_rule_response.data.id

# list out all alert rules on the budget
alert_rules = oci.pagination.list_call_get_all_results(
    budget_client.list_alert_rules,
    budget_id
).data
print('ListAlertRules for budget with OCID:{}'.format(budget_id))
for budget in budgets:
    print(budget)

# get a single alert rule (the one we just created)
get_alert_rule_response = budget_client.get_alert_rule(
    budget_id,
    alert_rule_id
)
print('GetAlertRule with OCID:{}'.format(alert_rule_id))
print(get_alert_rule_response.data)

# update the budget amount to increase it by 10%
update_budget_response = budget_client.update_budget(
    budget_id,
    oci.budget.models.UpdateBudgetDetails(
        amount=float(amount) * 1.1
    )
)
print('Updated budget with OCID: {}'.format(budget_id))
print('New budget amount = {}'.format(update_budget_response.data.amount))

# update the alert rule to make it trigger at 80% of actual spend and add a message.
update_alert_rule_response = budget_client.update_alert_rule(
    budget_id,
    alert_rule_id,
    oci.budget.models.UpdateAlertRuleDetails(
        threshold=float(80),
        type='ACTUAL',
        message='Spending has reached 80% of the budget'
    )
)
print('Updated AlertRule with OCID: {}'.format(alert_rule_id))
print('New alert rule threshold = {}, type = {}'.format(update_alert_rule_response.data.threshold, update_alert_rule_response.data.type))

# (Clean-up) delete the alert rule
delete_alert_rule_response = budget_client.delete_alert_rule(
    budget_id=budget_id,
    alert_rule_id=alert_rule_id
)
print('Delete AlertRule with OCID: {}'.format(alert_rule_id))

# (Clean-up) delete the budget
# Note, this triggers a cascading delete of all alert rules in the budget, and would have deleted the alert rule above.
delete_budget_response = budget_client.delete_budget(
    budget_id=budget_id
)
print('Delete Budget with OCID: {}'.format(budget_id))


print('\nScript Finished')
