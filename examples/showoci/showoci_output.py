##########################################################################
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# showoci_output.py
#
# @author: Adi Zohar
# @contributors: Olaf Heimburger
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
# ShowOCIOutput class, ShowOCISummary class
# accept data as JSON format and print nice output
#
# ShowOCICSV class - accept data as JSON and write CSV output files.
##########################################################################
from __future__ import print_function
import csv
import sys


class ShowOCIOutput(object):
    version = "25.08.26"

    ##########################################################################
    # spaces for align
    ##########################################################################
    tabs = ' ' * 4
    taba = '--> '
    tabs2 = tabs + tabs
    error = 0

    ############################################
    # Init
    ############################################
    def __init__(self):
        pass

    ##########################################################################
    # Print header centered
    ##########################################################################
    def print_header(self, name, category, topBorder=True, bottomBorder=True, printText=True):
        options = {0: 95, 1: 60, 2: 40, 3: 85}
        chars = int(options[category])
        if topBorder:
            print("")
            print('#' * chars)
        if printText:
            print("#" + name.center(chars - 2, " ") + "#")
        if bottomBorder:
            print('#' * chars)

    ##########################################################################
    # list_to_str
    ##########################################################################
    def list_to_str(self, v_list, attr=None):
        try:
            if not v_list or not isinstance(v_list, (list, tuple)):
                return ''

            if attr:
                return str(', '.join(x[attr] for x in v_list))
            else:
                return str(', '.join(x for x in v_list))

        except Exception as e:
            self.__print_error("list_to_str" + (" ATTR='" + attr + "'" if attr else ""), e)

    ##########################################################################
    # print_oci_main
    ##########################################################################

    def print_data(self, data, print_version=False):
        try:
            has_data = False
            for d in data:
                if 'type' in d:
                    if d['type'] == "showoci":
                        if print_version:
                            self.print_showoci_config(d['data'])

                    elif d['type'] == "identity":
                        self.__print_identity_main(d['data'])
                        has_data = True

                    elif d['type'] == "budgets":
                        self.__print_budgets_main(d['data'])
                        has_data = True

                    elif d['type'] == "announcement":
                        self.__print_announcement_main(d['data'])
                        has_data = True

                    elif d['type'] == "security_scores":
                        self.__print_security_scores_main(d['data'])
                        has_data = True

                    elif d['type'] == "region":

                        # Check if limits exist
                        limits_exist = False
                        if 'limits' in d:
                            if d['limits']:
                                limits_exist = True

                        if d['data'] or limits_exist:
                            self.print_header(d['region'], 0)
                            has_data = True

                        self.__print_region_data(d['region'], d['data'])
                        if limits_exist:
                            self.__print_limits_main(d['limits'])

                    elif d['type'] == "errors":
                        self.__print_errors(d['data'])
                        has_data = True

                    else:
                        print("Error Unknown Type in JSON file...")

            # if no data - print message
            if not has_data:
                print("")
                print("*** Data not found, please check your execution flags ***")

        except Exception as e:
            raise Exception("Error in self.__print_main: " + str(e.args))

    ##########################################################################
    # Print showoci data
    ##########################################################################
    def print_showoci_config(self, data):
        try:
            self.print_header(data['program'], 1)
            print("Author          : " + data['author'])
            print("Contributors    : " + data['contributors'])
            print("Disclaimer      : " + data['disclaimer1'])
            print("                : " + data['disclaimer2'])
            print("Machine         : " + data['machine'])
            print("Python Version  : " + data['python'])
            if data['use_instance_principals']:
                print("Authentication  : Instance Principals")
            elif data['use_delegation_token']:
                print("Authentication  : Instance Principals with Delegation Token")
                print("Config File     : " + data['config_file'])
                print("Config Profile  : " + data['config_profile'])
            elif data['use_security_token']:
                print("Authentication  : Config File with Security Token")
                print("Config File     : " + data['config_file'])
                print("Config Profile  : " + data['config_profile'])
            else:
                print("Authentication  : Config File")
                print("Config File     : " + data['config_file'])
                print("Config Profile  : " + data['config_profile'])
            print("Date/Time       : " + data['datetime'])
            print("API Conn Timeout: " + str(data['connection_timeout']))
            print("API Read Timeout: " + str(data['read_timeout']))
            print("Command Line    : " + data['cmdline'])
            print("Showoci Version : " + data['version'])
            print("OCI SDK Version : " + data['oci_sdk_version'])
            if 'proxy' in data:
                print("Proxy           : " + data['proxy'])
            if 'override_tenant_id' in data:
                if data['override_tenant_id']:
                    print("Override id     : " + data['override_tenant_id'])
            if 'joutfile' in data:
                print("JSON Out        : " + data['joutfile'])
            if 'threads' in data:
                print("Running Threads : " + str(data['threads']))

            print("")

        except Exception as e:
            raise Exception("Error in print_showoci_config: " + str(e.args))

    ##########################################################################
    # get errors
    ##########################################################################
    def get_errors(self):
        return self.error

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, msg, e):
        classname = type(self).__name__
        caller_function = sys._getframe(2).f_code.co_name + ":" + sys._getframe(1).f_code.co_name

        if isinstance(e, KeyError):
            print("\nError in " + classname + ":" + caller_function + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + caller_function + ":" + msg + ": " + str(e))

        self.error += 1

    ##########################################################################
    # Print Tenancy
    ##########################################################################
    def __print_identity_tenancy(self, tenancy):
        try:

            self.print_header("Tenancy", 0)
            print("Name        : " + tenancy['name'])
            print("Tenant Id   : " + tenancy['id'])
            print("Home Region : " + tenancy['home_region_key'])
            print("Subs Region : " + tenancy['subscribe_regions'])
            print("")

        except Exception as e:
            self.__print_error("__print_identity_tenancy", e)

    ##########################################################################
    # Print Identity Users
    ##########################################################################

    def __print_identity_users(self, users):
        try:
            self.print_header("Users", 2)

            for user in users:
                last_login = "" if user['last_successful_login_time'] == "None" else ", Last Login = " + user['last_successful_login_time'][0:10]
                mfa_enabled = "" if user['is_mfa_activated'] == "False" else ", MFA Enabled"
                print(self.taba + user['name'] + mfa_enabled + last_login)
                print(self.tabs + "Groups     : " + user['groups'])

                if 'api_keys' in user:
                    for arr in user['api_keys']:
                        print(self.tabs + "API Keys   : " + arr['id'][-47:] + " (" + arr['lifecycle_state'] + ")")

                if 'auth_token' in user:
                    for arr in user['auth_token']:
                        print(self.tabs + "Auth Token : " + arr['description'] + " (" + arr['lifecycle_state'] + ")")

                if 'secret_keys' in user:
                    for arr in user['secret_keys']:
                        print(self.tabs + "Secret Key : " + arr['display_name'] + " (" + arr['lifecycle_state'] + ")")

                if 'smtp_creds' in user:
                    for arr in user['smtp_creds']:
                        print(self.tabs + "Secret Key : " + arr['description'] + " (" + arr['lifecycle_state'] + ")")

                print("")

        except Exception as e:
            self.__print_error("__print_identity_users", e)

    ##########################################################################
    # Print Identity Domains
    ##########################################################################

    def __print_identity_domains(self, domains):
        try:
            if not domains:
                return

            self.print_header("Identity Domains", 2)

            for domain in domains:
                print(self.taba + domain['display_name'] + " - " + domain['description'] + " - Created: " + domain['time_created'])
                print(self.tabs + "Compartment : " + domain['compartment_path'])
                print(self.tabs + "URL         : " + domain['url'])
                print(self.tabs + "License     : " + domain['license_type'])
                print(self.tabs + "Type        : " + domain['type'])
                print("")

            for domain in domains:
                if 'users' in domain and domain['users']:
                    self.__print_identity_domains_users(domain['display_name'], domain['users'])
                if 'groups' in domain and domain['groups']:
                    self.__print_identity_domains_groups(domain['display_name'], domain['groups'])
                if 'dynamic_groups' in domain and domain['dynamic_groups']:
                    self.__print_identity_domains_dynamic_groups(domain['display_name'], domain['dynamic_groups'])
                if 'network_perimeters' in domain and domain['network_perimeters']:
                    self.__print_identity_domains_network_perimeters(domain['display_name'], domain['network_perimeters'])
                if 'identity_providers' in domain and domain['identity_providers']:
                    self.__print_identity_domains_idps(domain['display_name'], domain['identity_providers'])
                if 'policies' in domain and domain['policies']:
                    self.__print_identity_domains_policies(domain['display_name'], domain['policies'])

        except Exception as e:
            self.__print_error("__print_identity_domains", e)

    ##########################################################################
    # Print Identity Domains Users
    ##########################################################################
    def __print_identity_domains_users(self, domain_name, users):
        try:
            header = domain_name + ":Users"
            self.print_header(header, 2)

            # Calculate ljust for printout aligned
            ljust_value = 0
            for user in users:
                val = len(user['user_name'] + user['family_name'] + user['given_name']) + 2
                ljust_value = val if val > ljust_value else ljust_value
            ljust_value = 50 if ljust_value > 50 else ljust_value

            for user in users:
                username = user['user_name']
                family_name = user['family_name'] if user['family_name'] != username else ""
                given_name = user['given_name'] if user['given_name'] != username else ""
                family_given_name = (" (" + family_name + " " + given_name + ")") if family_name or given_name else ""

                last_login = ", Last Login = " + user['ext_user_state']['last_successful_login_date'] if user['ext_user_state']['last_successful_login_date'] else ", Last Login = None            "
                mfa_enabled = "" if user['ext_mfa']['mfa_enabled_on'] == "False" else ", MFA Enabled"

                groups = (", Groups: " + ', '.join(x['display'] for x in user['groups'])) if user['groups'] else ""
                api_keys = ", API: " + str(len(user['api_keys'])) if user['api_keys'] else ""
                roles = ", Roles: " + str(len(user['roles'])) if user['roles'] else ""
                customer_secret_keys = ", Secrets: " + str(len(user['customer_secret_keys'])) if user['customer_secret_keys'] else ""
                auth_tokens = ", AuthToken: " + str(len(user['auth_tokens'])) if user['auth_tokens'] else ""
                smtp_credentials = ", SMTP: " + str(len(user['smtp_credentials'])) if user['smtp_credentials'] else ""
                o_auth2_client_credentials = ", OAuth: " + str(len(user['o_auth2_client_credentials'])) if user['o_auth2_client_credentials'] else ""
                db_credentials = ", DBCred: " + str(len(user['db_credentials'])) if user['db_credentials'] else ""

                print(self.taba + (username + family_given_name).ljust(ljust_value) + last_login + mfa_enabled + api_keys + roles + customer_secret_keys + auth_tokens + smtp_credentials + o_auth2_client_credentials + db_credentials + groups)

        except Exception as e:
            self.__print_error("__print_identity_domains_users", e)

    ##########################################################################
    # Print Identity Domains groups
    ##########################################################################
    def __print_identity_domains_groups(self, domain_name, groups):
        try:
            header = domain_name + ":Groups"
            self.print_header(header, 2)

            for val in groups:
                print(self.taba + val['display_name'] + " (" + val['ext_group']['description'] + ")")
                if val['members']:
                    print(self.tabs + "Users    : " + ', '.join(x['name'] for x in val['members']))

        except Exception as e:
            self.__print_error("__print_identity_domains_groups", e)

    ##########################################################################
    # Print Identity Domains dynamic groups
    ##########################################################################
    def __print_identity_domains_dynamic_groups(self, domain_name, groups):
        try:
            header = domain_name + ":Dynamic Groups"
            self.print_header(header, 2)

            for val in groups:
                print(self.taba + val['display_name'] + " (" + val['description'] + ")")
                print(self.tabs + "Rule    : " + val['matching_rule'])
                print("")

        except Exception as e:
            self.__print_error("__print_identity_domains_dynamic_groups", e)

    ##########################################################################
    # Print Identity Domains network perimeters
    ##########################################################################
    def __print_identity_domains_network_perimeters(self, domain_name, nets):
        try:
            header = domain_name + ":Network Perimeters"
            self.print_header(header, 2)

            for val in nets:
                print(self.taba + val['name'] + " (" + val['description'] + ")")
                for ip in val['ip_addresses']:
                    print(self.tabs + "Address: " + ip['value'] + ", " + ip['type'] + ", " + ip['version'])
                print("")

        except Exception as e:
            self.__print_error("__print_identity_domains_network_perimeters", e)

    ##########################################################################
    # Print Identity Domains IDPs
    ##########################################################################
    def __print_identity_domains_idps(self, domain_name, idps):
        try:
            header = domain_name + ":Identity Providers"
            self.print_header(header, 2)

            for val in idps:
                if val['enabled'] == "True":
                    print(self.taba + val['partner_name'] + ", Type: " + val['type'] + ", Desc: " + val['description'])
                    for ig in val['jit_user_prov_group_mappings']:
                        print(self.tabs + "Group Map : " + ig['value'] + " - " + ig['idp_group'] + " - " + ig['ref'])

        except Exception as e:
            self.__print_error("__print_identity_domains_idps", e)

    ##########################################################################
    # Print Identity Domains Policies
    ##########################################################################
    def __print_identity_domains_policies(self, domain_name, policies):
        try:
            header = domain_name + ":Policies"
            self.print_header(header, 2)

            for val in policies:
                print(self.taba + val['id'])
                print(self.tabs + "Name: " + val['name'])
                if val['policy_type']['value']:
                    print(self.tabs + "Type: " + val['policy_type']['value'])
                if val['description']:
                    print(self.tabs + "Desc: " + val['description'])
                for rl in val['rules']:
                    print(self.tabs + "Rule: " + rl['name'] + " - " + rl['value'])
                    print(self.tabs + "      Position  : " + rl['position'])
                    for rt in rl['rule_return']:
                        print(self.tabs + "      Rule Ret  : " + rt['name'] + " - " + rt['value'])
                    if rl['condition_group']:
                        cn = rl['condition_group']
                        if 'name' in cn and 'description' in cn:
                            print(self.tabs + "      Condition : " + cn['name'] + " - " + cn['description'])
                        if 'attribute_name' in cn and 'operator' in cn and 'attribute_value' in cn:
                            if cn['attribute_name'] or cn['operator'] or cn['attribute_value']:
                                print(self.tabs + "      Attribute : " + cn['attribute_name'] + " - " + cn['operator'] + " - " + cn['attribute_value'])
                print("")

        except Exception as e:
            self.__print_error("__print_identity_domains_policies", e)

    ##########################################################################
    # Print Identity Groups
    ##########################################################################

    def __print_identity_groups(self, groups):
        try:
            self.print_header("Groups", 2)

            for group in groups:
                print(self.taba + group['name'].ljust(18, " ") + " : " + group['users'])

        except Exception as e:
            self.__print_error("__print_identity_groups", e)

    ##########################################################################
    # Print Identity Policies
    ##########################################################################
    def __print_identity_policies(self, policies_data):
        try:
            if not policies_data:
                return

            self.print_header("Policies", 2)

            for c in policies_data:
                policies = c['policies']
                if not policies:
                    continue

                print("\nCompartment " + c['compartment_path'] + ":")
                for policy in policies:
                    print("")
                    print(self.taba + policy['name'] + ":")
                    print(self.tabs + "\n    ".join(policy['statements']))

        except Exception as e:
            self.__print_error("__print_identity_policies", e)

    ##########################################################################
    # Print Tag Namespace
    ##########################################################################
    def __print_identity_tag_namespace(self, tag_data):
        try:
            if not tag_data:
                return

            self.print_header("Tag Namespace", 2)

            for c in tag_data:
                tags = c['tags']
                if not tags:
                    continue

                print("\nCompartment " + c['compartment_path'] + ":")
                for tag in tags:
                    retired = " Retired " if tag['is_retired'] == "True" else ""
                    print(self.taba + tag['name'] + retired + " (" + tag['lifecycle_state'] + "), " + tag['description'])

        except Exception as e:
            self.__print_error("__print_identity_tag_namespace", e)

    ##########################################################################
    # Print Identity Providers
    ##########################################################################
    def __print_identity_providers(self, identity_providers, providers_mapping):

        try:

            if not identity_providers:
                return

            self.print_header("identity providers", 2)

            for ip in identity_providers:
                print(self.taba + ip['name'])
                print(self.tabs + "Desc      : " + ip['description'])
                print(self.tabs + "Type      : " + ip['product_type'])
                print(self.tabs + "Protocol  : " + ip['protocol'])
                print(self.tabs + "Redirect  : " + ip['redirect_url'])
                print(self.tabs + "Metadata  : " + ip['metadata_url'])

                for map in providers_mapping:
                    if map['provider_id'] == ip['id'] and map['oci_group_name']:
                        print(self.tabs + "Group Map : " + map['provider_group_name'] + " <-> " + map['oci_group_name'])
                print("")
            print("")

        except Exception as e:
            self.__print_error("__print_identity_providers", e)

    ##########################################################################
    # Print Dynamic Groups
    ##########################################################################

    def __print_identity_dynamic_groups(self, dynamic_groups):
        try:
            if not dynamic_groups:
                return
            self.print_header("Dynamic Groups", 2)

            for dg in dynamic_groups:
                print(self.taba + dg['name'])
                print(self.tabs + "Desc      :" + dg['description'])
                print(self.tabs + "Rules     :" + dg['matching_rule'])
            print("")

        except Exception as e:
            self.__print_error("__print_identity_dynamic_groups", e)

    ##########################################################################
    # Print network sources
    ##########################################################################

    def __print_network_sources(self, network_sources):
        try:
            if not network_sources:
                return
            self.print_header("Network Sources", 2)

            for ns in network_sources:
                print(self.taba + ns['name'])
                print(self.tabs + "Desc      : " + ns['description'])
                print(self.tabs + "Services  : " + ", ".join(ns['services']))
                print(self.tabs + "Public IPs: " + ", ".join(ns['public_source_list']))
                print(self.tabs + "VCN IPs   : " + ", ".join(x['ip_ranges'] for x in ns['virtual_source_list']))

            print("")

        except Exception as e:
            self.__print_error("__print_network_sources", e)

    ##########################################################################
    # Print Cost Tracking Tags
    ##########################################################################
    def __print_identity_cost_tracking_tags(self, tags):
        try:
            if not tags:
                return
            self.print_header("Cost Tracking Tags", 2)

            for tag in tags:
                print(self.taba + tag['tag_namespace_name'] + "." + tag['name'])
                print(self.tabs + "Desc      :" + tag['description'])
                print(self.tabs + "Created   :" + tag['time_created'][0:16])
                print("")

        except Exception as e:
            self.__print_error("__print_identity_cost_tracking_tags", e)

    ##########################################################################
    # Identity Module
    ##########################################################################

    def __print_identity_main(self, data):
        try:

            if 'tenancy' in data:
                self.__print_identity_tenancy(data['tenancy'])
            if 'users' in data:
                self.__print_identity_users(data['users'])
            if 'groups' in data:
                self.__print_identity_groups(data['groups'])
            if 'dynamic_groups' in data:
                self.__print_identity_dynamic_groups(data['dynamic_groups'])
            if 'network_sources' in data:
                self.__print_network_sources(data['network_sources'])
            if 'policies' in data:
                self.__print_identity_policies(data['policies'])
            if 'cost_tracking_tags' in data:
                self.__print_identity_cost_tracking_tags(data['cost_tracking_tags'])
            if 'tag_namespace' in data:
                self.__print_identity_tag_namespace(data['tag_namespace'])
            if 'domains' in data:
                self.__print_identity_domains(data['domains'])

            provider_mapping = data['providers_mapping'] if 'providers_mapping' in data else ""
            if 'providers' in data:
                self.__print_identity_providers(data['providers'], provider_mapping)

        except Exception as e:
            self.__print_error("__print_identity_data", e)

    ##########################################################################
    # return compartment name
    ##########################################################################

    def __print_core_network_vcn_compartment(self, vcn_compartment, data_compartment):
        if vcn_compartment == data_compartment:
            return ""
        val = "  (Compartment=" + data_compartment + ")"
        return val

    ##########################################################################
    # Print Network VCN subnets
    ##########################################################################

    def __print_core_network_vcn_subnet(self, subnets, vcn_compartment):
        try:
            for subnet in subnets:
                print("")
                print(self.tabs + "Subnet " + subnet['subnet'] + self.__print_core_network_vcn_compartment(vcn_compartment, subnet['compartment_name']))
                print(self.tabs + self.tabs + "Name    : " + subnet['name'])
                print(self.tabs + self.tabs + "DNS     : " + subnet['dns'])
                print(self.tabs + self.tabs + "DHCP    : " + subnet['dhcp_options'])
                print(self.tabs + self.tabs + "Route   : " + subnet['route'])
                print(self.tabs + self.tabs + "Prv IPs : " + str(len(subnet['private_ips'])) + " Private IPs Allocated")
                for s in subnet['security_list']:
                    print(self.tabs + self.tabs + "Sec List: " + s)

                # print logs
                if 'logs' in subnet:
                    for index, log in enumerate(subnet['logs'], start=1):
                        print(self.tabs + self.tabs + "Log " + str(index) + "   : " + log['name'] + " - " + log['source_service'])

        except Exception as e:
            self.__print_error("__print_core_network_vcn_subnet", e)

    ##########################################################################
    # Print Network VCN VLAN
    ##########################################################################

    def __print_core_network_vcn_vlan(self, vlans, vcn_compartment):
        try:
            for vlan in vlans:
                print("")
                print(self.tabs + "VLAN " + vlan['vlan'] + self.__print_core_network_vcn_compartment(vcn_compartment, vlan['compartment_name']))
                print(self.tabs + self.tabs + "Route   : " + vlan['route'])
                for s in vlan['nsg']:
                    print(self.tabs + self.tabs + "NSG     : " + s)

        except Exception as e:
            self.__print_error("__print_core_network_vcn_vlan", e)

    ##########################################################################
    # get DHCP options for DHCP_ID
    ##########################################################################

    def __print_core_network_vcn_dhcp_options(self, dhcp_options, vcn_compartment):
        try:
            for dhcp in dhcp_options:
                print("")
                print(self.tabs + "DHCP Options: " + dhcp['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, dhcp['compartment_name']))

                for opt in dhcp['opt']:
                    print(self.tabs + self.tabs + opt)

        except Exception as e:
            self.__print_error("__print_core_network_vcn_dhcp_options", e)

    ##########################################################################
    # Print Network vcn security list
    ##########################################################################

    def __print_core_network_vcn_security_lists(self, sec_lists, vcn_compartment):
        try:
            if not sec_lists:
                return
            for sl in sec_lists:
                print("")
                print(self.tabs + "Sec List    : " + str(sl['name']) + self.__print_core_network_vcn_compartment(vcn_compartment, sl['compartment_name']))
                if len(sl['sec_rules']) == 0:
                    print(self.tabs + "            : Empty.")

                for slr in sl['sec_rules']:
                    print(self.tabs + self.tabs + slr['desc'])

        except Exception as e:
            self.__print_error("__print_core_network_vcn_security_lists", e)

    ##########################################################################
    # Print Network vcn security groups
    ##########################################################################

    def __print_core_network_vcn_security_groups(self, sec_groups, vcn_compartment):
        try:
            if not sec_groups:
                return
            for sl in sec_groups:
                print("")
                print(self.tabs + "Sec Group   : " + str(sl['name']) + self.__print_core_network_vcn_compartment(vcn_compartment, sl['compartment_name']))
                if len(sl['sec_rules']) == 0:
                    print(self.tabs + "            : Empty or no Permission.")

                for slr in sl['sec_rules']:
                    print(self.tabs + self.tabs + slr['desc'])

        except Exception as e:
            self.__print_error("__print_core_network_vcn_security_groups", e)

    ##########################################################################
    # Print Network vcn Route Tables
    ##########################################################################

    def __print_core_network_vcn_route_tables(self, route_tables, vcn_compartment):
        try:
            if not route_tables:
                return

            for rt in route_tables:
                print("")
                print(self.tabs + "Route Table : " + rt['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, rt['compartment_name']))

                if 'route_rules' not in rt:
                    print(self.tabs + self.tabs + "Route   : Empty.")
                else:
                    if len(rt['route_rules']) == 0:
                        print(self.tabs + self.tabs + "Route   : Empty.")
                    else:
                        for rl in rt['route_rules']:
                            print(self.tabs + self.tabs + "Route   : " + str(rl['desc']))

        except Exception as e:
            self.__print_error("__print_core_network_vcn_route_tables", e)

    ##########################################################################
    # print network vcn
    ##########################################################################
    def __print_core_network_vcn(self, vcns):

        try:
            if len(vcns) == 0:
                return

            self.print_header("VCNs", 2)
            for vcn in vcns:
                print(self.taba + "VCN    " + vcn['name'])
                vcn_compartment = vcn['compartment_name']

                if 'igw' in vcn['data']:
                    for igwloop in vcn['data']['igw']:
                        print(self.tabs + "Internet GW : " + igwloop['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, igwloop['compartment_name']))

                if 'sgw' in vcn['data']:
                    for sgwloop in vcn['data']['sgw']:
                        print(self.tabs + "Service GW  : " + sgwloop['name'] + sgwloop['transit'] + " - " + sgwloop['services'] + self.__print_core_network_vcn_compartment(vcn_compartment, sgwloop['compartment_name']))

                if 'nat' in vcn['data']:
                    for natloop in vcn['data']['nat']:
                        print(self.tabs + "NAT GW      : " + natloop['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, natloop['compartment_name']))

                if 'drg_attached' in vcn['data']:
                    for drgloop in vcn['data']['drg_attached']:
                        print(self.tabs + "DRG Attached: " + drgloop['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, drgloop['compartment_name']))

                if 'local_peering' in vcn['data']:
                    for lpeer in vcn['data']['local_peering']:
                        print(self.tabs + "Local Peer  : " + lpeer['name'] + " ---> " + lpeer['peer_name'] + self.__print_core_network_vcn_compartment(vcn_compartment, lpeer['compartment_name']))

                if 'subnets' in vcn['data']:
                    self.__print_core_network_vcn_subnet(vcn['data']['subnets'], vcn_compartment)

                if 'vlans' in vcn['data']:
                    self.__print_core_network_vcn_vlan(vcn['data']['vlans'], vcn_compartment)

                if 'security_lists' in vcn['data']:
                    self.__print_core_network_vcn_security_lists(vcn['data']['security_lists'], vcn_compartment)

                if 'security_groups' in vcn['data']:
                    self.__print_core_network_vcn_security_groups(vcn['data']['security_groups'], vcn_compartment)

                if 'route_tables' in vcn['data']:
                    self.__print_core_network_vcn_route_tables(vcn['data']['route_tables'], vcn_compartment)

                if 'dhcp_options' in vcn['data']:
                    self.__print_core_network_vcn_dhcp_options(vcn['data']['dhcp_options'], vcn_compartment)

                if 'dns_resolvers' in vcn['data']:
                    self.__print_core_network_dns_resolver(vcn['data']['dns_resolvers'])

                print("")

        except BaseException as e:
            self.__print_error("__print_core_network_vcn", e)

    ##########################################################################
    # print network drg
    ##########################################################################
    def __print_core_network_drg(self, drgs):

        try:
            if len(drgs) == 0:
                return

            self.print_header("DRGs", 2)
            for drg in drgs:
                print(self.taba + "DRG   Name      : " + drg['name'] + ", Redundant: " + drg['redundancy'])

                for index, arr in enumerate(drg['ip_sec_connections'], start=1):
                    drg_route_table = ", DRG Route: " + arr['drg_route_table'] if arr['drg_route_table'] else ""
                    print(self.tabs + "      IPSEC " + str(index) + "   : " + arr['name'] + " (" + arr['tunnels_status'] + ")" + drg_route_table)
                    if 'logs' in arr:
                        for log in arr['logs']:
                            print(self.tabs + self.tabs + "Log : " + log['name'] + " - " + log['source_service'])

                for index, arr in enumerate(drg['virtual_circuits'], start=1):
                    drg_route_table = ", DRG Route: " + arr['drg_route_table'] if arr['drg_route_table'] else ""
                    print(self.tabs + "      VC " + str(index) + "      : " + arr['name'] + " (" + arr['bgp_session_state'] + ")" + drg_route_table)
                    if 'logs' in arr:
                        for log in arr['logs']:
                            print(self.tabs + self.tabs + "Log : " + log['name'] + " - " + log['source_service'])

                for index, arr in enumerate(drg['remote_peerings'], start=1):
                    drg_route_table = ", DRG Route: " + arr['drg_route_table'] if arr['drg_route_table'] else ""
                    print(self.tabs + "      RPC " + str(index) + "     : " + arr['name'] + " (" + arr['peering_status'] + ")" + drg_route_table)

                for index, arr in enumerate(drg['vcns'], start=1):
                    drg_route_table = ", DRG Route: " + arr['drg_route_table'] if arr['drg_route_table'] else ""
                    route_table = ", Route Table: " + arr['route_table'] if arr['route_table'] else ""
                    print(self.tabs + "      VCN " + str(index) + "     : " + arr['name'] + drg_route_table + route_table)

                for rt in drg['drg_route_tables']:
                    print("")
                    print(self.tabs + "      DRG Route : " + rt['display_name'] + ", is_ecmp_enabled: " + rt['is_ecmp_enabled'])
                    for index, arr in enumerate(rt['route_rules'], start=1):
                        print(self.tabs + "         Rule " + str(index) + " : " + arr['name'])
                print("")

        except Exception as e:
            self.__print_error("__print_core_network_drg", e)

    ##########################################################################
    # print network remote peering
    ##########################################################################
    def __print_core_network_remote_peering(self, rpcs):

        try:
            if len(rpcs) == 0:
                return

            self.print_header("Remote Peering", 2)
            for rpc in rpcs:
                print(self.taba + "RPC   Name   : " + rpc['name'])
                print(self.tabs + "      DRG    : " + rpc['drg'])

                # if peer has name if not id
                if rpc['peer_rfc_name']:
                    print(self.tabs + "      Peer   : " + rpc['peer_rfc_name'] + " - " + rpc['peer_region_name'])
                else:
                    print(self.tabs + "      PeerId : " + rpc['peer_id'])
                    print(self.tabs + "      Region : " + rpc['peer_region_name'])

                print(self.tabs + "      Status : " + rpc['peering_status'])
                if rpc['is_cross_tenancy_peering'] == "True":
                    print(self.tabs + "       Tenant: Cross Tenant: " + rpc['peer_tenancy_id'])

        except Exception as e:
            self.__print_error("__print_core_network_vcn", e)

    ##########################################################################
    # print network cpe
    ##########################################################################
    def __print_core_network_cpe(self, cpes):

        try:

            if len(cpes) == 0:
                return

            self.print_header("CPEs", 2)
            for cpe in cpes:
                print(self.taba + "CPE    " + cpe['name'])

        except Exception as e:
            self.__print_error("__print_core_network_cpe", e)

    ##########################################################################
    # print network firewall
    ##########################################################################
    def __print_core_network_firewall(self, nfws):

        try:

            if len(nfws) == 0:
                return

            self.print_header("Network Firewalls", 2)

            for arr in nfws:
                print(self.taba + arr['name'] + " - " + arr['availability_domain'] + " - " + arr['ipv4_address'] + " - " + arr['lifecycle_state'])
                print(self.tabs + "Subnet: " + arr['subnet_name'])
                print(self.tabs + "Policy: " + arr['network_firewall_policy_name'])

        except Exception as e:
            self.__print_error("__print_core_network_firewall", e)

    ##########################################################################
    # print network firewall policies
    ##########################################################################
    def __print_core_network_firewall_policies(self, nfws):

        try:

            if len(nfws) == 0:
                return

            self.print_header("Network Firewalls Policies", 2)

            for arr in nfws:
                print(self.taba + arr['display_name'] + " - " + arr['lifecycle_state'])

        except Exception as e:
            self.__print_error("__print_core_network_firewall_policies", e)

    ##########################################################################
    # print network dns resolvers
    ##########################################################################
    def __print_core_network_dns_resolver(self, resolvers):

        try:
            if len(resolvers) == 0:
                return

            for rs in resolvers:
                if not rs['endpoints']:
                    continue
                print("")
                print(self.tabs + "DNS Resolver : " + rs['display_name'] + (" ( Protected )" if rs['is_protected'] else ""))

                # get end points
                for t in rs['endpoints']:
                    print(self.tabs + self.tabs + "Endpoint : " + t['endpoint_type'] + " - " + t['name'] + ", " + ("Forwarding: " + t['forwarding_address'] if t['is_forwarding'] else "Listening: " + t['listening_address']))

                # get rules
                for t in rs['rules']:
                    print(self.tabs + self.tabs + "Rule     : " + t['action'] + ": " + t['source_endpoint_name'] +
                          (": Domains: " + t['qname_cover_conditions'] if t['qname_cover_conditions'] else "") +
                          (": IPs: " + t['client_address_conditions'] if t['client_address_conditions'] else "") +
                          ", Dest = " + t['destination_addresses'])

        except Exception as e:
            self.__print_error("__print_core_network_dns_resolver", e)

    ##########################################################################
    # print network ipsec
    ##########################################################################
    def __print_core_network_ipsec(self, ipsecs):

        try:
            if len(ipsecs) == 0:
                return

            self.print_header("IPSec", 2)
            for ips in ipsecs:

                print(self.taba + "IPSEC  : " + ips['name'])
                print(self.tabs + "DRG    : " + ips['drg'])
                print(self.tabs + "CPE    : " + ips['cpe'])
                # get tunnel status
                for t in ips['tunnels']:
                    print(self.tabs + "Tunnel : " + t['display_name'].ljust(12) + " - " + t['status'] + ", " + t['routing'] + ", VPN: " + t['vpn_ip'] + ", CPE: " + t['cpe_ip'] + ", " + t['status_date'])
                    if t['bgp_info']:
                        print(self.tabs + "       : " + t['bgp_info'])

                if ips['routes']:
                    print(self.tabs + "Routes : " + "\n    Static : ".join(ips['routes']))
                print("")

        except Exception as e:
            self.__print_error("__print_core_network_ipsec", e)

    ##########################################################################
    # print virtual circuits
    ##########################################################################
    def __print_core_network_virtual_circuit(self, virtual_circuit):

        try:
            if len(virtual_circuit) == 0:
                return

            self.print_header("Virtual Circuits (FC)", 2)
            for vc in virtual_circuit:

                print(self.taba + "VC      : " + vc['name'] + " - " + vc['bandwidth_shape_name'] + " - " + vc['lifecycle_state'])
                print(self.tabs + "DRG     : " + vc['drg'])
                print(self.tabs + "BGP     : " + vc['bgp_management'] + " - " + vc['bgp_session_state'] + " - Cust ASN:" + vc['customer_bgp_asn'] + " - Ora ASN:" + vc['oracle_bgp_asn'])
                print(self.tabs + "PROVIDER: " + vc['provider_name'] + " - " + vc['provider_service_name'] + " - " + vc['provider_state'] + " - " + vc['service_type'])
                # get tunnel status
                for t in vc['cross_connect_mappings']:
                    print(self.tabs + "CCMAP   : Cust : " + str(t['customer_bgp_peering_ip']) + " - Ora : " + str(t['oracle_bgp_peering_ip']) + " - VLAN " + str(t['vlan']))
                print("")

        except Exception as e:
            self.__print_error("__print_core_network_virtual_circuit", e)

    ##########################################################################
    # print network main
    ##########################################################################

    def __print_core_network_main(self, data):
        try:
            if 'vcn' in data:
                self.__print_core_network_vcn(data['vcn'])
            if 'drg' in data:
                self.__print_core_network_drg(data['drg'])
            if 'cpe' in data:
                self.__print_core_network_cpe(data['cpe'])
            if 'network_firewall' in data:
                self.__print_core_network_firewall(data['network_firewall'])
            if 'network_firewall_policies' in data:
                self.__print_core_network_firewall_policies(data['network_firewall_policies'])
            if 'ipsec' in data:
                self.__print_core_network_ipsec(data['ipsec'])
            if 'remote_peering' in data:
                self.__print_core_network_remote_peering(data['remote_peering'])
            if 'virtual_circuit' in data:
                self.__print_core_network_virtual_circuit(data['virtual_circuit'])

        except Exception as e:
            self.__print_error("__print_core_network", e)

    ##########################################################################
    # print load balancer backendset
    ##########################################################################
    def __print_load_balancer_backendset(self, backendset):

        try:
            for bs in backendset:
                print("")
                if 'desc' in bs:
                    print(self.tabs + "backendSet : " + bs['desc'])
                if 'status' in bs:
                    print(self.tabs + self.tabs + "Status : " + bs['status'])

                # list of backends
                if 'backends' in bs:
                    for backend in bs['backends']:
                        print(self.tabs + self.tabs + "Backend: " + backend['desc'])

                if 'health_check' in bs:
                    health = bs['health_check']
                    print(self.tabs + self.tabs + "H.Chk  : " + health['desc1'])
                    print(self.tabs + self.tabs + "         " + health['desc2'])

                if 'session_persistence' in bs:
                    if bs['session_persistence']:
                        print(self.tabs + self.tabs + "Cookie : " + bs['session_persistence']['desc'])

                if 'lb_cookie_session_persistence_configuration' in bs:
                    if bs['lb_cookie_session_persistence_configuration']:
                        print(self.tabs + self.tabs + "LCookie: " + bs['lb_cookie_session_persistence_configuration']['desc'])

                if 'ssl_cert' in bs:
                    if bs['ssl_cert']:
                        print(self.tabs + self.tabs + "Cert   : " + bs['ssl_cert']['desc'])

        except Exception as e:
            self.__print_error("__print_load_balancer_backendset", e)

    ##########################################################################
    # print load balancer config
    ##########################################################################

    def __print_load_balancer_details(self, load_balance_obj):
        try:
            lb = load_balance_obj
            print(self.taba + "Name       : " + lb['name'])
            print(self.tabs + "Status     : " + lb['status'])

            # subnets
            if 'subnets' in lb:
                for subnet in lb['subnets']:
                    print(self.tabs + "Subnet     : " + subnet)

            if 'nsg_names' in lb:
                if lb['nsg_names']:
                    print(self.tabs + "SecGrp     : " + lb['nsg_names'])

            # ip_addresses
            if 'ips' in lb:
                for ip in lb['ips']:
                    print(self.tabs + "IP         : " + ip)

            # listeners
            if 'listeners' in lb:
                if not lb['listeners']:
                    print(self.tabs + "Listener   : None")
                for listener in lb['listeners']:
                    print(self.tabs + "Listener   : " + listener['desc'])
                    if listener['path_route_set_name']:
                        print(self.tabs + "           : Paths: " + listener['path_route_set_name'])
                    if listener['rule_set_names']:
                        print(self.tabs + "           : Rules: " + self.list_to_str(listener['rule_set_names']))
                    if listener['hostname_names']:
                        print(self.tabs + "           : Hosts: " + self.list_to_str(listener['hostname_names']))
                print("")

            # Path route set
            if 'path_route' in lb:
                for prs in lb['path_route']:
                    print(self.tabs + "Path Route : " + prs['name'])
                    if 'path_routes' in prs:
                        for p in prs['path_routes']:
                            print(self.tabs + "           : Backendset: " + str(p['backend_set_name']) + ',  Path: ' + p['path'])

            # Hostnames
            if 'hostnames' in lb:
                for hostname in lb['hostnames']:
                    print(self.tabs + "Hostname   : " + hostname)

            if 'rule_sets' in lb:
                for rs in lb['rule_sets']:
                    print(self.tabs + "RuleSet    : " + rs['name'] + ": " + self.list_to_str(rs['items'], 'action'))

        except Exception as e:
            self.__print_error("__print_load_balancer_details", e)

    ##########################################################################
    # print network load balancer config
    ##########################################################################

    def __print_load_balancer_network_details(self, load_balance_obj):
        try:
            lb = load_balance_obj
            sym = lb['is_symmetric_hash_enabled'] if lb['is_symmetric_hash_enabled'] else "False"
            prsv = lb['is_preserve_source_destination'] if lb['is_preserve_source_destination'] else "False"
            print(self.taba + "Name       : " + lb['name'])
            print(self.tabs + "Status     : " + lb['status'])
            print(self.tabs + "Subnet     : " + lb['subnet_name'])
            print(self.tabs + "Flags      : is_symmetric_hash_enabled = " + sym + ", is_preserve_source_destination = " + prsv)

            if 'nsg_names' in lb:
                if lb['nsg_names']:
                    print(self.tabs + "SecGrp     : " + lb['nsg_names'])

            # ip_addresses
            if 'ips' in lb:
                for ip in lb['ips']:
                    print(self.tabs + "IP         : " + ip)

            # listeners
            if 'listeners' in lb:
                if not lb['listeners']:
                    print(self.tabs + "Listener   : None")
                for listener in lb['listeners']:
                    print(self.tabs + "Listener   : " + listener['desc'])
                print("")

        except Exception as e:
            self.__print_error("__print_load_balancer_network_details", e)

    ##########################################################################
    # Load Balancer main
    ##########################################################################

    def __print_load_balancer_main(self, load_balancers):
        try:

            if len(load_balancers) == 0:
                return
            self.print_header("Load Balancers", 2)

            for load_balance_obj in load_balancers:
                if 'details' in load_balance_obj:
                    self.__print_load_balancer_details(load_balance_obj['details'])

                # print logs
                if 'logs' in load_balance_obj:
                    for index, log in enumerate(load_balance_obj['logs'], start=1):
                        print(self.tabs + "Log " + str(index) + "      : " + log['name'])

                if 'backendset' in load_balance_obj:
                    self.__print_load_balancer_backendset(load_balance_obj['backendset'])

                print("")

        except Exception as e:
            self.__print_error("__print_load_balancer_main", e)

    ##########################################################################
    # Network Load Balancer main
    ##########################################################################

    def __print_load_balancer_network_main(self, load_balancers):
        try:

            if len(load_balancers) == 0:
                return
            self.print_header("Network Load Balancers", 2)

            for load_balance_obj in load_balancers:
                if 'details' in load_balance_obj:
                    self.__print_load_balancer_network_details(load_balance_obj['details'])

                if 'backendset' in load_balance_obj:
                    self.__print_load_balancer_backendset(load_balance_obj['backendset'])

                print("")

        except Exception as e:
            self.__print_error("__print_load_balancer_network_main", e)

    ##########################################################################
    # print file systems mount targets
    ##########################################################################
    def __print_file_storage_mount_target(self, mount_targets):

        try:
            for mt in mount_targets:
                print(self.tabs + "Mount     : " + mt['mount'])

                for ip in mt['private_ip_ids']:
                    print(self.tabs + "Mount IP  : " + ip)

        except Exception as e:
            self.__print_error("__print_file_storage_mount_target", e)

    ##########################################################################
    # print file systems exports
    ##########################################################################
    def __print_file_storage_exports(self, exports):

        try:
            for export in exports:
                if 'path' in export:
                    print(self.tabs + "Export    : " + export['path'])
                if 'exportset' in export:
                    print(self.tabs + "ExportSet : " + export['exportset'])

                # Mount Target
                self.__print_file_storage_mount_target(export['mount_target'])

        except Exception as e:
            self.__print_error("__print_file_storage_exports", e)

    ##########################################################################
    # File System
    ##########################################################################

    def __print_file_storage_main(self, file_systems):
        try:

            if len(file_systems) == 0:
                return
            self.print_header("File Storage", 2)

            # print details
            for fs in file_systems:
                if 'filesystem' in fs:
                    print(self.taba + fs['filesystem'])
                self.__print_file_storage_exports(fs['exports'])

                # snapshots
                if 'snapshots' in fs:
                    for snap in fs['snapshots']:
                        print(self.tabs + "Snap  : " + snap)

                print("")

        except Exception as e:
            self.__print_error("__print_file_storage_main", e)

    ##########################################################################
    # database exadata vmcluster
    ##########################################################################
    def __print_database_db_exadata_vmcluster(self, vmclusters):
        try:
            for vm in vmclusters:
                print("")

                if 'display_name' in vm:
                    print(self.tabs + "VMCLSTR   : " + str(vm['display_name']) + " (" + vm['lifecycle_state'] + ")")

                if 'cluster_name' in vm:
                    if vm['cluster_name']:
                        print(self.tabs + "Cluster   : " + vm['cluster_name'])

                if 'cpu_core_count' in vm:
                    print(self.tabs + "Cores     : " + str(vm['cpu_core_count']))

                if 'total_e_cpu_count' in vm:
                    print(self.tabs + "Tot ECPUs : " + str(vm['total_e_cpu_count']))

                if 'enabled_e_cpu_count' in vm:
                    print(self.tabs + "Enab ECPUs: " + str(vm['enabled_e_cpu_count']))

                if 'memory_size_in_gbs' in vm:
                    print(self.tabs + "Memory GB : " + str(vm['memory_size_in_gbs']))

                if 'vm_file_system_storage_in_gbs' in vm:
                    print(self.tabs + "FS GB     : " + str(vm['vm_file_system_storage_in_gbs']))

                if 'node_count' in vm:
                    if vm['node_count']:
                        print(self.tabs + "Nodes     : " + str(vm['node_count']))

                if 'domain' in vm:
                    if vm['domain']:
                        print(self.tabs + "Domain    : " + vm['domain'])

                if 'data_subnet' in vm:
                    if vm['data_subnet']:
                        print(self.tabs + "DataSub   : " + vm['data_subnet'])

                if 'backup_subnet' in vm:
                    if vm['backup_subnet']:
                        print(self.tabs + "BackSub   : " + vm['backup_subnet'])

                if 'scan_dns' in vm:
                    if vm['scan_dns']:
                        print(self.tabs + "Scan      : " + vm['scan_dns_name'])

                if 'scan_ips' in vm:
                    for ip in vm['scan_ips']:
                        print(self.tabs + "Scan Ips  : " + ip)

                if 'vip_ips' in vm:
                    for ip in vm['vip_ips']:
                        print(self.tabs + "VIP Ips   : " + ip)

                if 'listener_port' in vm:
                    print(self.tabs + "Port      : " + vm['listener_port'])

                if 'gi_version' in vm:
                    if vm['gi_version']:
                        if 'gi_version_date' in vm:
                            print(self.tabs + "Grid Ver  : " + vm['gi_version'] + "  " + vm['gi_version_date'])
                        else:
                            print(self.tabs + "Grid Ver  : " + vm['gi_version'])

                if 'system_version' in vm:
                    if vm['system_version']:
                        if 'system_version_date' in vm:
                            print(self.tabs + "Sys Ver   : " + vm['system_version'] + "  " + vm['system_version_date'])
                        else:
                            print(self.tabs + "Sys Ver   : " + vm['system_version'])

                if 'data_storage_percentage' in vm:
                    print(self.tabs + "Data      : " + vm['data_storage_percentage'] + "%, Sparse: " + vm['is_sparse_diskgroup_enabled'] + ", Local Backup: " + vm['is_local_backup_enabled'])

                if 'patches' in vm:
                    for p in vm['patches']:
                        print(self.tabs + "Patches   : " + p)

                # db nodes
                for index, db_node in enumerate(vm['db_nodes'], start=1):
                    print(self.tabs + "DB Node " + str(index) + " : " + db_node['desc'])
                    if 'nsg_names' in db_node:
                        if db_node['nsg_names']:
                            print(self.tabs + "          : SecGrp : " + db_node['nsg_names'])

                    if 'time_maintenance_window_start' in db_node:
                        if db_node['maintenance_type'] != "None":
                            print(self.tabs + self.tabs + "        Maintenance: " + db_node['maintenance_type'] + "  " + db_node['time_maintenance_window_start'][0:16] + " - " + db_node['time_maintenance_window_end'][0:16])

                # db homes
                for db_home in vm['db_homes']:
                    print(self.tabs + "Home      : " + db_home['home'])

                    # patches
                    for p in db_home['patches']:
                        print(self.tabs + self.tabs + "   PT : " + p)

                    # databases
                    for db in db_home['databases']:
                        pdbs = ", PDBS: " + self.list_to_str(db['pdbs'], 'name')
                        print(self.tabs + self.tabs + "   DB : " + db['name'] + pdbs)

                        # print data guard
                        for dg in db['dataguard']:
                            print(self.tabs + self.tabs + "        " + dg['name'])

                        # print backups
                        for backup in db['backups']:
                            print(self.tabs + self.tabs + "        " + backup['name'] + " - " + backup['time'] + " - DB Size " + backup['size'])

                    print(self.tabs + "          : " + '-' * 90)

        except Exception as e:
            self.__print_error("__print_database_db_exadata_vmcluster", e)

    ##########################################################################
    # database exadata
    ##########################################################################
    def __print_database_db_exadata_infra(self, list_exadata):

        try:
            for dbs in list_exadata:
                print("")

                print(self.taba + "ExaCS     : " + dbs['name'])
                print(self.tabs + "Created   : " + dbs['time_created'][0:16])
                print(self.tabs + "AD        : " + dbs['availability_domain'])

                if 'compute_count' in dbs:
                    if dbs['compute_count'] != "None":
                        print(self.tabs + "VM Hosts  : " + str(dbs['compute_count']))

                if 'storage_count' in dbs:
                    if dbs['storage_count'] != "None" and dbs['total_storage_size_in_gbs'] != "None":
                        print(self.tabs + "Storage   : Hosts = " + str(dbs['storage_count']) + ", Total = " + str(dbs['total_storage_size_in_gbs']) + "GB")

                if 'maintenance_window' in dbs:
                    if dbs['maintenance_window']:
                        print(self.tabs + "Maint     : Window : " + dbs['maintenance_window']['display'])

                if 'last_maintenance_run' in dbs:
                    if dbs['last_maintenance_run']:
                        print(self.tabs + "Maint     : Last   : " + dbs['last_maintenance_run']['description'])
                        print(self.tabs + "                   : " + dbs['last_maintenance_run']['maintenance_display'])

                if 'next_maintenance_run' in dbs:
                    if dbs['next_maintenance_run']:
                        print(self.tabs + "Maint     : Next   : " + dbs['next_maintenance_run']['description'])
                        print(self.tabs + "                   : " + dbs['next_maintenance_run']['maintenance_display'])
                        if dbs['next_maintenance_run']['maintenance_alert']:
                            print(self.tabs + "            Alert  : " + dbs['next_maintenance_run']['maintenance_alert'])

                print("")
                for index, srv in enumerate(dbs['db_servers'], start=1):
                    print(self.tabs + "DB Srv " + str(index) + "  : " + srv['desc'])

                # vmclusters
                self.__print_database_db_exadata_vmcluster(dbs['vm_clusters'])

                # ADB-D Clusters
                for vm in dbs['adb_clusters']:
                    print("")
                    print(self.tabs + "ADB-D VMCLUSTER: " + str(vm['display_name']) + " (" + vm['lifecycle_state'] + ")")
                    print(self.tabs + "AD             : " + vm['availability_domain'])
                    print(self.tabs + "Cores          : " + str(vm['cpu_core_count']))
                    print(self.tabs + "Nodes          : " + str(vm['node_count']))
                    print(self.tabs + "Domain         : " + vm['domain'])
                    print(self.tabs + "Subnet         : " + vm['subnet_name'])
                    print("")

                    # containers
                    for ct in vm['containers']:
                        print(self.tabs + "Container      : " + ct['name'])

                        # databases
                        for db in ct['databases']:
                            print(self.tabs + self.taba + "ADB-D DB   : " + db['name'])
                            print(self.tabs + self.tabs + "Size       : " + str(db['cpu_core_count']) + " OCPUs, " + str(db['data_storage_size_in_tbs']) + "TB Storage")
                            print(self.tabs + self.tabs + "Created    : " + db['time_created'])
                            print(self.tabs + self.tabs + "DataSafe   : " + db['data_safe_status'])
                            print(self.tabs + self.tabs + "Maintenance: " + db['time_maintenance_begin'][0:16] + " - " + db['time_maintenance_end'][0:16])
                            if db['is_data_guard_enabled']:
                                print(self.tabs + self.tabs + "Data Guard : Lag In Second: " + db['standby_lag_time_in_seconds'] + ", lifecycle: " + db['standby_lifecycle_state'] + ",  Last Switch: " + db['time_of_last_switchover'][0:16] + ",  Last Failover: " + db['time_of_last_switchover'][0:16])

                            # print backups
                            if db['backups']:
                                for backup in db['backups']:
                                    print(self.tabs + self.tabs + "         " + backup['name'] + " - " + backup['time'])
                            print("")

        except Exception as e:
            self.__print_error("__print_database_db_exadata_infra", e)

    ##########################################################################
    # database exadata
    ##########################################################################
    def __print_database_db_exascale(self, list_exascale):

        try:
            for dbs in list_exascale:
                print("")

                print(self.taba + "Exascale  : Vault : " + dbs['display_name'] + " - " + dbs['lifecycle_state'])
                print(self.tabs + "Created   : " + dbs['time_created'][0:16])
                print(self.tabs + "AD        : " + dbs['availability_domain'])
                print(self.tabs + "Total GB  : " + dbs['total_size_in_gbs'])
                print(self.tabs + "Available : " + dbs['available_size_in_gbs'])
                print(self.tabs + "Flash %   : " + dbs['additional_flash_cache_in_percent'])
                print(self.tabs + "Clusters  : " + dbs['vm_cluster_count'])

                # vmclusters
                self.__print_database_db_exadata_vmcluster(dbs['vm_clusters'])

        except Exception as e:
            self.__print_error("__print_database_db_exascale", e)

    ##########################################################################
    # database exacc
    ##########################################################################
    def __print_database_db_exacc_infra(self, list_exadata):

        try:
            for dbs in list_exadata:
                print("")

                print(self.taba + "ExaCC          : " + dbs['name'])
                print(self.tabs + "Created        : " + dbs['time_created'][0:16])

                if 'cpus_enabled' in dbs:
                    if dbs['cpus_enabled'] != "None":
                        print(self.tabs + "CPU Enabled    : " + dbs['cpus_enabled'] + " out of " + dbs['max_cpu_count'])

                if 'memory_size_in_gbs' in dbs:
                    if dbs['memory_size_in_gbs'] != "None":
                        print(self.tabs + "Memory in GB   : " + dbs['memory_size_in_gbs'] + " out of " + dbs['max_memory_in_gbs'])

                if 'db_node_storage_size_in_gbs' in dbs:
                    if dbs['db_node_storage_size_in_gbs'] != "None":
                        print(self.tabs + "Node Storage GB: " + dbs['db_node_storage_size_in_gbs'] + " out of " + dbs['max_db_node_storage_in_g_bs'])

                if 'data_storage_size_in_tbs' in dbs:
                    if dbs['data_storage_size_in_tbs'] != "None":
                        print(self.tabs + "Data Storage TB: " + dbs['data_storage_size_in_tbs'] + " out of " + dbs['max_data_storage_in_t_bs'])

                print(self.tabs + "Compute Count  : " + dbs['compute_count'])
                print(self.tabs + "Storage        : Hosts = " + str(dbs['storage_count']) + ", Additional = " + dbs['additional_storage_count'] + ", Activated = " + dbs['activated_storage_count'])
                print(self.tabs + "Control Plane  : " + str(dbs['cloud_control_plane_server1']) + ", " + dbs['cloud_control_plane_server2'])
                print(self.tabs + "Network CIDR   : Admin CIDR = " + str(dbs['admin_network_cidr']) + ", Netmask = " + dbs['netmask'] + ", Gateway = " + dbs['gateway'] + ", Infiniband = " + str(dbs['infini_band_network_cidr']))
                print(self.tabs + "Network Proxy  : Proxy = " + dbs['corporate_proxy'])
                print(self.tabs + "Network DNS    : DNS = " + dbs['dns_server'] + ", NTP = " + dbs['ntp_server'])

                if 'maintenance_window' in dbs:
                    if dbs['maintenance_window']:
                        print(self.tabs + "Maintenance    : Window : " + dbs['maintenance_window']['display'])

                if 'last_maintenance_run' in dbs:
                    if dbs['last_maintenance_run']:
                        print(self.tabs + "Maintenance    : Last   : " + dbs['last_maintenance_run']['description'])
                        print(self.tabs + "                        : " + dbs['last_maintenance_run']['maintenance_display'])

                if 'next_maintenance_run' in dbs:
                    if dbs['next_maintenance_run']:
                        print(self.tabs + "Maintenance    : Next   : " + dbs['next_maintenance_run']['description'])
                        print(self.tabs + "                        : " + dbs['next_maintenance_run']['maintenance_display'])
                        if dbs['next_maintenance_run']['maintenance_alert']:
                            print(self.tabs + "                 Alert  : " + dbs['next_maintenance_run']['maintenance_alert'])

                print("")
                for index, srv in enumerate(dbs['db_servers'], start=1):
                    print(self.tabs + "DB Server " + str(index) + "    : " + srv['desc'])

                # clusters
                num = 0
                for vm in dbs['vm_clusters']:
                    print("")
                    num += 1

                    if 'display_name' in vm:
                        print(self.tabs + "VM Cluster " + str(num) + "   : " + str(vm['display_name']) + " (" + vm['lifecycle_state'] + ")")

                    if 'cpus_enabled' in vm:
                        print(self.tabs + "Cores          : " + str(vm['cpus_enabled']))

                    if 'shape' in vm:
                        if vm['shape']:
                            print(self.tabs + "Shape          : " + str(vm['shape']))

                    if 'gi_version' in vm:
                        if vm['gi_version']:
                            print(self.tabs + "Grid Ver       : " + vm['gi_version'] + "  " + vm['gi_version_date'])

                    if 'system_version' in vm:
                        if vm['system_version']:
                            print(self.tabs + "Sys Ver        : " + vm['system_version'] + "  " + vm['system_version_date'])

                    if 'license_model' in vm:
                        if vm['license_model']:
                            print(self.tabs + "License        : " + vm['license_model'])

                    if 'data_storage_size_in_tbs' in vm:
                        print(self.tabs + "Data TB        : " + vm['data_storage_size_in_tbs'] + ", Sparse: " + vm['is_sparse_diskgroup_enabled'] + ", Local Backup: " + vm['is_local_backup_enabled'])

                    if 'patches' in vm:
                        for p in vm['patches']:
                            print(self.tabs + "Patches        : " + p)

                    # db nodes
                    for index, db_node in enumerate(vm['db_nodes'], start=1):
                        print(self.tabs + "DB Node " + str(index) + "      : " + db_node['desc'])
                        if 'nsg_names' in db_node:
                            if db_node['nsg_names']:
                                print(self.tabs + "        : SecGrp : " + db_node['nsg_names'])

                        if 'time_maintenance_window_start' in db_node:
                            if db_node['maintenance_type'] != "None":
                                print(self.tabs + self.tabs + "          Maintenance: " + db_node['maintenance_type'] + "  " + db_node['time_maintenance_window_start'][0:16] + " - " + db_node['time_maintenance_window_end'][0:16])

                    # db homes
                    for db_home in vm['db_homes']:
                        print(self.tabs + "Home           : " + db_home['home'])

                        # patches
                        for p in db_home['patches']:
                            print(self.tabs + self.tabs + "        PT : " + p)

                        # databases
                        for db in db_home['databases']:
                            pdbs = ", PDBS: " + self.list_to_str(db['pdbs'], 'name')
                            print(self.tabs + self.tabs + "        DB : " + db['name'] + pdbs)

                            # print data guard
                            for dg in db['dataguard']:
                                print(self.tabs + self.tabs + "             " + dg['name'])

                            # print backups
                            for backup in db['backups']:
                                print(self.tabs + self.tabs + "             " + backup['name'] + " - " + backup['time'] + " - DB Size " + backup['size'])

                        print(self.tabs + "               : " + '-' * 90)

                # ADB-D Clusters
                for vm in dbs['adb_clusters']:
                    print("")
                    print(self.tabs + "ADB-D VMCLUSTER: " + str(vm['display_name']) + " (" + vm['lifecycle_state'] + ")")
                    print(self.tabs + "OCPUs Enabled  : " + str(vm['ocpus_enabled']))
                    print("")

                    # containers
                    for ct in vm['containers']:
                        print(self.tabs + "Container      : " + ct['name'])

                        # databases
                        for db in ct['databases']:
                            print(self.tabs + self.taba + "ADB-D DB   : " + db['name'])
                            print(self.tabs + self.tabs + "Size       : " + str(db['cpu_core_count']) + " OCPUs, " + str(db['data_storage_size_in_tbs']) + "TB Storage")
                            print(self.tabs + self.tabs + "Created    : " + db['time_created'])
                            print(self.tabs + self.tabs + "DataSafe   : " + db['data_safe_status'])
                            print(self.tabs + self.tabs + "Maintenance: " + db['time_maintenance_begin'][0:16] + " - " + db['time_maintenance_end'][0:16])
                            if db['is_data_guard_enabled']:
                                print(self.tabs + self.tabs + "Data Guard : Lag In Second: " + db['standby_lag_time_in_seconds'] + ", lifecycle: " + db['standby_lifecycle_state'] + ",  Last Switch: " + db['time_of_last_switchover'][0:16] + ",  Last Failover: " + db['time_of_last_switchover'][0:16])

                            # print backups
                            if db['backups']:
                                for backup in db['backups']:
                                    print(self.tabs + self.tabs + "         " + backup['name'] + " - " + backup['time'])
                            print("")

        except Exception as e:
            self.__print_error("__print_database_db_exacc_infra", e)

    ##########################################################################
    # print database db system
    ##########################################################################

    def __print_database_db_system_details(self, dbs):
        try:
            print(self.taba + "DBaaS   : " + dbs['name'] + " - " + dbs['version'] + " " + dbs['version_date'])
            print(self.tabs + "Created : " + dbs['time_created'][0:16])
            print(self.tabs + "AD      : " + dbs['availability_domain'] + ", " + dbs['fault_domains'])

            if 'cpu_core_count' in dbs:
                print(self.tabs + "Cores   : " + str(dbs['cpu_core_count']))

            if 'node_count' in dbs:
                if dbs['node_count']:
                    print(self.tabs + "Nodes   : " + str(dbs['node_count']))

            if 'host' in dbs:
                print(self.tabs + "Host    : " + dbs['host'])

            if 'license_model' in dbs:
                print(self.tabs + "License : " + dbs['license_model'])

            if 'domain' in dbs:
                if dbs['domain']:
                    print(self.tabs + "Domain  : " + dbs['domain'])

            if 'cluster_name' in dbs:
                if dbs['cluster_name']:
                    print(self.tabs + "Cluster : " + dbs['cluster_name'])

            if 'database_edition' in dbs:
                if dbs['database_edition']:
                    print(self.tabs + "Edition : " + dbs['database_edition'])

            if 'data' in dbs:
                if dbs['data']:
                    print(self.tabs + "Data    : " + dbs['data'])

            if 'data_subnet' in dbs:
                print(self.tabs + "DataSub : " + dbs['data_subnet'])

            if 'backup_subnet' in dbs:
                if dbs['backup_subnet']:
                    print(self.tabs + "BackSub : " + dbs['backup_subnet'])

            if 'scan_dns' in dbs:
                if dbs['scan_dns']:
                    print(self.tabs + "Scan    : " + dbs['scan_dns_name'])

            if 'scan_ips' in dbs:
                for ip in dbs['scan_ips']:
                    print(self.tabs + "Scan Ips: " + ip)

            if 'vip_ips' in dbs:
                for ip in dbs['vip_ips']:
                    print(self.tabs + "VIP Ips : " + ip)

            if 'listener_port' in dbs:
                print(self.tabs + "Port    : " + dbs['listener_port'])

            if 'cluster_name' in dbs:
                if dbs['cluster_name']:
                    print(self.tabs + "Cluster : " + dbs['cluster_name'])

            if 'patches' in dbs:
                for p in dbs['patches']:
                    print(self.tabs + "Patches : " + p)

            if 'maintenance_window' in dbs:
                if dbs['maintenance_window']:
                    print(self.tabs + "Maint   : Window : " + dbs['maintenance_window']['display'])

            if 'last_maintenance_run' in dbs:
                if dbs['last_maintenance_run']:
                    print(self.tabs + "Maint   : Last   : " + dbs['last_maintenance_run']['description'])
                    print(self.tabs + "                 : " + dbs['last_maintenance_run']['maintenance_display'])

            if 'next_maintenance_run' in dbs:
                if dbs['next_maintenance_run']:
                    print(self.tabs + "Maint   : Next   : " + dbs['next_maintenance_run']['description'])
                    print(self.tabs + "                 : " + dbs['next_maintenance_run']['maintenance_display'])
                    if dbs['next_maintenance_run']['maintenance_alert']:
                        print(self.tabs + "          Alert  : " + dbs['next_maintenance_run']['maintenance_alert'])

            print(self.tabs + "        : " + '-' * 90)

        except Exception as e:
            self.__print_error("__print_database_db_system_details", e)

    ##########################################################################
    # database db systems
    ##########################################################################
    def __print_database_db_system(self, list_db_systems):

        try:
            for dbs in list_db_systems:
                print("")

                # db systems
                self.__print_database_db_system_details(dbs)

                # db nodes
                for db_node in dbs['db_nodes']:
                    print(self.tabs + "Node    : " + db_node['desc'] + ", Software Size: " + db_node['software_storage_size_in_gb'] + "GB")
                    if 'nsg_names' in db_node:
                        if db_node['nsg_names']:
                            print(self.tabs + "        : SecGrp : " + db_node['nsg_names'])

                    if 'time_maintenance_window_start' in db_node:
                        if db_node['maintenance_type'] != "None":
                            print(self.tabs + self.tabs + "      Maintenance: " + db_node['maintenance_type'] + "  " + db_node['time_maintenance_window_start'][0:16] + " - " + db_node['time_maintenance_window_end'][0:16])

                # db homes
                for db_home in dbs['db_homes']:
                    print(self.tabs + "Home    : " + db_home['home'])

                    # patches
                    for p in db_home['patches']:
                        print(self.tabs + self.tabs + " PT : " + p)

                    for p in db_home['patches_history']:
                        print(self.tabs + self.tabs + " PTH: " + p)

                    # databases
                    for db in db_home['databases']:
                        pdbs = ", PDBS: " + self.list_to_str(db['pdbs'], 'name')
                        print(self.tabs + self.tabs + " DB : " + db['name'] + pdbs)

                        # print data guard
                        for dg in db['dataguard']:
                            print(self.tabs + self.tabs + "      " + dg['name'])

                        # print backups
                        for backup in db['backups']:
                            print(self.tabs + self.tabs + "      " + backup['name'] + " - " + backup['time'] + " - DB Size " + backup['size'])

        except Exception as e:
            self.__print_error("__print_database_db_system", e)

    ##########################################################################
    # print database Autonomous Shared
    ##########################################################################

    def __print_database_db_autonomous(self, dbs):
        try:
            for db in dbs:
                print(self.taba + "ADB-S      : " + db['name'])
                if 'cpu_core_count' in db:
                    print(self.tabs + "Size       : " + str(db['compute_count']) + " " + db['compute_model'] + ", " + str(db['data_storage_size_in_tbs']) + "TB Storage")
                if 'time_created' in db:
                    print(self.tabs + "Created    : " + db['time_created'])
                if 'whitelisted_ips' in db:
                    if db['whitelisted_ips']:
                        print(self.tabs + "Allowed IPs: " + db['whitelisted_ips'])
                if 'private_endpoint' in db:
                    if db['private_endpoint']:
                        print(self.tabs + "Private EP : " + db['private_endpoint'] + ", Subnet: " + db['subnet_name'])
                if 'nsg_names' in db:
                    for nsg in db['nsg_names']:
                        print(self.tabs + "           : Network Security Group: " + nsg)
                if 'data_safe_status' in db:
                    print(self.tabs + "DataSafe   : " + db['data_safe_status'])
                if 'time_maintenance_begin' in db:
                    print(self.tabs + "Maintenance: " + db['time_maintenance_begin'][0:16] + " - " + db['time_maintenance_end'][0:16])
                if db['is_data_guard_enabled']:
                    print(self.tabs + "Data Guard : Lag In Second: " + db['standby_lag_time_in_seconds'] + ", lifecycle: " + db['standby_lifecycle_state'] + ",  Last Switch: " + db['time_of_last_switchover'][0:16] + ",  Last Failover: " + db['time_of_last_switchover'][0:16])

                # print backups
                if db['backups']:
                    for backup in db['backups']:
                        print(self.tabs + self.tabs + "         " + backup['name'] + " - " + backup['time'])
                print("")

        except Exception as e:
            self.__print_error("__print_database_db_autonomous", e)

    ##########################################################################
    # print database standalone backups
    ##########################################################################

    def __print_database_standalone_backups(self, backups):
        try:
            for backup in backups:
                if backup['standalone']:
                    print(self.taba + "Name    : " + backup['name'] + " - " + backup['time'] + " - " + backup['size'] + " - " + backup["availability_domain"])
                    print(self.tabs + "Shape   : " + backup['shape'] + ", Edition: " + backup["database_edition"] + ", Version: " + backup["version"])
                    print("")

        except Exception as e:
            self.__print_error("__print_database_standalone_backups", e)

    ##########################################################################
    # print database nosql
    ##########################################################################

    def __print_database_software_images(self, dbs):
        try:
            for db in dbs:
                print(self.taba + "Name    : " + db['display_name'] + " - " + db['patch_set'] + " - " + db['image_shape_family'] + " - " + db['image_type'])
                print(self.tabs + "Created : " + db['time_created'][0:16] + " (" + db['lifecycle_state'] + ")")
                print("")

        except Exception as e:
            self.__print_error("__print_database_software_images", e)

    ##########################################################################
    # print database external cdb
    ##########################################################################
    def __print_database_external(self, dbs):
        try:
            for db in dbs:
                print(self.taba + "Name      : " + db['display_name'] + " - " + db['db_unique_name'] + " - " + db['database_configuration'])
                print(self.tabs + "Created   : " + db['time_created'][0:16] + " (" + db['lifecycle_state'] + ")")
                print(self.tabs + "DB Manage : " + db['database_management_status'] + ", " + db['database_management_license_model'])
                print(self.tabs + "DB Version: " + db['database_version'] + ", " + db['database_edition'])
                print("")

        except Exception as e:
            self.__print_error("__print_database_external", e)

    ##########################################################################
    # print datasafe targets
    ##########################################################################
    def __print_datasafe(self, dbs):
        try:
            for db in dbs:
                cfg = db['global_config']
                print(self.taba + "Global    : " + cfg['data_safe_nat_gateway_ip_address'] + ", Enabled: " + cfg['is_enabled'] + ", State: " + cfg['lifecycle_state'] + ", Time Enabled: " + cfg['time_enabled'])
                print("")

                for target in db['targets']:
                    print(self.taba + "Target    : " + target['display_name'] + " - " + target['description'] + " - " + target['database_type'] + " - " + target['infrastructure_type'])
                    print(self.tabs + "Created   : " + target['time_created'][0:16] + " (" + target['lifecycle_state'] + ")")
                    if target['lifecycle_details']:
                        print(self.tabs + "Details   : " + target['lifecycle_details'][0:130] + "...")
                    for trg in target['associated_resource_ids']:
                        print(self.tabs + "Assoc Id  : " + trg)
                    for trg in target['associated_resource_names']:
                        print(self.tabs + "Assoc Name: " + trg)
                    print("")

                for target in db['private_endpoints']:
                    print(self.taba + "End Point : " + target['display_name'] + " - " + target['description'] + " - " + target['lifecycle_state'] + " - " + target['time_created'])
                    print(self.tabs + "Subnet    : " + target['subnet_name'])
                    print("")

                for target in db['on_prem_connectors']:
                    print(self.taba + "On Prem   : " + target['display_name'] + " - " + target['description'] + " - " + target['lifecycle_state'] + " - " + target['time_created'])
                    print("")

        except Exception as e:
            self.__print_error("__print_datasafe", e)

    ##########################################################################
    # print database nosql
    ##########################################################################

    def __print_database_nosql(self, dbs):
        try:
            for db in dbs:
                print(self.taba + "Table   : " + db['name'])
                print(self.tabs + "Created : " + db['time_created'][0:16] + " (" + db['lifecycle_state'] + ")")
                print(self.tabs + "Limits  : max_read_units: " + str(db['max_read_units']) + ", max_write_units: " + str(db['max_read_units']) + ", max_storage_in_g_bs: " + str(db['max_storage_in_g_bs']))
                print("")

        except Exception as e:
            self.__print_error("__print_database_nosql", e)

    ##########################################################################
    # print database mysql
    ##########################################################################

    def __print_database_mysql(self, dbs):
        try:
            for db in dbs:
                print(self.taba + "MYSQL   : " + db['display_name'] + " - " + db['description'] + " (" + db['mysql_version'] + ") - " + db['shape_name'])
                print(self.tabs + "AD      : " + db['availability_domain'] + " - " + db['fault_domain'])
                print(self.tabs + "Created : " + db['time_created'][0:16] + " (" + db['lifecycle_state'] + "), AutoBackup = " + db['backup_is_enabled'])
                print(self.tabs + "Subnet  : " + db['subnet_name'])
                print(self.tabs + "Size    : " + db['data_storage_size_in_gbs'] + "gb")

                # Endpoints
                for ep in db['endpoints']:
                    print(self.tabs + "endpoint: " + str(ep['ip_address']) + ":" + ep['port'] + ", Modes: " + ep['modes'] + " (" + ep['status'] + ")")
                if db['backups']:
                    print(self.tabs + "Backups : ")
                    for backup in db['backups']:
                        print(self.tabs + self.tabs + "      " + backup['display_name'] + " - " + backup['time_created'] + " - " + backup['backup_size_in_gbs'] + "gb" + " - " + backup['data_storage_size_in_gbs'] + "gb" + " - " + backup['backup_type'])
                print("")

        except Exception as e:
            self.__print_error("__print_database_mysql", e)

    ##########################################################################
    # print database mysql standalone backups
    ##########################################################################

    def __print_database_mysql_standalone_backups(self, backups):
        try:
            for backup in backups:
                print(self.tabs + self.tabs + "      " + backup['display_name'] + " - " + backup['time_created'] + " - " + backup['backup_size_in_gbs'] + "gb" + " - " + backup['data_storage_size_in_gbs'] + "gb" + " - " + backup['backup_type'])

        except Exception as e:
            self.__print_error("__print_database_mysql_standalone_backups", e)

    ##########################################################################
    # print database postgresql
    ##########################################################################

    def __print_database_postgresql(self, dbs):
        try:
            for db in dbs:
                print(self.taba + "PostgreSQL : " + db['display_name'] + " - (" + db['db_version'] + ") - " + db['shape_full'])
                print(self.tabs + "AD         : " + db['storage_availability_domain'])
                print(self.tabs + "Created    : " + db['time_created'][0:16] + " (" + db['lifecycle_state'] + ")")
                print(self.tabs + "Subnet     : " + db['network_subnet_name'])
                print(self.tabs + "IOPS       : " + db['storage_iops'])
                print(self.tabs + "Admin      : " + db['admin_username'])

                if db['backups']:
                    print(self.tabs + "Backups    : ")
                    for backup in db['backups']:
                        print(self.tabs + self.tabs + "         " + backup['display_name'] + " - " + backup['time_created'] + " - " + backup['backup_size'] + "gb" + " - " + backup['source_type'])
                print("")

        except Exception as e:
            self.__print_error("__print_database_postgresql", e)

    ##########################################################################
    # print database postgresql standalone backups
    ##########################################################################

    def __print_database_postgresql_standalone_backups(self, backups):
        try:
            for backup in backups:
                print(self.tabs + self.tabs + backup['display_name'] + " - " + backup['time_created'] + " - " + backup['backup_size'] + "gb" + " - " + backup['source_type'])

        except Exception as e:
            self.__print_error("__print_database_postgresql", e)

    ##########################################################################
    # print database goldengate
    ##########################################################################

    def __print_database_goldengate(self, goldengates):
        try:
            if 'gg_deployments' in goldengates:
                for db in goldengates['gg_deployments']:
                    print(self.taba + "GG      : " + db['display_name'] + " - " + db['description'] + " (" + db['lifecycle_state'] + ") - " + db['license_model'])
                    print(self.tabs + "OCPU    : " + db['cpu_core_count'] + ", Auto Scale: " + db['is_auto_scaling_enabled'] + ", Is Latest Version: " + db['is_latest_version'])
                    print(self.tabs + "Created : " + db['time_created'][0:16] + ", Updated: " + db['time_updated'][0:16])
                    print(self.tabs + "Subnet  : " + db['subnet_name'])
                    print(self.tabs + "IPs     : Private: " + db['private_ip_address'] + ", Public: " + db['public_ip_address'])
                    print(self.tabs + "FQDN    : " + db['fqdn'])
                    print(self.tabs + "URL     : " + db['deployment_url'])
                    print("")

            if 'gg_db_registration' in goldengates:
                for db in goldengates['gg_db_registration']:
                    print(self.taba + "DB Reg  : " + db['display_name'] + " - " + db['description'] + " (" + db['lifecycle_state'] + ")")
                    print(self.tabs + "Created : " + db['time_created'][0:16] + ", Updated: " + db['time_updated'][0:16])
                    if db['subnet_name']:
                        print(self.tabs + "Subnet  : " + db['subnet_name'])
                    print(self.tabs + "FQDN    : " + db['fqdn'])
                    print("")

        except Exception as e:
            self.__print_error("__print_database_goldengate", e)

    ##########################################################################
    # database
    ##########################################################################

    def __print_database_main(self, list_databases):
        try:

            if len(list_databases) == 0:
                return

            if 'exadata_infrastructure' in list_databases:
                self.print_header("Exadata Infrastructure", 2)
                self.__print_database_db_exadata_infra(list_databases['exadata_infrastructure'])
                print("")

            if 'exacc_infrastructure' in list_databases:
                self.print_header("ExaCC Infrastructure", 2)
                self.__print_database_db_exacc_infra(list_databases['exacc_infrastructure'])
                print("")

            if 'exascale' in list_databases:
                self.print_header("Exascale", 2)
                self.__print_database_db_exascale(list_databases['exascale'])
                print("")

            if 'db_system' in list_databases:
                self.print_header("Databases DB Base", 2)
                self.__print_database_db_system(list_databases['db_system'])
                print("")

            if 'db_all_backups' in list_databases:
                self.print_header("Databases Standalone Backups", 2)
                self.__print_database_standalone_backups(list_databases['db_all_backups'])
                print("")

            if 'autonomous_dedicated' in list_databases:
                self.print_header("Autonomous Dedicated", 2)
                self.__print_database_db_autonomous_dedicated(list_databases['autonomous_dedicated'])
                print("")

            if 'autonomous' in list_databases:
                self.print_header("Autonomous databases", 2)
                self.__print_database_db_autonomous(list_databases['autonomous'])
                print("")

            if 'mysql' in list_databases:
                self.print_header("MYSQL databases", 2)
                self.__print_database_mysql(list_databases['mysql'])
                print("")

            if 'mysql_standalone_backups' in list_databases:
                self.print_header("MYSQL Standalone Backups", 2)
                self.__print_database_mysql_standalone_backups(list_databases['mysql_standalone_backups'])
                print("")

            if 'postgresql' in list_databases:
                self.print_header("PostgreSQL databases", 2)
                self.__print_database_postgresql(list_databases['postgresql'])
                print("")

            if 'postgresql_standalone_backups' in list_databases:
                self.print_header("PostgreSQL Standalone Backups", 2)
                self.__print_database_postgresql_standalone_backups(list_databases['postgresql_standalone_backups'])
                print("")

            if 'goldengate' in list_databases:
                self.print_header("Golden Gate", 2)
                self.__print_database_goldengate(list_databases['goldengate'])
                print("")

            if 'nosql' in list_databases:
                self.print_header("NOSQL Tables", 2)
                self.__print_database_nosql(list_databases['nosql'])
                print("")

            if 'software_images' in list_databases:
                self.print_header("Database Software Images", 2)
                self.__print_database_software_images(list_databases['software_images'])

            if 'db_external_cdb' in list_databases:
                self.print_header("Database External CDB", 2)
                self.__print_database_external(list_databases['db_external_cdb'])

            if 'db_external_pdb' in list_databases:
                self.print_header("Database External PDB", 2)
                self.__print_database_external(list_databases['db_external_pdb'])

            if 'db_external_nonpdb' in list_databases:
                self.print_header("Database External NON-PDB", 2)
                self.__print_database_external(list_databases['db_external_nonpdb'])

            if 'datasafe' in list_databases:
                self.print_header("Datasafe", 2)
                self.__print_datasafe(list_databases['datasafe'])

        except Exception as e:
            self.__print_error("__print_database_main", e)

    ##########################################################################
    # object storage
    ##########################################################################
    def __print_object_storage_main(self, objects):

        try:
            if len(objects) == 0:
                return
            self.print_header("Object Storage", 2)

            for obj in objects:
                print(self.taba + obj['desc'])

        except Exception as e:
            self.__print_error("__print_object_storage_main", e)

    ##########################################################################
    # Email
    ##########################################################################
    def __print_email_main(self, emails):

        try:
            if 'senders' not in emails and 'supp_list' not in emails:
                return

            self.print_header("EMails", 2)

            if 'senders' in emails:
                print(self.taba + "Approved Senders:")
                for val in emails['senders']:
                    print(self.tabs + str(val))
                print("")

            if 'supp_list' in emails:
                print(self.taba + "Suppression List:")
                for val in emails['supp_list']:
                    print(self.tabs + str(val))

        except Exception as e:
            self.__print_error("__print_email_main", e)

    ##########################################################################
    # Streams and Queues
    ##########################################################################
    def __print_streams_queues_main(self, sq):

        try:
            if not sq:
                return

            if "streams" in sq:
                if sq["streams"]:
                    self.print_header("Streams", 2)

                    for ct in sq["streams"]:
                        print(self.taba + ct['name'] + ", partitions (" + ct['partitions'] + "), Created: " + ct['time_created'][0:16])
                        print(self.tabs + "URL   : " + str(ct['messages_endpoint']))
                        print("")

            if "queues" in sq:
                if sq["queues"]:
                    self.print_header("Queues", 2)

                    for ct in sq["queues"]:
                        print(self.taba + ct['name'] + ", Created: " + ct['time_created'][0:16])
                        print(self.tabs + "URL   : " + str(ct['messages_endpoint']))
                        print(self.tabs + "Params: Retention (Sec): " + str(ct['retention_in_seconds']) + ", Visibility: " + str(ct['visibility_in_seconds']) + ", Timeout: " + str(ct['timeout_in_seconds']) + ", Dead Letter Delivery Count: " + str(ct['dead_letter_queue_delivery_count']))
                        print("")

        except Exception as e:
            self.__print_error("__print_streams_queues_main", e)

    ##########################################################################
    # FSDR
    ##########################################################################
    def __print_fsdr(self, drs):

        try:
            if not drs:
                return

            self.print_header("Full Stack Disaster Recovery (FSDR)", 2)

            for dr in drs:
                print(self.taba + dr['display_name'] + " (" + dr['role'] + ":" + dr['lifecycle_state'] + "), Created: " + dr['time_created'])
                print(self.tabs + "Peer Region  : " + dr['peer_region'])
                if dr['lifecycle_sub_state']:
                    print(self.tabs + "Sub State    : " + dr['lifecycle_sub_state'])
                if dr['log_location']:
                    print(self.tabs + "Log Location : " + dr['log_location'])
                for member in dr['members']:
                    print(self.tabs + "member       : " + member['member_id'] + " - " + member['member_type'])
                print("")

        except Exception as e:
            self.__print_error("__print_fsdr", e)

    ##########################################################################
    # Functions
    ##########################################################################
    def __print_functions_main(self, functions):

        try:
            if not functions:
                return

            self.print_header("Function Applications", 2)

            for ct in functions:
                print(self.taba + ct['display_name'] + ", Created: " + ct['time_created'] + " - " + ct['shape'])
                if ct['subnets']:
                    for sub in ct['subnets']:
                        print(self.tabs + self.tabs + "Subnet: " + sub)
                if ct['network_security_group_names']:
                    print(self.tabs + self.tabs + "NSG   : " + ct['network_security_group_names'])
                for fun in ct['functions']:
                    print(self.tabs + self.tabs + "FN    : " + fun['display_name'] + " - " + fun['image'])

                print("")

        except Exception as e:
            self.__print_error("__print_functions_main", e)

    ##########################################################################
    # API Gateways
    ##########################################################################
    def __print_api_gateways_main(self, apigatways):

        try:
            if not apigatways:
                return

            self.print_header("API Gateways", 2)

            for ct in apigatways:
                print(self.taba + ct['display_name'] + ", " + ct['endpoint_type'] + ", Created: " + ct['time_created'][0:16])
                print(self.tabs2 + "Host      : " + ct['hostname'])
                print(self.tabs2 + "Subnet    : " + ct['subnet_name'])
                for dp in ct['deployments']:
                    print(self.tabs2 + "Deployment: " + dp['display_name'] + ", " + dp['endpoint'])

                    # print logs
                    if 'logs' in dp:
                        for index, log in enumerate(dp['logs'], start=1):
                            print(self.tabs2 + "          : Log " + str(index) + " : " + log['name'])

                print("")

        except Exception as e:
            self.__print_error("__print_streams_main", e)

    ##########################################################################
    # Budgets
    ##########################################################################
    def __print_budgets_main(self, budgets):

        try:
            if not budgets:
                return

            self.print_header("Budgets", 2)

            for budget in budgets:
                print(self.taba + budget['display_name'] + " for Compartment: " + budget['compartment_name'] + " (" + budget['reset_period'] + ")")
                print(self.tabs + "Costs   : Spent: " + budget['actual_spend'] + ", Forcasted: " + budget['forecasted_spend'], ", Time Computed: " + budget['time_spend_computed'][0:16])
                print(self.tabs + "Created : " + budget['time_created'][0:16] + ", Total Alert Rules: " + budget['alert_rule_count'])
                print("")

        except Exception as e:
            self.__print_error("__print_budgets_main", e)

    ##########################################################################
    # Announcement
    ##########################################################################
    def __print_announcement_main(self, announcements):

        try:
            if not announcements:
                return

            self.print_header("Announcements", 2)

            for ann in announcements:
                print(self.taba + ann['summary'][0:100] + " (" + ann['reference_ticket_number'] + ") - " + ann['announcement_type'] + ", Time: " + ann['time_one_value'][0:16] + " - " + ann['time_two_value'][0:16] + ", Time Created: " + ann['time_created'][0:16] + " (" + ann['lifecycle_state'] + ")")
                if ann['affected_regions']:
                    print(self.tabs + "Regions  : " + ann['affected_regions'])
                if ann['services']:
                    print(self.tabs + "Services : " + ann['services'])
                print("")

        except Exception as e:
            self.__print_error("__print_announcement_main", e)

    ##########################################################################
    # Announcement Active and Detailed
    ##########################################################################
    def __print_announcement_detailed(self, announcements):

        try:
            if not announcements:
                return

            self.print_header("Announcements Active and Detailed", 2)

            for ann in announcements:
                print(self.taba + ann['summary'][0:100] + " (" + ann['reference_ticket_number'] + ") - " + ann['announcement_type'] + ", Time: " + ann['time_one_value'][0:16] + " - " + ann['time_two_value'][0:16] + ", Time Created: " + ann['time_created'][0:16] + " (" + ann['lifecycle_state'] + ")")
                if ann['affected_regions']:
                    print(self.tabs + "Regions     : " + ann['affected_regions'])
                if ann['services']:
                    print(self.tabs + "Services    : " + ann['services'])
                if ann['affected_resources']:
                    print(self.tabs + "Resources   : (Not all resources part of this compartment)")
                    for an in ann['affected_resources']:
                        print(self.tabs + "              " + an['resource_name'] + " - " + an['region'])
                print("")

        except Exception as e:
            self.__print_error("__print_announcement_main", e)

    ##########################################################################
    # Errors
    ##########################################################################
    def __print_errors(self, errors):

        try:
            if not errors:
                return

            self.print_header("Service and Processing Issues", 2)

            for arr in errors:
                is_warning = "Warning: " if arr['is_warning'] == 'True' else "Error:   "
                compartment = ", Compartment " + arr['compartment'] if arr['compartment'] else ""
                print(self.taba + is_warning + arr['class'] + ":" + arr['function'] + ", " + arr['region'] + compartment + ", " + arr['error'][0:60])
            print("")

        except Exception as e:
            self.__print_error("__print_errors", e)

    ##########################################################################
    # __print_security_scores_main
    ##########################################################################
    def __print_security_scores_main(self, security_scores):

        try:
            if not security_scores:
                return

            self.print_header("Cloud Guard Security Scores", 2)

            if 'cloud_guard_security_scores' in security_scores:
                for arr in security_scores['cloud_guard_security_scores']:
                    print(self.taba + "Security Score: " + str(arr['security_score']) + " ( " + arr['security_rating'] + ")")
                for arr in security_scores['cloud_guard_risk_scores']:
                    print(self.taba + "Risk     Score: " + str(arr['risk_score']))
                print("")

        except Exception as e:
            self.__print_error("__print_security_scores_main", e)

    ##########################################################################
    # Monitoring
    ##########################################################################
    def __print_monitoring_main(self, monitorings):

        try:
            if not monitorings:
                return

            # if alarms
            if 'alarms' in monitorings:
                if monitorings['alarms']:
                    alarms = monitorings['alarms']
                    self.print_header("Monitoring - Alarms", 2)

                    for alarm in alarms:
                        print(self.taba + alarm['display_name'] + " (" + alarm['namespace'] + "), Enabled = " + str(alarm['is_enabled']) + ", Severity = " + alarm['severity'])
                        print(self.tabs + "Query : " + alarm['query'])
                        for dest in alarm['destinations_names']:
                            print(self.tabs + "Topic : " + dest)
                        print("")

            # if events
            if 'events' in monitorings:
                if monitorings['events']:
                    events = monitorings['events']
                    self.print_header("Events", 2)

                    for event in events:
                        print(self.taba + event['display_name'] + " (" + event['description'] + "), Enabled = " + str(event['is_enabled']))
                        print(self.tabs + "Condition : " + event['condition'])
                        for act in event['actions']:
                            print(self.tabs + "Action    : " + act['action_type'] + ", Enabled = " + act['is_enabled'] + ", " + act['lifecycle_state'] + ", Dest: " + act['dest_name'])
                        print("")

            # if agents
            if 'agents' in monitorings:
                if monitorings['agents']:
                    agents = monitorings['agents']
                    self.print_header("Management Agents", 2)

                    for event in agents:
                        print(self.taba + event['display_name'] + " (" + event['platform_name'] + "), Version = " + str(event['version']) + ", Status = " + event['availability_status'])
                        print(self.tabs + "Auto Upgradable : " + event['is_agent_auto_upgradable'])
                        print(self.tabs + "Plugin List     : " + event['plugin_list'])
                        print(self.tabs + "Created         : " + event['time_created'][0:16] + ", Last Beat: " + event['time_last_heartbeat'][0:16])
                        print(self.tabs + "Host            : " + event['host'])
                        print("")

            # if db_managements
            if 'db_managements' in monitorings:
                if monitorings['db_managements']:
                    agents = monitorings['db_managements']
                    self.print_header("DB Managements", 2)

                    for event in agents:
                        print(self.taba + event['name'] + ", " + event['database_type'] + ", " + str(event['database_sub_type']) + ", is_cluster = " + event['is_cluster'] + ", Created : " + event['time_created'][0:16])

        except Exception as e:
            self.__print_error("__print_monitoring_main", e)

    ##########################################################################
    # Notifications
    ##########################################################################
    def __print_notifications_main(self, topics):

        try:
            if not topics:
                return

            self.print_header("Notifications - Topics", 2)

            for topic in topics:
                print(self.taba + topic['name'] + " - " + topic['description'] + ",  Created: " + topic['time_created'][0:16])
                for sub in topic['subscriptions']:
                    print(self.tabs + "Sub   : " + sub['protocol'] + ": " + sub['endpoint'])
                print("")

        except Exception as e:
            self.__print_error("__print_notifications_main", e)

    ##########################################################################
    # Edge Services
    ##########################################################################
    def __print_edge_services_main(self, edge):

        try:
            if not edge:
                return

            # if healthcheck
            if 'healthcheck' in edge:
                self.print_header("Edge - Healthcheck", 2)

                # if http check
                if 'http' in edge['healthcheck']:
                    for arr in edge['healthcheck']['http']:
                        print(self.taba + arr['display_name'] + " (" + arr['protocol'] + ": " + arr['method'] + "), Path = " + arr['path'] + ", Enabled = " + str(arr['is_enabled']))
                        print(self.tabs + "Interval : " + arr['interval_in_seconds'] + " secs")
                        print(self.tabs + "Targets  : " + arr['targets'])
                        print(self.tabs + "VPoints  : " + arr['vantage_point_names'])
                        print("")

                # if ping check
                if 'ping' in edge['healthcheck']:
                    for arr in edge['healthcheck']['ping']:
                        print(self.taba + arr['display_name'] + " (" + arr['protocol'] + ", Port: " + arr['port'] + "), Enabled = " + str(arr['is_enabled']))
                        print(self.tabs + "Interval : " + arr['interval_in_seconds'] + " secs, Timeout = " + arr['timeout_in_seconds'] + " secs")
                        print(self.tabs + "Targets  : " + arr['targets'])
                        print(self.tabs + "VPoints  : " + arr['vantage_point_names'])
                        print("")

            # if dns_zone
            if 'dns_zone' in edge:
                self.print_header("DNS Zone", 2)

                for arr in edge['dns_zone']:
                    print(self.taba + arr['name'] + " (" + arr['zone_type'] + "), Version: " + arr['version'] + ", Serial: " + arr['serial'])
                    print(self.tabs + "URI : " + arr['self_uri'])
                    print("")

            # if dns_steering
            if 'dns_steering' in edge:
                self.print_header("DNS Steering Policies", 2)

                for arr in edge['dns_steering']:
                    print(self.taba + arr['display_name'] + " (" + arr['template'] + "), TTL: " + arr['ttl'])
                    print(self.tabs + "Health Check Id : " + arr['health_check_monitor_id'])
                    print("")

            # if waas_policies
            if 'waas_policies' in edge:
                self.print_header("WAAS Policies", 2)

                for arr in edge['waas_policies']:
                    print(self.taba + arr['display_name'])
                    print(self.tabs + "Domain : " + arr['domain'])
                    print("")

            # if waf
            if 'waf' in edge:
                self.print_header("Web Application Firewall", 2)

                for arr in edge['waf']:
                    print(self.taba + arr['display_name'])
                    print(self.tabs + "backend_type : " + arr['backend_type'] + ", policy_id: " + arr['web_app_firewall_policy_id'])
                    print("")

        except Exception as e:
            self.__print_error("__print_edge_services_main", e)

    ##########################################################################
    # Limits
    ##########################################################################
    def __print_limits_main(self, limits):

        try:
            if not limits:
                return

            self.print_header("Limits > 0", 2)

            for ct in limits:
                limit_name = ct['limit_name'].ljust(37)
                value = " = " + ct['value'].ljust(16)[0:16]
                used = (" Used = " + ct['used'].ljust(16)[0:16] + " ") if ct['used'] != "" else str(" ").ljust(25)
                available = (" Available = " + ct['available'].ljust(16)[0:16] + " ") if ct['available'] != "" else str(" ").ljust(30)
                scope = " SCOPE=" + ct['scope_type'].ljust(8) + ct['availability_domain']
                print(self.taba + str(ct['name'] + " ").ljust(20) + limit_name + value + used + available + scope)

            print("* numbers trimmed to 16 digits, if you need full value, please use json output")
            print("")

        except Exception as e:
            self.__print_error("__print_limits_main", e)

    ##########################################################################
    # Quotas
    ##########################################################################
    def __print_quotas_main(self, quotas):

        try:
            if not quotas:
                return

            self.print_header("Quotas", 2)

            for ct in quotas:
                print(self.taba + ct['name'] + ", (" + ct['description'] + "), Created: " + ct['time_created'][0:16])
                for st in ct['statements']:
                    print(self.tabs + st)

                print("")

        except Exception as e:
            self.__print_error("__print_quotas_main", e)

    ##########################################################################
    # PaaS Servics
    ##########################################################################

    def __print_paas_services_main(self, paas_services):

        try:
            if not paas_services:
                return

            # OIC
            if 'oic' in paas_services:
                self.print_header("OIC Native", 2)
                for val in paas_services['oic']:
                    print(self.taba + val['display_name'] + ", (" + val['integration_instance_type'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Pack     : " + val['message_packs'] + ", " + ("BYOL License" if val['is_byol'] else "License Included"))
                    print(self.tabs + "URL      : " + val['instance_url'])
                    if val['disaster_recovery_role']:
                        print(self.tabs + "DR Role  : " + val['disaster_recovery_role'])
                    if val['private_endpoint_outbound_connection_type']:
                        print(self.tabs + "PE Type  : " + val['private_endpoint_outbound_connection_type'])
                    if val['private_endpoint_outbound_connection_subnet_name']:
                        print(self.tabs + "PE Subnet: " + val['private_endpoint_outbound_connection_subnet_name'])
                    print("")

            # OAC
            if 'oac' in paas_services:
                self.print_header("OAC Native", 2)
                for val in paas_services['oac']:
                    print(
                        self.taba + val['name'] + ", (" + val['feature_set'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Desc   : " + val['description'])
                    print(self.tabs + "Email  : " + val['email_notification'] + ", License: " + str(val['license_type']) + ", Capacity: " + val['capacity_type'] + ":" + val['capacity_value'] + ", End Point: " + val['network_endpoint_details'])
                    print(self.tabs + "URL    : " + val['service_url'])
                    if val['vanity_url']:
                        print(self.tabs + "Vanity : " + val['vanity_domain'] + ", " + val['vanity_url'])
                    print("")

            # OCE
            if 'oce' in paas_services:
                self.print_header("OCE Native", 2)
                for val in paas_services['oce']:
                    print(self.taba + val['name'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Email: " + val['admin_email'])
                    if 'pod' in val['service']:
                        pod = val['service']['pod']
                        print(self.tabs + "Pod: " + str(pod['name']) + " (" + str(pod['version']) + ") ")
                    print("")

            # VB
            if 'vb' in paas_services:
                self.print_header("Visual Builder", 2)
                for val in paas_services['vb']:
                    print(self.taba + val['display_name'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + "), " + val['consumption_model'] + ", Enabled = " + val['is_visual_builder_enabled'] + ", Nodes = " + val['node_count'])
                    print(self.tabs + "URL: " + val['instance_url'])
                    if val['custom_endpoint']:
                        print(self.tabs + "   : Custom Endpoint: " + str(pod['custom_endpoint']))
                    if val['alternate_custom_endpoints']:
                        print(self.tabs + "   : Alt    Endpoint: " + str(pod['alternate_custom_endpoints']))
                    print("")

            # DevOPS
            if 'devops' in paas_services:
                self.print_header("DevOPS Projects", 2)
                for val in paas_services['devops']:
                    print(self.taba + val['name'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + "), " + val['namespace'])
                    print("")

            # Open Search
            if 'open_search' in paas_services:
                self.print_header("Open Search Clusters", 2)
                for val in paas_services['open_search']:
                    print(self.taba + val['display_name'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + "), " + val['software_version'])
                    if val['availability_domains']:
                        print(self.tabs + "ADs       : " + val['availability_domains'])
                    if val['security_mode']:
                        print(self.tabs + "Sec       : " + val['security_mode'])
                    print(self.tabs + "Search URL: " + val['opensearch_fqdn'])
                    print(self.tabs + "Dash URL  : " + val['opendashboard_fqdn'])
                    print(self.tabs + "Storage   : " + val['total_storage_gb'])
                    print(self.tabs + "Subnet    : " + val['opensearch_private_ip'] + ", " + val['subnet_name'])
                    print(self.tabs + "Master    : " + val['master_node_count'] + " x " + val['master_node_host_type'] + "." + val['master_node_host_ocpu_count'] + "." + val['master_node_host_memory_gb'])
                    print(self.tabs + "Data      : " + val['data_node_count'] + " x " + val['data_node_host_type'] + "." + val['data_node_host_ocpu_count'] + "." + val['data_node_host_memory_gb'])
                    print(self.tabs + "Dashboard : " + val['opendashboard_node_count'] + " x " + val['opendashboard_node_host_ocpu_count'] + "." + val['opendashboard_node_host_memory_gb'])
                    print("")

            # OCVS
            if 'ocvs' in paas_services:
                self.print_header("OCVS VMWare", 2)
                for val in paas_services['ocvs']:
                    print(self.taba + val['display_name'] + ", (" + val['vmware_software_version'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")" + ", OCPUS: " + val['sddc_ocpus'])
                    print(self.tabs + "Version   : " + val['vmware_software_version'])
                    print(self.tabs + "HCX       : " + val['hcx_mode'] + ", URL: " + val['hcx_fqdn'] + ", HCX License Status Update: " + val['time_hcx_license_status_updated'])
                    print(self.tabs + "VCENTER   : " + val['vcenter_fqdn'] + " - " + val['vcenter_private_ip'] + ", User: " + val['vcenter_username'])
                    print(self.tabs + "NSX       : " + val['nsx_manager_fqdn'] + " - " + val['nsx_manager_private_ip'] + ", User: " + val['nsx_manager_username'])
                    print(self.tabs + "NSX GW    : " + val['nsx_edge_uplink_ip'])
                    print(self.tabs + "Other     : Is Single Host: " + val['is_single_host_sddc'])
                    print(self.tabs + "Clusters  : " + val['clusters_count'])
                    print("")

                    for cl in val['clusters']:
                        nl = cl['network_configuration']
                        print(self.tabs + "Cluster   : " + cl['display_name'] + " - " + cl['compute_availability_domain'] + " - " + cl['vmware_software_version'] + " - " + cl['lifecycle_state'] + " - OCPUs: " + cl['cluster_ocpus'])
                        print(self.tabs + "Subnet    : " + nl['provisioning_subnet'])
                        print(self.tabs + "Other     : Is Shielded Instances: " + (cl['is_shielded_instance_enabled'] if cl['is_shielded_instance_enabled'] else "False") + ", VSPHERE Type: " + cl['vsphere_type'] + ", Data Stores: " + (str(len(cl['datastores'])) if cl['datastores'] else "0"))
                        print(self.tabs + "Vlans     : " + nl['vsphere_vlan'])
                        print(self.tabs + "    vmot  : " + nl['vmotion_vlan'])
                        print(self.tabs + "    vsan  : " + nl['vsan_vlan'])
                        print(self.tabs + "    vtep  : " + nl['nsx_v_tep_vlan'])
                        print(self.tabs + "    Edge  : " + nl['nsx_edge_v_tep_vlan'])
                        print(self.tabs + "    Up1   : " + nl['nsx_edge_uplink1_vlan'])
                        print(self.tabs + "    Up2   : " + nl['nsx_edge_uplink2_vlan'])
                        print(self.tabs + "    Prov  : " + nl['provisioning_vlan'])
                        print(self.tabs + "    HCX   : " + nl['hcx_vlan'])
                        if cl['datastores']:
                            num = 0
                            print(self.tabs + "DataStore : " + str(len(cl['datastores'])))
                            for ds in cl['datastores']:
                                num += 1
                                print(self.tabs + "    Vol " + str(num) + " : " + ds['datastore_type'] + ", Size: " + ds['capacity'] + "GB")

                        print(self.tabs + "ESXi Hosts: " + cl['esxi_hosts_count'])
                        num = 0
                        for esx in cl['esxihosts']:
                            num += 1
                            print(self.tabs + "    ESXi " + str(num) + ": " + esx['display_name'] + ", Created: " + esx['time_created'] + " (" + esx['lifecycle_state'] + "),  Billing End Date: " + esx['billing_contract_end_date'][0:16] + ", Commit: " + esx['current_commitment'] + ", Next Commit: " + esx['next_commitment'] + ", Shape: " + esx['host_shape_name'] + ", Cores: " + esx['host_ocpu_count'])

                    print("")

        except Exception as e:
            self.__print_error("__print_paas_services_main", e)

    ##########################################################################
    # Security
    ##########################################################################
    def __print_security_main(self, security):

        try:
            if not security:
                return

            # cloud guard
            if 'cloud_guard' in security:
                self.print_header("Cloud Guard", 2)

                for val in security['cloud_guard']:
                    print(self.taba + "Cloud Guard: " + val['display_name'] + ", (Target = " + val['target_resource_type'] + " " + val['target_resource_name'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + "), Total Recipes : " + val['recipe_count'])
                    if val['inherited_by_compartments']:
                        print(self.tabs + "Inherited  : " + val['inherited_by_compartments_names'])

                    for dr in val['target_detector_recipes']:
                        print(self.tabs + "Det Recipes: Owner = " + dr['owner'] + ", " + dr['display_name'] + ", Created: " + dr['time_created'][0:16] + " (" + dr['lifecycle_state'] + ")" + " Rules: " + str(len(dr['effective_detector_rules'])))

                    for dr in val['target_responder_recipes']:
                        print(self.tabs + "Res Recipes: Owner = " + dr['owner'] + ", " + dr['display_name'] + ", Created: " + dr['time_created'][0:16] + " Rules: " + str(len(dr['effective_responder_rules'])))

            # bastions
            if 'bastions' in security:
                self.print_header("Bastions", 2)
                for val in security['bastions']:
                    subnet = "(" + val['target_subnet_name'] + "), " if val['target_subnet_name'] else ""
                    print(self.taba + val['name'] + ", " + val['bastion_type'] + ", " + subnet + "Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print("")

            # kms_vaults
            if 'kms_vaults' in security:
                self.print_header("KMS Vaults", 2)
                for val in security['kms_vaults']:
                    print(self.taba + val['name'] + ", " + val['vault_type'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs2 + "Keys          : " + val['key_count'] + ", Versions: " + val['key_version_count'])
                    print(self.tabs2 + "Software Keys : " + val['software_key_count'] + ", Versions: " + val['software_key_version_count'])
                    print(self.tabs2 + "Management URL: " + val['management_endpoint'])
                    print(self.tabs2 + "Crypto URL    : " + val['crypto_endpoint'])
                    for rep in val['replicas']:
                        print(self.tabs2 + "Replicas      : " + rep['status'] + ", " + rep['region'] + ", " + rep['crypto_endpoint'])
                    print("")

            # Logging
            if 'logging' in security:
                self.print_header("Logging Groups", 2)
                for val in security['logging']:
                    print(self.taba + val['display_name'] + ", (" + val['description'] + "), Created: " + val['time_created'][0:16])
                    for log in val['logs']:
                        print(self.taba + self.tabs + "Log: " + log['display_name'] +
                              ", Enabled = " + log['is_enabled'] +
                              ", " + log['source_service'] +
                              " (" + log['source_sourcetype'] + ")" +
                              ", Category = " + log['source_category'] +
                              ", Resource: " + str(log['source_resource'] + "..").split(".")[1] +
                              ", State: " + log['lifecycle_state'] +
                              ", Created: " + log['time_created'][0:16])
                    print("")

            # Logging unified agents
            if 'logging_unified_agents' in security:
                self.print_header("Logging Unified Agents Configuration", 2)
                for val in security['logging_unified_agents']:
                    print(self.taba + val['display_name'] + ", (" + val['description'] + "), Is Enabled: " + val['is_enabled'] + ", Type: " + val['configuration_type'] + ", Created: " + val['time_created'][0:16])
                    print("")

            # Certificates
            if 'certificates' in security:
                self.print_header("Certificates", 2)
                for val in security['certificates']:
                    print(self.taba + val['name'] + ", " + val['description'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Validity Between: " + val['current_validity_not_before'] + " - " + val['current_validity_not_after'])
                    if val['associated_resource_ids']:
                        print(self.tabs + "Associate Ids   : " + val['associated_resource_ids'])
                        print(self.tabs + "Associate Names : " + val['associated_resource_names'])
                    else:
                        print(self.tabs + "No Associations")
                    print("")

            # Certificate Authorities
            if 'certificate_authorities' in security:
                self.print_header("Certificate Authorities", 2)
                for val in security['certificate_authorities']:
                    print(self.taba + val['name'] + ", " + val['description'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Validity Between: " + val['current_validity_not_before'] + " - " + val['current_validity_not_after'])
                    if val['associated_resource_ids']:
                        print(self.tabs + "Associate Ids   : " + val['associated_resource_ids'])
                        print(self.tabs + "Associate Names : " + val['associated_resource_names'])
                    else:
                        print(self.tabs + "No Associations")
                    print("")

            # Certificates CA Bundle
            if 'certificate_ca_bundles' in security:
                self.print_header("Certificate CA Bundle", 2)
                for val in security['certificate_ca_bundles']:
                    print(self.taba + val['name'] + ", " + val['description'] + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    if val['associated_resource_ids']:
                        print(self.tabs + "Associate Ids   : " + val['associated_resource_ids'])
                        print(self.tabs + "Associate Names : " + val['associated_resource_names'])
                    else:
                        print(self.tabs + "No Associations")
                    print("")

        except Exception as e:
            self.__print_error("__print_security_main", e)

    ##########################################################################
    # Data AI
    ##########################################################################
    def __print_data_ai(self, data_ai):

        try:
            if not data_ai:
                return

            # Data Catalog
            if 'data_catalog' in data_ai:
                self.print_header("Data Catalog", 2)
                for val in data_ai['data_catalog']:
                    print(self.taba + val['display_name'] + ", (" + val['number_of_objects'] + " objects), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                print("")

            # Data Science
            if 'data_science' in data_ai:
                self.print_header("Data Science", 2)
                for val in data_ai['data_science']:
                    print(self.taba + val['display_name'] + ", (" + val['description'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                print("")

            # Data Flow
            if 'data_flow' in data_ai:
                self.print_header("Data Flow", 2)
                for val in data_ai['data_flow']:
                    print(self.taba + val['display_name'] + ", (" + val['language'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Owner: " + val['owner_user_name'])
                print("")

            # ODA
            if 'oda' in data_ai:
                self.print_header("ODA Native", 2)
                for val in data_ai['oda']:
                    print(self.taba + val['display_name'] + ", (" + val['shape_name'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + " - " + val['lifecycle_sub_state'] + ")")
                print("")

            # BDS
            if 'bds' in data_ai:
                self.print_header("Big Data Service", 2)
                for val in data_ai['bds']:
                    print(self.taba + val['display_name'] + ", (" + val['cluster_version'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    is_high_availability = ", High Availability" if val['is_high_availability'] else ", No HA"
                    is_secure = ", Secure" if val['is_secure'] else ", Not Secure"
                    is_cloud_sql_configured = ", Cloud SQL Configured" if val['is_cloud_sql_configured'] else ", No Cloud SQL"
                    is_kafka_configured = ", Kafka Configured" if val['is_kafka_configured'] else ", No Kafka Configured"
                    print(self.tabs + "Config    : " + val['number_of_nodes'] + " Nodes" + is_high_availability + is_secure + is_cloud_sql_configured + is_kafka_configured)
                    print(self.tabs + "Versions  : Cluster: " + val['cluster_version'] + ", BDS: " + val['cluster_details_bds_version'] + ", OS: " + val['cluster_details_os_version'] + ", BDCell: " + val['cluster_details_bd_cell_version'] + ", ODH: " + val['cluster_details_bd_cell_version'])
                    print(self.tabs + "URLS      : Ambhari: " + val['cluster_details_ambari_url'] + ", Hue: " + val['cluster_details_hue_server_url'] + ", Jupyter: " + val['cluster_details_jupyter_hub_url'] + ", BigData: " + val['cluster_details_big_data_manager_url'])
                    for index, nd in enumerate(val['nodes'], start=1):
                        volumes = str(' '.join(str(x) + "gb" for x in nd['attached_block_volumes_gbs'])) + " volumes"
                        print(self.tabs + "Node " + str(index).ljust(3) + "  : " + nd['display_name'] + " (" + nd['lifecycle_state'] + "), Created: " + nd['time_created'][0:16] + ", Type: " + nd['node_type'].ljust(9) + ", " + nd['shape'] + "." + nd['ocpus'] + "." + nd['memory_in_gbs'] + ", " + volumes + ", IP: " + nd['ip_address'] + " " + nd['subnet_name'] + ", " + nd['availability_domain'] + ":" + nd['fault_domain'])
                    for index, nd in enumerate(val['autoscale'], start=1):
                        print(self.tabs + "AutoScale : " + nd['display_name'] + " (" + nd['lifecycle_state'] + "), Created: " + nd['time_created'][0:16] + ", Type: " + nd['policy_type'].ljust(9) + ", " + nd['policy_trigger_type'] + ", " + nd['policy_action_type'])
                print("")

            # DI
            if 'data_integration' in data_ai:
                self.print_header("Data Integration", 2)
                for val in data_ai['data_integration']:
                    description = (" (" + val['description'] + ")") if val['description'] != "None" else ""
                    print(self.taba + val['display_name'] + description + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                print("")

            # GenAI
            if 'genai' in data_ai:
                self.print_header("Generative AI", 2)
                for val in data_ai['genai']:
                    description = (" (" + val['description'] + ")") if val['description'] else ""
                    print(self.taba + val['display_name'] + description + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "   Type    : " + val['type'] + ", Unit: " + val['unit_shape'] + ", Count: " + val['unit_count'])
                    print(self.tabs + "   Capacity: " + val['capacity_type'] + ", Total: " + val['capacity_total_endpoint_capacity'] + ", Used: " + val['capacity_used_endpoint_capacity'])
                print("")

            # GenAI Agents
            if 'genai_agent' in data_ai:
                self.print_header("Generative AI Agent", 2)
                for val in data_ai['genai_agent']:
                    description = (" (" + val['description'] + ")") if val['description'] else ""
                    print(self.taba + val['display_name'] + description + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    if val['llm_config']:
                        print(self.tabs + "  LLM Cfg : " + val['llm_config'])
                    if val['welcome_message']:
                        print(self.tabs + "  Welcome : " + val['welcome_message'])
                print("")

            # GenAI Agents KB
            if 'genai_agent_kb' in data_ai:
                self.print_header("Generative AI Agent KBs", 2)
                for val in data_ai['genai_agent_kb']:
                    description = (" (" + val['description'] + ")") if val['description'] else ""
                    print(self.taba + val['display_name'] + description + ", Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                print("")

        except Exception as e:
            self.__print_error("__print_data_ai", e)

    ##########################################################################
    # Container
    ##########################################################################
    def __print_container_main(self, containers):

        try:
            if not containers:
                return

            self.print_header("Containers", 2)

            for ct in containers:
                print(self.taba + ct['name'] + " - " + ct['lifecycle_state'] + " - " + ct['kubernetes_version'])
                print(self.tabs + "VCN   : " + str(ct['vcn_name']))

                # print backups
                if ct['node_pools']:
                    for nd in ct['node_pools']:
                        print(self.tabs + "Node  : " + nd['name'] + " - " + nd['node_image_name'] + " - " + nd['node_shape'])

                        # subnets
                        if nd['subnets']:
                            for sub in nd['subnets']:
                                print(self.tabs + self.tabs + self.tabs + sub)

                print("")

        except Exception as e:
            self.__print_error("__print_email_main", e)

    ##########################################################################
    # resource Management
    ##########################################################################
    def __print_resource_management_main(self, resource_management):

        try:
            if len(resource_management) == 0:
                return

            self.print_header("Resource Management", 2)

            for val in resource_management:
                print(self.taba + str(val['stack_name']))
                if 'jobs' in val:
                    for job in val['jobs']:
                        print(self.tabs +
                              str(job['display_name']) + " - " +
                              str(job['operation']).ljust(10) + " - " +
                              str(job['lifecycle_state']).ljust(10) + " - " +
                              str(job['time_finished'])[0:16]
                              )
                print("")

        except Exception as e:
            self.__print_error("__print_resource_management_main", e)

    ##########################################################################
    # print compute instances
    ##########################################################################
    def __print_core_compute_instances(self, instances):

        try:

            if len(instances) == 0:
                return

            self.print_header("Compute Instances", 2)
            for instance in instances:
                if 'name' in instance:
                    print(self.taba + instance['name'])

                if instance['shape_ocpu'] > 0:
                    burstable = (", Burstable Baseline: " + str(instance['shape_baseline_ocpu_utilization'])) if instance['shape_baseline_ocpu_utilization'] else ""
                    gpu = (", GPUs: " + str(instance['shape_gpus']) + " " + str(instance['shape_gpu_description'])) if instance['shape_gpus'] else ""
                    local_storage = (", Local Storage: " + str(instance['shape_storage_tb']) + "TB") if instance['shape_storage_tb'] else ""
                    print(self.tabs2 + "Shape: Ocpus: " + str(instance['shape_ocpu']) + ", Memory: " + str(instance['shape_memory_gb']) + "GB" + burstable + ", Processor: " + str(instance['shape_processor_description']))
                    print(self.tabs2 + "       NetBW: " + str(instance['shape_networking_bandwidth_in_gbps']) + ", Max Vnics: " + str(instance['shape_max_vnic_attachments']) + local_storage + gpu)

                if 'availability_domain' in instance and 'fault_domain' in instance:
                    print(self.tabs2 + "AD   : " + instance['availability_domain'] + " - " + instance['fault_domain'])

                if 'time_maintenance_reboot_due' in instance:
                    if instance['time_maintenance_reboot_due'] != "None":
                        print(self.tabs2 + "MRB  : Maintenance Reboot Due " + instance['time_maintenance_reboot_due'])

                if 'image' in instance:
                    print(self.tabs2 + "Img  : " + instance['image'] + " (" + instance['image_os'] + ")")

                print(self.tabs2 + "Mig  : Live Migration Preferred: " + (instance['is_live_migration_preferred'] if instance['is_live_migration_preferred'] else "Default") + ", Recovery Action: " + instance['recovery_action'])

                if 'boot_volume' in instance:
                    for bv in instance['boot_volume']:
                        if 'desc' in bv:
                            print(self.tabs2 + "Boot : " + bv['desc'])

                if 'block_volume' in instance:
                    for bv in instance['block_volume']:
                        if 'desc' in bv:
                            print(self.tabs2 + "Vol  : " + bv['desc'])

                if 'vnic' in instance:
                    for vnic in instance['vnic']:
                        if 'desc' in vnic:
                            print(self.tabs2 + "VNIC : " + vnic['desc'])
                        if 'nsg_names' in vnic['details']:
                            if vnic['details']['nsg_names']:
                                print(self.tabs2 + "     : SecGrp: " + vnic['details']['nsg_names'])
                        if 'internal_fqdn' in vnic['details']:
                            if vnic['details']['internal_fqdn']:
                                print(self.tabs2 + "     : Int FQDN     : " + vnic['details']['internal_fqdn'])
                        if 'ip_addresses' in vnic:
                            print(self.tabs2 + "     : IP Addresses : " + self.list_to_str(vnic['ip_addresses'], 'ip_address'))

                if 'console' in instance:
                    if instance['console']:
                        print(self.tabs2 + instance['console'])

                if 'agent_is_management_disabled' in instance:
                    print(self.tabs2 + "Agent: Is Management Disabled = " + instance['agent_is_management_disabled'] + ", Is Monitoring Disabled = " + instance['agent_is_monitoring_disabled'])

                # print logs
                if 'logs' in instance:
                    for index, log in enumerate(instance['logs'], start=1):
                        print(self.tabs + "Log " + str(index) + "      : " + log['name'])
                print("")

        except Exception as e:
            self.__print_error("__print_core_compute_instances", e)

    ##########################################################################
    # print compute images
    ##########################################################################
    def __print_core_compute_images(self, images):

        try:
            if len(images) == 0:
                return

            self.print_header("Compute Custom Images", 2)
            for image in images:
                print(self.taba + image['desc'])

        except Exception as e:
            self.__print_error("__print_core_compute_images", e)

    ##########################################################################
    # print compute capacity reservation
    ##########################################################################
    def __print_core_compute_capacity_reservation(self, reservations):

        try:
            if len(reservations) == 0:
                return

            self.print_header("Compute Capacity Reservations", 2)
            for ct in reservations:
                lifecycle_state = ct['lifecycle_state']
                display_name = ct['display_name']
                value = "Reserved : " + str(ct['reserved_instance_count'])
                used = "Used : " + str(ct['used_instance_count'])
                available = "Available : " + str(ct['reserved_instance_count'] - ct['used_instance_count'])
                availability_domain = ct['availability_domain']
                shapes = ",".join(x['instance_shape'] + " (R=" + str(x['reserved_count']) + ":U=" + str(x['used_count']) + ")" for x in ct['config'])

                print(self.taba + display_name + " (" + lifecycle_state + ")")
                print(self.tabs + "Reservation   = " + value + ", " + used + ", " + available)
                print(self.tabs + "Avail. Domain = " + availability_domain)
                print(self.tabs + "Config Shapes = " + shapes)
                print("")

        except Exception as e:
            self.__print_error("__print_core_compute_capacity_reservation", e)

    ##########################################################################
    # print compute pool
    ##########################################################################
    def __print_core_compute_instance_pool(self, pools):

        try:
            if len(pools) == 0:
                return

            self.print_header("Compute Instance Pool", 2)
            for pool in pools:
                print(self.taba + pool['name'])
                print(self.tabs + self.tabs + "ADs   : " + pool['availability_domains'])
                print(self.tabs + self.tabs + "Config: " + pool['instance_configuration_name'])
                print("")

        except Exception as e:
            self.__print_error("__print_core_compute_instance_pool", e)

    ##########################################################################
    # print compute autoscaling
    ##########################################################################
    def __print_core_compute_autoscaling(self, autos):

        try:
            if len(autos) == 0:
                return

            self.print_header("Compute Autoscaling", 2)
            for auto in autos:
                print(self.taba + auto['name'])
                print(self.tabs + "Resource    : " + auto['resource_type'] + ": " + auto['resource_name'])

                # Policies
                for pol in auto['policies']:
                    print(self.tabs + "Policy      : " + pol['display_name'] + " (" + pol['policy_type'] + ")")
                    print(self.tabs + "   Capacity : Initial = " + pol['capacity_initial'] + ", Min = " + pol['capacity_min'] + ", Max = " + pol['capacity_max'])

                    # Rules
                    for rule in pol['rules']:
                        print(self.tabs + "   Rule     : " + rule)

                print("")

        except Exception as e:
            self.__print_error("__print_core_compute_autoscaling", e)

    ##########################################################################
    # print compute images
    ##########################################################################
    def __print_core_compute_instance_configuration(self, configs):

        try:
            if len(configs) == 0:
                return

            self.print_header("Compute Inst Configuration", 2)
            for config in configs:
                print(self.taba + config['name'])
                print(self.tabs + self.tabs + "Shape : " + config['shape'])
                print(self.tabs + self.tabs + "Source: " + config['source'])
                print("")

        except Exception as e:
            self.__print_error("__print_core_compute_instance_configuration", e)

    ##########################################################################
    # print compute boot volume or volumes
    ##########################################################################
    def __print_core_compute_boot_volume_backup(self, backups, header):

        try:
            if len(backups) == 0:
                return

            self.print_header(header, 2)
            prev_id = ""
            for backup in backups:
                if prev_id and prev_id != backup['id']:
                    print("")

                # if auto backup, print only the policy name
                desc_name = backup['desc']
                if 'via policy' in backup['desc']:
                    start = backup['desc'].find('via policy') + 12
                    desc_name = "AUTO (" + backup['desc'][start:] + ")"

                # print the line
                print(self.taba + backup['name'] + ", " + backup['size'] + ", " + desc_name + ", " + backup['type'])

                prev_id = backup['id']

        except Exception as e:
            self.__print_error("__print_core_compute_boot_volume_backup", e)

    ##########################################################################
    # print compute block volume Groups
    ##########################################################################
    def __print_core_compute_volume_groups(self, volgroups):

        try:
            if len(volgroups) == 0:
                return

            self.print_header("Block Volume Groups", 2)
            for volgrp in volgroups:
                print(self.taba + volgrp['name'] + " - " + volgrp['size_in_gbs'] + "GB")
                for vol in volgrp['volumes']:
                    print(self.tabs + self.tabs + " Vol : " + vol)

        except Exception as e:
            self.__print_error("__print_core_compute_volume_groups", e)

    ##########################################################################
    # print compute block volume not attached
    ##########################################################################
    def __print_core_compute_volume_not_attached(self, vols):

        try:
            if len(vols) == 0:
                return

            self.print_header("Block Volume Not Attached", 2)
            for vol in vols:
                print(self.taba + vol['desc'])

        except Exception as e:
            self.__print_error("__print_core_compute_volume_groups", e)

    ##########################################################################
    # print compute boot volume not attached
    ##########################################################################
    def __print_core_compute_boot_vol_not_attached(self, vols):

        try:
            if len(vols) == 0:
                return

            self.print_header("Block Boot Not Attached", 2)
            for vol in vols:
                print(self.taba + vol['desc'])

        except Exception as e:
            self.__print_error("__print_core_compute_boot_vol_not_attached", e)

    ##########################################################################
    # print Compute
    ##########################################################################
    def __print_core_compute_main(self, data):

        try:
            if len(data) == 0:
                return

            if 'instances' in data:
                self.__print_core_compute_instances(data['instances'])

            if 'instance_configuration' in data:
                self.__print_core_compute_instance_configuration(data['instance_configuration'])

            if 'instance_pool' in data:
                self.__print_core_compute_instance_pool(data['instance_pool'])

            if 'autoscaling' in data:
                self.__print_core_compute_autoscaling(data['autoscaling'])

            if 'images' in data:
                self.__print_core_compute_images(data['images'])

            if 'capacity_reservation' in data:
                self.__print_core_compute_capacity_reservation(data['capacity_reservation'])

            if 'boot_not_attached' in data:
                self.__print_core_compute_boot_vol_not_attached(data['boot_not_attached'])

            if 'volume_not_attached' in data:
                self.__print_core_compute_volume_not_attached(data['volume_not_attached'])

            if 'volume_group' in data:
                self.__print_core_compute_volume_groups(data['volume_group'])

            if 'boot_volume_backup' in data:
                self.__print_core_compute_boot_volume_backup(data['boot_volume_backup'], "Boot Volume Backups")

            if 'volume_backup' in data:
                self.__print_core_compute_boot_volume_backup(data['volume_backup'], "Block Volume Backups")

            if 'volume_group_backup' in data:
                self.__print_core_compute_boot_volume_backup(data['volume_group_backup'], "Block Volume Group Backups")

        except Exception as e:
            self.__print_error("__print_core_compute_main", e)

    ##########################################################################
    # Print Identity data
    ##########################################################################
    def __print_region_data(self, region_name, data):

        try:
            if not data:
                return

            for cdata in data:
                if 'path' in cdata:
                    self.print_header("Compartment " + cdata['path'], 1)
                if 'network' in cdata:
                    self.__print_core_network_main(cdata['network'])
                if 'compute' in cdata:
                    self.__print_core_compute_main(cdata['compute'])
                if 'database' in cdata:
                    self.__print_database_main(cdata['database'])
                if 'object_storage' in cdata:
                    self.__print_object_storage_main(cdata['object_storage'])
                if 'file_storage' in cdata:
                    self.__print_file_storage_main(cdata['file_storage'])
                if 'load_balancer' in cdata:
                    self.__print_load_balancer_main(cdata['load_balancer'])
                if 'network_load_balancer' in cdata:
                    self.__print_load_balancer_network_main(cdata['network_load_balancer'])
                if 'email' in cdata:
                    self.__print_email_main(cdata['email'])
                if 'resource_management' in cdata:
                    self.__print_resource_management_main(cdata['resource_management'])
                if 'containers' in cdata:
                    self.__print_container_main(cdata['containers'])
                if 'streams_queues' in cdata:
                    self.__print_streams_queues_main(cdata['streams_queues'])
                if 'fsdr' in cdata:
                    self.__print_fsdr(cdata['fsdr'])
                if 'monitoring' in cdata:
                    self.__print_monitoring_main(cdata['monitoring'])
                if 'notifications' in cdata:
                    self.__print_notifications_main(cdata['notifications'])
                if 'edge_services' in cdata:
                    self.__print_edge_services_main(cdata['edge_services'])
                if 'quotas' in cdata:
                    self.__print_quotas_main(cdata['quotas'])
                if 'paas_services' in cdata:
                    self.__print_paas_services_main(cdata['paas_services'])
                if 'security' in cdata:
                    self.__print_security_main(cdata['security'])
                if 'data_ai' in cdata:
                    self.__print_data_ai(cdata['data_ai'])
                if 'apigateways' in cdata:
                    self.__print_api_gateways_main(cdata['apigateways'])
                if 'announcement_detailed' in cdata:
                    self.__print_announcement_detailed(cdata['announcement_detailed'])
                if 'functions' in cdata:
                    self.__print_functions_main(cdata['functions'])

        except Exception as e:
            self.__print_error("__print_region_data", e)
            raise


##########################################################################
# This section has ShowOCISummary class
# it accept data as JSON format and print summary
##########################################################################
class ShowOCISummary(object):

    ##########################################################################
    # spaces for align
    ##########################################################################
    tabs = ' ' * 4
    taba = '--> '
    error = 0

    summary_global_list = []
    summary_global_data = []
    summary_global_region_total = []
    summary_global_region_json = {}
    summary_global_total = []

    ############################################
    # Init
    ############################################
    def __init__(self):

        # Initiate summary objects everytime class is instantiated
        self.summary_global_list = []
        self.summary_global_data = []
        self.summary_global_region_total = []
        self.summary_global_region_json = {}
        self.summary_global_total = []

    ##########################################################################
    # get summary total
    ##########################################################################
    def get_summary_json(self):
        return {'data': self.summary_global_data, 'regions_totals': self.summary_global_region_json, 'total': self.summary_global_total}

    ##########################################################################
    # print_main
    ##########################################################################
    def print_summary(self, data):

        try:

            for d in data:
                if 'type' in d:

                    if d['type'] == "region":
                        self.__summary_region_data(d['region'], d['data'])

                    elif d['type'] == "identity":
                        self.__summary_identity(d['data'])

            self.summary_global_total = self.__summary_group_by("type", self.summary_global_total)
            self.__summary_print_results(self.summary_global_total, "Summary Total", 0)

        except Exception as e:
            self.__print_error("print_summary", e)

    ##########################################################################
    # get errors
    ##########################################################################
    def get_errors(self):
        return self.error

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, msg, e):
        classname = type(self).__name__

        if isinstance(e, KeyError):
            print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + msg + ": " + str(e))

        self.error += 1

    ##########################################################################
    # Print header centered
    ##########################################################################
    def __summary_print_header(self, name, category):
        options = {0: 95, 1: 60, 2: 30, 3: 85}
        chars = int(options[category])
        print("")
        print('#' * chars)
        print("#" + name.center(chars - 2, " ") + "#")
        print('#' * chars)

    ##########################################################################
    # Load Balancer
    ##########################################################################

    def __summary_load_balancer_main(self, load_balancers):
        try:

            if len(load_balancers) == 0:
                return

            for load_balance_obj in load_balancers:
                if 'sum_info' in load_balance_obj:
                    self.summary_global_list.append({'type': load_balance_obj['sum_info'], 'size': 1})

        except Exception as e:
            self.__print_error("__summary_load_balancer_main", e)

    ##########################################################################
    # File System
    ##########################################################################
    def __summary_file_storage_main(self, file_systems):
        try:

            if len(file_systems) == 0:
                return

            self.__summary_core_size(file_systems)

        except Exception as e:
            self.__print_error("__summary_file_storage_main", e)

    ##########################################################################
    # object storage
    ##########################################################################
    def __summary_object_storage_main(self, objects):

        try:
            if len(objects) == 0:
                return

            self.__summary_core_size(objects)

        except Exception as e:
            self.__print_error("__summary_object_storage_main", e)

    ##########################################################################
    # Containers OKE
    ##########################################################################
    def __summary_container_main(self, objects):

        try:
            if len(objects) == 0:
                return

            self.__summary_core_size(objects)

            for cn in objects:
                if 'node_pools' in cn:
                    for node in cn['node_pools']:
                        ocpus = node['node_shape_ocpus']
                        if ocpus:
                            if isinstance(ocpus, int) or isinstance(ocpus, float):
                                self.summary_global_list.append({
                                    'type': 'OKE Clusters OCPUs - ' + node['node_shape'],
                                    'size': float(ocpus)
                                })

        except Exception as e:
            self.__print_error("__summary_container_main", e)

    ##########################################################################
    # paas services
    ##########################################################################
    def __summary_paas_services_main(self, paas_services):

        try:
            if not paas_services:
                return

            if 'oic' in paas_services:
                array = [x for x in paas_services['oic'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['oic'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'oac' in paas_services:
                array = [x for x in paas_services['oac'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['oac'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'oce' in paas_services:
                array = [x for x in paas_services['oce'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['oce'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'ocvs' in paas_services:
                array = [x for x in paas_services['ocvs'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['ocvs'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")
                for ocvs in paas_services['ocvs']:
                    for cluster in ocvs['clusters']:
                        for esxi in cluster['esxihosts']:
                            self.summary_global_list.append({'type': "PaaS OCVS ESXi " + esxi['host_shape_name'] + " (Count)", 'size': float(1)})
                            if esxi['host_ocpu_count'] and str(esxi['host_ocpu_count']).replace(".", "").isnumeric():
                                self.summary_global_list.append({'type': "PaaS OCVS ESXi " + esxi['host_shape_name'] + " (OCPUs)", 'size': float(esxi['host_ocpu_count'])})

            if 'vb' in paas_services:
                array = [x for x in paas_services['vb'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['vb'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'devops' in paas_services:
                array = [x for x in paas_services['devops'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['devops'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'open_search' in paas_services:
                array = [x for x in paas_services['open_search'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in paas_services['open_search'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

        except Exception as e:
            self.__print_error("__summary_paas_services_main", e)

    ##########################################################################
    # security
    ##########################################################################
    def __summary_security(self, security):

        try:
            if not security:
                return

            if 'cloud_guard' in security:
                self.__summary_core_size(security['cloud_guard'])
            if 'logging' in security:
                self.__summary_core_size(security['logging'])
            if 'logging_unified_agents' in security:
                self.__summary_core_size(security['logging_unified_agents'])
            if 'bastions' in security:
                self.__summary_core_size(security['bastions'])
            if 'kms_vaults' in security:
                self.__summary_core_size(security['kms_vaults'])
                self.__summary_core_size(security['kms_vaults'], "sum_info_hsm", 'key_count')
                self.__summary_core_size(security['kms_vaults'], "sum_info_soft", 'software_key_count')
            if 'certificates' in security:
                self.__summary_core_size(security['certificates'])
            if 'certificate_associations' in security:
                self.__summary_core_size(security['certificate_associations'])
            if 'certificate_ca_bundles' in security:
                self.__summary_core_size(security['certificate_ca_bundles'])
            if 'certificate_authorities' in security:
                self.__summary_core_size(security['certificate_authorities'])

        except Exception as e:
            self.__print_error("__summary_security", e)

    ##########################################################################
    # data ai services
    ##########################################################################

    def __summary_data_ai_main(self, data_ai):

        try:
            if not data_ai:
                return

            if 'data_catalog' in data_ai:
                array = [x for x in data_ai['data_catalog'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['data_catalog'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'data_science' in data_ai:
                array = [x for x in data_ai['data_science'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['data_science'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'data_flow' in data_ai:
                array = [x for x in data_ai['data_flow'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['data_flow'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'oda' in data_ai:
                array = [x for x in data_ai['oda'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['oda'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'bds' in data_ai:
                array = [x for x in data_ai['bds'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['bds'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")
                # add shapes
                for bds in data_ai['bds']:
                    for nd in bds['nodes']:
                        for stg in nd['attached_block_volumes_gbs']:
                            self.summary_global_list.append({'type': "Big Data Service (Block Storage GB)", 'size': float(stg)})
                        if nd['lifecycle_state'] == 'ACTIVE':
                            info = "Big Data Service Compute - " + nd['shape'] + "." + nd['ocpus'] + "." + nd['memory_in_gbs']
                            self.summary_global_list.append({'type': info, 'size': float(1)})
                            self.summary_global_list.append({'type': "Big Data Service (OCPUs)", 'size': float(nd['ocpus'])})
                            self.summary_global_list.append({'type': "Big Data Service (Memory GB)", 'size': float(nd['memory_in_gbs'])})

            if 'data_integration' in data_ai:
                array = [x for x in data_ai['data_integration'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['data_integration'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'genai' in data_ai:
                array = [x for x in data_ai['genai'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in data_ai['genai'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'genai_agent' in data_ai:
                self.__summary_core_size(data_ai['genai_agent'])

            if 'genai_agent_kb' in data_ai:
                self.__summary_core_size(data_ai['genai_agent_kb'])

        except Exception as e:
            self.__print_error("__summary_data_ai_main", e)

    ##########################################################################
    # Identity Domains
    ##########################################################################

    def __summary_identity(self, identity):

        try:
            self.summary_global_list = []
            if not identity:
                return

            if 'compartments' in identity:
                self.__summary_core_count(identity['compartments'], 'Identity - Compartments')

            if 'policies' in identity:
                for policies in identity['policies']:
                    self.__summary_core_count(policies['policies'], 'Identity - Policies')
                    for policy in policies['policies']:
                        self.__summary_core_count(policy['statements'], 'Identity - Policies Statements')

            if 'tag_namespace' in identity:
                self.__summary_core_count(identity['tag_namespace'], 'Identity - Tag Namsespaces')

            if 'groups' in identity:
                self.__summary_core_count(identity['groups'], 'Identity - Groups')

            if 'users' in identity:
                self.__summary_core_count(identity['users'], 'Identity - Users')
                for arr in identity['users']:
                    if 'api_keys' in arr:
                        self.__summary_core_count(arr['api_keys'], 'Identity - Users API Keys')
                    if 'auth_token' in arr:
                        self.__summary_core_count(arr['auth_token'], 'Identity - Users Auth Tokens')
                    if 'secret_key' in arr:
                        self.__summary_core_count(arr['secret_key'], 'Identity - Users Secret Keys')
                    if 'smtp_cred' in arr:
                        self.__summary_core_count(arr['smtp_cred'], 'Identity - Users SMTP Creds')

            if 'domains' in identity:
                self.__summary_core_count(identity['domains'], "Identity - Domains")

                for domain in identity['domains']:

                    if 'users' in domain:
                        self.__summary_core_count(domain['users'], "Identity Domains - Users")
                        for arr in domain['users']:
                            self.__summary_core_count(arr['api_keys'], 'Identity Domains - Users API Keys')
                            self.__summary_core_count(arr['auth_tokens'], 'Identity Domains - Users Auth Tokens')
                            self.__summary_core_count(arr['customer_secret_keys'], 'Identity Domains - Users Secret Keys')
                            self.__summary_core_count(arr['smtp_credentials'], 'Identity Domains - Users SMTP Creds')
                            self.__summary_core_count(arr['o_auth2_client_credentials'], 'Identity Domains - Users OAuth Creds')
                            self.__summary_core_count(arr['db_credentials'], 'Identity Domains - Users DB Creds')

                    if 'groups' in domain:
                        self.__summary_core_count(domain['groups'], "Identity Domains - Groups")

                    if 'dynamic_groups' in domain:
                        self.__summary_core_count(domain['dynamic_groups'], "Identity Domains - DynGroups")

                    if 'network_perimeters' in domain:
                        self.__summary_core_count(domain['network_perimeters'], "Identity Domains - Network Perimeters")

                    if 'identity_providers' in domain:
                        self.__summary_core_count(domain['identity_providers'], "Identity Domains - IDPs")

                    if 'password_policies' in domain:
                        self.__summary_core_count(domain['password_policies'], 'Identity Domains - Password Policies')

            # aggregate the data
            self.summary_global_list = self.__summary_group_by("type", self.summary_global_list)

            # append data to global data
            self.summary_global_data.append({'type': 'identity', 'summary': self.summary_global_list})

            self.__summary_print_results(self.summary_global_list, "Summary Identity", 3)

            # Merge to Total
            self.summary_global_total.extend(self.summary_global_list)

        except Exception as e:
            self.__print_error("__summary_identity", e)

    ##########################################################################
    # edge services
    ##########################################################################

    def __summary_data_edge(self, edge):

        try:
            if not edge:
                return

            if 'waf' in edge:
                array = [x for x in edge['waf'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in edge['waf'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

            if 'waf' in edge:
                array = [x for x in edge['waas_policies'] if x['lifecycle_state'] == 'ACTIVE']
                self.__summary_core_size(array)
                array = [x for x in edge['waas_policies'] if x['lifecycle_state'] != 'ACTIVE']
                self.__summary_core_size(array, add_info="Stopped ")

        except Exception as e:
            self.__print_error("__summary_data_edge", e)

    ##########################################################################
    # print database autonumous
    ##########################################################################

    def __summary_database_db_autonomous(self, dbs):

        try:
            for db in dbs:
                if 'sum_info' in db and 'sum_count' in db:

                    if db['sum_count'].replace(".", "").isnumeric():
                        self.summary_global_list.append({'type': "Total " + db['compute_model'] + "s - Autonomous Database", 'size': float(db['sum_count'])})

                        if float(db['sum_count']) == 0:
                            self.summary_global_list.append({'type': db['sum_info_stopped'], 'size': 1})
                        else:
                            self.summary_global_list.append({'type': db['sum_info_count'], 'size': 1})
                            self.summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_count'])})

                if 'sum_info_storage' in db and 'sum_size_tb' in db:
                    if db['sum_size_tb'].replace(".", "").isnumeric():
                        self.summary_global_list.append({'type': db['sum_info_storage'], 'size': float(db['sum_size_tb'])})

        except Exception as e:
            self.__print_error("__summary_database_db_autonomous", e)

    ##########################################################################
    # print nosql + mysql
    ##########################################################################

    def __summary_database_nosql(self, dbs):

        try:
            for db in dbs:
                if 'sum_info' in db:
                    self.summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_size_gb'])})

        except Exception as e:
            self.__print_error("__summary_database_nosql", e)

    ##########################################################################
    # print external
    ##########################################################################

    def __summary_database_external(self, dbs):

        try:
            for db in dbs:
                if 'sum_info' in db:
                    self.summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_size_gb'])})

        except Exception as e:
            self.__print_error("__summary_database_external", e)

    ##########################################################################
    # Database
    ##########################################################################

    def __summary_database_main(self, list_databases):

        try:

            if len(list_databases) == 0:
                return

            if 'exadata_infrastructure' in list_databases:
                self.__summary_database_db_exadata(list_databases['exadata_infrastructure'])

            if 'exacc_infrastructure' in list_databases:
                self.__summary_database_db_exacc(list_databases['exacc_infrastructure'])

            if 'exascale' in list_databases:
                self.__summary_database_db_exascale(list_databases['exascale'])

            if 'db_system' in list_databases:
                self.__summary_database_db_system(list_databases['db_system'])

            if 'db_all_backups' in list_databases:
                self.__summary_database_all_backups(list_databases['db_all_backups'])

            if 'autonomous' in list_databases:
                self.__summary_database_db_autonomous(list_databases['autonomous'])

            if 'autonomous_dedicated' in list_databases:
                self.__summary_database_db_autonomous_dedicated(list_databases['autonomous_dedicated'])

            if 'nosql' in list_databases:
                self.__summary_database_nosql(list_databases['nosql'])

            if 'mysql' in list_databases:
                self.__summary_database_mysql(list_databases['mysql'])

            if 'postgresql' in list_databases:
                self.__summary_database_postgresql(list_databases['postgresql'])

            if 'goldengate' in list_databases:
                self.__summary_database_goldengate(list_databases['goldengate'])

            if 'db_external_cdb' in list_databases:
                self.__summary_database_external(list_databases['db_external_cdb'])

            if 'db_external_pdb' in list_databases:
                self.__summary_database_external(list_databases['db_external_pdb'])

            if 'db_external_nonpdb' in list_databases:
                self.__summary_database_external(list_databases['db_external_nonpdb'])

            if 'datasafe' in list_databases:
                self.__summary_database_external(list_databases['datasafe'])

        except Exception as e:
            self.__print_error("__summary_database_main", e)

    ##########################################################################
    # __summary_database_all_backups
    ##########################################################################
    def __summary_database_all_backups(self, list_db_backups):

        try:
            for dbs in list_db_backups:
                self.__summary_core_size(list_db_backups)

        except Exception as e:
            self.__print_error("__summary_database_all_backups", e)

    ##########################################################################
    # Database db systems
    ##########################################################################
    def __summary_database_db_system(self, list_db_systems):

        try:
            for dbs in list_db_systems:
                nodes = 1
                # Db System
                if 'Exadata' not in dbs['sum_info']:
                    if 'node_count' in dbs:
                        if dbs['node_count'] is not None and dbs['node_count'] != 'None' and dbs['node_count'] != "":
                            nodes = dbs['node_count']

                    # add ocpus for DB
                    if 'cpu_core_count' in dbs:
                        if 'db_nodes' in dbs:
                            for dbnode in dbs['db_nodes']:
                                if 'cpu_core_count' in dbnode:
                                    if dbnode['lifecycle_state'] == 'STOPPED':
                                        self.summary_global_list.append({'type': 'Total Stopped OCPUs - VM/BM Database', 'size': float(dbnode['cpu_core_count'])})
                                    else:
                                        self.summary_global_list.append({'type': 'Total OCPUs - VM/BM Database', 'size': float(dbnode['cpu_core_count'])})

                # if Exa add Exadata CPUs
                else:
                    if 'cpu_core_count' in dbs:
                        self.summary_global_list.append({'type': 'Total OCPUs - ExaCS Database', 'size': float(dbs['cpu_core_count'])})
                        self.summary_global_list.append({'type': dbs['sum_info'] + " OCPUs", 'size': float(dbs['cpu_core_count'])})

                # add db to summary
                if dbs['lifecycle_state'] == 'STOPPED':
                    self.summary_global_list.append({'type': 'Stopped ' + dbs['sum_info'], 'size': float(nodes)})
                else:
                    self.summary_global_list.append({'type': dbs['sum_info'], 'size': float(nodes)})

                if dbs['sum_size_gb'] is not None:
                    if dbs['sum_size_gb'] != 'None' and dbs['sum_size_gb'] != "":
                        self.summary_global_list.append({'type': dbs['sum_info_storage'], 'size': float(dbs['sum_size_gb'])})

        except Exception as e:
            self.__print_error("__summary_database_db_system", e)

    ##########################################################################
    # Database Exadata
    ##########################################################################
    def __summary_database_db_exadata(self, list_exa):

        try:
            for dbs in list_exa:
                if not (dbs['lifecycle_state'] == 'TERMINATED' or dbs['lifecycle_state'] == 'DELETED'):
                    self.summary_global_list.append({'type': dbs['sum_info'] + " - Count", 'size': 1})

                for vm in dbs['vm_clusters']:
                    if 'cpu_core_count' in vm:
                        self.summary_global_list.append({'type': 'Total OCPUs - ExaCS Database', 'size': float(vm['cpu_core_count'])})
                        self.summary_global_list.append({'type': vm['sum_info'] + " OCPUs", 'size': float(vm['cpu_core_count'])})

                    # add db to summary
                    if dbs['lifecycle_state'] == 'STOPPED':
                        self.summary_global_list.append({'type': 'Stopped ' + vm['sum_info'], 'size': 1})
                    else:
                        self.summary_global_list.append({'type': vm['sum_info'], 'size': 1})

                    # db homes
                    for db_home in vm['db_homes']:
                        for db in db_home['databases']:
                            self.__summary_core_size(db['backups'])

                # adb vm clusters and containers
                for vm in dbs['adb_clusters']:
                    for ct in vm['containers']:
                        for db in ct['databases']:
                            if 'sum_info' in db and 'sum_count' in db:
                                self.summary_global_list.append({'type': "Total OCPUs - Autonomous Database", 'size': float(db['sum_count'])})
                                if float(db['sum_count']) == 0:
                                    self.summary_global_list.append({'type': db['sum_info_stopped'], 'size': 1})
                                else:
                                    self.summary_global_list.append({'type': db['sum_info_count'], 'size': 1})
                                    self.summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_count'])})

                            if 'sum_info_storage' in db and 'sum_size_tb' in db:
                                self.summary_global_list.append({'type': db['sum_info_storage'], 'size': float(db['sum_size_tb'])})

        except Exception as e:
            self.__print_error("__summary_database_db_exadata", e)

    ##########################################################################
    # Database Exascale
    ##########################################################################
    def __summary_database_db_exascale(self, list_exa):

        try:
            for dbs in list_exa:
                if not (dbs['lifecycle_state'] == 'TERMINATED' or dbs['lifecycle_state'] == 'DELETED'):
                    self.summary_global_list.append({'type': dbs['sum_info'] + " - Count", 'size': 1})

                for vm in dbs['vm_clusters']:
                    if 'enabled_e_cpu_count' in vm:
                        self.summary_global_list.append({'type': 'Total ECPUs - ExaScale Database', 'size': float(vm['enabled_e_cpu_count'])})
                        self.summary_global_list.append({'type': vm['sum_info'] + " ECPUs", 'size': float(vm['enabled_e_cpu_count'])})

                    # add db to summary
                    if dbs['lifecycle_state'] == 'STOPPED':
                        self.summary_global_list.append({'type': 'Stopped ' + vm['sum_info'], 'size': 1})
                    else:
                        self.summary_global_list.append({'type': vm['sum_info'], 'size': 1})

                    # db homes
                    for db_home in vm['db_homes']:
                        for db in db_home['databases']:
                            self.__summary_core_size(db['backups'])

        except Exception as e:
            self.__print_error("__summary_database_db_exascale", e)

    ##########################################################################
    # Database ExaCC
    ##########################################################################
    def __summary_database_db_exacc(self, list_exa):

        try:
            for dbs in list_exa:
                if not (dbs['lifecycle_state'] == 'TERMINATED' or dbs['lifecycle_state'] == 'DELETED'):
                    self.summary_global_list.append({'type': dbs['sum_info'] + " - Count", 'size': 1})

                for vm in dbs['vm_clusters']:
                    if 'cpus_enabled' in vm:
                        self.summary_global_list.append({'type': 'Total OCPUs - ExaCC Database', 'size': float(vm['cpus_enabled'])})
                        self.summary_global_list.append({'type': vm['sum_info'] + " OCPUs", 'size': float(vm['cpus_enabled'])})

                    # db homes
                    for db_home in vm['db_homes']:
                        for db in db_home['databases']:
                            self.__summary_core_size(db['backups'])

                # adb vm clusters and containers
                for vm in dbs['adb_clusters']:
                    for ct in vm['containers']:
                        for db in ct['databases']:
                            if 'sum_info' in db and 'sum_count' in db:
                                self.summary_global_list.append({'type': "Total OCPUs - Autonomous Database", 'size': float(db['sum_count'])})
                                if float(db['sum_count']) == 0:
                                    self.summary_global_list.append({'type': db['sum_info_stopped'], 'size': 1})
                                else:
                                    self.summary_global_list.append({'type': db['sum_info_count'], 'size': 1})
                                    self.summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_count'])})

                            if 'sum_info_storage' in db and 'sum_size_tb' in db:
                                self.summary_global_list.append({'type': db['sum_info_storage'], 'size': float(db['sum_size_tb'])})

        except Exception as e:
            self.__print_error("__summary_database_db_exacc", e)

    ##########################################################################
    # Database mysql db system
    ##########################################################################
    def __summary_database_mysql(self, mysqls):

        try:
            for mysql in mysqls:

                # add db to summary
                if mysql['lifecycle_state'] == 'STOPPED' or mysql['lifecycle_state'] == 'INACTIVE':
                    self.summary_global_list.append({'type': 'Stopped ' + mysql['sum_info'], 'size': 1})
                else:
                    self.summary_global_list.append({'type': mysql['sum_info'], 'size': 1})
                    self.summary_global_list.append({'type': 'Total OCPUs - Mysql Database', 'size': float(mysql['shape_ocpu'])})

                if mysql['data_storage_size_in_gbs'] is not None:
                    if mysql['data_storage_size_in_gbs'] != 'None' and mysql['data_storage_size_in_gbs'] != "":
                        self.summary_global_list.append({'type': mysql['sum_info_storage'], 'size': float(mysql['data_storage_size_in_gbs'])})

        except Exception as e:
            self.__print_error("__summary_database_mysql", e)

    ##########################################################################
    # Database postgresql db system
    ##########################################################################
    def __summary_database_postgresql(self, postgresqls):

        try:
            for pq in postgresqls:

                # add db to summary
                if pq['lifecycle_state'] == 'STOPPED' or pq['lifecycle_state'] == 'INACTIVE':
                    self.summary_global_list.append({'type': 'Stopped ' + pq['sum_info'], 'size': 1})
                else:
                    self.summary_global_list.append({'type': pq['sum_info'], 'size': 1})
                    self.summary_global_list.append({'type': 'Total OCPUs - PostgreSQL Database', 'size': float(pq['instance_ocpu_count'])})

        except Exception as e:
            self.__print_error("__summary_database_postgresql", e)

    ##########################################################################
    # __summary_database_goldengate
    ##########################################################################
    def __summary_database_goldengate(self, goldengates):

        try:
            if 'gg_deployments' in goldengates:
                for gg in goldengates['gg_deployments']:

                    # add db to summary
                    if gg['lifecycle_state'] == 'STOPPED' or gg['lifecycle_state'] == "INACTIVE":
                        self.summary_global_list.append({'type': 'Stopped ' + gg['sum_info'] + " (Count)", 'size': 1})
                    else:
                        self.summary_global_list.append({'type': 'Total OCPUs - Goldengate', 'size': float(gg['cpu_core_count'])})
                        self.summary_global_list.append({'type': gg['sum_info'] + " OCPUs", 'size': float(gg['cpu_core_count'])})
                        self.summary_global_list.append({'type': gg['sum_info'] + " (Count)", 'size': 1})

        except Exception as e:
            self.__print_error("__summary_database_goldengate", e)

    ##########################################################################
    # print self.__summary_core_compute_shape
    ##########################################################################
    def __summary_core_compute_instances(self, instances):

        try:
            if len(instances) == 0:
                return

            for instance in instances:
                if instance['lifecycle_state'] == "STOPPED":
                    self.summary_global_list.append({'type': ("Stopped " + instance['sum_info'] + " - " + instance['sum_shape']), 'size': float(1)})
                    if 'shape_ocpu' in instance:
                        self.summary_global_list.append({'type': 'Total Stopped OCPUs - Compute - All', 'size': float(instance['shape_ocpu'])})
                    if 'image_os' in instance:
                        if instance['image_os'] == "Windows":
                            self.summary_global_list.append({'type': 'Total Stopped OCPUs - Compute - Windows', 'size': float(instance['shape_ocpu'])})
                else:
                    self.summary_global_list.append({'type': (instance['sum_info'] + " - " + instance['sum_shape']), 'size': float(1)})
                    if 'shape_ocpu' in instance:
                        self.summary_global_list.append({'type': 'Total OCPUs - Compute - All', 'size': float(instance['shape_ocpu'])})
                    if 'image_os' in instance:
                        if instance['image_os'] == "Windows":
                            self.summary_global_list.append({'type': 'Total OCPUs - Compute - Windows', 'size': float(instance['shape_ocpu'])})

                if 'boot_volume' in instance:
                    self.__summary_core_size(instance['boot_volume'])

                if 'block_volume' in instance:
                    self.__summary_core_size(instance['block_volume'])

        except Exception as e:
            self.__print_error("__summary_core_compute_instances", e)

    ##########################################################################
    # sum core sizes
    ##########################################################################

    def __summary_core_size(self, objects, sum_info="sum_info", sum_size="sum_size_gb", add_info=""):
        try:
            if len(objects) == 0:
                return

            for obj in objects:
                if sum_info in obj and sum_size in obj:
                    if obj[sum_size] != '':
                        if float(obj[sum_size]) > 0:
                            self.summary_global_list.append({'type': add_info + obj[sum_info], 'size': float(obj[sum_size])})

        except Exception as e:
            self.__print_error("__summary_core_size", e)

    ##########################################################################
    # sum core count
    ##########################################################################
    def __summary_core_count(self, objects, object_name):
        try:
            if not objects:
                return

            if len(objects) == 0:
                return

            self.summary_global_list.append({'type': object_name, 'size': len(objects)})

        except Exception as e:
            self.__print_error("__summary_core_count", e)

    ##########################################################################
    # summary Compute
    ##########################################################################
    def __summary_core_compute_main(self, data):

        try:
            if len(data) == 0:
                return

            if 'instances' in data:
                self.__summary_core_compute_instances(data['instances'])

            if 'images' in data:
                self.__summary_core_size(data['images'])
                self.__summary_core_size(data['images'], "sum_count_info", "sum_count_size")

            if 'capacity_reservation' in data:
                self.__summary_core_size(data['capacity_reservation'])

            if 'boot_volume_backup' in data:
                self.__summary_core_size(data['boot_volume_backup'])

            if 'volume_group_backup' in data:
                self.__summary_core_size(data['volume_group_backup'])

            if 'volume_backup' in data:
                self.__summary_core_size(data['volume_backup'])

            if 'boot_not_attached' in data:
                self.__summary_core_size(data['boot_not_attached'])

            if 'volume_not_attached' in data:
                self.__summary_core_size(data['volume_not_attached'])

        except Exception as e:
            self.__print_error("__summary_core_compute_main", e)

    ##########################################################################
    # summary network
    ##########################################################################
    def __summary_core_network_main(self, data):

        try:
            if len(data) == 0:
                return

            if 'vcn' in data:
                self.__summary_core_count(data['vcn'], "Network VCN Count")
                for vcn in data['vcn']:
                    if 'data' in vcn:
                        dt = vcn['data']

                        # Subnets
                        if 'subnets' in dt:
                            self.__summary_core_count(dt['subnets'], "Network VCN Subnets")

                        # SGW
                        if 'sgw' in dt:
                            for sgw in dt['sgw']:
                                if 'services' in sgw:
                                    if 'Object Storage' in sgw['services']:
                                        self.summary_global_list.append({'type': "Network VCN Service Gateway Object Storage", 'size': 1})
                                    else:
                                        self.summary_global_list.append({'type': "Network VCN Service Gateway All Services", 'size': 1})

                        # IGW
                        if 'igw' in dt:
                            self.__summary_core_count(dt['igw'], "Network VCN Internet Gateways")

                        # NATGW
                        if 'nat' in dt:
                            for nat in dt['nat']:
                                if 'block_traffic' in nat:
                                    if 'True' in nat['block_traffic']:
                                        self.summary_global_list.append({'type': "Network VCN NAT Gateways Blocked", 'size': 1})
                                    else:
                                        self.summary_global_list.append({'type': "Network VCN NAT Gateways", 'size': 1})
                            self.__summary_core_count(dt['vlans'], "Network VCN VLANs")

                        # NSG
                        if 'security_groups' in dt:
                            self.__summary_core_count(dt['security_groups'], "Network VCN Security Groups")

                        # SL
                        if 'security_lists' in dt:
                            self.__summary_core_count(dt['security_lists'], "Network VCN Security Lists")

                        # RT
                        if 'route_tables' in dt:
                            self.__summary_core_count(dt['route_tables'], "Network VCN Route Tables")

                        # LPG
                        if 'local_peering' in dt:
                            for lpg in dt['local_peering']:
                                if 'peering_status' in lpg:
                                    if lpg['peering_status'] == "PEERED":
                                        self.summary_global_list.append({'type': "Network VCN LPGs Peered", 'size': 1})
                                    else:
                                        self.summary_global_list.append({'type': "Network VCN LPGs Not Peered", 'size': 1})

            # DRG
            if 'drg' in data:
                self.__summary_core_count(data['drg'], "Network DRG Count")

            # Network Firewall
            if 'network_firewall' in data:
                self.__summary_core_count(data['network_firewall'], "Network Firewall Count")

            if 'network_firewall_policies' in data:
                self.__summary_core_count(data['network_firewall_policies'], "Network Firewall Policies Count")

            # CPE
            if 'cpe' in data:
                self.__summary_core_count(data['cpe'], "Network CPEs")

            # IPSEC
            if 'ipsec' in data:
                for ipsec in data['ipsec']:
                    if 'tunnels' in ipsec:
                        for tunnel in ipsec['tunnels']:
                            if tunnel['status'] == "UP":
                                self.summary_global_list.append({'type': "Network DRG IPSEC Tunnels UP", 'size': 1})
                            else:
                                self.summary_global_list.append({'type': "Network DRG IPSEC Tunnels Down", 'size': 1})

            # VC
            if 'virtual_circuit' in data:
                for vc in data['virtual_circuit']:
                    if vc['bgp_session_state'] == "UP":
                        self.summary_global_list.append({'type': "Network DRG Circuits BGP UP", 'size': 1})
                    else:
                        self.summary_global_list.append({'type': "Network DRG Circuits BGP Down", 'size': 1})

            # RPG
            if 'remote_peering' in data:
                for rpg in data['remote_peering']:
                    if 'peering_status' in rpg:
                        if rpg['peering_status'] == "PEERED":
                            self.summary_global_list.append({'type': "Network DRG RPG Peered", 'size': 1})
                        else:
                            self.summary_global_list.append({'type': "Network DRG RPG Not Peered", 'size': 1})

        except Exception as e:
            self.__print_error("__summary_core_network_main", e)

    ##########################################################################
    # Summary Group By
    # took the function from stackoverflow
    ##########################################################################

    def __summary_group_by(self, key, list_of_dicts):

        try:
            d = {}
            for dct in list_of_dicts:
                if dct[key] not in d:
                    d[dct[key]] = {}
                for k, v in dct.items():
                    if k != key:
                        if k not in d[dct[key]]:
                            d[dct[key]][k] = v
                        else:
                            d[dct[key]][k] += v
            final_list = []
            for k, v in d.items():
                temp_d = {key: k}
                for k2, v2 in v.items():
                    temp_d[k2] = v2
                final_list.append(temp_d)
            return final_list

        except Exception as e:
            self.__print_error("__summary_group_by", e)

    ##########################################################################
    # Print summary  data
    ##########################################################################
    def __summary_print_results(self, data, header, header_size):

        try:

            if len(data) > 0:
                self.__summary_print_header(header, header_size)

                # sort and print
                for d in sorted(data, key=lambda i: i['type']):
                    print(d['type'].ljust(75, '.')[0:74] + str(round(d['size'])).rjust(10, '.'))

        except Exception as e:
            self.__print_error("__summary_print_results", e)

    ##########################################################################
    # Print summary Identity data
    ##########################################################################
    def __summary_region_data(self, region_name, data):

        try:
            if not data:
                return
            self.__summary_print_header("Summary - " + region_name, 0)
            self.summary_global_region_total = []
            region_data_exist = False

            # loop on compartments
            for cdata in data:
                self.summary_global_list = []

                compartment_header = ""

                if 'network' in cdata:
                    self.__summary_core_network_main(cdata['network'])
                if 'compute' in cdata:
                    self.__summary_core_compute_main(cdata['compute'])
                if 'database' in cdata:
                    self.__summary_database_main(cdata['database'])
                if 'object_storage' in cdata:
                    self.__summary_object_storage_main(cdata['object_storage'])
                if 'containers' in cdata:
                    self.__summary_container_main(cdata['containers'])
                if 'file_storage' in cdata:
                    self.__summary_file_storage_main(cdata['file_storage'])
                if 'load_balancer' in cdata:
                    self.__summary_load_balancer_main(cdata['load_balancer'])
                if 'network_load_balancer' in cdata:
                    self.__summary_load_balancer_main(cdata['network_load_balancer'])
                if 'paas_services' in cdata:
                    self.__summary_paas_services_main(cdata['paas_services'])
                if 'security' in cdata:
                    self.__summary_security(cdata['security'])
                if 'data_ai' in cdata:
                    self.__summary_data_ai_main(cdata['data_ai'])
                if 'edge' in cdata:
                    self.__summary_data_edge(cdata['edge'])

                # print compartment header if data in the global list
                if 'path' in cdata and self.summary_global_list:
                    compartment_header = "Summary - Compartment " + cdata['path']
                    region_data_exist = True

                # aggregate the data
                self.summary_global_list = self.__summary_group_by("type", self.summary_global_list)

                # print results compartment
                self.__summary_print_results(self.summary_global_list, compartment_header, 3)

                # append data to global and region
                self.summary_global_total.extend(self.summary_global_list)
                self.summary_global_region_total.extend(self.summary_global_list)

                # append data to global data
                self.summary_global_data.append({'region': region_name, 'compartment_name': cdata['path'], 'summary': self.summary_global_list})

            # If region data , aggregate the data, print and add to JSON
            if region_data_exist:
                self.summary_global_region_total = self.__summary_group_by("type", self.summary_global_region_total)
                self.summary_global_region_json[region_name] = self.summary_global_region_total
                self.__summary_print_results(self.summary_global_region_total, "Summary Region Total - " + region_name, 3)
            else:
                print("")
                print("No Summary data exist in this region")

        except Exception as e:
            self.__print_error("__summary_region_data", e)
            raise


##########################################################################
# This section has ShowOCICSV class
# it accept data as JSON format and compile CSV files
##########################################################################
class ShowOCICSV(object):

    ############################################
    # class variables
    ############################################
    error = 0
    error_array = []
    csv_tags_to_cols = False
    csv_file_header = ""
    csv_announcements = []
    csv_announcements_detailed = []
    csv_errors = []
    csv_resources = []
    csv_advisor_recommendations = []
    csv_advisor_resource_actions = []
    csv_functions_apps = []
    csv_functions_fns = []
    csv_certificates = []
    csv_certificate_ca_bundle = []
    csv_identity_compartments = []
    csv_identity_groups = []
    csv_identity_dynamic_groups = []
    csv_identity_groups_mapping = []
    csv_identity_users = []
    csv_identity_policies = []
    csv_identity_network_sources = []
    csv_identity_tag_namespaces = []
    csv_identity_domains = []
    csv_identity_domains_users = []
    csv_identity_domains_groups = []
    csv_identity_domains_dyngroups = []
    csv_identity_domains_kmsi_setting = []
    csv_identity_domains_password_policies = []
    csv_identity_domains_policies = []
    csv_identity_domains_rules = []
    csv_identity_domains_idps = []
    csv_identity_domains_auth_factors = []
    csv_identity_domains_network_perimeters = []
    csv_compute = []
    csv_block_volumes_not_attached = []
    csv_block_volumes = []
    csv_block_volumes_backups = []
    csv_compute_reservations = []
    csv_db_exascale_vaults = []
    csv_db_exascale_vmclusters = []
    csv_db_exacc_vmclusters = []
    csv_db_exa_infrastructure = []
    csv_db_exacs_vmclusters = []
    csv_db_vm_bm = []
    csv_db_all = []
    csv_db_autonomous = []
    csv_datasafe_targets = []
    csv_datasafe_audit_profiles = []
    csv_datasafe_audit_policies = []
    csv_datasafe_alert_profiles = []
    csv_datasafe_connectors = []
    csv_datasafe_user_assessment = []
    csv_datasafe_security_assessment = []
    csv_database = []
    csv_database_pdbs = []
    csv_database_backups = []
    csv_db_goldengate_deployments = []
    csv_db_nosql = []
    csv_db_mysql = []
    csv_db_mysql_backups = []
    csv_db_postgresql = []
    csv_fsdr = []
    csv_db_postgresql_backups = []
    csv_network_drg = []
    csv_network_drg_ipsec_tunnels = []
    csv_network_drg_virtual_circuits = []
    csv_network_vcn = []
    csv_network_subnet = []
    csv_network_subnet_prv_ips = []
    csv_network_security_list = []
    csv_network_security_group = []
    csv_network_routes = []
    csv_network_dhcp_options = []
    csv_network_firewall = []
    csv_network_firewall_policies = []
    csv_file_storage = []
    csv_load_balancer = []
    csv_load_balancer_listeners = []
    csv_load_balancer_bs = []
    csv_object_storage_buckets = []
    csv_security_bastions = []
    csv_security_logging = []
    csv_security_log_unified_agents = []
    csv_security_kms_vault = []
    csv_security_cloud_guard = []
    csv_container = []
    csv_container_nodepool = []
    csv_edge_waas_policies = []
    csv_edge_waf = []
    csv_edge_dns_steering_policies = []
    csv_edge_healthcheck = []
    csv_apigw = []
    csv_limits = []
    csv_paas_oac = []
    csv_paas_oic = []
    csv_paas_ocvs = []
    csv_paas_ocvs_clusters = []
    csv_paas_oce = []
    csv_paas_vb = []
    csv_paas_devops = []
    csv_paas_open_search = []
    csv_data_ai_oda = []
    csv_data_ai_bds = []
    csv_data_science = []
    csv_data_flow = []
    csv_data_catalog = []
    csv_data_integration = []
    csv_genai = []
    csv_genai_agent = []
    csv_genai_agent_kb = []
    csv_add_date_field = True
    csv_columns = []
    csv_streams_queues = []
    csv_monitor_agents = []
    csv_monitor_db_management = []
    csv_monitor_alarms = []
    csv_monitor_events = []
    csv_notifications = []
    csv_quotas = []
    start_time = ""
    tenant_id = ""
    tenant_name = ""

    ############################################
    # Init
    # accept start time as string
    ############################################
    def __init__(self, start_time):
        self.start_time = start_time

    ##########################################################################
    # get errors
    ##########################################################################
    def get_errors(self):
        return self.error

    ##########################################################################
    # __add_to_error_array
    ##########################################################################
    def __add_to_error_array(self, classname, caller_function, compartment_name, err, warning=False):

        try:
            error_info = {
                'class': classname,
                'function': caller_function,
                'compartment': compartment_name,
                'error': str(err),
                'is_warning': str(warning)
            }
            self.error_array.append(error_info)

        except Exception as e:
            print("\nError in __add_to_error_array " + str(e))

    ##########################################################################
    # __csv_list_to_str
    ##########################################################################
    def __csv_list_to_str(self, v_list, attr=None):
        try:
            if not v_list or not isinstance(v_list, (list, tuple)):
                return ''

            if attr:
                return str(', '.join(x[attr] for x in v_list))
            else:
                return str(', '.join(x for x in v_list))

        except Exception as e:
            self.__print_error("__csv_list_to_str" + (" ATTR='" + attr + "'" if attr else ""), e)

    ##########################################################################
    # generate_csv
    ##########################################################################
    def generate_csv(self, data, csv_file_header, tenancy, add_date_field=True, csv_columns=""):
        self.csv_add_date_field = add_date_field
        self.csv_file_header = csv_file_header
        self.csv_columns = str(csv_columns).split(",")
        self.tenant_id = str(tenancy['id'])[-6:]
        self.tenant_name = str(tenancy['name'])
        try:
            for d in data:
                if 'type' in d:

                    if d['type'] == "identity":
                        self.__csv_identity_main(d['data'])

                    elif d['type'] == "errors":
                        self.__csv_error_data(d['data'])

                    elif d['type'] == "announcement":
                        self.__csv_announcements(d['data'])

                    elif d['type'] == "region":
                        self.__csv_region_data(d['region'], d['data'])

                        if 'limits' in d:
                            self.__csv_limits_main(d['region'], d['limits'])
                    else:
                        continue

            # Run again for the error csv
            for d in data:
                if 'type' in d:
                    if d['type'] == "errors":
                        self.__csv_error_data(d['data'])

            # generate CSV files from each file
            self.__print_header("Processing CSV Files", 0)
            self.__export_to_csv_file("all_resources", self.csv_resources)
            self.__export_to_csv_file("announcements", self.csv_announcements)
            self.__export_to_csv_file("announcements_detailed", self.csv_announcements_detailed)
            self.__export_to_csv_file("errors", self.csv_errors)

            self.__export_to_csv_file("advisor_recommendations", self.csv_advisor_recommendations)
            self.__export_to_csv_file("advisor_resource_actions", self.csv_advisor_resource_actions)

            self.__export_to_csv_file("identity_compartments", self.csv_identity_compartments)
            self.__export_to_csv_file("identity_users", self.csv_identity_users)
            self.__export_to_csv_file("identity_network_sources", self.csv_identity_network_sources)
            self.__export_to_csv_file("identity_policy", self.csv_identity_policies)
            self.__export_to_csv_file("identity_groups", self.csv_identity_groups)
            self.__export_to_csv_file("identity_dynamic_groups", self.csv_identity_dynamic_groups)
            self.__export_to_csv_file("identity_groups_mapping", self.csv_identity_groups_mapping)
            self.__export_to_csv_file("identity_tag_namespaces", self.csv_identity_tag_namespaces)

            self.__export_to_csv_file("identity_domains", self.csv_identity_domains)
            self.__export_to_csv_file("identity_domains_users", self.csv_identity_domains_users)
            self.__export_to_csv_file("identity_domains_groups", self.csv_identity_domains_groups)
            self.__export_to_csv_file("identity_domains_dyngroup", self.csv_identity_domains_dyngroups)
            self.__export_to_csv_file("identity_domains_kmsi", self.csv_identity_domains_kmsi_setting)
            self.__export_to_csv_file("identity_domains_idps", self.csv_identity_domains_idps)
            self.__export_to_csv_file("identity_domains_auth", self.csv_identity_domains_auth_factors)
            self.__export_to_csv_file("identity_domains_pwd_policies", self.csv_identity_domains_password_policies)
            self.__export_to_csv_file("identity_domains_policies", self.csv_identity_domains_policies)
            self.__export_to_csv_file("identity_domains_rules", self.csv_identity_domains_rules)
            self.__export_to_csv_file("identity_domains_net_perimeter", self.csv_identity_domains_network_perimeters)

            self.__export_to_csv_file("functions_apps", self.csv_functions_apps)
            self.__export_to_csv_file("functions_fns", self.csv_functions_fns)
            self.__export_to_csv_file("compute", self.csv_compute)
            self.__export_to_csv_file("compute_reservations", self.csv_compute_reservations)
            self.__export_to_csv_file("block_volumes", self.csv_block_volumes)
            self.__export_to_csv_file("block_volumes_backups", self.csv_block_volumes_backups)
            self.__export_to_csv_file("block_volumes_not_attached", self.csv_block_volumes_not_attached)
            self.__export_to_csv_file("network_vcn", self.csv_network_vcn)
            self.__export_to_csv_file("network_subnet", self.csv_network_subnet)
            self.__export_to_csv_file("network_subnet_prv_ips", self.csv_network_subnet_prv_ips)
            self.__export_to_csv_file("network_drgs", self.csv_network_drg)
            self.__export_to_csv_file("network_drg_ipsec_tunnels", self.csv_network_drg_ipsec_tunnels)
            self.__export_to_csv_file("network_drg_virtual_circuits", self.csv_network_drg_virtual_circuits)
            self.__export_to_csv_file("network_routes", self.csv_network_routes)
            self.__export_to_csv_file("network_security_list", self.csv_network_security_list)
            self.__export_to_csv_file("network_security_group", self.csv_network_security_group)
            self.__export_to_csv_file("network_dhcp_options", self.csv_network_dhcp_options)
            self.__export_to_csv_file("network_firewalls", self.csv_network_firewall)
            self.__export_to_csv_file("network_firewalls_policies", self.csv_network_firewall_policies)
            self.__export_to_csv_file("database", self.csv_database)
            self.__export_to_csv_file("database_backups", self.csv_database_backups)
            self.__export_to_csv_file("database_autonomous", self.csv_db_autonomous)
            self.__export_to_csv_file("database_db_pdbs", self.csv_database_pdbs)
            self.__export_to_csv_file("database_db_all", self.csv_db_all)
            self.__export_to_csv_file("database_db_vm_bm", self.csv_db_vm_bm)
            self.__export_to_csv_file("database_db_exa_infra", self.csv_db_exa_infrastructure)
            self.__export_to_csv_file("database_db_exascale_vaults", self.csv_db_exascale_vaults)
            self.__export_to_csv_file("database_db_exascale", self.csv_db_exascale_vmclusters)
            self.__export_to_csv_file("database_db_exacs", self.csv_db_exacs_vmclusters)
            self.__export_to_csv_file("database_db_exacc", self.csv_db_exacc_vmclusters)
            self.__export_to_csv_file("database_goldengate_deployments", self.csv_db_goldengate_deployments)
            self.__export_to_csv_file("database_mysql", self.csv_db_mysql)
            self.__export_to_csv_file("database_mysql_backups", self.csv_db_mysql_backups)
            self.__export_to_csv_file("database_postgresql", self.csv_db_postgresql)
            self.__export_to_csv_file("database_postgresql_backups", self.csv_db_postgresql_backups)
            self.__export_to_csv_file("database_nosql", self.csv_db_nosql)

            self.__export_to_csv_file("datasafe_targets", self.csv_datasafe_targets)
            self.__export_to_csv_file("datasafe_audit_policies", self.csv_datasafe_audit_policies)
            self.__export_to_csv_file("datasafe_audit_profiles", self.csv_datasafe_audit_profiles)
            self.__export_to_csv_file("datasafe_alert_profiles", self.csv_datasafe_alert_profiles)
            self.__export_to_csv_file("datasafe_connectors", self.csv_datasafe_connectors)
            self.__export_to_csv_file("datasafe_user_assessment", self.csv_datasafe_user_assessment)
            self.__export_to_csv_file("datasafe_security_assessment", self.csv_datasafe_security_assessment)

            self.__export_to_csv_file("load_balancers", self.csv_load_balancer)
            self.__export_to_csv_file("load_balancer_listeners", self.csv_load_balancer_listeners)
            self.__export_to_csv_file("load_balancer_backendset", self.csv_load_balancer_bs)
            self.__export_to_csv_file("file_storage", self.csv_file_storage)
            self.__export_to_csv_file("fsdr", self.csv_fsdr)
            self.__export_to_csv_file("api_gateways", self.csv_apigw)
            self.__export_to_csv_file("limits", self.csv_limits)
            self.__export_to_csv_file("quotas", self.csv_quotas)
            self.__export_to_csv_file("object_storage_buckets", self.csv_object_storage_buckets)
            self.__export_to_csv_file("security_bastions", self.csv_security_bastions)
            self.__export_to_csv_file("security_loggings", self.csv_security_logging)
            self.__export_to_csv_file("security_log_unified_agents", self.csv_security_log_unified_agents)
            self.__export_to_csv_file("security_cloud_guards", self.csv_security_cloud_guard)
            self.__export_to_csv_file("security_kms_vaults", self.csv_security_kms_vault)
            self.__export_to_csv_file("containers", self.csv_container)
            self.__export_to_csv_file("containers_nodepools", self.csv_container_nodepool)
            self.__export_to_csv_file("edge_dns_steering_policies", self.csv_edge_dns_steering_policies)
            self.__export_to_csv_file("edge_waas_policies", self.csv_edge_waas_policies)
            self.__export_to_csv_file("edge_web_application_firewall", self.csv_edge_waf)
            self.__export_to_csv_file("edge_healthchecks", self.csv_edge_healthcheck)
            self.__export_to_csv_file("paas_oac", self.csv_paas_oac)
            self.__export_to_csv_file("paas_oic", self.csv_paas_oic)
            self.__export_to_csv_file("paas_ocvs_vmware", self.csv_paas_ocvs)
            self.__export_to_csv_file("paas_ocvs_clusters", self.csv_paas_ocvs_clusters)
            self.__export_to_csv_file("paas_oce", self.csv_paas_oce)
            self.__export_to_csv_file("paas_devops", self.csv_paas_devops)
            self.__export_to_csv_file("paas_visualbuilder", self.csv_paas_vb)
            self.__export_to_csv_file("paas_opensearch", self.csv_paas_open_search)
            self.__export_to_csv_file("data_science", self.csv_data_science)
            self.__export_to_csv_file("data_flow", self.csv_data_flow)
            self.__export_to_csv_file("data_catalog", self.csv_data_catalog)
            self.__export_to_csv_file("data_integration", self.csv_data_integration)
            self.__export_to_csv_file("digital_assistance", self.csv_data_ai_oda)
            self.__export_to_csv_file("big_data_service", self.csv_data_ai_bds)
            self.__export_to_csv_file("monitor_agents", self.csv_monitor_agents)
            self.__export_to_csv_file("monitor_db_managements", self.csv_monitor_db_management)
            self.__export_to_csv_file("monitor_alarms", self.csv_monitor_alarms)
            self.__export_to_csv_file("monitor_events", self.csv_monitor_events)
            self.__export_to_csv_file("monitor_topics_subs", self.csv_notifications)
            self.__export_to_csv_file("streams_queues", self.csv_streams_queues)

            self.__export_to_csv_file("certificates", self.csv_certificates)
            self.__export_to_csv_file("certificates_ca_bundles", self.csv_certificate_ca_bundle)

            self.__export_to_csv_file("genai", self.csv_genai)
            self.__export_to_csv_file("genai_agent", self.csv_genai_agent)
            self.__export_to_csv_file("genai_agent_kb", self.csv_genai_agent_kb)

            print("")
        except Exception as e:
            raise Exception("Error in generate_csv: " + str(e.args))

    ##########################################################################
    # Print header centered
    ##########################################################################
    def __print_header(self, name, category):
        options = {0: 90, 1: 60, 2: 30, 3: 75}
        chars = int(options[category])
        print("")
        print('#' * chars)
        print("#" + name.center(chars - 2, " ") + "#")
        print('#' * chars)

    #######################################
    # get key in order                    #
    #######################################
    def get_all_keys_in_order(self, list_of_dicts):
        try:
            ordered_keys = []
            for dict_ in list_of_dicts:
                for key in dict_:
                    if key not in ordered_keys:
                        ordered_keys.append(key)
            return ordered_keys
        except Exception as e:
            raise Exception("Error in get_all_keys_in_order: " + str(e.args))

    #######################################
    # extract_tags_to_columns             #
    #######################################
    def extract_tags_to_columns(self, list_of_dicts):
        try:
            new_result = []
            for row in list_of_dicts:
                for tag_type in ['defined_tags', 'freeform_tags']:
                    if tag_type in row:
                        tags = row[tag_type].split(', ')
                        for tag in tags:
                            tag_split = tag.split("=")
                            if len(tag_split) > 1:
                                key_value = 'Tag_' + tag_split[0]
                                data_value = tag_split[1]
                                row.update({key_value: data_value})
                # Append the row
                new_result.append(row)
            return new_result
        except Exception as e:
            raise Exception("Error in extract_tags_to_columns: " + str(e.args))

    ##########################################################################
    # create csv file
    ##########################################################################
    def __export_to_csv_file(self, file_subject, data):

        try:
            # if no data
            if len(data) == 0:
                return

            # get the file name of the CSV
            file_name = self.csv_file_header + "_" + file_subject + ".csv"
            tenant_dict = {'tenant_name': self.tenant_name, 'tenant_id': self.tenant_id}

            # add start_date to each dictionary
            result = []
            if self.csv_add_date_field:
                result = [dict(list(tenant_dict.items()) + list(item.items()), extract_date=self.start_time) for item in data]
            else:
                result = [dict(list(tenant_dict.items()) + list(item.items())) for item in data]

            # if convert tags to cols
            if self.csv_tags_to_cols:
                result = self.extract_tags_to_columns(result)

            # generate fields
            fields = self.get_all_keys_in_order(result)

            with open(file_name, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fields)

                # write header
                writer.writeheader()

                for row in result:
                    writer.writerow(row)

            print("CSV: " + file_subject.ljust(35) + " --> " + file_name)

        except Exception as e:
            raise Exception("Error in __export_to_csv_file: " + str(e.args))

    ##########################################################################
    # print error
    ##########################################################################
    def __print_error(self, msg, e):
        try:

            classname = type(self).__name__
            caller_function = sys._getframe(2).f_code.co_name + ":" + sys._getframe(1).f_code.co_name
            self.error += 1
            if isinstance(e, KeyError):
                print("\nError in " + classname + ":" + caller_function + ":" + msg + ": KeyError " + str(e.args))
            else:
                print("\nError in " + classname + ":" + caller_function + ":" + msg + ": " + str(e))

            self.__add_to_error_array(classname, caller_function, "", e)

        except Exception as e:
            print("\nError in __print_error " + str(e))

    ##########################################################################
    # extract defined tags to string
    ##########################################################################
    def __get_defined_tags(self, defined_tags):

        try:
            if not defined_tags:
                return ""

            defarr = []
            for namespace in defined_tags.keys():
                for key in defined_tags[namespace].keys():
                    defarr.append(namespace + "." + key + "=" + defined_tags[namespace][key])
            return str(', '.join(x for x in defarr))

        except Exception as e:
            self.__print_error("__get_defined_tags", e)

    ##########################################################################
    # extract defined tags value
    ##########################################################################
    def __get_defined_tags_key_value(self, defined_tags, namespace_and_key):

        try:
            if not defined_tags or '.' not in namespace_and_key:
                return ""

            namespace = namespace_and_key.split(".")[0]
            key = namespace_and_key.split(".")[1]

            if namespace not in defined_tags.keys():
                return ""

            if key not in defined_tags[namespace].keys():
                return ""

            return defined_tags[namespace][key]

        except Exception as e:
            self.__print_error("__get_defined_tags_key_value", e)

    ##########################################################################
    # extract freeform tags
    ##########################################################################
    def __get_freeform_tags(self, freeform_tag):

        try:
            if not freeform_tag:
                return ""

            return str(', '.join(key + "=" + freeform_tag[key] for key in freeform_tag.keys()))

        except Exception as e:
            self.__print_error("__get_freeform_tags", e)

    ##########################################################################
    # check if managed paas compartment
    ##########################################################################
    def __if_managed_paas_compartment(self, name):
        return name == "ManagedCompartmentForPaaS"

    ##########################################################################
    # Add to Service
    ##########################################################################
    def __csv_add_service(self, arr, service_type, col_name="name", col_id="id", col_info="info"):

        try:
            if col_name not in arr:
                if 'display_name' in arr:
                    col_name = 'display_name'

            self.csv_resources.append({
                'resource_type': service_type,
                'region_name': arr['region_name'] if 'region_name' in arr else "",
                'availability_domain': arr['availability_domain'] if 'availability_domain' in arr else "",
                'compartment_name': arr['compartment_name'] if 'compartment_name' in arr else "",
                'compartment_path': arr['compartment_path'] if 'compartment_path' in arr else "",
                'resource_id': arr[col_id] if col_id in arr else "",
                'resource_name': arr[col_name] if col_name in arr else "",
                'resource_info': arr[col_info] if col_info in arr else "",
                'freeform_tags': arr['freeform_tags'] if 'freeform_tags' in arr else "",
                'defined_tags': arr['defined_tags'] if 'defined_tags' in arr else ""
            })

        except Exception as e:
            self.__print_error("__csv_add_service", e)

    ##########################################################################
    # CSV Identity Groups
    ##########################################################################

    def __csv_identity_groups(self, groups):
        try:
            for group in groups:
                for user in group['users'].split(','):

                    data = {'group_name': group['name'], 'user_name': user}

                    self.csv_identity_groups.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_groups", e)

    ##########################################################################
    # CSV Identity Groups
    ##########################################################################

    def __csv_identity_dynamic_groups(self, groups):
        try:
            for group in groups:
                data = {
                    'id': group['id'],
                    'name': group['name'],
                    'description': group['description'],
                    'matching_rule': group['matching_rule']
                }

                self.csv_identity_dynamic_groups.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_dynamic_groups", e)

    ##########################################################################
    # CSV Identity Groups Mapping
    ##########################################################################
    def __csv_identity_groups_mapping(self, groups_mapping):
        try:
            for grp in groups_mapping:

                data = {
                    'provider_id': grp['provider_id'],
                    'provider_name': grp['provider_name'],
                    'lifecycle_state': grp['lifecycle_state'],
                    'provider_group_name': grp['provider_group_name'],
                    'domain_name': grp['domain_name'],
                    'oci_group_id': grp['oci_group_id'],
                    'oci_group_name': grp['oci_group_name'],
                    'time_created': grp['time_created'],
                    'id': grp['id']
                }

                self.csv_identity_groups_mapping.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_groups_mapping", e)

    ##########################################################################
    # CSV Identity Users
    ##########################################################################

    def __csv_identity_users(self, users):
        try:
            for user in users:
                data = {
                    'id': user['id'],
                    'user_name': user['name'],
                    'description': user['description'],
                    'email': user['email'],
                    'is_mfa_activated': user['is_mfa_activated'],
                    'lifecycle_state': user['lifecycle_state'],
                    'identity_provider_name': user['identity_provider_name'],
                    'identity_provider_id': user['identity_provider_id'],
                    'external_identifier': user['external_identifier'],
                    'user_time_created': user['time_created'],
                    'groups': user['groups'],
                    'api_keys': "",
                    'auth_token': "",
                    'secret_key': "",
                    'smtp_cred': "",
                    'last_successful_login_time': user['last_successful_login_time'],
                    'previous_successful_login_time': user['previous_successful_login_time']
                }

                capabilities = user['capabilities']
                for k in capabilities:
                    data[k] = capabilities[k]

                # Check if credential exist
                if 'api_keys' in user:
                    if user['api_keys']:
                        data['api_keys'] = str(', '.join(x['id'] + " - " + x['lifecycle_state'] + " - " + x['time_created'] for x in user['api_keys']))
                if 'auth_token' in user:
                    if data['auth_token']:
                        data['auth_token'] = str(', '.join(x['id'] + " - " + x['description'] + " - " + x['time_created'] for x in user['auth_token']))
                if 'secret_key' in user:
                    if data['secret_key']:
                        data['secret_key'] = str(', '.join(x['id'] + " - " + x['display_name'] + " - " + x['time_created'] for x in user['secret_key']))
                if 'smtp_cred' in user:
                    if data['smtp_cred']:
                        data['smtp_cred'] = str(', '.join(x['id'] + " - " + x['description'] + " - " + x['time_created'] for x in user['smtp_cred']))

                self.csv_identity_users.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_users", e)

    ##########################################################################
    # CSV Identity Domains
    ##########################################################################

    def __csv_identity_domains(self, domains):
        try:
            for var in domains:
                data = {
                    'id': var['id'],
                    'display_name': var['display_name'],
                    'description': var['description'],
                    'url': var['url'],
                    'home_region_url': var['home_region_url'],
                    'home_region': var['home_region'],
                    'type': var['type'],
                    'license_type': var['license_type'],
                    'is_hidden_on_login': var['is_hidden_on_login'],
                    'time_created': var['time_created'],
                    'lifecycle_state': var['lifecycle_state'],
                    'freeform_tags': self.__get_freeform_tags(var['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(var['defined_tags']),
                    'replica_regions': var['replica_regions'],
                    'users': len(var['users']) if var['users'] else 0,
                    'groups': len(var['groups']) if var['groups'] else 0,
                    'dynamic_groups': len(var['dynamic_groups']) if var['dynamic_groups'] else 0,
                    'kmsi_setting': len(var['kmsi_setting']) if var['kmsi_setting'] else 0,
                    'identity_providers': len(var['identity_providers']) if var['identity_providers'] else 0,
                    'authentication_factor_settings': len(var['authentication_factor_settings']) if var['authentication_factor_settings'] else 0,
                    'compartment_id': var['compartment_id'],
                    'compartment_path': var['compartment_path'],
                    'compartment_name': var['compartment_name']
                }
                self.csv_identity_domains.append(data)

                # Extract the rest of the data
                if 'users' in var and var['users']:
                    self.__csv_identity_domains_users(var['users'], var['display_name'], var['id'])

                if 'groups' in var and var['groups']:
                    self.__csv_identity_domains_groups(var['groups'], var['display_name'], var['id'])

                if 'dynamic_groups' in var and var['dynamic_groups']:
                    self.__csv_identity_domains_dynamic_groups(var['dynamic_groups'], var['display_name'], var['id'])

                if 'identity_providers' in var and var['identity_providers']:
                    self.__csv_identity_domains_idps(var['identity_providers'], var['display_name'], var['id'])

                if 'network_perimeters' in var and var['network_perimeters']:
                    self.__csv_identity_domains_network_perimeters(var['network_perimeters'], var['display_name'], var['id'])

                if 'kmsi_setting' in var and var['kmsi_setting']:
                    self.__csv_identity_domains_kmsi_setting(var['kmsi_setting'], var['display_name'], var['id'])

                if 'authentication_factor_settings' in var and var['authentication_factor_settings']:
                    self.__csv_identity_domains_auth_factor(var['authentication_factor_settings'], var['display_name'], var['id'])

                if 'password_policies' in var and var['password_policies']:
                    self.__csv_identity_domains_password_policies(var['password_policies'], var['display_name'], var['id'])

                if 'policies' in var and var['policies']:
                    self.__csv_identity_domains_policies(var['policies'], var['display_name'], var['id'])

                if 'rules' in var and var['rules']:
                    self.__csv_identity_domains_rules(var['rules'], var['display_name'], var['id'])

        except Exception as e:
            self.__print_error("__csv_identity_domains", e)

    ##########################################################################
    # CSV Identity Domains Users
    ##########################################################################

    def __csv_identity_domains_users(self, users, domain_name, domain_id):
        try:
            for var in users:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'display_name': var['display_name'],
                    'compartment_ocid': var['compartment_ocid'],
                    'external_id': var['external_id'],
                    'user_name': var['user_name'],
                    'description': var['description'],
                    'nick_name': var['nick_name'],
                    'title': var['title'],
                    'user_type': var['user_type'],
                    'locale': var['locale'],
                    'preferred_language': var['preferred_language'],
                    'timezone': var['timezone'],
                    'active': var['active'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'family_name': var['family_name'],
                    'given_name': var['given_name'],
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'freeform_tags': self.__get_freeform_tags(var['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(var['defined_tags']),
                    'phone_numbers': self.__csv_list_to_str(var['phone_numbers']),
                    'ims': self.__csv_list_to_str(var['ims']),
                    'emails': self.__csv_list_to_str(var['emails']),
                    'entitlements': self.__csv_list_to_str(var['entitlements']),
                    'x509_certificates': self.__csv_list_to_str(var['x509_certificates']),
                    'groups': self.__csv_list_to_str(var['groups'], 'display'),
                    'groups_ids': self.__csv_list_to_str(var['groups'], 'ocid'),
                    'is_federated_user': var['ext_user']['is_federated_user'],
                    'is_authentication_delegated': var['ext_user']['is_authentication_delegated'],
                    'status': var['ext_user']['status'],
                    'provider': var['ext_user']['provider'],
                    'creation_mechanism': var['ext_user']['creation_mechanism'],
                    'do_not_show_getting_started': var['ext_user']['do_not_show_getting_started'],
                    'bypass_notification': var['ext_user']['bypass_notification'],
                    'is_account_recovery_enrolled': var['ext_user']['is_account_recovery_enrolled'],
                    'account_recovery_required': var['ext_user']['account_recovery_required'],
                    'user_flow_controlled_by_external_client': var['ext_user']['user_flow_controlled_by_external_client'],
                    'is_group_membership_normalized': var['ext_user']['is_group_membership_normalized'],
                    'is_group_membership_synced_to_users_groups': var['ext_user']['is_group_membership_synced_to_users_groups'],
                    'password_last_successful_set_date': var['ext_password']['last_successful_set_date'],
                    'password_cant_change': var['ext_password']['cant_change'],
                    'password_cant_expire': var['ext_password']['cant_expire'],
                    'password_must_change': var['ext_password']['must_change'],
                    'password_expired': var['ext_password']['expired'],
                    'password_last_successful_validation_date': var['ext_password']['last_successful_validation_date'],
                    'password_last_failed_validation_date': var['ext_password']['last_failed_validation_date'],
                    'password_applicable_password_policy': var['ext_password']['applicable_password_policy'],
                    'password_last_successful_login_date': var['ext_user_state']['last_successful_login_date'],
                    'state_previous_successful_login_date': var['ext_user_state']['previous_successful_login_date'],
                    'state_last_failed_login_date': var['ext_user_state']['last_failed_login_date'],
                    'state_login_attempts': var['ext_user_state']['login_attempts'],
                    'state_recovery_attempts': var['ext_user_state']['recovery_attempts'],
                    'state_recovery_enroll_attempts': var['ext_user_state']['recovery_enroll_attempts'],
                    'state_max_concurrent_sessions': var['ext_user_state']['max_concurrent_sessions'],
                    'state_recovery_locked_date': var['ext_user_state']['recovery_locked_date'],
                    'state_recovery_locked_on': var['ext_user_state']['recovery_locked_on'],
                    'state_locked_date': var['ext_user_state']['locked_date'],
                    'state_locked_expired': var['ext_user_state']['locked_expired'],
                    'state_locked_on': var['ext_user_state']['locked_on'],
                    'state_locked_reason': var['ext_user_state']['locked_reason'],
                    'mfa_preferred_authentication_factor': var['ext_mfa']['preferred_authentication_factor'],
                    'mfa_status': var['ext_mfa']['mfa_status'],
                    'mfa_preferred_third_party_vendor': var['ext_mfa']['preferred_third_party_vendor'],
                    'mfa_preferred_authentication_method': var['ext_mfa']['preferred_authentication_method'],
                    'mfa_login_attempts': var['ext_mfa']['login_attempts'],
                    'mfa_enabled_on': var['ext_mfa']['mfa_enabled_on'],
                    'mfa_ignored_apps': var['ext_mfa']['mfa_ignored_apps'],
                    'posix_uid_number': var['ext_posix']['uid_number'],
                    'posix_gid_number': var['ext_posix']['gid_number'],
                    'posix_gecos': var['ext_posix']['gecos'],
                    'posix_home_directory': var['ext_posix']['home_directory'],
                    'posix_login_shell': var['ext_posix']['login_shell'],
                    'risk_level': var['ext_adaptive']['risk_level'],
                    'risk_scores': var['ext_adaptive']['risk_scores'],
                    'db_is_db_user': var['ext_db_user']['is_db_user'],
                    'db_domain_level_schema': var['ext_db_user']['domain_level_schema'],
                    'db_instance_level_schema': var['ext_db_user']['instance_level_schema'],
                    'db_global_roles': var['ext_db_user']['db_global_roles'],
                    'db_user_name': var['ext_db_user_credential']['db_user_name'],
                    'db_login_attempts': var['ext_db_user_credential']['db_login_attempts'],
                    'can_use_api_keys': var['ext_capabilities']['can_use_api_keys'],
                    'can_use_auth_tokens': var['ext_capabilities']['can_use_auth_tokens'],
                    'can_use_console_password': var['ext_capabilities']['can_use_console_password'],
                    'can_use_customer_secret_keys': var['ext_capabilities']['can_use_customer_secret_keys'],
                    'can_use_o_auth2_client_credentials': var['ext_capabilities']['can_use_o_auth2_client_credentials'],
                    'can_use_smtp_credentials': var['ext_capabilities']['can_use_smtp_credentials'],
                    'can_use_db_credentials': var['ext_capabilities']['can_use_db_credentials'],
                    'roles': str(', '.join(x['value'] + ":" + x['type'] for x in var['roles'])),
                    'api_keys': str(', '.join(x['ocid'] + ":" + x['time_created'] for x in var['api_keys'])),
                    'customer_secret_keys': str(', '.join(x['ocid'] + ":" + x['time_created'] for x in var['customer_secret_keys'])),
                    'auth_tokens': str(', '.join(x['ocid'] + ":" + x['time_created'] for x in var['auth_tokens'])),
                    'smtp_credentials': str(', '.join(x['ocid'] + ":" + x['time_created'] for x in var['smtp_credentials'])),
                    'o_auth2_client_credentials': str(', '.join(x['ocid'] + ":" + x['time_created'] for x in var['o_auth2_client_credentials'])),
                    'db_credentials': str(', '.join(x['ocid'] + ":" + x['time_created'] for x in var['db_credentials'])),
                    'allow_self_change': var['allow_self_change']
                }

                self.csv_identity_domains_users.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_users", e)

    ##########################################################################
    # CSV Identity Domain Groups
    ##########################################################################

    def __csv_identity_domains_groups(self, groups, domain_name, domain_id):
        try:
            for var in groups:
                members = "Over 200 members" if len(var['members']) > 200 else self.__csv_list_to_str(var['members'], 'name')
                members_ids = "Over 200 members" if len(var['members']) > 200 else self.__csv_list_to_str(var['members'], 'ocid')
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'display_name': var['display_name'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'compartment_ocid': var['compartment_ocid'],
                    'external_id': var['external_id'],
                    'non_unique_display_name': var['non_unique_display_name'],
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'freeform_tags': self.__get_freeform_tags(var['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(var['defined_tags']),
                    'members': members,
                    'members_ids': members_ids,
                    'description': var['ext_group']['description'],
                    'creation_mechanism': var['ext_group']['creation_mechanism'],
                    'password_policy': var['ext_group']['password_policy'],
                    'synced_from_app': var['ext_group']['synced_from_app'],
                    'grants': var['ext_group']['grants'],
                    'owners': var['ext_group']['owners'],
                    'app_roles': var['ext_group']['app_roles'],
                    'db_instance_level_schema_names': var['ext_dbcs_group']['instance_level_schema_names'],
                    'db_domain_level_schema_names': var['ext_dbcs_group']['domain_level_schema_names'],
                    'db_domain_level_schema': var['ext_dbcs_group']['domain_level_schema'],
                    'db_instance_level_schema': var['ext_dbcs_group']['instance_level_schema'],
                    'dg_membership_type': var['ext_dynamic_group']['membership_type'],
                    'dg_membership_rule': var['ext_dynamic_group']['membership_rule'],
                    'gid_number': var['gid_number'],
                    'requestable_group': var['requestable_group']
                }

                self.csv_identity_domains_groups.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_groups", e)

    ##########################################################################
    # CSV Identity Domain Dynamic Groups
    ##########################################################################

    def __csv_identity_domains_dynamic_groups(self, groups, domain_name, domain_id):
        try:
            for var in groups:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'matching_rule': var['matching_rule'],
                    'description': var['description'],
                    'display_name': var['display_name'],
                    'grants': self.__csv_list_to_str(var['grants'], 'value'),
                    'dynamic_group_app_roles': self.__csv_list_to_str(var['dynamic_group_app_roles'], 'value'),
                    'freeform_tags': self.__get_freeform_tags(var['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(var['defined_tags'])
                }

                self.csv_identity_domains_dyngroups.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_dynamic_groups", e)

    ##########################################################################
    # CSV Identity Domain Dynamic Groups
    ##########################################################################

    def __csv_identity_domains_network_perimeters(self, network_perimeters, domain_name, domain_id):
        try:
            for var in network_perimeters:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'name': var['name'],
                    'description': var['description'],
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'ip_addresses': self.__csv_list_to_str(var['ip_addresses'], 'value')
                }

                self.csv_identity_domains_network_perimeters.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_network_perimeters", e)

    ##########################################################################
    # CSV Identity Domain Identity Providers
    ##########################################################################

    def __csv_identity_domains_idps(self, groups, domain_name, domain_id):
        try:
            for var in groups:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_created_by_display': str(var['idcs_created_by_display']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_modified_by_display': str(var['idcs_last_modified_by_display']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'external_id': var['external_id'],
                    'partner_name': var['partner_name'],
                    'description': var['description'],
                    'metadata': var['metadata'],
                    'partner_provider_id': var['partner_provider_id'],
                    'tenant_provider_id': var['tenant_provider_id'],
                    'succinct_id': var['succinct_id'],
                    'idp_sso_url': var['idp_sso_url'],
                    'logout_request_url': var['logout_request_url'],
                    'logout_response_url': var['logout_response_url'],
                    'signing_certificate': var['signing_certificate'],
                    'encryption_certificate': var['encryption_certificate'],
                    'name_id_format': var['name_id_format'],
                    'include_signing_cert_in_signature': var['include_signing_cert_in_signature'],
                    'authn_request_binding': var['authn_request_binding'],
                    'logout_binding': var['logout_binding'],
                    'logout_enabled': var['logout_enabled'],
                    'signature_hash_algorithm': var['signature_hash_algorithm'],
                    'enabled': var['enabled'],
                    'icon_url': var['icon_url'],
                    'shown_on_login_page': var['shown_on_login_page'],
                    'jit_enabled': var['jit_user_prov_enabled'],
                    'jit_group_assertion_attribute_enabled': var['jit_user_prov_group_assertion_attribute_enabled'],
                    'jit_group_static_list_enabled': var['jit_user_prov_group_static_list_enabled'],
                    'jit_create_user_enabled': var['jit_user_prov_create_user_enabled'],
                    'jit_attribute_update_enabled': var['jit_user_prov_attribute_update_enabled'],
                    'jit_group_assignment_method': var['jit_user_prov_group_assignment_method'],
                    'jit_group_mapping_mode': var['jit_user_prov_group_mapping_mode'],
                    'jit_group_mappings': str(','.join(x['value'] + ":" + x['idp_group'] for x in var['jit_user_prov_group_mappings'])),
                    'jit_group_saml_attribute_name': var['jit_user_prov_group_saml_attribute_name'],
                    'service_instance_identifier': var['service_instance_identifier'],
                    'user_mapping_method': var['user_mapping_method'],
                    'user_mapping_store_attribute': var['user_mapping_store_attribute'],
                    'assertion_attribute': var['assertion_attribute'],
                    'type': var['type'],
                    'require_force_authn': var['require_force_authn'],
                    'requires_encrypted_assertion': var['requires_encrypted_assertion'],
                    'saml_ho_k_required': var['saml_ho_k_required'],
                    'requested_authentication_context': var['requested_authentication_context'],
                    'jit_user_prov_ignore_error_on_absent_groups': var['jit_user_prov_ignore_error_on_absent_groups'],
                    'jit_user_prov_attributes': var['jit_user_prov_attributes'],
                    'jit_user_prov_assigned_groups': var['jit_user_prov_assigned_groups'],
                    'correlation_policy': var['correlation_policy'],
                    'social_account_linking_enabled': var['ext_social_idp']['account_linking_enabled'],
                    'social_registration_enabled': var['ext_social_idp']['registration_enabled'],
                    'social_status': var['ext_social_idp']['status'],
                    'social_authz_url': var['ext_social_idp']['authz_url'],
                    'social_access_token_url': var['ext_social_idp']['access_token_url'],
                    'social_profile_url': var['ext_social_idp']['profile_url'],
                    'social_scope': self.__csv_list_to_str(var['ext_social_idp']['scope']),
                    'social_admin_scope': self.__csv_list_to_str(var['ext_social_idp']['admin_scope']),
                    'social_consumer_key': var['ext_social_idp']['consumer_key'],
                    'social_consumer_secret': var['ext_social_idp']['consumer_secret'],
                    'social_service_provider_name': var['ext_social_idp']['service_provider_name'],
                    'social_clock_skew_in_seconds': var['ext_social_idp']['clock_skew_in_seconds'],
                    'social_redirect_url': var['ext_social_idp']['redirect_url'],
                    'social_discovery_url': var['ext_social_idp']['discovery_url'],
                    'social_client_credential_in_payload': var['ext_social_idp']['client_credential_in_payload'],
                    'social_id_attribute': var['ext_social_idp']['id_attribute'],
                    'x509_cert_match_attribute': var['ext_x509_idp']['cert_match_attribute'],
                    'x509_user_match_attribute': var['ext_x509_idp']['user_match_attribute'],
                    'x509_other_cert_match_attribute': var['ext_x509_idp']['other_cert_match_attribute'],
                    'x509_signing_certificate_chain': var['ext_x509_idp']['signing_certificate_chain'],
                    'x509_ocsp_server_name': var['ext_x509_idp']['ocsp_server_name'],
                    'x509_ocsp_responder_url': var['ext_x509_idp']['ocsp_responder_url'],
                    'x509_ocsp_allow_unknown_response_status': var['ext_x509_idp']['ocsp_allow_unknown_response_status'],
                    'x509_ocsp_revalidate_time': var['ext_x509_idp']['ocsp_revalidate_time'],
                    'x509_ocsp_enable_signed_response': var['ext_x509_idp']['ocsp_enable_signed_response'],
                    'x509_ocsp_trust_cert_chain': var['ext_x509_idp']['ocsp_trust_cert_chain'],
                    'x509_crl_enabled': var['ext_x509_idp']['crl_enabled'],
                    'x509_crl_check_on_ocsp_failure_enabled': var['ext_x509_idp']['crl_check_on_ocsp_failure_enabled'],
                    'x509_crl_location': var['ext_x509_idp']['crl_location'],
                    'x509_crl_reload_duration': var['ext_x509_idp']['crl_reload_duration']
                }

                self.csv_identity_domains_idps.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_idps", e)

    ##########################################################################
    # CSV Identity Domain KMSI Setting
    ##########################################################################

    def __csv_identity_domains_kmsi_setting(self, groups, domain_name, domain_id):
        try:
            for var in groups:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'external_id': var['external_id'],
                    'token_validity_in_days': var['token_validity_in_days'],
                    'last_used_validity_in_days': var['last_used_validity_in_days'],
                    'max_allowed_sessions': var['max_allowed_sessions'],
                    'kmsi_feature_enabled': var['kmsi_feature_enabled'],
                    'kmsi_prompt_enabled': var['kmsi_prompt_enabled'],
                    'tou_prompt_disabled': var['tou_prompt_disabled'],
                    'last_enabled_on': var['last_enabled_on']
                }

                self.csv_identity_domains_kmsi_setting.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_kmsi_setting", e)

    ##########################################################################
    # CSV Identity Domain Auth Factor
    ##########################################################################

    def __csv_identity_domains_auth_factor(self, groups, domain_name, domain_id):
        try:
            for var in groups:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'email_enabled': var['email_enabled'],
                    'sms_enabled': var['sms_enabled'],
                    'phone_call_enabled': var['phone_call_enabled'],
                    'totp_enabled': var['totp_enabled'],
                    'push_enabled': var['push_enabled'],
                    'bypass_code_enabled': var['bypass_code_enabled'],
                    'security_questions_enabled': var['security_questions_enabled'],
                    'fido_authenticator_enabled': var['fido_authenticator_enabled'],
                    'yubico_otp_enabled': var['yubico_otp_enabled'],
                    'mfa_enrollment_type': var['mfa_enrollment_type'],
                    'mfa_enabled_category': var['mfa_enabled_category'],
                    'hide_backup_factor_enabled': var['hide_backup_factor_enabled'],
                    'auto_enroll_email_factor_disabled': var['auto_enroll_email_factor_disabled'],
                    'user_enrollment_disabled_factors': var['user_enrollment_disabled_factors'],
                    'email_link_enabled': var['email_link_enabled'],
                    'third_party_factor_duo_security': var['third_party_factor_duo_security'],
                    'notification_settings_pull_enabled': var['notification_settings_pull_enabled'],
                    'identity_store_settings_mobile_number_enabled': var['identity_store_settings_mobile_number_enabled'],
                    'self_service_generation_enabled': var['bypass_code_settings']['self_service_generation_enabled'],
                    'help_desk_generation_enabled': var['bypass_code_settings']['help_desk_generation_enabled'],
                    'length': var['bypass_code_settings']['length'],
                    'max_active': var['bypass_code_settings']['max_active'],
                    'help_desk_max_usage': var['bypass_code_settings']['help_desk_max_usage'],
                    'client_app_min_pin_length': var['client_app_settings']['min_pin_length'],
                    'client_app_max_failures_before_warning': var['client_app_settings']['max_failures_before_warning'],
                    'client_app_max_failures_before_lockout': var['client_app_settings']['max_failures_before_lockout'],
                    'client_app_initial_lockout_period_in_secs': var['client_app_settings']['initial_lockout_period_in_secs'],
                    'client_app_lockout_escalation_pattern': var['client_app_settings']['lockout_escalation_pattern'],
                    'client_app_max_lockout_interval_in_secs': var['client_app_settings']['max_lockout_interval_in_secs'],
                    'client_app_request_signing_algo': var['client_app_settings']['request_signing_algo'],
                    'client_app_policy_update_freq_in_days': var['client_app_settings']['policy_update_freq_in_days'],
                    'client_app_key_pair_length': var['client_app_settings']['key_pair_length'],
                    'client_app_device_protection_policy': var['client_app_settings']['device_protection_policy'],
                    'client_app_unlock_app_for_each_request_enabled': var['client_app_settings']['unlock_app_for_each_request_enabled'],
                    'client_app_unlock_on_app_start_enabled': var['client_app_settings']['unlock_on_app_start_enabled'],
                    'client_app_unlock_app_interval_in_secs': var['client_app_settings']['unlock_app_interval_in_secs'],
                    'client_app_shared_secret_encoding': var['client_app_settings']['shared_secret_encoding'],
                    'client_app_unlock_on_app_foreground_enabled': var['client_app_settings']['unlock_on_app_foreground_enabled'],
                    'endp_max_enrolled_devices': var['endpoint_restrictions']['max_enrolled_devices'],
                    'endp_max_trusted_endpoints': var['endpoint_restrictions']['max_trusted_endpoints'],
                    'endp_max_endpoint_trust_duration_in_days': var['endpoint_restrictions']['max_endpoint_trust_duration_in_days'],
                    'endp_trusted_endpoints_enabled': var['endpoint_restrictions']['trusted_endpoints_enabled'],
                    'endp_max_incorrect_attempts': var['endpoint_restrictions']['max_incorrect_attempts'],
                    'totp_hashing_algorithm': var['totp_settings']['hashing_algorithm'],
                    'totp_passcode_length': var['totp_settings']['passcode_length'],
                    'totp_key_refresh_interval_in_days': var['totp_settings']['key_refresh_interval_in_days'],
                    'totp_time_step_in_secs': var['totp_settings']['time_step_in_secs'],
                    'totp_time_step_tolerance': var['totp_settings']['time_step_tolerance'],
                    'totp_sms_otp_validity_duration_in_mins': var['totp_settings']['sms_otp_validity_duration_in_mins'],
                    'totp_jwt_validity_duration_in_secs': var['totp_settings']['jwt_validity_duration_in_secs'],
                    'totp_sms_passcode_length': var['totp_settings']['sms_passcode_length'],
                    'totp_email_otp_validity_duration_in_mins': var['totp_settings']['email_otp_validity_duration_in_mins'],
                    'totp_email_passcode_length': var['totp_settings']['email_passcode_length'],
                    'third_party_duo_security_settings': var['third_party_duo_security_settings'],
                    'compliance_policy': self.__csv_list_to_str(var['compliance_policy'], 'value'),
                    'fido_attestation': var['ext_fido_auth_factor']['attestation'],
                    'fido_authenticator_selection_attachment': var['ext_fido_auth_factor']['authenticator_selection_attachment'],
                    'fido_authenticator_selection_user_verification': var['ext_fido_auth_factor']['authenticator_selection_user_verification'],
                    'fido_authenticator_selection_resident_key': var['ext_fido_auth_factor']['authenticator_selection_resident_key'],
                    'fido_timeout': var['ext_fido_auth_factor']['timeout'],
                    'fido_authenticator_selection_require_resident_key': var['ext_fido_auth_factor']['authenticator_selection_require_resident_key'],
                    'fido_public_key_types': var['ext_fido_auth_factor']['public_key_types'],
                    'fido_exclude_credentials': var['ext_fido_auth_factor']['exclude_credentials'],
                    'fido_domain_validation_level': var['ext_fido_auth_factor']['domain_validation_level']
                }

                self.csv_identity_domains_auth_factors.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_auth_factor", e)

    ##########################################################################
    # CSV Identity Domain Password Policies
    ##########################################################################

    def __csv_identity_domains_password_policies(self, policies, domain_name, domain_id):
        try:
            for var in policies:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'domain_ocid': var['domain_ocid'],
                    'external_id': var['external_id'],
                    'name': var['name'],
                    'description': var['description'],
                    'allowed_chars': var['allowed_chars'],
                    'configured_password_policy_rules': str(','.join(x['key'] + '=' + x['value'] for x in var['configured_password_policy_rules'])),
                    'dictionary_delimiter': var['dictionary_delimiter'],
                    'dictionary_location': var['dictionary_location'],
                    'dictionary_word_disallowed': var['dictionary_word_disallowed'],
                    'disallowed_chars': var['disallowed_chars'],
                    'disallowed_substrings': var['disallowed_substrings'],
                    'first_name_disallowed': var['first_name_disallowed'],
                    'force_password_reset': var['force_password_reset'],
                    'groups': str(','.join(x['ref'] + '=' + x['value'] for x in var['groups'])),
                    'last_name_disallowed': var['last_name_disallowed'],
                    'lockout_duration': var['lockout_duration'],
                    'max_incorrect_attempts': var['max_incorrect_attempts'],
                    'max_length': var['max_length'],
                    'max_repeated_chars': var['max_repeated_chars'],
                    'max_special_chars': var['max_special_chars'],
                    'min_alpha_numerals': var['min_alpha_numerals'],
                    'min_alphas': var['min_alphas'],
                    'min_length': var['min_length'],
                    'min_lower_case': var['min_lower_case'],
                    'min_numerals': var['min_numerals'],
                    'min_password_age': var['min_password_age'],
                    'min_special_chars': var['min_special_chars'],
                    'min_unique_chars': var['min_unique_chars'],
                    'min_upper_case': var['min_upper_case'],
                    'num_passwords_in_history': var['num_passwords_in_history'],
                    'password_expire_warning': var['password_expire_warning'],
                    'password_expires_after': var['password_expires_after'],
                    'password_strength': var['password_strength'],
                    'priority': var['priority'],
                    'required_chars': var['required_chars'],
                    'starts_with_alphabet': var['starts_with_alphabet'],
                    'user_name_disallowed': var['user_name_disallowed']
                }
                self.csv_identity_domains_password_policies.append(data)
        except Exception as e:
            self.__print_error("__csv_identity_domains_password_policies", e)

    ##########################################################################
    # CSV Identity Domain Policies
    ##########################################################################
    def __csv_identity_domains_policies(self, policies, domain_name, domain_id):
        try:
            for var in policies:

                # Generate Rule String
                rule_string = ""
                for rl in var['rules']:
                    rule_string += "Rule: " + rl['name'] + " - " + rl['value'] + "\n"
                    for rt in rl['rule_return']:
                        rule_string += "      Rule Ret  : " + rt['name'] + " - " + rt['value'] + "\n"
                    if rl['condition_group']:
                        cn = rl['condition_group']
                        if 'name' in cn and 'description' in cn:
                            rule_string += "      Condition : " + cn['name'] + " - " + cn['description'] + "\n"
                        if 'attribute_name' in cn and 'operator' in cn and 'attribute_value' in cn:
                            if cn['attribute_name'] or cn['operator'] or cn['attribute_value']:
                                rule_string += "      Attribute : " + cn['attribute_name'] + " - " + cn['operator'] + " - " + cn['attribute_value'] + "\n"

                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'domain_ocid': var['domain_ocid'],
                    'external_id': var['external_id'],
                    'name': var['name'],
                    'description': var['description'],
                    'active': var['active'],
                    'policy_groovy': var['policy_groovy'],
                    'rules': str(','.join(x['ref'] + ':' + x['name'] + ':' + x['value'] for x in var['rules'])),
                    'rule_string': rule_string,
                    'policy_type_value': var['policy_type']['value'] if var['policy_type'] else "",
                    'policy_type_ref': var['policy_type']['ref'] if var['policy_type'] else ""
                }
                self.csv_identity_domains_policies.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_policies", e)

    ##########################################################################
    # CSV Identity Domain Rules
    ##########################################################################
    def __csv_identity_domains_rules(self, rules, domain_name, domain_id):
        try:
            for var in rules:
                data = {
                    'domain_id': domain_id,
                    'domain_name': domain_name,
                    'id': var['id'],
                    'ocid': var['ocid'],
                    'schemas': var['schemas'],
                    'meta_resource_type': var['meta']['resource_type'],
                    'meta_created': var['meta']['created'],
                    'meta_last_modified': var['meta']['last_modified'],
                    'meta_location': var['meta']['location'],
                    'meta_version': var['meta']['version'],
                    'idcs_created_by': str(var['idcs_created_by']),
                    'idcs_last_modified_by': str(var['idcs_last_modified_by']),
                    'idcs_last_upgraded_in_release': str(var['idcs_last_upgraded_in_release']),
                    'idcs_prevented_operations': str(var['idcs_prevented_operations']),
                    'tags': str(','.join(x['key'] + "=" + x['value'] for x in var['tags'])),
                    'compartment_ocid': var['compartment_ocid'],
                    'domain_ocid': var['domain_ocid'],
                    'external_id': var['external_id'],
                    'name': var['name'],
                    'description': var['description'],
                    'active': var['active'],
                    'locked': var['locked'],
                    'rule_groovy': var['rule_groovy'],
                    'rule_return': str(','.join(x['name'] + ':' + x['value'] for x in var['rule_return'])),
                    'policy_ids': self.__csv_list_to_str(var['policy_ids']),
                    'policy_ids_position': self.__csv_list_to_str(var['policy_ids_position']),
                    'policy_names': self.__csv_list_to_str(var['policy_names']),
                    'policy_type_ref': var['policy_type']['ref'] if var['policy_type'] else "",
                    'policy_type_value': var['policy_type']['value'] if var['policy_type'] else "",
                    'condition_value': "",
                    'condition_type': "",
                    'condition_name': "",
                    'condition_desc': "",
                    'condition_attribute_name': "",
                    'condition_operator': "",
                    'condition_attribute_value': "",
                    'condition_evaluate_condition_if': ""
                }
                if var['condition_group']:
                    vr = var['condition_group']
                    data['condition_value'] = vr['value']
                    data['condition_name'] = vr['name']
                    data['condition_type'] = vr['type']
                    data['condition_desc'] = vr['description']
                    data['condition_attribute_name'] = vr['attribute_name']
                    data['condition_operator'] = vr['operator']
                    data['condition_attribute_value'] = vr['attribute_value']
                    data['condition_evaluate_condition_if'] = vr['evaluate_condition_if']

                self.csv_identity_domains_rules.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_domains_rules", e)

    ##########################################################################
    # CSV Identity Compartments
    ##########################################################################

    def __csv_identity_compartments(self, compartments):
        try:
            for compartment in compartments:
                data = {
                    'id': compartment['id'],
                    'name': compartment['name'],
                    'path': compartment['path'],
                    'description': compartment['description'],
                    'time_created': compartment['time_created'],
                    'is_accessible': compartment['is_accessible'],
                    'lifecycle_state': compartment['lifecycle_state'],
                    'inactive_status': compartment['inactive_status'],
                    'freeform_tags': self.__get_freeform_tags(compartment['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(compartment['defined_tags'])
                }
                self.csv_identity_compartments.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_compartments", e)

    ##########################################################################
    # CSV Announcement
    ##########################################################################

    def __csv_announcements(self, announcements):
        try:
            for ann in announcements:
                data = {
                    'region_name': ann['region_name'],
                    'time_created': ann['time_created'],
                    'type': ann['type'],
                    'affected_regions': ann['affected_regions'],
                    'services': ann['services'],
                    'environment_name': ann['environment_name'],
                    'lifecycle_state': ann['lifecycle_state'],
                    'reference_ticket_number': ann['reference_ticket_number'],
                    'time_one_type': ann['time_one_type'],
                    'time_one_title': ann['time_one_title'],
                    'time_one_value': ann['time_one_value'],
                    'time_two_type': ann['time_two_type'],
                    'time_two_title': ann['time_two_title'],
                    'time_two_value': ann['time_two_value'],
                    'announcement_type': ann['announcement_type'],
                    'summary': ann['summary'],
                    'is_banner': ann['is_banner'],
                    'time_updated': ann['time_updated'],
                    'platform_type': ann['platform_type'],
                    'id': ann['id'],
                    'chain_id': ann['chain_id']
                }
                self.csv_announcements.append(data)

        except Exception as e:
            self.__print_error("__csv_announcements", e)

    ##########################################################################
    # CSV Announcement Active and Detailed
    ##########################################################################

    def __csv_announcements_detailed(self, region_name, announcements):
        try:
            for ann in announcements:
                data = {
                    'region_name': ann['region_name'],
                    'compartment': ann['compartment_path'],
                    'time_created': ann['time_created'],
                    'type': ann['type'],
                    'affected_regions': ann['affected_regions'],
                    'services': ann['services'],
                    'environment_name': ann['environment_name'],
                    'lifecycle_state': ann['lifecycle_state'],
                    'reference_ticket_number': ann['reference_ticket_number'],
                    'time_one_type': ann['time_one_type'],
                    'time_one_title': ann['time_one_title'],
                    'time_one_value': ann['time_one_value'],
                    'time_two_type': ann['time_two_type'],
                    'time_two_title': ann['time_two_title'],
                    'time_two_value': ann['time_two_value'],
                    'announcement_type': ann['announcement_type'],
                    'summary': ann['summary'],
                    'is_banner': ann['is_banner'],
                    'time_updated': ann['time_updated'],
                    'platform_type': ann['platform_type'],
                    'description': ann['description'],
                    'additional_information': ann['additional_information'],
                    'affected_resources': str(ann['affected_resources']),
                    'compartment_id': ann['compartment_id'],
                    'id': ann['id'],
                    'chain_id': ann['chain_id']
                }
                self.csv_announcements_detailed.append(data)

        except Exception as e:
            self.__print_error("__csv_announcements_detailed", e)

    ##########################################################################
    # csv Identity Policies
    ##########################################################################
    def __csv_identity_policies(self, policies_data):
        try:
            if not policies_data:
                return

            for c in policies_data:
                if self.__if_managed_paas_compartment(c['compartment_name']):
                    continue

                policies = c['policies']
                if not policies:
                    continue

                for policy in policies:
                    seq = 0
                    for statement in policy['statements']:
                        seq += 1
                        self.csv_identity_policies.append({
                            'compartment': c['compartment_path'],
                            'policy_name': policy['name'],
                            'idpk': policy['id'] + ":" + str(seq),
                            'id': policy['id'],
                            'seq': seq,
                            'statement': statement,
                            'compartment_id': c['compartment_id']
                        })

        except Exception as e:
            self.__print_error("__csv_identity_policies", e)

    ##########################################################################
    # csv Identity Network Sources
    ##########################################################################
    def __csv_identity_network_sources(self, data):
        try:
            if not data:
                return

            for ns in data:

                value = {
                    'description': ns['description'],
                    'services': self.__csv_list_to_str(ns['services']),
                    'public_source_list': self.__csv_list_to_str(ns['public_source_list']),
                    'virtual_source_list': self.__csv_list_to_str(ns['virtual_source_list'], 'ip_ranges'),
                    'vcn_ids': self.__csv_list_to_str(ns['virtual_source_list'], 'vcn_id'),
                    'freeform_tags': self.__get_freeform_tags(ns['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(ns['defined_tags']),
                    'id': ns['id']
                }

                self.csv_identity_network_sources.append(value)

        except Exception as e:
            self.__print_error("__csv_identity_policies", e)

    ##########################################################################
    # csv Identity Tag Namespace
    ##########################################################################
    def __csv_identity_tag_namespace(self, data):
        try:
            if not data:
                return

            for c in data:
                tags = c['tags']
                if not tags:
                    continue

                for tag in tags:

                    value = {
                        'compartment': c['compartment_path'],
                        'name': tag['name'],
                        'description': tag['description'],
                        'is_retired': tag['is_retired'],
                        'time_created': tag['time_created'],
                        'id': tag['id'],
                        'compartment_id': c['compartment_id'],
                        'freeform_tags': self.__get_freeform_tags(tag['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(tag['defined_tags'])
                    }

                    self.csv_identity_tag_namespaces.append(value)

        except Exception as e:
            self.__print_error("__csv_identity_tag_namespace", e)

    ##########################################################################
    # CSV Identity Module
    ##########################################################################
    def __csv_identity_main(self, data):
        try:
            if data:
                if 'compartments' in data:
                    self.__csv_identity_compartments(data['compartments'])
                if 'users' in data:
                    self.__csv_identity_users(data['users'])
                if 'groups' in data:
                    self.__csv_identity_groups(data['groups'])
                if 'dynamic_groups' in data:
                    self.__csv_identity_dynamic_groups(data['dynamic_groups'])
                if 'policies' in data:
                    self.__csv_identity_policies(data['policies'])
                if 'network_sources' in data:
                    self.__csv_identity_network_sources(data['network_sources'])
                if 'tag_namespace' in data:
                    self.__csv_identity_tag_namespace(data['tag_namespace'])
                if 'domains' in data:
                    self.__csv_identity_domains(data['domains'])
                if 'providers_mapping' in data:
                    self.__csv_identity_groups_mapping(data['providers_mapping'])

        except Exception as e:
            self.__print_error("__csv_identity_main", e)

    ##########################################################################
    # CSV Network Subnets
    ##########################################################################
    def __csv_error_data(self, data):

        try:
            for err in data:
                value = {
                    'class': err['class'],
                    'function': err['function'],
                    'compartment': err['compartment'],
                    'region': '',
                    'is_warning': err['is_warning'],
                    'error': err['error']
                }
                self.csv_errors.append(value)

            # run on local errors
            for err in self.error_array:
                value = {
                    'class': err['class'],
                    'function': err['function'],
                    'compartment': err['compartment'],
                    'region': "",
                    'is_warning': err['is_warning'],
                    'error': err['error']
                }
                self.csv_errors.append(value)

            # if no error post one line to clean old errors
            if not self.csv_errors:
                self.csv_errors.append({
                    'class': "No Errors",
                    'function': "",
                    'compartment': "",
                    'region': "",
                    'is_warning': "",
                    'error': ""
                })

        except Exception as e:
            self.__print_error("__csv_error_data", e)

    ##########################################################################
    # CSV Network Subnets
    ##########################################################################
    def __csv_core_network_vcn_subnet(self, region_name, subnets, vcn, igw, sgw, nat, drg, lpg):
        try:
            for subnet in subnets:
                data = {
                    'region_name': region_name,
                    'vcn_name': vcn['display_name'],
                    'vcn_cidr': "",
                    'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                    'vcn_compartment': vcn['compartment_name'],
                    'vcn_compartment_path': vcn['compartment_path'],
                    'internet_gateway': igw,
                    'service_gateway': sgw,
                    'nat': nat,
                    'drg': drg,
                    'local_peering': lpg,
                    'subnet_name': subnet['name'],
                    'subnet_cidr': subnet['cidr_block'],
                    'availability_domain': subnet['availability_domain'],
                    'subnet_compartment': subnet['compartment_name'],
                    'subnet_compartment_path': subnet['compartment_path'],
                    'public_private': subnet['public_private'],
                    'dhcp_options': subnet['dhcp_options'],
                    'route': subnet['route'],
                    'security_list': self.__csv_list_to_str(subnet['security_list']),
                    'dns': subnet['dns'],
                    'logs': self.__csv_list_to_str(subnet['logs'], 'name'),
                    'freeform_tags': self.__get_freeform_tags(subnet['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(subnet['defined_tags']),
                    'vcn_id': vcn['id'],
                    'subnet_id': subnet['id']
                }
                self.csv_network_subnet.append(data)

                # private ips
                for ip in subnet['private_ips']:
                    data = {
                        'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': "",
                        'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_path': vcn['compartment_path'],
                        'subnet_name': subnet['name'],
                        'subnet_cidr': subnet['cidr_block'],
                        'subnet_compartment': subnet['compartment_name'],
                        'subnet_compartment_path': subnet['compartment_path'],
                        'ip_address': ip['ip_address'],
                        'display_name': ip['display_name'],
                        'hostname_label': ip['hostname_label'],
                        'is_primary': ip['is_primary'],
                        'time_created': ip['time_created'],
                        'ip_compartment_name': ip['compartment_name'],
                        'ip_compartment_path': ip['compartment_path'],
                        'ip_compartment_id': ip['compartment_id'],
                        'privateip_id': ip['id'],
                        'vlan_id': ip['vlan_id'],
                        'vcn_id': vcn['id'],
                        'subnet_id': subnet['id'],
                        'freeform_tags': self.__get_freeform_tags(ip['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ip['defined_tags'])
                    }

                    self.csv_network_subnet_prv_ips.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_subnet", e)

    ##########################################################################
    # CSV Network vcn security list
    ##########################################################################
    def __csv_core_network_vcn_security_lists(self, region_name, sec_lists, vcn):
        try:
            if not sec_lists:
                return

            for sl in sec_lists:
                if len(sl['sec_rules']) == 0:
                    data = {
                        'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': "",
                        'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_path': vcn['compartment_path'],
                        'sec_name': sl['name'],
                        'sec_compartment': sl['compartment_name'],
                        'sec_compartment_path': sl['compartment_path'],
                        'sec_rules': "Empty",
                        'direction': "",
                        'is_stateless': "",
                        'source': "",
                        'destination': "",
                        'protocol': "",
                        'sec_protocol': "",
                        'src_port_min': "",
                        'src_port_max': "",
                        'dst_port_min': "",
                        'dst_port_max': "",
                        'icmp_code': "",
                        'icmp_type': "",
                        'description': "",
                        'security_alert': "FALSE",
                        'time_created': sl['time_created'][0:16],
                        'vcn_id': vcn['id'],
                        'sec_id': sl['id'],
                        'id': sl['id'] + ":" + str(hash("Empty"))
                    }
                    self.csv_network_security_list.append(data)

                else:
                    for slr in sl['sec_rules']:
                        data = {
                            'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': "",
                            'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_path': vcn['compartment_path'],
                            'sec_name': sl['name'],
                            'sec_compartment': sl['compartment_name'],
                            'sec_compartment_path': sl['compartment_path'],
                            'sec_rules': slr['desc'],
                            'direction': slr['direction'],
                            'is_stateless': slr['is_stateless'],
                            'source': slr['source'],
                            'destination': slr['destination'],
                            'protocol': slr['protocol'],
                            'sec_protocol': slr['protocol_name'],
                            'src_port_min': slr['src_port_min'],
                            'src_port_max': slr['src_port_max'],
                            'dst_port_min': slr['dst_port_min'],
                            'dst_port_max': slr['dst_port_max'],
                            'icmp_code': slr['icmp_code'],
                            'icmp_type': slr['icmp_type'],
                            'security_alert': slr['security_alert'],
                            'description': slr['description'],
                            'time_created': sl['time_created'],
                            'vcn_id': vcn['id'],
                            'sec_id': sl['id'],
                            'id': sl['id'] + ":" + str(hash(slr['desc']))
                        }
                        # check if id is in the list already
                        item_exists = False
                        for ls in self.csv_network_security_list:
                            if data['id'] == ls['id']:
                                item_exists = True
                                break

                        if not item_exists:
                            self.csv_network_security_list.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_security_lists", e)

    ##########################################################################
    # CSV Network drg
    ##########################################################################
    def __csv_core_network_drg(self, region_name, drgs):
        try:
            if not drgs:
                return

            for drg in drgs:
                data = {
                    'region_name': region_name,
                    'compartment_name': drg['compartment_name'],
                    'compartment_path': drg['compartment_path'],
                    'name': drg['name'],
                    'redundancy': drg['redundancy'],
                    'time_created': drg['time_created'][0:16],
                    'drg_route_tables': self.__csv_list_to_str(drg['drg_route_tables'], 'display_name'),
                    'ip_sec_connections': str(', '.join(x['name'] + " " + x['tunnels_status'] for x in drg['ip_sec_connections'])),
                    'virtual_circuits': self.__csv_list_to_str(drg['virtual_circuits'], 'name'),
                    'remote_peerings': str(', '.join(x['name'] + " " + x['peering_status'] for x in drg['remote_peerings'])),
                    'vcns': self.__csv_list_to_str(drg['vcns'], 'name'),
                    'freeform_tags': self.__get_freeform_tags(drg['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(drg['defined_tags']),
                    'id': drg['id']
                }
                self.csv_network_drg.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_drg", e)

    ##########################################################################
    # CSV Network ipsec
    ##########################################################################
    def __csv_core_network_ipsec_tunnels(self, region_name, ipsecs):
        try:
            if not ipsecs:
                return

            for arr in ipsecs:
                for tun in arr['tunnels']:
                    data = {
                        'region_name': region_name,
                        'compartment_name': arr['compartment_name'],
                        'compartment_path': arr['compartment_path'],
                        'tunnel_name': tun['display_name'],
                        'status': tun['status'],
                        'routing': tun['routing'],
                        'time_created': tun['time_created'][0:16],
                        'bgp_info': tun['bgp_info'],
                        'ipsec_name': arr['name'],
                        'drg': arr['drg'],
                        'drg_route_table': arr['drg_route_table'],
                        'cpe': arr['cpe'],
                        'cpe_local_identifier': arr['cpe_local_identifier'],
                        'cpe_time_created': arr['time_created'][0:16],
                        'routes': self.__csv_list_to_str(arr['routes']),
                        'logs': self.__csv_list_to_str(arr['logs'], 'name'),
                        'drg_id': arr['drg_id'],
                        'cpe_id': arr['cpe_id'],
                        'ipsec_id': arr['id'],
                        'id': tun['id'],
                        'freeform_tags': self.__get_freeform_tags(arr['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(arr['defined_tags'])
                    }
                    self.csv_network_drg_ipsec_tunnels.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_ipsec_tunnels", e)

    ##########################################################################
    # CSV Network virtual circuits
    ##########################################################################
    def __csv_core_network_virtual_circuit(self, region_name, vcs):
        try:
            if not vcs:
                return

            for arr in vcs:
                data = {
                    'region_name': region_name,
                    'compartment_name': arr['compartment_name'],
                    'compartment_path': arr['compartment_path'],
                    'name': arr['name'],
                    'bandwidth_shape_name': arr['bandwidth_shape_name'],
                    'bgp_management': arr['bgp_management'],
                    'bgp_session_state': arr['bgp_session_state'],
                    'bgp_ipv6_session_state': arr['bgp_ipv6_session_state'],
                    'bgp_admin_state': arr['bgp_admin_state'],
                    'is_bfd_enabled': arr['is_bfd_enabled'],
                    'customer_asn': arr['customer_asn'],
                    'gateway_id': arr['gateway_id'],
                    'provider_service_id': arr['provider_service_id'],
                    'provider_service_key_name': arr['provider_service_key_name'],
                    'routing_policy': arr['routing_policy'],
                    'public_prefixes': arr['public_prefixes'],
                    'region': arr['region'],
                    'customer_bgp_asn': arr['customer_bgp_asn'],
                    'drg': arr['drg'],
                    'lifecycle_state': arr['lifecycle_state'],
                    'oracle_bgp_asn': arr['oracle_bgp_asn'],
                    'provider_name': arr['provider_name'],
                    'provider_service_name': arr['provider_service_name'],
                    'provider_state': arr['provider_state'],
                    'reference_comment': arr['reference_comment'],
                    'service_type': arr['service_type'],
                    'cross_connect_mappings': arr['cross_connect_mappings'],
                    'type': arr['type'],
                    'drg_route_table': arr['drg_route_table'],
                    'logs': self.__csv_list_to_str(arr['logs'], 'name'),
                    'drg_id': arr['drg_id'],
                    'drg_route_table_id': arr['drg_route_table_id'],
                    'time_created': arr['time_created'],
                    'id': arr['id'],
                    'freeform_tags': self.__get_freeform_tags(arr['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(arr['defined_tags'])
                }
                self.csv_network_drg_virtual_circuits.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_virtual_circuit", e)

    ##########################################################################
    # CSV Network Firewall
    ##########################################################################
    def __csv_core_network_firewall(self, region_name, network_firewalls):
        try:
            if not network_firewalls:
                return

            for arr in network_firewalls:
                data = {
                    'region_name': region_name,
                    'compartment_name': arr['compartment_name'],
                    'compartment_path': arr['compartment_path'],
                    'compartment_id': arr['compartment_id'],
                    'name': arr['display_name'],
                    'subnet_id': arr['subnet_id'],
                    'subnet_name': arr['subnet_name'],
                    'availability_domain': arr['availability_domain'],
                    'ipv4_address': arr['ipv4_address'],
                    'ipv6_address': arr['ipv6_address'],
                    'network_firewall_policy_id': arr['network_firewall_policy_id'],
                    'network_firewall_policy_name': arr['network_firewall_policy_name'],
                    'time_created': arr['time_created'],
                    'time_updated': arr['time_updated'],
                    'lifecycle_state': arr['lifecycle_state'],
                    'id': arr['id'],
                    'freeform_tags': self.__get_freeform_tags(arr['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(arr['defined_tags'])
                }
                self.csv_network_firewall.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_virtual_circuit", e)

    ##########################################################################
    # CSV Network Firewall Policies
    ##########################################################################
    def __csv_core_network_firewall_policies(self, region_name, network_firewalls_policies):
        try:
            if not network_firewalls_policies:
                return

            for arr in network_firewalls_policies:
                data = {
                    'region_name': region_name,
                    'compartment_name': arr['compartment_name'],
                    'compartment_path': arr['compartment_path'],
                    'compartment_id': arr['compartment_id'],
                    'name': arr['display_name'],
                    'lifecycle_state': arr['lifecycle_state'],
                    'time_created': arr['time_created'],
                    'time_updated': arr['time_updated'],
                    'id': arr['id'],
                    'freeform_tags': self.__get_freeform_tags(arr['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(arr['defined_tags'])
                }
                self.csv_network_firewall_policies.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_firewall_policies", e)

    ##########################################################################
    # CSV for  Network vcn security group
    ##########################################################################
    def __csv_core_network_vcn_security_groups(self, region_name, nsg, vcn):
        try:
            if not nsg:
                return

            for sl in nsg:
                if len(sl['sec_rules']) == 0:
                    data = {
                        'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': "",
                        'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_path': vcn['compartment_path'],
                        'sec_name': sl['name'],
                        'sec_compartment': sl['compartment_name'],
                        'sec_compartment_path': sl['compartment_path'],
                        'rule_id': '',
                        'sec_rules': "Empty",
                        'direction': '',
                        'is_stateless': '',
                        'is_valid': '',
                        'source': '',
                        'source_name': '',
                        'source_type': '',
                        'destination': '',
                        'destination_name': '',
                        'destination_type': '',
                        'protocol': '',
                        'sec_protocol': '',
                        'src_port_min': '',
                        'src_port_max': '',
                        'dst_port_min': '',
                        'dst_port_max': '',
                        'icmp_code': '',
                        'icmp_type': '',
                        'sec_time_created': '',
                        'security_alert': "FALSE",
                        'description': '',
                        'time_created': sl['time_created'],
                        'freeform_tags': '',
                        'defined_tags': '',
                        'vcn_id': vcn['id'],
                        'sec_id': sl['id'],
                        'id': sl['id'] + ":Empty",
                        'vnics': ""
                    }
                    self.csv_network_security_group.append(data)

                else:
                    for slr in sl['sec_rules']:
                        data = {
                            'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': "",
                            'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_path': vcn['compartment_path'],
                            'sec_name': sl['name'],
                            'sec_compartment': sl['compartment_name'],
                            'sec_compartment_path': sl['compartment_path'],
                            'rule_id': slr['id'],
                            'sec_rules': slr['desc'],
                            'direction': slr['direction'],
                            'protocol': slr['protocol'],
                            'sec_protocol': slr['protocol_name'],
                            'is_stateless': slr['is_stateless'],
                            'is_valid': slr['is_valid'],
                            'source': slr['source'],
                            'source_name': slr['source_name'],
                            'source_type': slr['source_type'],
                            'destination': slr['destination'],
                            'destination_name': slr['destination_name'],
                            'destination_type': slr['destination_type'],
                            'src_port_min': slr['src_port_min'],
                            'src_port_max': slr['src_port_max'],
                            'dst_port_min': slr['dst_port_min'],
                            'dst_port_max': slr['dst_port_max'],
                            'icmp_code': slr['icmp_code'],
                            'icmp_type': slr['icmp_type'],
                            'description': slr['description'],
                            'security_alert': slr['security_alert'],
                            'sec_time_created': slr['time_created'],
                            'time_created': sl['time_created'],
                            'freeform_tags': self.__get_freeform_tags(sl['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(sl['defined_tags']),
                            'vcn_id': vcn['id'],
                            'sec_id': sl['id'],
                            'id': sl['id'] + ":" + slr['id'],
                            'vnics': str(';'.join(f'vnic_id={x["vnic_id"]}, time_associated={x["time_associated"]}' for x in sl['vnics']))
                        }

                        # check if id is in the list already
                        item_exists = False
                        for ls in self.csv_network_security_group:
                            if data['id'] == ls['id']:
                                item_exists = True
                                break

                        if not item_exists:
                            self.csv_network_security_group.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_security_groups", e)

    ##########################################################################
    # csv DHCP options for DHCP_ID
    ##########################################################################

    def __csv_core_network_vcn_dhcp_options(self, region_name, dhcp_options, vcn):
        try:
            for dhcp in dhcp_options:
                data = {
                    'region_name': region_name,
                    'vcn_name': vcn['display_name'],
                    'vcn_cidr': "",
                    'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                    'vcn_compartment': vcn['compartment_name'],
                    'vcn_compartment_path': vcn['compartment_path'],
                    'dhcp_name': dhcp['name'],
                    'option_1': "",
                    'option_2': "",
                    'dhcp_compartment': dhcp['compartment_name'],
                    'dhcp_compartment_path': dhcp['compartment_path'],
                    'time_created': dhcp['time_created'][0:16],
                    'vcn_id': vcn['id'],
                    'dhcp_id': dhcp['id']
                }

                seq = 0
                for opt in dhcp['opt']:
                    seq += 1
                    opt_str = "option_" + str(seq)
                    data[opt_str] = opt

                self.csv_network_dhcp_options.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_dhcp_options", e)

    ########################################################################
    # CSV Network vcn Route Tables
    ##########################################################################
    def __csv_core_network_vcn_route_tables(self, region_name, route_tables, vcn):
        try:
            if not route_tables:
                return

            for rt in route_tables:

                if len(rt['route_rules']) == 0:
                    data = {
                        'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': "",
                        'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_path': vcn['compartment_path'],
                        'route_name': rt['name'],
                        'route_compartment': rt['compartment_name'],
                        'route_compartment_path': rt['compartment_path'],
                        'destination': "",
                        'route': "Empty",
                        'time_created': rt['time_created'][0:16],
                        'vcn_id': vcn['id'],
                        'route_id': rt['id'],
                        'id': rt['id'] + ":Empty"
                    }
                    self.csv_network_routes.append(data)

                else:
                    for rl in rt['route_rules']:
                        data = {
                            'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': "",
                            'vcn_cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_path': vcn['compartment_path'],
                            'route_name': rt['name'],
                            'route_compartment': rt['compartment_name'],
                            'route_compartment_path': rt['compartment_path'],
                            'destination': rl['destination'],
                            'route': rl['desc'],
                            'time_created': rt['time_created'][0:16],
                            'vcn_id': vcn['id'],
                            'route_id': rt['id'],
                            'id': rt['id'] + ":" + str(hash(rl['desc']))
                        }

                        # check if id is in the list already
                        item_exists = False
                        for ls in self.csv_network_routes:
                            if data['id'] == ls['id']:
                                item_exists = True
                                break

                        if not item_exists:
                            self.csv_network_routes.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_route_tables", e)

    ##########################################################################
    # csv network vcn
    ##########################################################################
    def __csv_core_network_vcn(self, region_name, vcns):

        data = []
        try:
            if len(vcns) == 0:
                return

            for vcn in vcns:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(vcn['compartment_name']):
                    continue

                igw = ""
                sgw = ""
                nat = ""
                drg = ""
                lpg = ""
                subnets = ""
                subnets_cidrs = ""

                if 'igw' in vcn['data']:
                    igw = self.__csv_list_to_str(vcn['data']['igw'], 'name')

                if 'sgw' in vcn['data']:
                    sgw = str(', '.join(x['name'] + " " + x['services'] for x in vcn['data']['sgw']))

                if 'nat' in vcn['data']:
                    nat = self.__csv_list_to_str(vcn['data']['nat'], 'name')

                if 'drg_attached' in vcn['data']:
                    drg = self.__csv_list_to_str(vcn['data']['drg_attached'], 'name')

                if 'local_peering' in vcn['data']:
                    lpg = self.__csv_list_to_str(vcn['data']['local_peering'], 'name')

                if 'subnets' in vcn['data']:
                    self.__csv_core_network_vcn_subnet(region_name, vcn['data']['subnets'], vcn, igw, sgw, nat, drg, lpg)
                    subnets = self.__csv_list_to_str(vcn['data']['subnets'], 'name')
                    subnets_cidrs = self.__csv_list_to_str(vcn['data']['subnets'], 'cidr_block')

                if 'security_lists' in vcn['data']:
                    self.__csv_core_network_vcn_security_lists(region_name, vcn['data']['security_lists'], vcn)

                if 'security_groups' in vcn['data']:
                    self.__csv_core_network_vcn_security_groups(region_name, vcn['data']['security_groups'], vcn)

                if 'route_tables' in vcn['data']:
                    self.__csv_core_network_vcn_route_tables(region_name, vcn['data']['route_tables'], vcn)

                if 'dhcp_options' in vcn['data']:
                    self.__csv_core_network_vcn_dhcp_options(region_name, vcn['data']['dhcp_options'], vcn)

                data = {
                    'region_name': region_name,
                    'compartment': vcn['compartment_name'],
                    'compartment_path': vcn['compartment_path'],
                    'name': vcn['display_name'],
                    'cidr': "",
                    'cidrs': self.__csv_list_to_str(vcn['cidr_blocks']),
                    'internet_gateway': igw,
                    'service_gateway': sgw,
                    'nat': nat,
                    'drg': drg,
                    'local_peering': lpg,
                    'subnets': subnets,
                    'subnets_cidrs': subnets_cidrs,
                    'freeform_tags': self.__get_freeform_tags(vcn['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(vcn['defined_tags']),
                    'vcn_id': vcn['id']
                }

                self.csv_network_vcn.append(data)

        except BaseException as e:
            self.__print_error("__csv_core_network_vcn", e)

    ##########################################################################
    # csv network Main
    ##########################################################################
    def __csv_core_network_main(self, region_name, data):
        try:
            if 'vcn' in data:
                self.__csv_core_network_vcn(region_name, data['vcn'])

            if 'drg' in data:
                self.__csv_core_network_drg(region_name, data['drg'])

            if 'ipsec' in data:
                self.__csv_core_network_ipsec_tunnels(region_name, data['ipsec'])

            if 'virtual_circuit' in data:
                self.__csv_core_network_virtual_circuit(region_name, data['virtual_circuit'])

            if 'network_firewall' in data:
                self.__csv_core_network_firewall(region_name, data['network_firewall'])

            if 'network_firewall_policies' in data:
                self.__csv_core_network_firewall_policies(region_name, data['network_firewall_policies'])

        except Exception as e:
            self.__print_error("__csv_core_network_main", e)

    ##########################################################################
    # csv database db systems
    ##########################################################################
    def __csv_database_db_backups(self, region_name, list_db_backups):

        self.__csv_database_backup_item(list_db_backups, "", "")

    ##########################################################################
    # csv database db systems
    ##########################################################################
    def __csv_add_numbers_in_array(self, array, field=""):
        try:
            if not array:
                return ""

            total = 0

            # if specific field in the array
            if field:
                for ar in array:
                    if field:
                        if field in ar:
                            if str(ar[field]).replace(".", "").isnumeric():
                                total += int(ar[field])
                    else:
                        if str(ar).replace(".", "").isnumeric():
                            total += int(ar)

            return str(total)

        except Exception as e:
            self.__print_error("__csv_add_numbers_in_array", e)

    ##########################################################################
    # csv database db systems
    ##########################################################################
    def __csv_database_db_system(self, region_name, list_db_systems):

        try:
            for dbs in list_db_systems:

                # Db System CSV
                dbsd = {'region_name': region_name,
                        'availability_domain': dbs['availability_domain'],
                        'fault_domains': dbs['fault_domains'],
                        'compartment_name': dbs['compartment_name'],
                        'compartment_path': dbs['compartment_path'],
                        'status': dbs['lifecycle_state'],
                        'type': "DB System",
                        'name': dbs['display_name'],
                        'vm_name': dbs['display_name'],
                        'shape': dbs['shape'],
                        'cpu_core_count': dbs['cpu_core_count'],
                        'db_storage_gb': dbs['sum_size_gb'],
                        'shape_ocpus': dbs['shape_ocpu'],
                        'memory_gb': dbs['shape_memory_gb'],
                        'local_storage_tb': dbs['shape_storage_tb'],
                        'node_count': len(dbs['db_nodes']),
                        'gi_version': dbs['version_only'],
                        'gi_version_date': dbs['version_date'],
                        'system_version': "",
                        'system_version_date': "",
                        'database_edition': dbs['database_edition_short'],
                        'license_model': dbs['license_model'],
                        'data_subnet': dbs['data_subnet'],
                        'data_subnet_name': dbs['data_subnet_name'],
                        'data_vcn_name': dbs['data_vcn_name'],
                        'backup_subnet': dbs['backup_subnet'],
                        'backup_subnet_name': dbs['backup_subnet_name'],
                        'backup_vcn_name': dbs['backup_vcn_name'],
                        'scan_ips': self.__csv_list_to_str(dbs['scan_ips']),
                        'vip_ips': self.__csv_list_to_str(dbs['vip_ips']),
                        'cluster_name': dbs['cluster_name'],
                        'time_created': dbs['time_created'][0:16],
                        'domain': dbs['domain'],
                        'db_nodes': self.__csv_list_to_str(dbs['db_nodes'], 'desc'),
                        'db_homes': self.__csv_list_to_str(dbs['db_homes'], 'home'),
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                        'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                        'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                        'nsg_ids_names': dbs['nsg_ids_names'],
                        'nsg_ids': self.__csv_list_to_str(dbs['nsg_ids']),
                        'backup_network_nsg_ids_names': dbs['backup_network_nsg_ids_names'],
                        'backup_network_nsg_ids': self.__csv_list_to_str(dbs['backup_network_nsg_ids']),
                        'memory_size_in_gbs': dbs['memory_size_in_gbs'],
                        'storage_volume_performance_mode': dbs['storage_volume_performance_mode'],
                        'time_zone': dbs['time_zone'],
                        'kms_key_id': dbs['kms_key_id'],
                        'os_version': dbs['os_version'],
                        'disk_redundancy': dbs['disk_redundancy'],
                        'point_in_time_data_disk_clone_timestamp': dbs['point_in_time_data_disk_clone_timestamp'],
                        'data_storage_size_in_gbs': dbs['data_storage_size_in_gbs'],
                        'reco_storage_size_in_gb': dbs['reco_storage_size_in_gb'],
                        'db_nodes_software_size_gb': str(self.__csv_add_numbers_in_array(dbs['db_nodes'], 'software_storage_size_in_gb')),
                        'id': dbs['id'],
                        'infra_id': ''
                        }

                self.csv_db_all.append(dbsd)
                self.csv_db_vm_bm.append(dbsd)
                self.__csv_add_service(dbsd, "DB System")

                # Build the database CSV
                for db_home in dbs['db_homes']:

                    for db in db_home['databases']:

                        # Database CSV
                        data = {
                            'region_name': region_name,
                            'availability_domain': dbs['availability_domain'],
                            'compartment_name': dbs['compartment_name'],
                            'compartment_path': dbs['compartment_path'],
                            'status': dbs['lifecycle_state'],
                            'type': "DB System",
                            'name': dbs['display_name'],
                            'shape': dbs['shape'],
                            'compute_model': 'OCPU',
                            'compute_count': dbs['cpu_core_count'],
                            'cpu_core_count': dbs['cpu_core_count'],
                            'db_storage_gb': dbs['sum_size_gb'],
                            'shape_ocpus': dbs['shape_ocpu'],
                            'memory_gb': dbs['shape_memory_gb'],
                            'local_storage_tb': dbs['shape_storage_tb'],
                            'node_count': len(dbs['db_nodes']),
                            'db_name': db['db_name'],
                            'database': db['name'],
                            'database_edition': dbs['database_edition_short'],
                            'license_model': dbs['license_model'],
                            'data_subnet': dbs['data_subnet'],
                            'data_subnet_name': dbs['data_subnet_name'],
                            'data_vcn_name': dbs['data_vcn_name'],
                            'backup_subnet': dbs['backup_subnet'],
                            'backup_subnet_name': dbs['backup_subnet_name'],
                            'backup_vcn_name': dbs['backup_vcn_name'],
                            'scan_ips': self.__csv_list_to_str(dbs['scan_ips']),
                            'vip_ips': self.__csv_list_to_str(dbs['vip_ips']),
                            'pdbs': self.__csv_list_to_str(db['pdbs'], 'name'),
                            'cluster_name': dbs['cluster_name'],
                            'vm_name': dbs['display_name'],
                            'time_created': dbs['time_created'][0:16],
                            'domain': dbs['domain'],
                            'auto_backup_enabled': db['auto_backup_enabled'],
                            'last_failed_backup_timestamp': db['last_failed_backup_timestamp'],
                            'last_backup_duration_in_seconds': db['last_backup_duration_in_seconds'],
                            'recovery_window_in_days': db['db_backup_config']['recovery_window_in_days'] if 'db_backup_config' in db else "",
                            'backup_destination_type': db['db_backup_config']['backup_destination_type'] if 'db_backup_config' in db else "",
                            'auto_full_backup_day': db['db_backup_config']['auto_full_backup_day'] if 'db_backup_config' in db else "",
                            'kms_key_id': db['kms_key_id'],
                            'kms_key_version_id': db['kms_key_version_id'],
                            'key_store_wallet_name': db['key_store_wallet_name'],
                            'db_nodes': self.__csv_list_to_str(dbs['db_nodes'], 'desc'),
                            'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(db['defined_tags']),
                            'vault_id': db['vault_id'],
                            'database_id': db['id'],
                            'id': db['id'],
                            'dbsystem_id': dbs['id'],
                            'db_home': db_home['home_name'],
                            'db_home_version': db_home['home_version']
                        }

                        self.csv_database.append(data)
                        self.__csv_add_service(data, "DB System Database")

                        # Produce PDB csv
                        for pdb in db['pdbs']:
                            data = {
                                'region_name': region_name,
                                'availability_domain': dbs['availability_domain'],
                                'compartment_name': dbs['compartment_name'],
                                'compartment_path': dbs['compartment_path'],
                                'name': pdb['name'],
                                'system_name': dbs['display_name'],
                                'system_shape': dbs['shape'],
                                'database_name': db['db_name'],
                                'time_created': pdb['time_created'],
                                'lifecycle_state': pdb['lifecycle_state'],
                                'connection_strings': pdb['connection_strings'],
                                'open_mode': pdb['open_mode'],
                                'is_restricted': pdb['is_restricted'],
                                'management_status': pdb['management_status'],
                                'is_refreshable_clone': pdb['is_refreshable_clone'],
                                'freeform_tags': self.__get_freeform_tags(pdb['freeform_tags']),
                                'defined_tags': self.__get_defined_tags(pdb['defined_tags']),
                                'database_id': db['id'],
                                'dbsystem_id': dbs['id'],
                                'id': pdb['id']
                            }
                            self.csv_database_pdbs.append(data)
                            self.__csv_add_service(data, "DB System Database PDB")

                        # database Backups
                        if 'backups' in db:
                            self.__csv_database_backup_item(db['backups'], dbs['display_name'], db['db_name'])

        except Exception as e:
            self.__print_error("__csv_database_db_system", e)

    ##########################################################################
    # csv database db systems
    ##########################################################################
    def __csv_database_backup_item(self, backups, dbs_name, db_name):
        try:

            for backup in backups:
                data = {
                    'region_name': backup['region_name'],
                    'compartment_name': backup['compartment_name'],
                    'compartment_path': backup['compartment_path'],
                    'dbs_name': dbs_name,
                    'database': db_name,
                    'shape': backup['shape'],
                    'database_edition': backup['database_edition'],
                    'backup_name': backup['display_name'],
                    'time': backup['time'],
                    'size': "",
                    'id': backup['id'],
                    'database_id': backup['database_id'],
                    'kms_key_id': backup['kms_key_id'],
                    'vault_id': backup['vault_id'],
                    'lifecycle_state': backup['lifecycle_state']
                }
                # if not exist in array add
                if not any(d['id'] == str(backup['id']) for d in self.csv_database_backups):
                    self.csv_database_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_database_backup_item", e)

    ##########################################################################
    # csv exascale
    ##########################################################################
    def __csv_database_db_exascale(self, region_name, list_vaults):

        try:
            for dbs in list_vaults:

                vault = {
                    'region_name': region_name,
                    'availability_domain': dbs['availability_domain'],
                    'compartment_name': dbs['compartment_name'],
                    'compartment_path': dbs['compartment_path'],
                    'status': dbs['lifecycle_state'],
                    'time_created': dbs['time_created'],
                    'type': "Exascale",
                    'name': dbs['display_name'],
                    'time_zone': dbs['time_zone'],
                    'total_size_in_gbs': dbs['total_size_in_gbs'],
                    'available_size_in_gbs': dbs['available_size_in_gbs'],
                    'additional_flash_cache_in_percent': dbs['additional_flash_cache_in_percent'],
                    'vm_cluster_count': dbs['vm_cluster_count'],
                    'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                    'id': dbs['id']
                }
                self.csv_db_exascale_vaults.append(vault)
                self.__csv_add_service(vault, "DB Exascale Vault")

                for vm in dbs['vm_clusters']:
                    dbsd = {
                        'region_name': region_name,
                        'availability_domain': dbs['availability_domain'],
                        'compartment_name': vm['compartment_name'],
                        'compartment_path': vm['compartment_path'],
                        'status': dbs['lifecycle_state'],
                        'type': "Exascale",
                        'name': dbs['display_name'],
                        'vm_name': vm['display_name'],
                        'shape': vm['shape'],
                        'total_e_cpu_count': vm['total_e_cpu_count'],
                        'enabled_e_cpu_count': vm['enabled_e_cpu_count'],
                        'vm_file_system_storage_in_gbs': vm['vm_file_system_storage_in_gbs'],
                        'snapshot_file_system_storage_in_gbs': vm['snapshot_file_system_storage_in_gbs'],
                        'total_file_system_storage_in_gbs': vm['total_file_system_storage_in_gbs'],
                        'memory_gb': vm['memory_size_in_gbs'],
                        'node_count': len(vm['db_nodes']),
                        'gi_version': vm['gi_version'],
                        'system_version': vm['system_version'],
                        'database_edition': 'XP',
                        'license_model': vm['license_model'],
                        'data_subnet': vm['data_subnet'],
                        'data_subnet_name': vm['data_subnet_name'],
                        'data_vcn_name': vm['data_vcn_name'],
                        'backup_subnet': vm['backup_subnet'],
                        'backup_subnet_name': vm['backup_subnet_name'],
                        'backup_vcn_name': vm['backup_vcn_name'],
                        'scan_ips': self.__csv_list_to_str(vm['scan_ips']),
                        'vip_ips': self.__csv_list_to_str(vm['vip_ips']),
                        'cluster_name': vm['cluster_name'],
                        'time_created': vm['time_created'][0:16],
                        'domain': vm['domain'],
                        'db_homes': self.__csv_list_to_str(vm['db_homes'], 'home'),
                        'freeform_tags': self.__get_freeform_tags(vm['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(vm['defined_tags']),
                        'id': vm['id'],
                        'info': "ecpus:" + str(vm['enabled_e_cpu_count']),
                        'vault_id': dbs['id']
                    }

                    self.csv_db_all.append(dbsd)
                    self.csv_db_exascale_vmclusters.append(dbsd)
                    self.__csv_add_service(dbsd, "DB Exascale VMCluster")

                    # Build the database CSV
                    for db_home in vm['db_homes']:

                        for db in db_home['databases']:

                            # Database CSV
                            data = {'region_name': region_name,
                                    'availability_domain': dbs['availability_domain'],
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'status': dbs['lifecycle_state'],
                                    'type': "Exascale",
                                    'name': dbs['display_name'],
                                    'shape': dbs['shape'],
                                    'info': dbs['shape'],
                                    'compute_model': 'ECPU',
                                    'compute_count': vm['cpu_core_count'],
                                    'cpu_core_count': vm['cpu_core_count'],
                                    'db_storage_gb': dbs['sum_size_gb'],
                                    'shape_ocpus': dbs['shape_ocpu'],
                                    'shape_ecpus': vm['enabled_e_cpu_count'],
                                    'memory_gb': vm['memory_size_in_gbs'],
                                    'local_storage_tb': "",
                                    'node_count': len(vm['db_nodes']),
                                    'database': db['name'],
                                    'database_edition': 'XP',
                                    'license_model': vm['license_model'],
                                    'data_subnet': vm['data_subnet'],
                                    'data_subnet_name': vm['data_subnet_name'],
                                    'data_vcn_name': vm['data_vcn_name'],
                                    'backup_subnet': vm['backup_subnet'],
                                    'backup_subnet_name': vm['backup_subnet_name'],
                                    'backup_vcn_name': vm['backup_vcn_name'],
                                    'scan_ips': self.__csv_list_to_str(vm['scan_ips']),
                                    'vip_ips': self.__csv_list_to_str(vm['vip_ips']),
                                    'pdbs': self.__csv_list_to_str(db['pdbs'], 'name'),
                                    'cluster_name': vm['cluster_name'],
                                    'vm_name': vm['display_name'],
                                    'time_created': vm['time_created'][0:16],
                                    'domain': vm['domain'],
                                    'auto_backup_enabled': db['auto_backup_enabled'],
                                    'last_failed_backup_timestamp': db['last_failed_backup_timestamp'],
                                    'last_backup_duration_in_seconds': db['last_backup_duration_in_seconds'],
                                    'recovery_window_in_days': db['db_backup_config']['recovery_window_in_days'] if 'db_backup_config' in db else "",
                                    'backup_destination_type': db['db_backup_config']['backup_destination_type'] if 'db_backup_config' in db else "",
                                    'auto_full_backup_day': db['db_backup_config']['auto_full_backup_day'] if 'db_backup_config' in db else "",
                                    'kms_key_id': db['kms_key_id'],
                                    'kms_key_version_id': db['kms_key_version_id'],
                                    'key_store_wallet_name': db['key_store_wallet_name'],
                                    'db_nodes': self.__csv_list_to_str(vm['db_nodes'], 'desc'),
                                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': db_home['home_name'],
                                    'db_home_version': db_home['home_version']
                                    }

                            self.csv_database.append(data)
                            self.__csv_add_service(dbsd, "DB ExaCS Database")

                            # Produce PDB csv
                            for pdb in db['pdbs']:
                                data = {
                                    'region_name': region_name,
                                    'availability_domain': dbs['availability_domain'],
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'name': pdb['name'],
                                    'system_name': dbs['display_name'],
                                    'system_shape': "Exascale",
                                    'database_name': db['name'],
                                    'time_created': pdb['time_created'],
                                    'lifecycle_state': pdb['lifecycle_state'],
                                    'connection_strings': pdb['connection_strings'],
                                    'open_mode': pdb['open_mode'],
                                    'is_restricted': pdb['is_restricted'],
                                    'management_status': pdb['management_status'],
                                    'is_refreshable_clone': pdb['is_refreshable_clone'],
                                    'freeform_tags': self.__get_freeform_tags(pdb['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(pdb['defined_tags']),
                                    'database_id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'id': pdb['id']
                                }
                                self.csv_database_pdbs.append(data)
                                self.__csv_add_service(data, "DB Exascale Database PDB")

                            # database Backups
                            if 'backups' in db:
                                self.__csv_database_backup_item(db['backups'], dbs['display_name'], db['db_name'])

        except Exception as e:
            self.__print_error("__csv_database_db_exadata", e)

    ##########################################################################
    # csv database exadata
    ##########################################################################
    def __csv_database_db_exadata(self, region_name, list_exa):

        try:
            for dbs in list_exa:

                infs = {'region_name': region_name,
                        'availability_domain': dbs['availability_domain'],
                        'compartment_name': dbs['compartment_name'],
                        'compartment_path': dbs['compartment_path'],
                        'status': dbs['lifecycle_state'],
                        'type': "ExaCS",
                        'name': dbs['display_name'],
                        'shape': dbs['shape'],
                        'time_zone': "",
                        'cpus_enabled': "",
                        'max_memory_in_gbs': dbs['shape_memory_gb'],
                        'max_db_node_storage_in_g_bs': "",
                        'max_data_storage_in_t_bs': dbs['shape_storage_tb'],
                        'total_storage_size_in_gbs': dbs['total_storage_size_in_gbs'],
                        'available_storage_size_in_gbs': dbs['available_storage_size_in_gbs'],
                        'storage_count': dbs['storage_count'],
                        'compute_count': dbs['compute_count'],
                        'dns_server': "",
                        'ntp_server': "",
                        'csi_number': "",
                        'node_count': "",
                        # Added 7/29/2024
                        'cluster_placement_group_id': dbs['cluster_placement_group_id'],
                        'subscription_id': dbs['subscription_id'],
                        'cpu_count': dbs['cpu_count'],
                        'max_cpu_count': dbs['max_cpu_count'],
                        'memory_size_in_gbs': dbs['memory_size_in_gbs'],
                        'db_node_storage_size_in_gbs': dbs['db_node_storage_size_in_gbs'],
                        'max_db_node_storage_in_gbs': dbs['max_db_node_storage_in_gbs'],
                        'data_storage_size_in_tbs': dbs['data_storage_size_in_tbs'],
                        'max_data_storage_in_tbs': dbs['max_data_storage_in_tbs'],
                        'additional_storage_count': dbs['additional_storage_count'],
                        'activated_storage_count': dbs['activated_storage_count'],
                        'storage_server_version': dbs['storage_server_version'],
                        'db_server_version': dbs['db_server_version'],
                        'monthly_storage_server_version': dbs['monthly_storage_server_version'],
                        'monthly_db_server_version': dbs['monthly_db_server_version'],
                        'customer_contacts': str(dbs['customer_contacts']),
                        'defined_file_system_configurations': str(dbs['defined_file_system_configurations']),
                        # End Added 7/29/2024
                        'db_servers': self.__csv_list_to_str(dbs['db_servers'], 'desc'),
                        'db_servers_ids': self.__csv_list_to_str(dbs['db_servers'], 'id'),
                        'cluster_count': len(dbs['vm_clusters']),
                        'cluster_names': self.__csv_list_to_str(dbs['vm_clusters'], 'display_name'),
                        'time_created': dbs['time_created'],
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                        'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                        'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                        'infra_id': dbs['id'],
                        'info': dbs['shape'],
                        'id': dbs['id']
                        }
                self.csv_db_exa_infrastructure.append(infs)
                self.__csv_add_service(infs, "DB ExaCS Infra")

                for vm in dbs['vm_clusters']:
                    # Db Exa CSV
                    dbsd = {'region_name': region_name,
                            'availability_domain': dbs['availability_domain'],
                            'compartment_name': vm['compartment_name'],
                            'compartment_path': vm['compartment_path'],
                            'status': dbs['lifecycle_state'],
                            'type': "ExaCS",
                            'name': dbs['display_name'],
                            'vm_name': vm['display_name'],
                            'shape': dbs['shape'],
                            'cpu_core_count': vm['cpu_core_count'],
                            'db_storage_gb': vm['sum_size_gb'],
                            'shape_ocpus': dbs['shape_ocpu'],
                            'memory_gb': dbs['shape_memory_gb'],
                            'local_storage_tb': dbs['shape_storage_tb'],
                            'node_count': len(vm['db_nodes']),
                            'gi_version': vm['gi_version'],
                            'gi_version_date': vm['gi_version_date'],
                            'system_version': vm['system_version'],
                            'system_version_date': vm['system_version_date'],
                            'database_edition': 'XP',
                            'license_model': vm['license_model'],
                            'data_subnet': vm['data_subnet'],
                            'data_subnet_name': vm['data_subnet_name'],
                            'data_vcn_name': vm['data_vcn_name'],
                            'backup_subnet': vm['backup_subnet'],
                            'backup_subnet_name': vm['backup_subnet_name'],
                            'backup_vcn_name': vm['backup_vcn_name'],
                            'scan_ips': self.__csv_list_to_str(vm['scan_ips']),
                            'vip_ips': self.__csv_list_to_str(vm['vip_ips']),
                            'cluster_name': vm['cluster_name'],
                            'time_created': vm['time_created'][0:16],
                            'domain': vm['domain'],
                            # Added 7/29/2024
                            'subscription_id': vm['subscription_id'],
                            'is_diagnostics_events_enabled': vm['is_diagnostics_events_enabled'],
                            'is_health_monitoring_enabled': vm['is_health_monitoring_enabled'],
                            'is_incident_logs_enabled': vm['is_incident_logs_enabled'],
                            'gi_software_image_id': vm['gi_software_image_id'],
                            'scan_listener_port_tcp_ssl': vm['scan_listener_port_tcp_ssl'],
                            'scan_listener_port_tcp': vm['scan_listener_port_tcp'],
                            'file_system_configuration_details': str(vm['file_system_configuration_details']),
                            # End Added 7/29/2024
                            'db_nodes': self.__csv_list_to_str(vm['db_nodes'], 'desc'),
                            'db_homes': self.__csv_list_to_str(vm['db_homes'], 'home'),
                            'freeform_tags': self.__get_freeform_tags(vm['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(vm['defined_tags']),
                            'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                            'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                            'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                            'id': vm['id'],
                            'info': "ocpus:" + str(dbs['shape_ocpu']),
                            'infra_id': dbs['id']
                            }

                    self.csv_db_all.append(dbsd)
                    self.csv_db_exacs_vmclusters.append(dbsd)
                    self.__csv_add_service(dbsd, "DB ExaCS VMCluster")

                    # Build the database CSV
                    for db_home in vm['db_homes']:

                        for db in db_home['databases']:

                            # Database CSV
                            data = {'region_name': region_name,
                                    'availability_domain': dbs['availability_domain'],
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'status': dbs['lifecycle_state'],
                                    'type': "ExaCS",
                                    'name': dbs['display_name'],
                                    'shape': dbs['shape'],
                                    'info': dbs['shape'],
                                    'compute_model': 'OCPU',
                                    'compute_count': vm['cpu_core_count'],
                                    'cpu_core_count': vm['cpu_core_count'],
                                    'db_storage_gb': dbs['sum_size_gb'],
                                    'shape_ocpus': dbs['shape_ocpu'],
                                    'memory_gb': dbs['shape_memory_gb'],
                                    'local_storage_tb': dbs['shape_storage_tb'],
                                    'node_count': len(vm['db_nodes']),
                                    'database': db['name'],
                                    'database_edition': 'XP',
                                    'license_model': vm['license_model'],
                                    'data_subnet': vm['data_subnet'],
                                    'data_subnet_name': vm['data_subnet_name'],
                                    'data_vcn_name': vm['data_vcn_name'],
                                    'backup_subnet': vm['backup_subnet'],
                                    'backup_subnet_name': vm['backup_subnet_name'],
                                    'backup_vcn_name': vm['backup_vcn_name'],
                                    'scan_ips': self.__csv_list_to_str(vm['scan_ips']),
                                    'vip_ips': self.__csv_list_to_str(vm['vip_ips']),
                                    'pdbs': self.__csv_list_to_str(db['pdbs'], 'name'),
                                    'cluster_name': vm['cluster_name'],
                                    'vm_name': vm['display_name'],
                                    'time_created': vm['time_created'][0:16],
                                    'domain': vm['domain'],
                                    'auto_backup_enabled': db['auto_backup_enabled'],
                                    'last_failed_backup_timestamp': db['last_failed_backup_timestamp'],
                                    'last_backup_duration_in_seconds': db['last_backup_duration_in_seconds'],
                                    'recovery_window_in_days': db['db_backup_config']['recovery_window_in_days'] if 'db_backup_config' in db else "",
                                    'backup_destination_type': db['db_backup_config']['backup_destination_type'] if 'db_backup_config' in db else "",
                                    'auto_full_backup_day': db['db_backup_config']['auto_full_backup_day'] if 'db_backup_config' in db else "",
                                    'kms_key_id': db['kms_key_id'],
                                    'kms_key_version_id': db['kms_key_version_id'],
                                    'key_store_wallet_name': db['key_store_wallet_name'],
                                    'db_nodes': self.__csv_list_to_str(vm['db_nodes'], 'desc'),
                                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': db_home['home_name'],
                                    'db_home_version': db_home['home_version']
                                    }

                            self.csv_database.append(data)
                            self.__csv_add_service(dbsd, "DB ExaCS Database")

                            # Produce PDB csv
                            for pdb in db['pdbs']:
                                data = {
                                    'region_name': region_name,
                                    'availability_domain': dbs['availability_domain'],
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'name': pdb['name'],
                                    'system_name': dbs['display_name'],
                                    'system_shape': dbs['shape'],
                                    'database_name': db['name'],
                                    'time_created': pdb['time_created'],
                                    'lifecycle_state': pdb['lifecycle_state'],
                                    'connection_strings': pdb['connection_strings'],
                                    'open_mode': pdb['open_mode'],
                                    'is_restricted': pdb['is_restricted'],
                                    'management_status': pdb['management_status'],
                                    'is_refreshable_clone': pdb['is_refreshable_clone'],
                                    'freeform_tags': self.__get_freeform_tags(pdb['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(pdb['defined_tags']),
                                    'database_id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'id': pdb['id']
                                }
                                self.csv_database_pdbs.append(data)
                                self.__csv_add_service(data, "DB ExaCS Database PDB")

                            # database Backups
                            if 'backups' in db:
                                self.__csv_database_backup_item(db['backups'], dbs['display_name'], db['db_name'])

        except Exception as e:
            self.__print_error("__csv_database_db_exadata", e)

    ##########################################################################
    # csv database exacc
    ##########################################################################
    def __csv_database_db_exacc(self, region_name, list_exa):

        try:
            for dbs in list_exa:

                infs = {'region_name': region_name,
                        'availability_domain': 'ExaCC',
                        'compartment_name': dbs['compartment_name'],
                        'compartment_path': dbs['compartment_path'],
                        'status': dbs['lifecycle_state'],
                        'type': "ExaCC",
                        'name': dbs['display_name'],
                        'shape': dbs['shape'],
                        'info': dbs['shape'],
                        'time_zone': dbs['time_zone'],
                        'cpus_enabled': dbs['cpus_enabled'],
                        'max_cpu_count': dbs['max_cpu_count'],
                        'memory_size_in_gbs': dbs['memory_size_in_gbs'],
                        'max_memory_in_gbs': dbs['max_memory_in_gbs'],
                        'db_node_storage_size_in_gbs': dbs['db_node_storage_size_in_gbs'],
                        'max_db_node_storage_in_g_bs': dbs['max_db_node_storage_in_g_bs'],
                        'data_storage_size_in_tbs': dbs['data_storage_size_in_tbs'],
                        'max_data_storage_in_t_bs': dbs['max_data_storage_in_t_bs'],
                        'total_storage_size_in_gbs': "",
                        'available_storage_size_in_gbs': "",
                        'storage_count': dbs['storage_count'],
                        'additional_storage_count': dbs['additional_storage_count'],
                        'activated_storage_count': dbs['activated_storage_count'],
                        'compute_count': dbs['compute_count'],
                        'dns_server': dbs['dns_server'],
                        'ntp_server': dbs['ntp_server'],
                        'csi_number': dbs['csi_number'],
                        'node_count': len(dbs['db_servers']),
                        'db_servers': self.__csv_list_to_str(dbs['db_servers'], 'desc'),
                        'db_servers_ids': self.__csv_list_to_str(dbs['db_servers'], 'id'),
                        'cluster_count': len(dbs['vm_clusters']),
                        'cluster_names': self.__csv_list_to_str(dbs['vm_clusters'], 'display_name'),
                        'time_created': dbs['time_created'],
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                        'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                        'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                        'infra_id': dbs['id'],
                        'id': dbs['id']
                        }
                self.csv_db_exa_infrastructure.append(infs)
                self.__csv_add_service(infs, "DB ExaCC Infra")

                # VM Clusters
                for vm in dbs['vm_clusters']:
                    # Db Exa CSV
                    dbsd = {'region_name': region_name,
                            'availability_domain': 'ExaCC',
                            'compartment_name': vm['compartment_name'],
                            'compartment_path': vm['compartment_path'],
                            'status': dbs['lifecycle_state'],
                            'type': "ExaCC",
                            'name': dbs['display_name'],
                            'vm_name': vm['display_name'],
                            'shape': dbs['shape'],
                            'cpu_core_count': vm['cpus_enabled'],
                            'db_storage_gb': vm['db_node_storage_size_in_gbs'],
                            'shape_ocpus': "",
                            'memory_gb': dbs['memory_size_in_gbs'],
                            'local_storage_tb': dbs['data_storage_size_in_tbs'],
                            'node_count': len(vm['db_nodes']),
                            'gi_version': vm['gi_version'],
                            'gi_version_date': vm['gi_version_date'],
                            'system_version': vm['system_version'],
                            'system_version_date': vm['system_version_date'],
                            'database_edition': 'XP',
                            'license_model': vm['license_model'],
                            'data_subnet': "",
                            'data_subnet_name': "",
                            'data_vcn_name': "",
                            'backup_subnet': "",
                            'backup_subnet_name': "",
                            'backup_vcn_name': "",
                            'scan_ips': "",
                            'vip_ips': "",
                            'cluster_name': vm['display_name'],
                            'time_created': vm['time_created'][0:16],
                            'domain': "",
                            'db_nodes': self.__csv_list_to_str(vm['db_nodes'], 'desc'),
                            'db_homes': self.__csv_list_to_str(vm['db_homes'], 'home'),
                            'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                            'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                            'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                            'freeform_tags': self.__get_freeform_tags(vm['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(vm['defined_tags']),
                            'id': vm['id'],
                            'info': "ocpus:" + str(vm['cpus_enabled']),
                            'infra_id': dbs['id']
                            }

                    self.csv_db_all.append(dbsd)
                    self.csv_db_exacc_vmclusters.append(dbsd)

                    # Add to CSV Service
                    self.__csv_add_service(dbsd, "DB ExaCC VMCluster")

                    # Build the database CSV
                    for db_home in vm['db_homes']:

                        for db in db_home['databases']:

                            # Database CSV
                            data = {'region_name': region_name,
                                    'availability_domain': "ExaCC",
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'status': dbs['lifecycle_state'],
                                    'type': "ExaCC",
                                    'name': dbs['display_name'],
                                    'shape': dbs['shape'],
                                    'info': dbs['shape'],
                                    'compute_model': 'OCPU',
                                    'compute_count': vm['cpus_enabled'],
                                    'cpu_core_count': vm['cpus_enabled'],
                                    'db_storage_gb': "",
                                    'shape_ocpus': "",
                                    'memory_gb': dbs['memory_size_in_gbs'],
                                    'local_storage_tb': dbs['data_storage_size_in_tbs'],
                                    'node_count': len(vm['db_nodes']),
                                    'database': db['name'],
                                    'database_edition': 'XP',
                                    'license_model': vm['license_model'],
                                    'data_subnet': "",
                                    'data_subnet_name': "",
                                    'data_vcn_name': "",
                                    'backup_subnet': "",
                                    'backup_subnet_name': "",
                                    'backup_vcn_name': "",
                                    'scan_ips': "",
                                    'vip_ips': "",
                                    'pdbs': self.__csv_list_to_str(db['pdbs'], 'name'),
                                    'cluster_name': vm['display_name'],
                                    'vm_name': vm['display_name'],
                                    'time_created': vm['time_created'][0:16],
                                    'domain': "",
                                    'auto_backup_enabled': db['auto_backup_enabled'],
                                    'last_failed_backup_timestamp': db['last_failed_backup_timestamp'],
                                    'last_backup_duration_in_seconds': db['last_backup_duration_in_seconds'],
                                    'recovery_window_in_days': db['db_backup_config']['recovery_window_in_days'] if 'db_backup_config' in db else "",
                                    'backup_destination_type': db['db_backup_config']['backup_destination_type'] if 'db_backup_config' in db else "",
                                    'auto_full_backup_day': db['db_backup_config']['auto_full_backup_day'] if 'db_backup_config' in db else "",
                                    'kms_key_version_id': db['kms_key_version_id'],
                                    'key_store_wallet_name': db['key_store_wallet_name'],
                                    'db_nodes': self.__csv_list_to_str(vm['db_nodes'], 'desc'),
                                    'kms_key_id': db['kms_key_id'],
                                    'vault_id': db['vault_id'],
                                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': db_home['home_name'],
                                    'db_home_version': db_home['home_version']
                                    }

                            self.csv_database.append(data)
                            self.__csv_add_service(data, "DB ExaCC Database")

                            # Produce PDB csv
                            for pdb in db['pdbs']:
                                data = {
                                    'region_name': region_name,
                                    'availability_domain': 'ExaCC',
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'name': pdb['name'],
                                    'system_name': dbs['display_name'],
                                    'system_shape': dbs['shape'],
                                    'database_name': db['name'],
                                    'time_created': pdb['time_created'],
                                    'lifecycle_state': pdb['lifecycle_state'],
                                    'connection_strings': pdb['connection_strings'],
                                    'open_mode': pdb['open_mode'],
                                    'is_restricted': pdb['is_restricted'],
                                    'management_status': pdb['management_status'],
                                    'is_refreshable_clone': pdb['is_refreshable_clone'],
                                    'freeform_tags': self.__get_freeform_tags(pdb['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(pdb['defined_tags']),
                                    'database_id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'id': pdb['id']
                                }
                                self.csv_database_pdbs.append(data)
                                self.__csv_add_service(data, "DB ExaCC Database PDB")

                            # database Backups
                            if 'backups' in db:
                                self.__csv_database_backup_item(db['backups'], dbs['display_name'], db['db_name'])

        except Exception as e:
            self.__print_error("__csv_database_db_exacc", e)

    ##########################################################################
    # csv database autonomous dedicated
    ##########################################################################

    def __csv_database_db_exacc_autonomous_dedicated(self, region_name, databases):
        try:
            for dbs in databases:
                for vm in dbs['adb_clusters']:
                    for ct in vm['containers']:
                        for db in ct['databases']:
                            data = {'region_name': region_name,
                                    'availability_domain': "",
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'status': dbs['lifecycle_state'],
                                    'type': "Autonomous Dedicated " + str(db['db_workload']),
                                    'name': db['display_name'],
                                    'shape': vm['shape'],
                                    'compute_model': db['compute_model'],
                                    'compute_count': db['compute_count'],
                                    'cpu_core_count': db['cpu_core_count'],
                                    'info': str(db['cpu_core_count']),
                                    'db_storage_gb': str(int(db['data_storage_size_in_tbs']) * 1024),
                                    'shape_ocpus': vm['ocpu_count'],
                                    'memory_gb': vm['memory_size_in_gbs'],
                                    'local_storage_tb': vm['memory_per_oracle_compute_unit_in_gbs'],
                                    'node_count': "",
                                    'database': db['name'],
                                    'database_edition': 'ADB-D',
                                    'license_model': vm['license_model'],
                                    'data_subnet': vm['subnet_name'],
                                    'backup_subnet': "",
                                    'scan_ips': "",
                                    'vip_ips': "",
                                    'pdbs': "",
                                    'vm_name': ct['name'],
                                    'cluster_name': vm['display_name'],
                                    'time_created': db['time_created'],
                                    'domain': "",
                                    'auto_backup_enabled': "True",
                                    'db_nodes': "",
                                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': "",
                                    'db_home_version': ""
                                    }
                            self.csv_database.append(data)
                            self.__csv_add_service(data, "DB ExaCC ADB")

        except Exception as e:
            self.__print_error("__csv_database_db_exacc_autonomous_dedicated", e)

    ##########################################################################
    # csv database db system
    ##########################################################################

    def __csv_database_db_autonomous(self, region_name, databases):
        try:
            for dbs in databases:
                data = {'region_name': region_name,
                        'availability_domain': "",
                        'compartment_name': dbs['compartment_name'],
                        'compartment_path': dbs['compartment_path'],
                        'status': dbs['lifecycle_state'],
                        'type': "Autonomous " + dbs['db_workload'],
                        'name': dbs['display_name'], 'shape': "",
                        'compute_model': dbs['compute_model'],
                        'compute_count': dbs['compute_count'],
                        'cpu_core_count': dbs['cpu_core_count'],
                        'db_storage_gb': str(int(dbs['data_storage_size_in_tbs']) * 1024) if str(dbs['data_storage_size_in_tbs']).replace(".", "").isnumeric() else '',
                        'shape_ocpus': "",
                        'memory_gb': "",
                        'local_storage_tb': "",
                        'node_count': "",
                        'database': dbs['db_name'],
                        'database_edition': 'ADB',
                        'license_model': dbs['license_model'],
                        'data_subnet': "",
                        'data_subnet_name': "",
                        'data_vcn_name': "",
                        'backup_subnet': "",
                        'backup_subnet_name': "",
                        'backup_vcn_name': "",
                        'scan_ips': "",
                        'vip_ips': "",
                        'pdbs': "",
                        'vm_name': "",
                        'cluster_name': "",
                        'time_created': dbs['time_created'],
                        'domain': "",
                        'auto_backup_enabled': "True",
                        'db_nodes': "",
                        'kms_key_id': dbs['kms_key_id'],
                        'vault_id': dbs['vault_id'],
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'database_id': dbs['id'],
                        'dbsystem_id': dbs['id'],
                        'db_home': "",
                        'db_home_version': dbs['db_version']
                        }
                self.csv_database.append(data)

                # for autonomous only
                dadb = {'region_name': region_name,
                        'compartment_name': dbs['compartment_name'],
                        'compartment_path': dbs['compartment_path'],
                        'status': dbs['lifecycle_state'],
                        'type': "Autonomous " + dbs['db_workload'],
                        'name': dbs['display_name'],
                        'infra_name': "",
                        'cluster_name': "",
                        'container_name': "",
                        'cpu_core_count': dbs['cpu_core_count'],
                        'compute_model': dbs['compute_model'],
                        'compute_count': dbs['compute_count'],
                        'db_storage_tb': dbs['data_storage_size_in_tbs'],
                        'db_version': dbs['db_version'],
                        'db_name': dbs['db_name'],
                        'version_license_model': dbs['license_model'],
                        'time_created': dbs['time_created'],
                        'data_safe_status': dbs['data_safe_status'],
                        'time_maintenance_begin': dbs['time_maintenance_begin'],
                        'time_maintenance_end': dbs['time_maintenance_end'],
                        'subnet_id': dbs['subnet_id'] if dbs['subnet_id'] != "None" else "",
                        'subnet_name': dbs['subnet_name'] if dbs['subnet_name'] != "None" else "",
                        'private_endpoint': dbs['private_endpoint'] if dbs['private_endpoint'] != "None" else "",
                        'private_endpoint_label': dbs['private_endpoint_label'] if dbs['private_endpoint_label'] != "None" else "",
                        'nsg_ids': self.__csv_list_to_str(dbs['nsg_ids']),
                        'nsg_names': self.__csv_list_to_str(dbs['nsg_names']),
                        'whitelisted_ips': dbs['whitelisted_ips'],
                        'service_console_url': dbs['service_console_url'],
                        'connection_strings': dbs['connection_strings'],
                        'is_auto_scaling_enabled': dbs['is_auto_scaling_enabled'],
                        'is_dedicated': dbs['is_dedicated'],
                        'is_data_guard_enabled': dbs['is_data_guard_enabled'],
                        'standby_lag_time_in_seconds': dbs['standby_lag_time_in_seconds'],
                        'standby_lifecycle_state': dbs['standby_lifecycle_state'],
                        'time_of_last_switchover': dbs['time_of_last_switchover'],
                        'time_local_data_guard_enabled': dbs['time_local_data_guard_enabled'],
                        'dataguard_region_type': dbs['dataguard_region_type'],
                        'supported_regions_to_clone_to': dbs['supported_regions_to_clone_to'],
                        'key_store_wallet_name': dbs['key_store_wallet_name'],
                        'key_store_id': dbs['key_store_id'],
                        'kms_key_id': dbs['kms_key_id'],
                        'vault_id': dbs['vault_id'],
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'info': "ocpus:" + str(dbs['cpu_core_count']),
                        'id': dbs['id']
                        }

                self.csv_db_autonomous.append(dadb)
                self.__csv_add_service(dadb, "DB ADB-S")

                # database Backups
                if 'backups' in dbs:
                    for backup in dbs['backups']:
                        data = {
                            'region_name': region_name,
                            'compartment_name': dbs['compartment_name'],
                            'compartment_path': dbs['compartment_path'],
                            'dbs_name': dbs['display_name'],
                            'database': dbs['db_name'],
                            'shape': 'Autononous',
                            'database_edition': "",
                            'backup_name': ("Automatic Backup - " if backup['is_automatic'] == 'True' else "") + backup['display_name'],
                            'time': backup['time'],
                            'size': "",
                            'id': backup['id'],
                            'database_id': dbs['id'],
                            'kms_key_id': dbs['kms_key_id'],
                            'vault_id': dbs['vault_id'],
                            'lifecycle_state': backup['lifecycle_state']
                        }
                        self.csv_database_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_database_db_autonomous", e)

    ##########################################################################
    # csv database autonouns dedicated
    ##########################################################################

    def __csv_database_db_autonomous_dedicated(self, region_name, databases):
        try:
            for dbs in databases:
                for vm in dbs['adb_clusters']:
                    for ct in vm['containers']:
                        for db in ct['databases']:
                            data = {'region_name': region_name,
                                    'availability_domain': dbs['availability_domain'],
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'status': dbs['lifecycle_state'],
                                    'type': "Autonomous Dedicated " + str(db['db_workload']),
                                    'name': db['display_name'],
                                    'shape': dbs['shape'],
                                    'cpu_core_count': db['cpu_core_count'],
                                    'compute_model': db['compute_model'],
                                    'compute_count': db['compute_count'],
                                    'db_storage_gb': str(int(db['data_storage_size_in_tbs']) * 1024),
                                    'shape_ocpus': vm['ocpu_count'],
                                    'memory_gb': vm['memory_size_in_gbs'],
                                    'local_storage_tb': vm['data_storage_size_in_gbs'],
                                    'node_count': vm['node_count'],
                                    'database': db['name'],
                                    'database_edition': 'ADB-D',
                                    'license_model': vm['license_model'],
                                    'data_subnet': vm['subnet_name_full'],
                                    'data_subnet_name': vm['subnet_name'],
                                    'data_vcn_name': vm['vcn_name'],
                                    'backup_subnet': "",
                                    'backup_subnet_name': "",
                                    'backup_vcn_name': "",
                                    'scan_ips': "",
                                    'vip_ips': "",
                                    'pdbs': "",
                                    'vm_name': ct['name'],
                                    'cluster_name': vm['display_name'],
                                    'time_created': db['time_created'],
                                    'domain': vm['domain'],
                                    'auto_backup_enabled': "True",
                                    'db_nodes': "",
                                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': "",
                                    'info': "ocpus:" + str(db['cpu_core_count']),
                                    'db_home_version': ""
                                    }
                            self.csv_database.append(data)
                            self.__csv_add_service(data, "DB ADB-D")

        except Exception as e:
            self.__print_error("__csv_database_db_autonomous_dedicated", e)

    ##########################################################################
    # csv database autonouns dedicated
    ##########################################################################

    def __csv_database_db_autonomous_databases(self, region_name, databases):
        try:
            for dbs in databases:
                for vm in dbs['adb_clusters']:
                    for ct in vm['containers']:
                        for db in ct['databases']:
                            dadb = {'region_name': region_name,
                                    'compartment_name': db['compartment_name'],
                                    'compartment_path': db['compartment_path'],
                                    'status': db['lifecycle_state'],
                                    'type': "Autonomous Dedicated " + db['db_workload'],
                                    'name': db['display_name'],
                                    'infra_name': dbs['display_name'],
                                    'cluster_name': vm['display_name'],
                                    'container_name': ct['display_name'],
                                    'compute_model': db['compute_model'],
                                    'compute_count': db['compute_count'],
                                    'cpu_core_count': db['cpu_core_count'],
                                    'db_storage_tb': db['data_storage_size_in_tbs'],
                                    'db_version': db['db_version'],
                                    'db_name': db['db_name'],
                                    'version_license_model': vm['license_model'],
                                    'time_created': db['time_created'],
                                    'data_safe_status': db['data_safe_status'],
                                    'time_maintenance_begin': db['time_maintenance_begin'],
                                    'time_maintenance_end': db['time_maintenance_end'],
                                    'subnet_id': vm['subnet_id'],
                                    'subnet_name': vm['subnet_name'],
                                    'private_endpoint': db['private_endpoint'],
                                    'private_endpoint_label': db['private_endpoint_label'],
                                    # Adi - To Check NSG Variables
                                    'nsg_ids': "",
                                    'nsg_names': "",
                                    'whitelisted_ips': db['whitelisted_ips'],
                                    'service_console_url': db['service_console_url'],
                                    'connection_strings': db['connection_strings'],
                                    'is_auto_scaling_enabled': db['is_auto_scaling_enabled'],
                                    'is_data_guard_enabled': db['is_data_guard_enabled'],
                                    'is_dedicated': db['is_dedicated'],
                                    'standby_lag_time_in_seconds': db['standby_lag_time_in_seconds'],
                                    'standby_lifecycle_state': db['standby_lifecycle_state'],
                                    'time_of_last_switchover': db['time_of_last_switchover'],
                                    'time_local_data_guard_enabled': db['time_local_data_guard_enabled'],
                                    'dataguard_region_type': db['dataguard_region_type'],
                                    'supported_regions_to_clone_to': db['supported_regions_to_clone_to'],
                                    'key_store_wallet_name': db['key_store_wallet_name'],
                                    'key_store_id': db['key_store_id'],
                                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'info': "ocpus" + str(db['cpu_core_count']),
                                    'id': db['id']
                                    }

                            self.csv_db_autonomous.append(dadb)
                            self.__csv_add_service(dadb, "DB ADB-D")

                            # database Backups
                            if 'backups' in dbs:
                                for backup in db['backups']:
                                    data = {
                                        'region_name': region_name,
                                        'compartment_name': dbs['compartment_name'],
                                        'compartment_path': dbs['compartment_path'],
                                        'dbs_name': dbs['display_name'],
                                        'database': dbs['db_name'],
                                        'shape': 'Autononous',
                                        'database_edition': "",
                                        'backup_name': ("Automatic Backup - " if backup['is_automatic'] == 'True' else "") + backup['display_name'],
                                        'time': backup['time'],
                                        'size': "",
                                        'id': backup['id'],
                                        'database_id': dbs['id'],
                                        'lifecycle_state': backup['lifecycle_state']
                                    }
                                    self.csv_database_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_database_db_autonomous_databases", e)

    ##########################################################################
    # __csv_database_goldengate
    ##########################################################################

    def __csv_database_goldengate(self, region_name, goldengates):
        try:
            if 'gg_deployments' in goldengates:
                for db in goldengates['gg_deployments']:
                    gg = {
                        'region_name': region_name,
                        'compartment_name': db['compartment_name'],
                        'compartment_path': db['compartment_path'],
                        'display_name': db['display_name'],
                        'description': db['description'],
                        'time_created': db['time_created'],
                        'time_updated': db['time_updated'],
                        'lifecycle_state': db['lifecycle_state'],
                        'subnet_id': db['subnet_id'],
                        'subnet_name': db['subnet_name'],
                        'license_model': db['license_model'],
                        'fqdn': db['fqdn'],
                        'cpu_core_count': db['cpu_core_count'],
                        'is_auto_scaling_enabled': db['is_auto_scaling_enabled'],
                        'is_public': db['is_public'],
                        'public_ip_address': db['public_ip_address'],
                        'private_ip_address': db['private_ip_address'],
                        'deployment_url': db['deployment_url'],
                        'is_latest_version': db['is_latest_version'],
                        'deployment_type': db['deployment_type'],
                        'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(db['defined_tags']),
                        'info': "ocpus:" + str(db['cpu_core_count']),
                        'id': db['id']
                    }

                    self.csv_db_goldengate_deployments.append(gg)
                    self.__csv_add_service(gg, "Golden Gate", col_name="display_name")

        except Exception as e:
            self.__print_error("__csv_database_goldengate", e)

    ##########################################################################
    # __csv_database_mysql
    ##########################################################################

    def __csv_database_mysql(self, region_name, mysql):
        try:
            for db in mysql:
                var = {
                    'region_name': region_name,
                    'compartment_name': db['compartment_name'],
                    'compartment_path': db['compartment_path'],
                    'compartment_id': db['compartment_id'],
                    'display_name': db['display_name'],
                    'description': db['description'],
                    'is_highly_available': db['is_highly_available'],
                    'current_placement': db['current_placement'],
                    'is_analytics_cluster_attached': '',
                    'analytics_cluster': '',
                    'is_heat_wave_cluster_attached': db['is_heat_wave_cluster_attached'],
                    'heat_wave_cluster': db['heat_wave_cluster'],
                    'availability_domain': db['availability_domain'],
                    'fault_domain': db['fault_domain'],
                    'endpoints': db['endpoints'],
                    'endpoints_text': db['endpoints_text'],
                    'lifecycle_state': db['lifecycle_state'],
                    'mysql_version': db['mysql_version'],
                    'time_created': db['time_created'],
                    'time_updated': db['time_updated'],
                    'deletion_policy': db['deletion_policy'],
                    'shape_name': db['shape_name'],
                    'shape_ocpu': db['shape_ocpu'],
                    'shape_memory_gb': db['shape_memory_gb'],
                    'crash_recovery': db['crash_recovery'],
                    'backup_is_enabled': db['backup_is_enabled'],
                    'sum_info': db['sum_info'],
                    'sum_info_storage': db['sum_info_storage'],
                    'sum_size_gb': db['sum_size_gb'],
                    'subnet_id': db['subnet_id'],
                    'subnet_name': db['subnet_name'],
                    'configuration_id': db['configuration_id'],
                    'source': db['source'],
                    'hostname_label': db['hostname_label'],
                    'ip_address': db['ip_address'],
                    'port': db['port'],
                    'port_x': db['port_x'],
                    'channels': db['channels'],
                    'maintenance': db['maintenance'],
                    'time_earliest_recovery_point': db['time_earliest_recovery_point'],
                    'time_latest_recovery_point': db['time_latest_recovery_point'],
                    'data_storage_size_in_gbs': db['data_storage_size_in_gbs'],
                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                    'info': db['shape_name'] + ":" + str(db['shape_ocpu']) + ":" + str(db['shape_memory_gb']),
                    'id': db['id']
                }

                self.csv_db_mysql.append(var)
                self.__csv_add_service(var, "MySQL", col_name="display_name")

                for bk in db['backups']:
                    varb = {
                        'region_name': region_name,
                        'compartment_name': bk['compartment_name'],
                        'compartment_path': bk['compartment_path'],
                        'compartment_id': bk['compartment_id'],
                        'system_name': db['display_name'],
                        'display_name': bk['display_name'],
                        'description': bk['description'],
                        'db_system_id': bk['db_system_id'],
                        'time_created': bk['time_created'],
                        'lifecycle_state': bk['lifecycle_state'],
                        'backup_type': bk['backup_type'],
                        'creation_type': bk['creation_type'],
                        'data_storage_size_in_gbs': bk['data_storage_size_in_gbs'],
                        'backup_size_in_gbs': bk['backup_size_in_gbs'],
                        'retention_in_days': bk['retention_in_days'],
                        'mysql_version': bk['mysql_version'],
                        'shape_name': bk['shape_name'],
                        'freeform_tags': self.__get_freeform_tags(bk['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(bk['defined_tags']),
                        'id': bk['id']
                    }

                    self.csv_db_mysql_backups.append(varb)

        except Exception as e:
            self.__print_error("__csv_database_mysql", e)

    ##########################################################################
    # __csv_database_mysql_standalone_backups
    ##########################################################################

    def __csv_database_mysql_standalone_backups(self, region_name, mysql):
        try:
            for bk in mysql:
                varb = {
                    'region_name': region_name,
                    'compartment_name': bk['compartment_name'],
                    'compartment_path': bk['compartment_path'],
                    'compartment_id': bk['compartment_id'],
                    'system_name': "(Not Exist)",
                    'display_name': bk['display_name'],
                    'description': bk['description'],
                    'db_system_id': bk['db_system_id'],
                    'time_created': bk['time_created'],
                    'lifecycle_state': bk['lifecycle_state'],
                    'backup_type': bk['backup_type'],
                    'creation_type': bk['creation_type'],
                    'data_storage_size_in_gbs': bk['data_storage_size_in_gbs'],
                    'backup_size_in_gbs': bk['backup_size_in_gbs'],
                    'retention_in_days': bk['retention_in_days'],
                    'mysql_version': bk['mysql_version'],
                    'shape_name': bk['shape_name'],
                    'freeform_tags': self.__get_freeform_tags(bk['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(bk['defined_tags']),
                    'id': bk['id']
                }

                self.csv_db_mysql_backups.append(varb)

        except Exception as e:
            self.__print_error("__csv_database_mysql_standalone_backups", e)

    ##########################################################################
    # __csv_database_postgresql
    ##########################################################################

    def __csv_database_postgresql(self, region_name, postgresql):
        try:
            for db in postgresql:
                var = {
                    'region_name': region_name,
                    'compartment_name': db['compartment_name'],
                    'compartment_path': db['compartment_path'],
                    'compartment_id': db['compartment_id'],
                    'display_name': db['display_name'],
                    'system_type': db['system_type'],
                    'instance_count': db['instance_count'],
                    'instance_ocpu_count': db['instance_ocpu_count'],
                    'instance_memory_size_in_gbs': db['instance_memory_size_in_gbs'],
                    'db_version': db['db_version'],
                    'config_id': db['config_id'],
                    'shape': db['shape_full'],
                    'admin_username': db['admin_username'],
                    'storage_system_type': db['storage_system_type'],
                    'instances': self.__csv_list_to_str(db['instances'], 'display_name'),
                    'storage_is_regionally_durable': db['storage_is_regionally_durable'],
                    'storage_availability_domain': db['storage_availability_domain'],
                    'storage_iops': db['storage_iops'],
                    'network_subnet_id': db['network_subnet_id'],
                    'network_subnet_name': db['network_subnet_name'],
                    'network_primary_db_endpoint_private_ip': db['network_primary_db_endpoint_private_ip'],
                    'network_nsg_ids': self.__csv_list_to_str(db['network_nsg_ids']),
                    'network_nsg_names': self.__csv_list_to_str(db['network_nsg_names']),
                    'management_maintenance_window_start': db['management_maintenance_window_start'],
                    'management_backup_policy': db['management_backup_policy'],
                    'source_type': db['source_type'],
                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                    'info': db['shape'],
                    'id': db['id']
                }

                self.csv_db_postgresql.append(var)
                self.__csv_add_service(var, "Golden Gate", col_name="PostgreSQL")

                for bk in db['backups']:
                    varb = {
                        'region_name': region_name,
                        'compartment_name': bk['compartment_name'],
                        'compartment_path': bk['compartment_path'],
                        'compartment_id': bk['compartment_id'],
                        'system_name': db['display_name'],
                        'display_name': bk['display_name'],
                        'db_system_id': bk['db_system_id'],
                        'time_created': bk['time_created'],
                        'time_updated': bk['time_updated'],
                        'lifecycle_state': bk['lifecycle_state'],
                        'lifecycle_details': bk['lifecycle_details'],
                        'source_type': bk['source_type'],
                        'backup_size': bk['backup_size'],
                        'retention_period': bk['retention_period'],
                        'freeform_tags': self.__get_freeform_tags(bk['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(bk['defined_tags']),
                        'id': bk['id']
                    }

                    self.csv_db_postgresql_backups.append(varb)

        except Exception as e:
            self.__print_error("__csv_database_postgresql", e)

    ##########################################################################
    # __csv_database_postgresql
    ##########################################################################

    def __csv_database_postgresql_standalone_backups(self, region_name, postgresql):
        try:
            for bk in postgresql:
                varb = {
                    'region_name': region_name,
                    'compartment_name': bk['compartment_name'],
                    'compartment_path': bk['compartment_path'],
                    'compartment_id': bk['compartment_id'],
                    'system_name': "(Not Exist)",
                    'display_name': bk['display_name'],
                    'db_system_id': bk['db_system_id'],
                    'time_created': bk['time_created'],
                    'time_updated': bk['time_updated'],
                    'lifecycle_state': bk['lifecycle_state'],
                    'lifecycle_details': bk['lifecycle_details'],
                    'source_type': bk['source_type'],
                    'backup_size': bk['backup_size'],
                    'retention_period': bk['retention_period'],
                    'freeform_tags': self.__get_freeform_tags(bk['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(bk['defined_tags']),
                    'id': bk['id']
                }

                self.csv_db_postgresql_backups.append(varb)

        except Exception as e:
            self.__print_error("__csv_database_postgresql_standalone_backups", e)

    ##########################################################################
    # __csv_database_nosql
    ##########################################################################

    def __csv_database_nosql(self, region_name, nosqls):
        try:
            for db in nosqls:
                arr = {
                    'region_name': region_name,
                    'compartment_name': db['compartment_name'],
                    'compartment_path': db['compartment_path'],
                    'name': db['name'],
                    'time_created': db['time_created'],
                    'time_updated': db['time_updated'],
                    'lifecycle_state': db['lifecycle_state'],
                    'is_auto_reclaimable': db['is_auto_reclaimable'],
                    'time_of_expiration': db['time_of_expiration'],
                    'capacity_mode': db['capacity_mode'],
                    'max_read_units': db['max_read_units'],
                    'max_write_units': db['max_write_units'],
                    'max_storage_in_g_bs': db['max_storage_in_g_bs'],
                    'freeform_tags': self.__get_freeform_tags(db['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                    'id': db['id']
                }

                self.csv_db_nosql.append(arr)
                self.__csv_add_service(arr, "NOSQL")

        except Exception as e:
            self.__print_error("__csv_database_goldengate", e)

    ##########################################################################
    # __csv_datasafe_get_target_info
    ##########################################################################
    def __csv_datasafe_get_target_info(self, targets, target_id):
        try:
            for tg in targets:
                if tg['id'] == target_id:
                    return tg['display_name'] + ":" + tg['infrastructure_type'] + ":" + tg['database_type']
            return ""

        except Exception as e:
            self.__print_error("__csv_datasafe_get_target_info", e)

    ##########################################################################
    # __csv_datasafe
    ##########################################################################
    def __csv_datasafe(self, region_name, list_datasafe):
        try:
            issue_location = ""
            for ds in list_datasafe:
                config = ds['global_config']

                # Targets
                issue_location = "targets"
                for target in ds['targets']:
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'display_name': target['display_name'],
                        'description': target['description'],
                        'infrastructure_type': target['infrastructure_type'],
                        'database_type': target['database_type'],
                        'lifecycle_state': target['lifecycle_state'],
                        'lifecycle_details': target['lifecycle_details'],
                        'time_created': target['time_created'],
                        'associated_resource_ids': self.__csv_list_to_str(target['associated_resource_ids']),
                        'associated_resource_names': self.__csv_list_to_str(target['associated_resource_names']),
                        'freeform_tags': self.__get_freeform_tags(target['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(target['defined_tags']),
                        'global_ip_address': config['data_safe_nat_gateway_ip_address'],
                        'global_is_paid_usage': config['is_paid_usage'],
                        'global_is_enabled': config['is_enabled'],
                        'global_time_enabled': config['time_enabled'],
                        'global_lifecycle_state': config['lifecycle_state'],
                        'id': target['id']
                    }

                    self.csv_datasafe_targets.append(arr)
                    self.__csv_add_service(arr, "Datasafe Target")

                # Audit Profiled
                issue_location = "audit_profiles"
                for adt in ds['audit_profiles']:
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'display_name': adt['display_name'],
                        'description': adt['description'],
                        'audit_collected_volume': adt['audit_collected_volume'],
                        'is_override_global_retention_setting': adt['is_override_global_retention_setting'],
                        'is_paid_usage_enabled': adt['is_paid_usage_enabled'],
                        'online_months': adt['online_months'],
                        'offline_months': adt['offline_months'],
                        'target_id': adt['target_id'],
                        'target_name': self.__csv_datasafe_get_target_info(ds['targets'], adt['target_id']),
                        'time_created': adt['time_created'],
                        'lifecycle_state': adt['lifecycle_state'],
                        'lifecycle_details': adt['lifecycle_details'],
                        'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                        'id': adt['id']
                    }

                    self.csv_datasafe_audit_profiles.append(arr)
                    self.__csv_add_service(arr, "Datasafe Audit Profiles")

                # Audit Policies
                issue_location = "audit_policies"
                for adt in ds['audit_policies']:
                    for spc in adt['audit_specifications']:
                        arr = {
                            'region_name': region_name,
                            'compartment_name': ds['compartment_name'],
                            'compartment_path': ds['compartment_path'],
                            'display_name': adt['display_name'],
                            'description': adt['description'],
                            'is_data_safe_service_account_excluded': adt['is_data_safe_service_account_excluded'],
                            'audit_policy_category': spc['audit_policy_category'],
                            'audit_policy_name': spc['audit_policy_name'],
                            'database_policy_names': self.__csv_list_to_str(spc['database_policy_names']),
                            'enable_status': spc['enable_status'],
                            'enabled_entities': spc['enabled_entities'],
                            'is_created': spc['is_created'],
                            'is_enabled_for_all_users': spc['is_enabled_for_all_users'],
                            'is_seeded_in_data_safe': spc['is_seeded_in_data_safe'],
                            'is_seeded_in_target': spc['is_seeded_in_target'],
                            'is_view_only': spc['is_view_only'],
                            'partially_enabled_msg': spc['partially_enabled_msg'],
                            'time_created': adt['time_created'],
                            'lifecycle_state': adt['lifecycle_state'],
                            'lifecycle_details': adt['lifecycle_details'],
                            'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                            'id': adt['id']
                        }

                        self.csv_datasafe_audit_policies.append(arr)

                # Alert Policies
                issue_location = "alert_policies"
                for adt in ds['alert_policies']:
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'display_name': adt['display_name'],
                        'description': adt['description'],
                        'alert_policy_type': adt['alert_policy_type'],
                        'severity': adt['severity'],
                        'is_user_defined': adt['is_user_defined'],
                        'time_created': adt['time_created'],
                        'lifecycle_state': adt['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                        'id': adt['id']
                    }

                    self.csv_datasafe_alert_profiles.append(arr)

                # Connectors
                issue_location = "on_prem_connectors"
                for adt in ds['on_prem_connectors']:
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'type': "On Prem Connector",
                        'display_name': adt['display_name'],
                        'description': adt['description'],
                        'time_created': adt['time_created'],
                        'lifecycle_state': adt['lifecycle_state'],
                        'lifecycle_details': adt['lifecycle_details'],
                        'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                        'id': adt['id']
                    }

                    self.csv_datasafe_connectors.append(arr)

                # Connectors
                issue_location = "private_endpoints"
                for adt in ds['private_endpoints']:
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'type': "Private End Point",
                        'display_name': adt['display_name'],
                        'description': adt['description'],
                        'time_created': adt['time_created'],
                        'lifecycle_state': adt['lifecycle_state'],
                        'lifecycle_details': adt['lifecycle_details'],
                        'subnet_id': adt['subnet_id'],
                        'subnet_name': adt['subnet_name'],
                        'vcn_id': adt['vcn_id'],
                        'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                        'id': adt['id']
                    }

                    self.csv_datasafe_connectors.append(arr)

                # User Assesments
                issue_location = "user_assessments"
                for adt in ds['user_assessments']:
                    stats = adt['statistics']
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'display_name': adt['display_name'],
                        'description': adt['description'],
                        'ignored_assessment_ids': self.__csv_list_to_str(adt['ignored_assessment_ids']),
                        'ignored_targets': self.__csv_list_to_str(adt['ignored_targets']),
                        'is_baseline': adt['is_baseline'],
                        'is_deviated_from_baseline': adt['is_deviated_from_baseline'],
                        'last_compared_baseline_id': adt['last_compared_baseline_id'],
                        'schedule': adt['schedule'],
                        'schedule_assessment_id': adt['schedule_assessment_id'],
                        'stat_critical': str(stats['critical']) if 'critical' in stats else "",
                        'stat_high': str(stats['high']) if 'high' in stats else "",
                        'stat_medium': str(stats['medium']) if 'medium' in stats else "",
                        'stat_low': str(stats['low']) if 'low' in stats else "",
                        'triggered_by': adt['triggered_by'],
                        'time_created': adt['time_created'],
                        'lifecycle_state': adt['lifecycle_state'],
                        'lifecycle_details': adt['lifecycle_details'],
                        'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                        'id': adt['id']
                    }

                    self.csv_datasafe_user_assessment.append(arr)

                # Security Assesments
                issue_location = "security_assessments"
                for adt in ds['security_assessments']:
                    stats = adt['statistics']
                    arr = {
                        'region_name': region_name,
                        'compartment_name': ds['compartment_name'],
                        'compartment_path': ds['compartment_path'],
                        'display_name': adt['display_name'],
                        'description': adt['description'],
                        'ignored_assessment_ids': self.__csv_list_to_str(adt['ignored_assessment_ids']),
                        'ignored_target_ids': self.__csv_list_to_str(adt['ignored_target_ids']),
                        'is_baseline': adt['is_baseline'],
                        'is_deviated_from_baseline': adt['is_deviated_from_baseline'],
                        'last_compared_baseline_id': adt['last_compared_baseline_id'],
                        'link': adt['link'],
                        'schedule': adt['schedule'],
                        'schedule_security_assessment_id': adt['schedule_security_assessment_id'],
                        'stat_advisory': str(stats['advisory']) if 'advisory' in stats else "",
                        'stat_deferred': str(stats['deferred']) if 'deferred' in stats else "",
                        'stat_evaluate': str(stats['evaluate']) if 'evaluate' in stats else "",
                        'stat_high': str(stats['high_risk']) if 'high_risk' in stats else "",
                        'stat_medium': str(stats['medium_risk']) if 'medium_risk' in stats else "",
                        'stat_low': str(stats['low_risk']) if 'low_risk' in stats else "",
                        'targets_count': str(stats['targets_count']) if 'targets_count' in stats else "",
                        'triggered_by': adt['triggered_by'],
                        'time_created': adt['time_created'],
                        'lifecycle_state': adt['lifecycle_state'],
                        'lifecycle_details': adt['lifecycle_details'],
                        'freeform_tags': self.__get_freeform_tags(adt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(adt['defined_tags']),
                        'id': adt['id']
                    }

                    self.csv_datasafe_security_assessment.append(arr)

        except Exception as e:
            self.__print_error("__csv_datasafe: " + issue_location, e)

    ##########################################################################
    # database
    ##########################################################################

    def __csv_database_main(self, region_name, list_databases):
        try:

            if len(list_databases) == 0:
                return

            if 'exadata_infrastructure' in list_databases:
                self.__csv_database_db_exadata(region_name, list_databases['exadata_infrastructure'])
                self.__csv_database_db_autonomous_dedicated(region_name, list_databases['exadata_infrastructure'])
                self.__csv_database_db_autonomous_databases(region_name, list_databases['exadata_infrastructure'])

            if 'exacc_infrastructure' in list_databases:
                self.__csv_database_db_exacc(region_name, list_databases['exacc_infrastructure'])
                self.__csv_database_db_exacc_autonomous_dedicated(region_name, list_databases['exacc_infrastructure'])
                self.__csv_database_db_autonomous_databases(region_name, list_databases['exacc_infrastructure'])

            if 'db_system' in list_databases:
                self.__csv_database_db_system(region_name, list_databases['db_system'])

            if 'exascale' in list_databases:
                self.__csv_database_db_exascale(region_name, list_databases['exascale'])

            if 'db_all_backups' in list_databases:
                self.__csv_database_db_backups(region_name, list_databases['db_all_backups'])

            if 'autonomous' in list_databases:
                self.__csv_database_db_autonomous(region_name, list_databases['autonomous'])

            if 'goldengate' in list_databases:
                self.__csv_database_goldengate(region_name, list_databases['goldengate'])

            if 'nosql' in list_databases:
                self.__csv_database_nosql(region_name, list_databases['nosql'])

            if 'mysql' in list_databases:
                self.__csv_database_mysql(region_name, list_databases['mysql'])

            if 'mysql_standalone_backups' in list_databases:
                self.__csv_database_mysql_standalone_backups(region_name, list_databases['mysql_standalone_backups'])

            if 'postgresql' in list_databases:
                self.__csv_database_postgresql(region_name, list_databases['postgresql'])

            if 'postgresql_standalone_backups' in list_databases:
                self.__csv_database_postgresql_standalone_backups(region_name, list_databases['postgresql_standalone_backups'])

            if 'datasafe_targets' in list_databases:
                self.__csv_datasafe_targets(region_name, list_databases['datasafe_targets'])

            if 'datasafe' in list_databases:
                self.__csv_datasafe(region_name, list_databases['datasafe'])

        except Exception as e:
            self.__print_error("__print_database_main", e)

    ##########################################################################
    # Limits
    ##########################################################################
    def __csv_limits_main(self, region_name, limits):

        try:
            if not limits:
                return

            for lt in limits:
                data = {
                    'region_name': region_name,
                    'scope_type': lt['scope_type'],
                    'availability_domain': lt['availability_domain'],
                    'name': lt['name'],
                    'description': lt['description'],
                    'limit_name': lt['limit_name'],
                    'value': lt['value'],
                    'used': lt['used'],
                    'available': lt['available'],
                    'id': self.tenant_name + ":" + lt['region_name'] + ":" + lt['scope_type'] + ":" + lt['availability_domain'] + ":" + lt['name'] + ":" + lt['limit_name']
                }

                self.csv_limits.append(data)

        except Exception as e:
            self.__print_error("__csv_limits_main", e)

    ##########################################################################
    # quotas
    ##########################################################################
    def __csv_quotas_main(self, region_name, quotas):

        try:
            if not quotas:
                return

            for lt in quotas:
                data = {'region_name': lt['region_name'],
                        'id': lt['id'],
                        'name': lt['name'],
                        'description': lt['description'],
                        'statements': str(',\n'.join(x for x in lt['statements'])),
                        'time_created': lt['time_created'][0:16],
                        'compartment_name': lt['compartment_name'],
                        'compartment_path': lt['compartment_path'],
                        'compartment_id': lt['compartment_id'],
                        'freeform_tags': self.__get_freeform_tags(lt['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(lt['defined_tags'])
                        }

                self.csv_quotas.append(data)

        except Exception as e:
            self.__print_error("__csv_quotas_main", e)

    ##########################################################################
    # csv compute instances
    ##########################################################################
    def __csv_core_compute_instances(self, region_name, instances):

        try:

            if len(instances) == 0:
                return

            for instance in instances:
                data = {'region_name': region_name,
                        'availability_domain': instance['availability_domain'],
                        'compartment_name': instance['compartment_name'],
                        'compartment_path': instance['compartment_path'],
                        'server_name': instance['display_name'],
                        'status': instance['lifecycle_state'],
                        'type': instance['image_os'],
                        'image': instance['image'],
                        'fault_domain': instance['fault_domain'],
                        'primary_vcn': "",
                        'primary_subnet': "",
                        'shape': instance['shape'],
                        'is_live_migration_preferred': instance['is_live_migration_preferred'],
                        'recovery_action': instance['recovery_action'],
                        'ocpus': instance['shape_ocpu'],
                        'memory_gb': instance['shape_memory_gb'],
                        'baseline_ocpu_utilization': instance['shape_baseline_ocpu_utilization'],
                        'gpus': instance['shape_gpus'],
                        'gpu_description': instance['shape_gpu_description'],
                        'processor_description': instance['shape_processor_description'],
                        'max_vnic_attachments': instance['shape_max_vnic_attachments'],
                        'networking_bandwidth_in_gbps': instance['shape_networking_bandwidth_in_gbps'],
                        'launch_mode': instance['launch_mode'],
                        'launch_boot_volume_type': instance['launch_boot_volume_type'],
                        'launch_firmware': instance['launch_firmware'],
                        'launch_network_type': instance['launch_network_type'],
                        'launch_remote_data_volume_type': instance['launch_remote_data_volume_type'],
                        'launch_is_pv_encryption_in_transit_enabled': instance['launch_is_pv_encryption_in_transit_enabled'],
                        'launch_is_consistent_volume_naming_enabled': instance['launch_is_consistent_volume_naming_enabled'],
                        'are_legacy_imds_endpoints_disabled': instance['are_legacy_imds_endpoints_disabled'],
                        'is_cross_numa_node': instance['is_cross_numa_node'],
                        'platform_type': instance['platform_type'],
                        'platform_is_secure_boot_enabled': instance['platform_is_secure_boot_enabled'],
                        'platform_is_trusted_platform_module_enabled': instance['platform_is_trusted_platform_module_enabled'],
                        'platform_is_measured_boot_enabled': instance['platform_is_measured_boot_enabled'],
                        'platform_is_memory_encryption_enabled': instance['platform_is_memory_encryption_enabled'],
                        'local_storage_tb': instance['shape_storage_tb'],
                        'public_ips': str(', '.join(x['details']['public_ip'] for x in instance['vnic'])),
                        'private_ips': str(', '.join(x['details']['private_ip'] for x in instance['vnic'])),
                        'security_groups': str(', '.join(x['details']['nsg_names'] for x in instance['vnic'])),
                        'security_groups_ids': str(','.join(self.__csv_list_to_str(x['details']['nsg_ids']) for x in instance['vnic'])),
                        'internal_fqdn': str(', '.join(x['details']['internal_fqdn'] for x in instance['vnic'])),
                        'plugin_status': str(', '.join(x['name'] + ":" + x['status'] for x in instance['agent_plugin_status'])),
                        'time_created': instance['time_created'][0:16],
                        'boot_volume': "",
                        'boot_volume_id': "",
                        'boot_volume_size_gb': "",
                        'boot_volume_b_policy': "",
                        'boot_volume_transit_encryption': "",
                        'boot_volume_encryption_in_transit_type': "",
                        'block_volumes': "",
                        'block_volumes_ids': "",
                        'block_volumes_total_gb': "",
                        'block_volumes_size_gb': "",
                        'block_volumes_b_policy': "",
                        'block_volumes_attachment_type': "",
                        'block_volumes_transit_encryption': "",
                        'block_volumes_iscsi_login_state': "",
                        'block_volumes_is_multipath': "",
                        'block_volumes_is_read_only': "",
                        'vnic_ids': "",
                        'time_maintenance_reboot_due': instance['time_maintenance_reboot_due'],
                        'licensing_configs': str(instance['licensing_configs']),
                        'freeform_tags': self.__get_freeform_tags(instance['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(instance['defined_tags']),
                        'instance_id': instance['id'],
                        'info': instance['shape'] + ":" + str(instance['shape_ocpu']) + ":" + str(instance['shape_memory_gb']),
                        'id': instance['id']
                        }

                # add columns for csvcol parameter
                for csvcol in self.csv_columns:
                    if str(csvcol).lstrip():
                        data[csvcol] = self.__get_defined_tags_key_value(instance['defined_tags'], csvcol)

                # go over the vnics
                if 'vnic' in instance:
                    data['vnic_ids'] = self.__csv_list_to_str(instance['vnic'], 'id')

                    vnic_num = 0
                    for vnic in instance['vnic']:
                        vnic_num += 1

                        # for vnic #1 add primary vcn_subnet
                        if vnic_num == 1:
                            data['primary_vcn'] = vnic['details']['vcn']
                            data['primary_subnet'] = vnic['details']['subnet']

                if 'boot_volume' in instance:
                    for bv in instance['boot_volume']:
                        data['boot_volume_id'] = bv['id']
                        data['boot_volume'] = bv['display_name']
                        data['boot_volume_size_gb'] = bv['sum_size_gb']
                        data['boot_volume_b_policy'] = bv['backup_policy']
                        data['boot_volume_transit_encryption'] = bv['is_pv_encryption_in_transit_enabled']
                        data['boot_volume_encryption_in_transit_type'] = bv['encryption_in_transit_type']

                if 'block_volume' in instance:
                    data['block_volumes'] = self.__csv_list_to_str(instance['block_volume'], 'display_name')
                    data['block_volumes_ids'] = self.__csv_list_to_str(instance['block_volume'], 'id')
                    data['block_volumes_size_gb'] = self.__csv_list_to_str(instance['block_volume'], 'size')
                    data['block_volumes_b_policy'] = self.__csv_list_to_str(instance['block_volume'], 'backup_policy')
                    data['block_volumes_attachment_type'] = self.__csv_list_to_str(instance['block_volume'], 'attachment_type')
                    data['block_volumes_transit_encryption'] = self.__csv_list_to_str(instance['block_volume'], 'is_pv_encryption_in_transit_enabled')
                    data['block_volumes_iscsi_login_state'] = self.__csv_list_to_str(instance['block_volume'], 'iscsi_login_state')
                    data['block_volumes_is_multipath'] = self.__csv_list_to_str(instance['block_volume'], 'is_multipath')
                    data['block_volumes_is_read_only'] = self.__csv_list_to_str(instance['block_volume'], 'is_read_only')

                    bv_total_size = 0
                    for bv in instance['block_volume']:
                        bv_total_size += int(bv['size'])
                    data['block_volumes_total_gb'] = str(bv_total_size)

                self.csv_compute.append(data)
                self.__csv_add_service(data, "Compute Instance", col_name="server_name")

        except Exception as e:
            self.__print_error("__csv_core_compute_instances", e)

    ##########################################################################
    # csv compute block volumes
    ##########################################################################
    def __csv_core_compute_block_volumes(self, region_name, instances):

        try:
            if len(instances) == 0:
                return

            for instance in instances:

                # Add boot Volumes
                if 'boot_volume' in instance:
                    for bv in instance['boot_volume']:
                        data = {
                            'region_name': region_name,
                            'availability_domain': instance['availability_domain'],
                            'compartment_name': bv['compartment_name'],
                            'compartment_path': bv['compartment_path'],
                            'display_name': bv['display_name'],
                            'size': bv['size'],
                            'backup_policy': bv['backup_policy'],
                            'vpus_per_gb': bv['vpus_per_gb'],
                            'volume_group_name': bv['volume_group_name'],
                            'instance_name': instance['display_name'],
                            'is_auto_tune_enabled': bv['is_auto_tune_enabled'],
                            'auto_tuned_vpus_per_gb': bv['auto_tuned_vpus_per_gb'],
                            'is_pv_encryption_in_transit_enabled': bv['is_pv_encryption_in_transit_enabled'],
                            'encryption_in_transit_type': bv['encryption_in_transit_type'],
                            'is_hydrated': bv['is_hydrated'],
                            'kms_key_id': bv['kms_key_id'],
                            'kms_key_name': bv['kms_key_name'],
                            'is_read_only': "",
                            'is_shareable': "",
                            'is_multipath': "",
                            'iscsi_login_state': "",
                            'bv_volume_replicas': ",".join(x['display_name'] + ":" + x['availability_domain'] for x in bv['bv_volume_replicas']),
                            'instance_id': instance['id'],
                            'id': bv['id'] + ((":" + instance['id']) if instance['id'] else ""),
                            'bv_id': bv['id'],
                            'info': "size:" + str(bv['size']),
                            'freeform_tags': self.__get_freeform_tags(bv['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(bv['defined_tags'])
                        }
                        self.csv_block_volumes.append(data)
                        self.__csv_add_service(data, "Compute Boot Volume", col_name="display_name")

                # Add block Volumes
                if 'block_volume' in instance:
                    for bv in instance['block_volume']:
                        data = {
                            'region_name': region_name,
                            'availability_domain': instance['availability_domain'],
                            'compartment_name': bv['compartment_name'],
                            'compartment_path': bv['compartment_path'],
                            'display_name': bv['display_name'],
                            'size': bv['size'],
                            'backup_policy': bv['backup_policy'],
                            'vpus_per_gb': bv['vpus_per_gb'],
                            'volume_group_name': bv['volume_group_name'],
                            'instance_name': instance['display_name'],
                            'is_auto_tune_enabled': bv['is_auto_tune_enabled'],
                            'auto_tuned_vpus_per_gb': bv['auto_tuned_vpus_per_gb'],
                            'is_pv_encryption_in_transit_enabled': bv['is_pv_encryption_in_transit_enabled'],
                            'encryption_in_transit_type': "",
                            'is_hydrated': bv['is_hydrated'],
                            'kms_key_id': bv['kms_key_id'],
                            'kms_key_name': bv['kms_key_name'],
                            'is_read_only': bv['is_read_only'],
                            'is_shareable': bv['is_shareable'],
                            'is_multipath': bv['is_multipath'],
                            'iscsi_login_state': bv['iscsi_login_state'],
                            'bv_volume_replicas': ",".join(x['display_name'] + ":" + x['availability_domain'] for x in bv['bv_volume_replicas']),
                            'instance_id': instance['id'],
                            'id': bv['id'] + ((":" + instance['id']) if instance['id'] else ""),
                            'bv_id': bv['id'],
                            'info': "size:" + str(bv['size']),
                            'freeform_tags': self.__get_freeform_tags(bv['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(bv['defined_tags'])
                        }
                        self.csv_block_volumes.append(data)
                        self.__csv_add_service(data, "Compute Volume", col_name="display_name")

        except Exception as e:
            self.__print_error("__csv_core_compute_block_volumes", e)

    ##########################################################################
    # csv compute capacity reservation
    ##########################################################################
    def __csv_core_compute_capacity_reservation(self, region_name, reservations):

        try:
            if len(reservations) == 0:
                return

            for ct in reservations:

                val = {
                    'region_name': region_name,
                    'compartment_name': ct['compartment_name'],
                    'compartment_path': ct['compartment_path'],
                    'compartment_id': ct['compartment_id'],
                    'id': ct['id'],
                    'display_name': ct['display_name'],
                    'lifecycle_state': ct['lifecycle_state'],
                    'availability_domain': ct['availability_domain'],
                    'is_default_reservation': ct['is_default_reservation'],
                    'time_created': ct['time_created'],
                    'reserved_instance_count': str(ct['reserved_instance_count']),
                    'used_instance_count': str(ct['used_instance_count']),
                    'shapes': ",".join(x['instance_shape'] for x in ct['config']),
                    'shapes_capacity': ",".join(x['instance_shape'] + ":Shape OCPUs=" + str(x['ocpus']) + ":Shape Mem=" + str(x['memory_in_gbs']) + " (Reserve=" + str(x['reserved_count']) + ":Use=" + str(x['used_count']) + ")" for x in ct['config']),
                    'freeform_tags': self.__get_freeform_tags(ct['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(ct['defined_tags'])
                }

                self.csv_compute_reservations.append(val)

        except Exception as e:
            self.__print_error("__csv_core_compute_capacity_reservation", e)

    ##########################################################################
    # csv compute block volumes
    ##########################################################################
    def __csv_core_compute_block_not_attached(self, region_name, blocks):

        try:
            if len(blocks) == 0:
                return

            for bv in blocks:

                data = {
                    'region_name': region_name,
                    'availability_domain': bv['availability_domain'],
                    'compartment_name': bv['compartment_name'],
                    'compartment_path': bv['compartment_path'],
                    'id': bv['id'],
                    'kms_key_id': bv['kms_key_id'],
                    'kms_key_name': bv['kms_key_name'],
                    'display_name': bv['display_name'],
                    'size': bv['size'],
                    'backup_policy': bv['backup_policy'],
                    'vpus_per_gb': bv['vpus_per_gb'],
                    'volume_group_name': bv['volume_group_name'],
                    'instance_name': '',
                    'instance_id': '',
                    'bv_volume_replicas': ",".join(x['display_name'] + ":" + x['availability_domain'] for x in bv['bv_volume_replicas']),
                    'info': "size:" + str(bv['size']),
                    'freeform_tags': self.__get_freeform_tags(bv['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(bv['defined_tags'])
                }
                self.csv_block_volumes.append(data)
                self.__csv_add_service(data, "Compute Volume Not Attached", col_name="display_name")

        except Exception as e:
            self.__print_error("__csv_core_compute_block_not_attached", e)

    ##########################################################################
    # csv compute block volumes backups
    ##########################################################################
    def __csv_core_compute_block_volume_backups(self, region_name, blocks):

        try:
            if len(blocks) == 0:
                return

            for bv in blocks:

                data = {
                    'region_name': region_name,
                    'compartment_name': bv['compartment_name'],
                    'compartment_path': bv['compartment_path'],
                    'desc': bv['desc'],
                    'volume_type': bv['volume_type'],
                    'backup_type': bv['backup_type'],
                    'schedule_type': bv['schedule_type'],
                    'source_name': bv['source_name'],
                    'time_created': bv['time_created'],
                    'expiration_time': bv['expiration_time'],
                    'unique_size_in_gbs': bv['unique_size_in_gbs'],
                    'size_in_gbs': bv['size_in_gbs'],
                    'backup_id': bv['id'],
                    'volume_id': bv['volume_id']
                }
                self.csv_block_volumes_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_core_compute_block_volume_backups", e)

    ##########################################################################
    # csv Compute
    ##########################################################################
    def __csv_core_compute_main(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'instances' in data:
                self.__csv_core_compute_instances(region_name, data['instances'])
                self.__csv_core_compute_block_volumes(region_name, data['instances'])

            if 'boot_not_attached' in data:
                self.__csv_core_compute_block_not_attached(region_name, data['boot_not_attached'])

            if 'boot_volume_backup' in data:
                self.__csv_core_compute_block_volume_backups(region_name, data['boot_volume_backup'])

            if 'volume_backup' in data:
                self.__csv_core_compute_block_volume_backups(region_name, data['volume_backup'])

            if 'volume_group_backup' in data:
                self.__csv_core_compute_block_volume_backups(region_name, data['volume_group_backup'])

            if 'capacity_reservation' in data:
                self.__csv_core_compute_capacity_reservation(region_name, data['capacity_reservation'])

            if 'volume_not_attached' in data:
                self.__csv_core_compute_block_not_attached(region_name, data['volume_not_attached'])

        except Exception as e:
            self.__print_error("__csv_core_compute_main", e)

    ##########################################################################
    # csv load balancer config
    ##########################################################################
    def __csv_load_balancer_details(self, region_name, load_balance_obj):
        try:
            lb = load_balance_obj['details']

            # listeners
            if 'listeners' in lb:

                # get error and access log:
                log_errors = ""
                log_access = ""
                for log in load_balance_obj['logs']:
                    if 'error' in log['name']:
                        log_errors = log['name']
                    if 'access' in log['name']:
                        log_access = log['name']

                # load balancers
                data = {
                    'region_name': region_name,
                    'compartment_name': lb['compartment_name'],
                    'compartment_path': lb['compartment_path'],
                    'name': lb['display_name'],
                    'status': lb['status'],
                    'shape': lb['shape_name'],
                    'type': ("Private" if lb['is_private'] else "Public"),
                    'is_preserve_source_destination': "",
                    'nlb_ip_version': "",
                    'is_symmetric_hash_enabled': "",
                    'ip_addresses': self.__csv_list_to_str(lb['ips']),
                    'listeners': self.__csv_list_to_str(lb['listeners'], 'desc'),
                    'log_errors': log_errors,
                    'log_access': log_access,
                    'logs': self.__csv_list_to_str(load_balance_obj['logs'], 'name'),
                    'subnets': self.__csv_list_to_str(lb['subnets']),
                    'nsg_ids': self.__csv_list_to_str(lb['nsg_ids']),
                    'nsg_names': lb['nsg_names'],
                    'time_created': lb['time_created'],
                    'lb_certificates': lb['certificates'],
                    'ssl_cipher_suites': self.__csv_list_to_str(lb['ssl_cipher_suites']),
                    'routing_policies': self.__csv_list_to_str(lb['routing_policies']),
                    'freeform_tags': self.__get_freeform_tags(lb['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(lb['defined_tags']),
                    'loadbalancer_id': lb['id'],
                    'id': lb['id']
                }
                self.csv_load_balancer.append(data)
                self.__csv_add_service(data, "Load Balancer")

                # listeners
                for listener in lb['listeners']:
                    data = {
                        'region_name': region_name,
                        'compartment_name': lb['compartment_name'],
                        'compartment_path': lb['compartment_path'],
                        'name': lb['display_name'],
                        'status': lb['status'],
                        'shape': lb['shape_name'],
                        'type': ("Private" if lb['is_private'] else "Public"),
                        'ip_addresses': self.__csv_list_to_str(lb['ips']),
                        'log_errors': log_errors,
                        'log_access': log_access,
                        'logs': self.__csv_list_to_str(load_balance_obj['logs'], 'name'),
                        'subnets': self.__csv_list_to_str(lb['subnets']),
                        'listener_name': listener['id'],
                        'listener_port': listener['port'],
                        'listener_def_bs': listener['default_backend_set_name'],
                        'listener_ssl': listener['ssl_configuration'],
                        'listener_host': self.__csv_list_to_str(listener['hostname_names']),
                        'listener_path': listener['path_route_set_name'],
                        'listener_rule': self.__csv_list_to_str(listener['rule_set_names']),
                        'time_created': lb['time_created'],
                        'lb_certificates': lb['certificates'],
                        'ssl_cipher_suites': self.__csv_list_to_str(lb['ssl_cipher_suites']),
                        'routing_policies': self.__csv_list_to_str(lb['routing_policies']),
                        'freeform_tags': self.__get_freeform_tags(lb['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(lb['defined_tags']),
                        'loadbalancer_id': lb['id'],
                        'id': lb['id'] + ":" + listener['id']
                    }
                    self.csv_load_balancer_listeners.append(data)

        except Exception as e:
            self.__print_error("__csv_load_balancer_details", e)

    ##########################################################################
    # csv load balancer config
    ##########################################################################
    def __csv_network_load_balancer_main(self, region_name, network_load_balancers):
        try:
            if len(network_load_balancers) == 0:
                return

            for lbs in network_load_balancers:
                if 'details' in lbs:
                    lb = lbs['details']

                    # Load Balancers
                    data = {
                        'region_name': region_name,
                        'compartment_name': lb['compartment_name'],
                        'compartment_path': lb['compartment_path'],
                        'name': lb['display_name'],
                        'shape': 'Network',
                        'status': lb['status'],
                        'time_created': lb['time_created'],
                        'time_updated': lb['time_updated'],
                        'type': "Private" if lb['is_private'] else "Public",
                        'is_preserve_source_destination': lb['is_preserve_source_destination'],
                        'nlb_ip_version': lb['nlb_ip_version'],
                        'is_symmetric_hash_enabled': lb['is_symmetric_hash_enabled'],
                        'subnets': lb['subnet_name'],
                        'nsg_ids': self.__csv_list_to_str(lb['nsg_ids']),
                        'nsg_names': lb['nsg_names'],
                        'ip_addresses': self.__csv_list_to_str(lb['ips']),
                        'loadbalancer_id': lb['id'],
                        'listeners': self.__csv_list_to_str(lb['listeners'], 'csvname'),
                        'freeform_tags': self.__get_freeform_tags(lb['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(lb['defined_tags']),
                        'id': lb['id']
                    }
                    self.csv_load_balancer.append(data)
                    self.__csv_add_service(data, "Network Load Balancer")

                    # Listeners
                    for listener in lb['listeners']:
                        data = {
                            'region_name': region_name,
                            'compartment_name': lb['compartment_name'],
                            'compartment_path': lb['compartment_path'],
                            'name': lb['display_name'],
                            'status': lb['status'],
                            'shape': 'Network',
                            'type': ("Private" if lb['is_private'] else "Public"),
                            'subnets': lb['subnet_name'],
                            'ip_addresses': self.__csv_list_to_str(lb['ips']),
                            'listener_name': listener['id'],
                            'listener_port': listener['port'],
                            'listener_def_bs': listener['default_backend_set_name'],
                            'freeform_tags': self.__get_freeform_tags(lb['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(lb['defined_tags']),
                            'loadbalancer_id': lb['id'],
                            'time_created': lb['time_created'][0:16],
                            'id': lb['id'] + ":" + listener['id']}

                    self.csv_load_balancer_listeners.append(data)

                    for bs in lbs['backendset']:
                        for backend in bs['backends']:
                            data = {'region_name': region_name,
                                    'compartment_name': lb['compartment_name'],
                                    'compartment_path': lb['compartment_path'],
                                    'name': lb['display_name'],
                                    'status': lb['status'],
                                    'shape': 'Network Load Balancer',
                                    'type': ("Private" if lb['is_private'] else "Public"),
                                    'ip_addresses': self.__csv_list_to_str(lb['ips']),
                                    'subnets': lb['subnet_name'],
                                    'bs_name': bs['name'],
                                    'bs_desc': bs['name'],
                                    'bs_status': bs['status'],
                                    'backend_name': backend['name'],
                                    'backend': backend['desc'],
                                    'backend_ip': backend['ip_address'] + ":" + backend['port'],
                                    'loadbalancer_id': lb['id'],
                                    'id': lb['id'] + ":" + bs['name'] + ":" + backend['name'] + ":" + backend['ip_address'] + ":" + backend['port']
                                    }
                            self.csv_load_balancer_bs.append(data)

        except Exception as e:
            self.__print_error("__csv_network_load_balancer_main", e)

    ##########################################################################
    # __csv_apigw
    ##########################################################################
    def __csv_apigw(self, region_name, apigw):
        try:
            for api in apigw:
                for dp in api['deployments']:

                    # get error and access log:
                    log_execution = ""
                    log_access = ""
                    for log in dp['logs']:
                        if 'execution' in log['name']:
                            log_execution = log['name']
                        if 'access' in log['name']:
                            log_access = log['name']

                    data = {
                        'region_name': region_name,
                        'compartment_name': dp['compartment_name'],
                        'compartment_path': dp['compartment_path'],
                        'gw_name': api['display_name'],
                        'gw_endpoint_type': api['endpoint_type'],
                        'gw_hostname': api['hostname'],
                        'gw_subnet_id': api['subnet_id'],
                        'gw_subnet_name': api['subnet_name'],
                        'gw_time_created': api['time_created'],
                        'gw_time_updated': api['time_updated'],
                        'gw_lifecycle_state': api['lifecycle_state'],
                        'gw_nsg_ids': self.__csv_list_to_str(api['nsg_ids']),
                        'gw_nsg_names': api['nsg_names'],
                        'gw_certificate_id': api['certificate_id'],
                        'gw_freeform_tags': self.__get_freeform_tags(api['freeform_tags']),
                        'gw_defined_tags': self.__get_defined_tags(api['defined_tags']),
                        'dp_display_name': dp['display_name'],
                        'path_prefix': dp['path_prefix'],
                        'endpoint': dp['endpoint'],
                        'lifecycle_state': dp['lifecycle_state'],
                        'time_created': dp['time_created'],
                        'time_updated': dp['time_updated'],
                        'freeform_tags': self.__get_freeform_tags(dp['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dp['defined_tags']),
                        'log_execution': log_execution,
                        'log_access': log_access,
                        'logs': self.__csv_list_to_str(dp['logs'], 'name'),
                        'dp_id': dp['id'],
                        'api_id': api['id'],
                        'id': api['id']
                    }
                    self.csv_apigw.append(data)
                    self.__csv_add_service(data, "API Gateway", col_name="gw_name")

        except Exception as e:
            self.__print_error("__csv_apigw", e)

    ##########################################################################
    # csv load balancer backendset
    ##########################################################################
    def __csv_load_balancer_backendset(self, region_name, load_balance_obj):

        try:
            lb = load_balance_obj['details']
            backendset = load_balance_obj['backendset']

            for bs in backendset:
                # list of backends
                if 'backends' in bs:
                    for backend in bs['backends']:

                        # session_persistence
                        session_persistence = ""
                        if 'desc' in bs['session_persistence']:
                            session_persistence = bs['session_persistence']['desc']

                        # ssl_cert
                        ssl_cert = ""
                        if 'desc' in bs['ssl_cert']:
                            ssl_cert = bs['ssl_cert']['desc']

                        data = {
                            'region_name': region_name,
                            'compartment_name': lb['compartment_name'],
                            'compartment_path': lb['compartment_path'],
                            'name': lb['display_name'],
                            'status': lb['status'],
                            'shape': lb['shape_name'],
                            'type': ("Private" if lb['is_private'] else "Public"),
                            'ip_addresses': self.__csv_list_to_str(lb['ips']),
                            'subnets': self.__csv_list_to_str(lb['subnets']),
                            'bs_name': bs['name'],
                            'bs_desc': bs['desc'],
                            'bs_status': bs['status'],
                            'health_check': bs['health_check']['desc1'] + " " + bs['health_check']['desc2'],
                            'session_persistence': session_persistence,
                            'ssl_cert': ssl_cert,
                            'backend_name': backend['name'],
                            'backend': backend['desc'],
                            'backend_ip': backend['ip_address'] + ":" + backend['port'],
                            'loadbalancer_id': lb['id'],
                            'id': lb['id'] + ":" + bs['name'] + ":" + backend['name'] + ":" + backend['ip_address'] + ":" + backend['port']
                        }
                        self.csv_load_balancer_bs.append(data)

        except Exception as e:
            self.__print_error("__csv_load_balancer_backendset", e)

    ##########################################################################
    # Load Balancer
    ##########################################################################

    def __csv_load_balancer_main(self, region_name, load_balancers):
        try:

            if len(load_balancers) == 0:
                return

            for load_balance_obj in load_balancers:
                if 'details' in load_balance_obj:
                    self.__csv_load_balancer_details(region_name, load_balance_obj)

                if 'backendset' in load_balance_obj:
                    self.__csv_load_balancer_backendset(region_name, load_balance_obj)

        except Exception as e:
            self.__print_error("__csv_load_balancer_main", e)

    ##########################################################################
    # File Storage
    ##########################################################################

    def __csv_file_storage_main(self, region_name, file_storage):
        try:

            if len(file_storage) == 0:
                return

            if file_storage:
                for fs in file_storage:

                    mount_ips = ""
                    exports = ""
                    options = ""
                    # list the exports
                    fs_exports = fs['exports']
                    if fs_exports:
                        for ex in fs_exports:
                            if ex['path'] not in exports:
                                exports += ex['path'] + ","

                        ex_options = ex['options']
                        if ex_options:
                            for opt in ex_options:
                                options += str(opt)

                        # list the Ips for each mount
                        ex_mount_target = ex['mount_target']
                        if ex_mount_target:
                            for mnt in ex_mount_target:
                                ip_to_add = self.__csv_list_to_str(mnt['private_ip_ids'])
                                if ip_to_add not in mount_ips:
                                    mount_ips += ip_to_add + ","

                    data = {'region_name': region_name,
                            'compartment_name': fs['compartment_name'],
                            'compartment_path': fs['compartment_path'],
                            'availability_domain': fs['availability_domain'],
                            'display_name': fs['display_name'],
                            'kms_key_id': fs['kms_key_id'],
                            'size_gb': fs['size_gb'],
                            'info': "size:" + str(fs['size_gb']),
                            'id': fs['id'],
                            'time_created': fs['time_created'],
                            'exports': exports,
                            'export_options': options,
                            'mount_ips': mount_ips,
                            'snapshots': self.__csv_list_to_str(fs['snapshots']),
                            'freeform_tags': self.__get_freeform_tags(fs['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(fs['defined_tags'])
                            }

                    self.csv_file_storage.append(data)
                    self.__csv_add_service(data, "File Storage", col_name="display_name")

        except Exception as e:
            self.__print_error("__csv_file_storage_main", e)

    ##########################################################################
    # Object Storage
    ##########################################################################
    def __csv_object_storage_main(self, region_name, object_storage):
        try:

            if len(object_storage) == 0:
                return

            if object_storage:
                for ar in object_storage:

                    data = {
                        'namespace_name': ar['namespace_name'],
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'bucket_name': ar['name'],
                        'objects': ar['count'],
                        'size_gb': ar['sum_size_gb'],
                        'info': "size:" + str(ar['sum_size_gb']),
                        'preauthenticated_requests': ar['preauthenticated_requests'],
                        'object_lifecycle': ar['object_lifecycle'],
                        'public_access_type': ar['public_access_type'],
                        'storage_tier': ar['storage_tier'],
                        'object_events_enabled': ar['object_events_enabled'],
                        'replication_enabled': ar['replication_enabled'],
                        'is_read_only': ar['is_read_only'],
                        'versioning': ar['versioning'],
                        'auto_tiering': ar['auto_tiering'],
                        'kms_key_id': ar['kms_key_id'],
                        'bucket_id': ar['id'],
                        'id': ar['id'],
                        'time_created': ar['time_created'],
                        'error_message': ar['error_message'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'logs': self.__csv_list_to_str(ar['logs'], 'name')
                    }

                    self.csv_object_storage_buckets.append(data)
                    self.__csv_add_service(data, "Object Storage", col_name="bucket_name")

        except Exception as e:
            self.__print_error("__csv_object_storage_main", e)

    ##########################################################################
    # csv Security
    ##########################################################################
    def __csv_security_main(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'bastions' in data:
                self.__csv_security_bastions(region_name, data['bastions'])

            if 'logging' in data:
                self.__csv_security_logging(region_name, data['logging'])

            if 'logging_unified_agents' in data:
                self.__csv_security_logging_unified_agents(region_name, data['logging_unified_agents'])

            if 'cloud_guard' in data:
                self.__csv_security_cloud_guard(region_name, data['cloud_guard'])

            if 'kms_vaults' in data:
                self.__csv_security_kms_vaults(region_name, data['kms_vaults'])

            if 'certificates' in data:
                self.__csv_certificate_certificates(region_name, data['certificates'])

            if 'certificate_authorities' in data:
                self.__csv_certificate_authorities(region_name, data['certificate_authorities'])

            if 'certificate_ca_bundles' in data:
                self.__csv_certificate_ca_bundles(region_name, data['certificate_ca_bundles'])

        except Exception as e:
            self.__print_error("__csv_security_main", e)

    ##########################################################################
    # Bastions
    ##########################################################################
    def __csv_security_bastions(self, region_name, bastions):
        try:

            if len(bastions) == 0:
                return

            if bastions:
                for ar in bastions:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'target_vcn_name': ar['target_vcn_name'],
                        'target_subnet_name': ar['target_subnet_name'],
                        'bastion_type': ar['bastion_type'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'id': ar['id'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'target_vcn_id': ar['target_vcn_id'],
                        'target_subnet_id': ar['target_subnet_id']
                    }

                    self.csv_security_bastions.append(data)
                    self.__csv_add_service(data, "Bastion")

        except Exception as e:
            self.__print_error("__csv_security_bastions", e)

    ##########################################################################
    # Certificates
    ##########################################################################
    def __csv_certificate_certificates(self, region_name, certs):
        try:

            if len(certs) == 0:
                return

            if certs:
                for ar in certs:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'type': 'Certificate',
                        'name': ar['name'],
                        'description': ar['description'],
                        'config_type': ar['config_type'],
                        'time_created': ar['time_created'],
                        'time_of_deletion': ar['time_of_deletion'],
                        'certificate_rules': str(','.join(x['rule_type'] + ":" + x['renewal_interval'] + ":" + x['advance_renewal_period'] for x in ar['certificate_rules'])),
                        'current_certificate_id': ar['current_certificate_id'],
                        'current_serial_number': ar['current_serial_number'],
                        'current_time_created': ar['current_time_created'],
                        'current_version_number': ar['current_version_number'],
                        'current_issuer_ca_version_number': ar['current_issuer_ca_version_number'],
                        'current_version_name': ar['current_version_name'],
                        'current_time_of_deletion': ar['current_time_of_deletion'],
                        'current_validity_not_before': ar['current_validity_not_before'],
                        'current_validity_not_after': ar['current_validity_not_after'],
                        'current_time_of_revocation': ar['current_time_of_revocation'],
                        'current_revocation_reason': ar['current_revocation_reason'],
                        'common_name': ar['common_name'],
                        'country': ar['country'],
                        'domain_component': ar['domain_component'],
                        'distinguished_name_qualifier': ar['distinguished_name_qualifier'],
                        'generation_qualifier': ar['generation_qualifier'],
                        'given_name': ar['given_name'],
                        'locality_name': ar['locality_name'],
                        'organization': ar['organization'],
                        'organizational_unit': ar['organizational_unit'],
                        'pseudonym': ar['pseudonym'],
                        'serial_number': ar['serial_number'],
                        'state_or_province_name': ar['state_or_province_name'],
                        'street': ar['street'],
                        'surname': ar['surname'],
                        'user_id': ar['user_id'],
                        'key_algorithm': ar['key_algorithm'],
                        'signature_algorithm': ar['signature_algorithm'],
                        'certificate_profile_type': ar['certificate_profile_type'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'associated_resource_ids': ar['associated_resource_ids'],
                        'associated_resource_names': ar['associated_resource_names'],
                        'id': ar['id'],
                        'kms_key_id': "",
                        'issuer_certificate_authority_id': ar['issuer_certificate_authority_id'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                    }

                    self.csv_certificates.append(data)
                    self.__csv_add_service(data, "Certificates")

        except Exception as e:
            self.__print_error("__csv_certificate_certificates", e)

    ##########################################################################
    # Certificates Authorities
    ##########################################################################
    def __csv_certificate_authorities(self, region_name, certs):
        try:

            if len(certs) == 0:
                return

            if certs:
                for ar in certs:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'type': 'Certificate Authorities',
                        'name': ar['name'],
                        'description': ar['description'],
                        'config_type': ar['config_type'],
                        'time_created': ar['time_created'],
                        'time_of_deletion': ar['time_of_deletion'],
                        'certificate_rules': str(','.join(x['rule_type'] + ":" + x['leaf_certificate_max_validity_duration'] + ":" + x['certificate_authority_max_validity_duration'] for x in ar['certificate_authority_rules'])),
                        'current_certificate_authority_id': ar['current_certificate_authority_id'],
                        'current_issuer_ca_version_number': ar['current_issuer_ca_version_number'],
                        'current_serial_number': ar['current_serial_number'],
                        'current_time_created': ar['current_time_created'],
                        'current_version_number': ar['current_version_number'],
                        'current_version_name': ar['current_version_name'],
                        'current_time_of_deletion': ar['current_time_of_deletion'],
                        'current_validity_not_before': ar['current_validity_not_before'],
                        'current_validity_not_after': ar['current_validity_not_after'],
                        'current_time_of_revocation': ar['current_time_of_revocation'],
                        'current_revocation_reason': ar['current_revocation_reason'],
                        'common_name': ar['common_name'],
                        'country': ar['country'],
                        'domain_component': ar['domain_component'],
                        'distinguished_name_qualifier': ar['distinguished_name_qualifier'],
                        'generation_qualifier': ar['generation_qualifier'],
                        'given_name': ar['given_name'],
                        'locality_name': ar['locality_name'],
                        'organization': ar['organization'],
                        'organizational_unit': ar['organizational_unit'],
                        'pseudonym': ar['pseudonym'],
                        'serial_number': ar['serial_number'],
                        'state_or_province_name': ar['state_or_province_name'],
                        'street': ar['street'],
                        'surname': ar['surname'],
                        'user_id': ar['user_id'],
                        'signature_algorithm': ar['signing_algorithm'],
                        'key_algorithm': "",
                        'certificate_profile_type': "",
                        'lifecycle_state': ar['lifecycle_state'],
                        'associated_resource_ids': ar['associated_resource_ids'],
                        'associated_resource_names': ar['associated_resource_names'],
                        'id': ar['id'],
                        'kms_key_id': ar['kms_key_id'],
                        'issuer_certificate_authority_id': ar['issuer_certificate_authority_id'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                    }

                    self.csv_certificates.append(data)
                    self.__csv_add_service(data, "Certificates Authorities")

        except Exception as e:
            self.__print_error("__csv_certificate_authorities", e)

    ##########################################################################
    # Certificates CA Bundle
    ##########################################################################
    def __csv_certificate_ca_bundles(self, region_name, certs):
        try:

            if len(certs) == 0:
                return

            if certs:
                for ar in certs:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'associated_resource_ids': ar['associated_resource_ids'],
                        'associated_resource_names': ar['associated_resource_names'],
                        'id': ar['id'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                    }

                    self.csv_certificate_ca_bundle.append(data)
                    self.__csv_add_service(data, "Certificates CA Bundle")

        except Exception as e:
            self.__print_error("__csv_certificate_ca_bundles", e)

    ##########################################################################
    # Cloud Guard
    ##########################################################################
    def __csv_security_cloud_guard(self, region_name, cloud_guards):
        try:

            if len(cloud_guards) == 0:
                return

            if cloud_guards:
                for ar in cloud_guards:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_id': ar['compartment_id'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'target_resource_type': ar['target_resource_type'],
                        'target_resource_id': ar['target_resource_id'],
                        'target_resource_name': ar['target_resource_name'],
                        'inherited_by_compartments': ar['inherited_by_compartments'],
                        'inherited_by_compartments_names': ar['inherited_by_compartments_names'],
                        'target_detector_recipes': self.__csv_list_to_str(ar['target_detector_recipes'], 'display_name'),
                        'target_responder_recipes': self.__csv_list_to_str(ar['target_responder_recipes'], 'display_name'),
                        'target_detector_rules': "",
                        'target_responder_rules': "",
                        'recipe_count': ar['recipe_count'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    # target_detector_rules
                    if ar['target_detector_recipes']:
                        arrrules = []
                        for dt in ar['target_detector_recipes']:
                            for rule in dt['effective_detector_rules']:
                                arrrules.append(rule)
                        data['target_detector_rules'] = self.__csv_list_to_str(list(set(arrrules)))

                    # target_detector_rules
                    if ar['target_responder_recipes']:
                        arrrules = []
                        for dt in ar['target_responder_recipes']:
                            for rule in dt['effective_responder_rules']:
                                arrrules.append(rule)
                        data['target_responder_rules'] = self.__csv_list_to_str(list(set(arrrules)))

                    self.csv_security_cloud_guard.append(data)

        except Exception as e:
            self.__print_error("__csv_security_cloud_guard", e)

    ##########################################################################
    # KMS Vaults
    ##########################################################################
    def __csv_security_kms_vaults(self, region_name, kms_vaults):
        try:

            if len(kms_vaults) == 0:
                return

            if kms_vaults:
                for ar in kms_vaults:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'crypto_endpoint': ar['crypto_endpoint'],
                        'management_endpoint': ar['management_endpoint'],
                        'vault_type': ar['vault_type'],
                        'key_count': ar['key_count'],
                        'key_version_count': ar['key_version_count'],
                        'software_key_count': ar['software_key_count'],
                        'software_key_version_count': ar['software_key_version_count'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'vault_id': ar['id'],
                        'id': ar['id'] + ":" + region_name,
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                    }

                    self.csv_security_kms_vault.append(data)
                    self.__csv_add_service(data, "KMS Vault")

        except Exception as e:
            self.__print_error("__csv_security_kms_vaults", e)

    ##########################################################################
    # Logging
    ##########################################################################
    def __csv_security_logging(self, region_name, log_groups):
        try:

            if len(log_groups) == 0:
                return

            if log_groups:
                for ar in log_groups:
                    for lg in ar['logs']:
                        data = {
                            'region_name': region_name,
                            'compartment_name': ar['compartment_name'],
                            'compartment_path': ar['compartment_path'],
                            'log_group': ar['display_name'],
                            'log_group_description': ar['description'],
                            'log_group_time_last_modified': ar['time_last_modified'][0:16],
                            'log_name': lg['display_name'],
                            'is_enabled': lg['is_enabled'],
                            'lifecycle_state': lg['lifecycle_state'],
                            'log_type': lg['log_type'],
                            'time_created': lg['time_created'][0:16],
                            'retention_duration': lg['retention_duration'],
                            'time_last_modified': lg['time_last_modified'][0:16],
                            'archiving': lg['archiving'],
                            'source_service': lg['source_service'],
                            'source_category': lg['source_category'],
                            'source_sourcetype': lg['source_sourcetype'],
                            'source_resource': lg['source_resource'],
                            'source_parameters': lg['source_parameters'],
                            'log_group_id': ar['id'],
                            'log_id': lg['id'],
                            'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                        }

                        self.csv_security_logging.append(data)

        except Exception as e:
            self.__print_error("__csv_security_logging", e)

    ##########################################################################
    # Logging unified agents
    ##########################################################################
    def __csv_security_logging_unified_agents(self, region_name, logging_unified_agents):
        try:

            if len(logging_unified_agents) == 0:
                return

            if logging_unified_agents:
                for ar in logging_unified_agents:
                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'][0:16],
                        'time_last_modified': ar['time_last_modified'][0:16],
                        'is_enabled': ar['is_enabled'],
                        'configuration_type': ar['configuration_type'],
                        'configuration_state': ar['configuration_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                    }

                    self.csv_security_log_unified_agents.append(data)

        except Exception as e:
            self.__print_error("__csv_security_logging_unified_agents", e)

    ##########################################################################
    # Container
    ##########################################################################
    def __csv_container(self, region_name, containers):
        try:

            if len(containers) == 0:
                return

            # Containers
            if containers:
                for ar in containers:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'vcn': ar['vcn_name'],
                        'node_pools': len(ar['node_pools']),
                        'lifecycle_state': ar['lifecycle_state'],
                        'kubernetes_version': ar['kubernetes_version'],
                        'compartment_id': ar['compartment_id'],
                        'endpoint_is_public_ip_enabled': ar['endpoint_is_public_ip_enabled'],
                        'endpoint_nsg_ids': self.__csv_list_to_str(ar['endpoint_nsg_ids']),
                        'endpoint_nsg_names': ar['endpoint_nsg_names'],
                        'endpoint_subnet_id': ar['endpoint_subnet_id'],
                        'endpoint_subnet_name': ar['endpoint_subnet_name'],
                        'option_lb_ids': ar['option_lb_ids'],
                        'option_network_pods_cidr': ar['option_network_pods_cidr'],
                        'option_network_services_cidr': ar['option_network_services_cidr'],
                        'option_is_kubernetes_dashboard_enabled': ar['option_is_kubernetes_dashboard_enabled'],
                        'option_is_tiller_enabled': ar['option_is_tiller_enabled'],
                        'option_is_pod_security_policy_enabled': ar['option_is_pod_security_policy_enabled'],
                        'time_created': ar['time_created'],
                        'time_deleted': ar['time_deleted'],
                        'time_updated': ar['time_updated'],
                        'created_by_user_id': ar['created_by_user_id'],
                        'deleted_by_user_id': ar['deleted_by_user_id'],
                        'updated_by_user_id': ar['updated_by_user_id'],
                        'endpoint_kubernetes': ar['endpoint_kubernetes'],
                        'endpoint_public_endpoint': ar['endpoint_public_endpoint'],
                        'endpoint_private_endpoint': ar['endpoint_private_endpoint'],
                        'endpoint_vcn_hostname_endpoint': ar['endpoint_vcn_hostname_endpoint'],
                        'available_kubernetes_upgrades': ar['available_kubernetes_upgrades'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id'],
                        'vcn_id': ar['vcn_id'],
                    }

                    self.csv_container.append(data)
                    self.__csv_add_service(data, "OKE Container")

            # Containers nodepools
            if containers:
                for ar in containers:
                    for nd in ar['node_pools']:
                        data = {
                            'region_name': region_name,
                            'compartment_name': ar['compartment_name'],
                            'compartment_path': ar['compartment_path'],
                            'container_name': ar['name'],
                            'node_name': nd['name'],
                            'node_image_name': nd['node_image_name'],
                            'kubernetes_version': nd['kubernetes_version'],
                            'node_shape': nd['node_shape'],
                            'quantity_per_subnet': nd['quantity_per_subnet'],
                            'node_shape_mem_gb': nd['node_shape_mem_gb'],
                            'node_shape_ocpus': nd['node_shape_ocpus'],
                            'node_source_type': nd['node_source_type'],
                            'node_source_name': nd['node_source_name'],
                            'freeform_tags': self.__get_freeform_tags(nd['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(nd['defined_tags']),
                            'vcn': ar['vcn_name'],
                            'subnets': self.__csv_list_to_str(nd['subnets']),
                            'subnet_ids': self.__csv_list_to_str(nd['subnet_ids']),
                            'container_id': ar['id'],
                            'node_pool_id': nd['id'],
                            'vcn_id': ar['vcn_id'],
                        }

                        self.csv_container_nodepool.append(data)

        except Exception as e:
            self.__print_error("__csv_container", e)

    ##########################################################################
    # csv edge
    ##########################################################################
    def __csv_edge_main(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'waas_policies' in data:
                self.__csv_edge_waas_policies(region_name, data['waas_policies'])

            if 'waf' in data:
                self.__csv_edge_waf(region_name, data['waf'])

            if 'dns_steering' in data:
                self.__csv_edge_dns_steering(region_name, data['dns_steering'])

            if 'healthcheck' in data:
                self.__csv_edge_healthcheck(region_name, data['healthcheck'])

        except Exception as e:
            self.__print_error("__csv_edge_main", e)

    ##########################################################################
    # Edge Waas Policies
    ##########################################################################
    def __csv_edge_waas_policies(self, region_name, waas_policies):
        try:

            if len(waas_policies) == 0:
                return

            # WAAS policies
            if waas_policies:
                for ar in waas_policies:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'domain': ar['domain'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'time_created': ar['time_created'][0:16],
                        'id': ar['id']
                    }

                    self.csv_edge_waas_policies.append(data)
                    self.__csv_add_service(data, "WaaS Policies")

        except Exception as e:
            self.__print_error("__csv_edge_waas_policies", e)

    ##########################################################################
    # Edge WAF
    ##########################################################################
    def __csv_edge_waf(self, region_name, waf):
        try:

            if len(waf) == 0:
                return

            # Containers
            if waf:
                for ar in waf:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'backend_type': ar['backend_type'],
                        'web_app_firewall_policy_id': ar['web_app_firewall_policy_id'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'time_updated': ar['time_updated'][0:16],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_edge_waf.append(data)
                    self.__csv_add_service(data, "WAF")

        except Exception as e:
            self.__print_error("__csv_edge_waf", e)

    ##########################################################################
    # Edge DNS Steering
    ##########################################################################
    def __csv_edge_dns_steering(self, region_name, steering_policies):
        try:

            if len(steering_policies) == 0:
                return

            # Containers
            if steering_policies:
                for ar in steering_policies:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'ttl': ar['ttl'],
                        'template': ar['template'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'health_check_monitor_id': ar['health_check_monitor_id'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id'] + ":" + self.tenant_name + ":" + region_name
                    }

                    self.csv_edge_dns_steering_policies.append(data)
                    self.__csv_add_service(data, "DNS Steering Policies")

        except Exception as e:
            self.__print_error("__csv_edge_dns_steering", e)

    ##########################################################################
    # Edge Healthcheck
    ##########################################################################
    def __csv_edge_healthcheck(self, region_name, healthchecks):
        try:

            if 'http' in healthchecks:
                for ar in healthchecks['http']:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'type': 'http',
                        'results_url': ar['results_url'],
                        'targets': ar['targets'],
                        'vantage_point_names': ar['vantage_point_names'],
                        'port': '',
                        'timeout_in_seconds': '',
                        'is_enabled': ar['is_enabled'],
                        'interval_in_seconds': ar['interval_in_seconds'],
                        'protocol': ar['protocol'],
                        'method': ar['method'],
                        'path': ar['path'],
                        'headers': ar['headers'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id'] + ":" + self.tenant_name + ":" + region_name
                    }

                    self.csv_edge_healthcheck.append(data)
                    self.__csv_add_service(data, "Health Check HTTP", col_name="display_name")

            if 'ping' in healthchecks:
                for ar in healthchecks['ping']:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'type': 'ping',
                        'results_url': ar['results_url'],
                        'targets': ar['targets'],
                        'vantage_point_names': ar['vantage_point_names'],
                        'port': ar['port'],
                        'timeout_in_seconds': ar['timeout_in_seconds'],
                        'is_enabled': ar['is_enabled'],
                        'interval_in_seconds': ar['interval_in_seconds'],
                        'protocol': ar['protocol'],
                        'method': '',
                        'path': '',
                        'headers': '',
                        'lifecycle_state': ar['lifecycle_state'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id'] + ":" + self.tenant_name + ":" + region_name
                    }

                    self.csv_edge_healthcheck.append(data)
                    self.__csv_add_service(data, "Health Check Ping")

        except Exception as e:
            self.__print_error("__csv_edge_healthcheck", e)

    ##########################################################################
    # FSDR
    ##########################################################################
    def __csv_fsdr(self, region_name, fsdrs):
        try:

            if len(fsdrs) == 0:
                return

            if fsdrs:
                for ar in fsdrs:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'role': ar['role'],
                        'peer_id': ar['peer_id'],
                        'peer_region': ar['peer_region'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'life_cycle_details': ar['life_cycle_details'],
                        'lifecycle_sub_state': ar['lifecycle_sub_state'],
                        'log_location': ar['log_location'],
                        'members': self.__csv_list_to_str(ar['members'], 'member_id'),
                        'members_raw': self.__csv_list_to_str(ar['members'], 'raw_data'),
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_fsdr.append(data)
                    self.__csv_add_service(data, "FSDR")

        except Exception as e:
            self.__print_error("__csv_paas_oic", e)

    ##########################################################################
    # Paas OIC
    ##########################################################################
    def __csv_paas_oic(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'instance_url': ar['instance_url'],
                        'message_packs': ar['message_packs'],
                        'is_byol': ar['is_byol'],
                        'is_file_server_enabled': ar['is_file_server_enabled'],
                        'is_visual_builder_enabled': ar['is_visual_builder_enabled'],
                        'network_endpoint_type': ar['network_endpoint_type'],
                        'shape': ar['shape'],
                        'consumption_model': ar['consumption_model'],
                        # Added 8/25/2025
                        'integration_instance_type': ar['integration_instance_type'],
                        'network_endpoint_allowlisted_http_ips': ar['network_endpoint_allowlisted_http_ips'],
                        'network_endpoint_allowlisted_http_vcns': ar['network_endpoint_allowlisted_http_vcns'],
                        'network_endpoint_is_integration_vcn_allowlisted': ar['network_endpoint_is_integration_vcn_allowlisted'],
                        'custom_endpoint_hostname': ar['custom_endpoint_hostname'],
                        'custom_endpoint_managed_type': ar['custom_endpoint_managed_type'],
                        'custom_endpoint_dns_zone_name': ar['custom_endpoint_dns_zone_name'],
                        'custom_endpoint_dns_type': ar['custom_endpoint_dns_type'],
                        'custom_endpoint_certificate_secret_id': ar['custom_endpoint_certificate_secret_id'],
                        'custom_endpoint_certificate_secret_version': ar['custom_endpoint_certificate_secret_version'],
                        'custom_endpoint_alias': ar['custom_endpoint_alias'],
                        'private_endpoint_outbound_connection_type': ar['private_endpoint_outbound_connection_type'],
                        'private_endpoint_outbound_connection_subnet_id': ar['private_endpoint_outbound_connection_subnet_id'],
                        'private_endpoint_outbound_connection_subnet_name': ar['private_endpoint_outbound_connection_subnet_name'],
                        'private_endpoint_outbound_connection_nsg_ids': ar['private_endpoint_outbound_connection_nsg_ids'],
                        'is_disaster_recovery_enabled': ar['is_disaster_recovery_enabled'],
                        'data_retention_period': ar['data_retention_period'],
                        'instance_design_time_url': ar['instance_design_time_url'],
                        'idcs_info_app_location_url': ar['idcs_info_app_location_url'],
                        'idcs_info_app_display_name': ar['idcs_info_app_display_name'],
                        'idcs_info_app_id': ar['idcs_info_app_id'],
                        'idcs_info_app_name': ar['idcs_info_app_name'],
                        'idcs_info_instance_primary_audience_url': ar['idcs_info_instance_primary_audience_url'],
                        'attachments': str(ar['attachments']),
                        'disaster_recovery_role': ar['disaster_recovery_role'],
                        'disaster_recovery_regional_instance_url': ar['disaster_recovery_regional_instance_url'],
                        'disaster_recovery_peer_role': ar['disaster_recovery_peer_role'],
                        'disaster_recovery_peer_id': ar['disaster_recovery_peer_id'],
                        'disaster_recovery_peer_time_role_changed': ar['disaster_recovery_peer_time_role_changed'],
                        # End Added
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'info': "msgpack:" + str(ar['message_packs']),
                        'id': ar['id']
                    }

                    self.csv_paas_oic.append(data)
                    self.__csv_add_service(data, "OIC")

        except Exception as e:
            self.__print_error("__csv_paas_oic", e)

    ##########################################################################
    # Streams
    ##########################################################################
    def __csv_streams_queues(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                if 'streams' in services:
                    if services['streams']:
                        for ar in services['streams']:

                            data = {
                                'region_name': region_name,
                                'compartment_name': ar['compartment_name'],
                                'compartment_path': ar['compartment_path'],
                                'type': "STREAM",
                                'name': ar['name'],
                                'partitions': ar['partitions'],
                                'time_created': ar['time_created'][0:16],
                                'lifecycle_state': ar['lifecycle_state'],
                                'lifecycle_details': "",
                                'messages_endpoint': ar['messages_endpoint'],
                                'retention_in_seconds': "",
                                'visibility_in_seconds': "",
                                'timeout_in_seconds': "",
                                'dead_letter_queue_delivery_count': "",
                                'custom_encryption_key_id': "",
                                'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                                'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                                'id': ar['id']
                            }

                            self.csv_streams_queues.append(data)
                            self.__csv_add_service(data, "Stream")

                if 'queues' in services:
                    if services['queues']:
                        for ar in services['queues']:

                            data = {
                                'region_name': region_name,
                                'compartment_name': ar['compartment_name'],
                                'compartment_path': ar['compartment_path'],
                                'type': "QUEUE",
                                'name': ar['name'],
                                'partitions': "",
                                'time_created': ar['time_created'][0:16],
                                'lifecycle_state': ar['lifecycle_state'],
                                'lifecycle_details': ar['lifecycle_details'],
                                'messages_endpoint': ar['messages_endpoint'],
                                'retention_in_seconds': ar['retention_in_seconds'],
                                'visibility_in_seconds': ar['visibility_in_seconds'],
                                'timeout_in_seconds': ar['timeout_in_seconds'],
                                'dead_letter_queue_delivery_count': ar['dead_letter_queue_delivery_count'],
                                'custom_encryption_key_id': ar['custom_encryption_key_id'],
                                'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                                'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                                'id': ar['id']
                            }

                            self.csv_streams_queues.append(data)
                            self.__csv_add_service(data, "Queue")

        except Exception as e:
            self.__print_error("__csv_streams_queues", e)

    ##########################################################################
    # Functions Apps
    ##########################################################################
    def __csv_functions(self, region_name, functions_apps):
        try:

            for ar in functions_apps:
                data = {
                    'region_name': region_name,
                    'compartment_name': ar['compartment_name'],
                    'compartment_path': ar['compartment_path'],
                    'name': ar['display_name'],
                    'lifecycle_state': ar['lifecycle_state'],
                    'subnets': self.__csv_list_to_str(ar['subnets']),
                    'network_security_group_names': ar['network_security_group_names'],
                    'network_security_group_ids': self.__csv_list_to_str(ar['network_security_group_ids']),
                    'shape': ar['shape'],
                    'trace_config_is_enabled': ar['trace_config_is_enabled'],
                    'trace_config_domain_id': ar['trace_config_domain_id'],
                    'image_policy_is_enabled': ar['image_policy_is_enabled'],
                    'time_created': ar['time_created'],
                    'time_updated': ar['time_updated'],
                    'functions': self.__csv_list_to_str(ar['functions'], 'display_name'),
                    'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                    'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                    'id': ar['id']
                }

                self.csv_functions_apps.append(data)
                self.__csv_add_service(data, "Functions Apps")

                for fn in ar['functions']:
                    data = {
                        'region_name': region_name,
                        'compartment_name': fn['compartment_name'],
                        'compartment_path': fn['compartment_path'],
                        'app_name': ar['display_name'],
                        'name': fn['display_name'],
                        'lifecycle_state': fn['lifecycle_state'],
                        'subnets': self.__csv_list_to_str(ar['subnets']),
                        'network_security_group_names': ar['network_security_group_names'],
                        'network_security_group_ids': self.__csv_list_to_str(ar['network_security_group_ids']),
                        'shape': fn['shape'],
                        'image': fn['image'],
                        'image_digest': fn['image_digest'],
                        'memory_in_mbs': fn['memory_in_mbs'],
                        'timeout_in_seconds': fn['timeout_in_seconds'],
                        'invoke_endpoint': fn['invoke_endpoint'],
                        'time_created': fn['time_created'],
                        'time_updated': fn['time_updated'],
                        'source_type': fn['source_type'],
                        'provisioned_strategy': fn['provisioned_strategy'],
                        'trace_config_is_enabled': fn['trace_config_is_enabled'],
                        'freeform_tags': self.__get_freeform_tags(fn['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(fn['defined_tags']),
                        'app_id': ar['id'],
                        'id': fn['id']
                    }

                    self.csv_functions_fns.append(data)
                    self.__csv_add_service(data, "Functions Fns")

        except Exception as e:
            self.__print_error("__csv_functions", e)

    ##########################################################################
    # Paas OAC
    ##########################################################################
    def __csv_paas_oac(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'feature_set': ar['feature_set'],
                        'license_type': ar['license_type'],
                        'capacity_type': ar['capacity_type'],
                        'capacity_value': ar['capacity_value'],
                        'email_notification': ar['email_notification'],
                        'service_url': ar['service_url'],
                        'vanity_domain': ar['vanity_domain'],
                        'vanity_url': ar['vanity_url'],
                        'network_endpoint_details': ar['network_endpoint_details'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'info': ar['capacity_type'] + ":" + str(ar['capacity_value']),
                        'id': ar['id']
                    }

                    self.csv_paas_oac.append(data)
                    self.__csv_add_service(data, "OAC")

        except Exception as e:
            self.__print_error("__csv_paas_oac", e)

    ##########################################################################
    # Paas OCE
    ##########################################################################
    def __csv_paas_oce(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'description': ar['description'],
                        'guid': ar['guid'],
                        'tenancy_name': ar['tenancy_name'],
                        'idcs_tenancy': ar['idcs_tenancy'],
                        'object_storage_namespace': ar['object_storage_namespace'],
                        'admin_email': ar['admin_email'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'service': ar['service'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_paas_oce.append(data)
                    self.__csv_add_service(data, "OCE")

        except Exception as e:
            self.__print_error("__csv_paas_oce", e)

    ##########################################################################
    # Paas VB
    ##########################################################################
    def __csv_paas_visualbuilder(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'state_message': ar['state_message'],
                        'instance_url': ar['instance_url'],
                        'node_count': ar['node_count'],
                        'is_visual_builder_enabled': ar['is_visual_builder_enabled'],
                        'custom_endpoint': ar['custom_endpoint'],
                        'alternate_custom_endpoints': ar['alternate_custom_endpoints'],
                        'consumption_model': ar['consumption_model'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_paas_vb.append(data)
                    self.__csv_add_service(data, "Visual Builder")

        except Exception as e:
            self.__print_error("__csv_paas_visualbuilder", e)

    ##########################################################################
    # __csv_paas_open_search
    ##########################################################################
    def __csv_paas_open_search(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'software_version': ar['software_version'],
                        'total_storage_gb': ar['total_storage_gb'],
                        'security_mode': ar['security_mode'],
                        'availability_domains': ar['availability_domains'],
                        'opensearch_fqdn': ar['opensearch_fqdn'],
                        'opensearch_private_ip': ar['opensearch_private_ip'],
                        'opendashboard_fqdn': ar['opendashboard_fqdn'],
                        'opendashboard_private_ip': ar['opendashboard_private_ip'],
                        'master_node_count': ar['master_node_count'],
                        'master_node_host_type': ar['master_node_host_type'],
                        'master_node_host_bare_metal_shape': ar['master_node_host_bare_metal_shape'],
                        'master_node_host_ocpu_count': ar['master_node_host_ocpu_count'],
                        'master_node_host_memory_gb': ar['master_node_host_memory_gb'],
                        'data_node_count': ar['data_node_count'],
                        'data_node_host_type': ar['data_node_host_type'],
                        'data_node_host_bare_metal_shape': ar['data_node_host_bare_metal_shape'],
                        'data_node_host_ocpu_count': ar['data_node_host_ocpu_count'],
                        'data_node_host_memory_gb': ar['data_node_host_memory_gb'],
                        'data_node_storage_gb': ar['data_node_storage_gb'],
                        'opendashboard_node_count': ar['opendashboard_node_count'],
                        'opendashboard_node_host_ocpu_count': ar['opendashboard_node_host_ocpu_count'],
                        'opendashboard_node_host_memory_gb': ar['opendashboard_node_host_memory_gb'],
                        'vcn_id': ar['vcn_id'],
                        'vcn_name': ar['vcn_name'],
                        'subnet_id': ar['subnet_id'],
                        'subnet_name': ar['subnet_name'],
                        'vcn_compartment_id': ar['vcn_compartment_id'],
                        'subnet_compartment_id': ar['subnet_compartment_id'],
                        'security_master_user_name': ar['security_master_user_name'],
                        'security_master_user_password_hash': ar['security_master_user_password_hash'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_paas_open_search.append(data)
                    self.__csv_add_service(data, "Search", col_name="display_name")

        except Exception as e:
            self.__print_error("__csv_paas_open_search", e)

    ##########################################################################
    # Paas DevOps
    ##########################################################################
    def __csv_paas_devops(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'namespace': ar['namespace'],
                        'notification_config': ar['notification_config'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_paas_devops.append(data)
                    self.__csv_add_service(data, "DevOPS")

        except Exception as e:
            self.__print_error("__csv_paas_devops", e)

    ##########################################################################
    # Paas OCVS
    ##########################################################################
    def __csv_paas_ocvs(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'ocpus': ar['sddc_ocpus'],
                        'vmware_software_version': ar['vmware_software_version'],
                        'esxi_software_version': ar['esxi_software_version'],
                        'clusters_count': ar['clusters_count'],
                        'vcenter_fqdn': ar['vcenter_fqdn'],
                        'nsx_manager_fqdn': ar['nsx_manager_fqdn'],
                        'vcenter_private_ip': ar['vcenter_private_ip'],
                        'nsx_manager_private_ip': ar['nsx_manager_private_ip'],
                        'vcenter_username': ar['vcenter_username'],
                        'nsx_manager_username': ar['nsx_manager_username'],
                        'nsx_edge_uplink_ip': ar['nsx_edge_uplink_ip'],
                        'hcx_private_ip': ar['hcx_private_ip'],
                        'hcx_fqdn': ar['hcx_fqdn'],
                        'hcx_mode': ar['hcx_mode'],
                        'is_hcx_pending_downgrade': ar['is_hcx_pending_downgrade'],
                        'time_hcx_billing_cycle_end': ar['time_hcx_billing_cycle_end'],
                        'time_hcx_license_status_updated': ar['time_hcx_license_status_updated'],
                        'is_single_host_sddc': ar['is_single_host_sddc'],
                        'time_created': ar['time_created'],
                        'time_updated': ar['time_updated'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'cluster_query_error': ar['cluster_query_error'],
                        'clusters': self.__csv_list_to_str(ar['clusters'], 'display_name'),
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'info': "ocpus:" + str(ar['sddc_ocpus']),
                        'id': ar['id']
                    }

                    self.csv_paas_ocvs.append(data)
                    self.__csv_add_service(data, "OCVS")

                    for cl in ar['clusters']:
                        nt = cl['network_configuration']
                        cdata = {
                            'region_name': region_name,
                            'compartment_name': ar['compartment_name'],
                            'compartment_path': ar['compartment_path'],
                            'sddc_name': ar['display_name'],
                            'ocpus': cl['cluster_ocpus'],
                            'name': cl['display_name'],
                            'compute_availability_domain': cl['compute_availability_domain'],
                            'instance_display_name_prefix': cl['instance_display_name_prefix'],
                            'vmware_software_version': cl['vmware_software_version'],
                            'esxi_hosts_count': cl['esxi_hosts_count'],
                            'esxi_software_version': cl['esxi_software_version'],
                            'initial_commitment': cl['initial_commitment'],
                            'workload_network_cidr': cl['workload_network_cidr'],
                            'time_created': cl['time_created'],
                            'time_updated': cl['time_updated'],
                            'lifecycle_state': cl['lifecycle_state'],
                            'initial_host_shape_name': cl['initial_host_shape_name'],
                            'initial_host_ocpu_count': cl['initial_host_ocpu_count'],
                            'is_shielded_instance_enabled': cl['is_shielded_instance_enabled'],
                            'capacity_reservation_id': cl['capacity_reservation_id'],
                            'vsphere_type': cl['vsphere_type'],
                            'datastores': str(cl['datastores']) if cl['datastores'] else "None",
                            'provisioning_subnet': nt['provisioning_subnet'],
                            'provisioning_vlan': nt['provisioning_vlan'],
                            'hcx_vlan': nt['hcx_vlan'],
                            'vsphere_vlan': nt['vsphere_vlan'],
                            'vmotion_vlan': nt['vmotion_vlan'],
                            'vsan_vlan': nt['vsan_vlan'],
                            'nsx_v_tep_vlan': nt['nsx_v_tep_vlan'],
                            'nsx_edge_v_tep_vlan': nt['nsx_edge_v_tep_vlan'],
                            'nsx_edge_uplink1_vlan': nt['nsx_edge_uplink1_vlan'],
                            'nsx_edge_uplink2_vlan': nt['nsx_edge_uplink2_vlan'],
                            'exsi_hosts': str(', '.join(x['display_name'] + " - " + x['current_commitment'] + " - " + x['host_shape_name'] + " - " + x['host_ocpu_count'] for x in cl['esxihosts'])),
                            'esxi_query_error': cl['esxi_query_error'],
                            'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                            'sddc_id': ar['id'],
                            'id': cl['id']
                        }
                        self.csv_paas_ocvs_clusters.append(cdata)
                        self.__csv_add_service(data, "OCVS Cluster")

        except Exception as e:
            self.__print_error("__csv_paas_ocvs", e)

    ##########################################################################
    # csv paas
    ##########################################################################
    def __csv_paas_main(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'oic' in data:
                self.__csv_paas_oic(region_name, data['oic'])

            if 'oac' in data:
                self.__csv_paas_oac(region_name, data['oac'])

            if 'oce' in data:
                self.__csv_paas_oce(region_name, data['oce'])

            if 'vb' in data:
                self.__csv_paas_visualbuilder(region_name, data['vb'])

            if 'ocvs' in data:
                self.__csv_paas_ocvs(region_name, data['ocvs'])

            if 'devops' in data:
                self.__csv_paas_devops(region_name, data['devops'])

            if 'open_search' in data:
                self.__csv_paas_open_search(region_name, data['open_search'])

        except Exception as e:
            self.__print_error("__csv_paas_main", e)

    ##########################################################################
    # csv data_ai
    ##########################################################################
    def __csv_data_ai_main(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'oda' in data:
                self.__csv_data_ai_oda(region_name, data['oda'])

            if 'bds' in data:
                self.__csv_data_ai_bds(region_name, data['bds'])

            if 'data_science' in data:
                self.__csv_data_science(region_name, data['data_science'])

            if 'data_flow' in data:
                self.__csv_data_flow(region_name, data['data_flow'])

            if 'data_catalog' in data:
                self.__csv_data_catalog(region_name, data['data_catalog'])

            if 'data_integration' in data:
                self.__csv_data_integration(region_name, data['data_integration'])

            if 'genai' in data:
                self.__csv_genai(region_name, data['genai'])

            if 'genai_agent' in data:
                self.__csv_genai_agent(region_name, data['genai_agent'])

            if 'genai_agent_kb' in data:
                self.__csv_genai_agent_kb(region_name, data['genai_agent_kb'])

        except Exception as e:
            self.__print_error("__csv_data_ai_main", e)

    ##########################################################################
    # Data AI ODA
    ##########################################################################
    def __csv_data_ai_oda(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'description': ar['description'],
                        'shape_name': ar['shape_name'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'is_role_based_access': ar['is_role_based_access'],
                        'identity_domain': ar['identity_domain'],
                        'imported_package_names': ar['imported_package_names'],
                        'attachment_types': ar['attachment_types'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_ai_oda.append(data)
                    self.__csv_add_service(data, "ODA")

        except Exception as e:
            self.__print_error("__csv_data_ai_oda", e)

    ##########################################################################
    # Data AI BDS
    ##########################################################################
    def __csv_data_ai_bds(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'number_of_nodes': ar['number_of_nodes'],
                        'is_high_availability': ar['is_high_availability'],
                        'cluster_version': ar['cluster_version'],
                        'is_secure': ar['is_secure'],
                        'cluster_profile': ar['cluster_profile'],
                        'is_cloud_sql_configured': ar['is_cloud_sql_configured'],
                        'is_kafka_configured': ar['is_kafka_configured'],
                        'number_of_nodes_requiring_maintenance_reboot': ar['number_of_nodes_requiring_maintenance_reboot'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'network_cidr_block': ar['network_cidr_block'],
                        'network_is_nat_gateway_required': ar['network_is_nat_gateway_required'],
                        'cluster_details_bda_version': ar['cluster_details_bda_version'],
                        'cluster_details_bdm_version': ar['cluster_details_bdm_version'],
                        'cluster_details_bds_version': ar['cluster_details_bds_version'],
                        'cluster_details_os_version': ar['cluster_details_os_version'],
                        'cluster_details_db_version': ar['cluster_details_db_version'],
                        'cluster_details_bd_cell_version': ar['cluster_details_bd_cell_version'],
                        'cluster_details_csql_cell_version': ar['cluster_details_csql_cell_version'],
                        'cluster_details_time_refreshed': ar['cluster_details_time_refreshed'],
                        'cluster_details_c_manager_url': ar['cluster_details_c_manager_url'],
                        'cluster_details_ambari_url': ar['cluster_details_ambari_url'],
                        'cluster_details_big_data_manager_url': ar['cluster_details_big_data_manager_url'],
                        'cluster_details_hue_server_url': ar['cluster_details_hue_server_url'],
                        'cluster_details_odh_version': ar['cluster_details_odh_version'],
                        'cluster_details_jupyter_hub_url': ar['cluster_details_jupyter_hub_url'],
                        'cloud_sql_details_shape': ar['cloud_sql_details_shape'],
                        'cloud_sql_details_block_volume_size_in_gbs': ar['cloud_sql_details_block_volume_size_in_gbs'],
                        'cloud_sql_details_is_kerberos_mapped_to_database_users': ar['cloud_sql_details_is_kerberos_mapped_to_database_users'],
                        'cloud_sql_details_ip_address': ar['cloud_sql_details_ip_address'],
                        'created_by': ar['created_by'],
                        'kms_key_id': ar['kms_key_id'],
                        'nodes_ids': str(':'.join(x['instance_id'] for x in ar['nodes'])),
                        'nodes_hostname': str(':'.join(x['hostname'] for x in ar['nodes'])),
                        'nodes_ip_address': str(':'.join(x['ip_address'] for x in ar['nodes'])),
                        'nodes_shapes': str(':'.join(x['shape'] + "." + x['ocpus'] + "." + x['memory_in_gbs'] for x in ar['nodes'])),
                        'id': ar['id']
                    }

                    self.csv_data_ai_bds.append(data)
                    self.__csv_add_service(data, "BDS")

        except Exception as e:
            self.__print_error("__csv_data_ai_bds", e)

    ##########################################################################
    # Data Flow
    ##########################################################################
    def __csv_data_flow(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'language': ar['language'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'owner_principal_id': ar['owner_principal_id'],
                        'owner_user_name': ar['owner_user_name'],
                        'spark_version': ar['spark_version'],
                        'type': ar['type'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_flow.append(data)
                    self.__csv_add_service(data, "Data Flow")

        except Exception as e:
            self.__print_error("__csv_data_flow", e)

    ##########################################################################
    # Data Catalog
    ##########################################################################
    def __csv_data_catalog(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'time_created': ar['time_created'][0:16],
                        'number_of_objects': ar['number_of_objects'],
                        'attached_catalog_private_endpoints': ar['attached_catalog_private_endpoints'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_catalog.append(data)
                    self.__csv_add_service(data, "Data Catalog")

        except Exception as e:
            self.__print_error("__csv_data_catalog", e)

    ##########################################################################
    # Data Integration
    ##########################################################################
    def __csv_data_integration(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_integration.append(data)
                    self.__csv_add_service(data, "Data Integration")

        except Exception as e:
            self.__print_error("__csv_data_integration", e)

    ##########################################################################
    # __csv_genai
    ##########################################################################
    def __csv_genai(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'],
                        'type': ar['type'],
                        'unit_count': ar['unit_count'],
                        'unit_shape': ar['unit_shape'],
                        'capacity_type': ar['capacity_type'],
                        'capacity_total_endpoint_capacity': ar['capacity_total_endpoint_capacity'],
                        'capacity_used_endpoint_capacity': ar['capacity_used_endpoint_capacity'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_genai.append(data)
                    self.__csv_add_service(data, "GenAI")

        except Exception as e:
            self.__print_error("__csv_genai", e)

    ##########################################################################
    # __csv_genai_agent
    ##########################################################################
    def __csv_genai_agent(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'description': ar['description'],
                        'welcome_message': ar['welcome_message'],
                        'llm_config': ar['llm_config'],
                        'knowledge_base_ids': str(ar['knowledge_base_ids']),
                        'time_created': ar['time_created'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_genai_agent.append(data)
                    self.__csv_add_service(data, "GenAI Agent")

        except Exception as e:
            self.__print_error("__csv_genai_agent", e)

    ##########################################################################
    # __csv_genai_agent_kb
    ##########################################################################
    def __csv_genai_agent_kb(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_genai_agent_kb.append(data)
                    self.__csv_add_service(data, "GenAI Agent KB")

        except Exception as e:
            self.__print_error("__csv_genai_agent_kb", e)

    ##########################################################################
    # Data Science
    ##########################################################################
    def __csv_data_science(self, region_name, services):
        try:

            if len(services) == 0:
                return

            if services:
                for ar in services:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'description': ar['description'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_science.append(data)
                    self.__csv_add_service(data, "Data Science")

        except Exception as e:
            self.__print_error("__csv_data_science", e)

    ##########################################################################
    # csv monitoring
    ##########################################################################
    def __csv_monitoring(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'events' in data:
                self.__csv_monitor_events(region_name, data['events'])

            if 'agents' in data:
                self.__csv_monitor_agents(region_name, data['agents'])

            if 'db_managements' in data:
                self.__csv_monitor_db_managements(region_name, data['db_managements'])

            if 'alarms' in data:
                self.__csv_monitor_alarms(region_name, data['alarms'])

            if 'advisor_recommendations' in data:
                self.__csv_monitor_advisor_recommendations(data['advisor_recommendations'])

            if 'advisor_resource_actions' in data:
                self.__csv_monitor_advisor_resource_actions(data['advisor_resource_actions'])

        except Exception as e:
            self.__print_error("__csv_monitoring", e)

    ##########################################################################
    # Monitor Agents
    ##########################################################################
    def __csv_monitor_agents(self, region_name, agents):
        try:

            if len(agents) == 0:
                return

            if agents:
                for ar in agents:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'time_created': ar['time_created'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'platform_type': ar['platform_type'],
                        'platform_name': ar['platform_name'],
                        'platform_version': ar['platform_version'],
                        'version': ar['version'],
                        'is_agent_auto_upgradable': ar['is_agent_auto_upgradable'],
                        'host': ar['host'],
                        'plugin_list': ar['plugin_list'],
                        'time_last_heartbeat': ar['time_last_heartbeat'],
                        'availability_status': ar['availability_status'],
                        'install_key_id': ar['install_key_id'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_monitor_agents.append(data)

        except Exception as e:
            self.__print_error("__csv_monitor_agents", e)

    ##########################################################################
    # Advisor Recommendations
    ##########################################################################
    def __csv_monitor_advisor_recommendations(self, advisors):
        try:

            if len(advisors) == 0:
                return

            if advisors:
                for ar in advisors:

                    data = {
                        'category_id': ar['category_id'],
                        'name': ar['name'],
                        'description': ar['description'],
                        'importance': ar['importance'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'estimated_cost_saving': ar['estimated_cost_saving'],
                        'nodes_shapes': str(':'.join(x['status'] + "=" + x['count'] for x in ar['resource_counts'])),
                        'status': ar['status'],
                        'time_status_begin': ar['time_status_begin'],
                        'time_status_end': ar['time_status_end'],
                        'time_created': ar['time_created'],
                        'time_updated': ar['time_updated'],
                        'compartment_id': ar['compartment_id'],
                        'extended_metadata': str(ar['extended_metadata']),
                        'id': ar['id']
                    }

                    self.csv_advisor_recommendations.append(data)

        except Exception as e:
            self.__print_error("__csv_monitor_advisor_recommendations", e)

    ##########################################################################
    # Advisor Resource Actions
    ##########################################################################
    def __csv_monitor_advisor_resource_actions(self, advisors):
        try:

            if len(advisors) == 0:
                return

            if advisors:
                for ar in advisors:

                    data = {
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'category_id': ar['category_id'],
                        'recommendation_id': ar['recommendation_id'],
                        'recommendation_name': ar['recommendation_name'],
                        'resource_id': ar['resource_id'],
                        'name': ar['name'],
                        'resource_type': ar['resource_type'],
                        'action_type': ar['action_type'],
                        'action_description': ar['action_description'],
                        'action_url': ar['action_url'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'estimated_cost_saving': ar['estimated_cost_saving'],
                        'status': ar['status'],
                        'time_status_begin': ar['time_status_begin'],
                        'time_status_end': ar['time_status_end'],
                        'time_created': ar['time_created'],
                        'time_updated': ar['time_updated'],
                        'metadata': str(ar['metadata']),
                        'extended_metadata': str(ar['extended_metadata']),
                        'compartment_id': ar['compartment_id'],
                        'id': ar['id']
                    }

                    self.csv_advisor_resource_actions.append(data)

        except Exception as e:
            self.__print_error("__csv_monitor_advisor_resource_actions", e)

    ##########################################################################
    # Monitor Events
    ##########################################################################
    def __csv_monitor_events(self, region_name, events):
        try:

            if len(events) == 0:
                return

            if events:
                for ar in events:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'description': ar['description'],
                        'condition': ar['condition'],
                        'is_enabled': ar['is_enabled'],
                        'actions': str(ar['actions']),
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_monitor_events.append(data)

        except Exception as e:
            self.__print_error("__csv_monitor_events", e)

    ##########################################################################
    # Monitor db_managements
    ##########################################################################
    def __csv_monitor_db_managements(self, region_name, db_managements):
        try:

            if len(db_managements) == 0:
                return

            if db_managements:
                for ar in db_managements:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'name': ar['name'],
                        'time_created': ar['time_created'][0:16],
                        'database_type': ar['database_type'],
                        'database_sub_type': ar['database_sub_type'],
                        'is_cluster': ar['is_cluster'],
                        'deployment_type': ar['deployment_type'],
                        'management_option': ar['management_option'],
                        'workload_type': ar['workload_type'],
                        'db_system_id': ar['db_system_id'],
                        'parent_container_id': ar['parent_container_id'],
                        'storage_system_id': ar['storage_system_id'],
                        'id': ar['id']
                    }

                    self.csv_monitor_db_management.append(data)
                    self.__csv_add_service(data, "DB Management")

        except Exception as e:
            self.__print_error("__csv_monitor_db_managements", e)

    ##########################################################################
    # Monitor Alarms
    ##########################################################################
    def __csv_monitor_alarms(self, region_name, alarms):
        try:

            if len(alarms) == 0:
                return

            if alarms:
                for ar in alarms:

                    data = {
                        'region_name': region_name,
                        'compartment_name': ar['compartment_name'],
                        'compartment_path': ar['compartment_path'],
                        'display_name': ar['display_name'],
                        'namespace': ar['namespace'],
                        'query': ar['query'],
                        'severity': ar['severity'],
                        'destinations': self.__csv_list_to_str(ar['destinations']),
                        'destinations_names': self.__csv_list_to_str(ar['destinations_names']),
                        'is_enabled': ar['is_enabled'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'metric_compartment_id': ar['metric_compartment_id'],
                        'id': ar['id']
                    }

                    self.csv_monitor_alarms.append(data)
                    self.__csv_add_service(data, "Monitor Alarm", col_name='display_name')

        except Exception as e:
            self.__print_error("__csv_monitor_alarms", e)

    ##########################################################################
    # Monitor Notifications
    ##########################################################################
    def __csv_notifications(self, region_name, notifications):
        try:

            if len(notifications) == 0:
                return

            if notifications:
                for ar in notifications:
                    for sr in ar['subscriptions']:

                        data = {
                            'region_name': region_name,
                            'topic_compartment_name': ar['compartment_name'],
                            'topic_compartment_path': ar['compartment_path'],
                            'topic_name': ar['name'],
                            'topic_description': ar['description'],
                            'topic_time_created': ar['time_created'][0:16],
                            'topic_etag': ar['etag'],
                            'topic_api_endpoint': ar['api_endpoint'],
                            'topic_freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                            'topic_defined_tags': self.__get_defined_tags(ar['defined_tags']),
                            'topic_id': ar['topic_id'],
                            'protocol': sr['protocol'],
                            'endpoint': sr['endpoint'],
                            'compartment_name': sr['compartment_name'],
                            'compartment_path': sr['compartment_path'],
                            'etag': sr['etag'],
                            'created_time': sr['created_time'],
                            'freeform_tags': self.__get_freeform_tags(sr['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(sr['defined_tags']),
                            'id': sr['id']
                        }

                        self.csv_notifications.append(data)
                        self.__csv_add_service(data, "Notification", col_name="topic_name")

        except Exception as e:
            self.__print_error("__csv_notifications", e)

    ##########################################################################
    # Print Identity data
    ##########################################################################
    def __csv_region_data(self, region_name, data):

        try:
            if not data:
                return

            for cdata in data:
                if 'network' in cdata:
                    self.__csv_core_network_main(region_name, cdata['network'])
                if 'compute' in cdata:
                    self.__csv_core_compute_main(region_name, cdata['compute'])
                if 'database' in cdata:
                    self.__csv_database_main(region_name, cdata['database'])
                if 'load_balancer' in cdata:
                    self.__csv_load_balancer_main(region_name, cdata['load_balancer'])
                if 'network_load_balancer' in cdata:
                    self.__csv_network_load_balancer_main(region_name, cdata['network_load_balancer'])
                if 'file_storage' in cdata:
                    self.__csv_file_storage_main(region_name, cdata['file_storage'])
                if 'apigateways' in cdata:
                    self.__csv_apigw(region_name, cdata['apigateways'])
                if 'object_storage' in cdata:
                    self.__csv_object_storage_main(region_name, cdata['object_storage'])
                if 'security' in cdata:
                    self.__csv_security_main(region_name, cdata['security'])
                if 'containers' in cdata:
                    self.__csv_container(region_name, cdata['containers'])
                if 'edge_services' in cdata:
                    self.__csv_edge_main(region_name, cdata['edge_services'])
                if 'paas_services' in cdata:
                    self.__csv_paas_main(region_name, cdata['paas_services'])
                if 'streams_queues' in cdata:
                    self.__csv_streams_queues(region_name, cdata['streams_queues'])
                if 'data_ai' in cdata:
                    self.__csv_data_ai_main(region_name, cdata['data_ai'])
                if 'monitoring' in cdata:
                    self.__csv_monitoring(region_name, cdata['monitoring'])
                if 'notifications' in cdata:
                    self.__csv_notifications(region_name, cdata['notifications'])
                if 'quotas' in cdata:
                    self.__csv_quotas_main(region_name, cdata['quotas'])
                if 'announcement_detailed' in cdata:
                    self.__csv_announcements_detailed(region_name, cdata['announcement_detailed'])
                if 'functions' in cdata:
                    self.__csv_functions(region_name, cdata['functions'])
                if 'fsdr' in cdata:
                    self.__csv_fsdr(region_name, cdata['fsdr'])

        except Exception as e:
            self.__print_error("__csv_region_data", e)
            raise
