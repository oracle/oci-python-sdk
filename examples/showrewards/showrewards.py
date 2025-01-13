# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

####################################################################################################################
# showrewards.py
#
# @author: Adi Zohar, Apr 01 2024
#
# Supports Python 3
####################################################################################################################
# Application Command line parameters
#
#   -c config         - OCI CLI Config
#   -t profile        - profile inside the config file
#   -p proxy          - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip               - Use Instance Principals for Authentication
#   -dt               - Use Instance Principals with delegation token for cloud shell
#   -include_products - Include Extract Product Per Rewards
#   -f FILE_NAME      - Write to JSON file
#   -csv              - Write to CSV files - rewards.csv, redemption.csv, reward_products.csv if -include_products specificed
#
####################################################################################################################
# Modules Included:
# - oci.identity.IdentityClient
# - OrganizationSubscriptionClient
# - oci.usage.RewardsClient
#
# APIs Used:
# - IdentityClient.get_tenancy                                     - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions                       - Policy TENANCY_INSPECT
# - OrganizationSubscriptionClient.list_organization_subscriptions - Policy ORGANIZATIONS_SUBSCRIPTION_INSPECT
# - RewardsClient.list_rewards                                     - Policy REWARDS_READ
# - RewardsClient.list_redemptions                                 - Policy REWARDS_READ
# - RewardsClient.list_products                                    - Policy REWARDS_READ
#
# Policies:
#   Allow group ShowRewardsGroup to inspect tenancies in tenancy
#   Allow group ShowRewardsGroup to inspect organizations-subscription in tenancy
#   Allow group ShowRewardsGroup to read support-rewards in tenancy
#
####################################################################################################################
import sys
import argparse
import datetime
import oci
import os
import platform
import json
import csv

version = "2024.04.02"

csv_file_rewards = "rewards.csv"
csv_file_redemption = "redemption.csv"
csv_file_reward_products = "reward_products.csv"


##########################################################################
# Print header centered
##########################################################################
def print_header(name, category):
    options = {0: 120, 1: 100, 2: 90, 3: 85}
    chars = int(options[category])
    print("")
    print('#' * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print('#' * chars)


##########################################################################
# number_format
##########################################################################
def number_format(var):
    if str(var).replace(".", "").isnumeric():
        return str("{:,.0f}".format(float(var))).rjust(12)
    return var


##########################################################################
# Create signer for Authentication
# Input - config_profile and is_instance_principals and is_delegation_token
# Output - config and signer objects
##########################################################################
def create_signer(config_file, config_profile, is_instance_principals, is_delegation_token):

    # if instance principals authentications
    if is_instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer

        except Exception:
            print_header("Error obtaining instance principals certificate, aborting", 0)
            raise SystemExit

    # -----------------------------
    # Delegation Token
    # -----------------------------
    elif is_delegation_token:

        try:
            # check if env variables OCI_CONFIG_FILE, OCI_CONFIG_PROFILE exist and use them
            env_config_file = os.environ.get('OCI_CONFIG_FILE')
            env_config_section = os.environ.get('OCI_CONFIG_PROFILE')

            # check if file exist
            if env_config_file is None or env_config_section is None:
                print("*** OCI_CONFIG_FILE and OCI_CONFIG_PROFILE env variables not found, abort. ***")
                print("")
                raise SystemExit

            config = oci.config.from_file(env_config_file, env_config_section)
            delegation_token_location = config["delegation_token_file"]

            with open(delegation_token_location, 'r') as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
                # get signer from delegation token
                signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)

                return config, signer

        except KeyError:
            print("* Key Error obtaining delegation_token_file")
            raise SystemExit

        except Exception:
            raise

    # -----------------------------
    # config file authentication
    # -----------------------------
    else:
        config = oci.config.from_file(
            (config_file if config_file else oci.config.DEFAULT_LOCATION),
            (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
        )
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        return config, signer


##########################################################################
# create csv file
##########################################################################
def export_to_csv_file(file_name, data):

    try:
        # if no data
        if len(data) == 0:
            return

        # generate fields keys
        fields = []
        for dict_ in data:
            for key in dict_:
                if key not in fields:
                    fields.append(key)

        with open(file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)

            # write header
            writer.writeheader()

            for row in data:
                writer.writerow(row)

        print("CSV: " + file_name + " created")

    except Exception as e:
        raise Exception("Error in export_to_csv_file: " + str(e.args))


##########################################################################
# rewards_report Report
##########################################################################
def rewards_csv(data):
    csv_redemption = []
    csv_rewards = []
    csv_product = []
    try:
        print("")
        for sub in data['subscriptions']:

            # redemption
            for redemption in sub['redemptions']:
                csv_redemption.append({
                    'sub_id': str(sub['id']),
                    'service_name': str(sub['service_name']),
                    'time_invoiced': str(redemption['time_invoiced']),
                    'time_redeemed': str(redemption['time_redeemed']),
                    'redemption_email': str(redemption['redemption_email']),
                    'redemption_code': str(redemption['redemption_code']),
                    'invoice_number': str(redemption['invoice_number']),
                    'invoice_currency': str(redemption['invoice_currency']),
                    'invoice_total_amount': str(redemption['invoice_total_amount']),
                    'redeemed_rewards': str(redemption['redeemed_rewards']),
                    'base_rewards': str(redemption['base_rewards']),
                    'fx_rate': str(redemption['fx_rate'])
                })

            # rewards
            for reward in sub['rewards']:
                csv_rewards.append({
                    'sub_id': str(sub['id']),
                    'service_name': str(sub['service_name']),
                    'time_usage_started': str(reward['time_usage_started']),
                    'time_usage_ended': str(reward['time_usage_ended']),
                    'time_rewards_expired': str(reward['time_rewards_expired']),
                    'time_rewards_earned': str(reward['time_rewards_earned']),
                    'usage_period_key': str(reward['usage_period_key']),
                    'usage_amount': str(reward['usage_amount']),
                    'eligible_usage_amount': str(reward['eligible_usage_amount']),
                    'ineligible_usage_amount': str(reward['ineligible_usage_amount']),
                    'available_rewards': str(reward['available_rewards']),
                    'redeemed_rewards': str(reward['redeemed_rewards']),
                    'earned_rewards': str(reward['earned_rewards']),
                    'is_manual': str(reward['is_manual'])
                })

                # rewards
                for product in reward['products']:
                    csv_product.append({
                        'sub_id': str(sub['id']),
                        'service_name': str(sub['service_name']),
                        'time_usage_started': str(reward['time_usage_started']),
                        'time_usage_ended': str(reward['time_usage_ended']),
                        'usage_period_key': str(reward['usage_period_key']),
                        'product_number': str(product['product_number']),
                        'product_name': str(product['product_name']),
                        'usage_amount': str(product['usage_amount']),
                        'earned_rewards': str(product['earned_rewards']),
                        'is_eligible_to_earn_rewards': str(product['is_eligible_to_earn_rewards'])
                    })

            # Write the files
            export_to_csv_file(csv_file_rewards, csv_rewards)
            export_to_csv_file(csv_file_redemption, csv_redemption)
            export_to_csv_file(csv_file_reward_products, csv_product)

    except Exception as e:
        print("\nException Error at 'rewards_csv' - " + str(e))


##########################################################################
# rewards_report Report
##########################################################################
def rewards_report(cmd, config, signer, tenancy):

    status = "Start"
    data = {
        'tenant_id': tenancy.id,
        'tenant_name': tenancy.name,
        'subscriptions': []
    }

    try:
        osub_org_client = oci.osub_organization_subscription.OrganizationSubscriptionClient(config, signer=signer)
        rewards_client = oci.usage.RewardsClient(config, signer=signer)

        if cmd.proxy:
            osub_org_client.base_client.session.proxies = {'https': cmd.proxy}
            rewards_client.base_client.session.proxies = {'https': cmd.proxy}

        ############################
        # Get Subscription list
        ############################
        status = "subscription_list"
        subscription_list = osub_org_client.list_organization_subscriptions(tenancy.id, "0")
        ucc_sub = [x for x in subscription_list.data if 'Universal' in x.service_name]

        for sub in ucc_sub:

            sub_info = {
                'id': sub.id,
                'service_name': str(sub.service_name),
                'currency': sub.currency.iso_code if sub.currency else "",
                'time_start': str(sub.time_start)[0:16],
                'time_end': str(sub.time_end)[0:16],
                'status': str(sub.status),
                'total_value': str(sub.total_value),
                'redemptions': [],
                'rewards_summary': {},
                'rewards': []
            }

            print_header(sub.service_name, 1)
            print("")
            print(f"Id           : {sub_info['id']}")
            print(f"Service Name : {sub_info['service_name']}")
            print(f"Currency     : {sub_info['currency']}")
            print(f"Time Start   : {sub_info['time_start']}")
            print(f"Time End     : {sub_info['time_end']}")
            print(f"Status       : {sub_info['status']}")
            print(f"Total Value  : {number_format(sub_info['total_value'])}")

            ############################
            # Get Redemptions
            ############################
            status = "list_redemptions"
            redemptions = rewards_client.list_redemptions(tenancy_id=tenancy.id, subscription_id=sub.id).data

            if redemptions:

                if redemptions.items:
                    print_header("Reward Redemptions", 3)

                # oci.usage.models.RedemptionSummary
                for ss in redemptions.items:

                    redemption = {
                        'time_invoiced': str(ss.time_invoiced)[0:16],
                        'time_redeemed': str(ss.time_redeemed)[0:16],
                        'redemption_email': str(ss.redemption_email),
                        'redemption_code': str(ss.redemption_code),
                        'invoice_number': str(ss.invoice_number),
                        'invoice_currency': str(ss.invoice_currency),
                        'invoice_total_amount': ss.invoice_total_amount,
                        'redeemed_rewards': ss.redeemed_rewards,
                        'base_rewards': ss.base_rewards,
                        'fx_rate': ss.fx_rate
                    }

                    print("")
                    print(f"time_invoiced        : {redemption['time_invoiced']}")
                    print(f"time_redeemed        : {redemption['time_redeemed']}")
                    print(f"redemption_email     : {redemption['redemption_email']}")
                    print(f"redemption_code      : {redemption['redemption_code']}")
                    print(f"invoice_number       : {redemption['invoice_number']}")
                    print(f"invoice_currency     : {redemption['invoice_currency']}")
                    print(f"invoice_total_amount : {number_format(redemption['invoice_total_amount'])}")
                    print(f"redeemed_rewards     : {number_format(redemption['redeemed_rewards'])}")
                    print(f"base_rewards         : {number_format(redemption['base_rewards'])}")
                    print(f"fx_rate              : {number_format(redemption['fx_rate'])}")

                    sub_info['redemptions'].append(redemption)

            ############################
            # Get Rewards Service
            ############################
            status = "list_rewards"
            rewards = rewards_client.list_rewards(tenancy.id, sub.id).data

            if rewards and rewards.items:

                # oci.usage.models.MonthlyRewardSummary
                for ss in rewards.items:

                    reward = {
                        'time_usage_started': str(ss.time_usage_started)[0:16],
                        'time_usage_ended': str(ss.time_usage_ended)[0:16],
                        'time_rewards_expired': str(ss.time_rewards_expired)[0:16],
                        'time_rewards_earned': str(ss.time_rewards_earned)[0:16],
                        'usage_period_key': str(ss.usage_period_key),
                        'usage_amount': ss.usage_amount,
                        'eligible_usage_amount': ss.eligible_usage_amount,
                        'ineligible_usage_amount': ss.ineligible_usage_amount,
                        'available_rewards': ss.available_rewards,
                        'redeemed_rewards': ss.redeemed_rewards,
                        'earned_rewards': ss.earned_rewards,
                        'is_manual': ss.is_manual,
                        'products': []
                    }

                    # extract products if flag specified
                    if cmd.include_products:
                        status = "list_products"
                        products = rewards_client.list_products(tenancy.id, sub.id, ss.usage_period_key).data

                        for p in products.items:
                            prd = {
                                'product_number': str(p.product_number),
                                'product_name': str(p.product_name),
                                'usage_amount': p.usage_amount,
                                'earned_rewards': p.earned_rewards,
                                'is_eligible_to_earn_rewards': str(p.is_eligible_to_earn_rewards)
                            }
                            reward['products'].append(prd)

                    print_header("Reward Monthly Summary for " + reward['time_usage_started'] + " - " + reward['time_usage_ended'], 3)
                    print("")
                    print(f"time_rewards_earned     : {reward['time_rewards_earned']}")
                    print(f"time_rewards_expired    : {reward['time_rewards_expired']}")
                    print(f"usage_period_key        : {reward['usage_period_key']}")
                    print(f"is_manual               : {reward['is_manual']}")
                    print(f"usage_amount            : {number_format(reward['usage_amount'])}")
                    print(f"eligible_usage_amount   : {number_format(reward['eligible_usage_amount'])}")
                    print(f"ineligible_usage_amount : {number_format(reward['ineligible_usage_amount'])}")
                    print(f"available_rewards       : {number_format(reward['available_rewards'])}")
                    print(f"redeemed_rewards        : {number_format(reward['redeemed_rewards'])}")
                    print(f"earned_rewards          : {number_format(reward['earned_rewards'])}")

                    if reward['products']:
                        print(f"products_extracted      : {number_format(len(reward['products']))}")

                    sub_info['rewards'].append(reward)

                #######################
                # Details Summary
                #######################
                status = "rewards.summary"
                # oci.usage.models.RewardDetails
                ss = rewards.summary

                reward_summary = {
                    'tenancy_id': str(ss.tenancy_id),
                    'subscription_id': str(ss.subscription_id),
                    'currency': str(ss.currency),
                    'redemption_code': str(ss.redemption_code),
                    'rewards_rate': ss.rewards_rate,
                    'total_rewards_available': ss.total_rewards_available
                }

                print_header("Reward Summary", 3)
                print("")
                print(f"tenancy_id              : {reward_summary['tenancy_id']}")
                print(f"subscription_id         : {reward_summary['subscription_id']}")
                print(f"currency                : {reward_summary['currency']}")
                print(f"redemption_code         : {reward_summary['redemption_code']}")
                print(f"rewards_rate            : {number_format(reward_summary['rewards_rate'])}")
                print(f"total_rewards_available : {number_format(reward_summary['total_rewards_available'])}")

                sub_info['rewards_summary'] = reward_summary

                # add to data
                data['subscriptions'].append(sub_info)

            else:
                print("")
                print("No Support Rewards...")

        # return the data
        return data

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'rewards_report' - " + status + " - " + str(e))
        return data

    except Exception as e:
        print("\nException Error at 'rewards_report' - " + status + " - " + str(e))
        return data


##########################################################################
# Main Process
##########################################################################
def main():

    # Get Command Line Parser
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS, formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=130))
    parser.add_argument('-c', default="", dest='config_file', help='OCI CLI Config file')
    parser.add_argument('-t', default="", dest='config_profile', help='Config Profile inside the config file')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
    parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
    parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
    parser.add_argument('-include_products', action='store_true', default=False, dest='include_products', help='Include products per rewards for JSON file only')
    parser.add_argument('-f', type=argparse.FileType('w'), dest='file', help="Output to file (as json)")
    parser.add_argument('-csv', action='store_true', default=False, dest='csv', help='Write to CSV files - rewards.csv, redemption.csv, reward_products.csv if -include_products specificed')

    cmd = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    # Start print time info
    print_header("Running Show Rewards", 0)

    print("Author          : Adi Zohar")
    print("Disclaimer      : This is not an official Oracle application, It does not supported by Oracle !")
    print("Machine         : " + platform.node() + " (" + platform.machine() + ")")
    print("App Version     : " + version)
    print("OCI SDK Version : " + oci.version.__version__)
    print("Python Version  : " + platform.python_version())
    if cmd.is_instance_principals:
        print("Authentication  : Instance Principals")
    elif cmd.is_delegation_token:
        print("Authentication  : Instance Principals With Delegation Token")
    else:
        print("Authentication  : Config File")
    print("Date/Time       : " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("Command Line    : " + ' '.join(x for x in sys.argv[1:]))
    if cmd.file:
        print("Writing to file..." + cmd.file.name)

    ############################################
    # create signer
    ############################################
    config, signer = create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)

    print_header("Fetching data", 0)
    tenancy = None
    try:
        print("\nConnecting to Identity Service...\n")
        identity = oci.identity.IdentityClient(config, signer=signer)
        if cmd.proxy:
            identity.base_client.session.proxies = {'https': cmd.proxy}

        tenancy = identity.get_tenancy(config["tenancy"]).data
        regions = identity.list_region_subscriptions(tenancy.id).data

        # Set home region for connection
        for reg in regions:
            if reg.is_home_region:
                tenancy_home_region = str(reg.region_name)

        config['region'] = tenancy_home_region
        signer.region = tenancy_home_region

        print("Tenant Name  : " + str(tenancy.name))
        print("Tenant Id    : " + tenancy.id)
        print("Home Region  : " + tenancy_home_region)

    except Exception as e:
        raise RuntimeError("\nError fetching tenant information - " + str(e))

    ############################################
    # Main
    ############################################
    try:
        data = rewards_report(cmd, config, signer, tenancy)

        # If write to json file
        if cmd.file and data:
            with open(cmd.file.name, 'w') as outfile:
                json.dump(data, outfile, indent=4, sort_keys=False)
            print("")
            print("Exported to file " + cmd.file.name)

        # If write to csv file
        if cmd.csv and data:
            rewards_csv(data)

    except Exception as e:
        raise RuntimeError("\nError at main function - " + str(e))


##########################################################################
# Main Process
##########################################################################
main()
