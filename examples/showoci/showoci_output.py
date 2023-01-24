##########################################################################
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# showoci_output.py
#
# @author: Adi Zohar
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


class ShowOCIOutput(object):

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
            print("Disclaimer      : " + data['disclaimer'])
            print("Machine         : " + data['machine'])
            print("Python Version  : " + data['python'])
            if data['use_instance_principals']:
                print("Authentication  : Instance Principals")
            elif data['use_delegation_token']:
                print("Authentication  : Instance Principals With Delegation Token")
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
            print("Comand Line     : " + data['cmdline'])
            print("Showoci Version : " + data['version'])
            print("OCI SDK Version : " + data['oci_sdk_version'])
            if 'proxy' in data:
                print("Proxy           : " + data['proxy'])
            if 'override_tenant_id' in data:
                if data['override_tenant_id']:
                    print("Override id     : " + data['override_tenant_id'])
            if 'joutfile' in data:
                print("JSON Out        : " + data['joutfile'])

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

        if isinstance(e, KeyError):
            print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + msg + ": " + str(e))

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
                    retired = "" if tag['is_retired'] == "False" else " Retired "
                    print(self.taba + tag['name'] + retired + " (" + tag['lifecycle_state'] + "), " + tag['description'])

        except Exception as e:
            self.__print_error("__print_identity_tag_namespace", e)

    ##########################################################################
    # Print Identity Providers
    ##########################################################################
    def __print_identity_providers(self, identity_providers):

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
                for ig in ip['group_map']:
                    print(self.tabs + "Group Map : " + ig)
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
            if 'providers' in data:
                self.__print_identity_providers(data['providers'])
            if 'cost_tracking_tags' in data:
                self.__print_identity_cost_tracking_tags(data['cost_tracking_tags'])
            if 'tag_namespace' in data:
                self.__print_identity_tag_namespace(data['tag_namespace'])

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
                print(self.tabs + "VLAN " + vlan['vlan'] + self.__print_core_network_vcn_compartment(vcn_compartment,
                                                                                                     vlan[
                                                                                                         'compartment_name']))
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

    ########################################################################
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

                for index, arr in enumerate(drg['virtual_circuits'], start=1):
                    drg_route_table = ", DRG Route: " + arr['drg_route_table'] if arr['drg_route_table'] else ""
                    print(self.tabs + "      VC " + str(index) + "      : " + arr['name'] + " (" + arr['bgp_session_state'] + ")" + drg_route_table)

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
    # print virtual cirtuicts
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
    # print network Main
    ##########################################################################

    def __print_core_network_main(self, data):
        try:
            if 'vcn' in data:
                self.__print_core_network_vcn(data['vcn'])
            if 'drg' in data:
                self.__print_core_network_drg(data['drg'])
            if 'cpe' in data:
                self.__print_core_network_cpe(data['cpe'])
            if 'ipsec' in data:
                self.__print_core_network_ipsec(data['ipsec'])
            if 'remote_peering' in data:
                self.__print_core_network_remote_peering(data['remote_peering'])
            if 'virtual_circuit' in data:
                self.__print_core_network_virtual_circuit(data['virtual_circuit'])

        except Exception as e:
            self.__print_error("__print_core_network", e)

    ##########################################################################
    # print load balancer backedset
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
                        print(self.tabs + "           : Rules: " + str(', '.join(x for x in listener['rule_set_names'])))
                    if listener['hostname_names']:
                        print(self.tabs + "           : Hosts: " + str(', '.join(x for x in listener['hostname_names'])))
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
                    print(self.tabs + "RuleSet    : " + rs['name'] + ": " + str(', '.join(x['action'] for x in rs['items'])))

        except Exception as e:
            self.__print_error("__print_load_balancer_details", e)

    ##########################################################################
    # print network_load balancer config
    ##########################################################################

    def __print_load_balancer_network_details(self, load_balance_obj):
        try:
            lb = load_balance_obj
            print(self.taba + "Name       : " + lb['name'])
            print(self.tabs + "Status     : " + lb['status'])
            print(self.tabs + "Subnet     : " + lb['subnet_name'])

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
    # Load Balancer
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
    # Network Load Balancer
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

                # clusters
                for vm in dbs['vm_clusters']:
                    print("")

                    if 'display_name' in vm:
                        print(self.tabs + "VMCLSTR   : " + str(vm['display_name']) + " (" + vm['lifecycle_state'] + ")")

                    if 'cluster_name' in vm:
                        if vm['cluster_name']:
                            print(self.tabs + "Cluster   : " + vm['cluster_name'])

                    if 'cpu_core_count' in vm:
                        print(self.tabs + "Cores     : " + str(vm['cpu_core_count']))

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
                            print(self.tabs + "Grid Ver  : " + vm['gi_version'] + "  " + vm['gi_version_date'])

                    if 'system_version' in vm:
                        if vm['system_version']:
                            print(self.tabs + "Sys Ver   : " + vm['system_version'] + "  " + vm['system_version_date'])

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
                                print(self.tabs + self.tabs + "     Maintenance: " + db_node['maintenance_type'] + "  " + db_node['time_maintenance_window_start'][0:16] + " - " + db_node['time_maintenance_window_end'][0:16])

                    # db homes
                    for db_home in vm['db_homes']:
                        print(self.tabs + "Home      : " + db_home['home'])

                        # patches
                        for p in db_home['patches']:
                            print(self.tabs + self.tabs + "   PT : " + p)

                        # databases
                        for db in db_home['databases']:
                            pdbs = ", PDBS: " + str(', '.join(x['name'] for x in db['pdbs'])) if db['pdbs'] else ""
                            print(self.tabs + self.tabs + "   DB : " + db['name'] + pdbs)

                            # print data guard
                            for dg in db['dataguard']:
                                print(self.tabs + self.tabs + "        " + dg['name'])

                            # print backups
                            for backup in db['backups']:
                                print(self.tabs + self.tabs + "      " + backup['name'] + " - " + backup['time'] + " - " + backup['size'])

                        print(self.tabs + "          : " + '-' * 90)

        except Exception as e:
            self.__print_error("__print_database_db_exadata_infra", e)

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
                                print(self.tabs + self.tabs + "     Maintenance: " + db_node['maintenance_type'] + "  " + db_node['time_maintenance_window_start'][0:16] + " - " + db_node['time_maintenance_window_end'][0:16])

                    # db homes
                    for db_home in vm['db_homes']:
                        print(self.tabs + "Home           : " + db_home['home'])

                        # patches
                        for p in db_home['patches']:
                            print(self.tabs + self.tabs + "        PT : " + p)

                        # databases
                        for db in db_home['databases']:
                            pdbs = ", PDBS: " + str(', '.join(x['name'] for x in db['pdbs'])) if db['pdbs'] else ""
                            print(self.tabs + self.tabs + "        DB : " + db['name'] + pdbs)

                            # print data guard
                            for dg in db['dataguard']:
                                print(self.tabs + self.tabs + "             " + dg['name'])

                            # print backups
                            for backup in db['backups']:
                                print(self.tabs + self.tabs + "             " + backup['name'] + " - " + backup['time'] + " - " + backup['size'])

                        print(self.tabs + "               : " + '-' * 90)

        except Exception as e:
            self.__print_error("__print_database_db_exacc_infra", e)

    ##########################################################################
    # print database db system
    ##########################################################################

    def __print_database_db_system_details(self, dbs):
        try:
            print(self.taba + "DBaaS   : " + dbs['name'] + " - " + dbs['version'] + " " + dbs['version_date'])
            print(self.tabs + "Created : " + dbs['time_created'][0:16])
            print(self.tabs + "AD      : " + dbs['availability_domain'])

            if 'cpu_core_count' in dbs:
                print(self.tabs + "Cores   : " + str(dbs['cpu_core_count']))

            if 'node_count' in dbs:
                if dbs['node_count']:
                    print(self.tabs + "Nodes   : " + str(dbs['node_count']))

            if 'host' in dbs:
                print(self.tabs + "Host    : " + dbs['host'])

            if 'domain' in dbs:
                if dbs['domain']:
                    print(self.tabs + "Domain  : " + dbs['domain'])

            if 'cluster_name' in dbs:
                if dbs['cluster_name']:
                    print(self.tabs + "Cluster : " + dbs['cluster_name'])

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
                    print(self.tabs + db_node['desc'])
                    if 'nsg_names' in db_node:
                        if db_node['nsg_names']:
                            print(self.tabs + "        : SecGrp : " + db_node['nsg_names'])

                    if 'time_maintenance_window_start' in db_node:
                        if db_node['maintenance_type'] != "None":
                            print(self.tabs + self.tabs + "     Maintenance: " + db_node['maintenance_type'] + "  " + db_node['time_maintenance_window_start'][0:16] + " - " + db_node['time_maintenance_window_end'][0:16])

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
                        pdbs = ", PDBS: " + str(', '.join(x['name'] for x in db['pdbs'])) if db['pdbs'] else ""
                        print(self.tabs + self.tabs + " DB : " + db['name'] + pdbs)

                        # print data guard
                        for dg in db['dataguard']:
                            print(self.tabs + self.tabs + "      " + dg['name'])

                        # print backups
                        for backup in db['backups']:
                            print(self.tabs + self.tabs + "      " + backup['name'] + " - " + backup['time'] + " - " + backup['size'])

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
                    print(self.tabs + "Size       : " + str(db['cpu_core_count']) + " OCPUs, " + str(db['data_storage_size_in_tbs']) + "TB Storage")
                if 'time_created' in db:
                    print(self.tabs + "Created    : " + db['time_created'])
                if 'whitelisted_ips' in db:
                    if db['whitelisted_ips']:
                        print(self.tabs + "Allowed IPs: " + db['whitelisted_ips'])
                if 'private_endpoint' in db:
                    if db['private_endpoint'] != 'None':
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
    # ADB-D
    ##########################################################################
    def __print_database_db_autonomous_dedicated(self, list_exadata):

        try:
            for dbs in list_exadata:
                print("")

                print(self.taba + "ADB-D    : " + dbs['name'])
                print(self.tabs + "Created  : " + dbs['time_created'][0:16])
                print(self.tabs + "AD       : " + dbs['availability_domain'])
                print(self.tabs + "Hostname : " + dbs['hostname'])
                print(self.tabs + "Domain   : " + dbs['domain'])
                print(self.tabs + "ScanDNS  : " + dbs['scan_dns_name'])

                if 'subnet_name' in dbs:
                    if dbs['subnet_name'] != "None" and dbs['subnet_name']:
                        print(self.tabs + "Subnet   : " + str(dbs['subnet_name']))

                if 'maintenance_window' in dbs:
                    if dbs['maintenance_window']:
                        print(self.tabs + "Maint    : Window : " + dbs['maintenance_window']['display'])

                if 'last_maintenance_run' in dbs:
                    if dbs['last_maintenance_run']:
                        print(self.tabs + "Maint    : Last   : " + dbs['last_maintenance_run']['description'])
                        print(self.tabs + "                 : " + dbs['last_maintenance_run']['maintenance_display'])

                if 'next_maintenance_run' in dbs:
                    if dbs['next_maintenance_run']:
                        print(self.tabs + "Maint    : Next   : " + dbs['next_maintenance_run']['description'])
                        print(self.tabs + "                 : " + dbs['next_maintenance_run']['maintenance_display'])
                        if dbs['next_maintenance_run']['maintenance_alert']:
                            print(self.tabs + "           Alert  : " + dbs['next_maintenance_run']['maintenance_alert'])

                print("")

                # containers
                for vm in dbs['containers']:

                    print(self.tabs + "Container: " + vm['name'])

                    # databases
                    for db in vm['databases']:
                        print(self.tabs + self.taba + "ADB-S      : " + db['name'])
                        if 'cpu_core_count' in db:
                            print(self.tabs + self.tabs + "Size       : " + str(db['cpu_core_count']) + " OCPUs, " + str(db['data_storage_size_in_tbs']) + "TB Storage")
                        if 'time_created' in db:
                            print(self.tabs + self.tabs + "Created    : " + db['time_created'])
                        if 'data_safe_status' in db:
                            print(self.tabs + self.tabs + "DataSafe   : " + db['data_safe_status'])
                        if 'time_maintenance_begin' in db:
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
                print("")

        except Exception as e:
            self.__print_error("__print_database_mysql", e)

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

            if 'exadata_infrustructure' in list_databases:
                self.print_header("Exadata Infrastructure", 2)
                self.__print_database_db_exadata_infra(list_databases['exadata_infrustructure'])
                print("")

            if 'exacc_infrustructure' in list_databases:
                self.print_header("ExaCC Infrastructure", 2)
                self.__print_database_db_exacc_infra(list_databases['exacc_infrustructure'])
                print("")

            if 'db_system' in list_databases:
                self.print_header("databases DB Systems", 2)
                self.__print_database_db_system(list_databases['db_system'])
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
    # Streams
    ##########################################################################
    def __print_streams_main(self, streams):

        try:
            if not streams:
                return

            self.print_header("Streams", 2)

            for ct in streams:
                print(self.taba + ct['name'] + ", partitions (" + ct['partitions'] + "), Created: " + ct['time_created'][0:16])
                print(self.tabs + "URL   : " + str(ct['messages_endpoint']))

                print("")

        except Exception as e:
            self.__print_error("__print_streams_main", e)

    ##########################################################################
    # Functions
    ##########################################################################
    def __print_functions_main(self, functions):

        try:
            if not functions:
                return

            self.print_header("Function Applications", 2)

            for ct in functions:
                print(self.taba + ct['display_name'] + ", Created: " + ct['time_created'][0:16])
                if ct['subnets']:
                    for sub in ct['subnets']:
                        print(self.tabs + self.tabs + "Subnet: " + sub)
                for fun in ct['functions']:
                    print(self.tabs + self.tabs + "FN    : " + fun['display_name'] + " - " + fun['image'])

                print("")

        except Exception as e:
            self.__print_error("__print_streams_main", e)

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
                print(self.taba + ann['summary'][0:100] + " (" + ann['reference_ticket_number'] + ") - " + ann['announcement_type'] + ", Start Time: " + ann['time_one_value'][0:16] + ", Time Created: " + ann['time_created'][0:16] + " (" + ann['lifecycle_state'] + ")")
                if ann['affected_regions']:
                    print(self.tabs + "Regions  : " + ann['affected_regions'])
                if ann['services']:
                    print(self.tabs + "Services : " + ann['services'])
                print("")

        except Exception as e:
            self.__print_error("__print_announcement_main", e)

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
                    print(self.tabs + "Pack : " + val['message_packs'] + ", " + ("BYOL License" if val['is_byol'] else "License Included"))
                    print(self.tabs + "URL  : " + val['instance_url'])
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

            # OCVS
            if 'ocvs' in paas_services:
                self.print_header("OCVS VMWare", 2)
                for val in paas_services['ocvs']:
                    print(self.taba + val['display_name'] + ", (" + val['compute_availability_domain'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                    print(self.tabs + "Version  : " + val['vmware_software_version'] + ", esxi hosts: " + val['esxi_hosts_count'])
                    print(self.tabs + "HCX      : " + val['is_hcx_enabled'] + ", URL: " + val['hcx_fqdn'] + ", OnPremKey: " + val['hcx_on_prem_key'] + ", initial: " + val['hcx_initial_password'])
                    print(self.tabs + "VCENTER  : " + val['vcenter_fqdn'] + " - " + val['vcenter_private_ip'] + ", User: " + val['vcenter_username'] + ", initial: " + val['vcenter_initial_password'])
                    print(self.tabs + "NSX      : " + val['nsx_manager_fqdn'] + " - " + val['nsx_manager_private_ip'] + ", User: " + val['nsx_manager_username'] + ", initial: " + val['nsx_manager_initial_password'])
                    print(self.tabs + "NSX GW   : " + val['nsx_edge_uplink_ip'])
                    print(self.tabs + "Subnet   : " + val['provisioning_subnet'])
                    print(self.tabs + "Vlans    : " + val['vsphere_vlan'])
                    print(self.tabs + "         : " + val['vmotion_vlan'])
                    print(self.tabs + "         : " + val['vsan_vlan'])
                    print(self.tabs + "         : " + val['nsx_v_tep_vlan'])
                    print(self.tabs + "         : " + val['nsx_edge_v_tep_vlan'])
                    print(self.tabs + "         : " + val['nsx_edge_uplink1_vlan'])
                    print(self.tabs + "         : " + val['nsx_edge_uplink2_vlan'])
                    num = 0
                    for esx in val['esxihosts']:
                        num += 1
                        print(self.tabs + "ESXi " + str(num) + "   : " + esx['display_name'] + ", Created: " + esx['time_created'][0:16] + " (" + esx['lifecycle_state'] + "),  Billing End Date: " + esx['billing_contract_end_date'][0:16] + ", Curr SKU: " + esx['current_sku'] + ", Next SKU: " + esx['next_sku'])

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
                    print(self.taba + val['display_name'] + ", (Target = " + val['target_resource_type'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + "), Total Recipes : " + val['recipe_count'])
                    print("")

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
                        print(self.tabs2 + "Replicas      : " + val['status'] + ", " + val['region'] + ", " + val['crypto_endpoint'])
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

        except Exception as e:
            self.__print_error("__print_security_main", e)

    ##########################################################################
    # Data AI
    ##########################################################################
    def __print_data_ai(self, data_ai):

        try:
            if not data_ai:
                return

            # Data Conn Registry
            if 'data_connectivity_registry' in data_ai:
                self.print_header("Data Conn. Registry", 2)
                for val in data_ai['data_connectivity_registry']:
                    print(self.taba + val['display_name'] + ", (" + val['description'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'] + ")")
                print("")

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
                    print(self.taba + val['display_name'] + ", (" + val['cluster_version'] + "), Created: " + val['time_created'][0:16] + " (" + val['lifecycle_state'])
                    print(self.tabs + "Nodes: " + val['number_of_nodes'] + ", is_high_availability: " + val['is_high_availability'] + ", is_secure: " + val['is_secure'] + ", is_cloud_sql_configured: " + val['is_cloud_sql_configured'])
                print("")

            # DI
            if 'data_integration' in data_ai:
                self.print_header("Data Integration", 2)
                for val in data_ai['data_integration']:
                    description = (" (" + val['description'] + ")") if val['description'] != "None" else ""
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
                    print(self.tabs2 + "Shape: Ocpus: " + str(instance['shape_ocpu']) + ", Memory: " + str(instance['shape_memory_gb']) + "GB, Local Storage: " + str(instance['shape_storage_tb']) + "TB, Processor: " + str(instance['shape_processor_description']))

                if 'availability_domain' in instance and 'fault_domain' in instance:
                    print(self.tabs2 + "AD   : " + instance['availability_domain'] + " - " + instance['fault_domain'])

                if 'time_maintenance_reboot_due' in instance:
                    if instance['time_maintenance_reboot_due'] != "None":
                        print(self.tabs2 + "MRB  : Maintenance Reboot Due " + instance['time_maintenance_reboot_due'])

                if 'image' in instance:
                    print(self.tabs2 + "Img  : " + instance['image'] + " (" + instance['image_os'] + ")")

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
                            print(self.tabs2 + "     : IP Addresses : " + str(', '.join(x['ip_address'] for x in vnic['ip_addresses'])))

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
                if 'streams' in cdata:
                    self.__print_streams_main(cdata['streams'])
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
    # paas services
    ##########################################################################
    def __summary_paas_services_main(self, paas_services):

        try:
            if not paas_services:
                return

            if 'oic' in paas_services:
                self.__summary_core_size(paas_services['oic'])
            if 'oac' in paas_services:
                self.__summary_core_size(paas_services['oac'])
            if 'oce' in paas_services:
                self.__summary_core_size(paas_services['oce'])
            if 'ocvs' in paas_services:
                self.__summary_core_size(paas_services['ocvs'])
            if 'vb' in paas_services:
                self.__summary_core_size(paas_services['vb'])

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
            if 'bastions' in security:
                self.__summary_core_size(security['bastions'])
            if 'kms_vaults' in security:
                self.__summary_core_size(security['kms_vaults'])
                self.__summary_core_size(security['kms_vaults'], "sum_info_hsm", 'key_count')
                self.__summary_core_size(security['kms_vaults'], "sum_info_soft", 'software_key_count')

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
                self.__summary_core_size(data_ai['data_catalog'])
            if 'data_science' in data_ai:
                self.__summary_core_size(data_ai['data_science'])
            if 'data_flow' in data_ai:
                self.__summary_core_size(data_ai['data_flow'])
            if 'oda' in data_ai:
                self.__summary_core_size(data_ai['oda'])
            if 'bds' in data_ai:
                self.__summary_core_size(data_ai['bds'])
            if 'data_integration' in data_ai:
                self.__summary_core_size(data_ai['data_integration'])
            if 'data_connectivity_registry' in data_ai:
                self.__summary_core_size(data_ai['data_connectivity_registry'])

        except Exception as e:
            self.__print_error("__summary_data_ai_main", e)

    ##########################################################################
    # print database autonumous
    ##########################################################################

    def __summary_database_db_autonomous(self, dbs):

        try:
            for db in dbs:
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
            self.__print_error("__summary_database_db_autonomous", e)

    ##########################################################################
    # print database autonumous
    ##########################################################################

    def __summary_database_db_autonomous_dedicated(self, list_exa):

        try:
            for dbs in list_exa:

                # add db to summary
                if dbs['lifecycle_state'] == 'STOPPED':
                    self.summary_global_list.append({'type': 'Stopped ' + dbs['sum_info'], 'size': 1})
                else:
                    self.summary_global_list.append({'type': dbs['sum_info'], 'size': 1})

                # containers
                for ct in dbs['containers']:
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
            self.__print_error("__summary_database_db_autonomous_dedicated", e)

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

            if 'exadata_infrustructure' in list_databases:
                self.__summary_database_db_exadata(list_databases['exadata_infrustructure'])

            if 'exacc_infrustructure' in list_databases:
                self.__summary_database_db_exacc(list_databases['exacc_infrustructure'])

            if 'db_system' in list_databases:
                self.__summary_database_db_system(list_databases['db_system'])

            if 'autonomous' in list_databases:
                self.__summary_database_db_autonomous(list_databases['autonomous'])

            if 'autonomous_dedicated' in list_databases:
                self.__summary_database_db_autonomous_dedicated(list_databases['autonomous_dedicated'])

            if 'nosql' in list_databases:
                self.__summary_database_nosql(list_databases['nosql'])

            if 'mysql' in list_databases:
                self.__summary_database_mysql(list_databases['mysql'])

            if 'goldengate' in list_databases:
                self.__summary_database_goldengate(list_databases['goldengate'])

            if 'db_external_cdb' in list_databases:
                self.__summary_database_external(list_databases['db_external_cdb'])

            if 'db_external_pdb' in list_databases:
                self.__summary_database_external(list_databases['db_external_pdb'])

            if 'db_external_nonpdb' in list_databases:
                self.__summary_database_external(list_databases['db_external_nonpdb'])

        except Exception as e:
            self.__print_error("__summary_database_main", e)

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
                                if dbnode['lifecycle_state'] == 'STOPPED':
                                    self.summary_global_list.append({'type': 'Total Stopped OCPUs - VM/BM Database', 'size': float(dbs['cpu_core_count'])})
                                else:
                                    self.summary_global_list.append({'type': 'Total OCPUs - VM/BM Database', 'size': float(dbs['cpu_core_count'])})

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

                # db homes
                for db_home in dbs['db_homes']:
                    for db in db_home['databases']:
                        self.__summary_core_size(db['backups'])

        except Exception as e:
            self.__print_error("__summary_database_db_system", e)

    ##########################################################################
    # Database Exadata
    ##########################################################################
    def __summary_database_db_exadata(self, list_exa):

        try:
            for dbs in list_exa:

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

        except Exception as e:
            self.__print_error("__summary_database_db_exadata", e)

    ##########################################################################
    # Database ExaCC
    ##########################################################################
    def __summary_database_db_exacc(self, list_exa):

        try:
            for dbs in list_exa:
                if dbs['lifecycle_state'] == 'ACTIVE' or dbs['lifecycle_state'] == 'UPDATING':
                    self.summary_global_list.append({'type': dbs['sum_info'] + " - Count", 'size': 1})

                for vm in dbs['vm_clusters']:
                    if 'cpus_enabled' in vm:
                        self.summary_global_list.append({'type': 'Total OCPUs - ExaCC Database', 'size': float(vm['cpus_enabled'])})
                        self.summary_global_list.append({'type': vm['sum_info'] + " OCPUs", 'size': float(vm['cpus_enabled'])})

                    # db homes
                    for db_home in vm['db_homes']:
                        for db in db_home['databases']:
                            self.__summary_core_size(db['backups'])

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

    def __summary_core_size(self, objects, sum_info="sum_info", sum_size="sum_size_gb"):
        try:
            if len(objects) == 0:
                return

            for obj in objects:
                if sum_info in obj and sum_size in obj:
                    if obj[sum_size] != '':
                        if float(obj[sum_size]) > 0:
                            self.summary_global_list.append({'type': obj[sum_info], 'size': float(obj[sum_size])})

        except Exception as e:
            self.__print_error("__summary_core_size", e)

    ##########################################################################
    # sum core count
    ##########################################################################

    def __summary_core_count(self, objects, object_name):
        try:
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
    csv_file_header = ""
    csv_identity_compartments = []
    csv_identity_groups = []
    csv_identity_users = []
    csv_identity_policies = []
    csv_compute = []
    csv_block_volumes_not_attached = []
    csv_block_volumes = []
    csv_block_volumes_backups = []
    csv_compute_reservations = []
    csv_db_exacc_vmclusters = []
    csv_db_exa_infrastructure = []
    csv_db_exacs_vmclusters = []
    csv_db_vm_bm = []
    csv_db_all = []
    csv_db_autonomous = []
    csv_database = []
    csv_database_backups = []
    csv_network_drg = []
    csv_network_drg_ipsec_tunnels = []
    csv_network_drg_virtual_circuits = []
    csv_network_subnet = []
    csv_network_subnet_prv_ips = []
    csv_network_security_list = []
    csv_network_security_group = []
    csv_network_routes = []
    csv_network_dhcp_options = []
    csv_file_storage = []
    csv_load_balancer = []
    csv_load_balancer_bs = []
    csv_object_storage_buckets = []
    csv_security_bastions = []
    csv_security_logging = []
    csv_security_kms_vault = []
    csv_security_cloud_guard = []
    csv_container = []
    csv_container_nodepool = []
    csv_edge_waas_policies = []
    csv_edge_dns_steering_policies = []
    csv_edge_healthcheck = []
    csv_apigw = []
    csv_limits = []
    csv_paas_oac = []
    csv_paas_oic = []
    csv_paas_ocvs = []
    csv_paas_oce = []
    csv_paas_vb = []
    csv_data_ai_oda = []
    csv_data_ai_bds = []
    csv_data_science = []
    csv_data_flow = []
    csv_data_catalog = []
    csv_data_conn_registgry = []
    csv_data_integration = []
    start_time = ""
    csv_add_date_field = True
    csv_columns = []
    csv_monitor_agents = []
    csv_monitor_db_management = []
    csv_monitor_alarms = []
    csv_monitor_events = []
    csv_notifications = []

    ############################################
    # Init
    # accept start time as string
    ############################################
    def __init__(self, start_time):
        self.start_time = start_time

    ##########################################################################
    # generate_csv
    ##########################################################################
    def generate_csv(self, data, csv_file_header, add_date_field=True, csv_columns=""):
        self.csv_add_date_field = add_date_field
        self.csv_file_header = csv_file_header
        self.csv_columns = str(csv_columns).split(",")
        try:
            for d in data:
                if 'type' in d:

                    if d['type'] == "identity":
                        self.__csv_identity_main(d['data'])

                    elif d['type'] == "region":
                        self.__csv_region_data(d['region'], d['data'])

                        if 'limits' in d:
                            self.__csv_limits_main(d['region'], d['limits'])

                    else:
                        continue

            # generate CSV files from each file
            self.__print_header("Processing CSV Files", 0)
            self.__export_to_csv_file("identity_compartments", self.csv_identity_compartments)
            self.__export_to_csv_file("identity_users", self.csv_identity_users)
            self.__export_to_csv_file("identity_policy", self.csv_identity_policies)
            self.__export_to_csv_file("identity_groups", self.csv_identity_groups)
            self.__export_to_csv_file("compute", self.csv_compute)
            self.__export_to_csv_file("compute_reservations", self.csv_compute_reservations)
            self.__export_to_csv_file("block_volumes", self.csv_block_volumes)
            self.__export_to_csv_file("block_volumes_backups", self.csv_block_volumes_backups)
            self.__export_to_csv_file("network_subnet", self.csv_network_subnet)
            self.__export_to_csv_file("network_subnet_prv_ips", self.csv_network_subnet_prv_ips)
            self.__export_to_csv_file("network_drgs", self.csv_network_drg)
            self.__export_to_csv_file("network_drg_ipsec_tunnels", self.csv_network_drg_ipsec_tunnels)
            self.__export_to_csv_file("network_drg_virtual_circuits", self.csv_network_drg_virtual_circuits)
            self.__export_to_csv_file("network_routes", self.csv_network_routes)
            self.__export_to_csv_file("network_security_list", self.csv_network_security_list)
            self.__export_to_csv_file("network_security_group", self.csv_network_security_group)
            self.__export_to_csv_file("network_dhcp_options", self.csv_network_dhcp_options)
            self.__export_to_csv_file("database", self.csv_database)
            self.__export_to_csv_file("database_backups", self.csv_database_backups)
            self.__export_to_csv_file("database_autonomous", self.csv_db_autonomous)
            self.__export_to_csv_file("database_db_all", self.csv_db_all)
            self.__export_to_csv_file("database_db_vm_bm", self.csv_db_vm_bm)
            self.__export_to_csv_file("database_db_exa_infra", self.csv_db_exa_infrastructure)
            self.__export_to_csv_file("database_db_exacs", self.csv_db_exacs_vmclusters)
            self.__export_to_csv_file("database_db_exacc", self.csv_db_exacc_vmclusters)
            self.__export_to_csv_file("load_balancer_listeners", self.csv_load_balancer)
            self.__export_to_csv_file("load_balancer_backendset", self.csv_load_balancer_bs)
            self.__export_to_csv_file("file_storage", self.csv_file_storage)
            self.__export_to_csv_file("api_gateways", self.csv_apigw)
            self.__export_to_csv_file("limits", self.csv_limits)
            self.__export_to_csv_file("object_storage_buckets", self.csv_object_storage_buckets)
            self.__export_to_csv_file("security_bastions", self.csv_security_bastions)
            self.__export_to_csv_file("security_loggings", self.csv_security_logging)
            self.__export_to_csv_file("security_cloud_guards", self.csv_security_cloud_guard)
            self.__export_to_csv_file("security_kms_vaults", self.csv_security_kms_vault)
            self.__export_to_csv_file("containers", self.csv_container)
            self.__export_to_csv_file("containers_nodepools", self.csv_container_nodepool)
            self.__export_to_csv_file("edge_dns_steering_policies", self.csv_edge_dns_steering_policies)
            self.__export_to_csv_file("edge_waas_policies", self.csv_edge_waas_policies)
            self.__export_to_csv_file("edge_healthchecks", self.csv_edge_healthcheck)
            self.__export_to_csv_file("paas_oac", self.csv_paas_oac)
            self.__export_to_csv_file("paas_oic", self.csv_paas_oic)
            self.__export_to_csv_file("paas_ocvs_vmware", self.csv_paas_ocvs)
            self.__export_to_csv_file("paas_oce", self.csv_paas_oce)
            self.__export_to_csv_file("paas_visualbuilder", self.csv_paas_vb)
            self.__export_to_csv_file("data_science", self.csv_data_science)
            self.__export_to_csv_file("data_flow", self.csv_data_flow)
            self.__export_to_csv_file("data_catalog", self.csv_data_catalog)
            self.__export_to_csv_file("data_conn_registry", self.csv_data_conn_registgry)
            self.__export_to_csv_file("data_integration", self.csv_data_integration)
            self.__export_to_csv_file("digital_assistance", self.csv_data_ai_oda)
            self.__export_to_csv_file("big_data_service", self.csv_data_ai_bds)
            self.__export_to_csv_file("monitor_agents", self.csv_monitor_agents)
            self.__export_to_csv_file("monitor_db_managements", self.csv_monitor_db_management)
            self.__export_to_csv_file("monitor_alarms", self.csv_monitor_alarms)
            self.__export_to_csv_file("monitor_events", self.csv_monitor_events)
            self.__export_to_csv_file("monitor_topics_subs", self.csv_notifications)

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

            # add start_date to each dictionary
            result = []
            if self.csv_add_date_field:
                result = [dict(item, extract_date=self.start_time) for item in data]
            else:
                result = [dict(item) for item in data]

            # generate fields
            fields = [key for key in result[0].keys()]

            with open(file_name, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fields)

                # write header
                writer.writeheader()

                for row in result:
                    writer.writerow(row)

            print("CSV: " + file_subject.ljust(26) + " --> " + file_name)

        except Exception as e:
            raise Exception("Error in __export_to_csv_file: " + str(e.args))

    ##########################################################################
    # print error
    ##########################################################################
    def __print_error(self, msg, e):
        classname = type(self).__name__

        if isinstance(e, KeyError):
            print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + msg + ": " + str(e))

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

            ret_str = str(', '.join(key + "=" + freeform_tag[key] for key in freeform_tag.keys()))

            return ret_str

        except Exception as e:
            self.__print_error("__get_freeform_tags", e)

    ##########################################################################
    # check if managed paas compartment
    ##########################################################################
    def __if_managed_paas_compartment(self, name):
        return name == "ManagedCompartmentForPaaS"

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
    # CSV Identity Users
    ##########################################################################

    def __csv_identity_users(self, users):
        try:
            for user in users:
                data = {
                    'id': user['id'],
                    'user_name': user['name'],
                    'description': user['description'],
                    'is_mfa_activated': user['is_mfa_activated'],
                    'lifecycle_state': user['lifecycle_state'],
                    'identity_provider_name': user['identity_provider_name'],
                    'user_time_created': user['time_created'],
                    'groups': user['groups'],
                    'api_keys': "Not Checked",
                    'auth_token': "Not Checked",
                    'secret_key': "Not Checked",
                    'smtp_cred': "Not Checked",
                    'last_successful_login_time': user['last_successful_login_time'],
                    'previous_successful_login_time': user['previous_successful_login_time']
                }

                # Check if credential exist
                if 'api_keys' in user:
                    data['api_keys'] = str(', '.join(x['id'] + " - " + x['lifecycle_state'] + " - " + x['time_created'] for x in user['api_keys']))
                if 'auth_token' in user:
                    data['auth_token'] = str(', '.join(x['id'] + " - " + x['description'] + " - " + x['time_created'] for x in user['auth_token']))
                if 'secret_key' in user:
                    data['secret_key'] = str(', '.join(x['id'] + " - " + x['display_name'] + " - " + x['time_created'] for x in user['secret_key']))
                if 'smtp_cred' in user:
                    data['smtp_cred'] = str(', '.join(x['id'] + " - " + x['description'] + " - " + x['time_created'] for x in user['smtp_cred']))

                self.csv_identity_users.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_users", e)

    ##########################################################################
    # CSV Identity Compartments
    ##########################################################################

    def __csv_identity_compartments(self, compartments):
        try:
            for compartment in compartments:
                data = {
                    'id': compartment['id'],
                    'name': compartment['name'],
                    'description': compartment['description'],
                    'time_created': compartment['time_created'],
                    'path': compartment['path']
                }
                self.csv_identity_compartments.append(data)

        except Exception as e:
            self.__print_error("__csv_identity_compartments", e)

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
                        self.csv_identity_policies.append({'compartment': c['compartment_path'], 'policy_name': policy['name'], 'seq': seq, 'statement': statement})

        except Exception as e:
            self.__print_error("__csv_identity_policies", e)

    ##########################################################################
    # CSV Identity Module
    ##########################################################################
    def __csv_identity_main(self, data):
        try:
            if 'compartments' in data:
                self.__csv_identity_compartments(data['compartments'])

            if 'users' in data:
                self.__csv_identity_users(data['users'])
            if 'groups' in data:
                self.__csv_identity_groups(data['groups'])

            if 'policies' in data:
                self.__csv_identity_policies(data['policies'])

        except Exception as e:
            self.__print_error("__csv_identity_main", e)

    ##########################################################################
    # CSV Network Subnets
    ##########################################################################
    def __csv_core_network_vcn_subnet(self, region_name, subnets, vcn, igw, sgw, nat, drg, lpg):
        try:
            for subnet in subnets:
                data = {'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': vcn['cidr_block'],
                        'vcn_cidrs': vcn['cidr_blocks'],
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
                        'security_list': str(', '.join(x for x in subnet['security_list'])),
                        'dns': subnet['dns'],
                        'logs': str(', '.join(x['name'] for x in subnet['logs'])),
                        'vcn_id': vcn['id'],
                        'subnet_id': subnet['id']}
                self.csv_network_subnet.append(data)

                # private ips
                for ip in subnet['private_ips']:
                    data = {'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_cidrs': vcn['cidr_blocks'],
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
                    data = {'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_path': vcn['compartment_path'],
                            'sec_name': sl['name'],
                            'sec_compartment': sl['compartment_name'],
                            'sec_compartment_path': sl['compartment_path'],
                            'sec_protocol': "",
                            'is_stateless': "",
                            'sec_rules': "Empty",
                            'time_created': sl['time_created'][0:16],
                            'vcn_id': vcn['id'],
                            'sec_id': sl['id']
                            }
                    self.csv_network_security_list.append(data)

                else:
                    for slr in sl['sec_rules']:
                        data = {'region_name': region_name,
                                'vcn_name': vcn['display_name'],
                                'vcn_cidr': vcn['cidr_block'],
                                'vcn_compartment': vcn['compartment_name'],
                                'vcn_compartment_path': vcn['compartment_path'],
                                'sec_name': sl['name'],
                                'sec_compartment': sl['compartment_name'],
                                'sec_compartment_path': sl['compartment_path'],
                                'sec_protocol': slr['protocol_name'],
                                'is_stateless': slr['is_stateless'],
                                'sec_rules': slr['desc'],
                                'time_created': sl['time_created'],
                                'vcn_id': vcn['id'],
                                'sec_id': sl['id']
                                }
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
                    'drg_route_tables': str(', '.join(x['display_name'] for x in drg['drg_route_tables'])),
                    'ip_sec_connections': str(', '.join(x['name'] + " " + x['tunnels_status'] for x in drg['ip_sec_connections'])),
                    'virtual_circuits': str(', '.join(x['name'] for x in drg['virtual_circuits'])),
                    'remote_peerings': str(', '.join(x['name'] + " " + x['peering_status'] for x in drg['remote_peerings'])),
                    'vcns': str(', '.join(x['name'] for x in drg['vcns'])),
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
                        'routes': str(', '.join(x for x in arr['routes'])),
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
                    'customer_bgp_asn': arr['customer_bgp_asn'],
                    'drg': arr['drg'],
                    'lifecycle_state': arr['lifecycle_state'],
                    'oracle_bgp_asn': arr['oracle_bgp_asn'],
                    'provider_name': arr['provider_name'],
                    'provider_service_name': arr['provider_service_name'],
                    'provider_state': arr['provider_state'],
                    'reference_comment': arr['reference_comment'],
                    'service_type': arr['service_type'],
                    'time_created': arr['time_created'],
                    'cross_connect_mappings': arr['cross_connect_mappings'],
                    'type': arr['type'],
                    'drg_route_table': arr['drg_route_table'],
                    'drg_id': arr['drg_id'],
                    'drg_route_table_id': arr['drg_route_table_id'],
                    'id': arr['id']
                }
                self.csv_network_drg_virtual_circuits.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_virtual_circuit", e)

    ##########################################################################
    # CSV for  Network vcn security group
    ##########################################################################
    def __csv_core_network_vcn_security_groups(self, region_name, nsg, vcn):
        try:
            if not nsg:
                return

            for sl in nsg:
                if len(sl['sec_rules']) == 0:
                    data = {'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_path': vcn['compartment_path'],
                            'sec_name': sl['name'],
                            'sec_compartment': sl['compartment_name'],
                            'sec_compartment_path': sl['compartment_path'],
                            'sec_protocol': "",
                            'is_stateless': "",
                            'sec_rules': "Empty",
                            'time_created': sl['time_created'],
                            'vcn_id': vcn['id'],
                            'sec_id': sl['id']
                            }
                    self.csv_network_security_list.append(data)

                else:
                    for slr in sl['sec_rules']:
                        data = {'region_name': region_name,
                                'vcn_name': vcn['display_name'],
                                'vcn_cidr': vcn['cidr_block'],
                                'vcn_compartment': vcn['compartment_name'],
                                'vcn_compartment_path': vcn['compartment_path'],
                                'sec_name': sl['name'],
                                'sec_compartment': sl['compartment_name'],
                                'sec_compartment_path': sl['compartment_path'],
                                'sec_protocol': slr['protocol_name'],
                                'is_stateless': slr['is_stateless'],
                                'sec_rules': slr['desc'],
                                'time_created': sl['time_created'],
                                'vcn_id': vcn['id'],
                                'sec_id': sl['id']
                                }
                        self.csv_network_security_group.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_security_groups", e)

    ##########################################################################
    # csv DHCP options for DHCP_ID
    ##########################################################################

    def __csv_core_network_vcn_dhcp_options(self, region_name, dhcp_options, vcn):
        try:
            for dhcp in dhcp_options:
                data = {'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': vcn['cidr_block'],
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
                    data = {'region_name': region_name,
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_path': vcn['compartment_path'],
                            'route_name': rt['name'],
                            'route_compartment': rt['compartment_name'],
                            'route_compartment_path': rt['compartment_path'],
                            'destination': "",
                            'route': "Empty",
                            'time_created': rt['time_created'][0:16],
                            'vcn_id': vcn['id'],
                            'route_id': rt['id']
                            }
                    self.csv_network_routes.append(data)

                else:
                    for rl in rt['route_rules']:
                        data = {'region_name': region_name,
                                'vcn_name': vcn['display_name'],
                                'vcn_cidr': vcn['cidr_block'],
                                'vcn_compartment': vcn['compartment_name'],
                                'vcn_compartment_path': vcn['compartment_path'],
                                'route_name': rt['name'],
                                'route_compartment': rt['compartment_name'],
                                'route_compartment_path': rt['compartment_path'],
                                'destination': rl['destination'],
                                'route': rl['desc'],
                                'time_created': rt['time_created'][0:16],
                                'vcn_id': vcn['id'],
                                'route_id': rt['id']
                                }
                        self.csv_network_routes.append(data)

        except Exception as e:
            self.__print_error("__csv_core_network_vcn_route_tables", e)

    ##########################################################################
    # csv network vcn
    ##########################################################################
    def __csv_core_network_vcn(self, region_name, vcns):

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

                if 'igw' in vcn['data']:
                    igw = str(', '.join(x['name'] for x in vcn['data']['igw']))

                if 'sgw' in vcn['data']:
                    sgw = str(', '.join(x['name'] + " " + x['services'] for x in vcn['data']['sgw']))

                if 'nat' in vcn['data']:
                    nat = str(', '.join(x['name'] for x in vcn['data']['nat']))

                if 'drg_attached' in vcn['data']:
                    drg = str(', '.join(x['name'] for x in vcn['data']['drg_attached']))

                if 'local_peering' in vcn['data']:
                    lpg = str(', '.join(x['name'] for x in vcn['data']['local_peering']))

                if 'subnets' in vcn['data']:
                    self.__csv_core_network_vcn_subnet(region_name, vcn['data']['subnets'], vcn, igw, sgw, nat, drg, lpg)

                if 'security_lists' in vcn['data']:
                    self.__csv_core_network_vcn_security_lists(region_name, vcn['data']['security_lists'], vcn)

                if 'security_groups' in vcn['data']:
                    self.__csv_core_network_vcn_security_groups(region_name, vcn['data']['security_groups'], vcn)

                if 'route_tables' in vcn['data']:
                    self.__csv_core_network_vcn_route_tables(region_name, vcn['data']['route_tables'], vcn)

                if 'dhcp_options' in vcn['data']:
                    self.__csv_core_network_vcn_dhcp_options(region_name, vcn['data']['dhcp_options'], vcn)

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

        except Exception as e:
            self.__print_error("__csv_core_network_main", e)

    ##########################################################################
    # csv database db systems
    ##########################################################################
    def __csv_database_db_system(self, region_name, list_db_systems):

        try:
            for dbs in list_db_systems:

                # Db System CSV
                dbsd = {'region_name': region_name,
                        'availability_domain': dbs['availability_domain'],
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
                        'backup_subnet': dbs['backup_subnet'],
                        'scan_ips': str(', '.join(x for x in dbs['scan_ips'])),
                        'vip_ips': str(', '.join(x for x in dbs['vip_ips'])),
                        'cluster_name': dbs['cluster_name'],
                        'time_created': dbs['time_created'][0:16],
                        'domain': dbs['domain'],
                        'db_nodes': str(', '.join(x['desc'] for x in dbs['db_nodes'])),
                        'db_homes': str(', '.join(x['home'] for x in dbs['db_homes'])),
                        'freeform_tags': str(', '.join(key + "=" + dbs['freeform_tags'][key] for key in dbs['freeform_tags'].keys())),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                        'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                        'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                        'id': dbs['id'],
                        'infra_id': ''
                        }

                self.csv_db_all.append(dbsd)
                self.csv_db_vm_bm.append(dbsd)

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
                            'cpu_core_count': dbs['cpu_core_count'],
                            'db_storage_gb': dbs['sum_size_gb'],
                            'shape_ocpus': dbs['shape_ocpu'],
                            'memory_gb': dbs['shape_memory_gb'],
                            'local_storage_tb': dbs['shape_storage_tb'],
                            'node_count': len(dbs['db_nodes']),
                            'database': db['name'],
                            'database_edition': dbs['database_edition_short'],
                            'license_model': dbs['license_model'],
                            'data_subnet': dbs['data_subnet'],
                            'backup_subnet': dbs['backup_subnet'],
                            'scan_ips': str(', '.join(x for x in dbs['scan_ips'])),
                            'vip_ips': str(', '.join(x for x in dbs['vip_ips'])),
                            'pdbs': str(', '.join(x['name'] for x in db['pdbs'])),
                            'cluster_name': dbs['cluster_name'],
                            'vm_name': dbs['display_name'],
                            'time_created': dbs['time_created'][0:16],
                            'domain': dbs['domain'],
                            'auto_backup_enabled': db['auto_backup_enabled'],
                            'db_nodes': str(', '.join(x['desc'] for x in dbs['db_nodes'])),
                            'freeform_tags': str(', '.join(key + "=" + db['freeform_tags'][key] for key in db['freeform_tags'].keys())),
                            'defined_tags': self.__get_defined_tags(db['defined_tags']),
                            'database_id': db['id'],
                            'dbsystem_id': dbs['id'],
                            'db_home': db_home['home_name'],
                            'db_home_version': db_home['home_version']
                        }

                        self.csv_database.append(data)

                        # database Backups
                        if 'backups' in db:
                            for backup in db['backups']:
                                data = {
                                    'region_name': region_name,
                                    'compartment_name': dbs['compartment_name'],
                                    'compartment_path': dbs['compartment_path'],
                                    'dbs_name': dbs['display_name'],
                                    'database': db['db_name'],
                                    'shape': dbs['shape'],
                                    'backup_name': backup['display_name'],
                                    'time': backup['time'],
                                    'size': backup['size'],
                                    'lifecycle_state': backup['lifecycle_state']
                                }
                                self.csv_database_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_database_db_system", e)

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
                        'max_cpu_count': dbs['shape_ocpu'],
                        'memory_size_in_gbs': "",
                        'max_memory_in_gbs': dbs['shape_memory_gb'],
                        'db_node_storage_size_in_gbs': "",
                        'max_db_node_storage_in_g_bs': "",
                        'data_storage_size_in_tbs': "",
                        'max_data_storage_in_t_bs': dbs['shape_storage_tb'],
                        'total_storage_size_in_gbs': dbs['total_storage_size_in_gbs'],
                        'available_storage_size_in_gbs': dbs['available_storage_size_in_gbs'],
                        'storage_count': dbs['storage_count'],
                        'additional_storage_count': "",
                        'activated_storage_count': "",
                        'compute_count': dbs['compute_count'],
                        'dns_server': "",
                        'ntp_server': "",
                        'csi_number': "",
                        'node_count': "",
                        'db_servers': str(', '.join(x['desc'] for x in dbs['db_servers'])),
                        'db_servers_ids': str(', '.join(x['id'] for x in dbs['db_servers'])),
                        'cluster_count': len(dbs['vm_clusters']),
                        'cluster_names': str(', '.join(x['display_name'] for x in dbs['vm_clusters'])),
                        'time_created': dbs['time_created'],
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                        'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                        'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                        'infra_id': dbs['id']
                        }
                self.csv_db_exa_infrastructure.append(infs)

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
                            'backup_subnet': vm['backup_subnet'],
                            'scan_ips': str(', '.join(x for x in vm['scan_ips'])),
                            'vip_ips': str(', '.join(x for x in vm['vip_ips'])),
                            'cluster_name': vm['cluster_name'],
                            'time_created': vm['time_created'][0:16],
                            'domain': vm['domain'],
                            'db_nodes': str(', '.join(x['desc'] for x in vm['db_nodes'])),
                            'db_homes': str(', '.join(x['home'] for x in vm['db_homes'])),
                            'freeform_tags': str(', '.join(key + "=" + vm['freeform_tags'][key] for key in vm['freeform_tags'].keys())),
                            'defined_tags': self.__get_defined_tags(vm['defined_tags']),
                            'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                            'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                            'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                            'id': vm['id'],
                            'infra_id': dbs['id']
                            }

                    self.csv_db_all.append(dbsd)
                    self.csv_db_exacs_vmclusters.append(dbsd)

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
                                    'backup_subnet': vm['backup_subnet'],
                                    'scan_ips': str(', '.join(x for x in vm['scan_ips'])),
                                    'vip_ips': str(', '.join(x for x in vm['vip_ips'])),
                                    'pdbs': str(', '.join(x['name'] for x in db['pdbs'])),
                                    'cluster_name': vm['cluster_name'],
                                    'vm_name': vm['display_name'],
                                    'time_created': vm['time_created'][0:16],
                                    'domain': vm['domain'],
                                    'auto_backup_enabled': db['auto_backup_enabled'],
                                    'db_nodes': str(', '.join(x['desc'] for x in vm['db_nodes'])),
                                    'freeform_tags': str(', '.join(key + "=" + db['freeform_tags'][key] for key in db['freeform_tags'].keys())),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': db_home['home_name'],
                                    'db_home_version': db_home['home_version']
                                    }

                            self.csv_database.append(data)

                            # database Backups
                            if 'backups' in db:
                                for backup in db['backups']:
                                    data = {
                                        'region_name': region_name,
                                        'compartment_name': dbs['compartment_name'],
                                        'compartment_path': dbs['compartment_path'],
                                        'dbs_name': dbs['display_name'],
                                        'database': db['db_name'],
                                        'shape': dbs['shape'],
                                        'backup_name': backup['display_name'],
                                        'time': backup['time'],
                                        'size': backup['size'],
                                        'lifecycle_state': backup['lifecycle_state']
                                    }
                                    self.csv_database_backups.append(data)

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
                        'db_servers': str(', '.join(x['desc'] for x in dbs['db_servers'])),
                        'db_servers_ids': str(', '.join(x['id'] for x in dbs['db_servers'])),
                        'cluster_count': len(dbs['vm_clusters']),
                        'cluster_names': str(', '.join(x['display_name'] for x in dbs['vm_clusters'])),
                        'time_created': dbs['time_created'],
                        'freeform_tags': self.__get_freeform_tags(dbs['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                        'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                        'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                        'infra_id': dbs['id']
                        }
                self.csv_db_exa_infrastructure.append(infs)

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
                            'backup_subnet': "",
                            'scan_ips': "",
                            'vip_ips': "",
                            'cluster_name': vm['display_name'],
                            'time_created': vm['time_created'][0:16],
                            'domain': "",
                            'db_nodes': str(', '.join(x['desc'] for x in vm['db_nodes'])),
                            'db_homes': str(', '.join(x['home'] for x in vm['db_homes'])),
                            'freeform_tags': str(', '.join(key + "=" + vm['freeform_tags'][key] for key in vm['freeform_tags'].keys())),
                            'defined_tags': self.__get_defined_tags(vm['defined_tags']),
                            'maintenance_window': dbs['maintenance_window']['display'] if dbs['maintenance_window'] else "",
                            'last_maintenance_run': dbs['last_maintenance_run']['maintenance_display'] if dbs['last_maintenance_run'] else "",
                            'next_maintenance_run': dbs['next_maintenance_run']['maintenance_display'] if dbs['next_maintenance_run'] else "",
                            'id': vm['id'],
                            'infra_id': dbs['id'],
                            }

                    self.csv_db_all.append(dbsd)
                    self.csv_db_exacc_vmclusters.append(dbsd)

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
                                    'backup_subnet': "",
                                    'scan_ips': "",
                                    'vip_ips': "",
                                    'pdbs': str(', '.join(x['name'] for x in db['pdbs'])),
                                    'cluster_name': vm['display_name'],
                                    'vm_name': vm['display_name'],
                                    'time_created': vm['time_created'][0:16],
                                    'domain': "",
                                    'auto_backup_enabled': db['auto_backup_enabled'],
                                    'db_nodes': str(', '.join(x['desc'] for x in vm['db_nodes'])),
                                    'freeform_tags': str(', '.join(key + "=" + db['freeform_tags'][key] for key in db['freeform_tags'].keys())),
                                    'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                    'database_id': db['id'],
                                    'dbsystem_id': vm['id'],
                                    'db_home': db_home['home_name'],
                                    'db_home_version': db_home['home_version']
                                    }

                            self.csv_database.append(data)

                            # database Backups
                            if 'backups' in db:
                                for backup in db['backups']:
                                    data = {
                                        'region_name': region_name,
                                        'compartment_name': dbs['compartment_name'],
                                        'compartment_path': dbs['compartment_path'],
                                        'dbs_name': dbs['display_name'],
                                        'database': db['db_name'],
                                        'shape': dbs['shape'],
                                        'backup_name': backup['display_name'],
                                        'time': backup['time'],
                                        'size': backup['size'],
                                        'lifecycle_state': backup['lifecycle_state']
                                    }
                                    self.csv_database_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_database_db_exacc", e)

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
                        'cpu_core_count': dbs['cpu_core_count'],
                        'db_storage_gb': str(int(dbs['data_storage_size_in_tbs']) * 1024),
                        'shape_ocpus': "",
                        'memory_gb': "",
                        'local_storage_tb': "",
                        'node_count': "",
                        'database': dbs['db_name'],
                        'database_edition': 'ADB',
                        'license_model': dbs['license_model'],
                        'data_subnet': "",
                        'backup_subnet': "",
                        'scan_ips': "",
                        'vip_ips': "",
                        'pdbs': "",
                        'vm_name': "",
                        'cluster_name': "",
                        'time_created': dbs['time_created'],
                        'domain': "",
                        'auto_backup_enabled': "True",
                        'db_nodes': "",
                        'freeform_tags': str(', '.join(key + "=" + dbs['freeform_tags'][key] for key in dbs['freeform_tags'].keys())),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'database_id': "",
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
                        'container_name': "",
                        'cpu_core_count': dbs['cpu_core_count'],
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
                        'nsg_ids': dbs['nsg_ids'] if dbs['nsg_ids'] != "None" else "",
                        'nsg_names': str(', '.join(x for x in dbs['nsg_names'])),
                        'whitelisted_ips': dbs['whitelisted_ips'],
                        'service_console_url': dbs['service_console_url'],
                        'connection_strings': dbs['connection_strings'],
                        'is_auto_scaling_enabled': dbs['is_auto_scaling_enabled'],
                        'is_dedicated': dbs['is_dedicated'],
                        'freeform_tags': str(', '.join(key + "=" + dbs['freeform_tags'][key] for key in dbs['freeform_tags'].keys())),
                        'defined_tags': self.__get_defined_tags(dbs['defined_tags']),
                        'id': dbs['id']
                        }

                self.csv_db_autonomous.append(dadb)

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
                            'backup_name': ("Automatic Backup - " if backup['is_automatic'] == 'True' else "") + backup['display_name'],
                            'time': backup['time'],
                            'size': "",
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
                for vm in dbs['containers']:
                    for db in vm['databases']:
                        data = {'region_name': region_name,
                                'availability_domain': dbs['availability_domain'],
                                'compartment_name': dbs['compartment_name'],
                                'compartment_path': dbs['compartment_path'],
                                'status': dbs['lifecycle_state'],
                                'type': "Autonomous Dedicated " + str(db['db_workload']),
                                'name': db['display_name'],
                                'shape': dbs['shape'],
                                'cpu_core_count': db['cpu_core_count'],
                                'db_storage_gb': str(int(db['data_storage_size_in_tbs']) * 1024),
                                'shape_ocpus': dbs['shape_ocpu'],
                                'memory_gb': dbs['shape_memory_gb'],
                                'local_storage_tb': dbs['shape_storage_tb'],
                                'node_count': "",
                                'database': db['name'],
                                'database_edition': 'ADB-D',
                                'license_model': dbs['license_model'],
                                'data_subnet': dbs['subnet_name'],
                                'backup_subnet': "",
                                'scan_ips': "",
                                'vip_ips': "",
                                'pdbs': "",
                                'vm_name': dbs['name'],
                                'cluster_name': vm['name'],
                                'time_created': db['time_created'],
                                'domain': dbs['domain'],
                                'auto_backup_enabled': "True",
                                'db_nodes': "",
                                'freeform_tags': str(', '.join(key + "=" + db['freeform_tags'][key] for key in db['freeform_tags'].keys())),
                                'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                'database_id': db['id'],
                                'dbsystem_id': dbs['id'],
                                'db_home': "",
                                'db_home_version': ""
                                }
                        self.csv_database.append(data)

                        # for autonomous only
                        dadb = {'region_name': region_name,
                                'compartment_name': dbs['compartment_name'],
                                'compartment_path': dbs['compartment_path'],
                                'status': db['lifecycle_state'],
                                'type': "Autonomous Dedicated " + db['db_workload'],
                                'name': db['display_name'],
                                'infra_name': dbs['display_name'],
                                'container_name': vm['display_name'],
                                'cpu_core_count': db['cpu_core_count'],
                                'db_storage_tb': db['data_storage_size_in_tbs'],
                                'db_version': db['db_version'],
                                'db_name': db['db_name'],
                                'version_license_model': dbs['license_model'],
                                'time_created': db['time_created'],
                                'data_safe_status': db['data_safe_status'],
                                'time_maintenance_begin': db['time_maintenance_begin'],
                                'time_maintenance_end': db['time_maintenance_end'],
                                'subnet_id': dbs['subnet_id'] if dbs['subnet_id'] != "None" else "",
                                'subnet_name': dbs['subnet_name'] if dbs['subnet_name'] != "None" else "",
                                'private_endpoint': db['private_endpoint'] if db['private_endpoint'] != "None" else "",
                                'private_endpoint_label': db['private_endpoint_label'] if db['private_endpoint_label'] != "None" else "",
                                'nsg_ids': db['nsg_ids'] if db['nsg_ids'] != "None" else "",
                                'nsg_names': str(', '.join(x for x in dbs['nsg_names'])),
                                'whitelisted_ips': db['whitelisted_ips'],
                                'service_console_url': db['service_console_url'],
                                'connection_strings': db['connection_strings'],
                                'is_auto_scaling_enabled': db['is_auto_scaling_enabled'],
                                'is_dedicated': db['is_dedicated'],
                                'freeform_tags': str(', '.join(key + "=" + db['freeform_tags'][key] for key in db['freeform_tags'].keys())),
                                'defined_tags': self.__get_defined_tags(db['defined_tags']),
                                'id': db['id']
                                }

                        self.csv_db_autonomous.append(dadb)

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
                                    'backup_name': ("Automatic Backup - " if backup['is_automatic'] == 'True' else "") + backup['display_name'],
                                    'time': backup['time'],
                                    'size': "",
                                    'lifecycle_state': backup['lifecycle_state']
                                }
                                self.csv_database_backups.append(data)

        except Exception as e:
            self.__print_error("__csv_database_db_autonomous_dedicated", e)

    ##########################################################################
    # database
    ##########################################################################

    def __csv_database_main(self, region_name, list_databases):
        try:

            if len(list_databases) == 0:
                return

            if 'exadata_infrustructure' in list_databases:
                self.__csv_database_db_exadata(region_name, list_databases['exadata_infrustructure'])

            if 'exacc_infrustructure' in list_databases:
                self.__csv_database_db_exacc(region_name, list_databases['exacc_infrustructure'])

            if 'db_system' in list_databases:
                self.__csv_database_db_system(region_name, list_databases['db_system'])

            if 'autonomous' in list_databases:
                self.__csv_database_db_autonomous(region_name, list_databases['autonomous'])

            if 'autonomous_dedicated' in list_databases:
                self.__csv_database_db_autonomous_dedicated(region_name, list_databases['autonomous_dedicated'])

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
                data = {'region_name': region_name,
                        'scope_type': lt['scope_type'],
                        'availability_domain': lt['availability_domain'],
                        'name': lt['name'],
                        'description': lt['description'],
                        'limit_name': lt['limit_name'],
                        'value': lt['value'],
                        'used': lt['used'],
                        'available': lt['available']
                        }

                self.csv_limits.append(data)

        except Exception as e:
            self.__print_error("__csv_limits_main", e)

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
                        'Status': instance['lifecycle_state'],
                        'Type': instance['image_os'],
                        'image': instance['image'],
                        'fault_domain': instance['fault_domain'],
                        'primary_vcn': "",
                        'primary_subnet': "",
                        'shape': instance['shape'],
                        'ocpus': instance['shape_ocpu'],
                        'memory_gb': instance['shape_memory_gb'],
                        'local_storage_tb': instance['shape_storage_tb'],
                        'public_ips': str(', '.join(x['details']['public_ip'] for x in instance['vnic'])),
                        'private_ips': str(', '.join(x['details']['private_ip'] for x in instance['vnic'])),
                        'security_groups': str(', '.join(x['details']['nsg_names'] for x in instance['vnic'])),
                        'internal_fqdn': str(', '.join(x['details']['internal_fqdn'] for x in instance['vnic'])),
                        'plugin_status': str(', '.join(x['name'] + ":" + x['status'] for x in instance['agent_plugin_status'])),
                        'time_created': instance['time_created'][0:16],
                        'boot_volume': "",
                        'boot_volume_size_gb': "",
                        'boot_volume_b_policy': "",
                        'boot_volume_encryption': "",
                        'block_volumes': "",
                        'block_volumes_total_gb': "",
                        'block_volumes_size_gb': "",
                        'block_volumes_b_policy': "",
                        'freeform_tags': str(', '.join(key + "=" + instance['freeform_tags'][key] for key in instance['freeform_tags'].keys())),
                        'defined_tags': self.__get_defined_tags(instance['defined_tags']),
                        'instance_id': instance['id']
                        }

                # add columns for csvcol parameter
                for csvcol in self.csv_columns:
                    data[csvcol] = self.__get_defined_tags_key_value(instance['defined_tags'], csvcol)

                # go over the vnics
                if 'vnic' in instance:

                    vnic_num = 0
                    for vnic in instance['vnic']:
                        vnic_num += 1

                        # for vnic #1 add primary vcn_subnet
                        if vnic_num == 1:
                            data['primary_vcn'] = vnic['details']['vcn']
                            data['primary_subnet'] = vnic['details']['subnet']

                if 'boot_volume' in instance:
                    for bv in instance['boot_volume']:
                        data['boot_volume'] = bv['display_name']
                        data['boot_volume_size_gb'] = bv['sum_size_gb']
                        data['boot_volume_b_policy'] = bv['backup_policy']
                        data['boot_volume_encryption'] = bv['is_pv_encryption_in_transit_enabled']

                if 'block_volume' in instance:
                    data['block_volumes'] = str(', '.join(x['display_name'] for x in instance['block_volume']))
                    data['block_volumes_size_gb'] = str('+ '.join(x['size'] for x in instance['block_volume']))
                    data['block_volumes_b_policy'] = str(', '.join(x['backup_policy'] for x in instance['block_volume']))

                    bv_total_size = 0
                    for bv in instance['block_volume']:
                        bv_total_size += int(bv['size'])
                    data['block_volumes_total_gb'] = str(bv_total_size)

                self.csv_compute.append(data)

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
                            'id': bv['id'],
                            'display_name': bv['display_name'],
                            'size': bv['size'],
                            'backup_policy': bv['backup_policy'],
                            'vpus_per_gb': bv['vpus_per_gb'],
                            'volume_group_name': bv['volume_group_name'],
                            'instance_name': instance['display_name'],
                            'instance_id': instance['id']
                        }
                        self.csv_block_volumes.append(data)

                # Add block Volumes
                if 'block_volume' in instance:
                    for bv in instance['block_volume']:
                        data = {
                            'region_name': region_name,
                            'availability_domain': instance['availability_domain'],
                            'compartment_name': bv['compartment_name'],
                            'compartment_path': bv['compartment_path'],
                            'id': bv['id'],
                            'display_name': bv['display_name'],
                            'size': bv['size'],
                            'backup_policy': bv['backup_policy'],
                            'vpus_per_gb': bv['vpus_per_gb'],
                            'volume_group_name': bv['volume_group_name'],
                            'instance_name': instance['display_name'],
                            'instance_id': instance['id']
                        }
                        self.csv_block_volumes.append(data)

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
                    'shapes_capacity': ",".join(x['instance_shape'] + ":Shape OCPUs=" + str(x['ocpus']) + ":Shape Mem=" + str(x['memory_in_gbs']) + " (Reserve=" + str(x['reserved_count']) + ":Use=" + str(x['used_count']) + ")" for x in ct['config'])
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
                    'display_name': bv['display_name'],
                    'size': bv['size'],
                    'backup_policy': bv['backup_policy'],
                    'vpus_per_gb': bv['vpus_per_gb'],
                    'volume_group_name': bv['volume_group_name'],
                    'instance_name': '',
                    'instance_id': ''
                }
                self.csv_block_volumes.append(data)

        except Exception as e:
            self.__print_error("__csv_core_compute_block_volumes", e)

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

                # if no listener
                if not lb['listeners']:
                    data = {'region_name': region_name,
                            'compartment_name': lb['compartment_name'],
                            'compartment_path': lb['compartment_path'],
                            'name': lb['display_name'],
                            'status': lb['status'],
                            'shape': lb['shape_name'],
                            'type': ("Private" if lb['is_private'] else "Public"),
                            'ip_addresses': str(', '.join(x for x in lb['ips'])),
                            'log_errors': log_errors,
                            'log_access': log_access,
                            'logs': str(', '.join(x['name'] for x in load_balance_obj['logs'])),
                            'subnets': str(', '.join(x for x in lb['subnets'])),
                            'listener_port': "No Listener",
                            'listener_def_bs': "",
                            'listener_ssl': "",
                            'listener_path': "",
                            'listener_rule': "",
                            'listener_host': "",
                            'lb_certificates': lb['certificates'],
                            'loadbalancer_id': lb['id']
                            }
                    self.csv_load_balancer.append(data)

                # look over the listeners
                for listener in lb['listeners']:
                    data = {'region_name': region_name,
                            'compartment_name': lb['compartment_name'],
                            'compartment_path': lb['compartment_path'],
                            'name': lb['display_name'],
                            'status': lb['status'],
                            'shape': lb['shape_name'],
                            'type': ("Private" if lb['is_private'] else "Public"),
                            'ip_addresses': str(', '.join(x for x in lb['ips'])),
                            'log_errors': log_errors,
                            'log_access': log_access,
                            'logs': str(', '.join(x['name'] for x in load_balance_obj['logs'])),
                            'subnets': str(', '.join(x for x in lb['subnets'])),
                            'listener_port': listener['port'],
                            'listener_def_bs': listener['default_backend_set_name'],
                            'listener_ssl': listener['ssl_configuration'],
                            'listener_host': str(', '.join(x for x in listener['hostname_names'])),
                            'listener_path': listener['path_route_set_name'],
                            'listener_rule': str(', '.join(x for x in listener['rule_set_names'])),
                            'lb_certificates': lb['certificates'],
                            'loadbalancer_id': lb['id']
                            }
                    self.csv_load_balancer.append(data)

        except Exception as e:
            self.__print_error("__csv_load_balancer_details", e)

    ##########################################################################
    # csv load balancer config
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

                    data = {'region_name': region_name,
                            'compartment_name': dp['compartment_name'],
                            'compartment_path': dp['compartment_path'],
                            'gw_name': api['display_name'],
                            'gw_endpoint_type': api['endpoint_type'],
                            'gw_hostname': api['hostname'],
                            'gw_subnet_name': api['subnet_name'],
                            'gw_time_created': api['time_created'],
                            'dp_display_name': dp['display_name'],
                            'path_prefix': dp['path_prefix'],
                            'endpoint': dp['endpoint'],
                            'time_created': dp['time_created'],
                            'log_execution': log_execution,
                            'log_access': log_access,
                            'logs': str(', '.join(x['name'] for x in dp['logs'])),
                            'dp_id': dp['id'],
                            'api_id': api['id'],
                            }
                    self.csv_apigw.append(data)

        except Exception as e:
            self.__print_error("__csv_load_balancer_details", e)

    ##########################################################################
    # csv load balancer backedset
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

                        data = {'region_name': region_name,
                                'compartment_name': lb['compartment_name'],
                                'compartment_path': lb['compartment_path'],
                                'name': lb['display_name'],
                                'status': lb['status'],
                                'shape': lb['shape_name'],
                                'type': ("Private" if lb['is_private'] else "Public"),
                                'ip_addresses': str(', '.join(x for x in lb['ips'])),
                                'subnets': str(', '.join(x for x in lb['subnets'])),
                                'bs_name': bs['desc'],
                                'bs_status': bs['status'],
                                'health_check': bs['health_check']['desc1'] + " " + bs['health_check']['desc2'],
                                'session_persistence': session_persistence,
                                'ssl_cert': ssl_cert,
                                'backend': backend['desc'],
                                'loadbalancer_id': lb['id']
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
                    # list the exports
                    for ex in fs['exports']:
                        if ex['path'] not in exports:
                            exports += ex['path'] + ","

                        # list the Ips for each mount
                        for mnt in ex['mount_target']:
                            ip_to_add = str(','.join(x for x in mnt['private_ip_ids']))
                            if ip_to_add not in mount_ips:
                                mount_ips += ip_to_add + ","

                    data = {'region_name': region_name,
                            'compartment_name': fs['compartment_name'],
                            'compartment_path': fs['compartment_path'],
                            'availability_domain': fs['availability_domain'],
                            'display_name': fs['display_name'],
                            'size_gb': fs['size_gb'],
                            'id': fs['id'],
                            'exports': exports,
                            'mount_ips': mount_ips
                            }

                    self.csv_file_storage.append(data)

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
                        'objects': ar['objects'],
                        'size': ar['size'],
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
                        'logs': str(', '.join(x['name'] for x in ar['logs']))
                    }

                    self.csv_object_storage_buckets.append(data)

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

            if 'cloud_guard' in data:
                self.__csv_security_cloud_guard(region_name, data['cloud_guard'])

            if 'kms_vaults' in data:
                self.__csv_security_kms_vaults(region_name, data['kms_vaults'])

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
                        'target_vcn_id': ar['target_vcn_id'],
                        'target_subnet_id': ar['target_subnet_id']
                    }

                    self.csv_security_bastions.append(data)

        except Exception as e:
            self.__print_error("__csv_security_bastions", e)

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
                        'compartment_path': ar['compartment_path'],
                        'name': ar['display_name'],
                        'target_resource_type': ar['target_resource_type'],
                        'target_resource_id': ar['target_resource_id'],
                        'recipe_count': ar['recipe_count'],
                        'time_created': ar['time_created'][0:16],
                        'time_updated': ar['time_updated'][0:16],
                        'lifecycle_state': ar['lifecycle_state'],
                        'id': ar['id']
                    }

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
                        'id': ar['id'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags'])
                    }

                    self.csv_security_kms_vault.append(data)

        except Exception as e:
            self.__print_error("__csv_security_kms_vaults", e)

    ##########################################################################
    # Bastions
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
                            'log_id': lg['id']
                        }

                        self.csv_security_logging.append(data)

        except Exception as e:
            self.__print_error("__csv_security_logging", e)

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
                        'lifecycle_state': ar['lifecycle_state'],
                        'kubernetes_version': ar['kubernetes_version'],
                        'vcn': ar['vcn_name'],
                        'node_pools': len(ar['node_pools']),
                        'id': ar['id'],
                        'vcn_id': ar['vcn_id'],
                    }

                    self.csv_container.append(data)

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
                            'vcn': ar['vcn_name'],
                            'subnets': str(', '.join(x for x in nd['subnets'])),
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

            # Containers
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

        except Exception as e:
            self.__print_error("__csv_edge_waas_policies", e)

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
                        'health_check_monitor_id': ar['health_check_monitor_id'],
                        'time_created': ar['time_created'][0:16],
                        'id': ar['id']
                    }

                    self.csv_edge_dns_steering_policies.append(data)

        except Exception as e:
            self.__print_error("__csv_edge_dns_steering", e)

    ##########################################################################
    # Edge Healthchecl
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
                        'id': ar['id']
                    }

                    self.csv_edge_healthcheck.append(data)

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
                        'id': ar['id']
                    }

                    self.csv_edge_healthcheck.append(data)

        except Exception as e:
            self.__print_error("__csv_edge_healthcheck", e)

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
                        'consumption_model': ar['consumption_model'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_paas_oic.append(data)

        except Exception as e:
            self.__print_error("__csv_paas_oic", e)

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
                        'id': ar['id']
                    }

                    self.csv_paas_oac.append(data)

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

        except Exception as e:
            self.__print_error("__csv_paas_visualbuilder", e)

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
                        'compute_availability_domain': ar['compute_availability_domain'],
                        'instance_display_name_prefix': ar['instance_display_name_prefix'],
                        'vmware_software_version': ar['vmware_software_version'],
                        'esxi_hosts_count': ar['esxi_hosts_count'],
                        'nsx_manager_fqdn': ar['nsx_manager_fqdn'],
                        'nsx_manager_private_ip': ar['nsx_manager_private_ip'],
                        'vcenter_fqdn': ar['vcenter_fqdn'],
                        'vcenter_private_ip': ar['vcenter_private_ip'],
                        'workload_network_cidr': ar['workload_network_cidr'],
                        'nsx_overlay_segment_name': ar['nsx_overlay_segment_name'],
                        'nsx_edge_uplink_ip': ar['nsx_edge_uplink_ip'],
                        'provisioning_subnet': ar['provisioning_subnet'],
                        'vsphere_vlan': ar['vsphere_vlan'],
                        'vmotion_vlan': ar['vmotion_vlan'],
                        'vsan_vlan': ar['vsan_vlan'],
                        'nsx_v_tep_vlan': ar['nsx_v_tep_vlan'],
                        'nsx_edge_v_tep_vlan': ar['nsx_edge_v_tep_vlan'],
                        'nsx_edge_uplink1_vlan': ar['nsx_edge_uplink1_vlan'],
                        'nsx_edge_uplink2_vlan': ar['nsx_edge_uplink2_vlan'],
                        'hcx_fqdn': ar['hcx_fqdn'],
                        'is_hcx_enabled': ar['is_hcx_enabled'],
                        'time_created': ar['time_created'][0:16],
                        'exsi_hosts': str(', '.join(x['display_name'] + " - " + x['current_sku'] for x in ar['esxihosts'])),
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_paas_ocvs.append(data)

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

            if 'data_connectivity_registry' in data:
                self.__csv_data_conn_registry(region_name, data['data_connectivity_registry'])

            if 'data_integration' in data:
                self.__csv_data_integration(region_name, data['data_integration'])

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
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_ai_oda.append(data)

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
                        'is_cloud_sql_configured': ar['is_cloud_sql_configured'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_ai_bds.append(data)

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
                        'time_created': ar['time_created'][0:16],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_flow.append(data)

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
                        'lifecycle_state': ar['lifecycle_state'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_catalog.append(data)

        except Exception as e:
            self.__print_error("__csv_data_catalog", e)

    ##########################################################################
    # Data Connectivity registry
    ##########################################################################
    def __csv_data_conn_registry(self, region_name, services):
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
                        'time_updated': ar['time_updated'][0:16],
                        'updated_by': ar['updated_by'],
                        'lifecycle_state': ar['lifecycle_state'],
                        'state_message': ar['state_message'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_conn_registgry.append(data)

        except Exception as e:
            self.__print_error("__csv_data_conn_registry", e)

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
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'id': ar['id']
                    }

                    self.csv_data_integration.append(data)

        except Exception as e:
            self.__print_error("__csv_data_integration", e)

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
                        'parent_container_id': ar['parent_container_id'],
                        'id': ar['id']
                    }

                    self.csv_monitor_db_management.append(data)

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
                        'destinations': str(', '.join(x for x in ar['destinations'])),
                        'destinations_names': str(', '.join(x for x in ar['destinations_names'])),
                        'is_enabled': ar['is_enabled'],
                        'freeform_tags': self.__get_freeform_tags(ar['freeform_tags']),
                        'defined_tags': self.__get_defined_tags(ar['defined_tags']),
                        'metric_compartment_id': ar['metric_compartment_id'],
                        'id': ar['id']
                    }

                    self.csv_monitor_alarms.append(data)

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
                            'freeform_tags': self.__get_freeform_tags(sr['freeform_tags']),
                            'defined_tags': self.__get_defined_tags(sr['defined_tags']),
                            'id': sr['id']
                        }

                        self.csv_notifications.append(data)

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
                if 'data_ai' in cdata:
                    self.__csv_data_ai_main(region_name, cdata['data_ai'])
                if 'monitoring' in cdata:
                    self.__csv_monitoring(region_name, cdata['monitoring'])
                if 'notifications' in cdata:
                    self.__csv_notifications(region_name, cdata['notifications'])

        except Exception as e:
            self.__print_error("__csv_region_data", e)
            raise
