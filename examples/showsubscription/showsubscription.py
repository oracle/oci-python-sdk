# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

####################################################################################################################
# showsubscription.py
#
# @author: Adi Zohar, Mar 01 2024, Updated Aug 12 2024.
#
# Supports Python 3
####################################################################################################################
# Application Command line parameters
#
#   -c config     - OCI CLI Config
#   -t profile    - profile inside the config file
#   -p proxy      - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip           - Use Instance Principals for Authentication
#   -dt           - Use Instance Principals with delegation token for cloud shell
#   -all_services - Show all services (default Universal Credit only)
#   -all_statuses - Show all Statuses (default ACTIVE only)
#   -f FILE_NAME  - Write to JSON file
#
####################################################################################################################
# Modules Included:
# - oci.onesubscription.OrganizationSubscriptionClient
# - oci.onesubscription.CommitmentClient
# - oci.onesubscription.SubscribedServiceClient
#
# APIs Used:
# - IdentityClient.get_tenancy                                     - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions                       - Policy TENANCY_INSPECT
# - OrganizationSubscriptionClient.list_organization_subscriptions - Policy ORGANIZATIONS_SUBSCRIPTION_INSPECT
# - SubscribedServiceClient.list_subscribed_services               - Policy SUBSCRIBED_SERVICE_INSPECT
# - CommitmentClient.list_commitments                              - Policy SUBSCRIBED_SERVICE_INSPECT
#
# Policies:
#   Allow group ShowSubscriptionGroup to inspect tenancies in tenancy
#   Allow group ShowSubscriptionGroup to inspect subscribed-services in tenancy
#   Allow group ShowSubscriptionGroup to inspect organizations-subscription in tenancy
####################################################################################################################
import sys
import argparse
import datetime
import oci
import os
import platform
import json

version = "2024.08.12"


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
# Subscription Report
##########################################################################
def subscription_report(cmd, config, signer, tenancy):

    data = {
        'tenant_id': tenancy.id,
        'tenant_name': tenancy.name,
        'subscriptions': []
    }

    try:
        osub_org_client = oci.onesubscription.OrganizationSubscriptionClient(config, signer=signer)
        one_sub_client = oci.onesubscription.SubscribedServiceClient(config, signer=signer)
        osub_commit_client = oci.onesubscription.CommitmentClient(config, signer=signer)

        if cmd.proxy:
            osub_org_client.base_client.session.proxies = {'https': cmd.proxy}
            one_sub_client.base_client.session.proxies = {'https': cmd.proxy}
            osub_commit_client.base_client.session.proxies = {'https': cmd.proxy}

        ############################
        # Get Subscription list
        ############################
        subscription_list = osub_org_client.list_organization_subscriptions(tenancy.id)
        ucc_sub = [x for x in subscription_list.data if cmd.all_services or 'Universal' in x.service_name]

        for sub in ucc_sub:

            sub_info = {
                'id': sub.id,
                'service_name': str(sub.service_name),
                'currency': sub.currency.iso_code if sub.currency else "",
                'time_start': str(sub.time_start)[0:16],
                'time_end': str(sub.time_end)[0:16],
                'status': str(sub.status),
                'total_value': str(sub.total_value),
                'services': []
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
            # Get Subscribed Service
            ############################
            subscribed_services = one_sub_client.list_subscribed_services(tenancy.id, sub.id).data
            for ss in subscribed_services:
                if not cmd.all_statuses and ss.status != 'ACTIVE':
                    continue

                small_sub = {
                    'status': ss.status,
                    'subscription_id': ss.subscription_id,
                    'id': ss.id,
                    'time_start': str(ss.time_start)[0:16],
                    'time_end': str(ss.time_end)[0:16],
                    'term_value': str(ss.term_value),
                    'admin_email': ss.admin_email,
                    'buyer_email': ss.buyer_email,
                    'agreement_id': ss.agreement_id,
                    'agreement_name': ss.agreement_name,
                    'time_agreement_end': str(ss.time_agreement_end)[0:16],
                    'bill_to_customer': ss.bill_to_customer.name if ss.bill_to_customer else "",
                    'end_user_customer': ss.end_user_customer.name if ss.end_user_customer else "",
                    'service_to_customer': ss.service_to_customer.name if ss.service_to_customer else "",
                    'billing_frequency': ss.billing_frequency,
                    'csi': ss.csi,
                    'operation_type': ss.operation_type,
                    'order_type': ss.order_type,
                    'order_number': ss.order_number,
                    'payment_method': ss.payment_method,
                    'payment_number': ss.payment_number,
                    'pricing_model': ss.pricing_model,
                    'product_number': ss.product.part_number if ss.product else "",
                    'product_name': ss.product.name if ss.product else "",
                    'is_payg': str(ss.is_payg) if ss.is_payg else "",
                    'is_having_usage': str(ss.is_having_usage),
                    'is_variable_commitment': str(ss.is_variable_commitment),
                    'original_promo_amount': "" if str(ss.original_promo_amount) == "null" else ss.original_promo_amount,
                    'funded_allocation_value': "" if str(ss.funded_allocation_value) == "null" else ss.funded_allocation_value,
                    'line_net_amount': ss.line_net_amount,
                    'total_value': ss.total_value,
                    'used_amount': ss.used_amount,
                    'available_amount': ss.available_amount,
                    'commits': []
                }

                print_header(small_sub['product_number'] + " - " + small_sub['product_name'], 3)
                print("")
                print(f"status                  : {small_sub['status']}")
                print(f"subscription_id         : {small_sub['subscription_id']}")
                print(f"id                      : {small_sub['id']}")
                print(f"time_start              : {small_sub['time_start']}")
                print(f"time_end                : {small_sub['time_end']}")
                print(f"term_value              : {small_sub['term_value']}")
                print(f"admin_email             : {small_sub['admin_email']}")
                print(f"buyer_email             : {small_sub['buyer_email']}")
                print(f"agreement_id            : {small_sub['agreement_id']}")
                print(f"agreement_name          : {small_sub['agreement_name']}")
                print(f"time_agreement_end      : {small_sub['time_agreement_end']}")
                print(f"bill_to_customer        : {small_sub['bill_to_customer']}")
                print(f"end_user_customer       : {small_sub['end_user_customer']}")
                print(f"service_to_customer     : {small_sub['service_to_customer']}")
                print(f"billing_frequency       : {small_sub['billing_frequency']}")
                print(f"csi                     : {small_sub['csi']}")
                print(f"operation_type          : {small_sub['operation_type']}")
                print(f"order_type              : {small_sub['order_type']}")
                print(f"order_number            : {small_sub['order_number']}")
                print(f"payment_method          : {small_sub['payment_method']}")
                print(f"payment_number          : {small_sub['payment_number']}")
                print(f"pricing_model           : {small_sub['pricing_model']}")
                print(f"product_number          : {small_sub['product_number']}")
                print(f"product_name            : {small_sub['product_name']}")
                print(f"is_payg                 : {small_sub['is_payg']}")
                print(f"is_having_usage         : {small_sub['is_having_usage']}")
                print(f"is_variable_commitment  : {small_sub['is_variable_commitment']}")
                print(f"original_promo_amount   : {small_sub['original_promo_amount']}")
                print(f"funded_allocation_value : {small_sub['funded_allocation_value']}")
                print(f"line_net_amount         : {number_format(small_sub['line_net_amount'])}")
                print(f"total_value             : {number_format(small_sub['total_value'])}")
                print(f"used_amount             : {number_format(small_sub['used_amount'])}")
                print(f"available_amount        : {number_format(small_sub['available_amount'])}")

                # Add the commits
                try:
                    commits = osub_commit_client.list_commitments(ss.id, compartment_id=tenancy.id).data
                    for commit in commits:
                        carr = {
                            'funded_allocation_value': "" if commit.funded_allocation_value == "null" else commit.funded_allocation_value,
                            'time_start': str(commit.time_start)[0:16],
                            'time_end': str(commit.time_end)[0:16],
                            'quantity': str(commit.quantity),
                            'used_amount': str(commit.used_amount),
                            'available_amount': str(commit.available_amount)
                        }
                        small_sub['commits'].append(carr)

                        print(
                            f"--> Commit              : {carr['time_start'][0:10]} - {carr['time_end'][0:10]}, "
                            f"Total: {number_format(carr['quantity'])}  "
                            f"Used: {number_format(carr['used_amount'])}  "
                            f"Available: {number_format(carr['available_amount'])}  "
                            f"Funded: {number_format(carr['funded_allocation_value'])}")

                except oci.exceptions.ServiceError as e:
                    small_sub['commits_error'] = e.code

                sub_info['services'].append(small_sub)

            # add to data
            data['subscriptions'].append(sub_info)

        # return the data
        return data

    except oci.exceptions.ServiceError as e:
        print("\nService Error at 'subscription_report' - " + str(e))
        return data

    except Exception as e:
        print("\nException Error at 'subscription_report' - " + str(e))
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
    parser.add_argument('-all_services', action='store_true', default=False, dest='all_services', help='All Services (Default Universal Credit)')
    parser.add_argument('-all_statuses', action='store_true', default=False, dest='all_statuses', help='All Subscription Statuses (Default ACTIVE)')
    parser.add_argument('-f', type=argparse.FileType('w'), dest='file', help="Output to file (as json)")
    cmd = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return

    # Start print time info
    print_header("Running Show Subscription", 0)

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
    print("Service Filter  : " + ("ALL" if cmd.all_services else "UCC"))
    print("Status  Filter  : " + ("ALL" if cmd.all_statuses else "ACTIVE"))
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
    # Connection to UsageAPI
    ############################################
    try:
        data = subscription_report(cmd, config, signer, tenancy)

        # If print to json file
        if cmd.file and data:
            with open(cmd.file.name, 'w') as outfile:
                json.dump(data, outfile, indent=4, sort_keys=False)
            print("")
            print("Exported to file " + cmd.file.name)

    except Exception as e:
        raise RuntimeError("\nError at main function - " + str(e))


##########################################################################
# Main Process
##########################################################################
main()
