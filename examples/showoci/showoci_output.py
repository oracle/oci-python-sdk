##########################################################################
# Copyright(c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# showocy_output.py
#
# @Created On  : Mar 17 2019
# @Last Updated: Apr  2 2019
# @author      : Adi Zohar
# @Version     : 19.4.2
#
# Supports Python 2.7 and above, Python 3 recommended
#
# coding: utf-8
#
##########################################################################
# This file has ShowOCIOutput class and ShowOCISummary class
# it accept data as JSON format and print nice output
##########################################################################
from __future__ import print_function


class ShowOCIOutput(object):

    ##########################################################################
    # spaces for align
    ##########################################################################
    tabs = ' ' * 4
    taba = '--> '
    tabs2 = tabs + tabs

    ############################################
    # Init
    ############################################
    def __init__(self):
        pass

    ##########################################################################
    # Print header centered
    ##########################################################################
    def print_header(self, name, category):
        options = {0: 90, 1: 60, 2: 30, 3: 75}
        chars = int(options[category])
        print("")
        print('#' * chars)
        print("#" + name.center(chars - 2, " ") + "#")
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

                    elif d['type'] == "region":
                        self.__print_region_data(d['region'], d['data'])
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
            print("Config File    : " + data['config_file'])
            print("Config Profile : " + data['config_profile'])
            print("Version        : " + data['version'])
            print("Date/Time      : " + data['datetime'])
            print("Comand Line    : " + data['cmdline'])
            print("OCI SDK Ver    : " + data['oci_sdk_version'])
            if 'proxy' in data:
                print("Proxy         : " + data['proxy'])
            if 'joutfile' in data:
                print("JSON Out      : " + data['joutfile'])

            print("")

        except Exception as e:
            raise Exception("Error in print_showoci_config: " + str(e.args))

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, msg, e):
        classname = type(self).__name__

        if isinstance(e, KeyError):
            print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + msg + ": " + str(e))

    ##########################################################################
    # Print Tenancy
    ##########################################################################
    def __print_identity_tenancy(self, tenancy):
        try:

            self.print_header("Tenancy", 1)
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
                print(self.taba + user['name'])
                print(self.tabs + "Groups : " + user['groups'])
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

                print("\n" + c['compartment_path'] + ":")
                for policy in policies:
                    print("")
                    print(self.taba + policy['name'] + ":")
                    print(self.tabs + "\n    ".join(policy['statements']))

        except Exception as e:
            self.__print_error("__print_identity_policies", e)

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
            if 'policies' in data:
                self.__print_identity_policies(data['policies'])
            if 'providers' in data:
                self.__print_identity_providers(data['providers'])

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
    # Print Network VCN Local Peering
    ##########################################################################

    def __print_core_network_vcn_subnet(self, subnets, vcn_compartment):
        try:
            for subnet in subnets:
                print("")
                print(self.tabs + "Subnet " + subnet['subnet'] + self.__print_core_network_vcn_compartment(vcn_compartment, subnet['compartment']))
                print(self.tabs + self.tabs + "Name    : " + subnet['name'])
                print(self.tabs + self.tabs + "DNS     : " + subnet['dns'])
                print(self.tabs + self.tabs + "DHCP    : " + subnet['dhcp_options'])
                print(self.tabs + self.tabs + "Route   : " + subnet['route'])
                for s in subnet['security_list']:
                    print(self.tabs + self.tabs + "Sec List: " + s)

        except Exception as e:
            self.__print_error("__print_core_network_vcn_subnet", e)

    ##########################################################################
    # get DHCP options for DHCP_ID
    ##########################################################################

    def __print_core_network_vcn_dhcp_options(self, dhcp_options, vcn_compartment):
        try:
            for dhcp in dhcp_options:
                print("")
                print(self.tabs + "DHCP Options: " + dhcp['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, dhcp['compartment']))

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
                print(self.tabs + "Sec List    : " + str(sl['name']) + self.__print_core_network_vcn_compartment(vcn_compartment, sl['compartment']))
                if len(sl['sec_rules']) == 0:
                    print(self.tabs + "            : Empty.")

                for slr in sl['sec_rules']:
                    print(self.tabs + self.tabs + slr)

        except Exception as e:
            self.__print_error("__print_core_network_vcn_security_lists", e)

    ########################################################################
    # Print Network vcn Route Tables
    ##########################################################################

    def __print_core_network_vcn_route_tables(self, route_tables, vcn_compartment):
        try:
            if not route_tables:
                return
            for rt in route_tables:
                print("")
                print(self.tabs + "Route Table : " + rt['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, rt['compartment']))
                if 'route_rules' not in rt:
                    print(self.tabs + self.tabs + "Route   : Empty.")
                    return
                if len(rt['route_rules']) == 0:
                    print(self.tabs + self.tabs + "Route   : Empty.")
                    return

                for rl in rt['route_rules']:
                    print(self.tabs + self.tabs + "Route   : " + str(rl))

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
                vcn_compartment = vcn['compartment']

                if 'igw' in vcn['data']:
                    for igwloop in vcn['data']['igw']:
                        print(self.tabs + "Internet GW : " + igwloop['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, igwloop['compartment']))

                if 'sgw' in vcn['data']:
                    for sgwloop in vcn['data']['sgw']:
                        print(self.tabs + "Service GW  : " + sgwloop['name'] + " - " + sgwloop['services'] + self.__print_core_network_vcn_compartment(vcn_compartment, sgwloop['compartment']))

                if 'nat' in vcn['data']:
                    for natloop in vcn['data']['nat']:
                        print(self.tabs + "NAT GW      : " + natloop['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, natloop['compartment']))

                if 'drg_attached' in vcn['data']:
                    for drgloop in vcn['data']['drg_attached']:
                        print(self.tabs + "DRG Attached: " + drgloop['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, drgloop['compartment']))

                if 'local_peering' in vcn['data']:
                    for lpeer in vcn['data']['local_peering']:
                        print(self.tabs + "Local Peer  : " + lpeer['name'] + self.__print_core_network_vcn_compartment(vcn_compartment, lpeer['compartment']))

                if 'subnets' in vcn['data']:
                    self.__print_core_network_vcn_subnet(vcn['data']['subnets'], vcn_compartment)

                if 'security_lists' in vcn['data']:
                    self.__print_core_network_vcn_security_lists(vcn['data']['security_lists'], vcn_compartment)

                if 'route_tables' in vcn['data']:
                    self.__print_core_network_vcn_route_tables(vcn['data']['route_tables'], vcn_compartment)

                if 'dhcp_options' in vcn['data']:
                    self.__print_core_network_vcn_dhcp_options(vcn['data']['dhcp_options'], vcn_compartment)

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
                print(self.taba + "DRG    " + drg)

        except Exception as e:
            self.__print_error("__print_core_network_vcn", e)

    ##########################################################################
    # print network remote peering
    ##########################################################################
    def __print_core_network_remote_peering(self, rpcs):

        try:
            if len(rpcs) == 0:
                return

            self.print_header("Remote Peering", 2)
            for rpc in rpcs:
                print(self.tabs + "RPC   Name   : " + rpc['name'])
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
                print(self.taba + "CPE    " + cpe)

        except Exception as e:
            self.__print_error("__print_core_network_cpe", e)

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
                    print(self.tabs + "Tunnel : " + t['ip_address'] + " - " + t['status'] + " - " + t['status_date'])
                print(self.tabs + "Routes : " + "\n    Routes : ".join(ips['routes']))
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
                if 'backend_set' in bs:
                    print(self.tabs + "backendSet : " + bs['backend_set'])
                if 'status' in bs:
                    print(self.tabs + self.tabs + "Status : " + bs['status'])

                # list of backends
                if 'backends' in bs:
                    for backend in bs['backends']:
                        print(self.tabs + self.tabs + "Backend: " + backend)
                if 'health_check' in bs:
                    for health in bs['health_check']:
                        print(self.tabs + self.tabs + "H.Chk  : " + health)

                if 'session_persistence' in bs:
                    if bs['session_persistence']:
                        print(self.tabs + self.tabs + "Cookie : " + bs['session_persistence'])

                if 'ssl_cert' in bs:
                    if bs['ssl_cert']:
                        print(self.tabs + self.tabs + "Cert   : " + bs['ssl_cert'])

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

            # ip_addresses
            if 'ips' in lb:
                for ip in lb['ips']:
                    print(self.tabs + "IP         : " + ip)

            # listeners
            if 'listeners' in lb:
                if not lb['listeners']:
                    print(self.tabs + "Listener   : None")
                for listener in lb['listeners']:
                    print(self.tabs + "Listener   : " + listener)

            # Path route set - need to test -  TBD
            if 'path_route' in lb:
                for prs in lb['path_route']:
                    print(self.tabs + "Path Route : " + prs['name'])
                    if 'path_routes' in prs:
                        for p in prs['path_routes']:
                            print(self.tabs + "           : Backend: " + str(p.backend_set_name) + ',  Path: ' + p.path)

            # Hostnames
            if 'hostnames' in lb:
                for hostname in lb['hostnames']:
                    print(self.tabs + "Hostname   : " + hostname)

        except Exception as e:
            self.__print_error("__print_load_balancer_details", e)

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

                if 'backendset' in load_balance_obj:
                    self.__print_load_balancer_backendset(load_balance_obj['backendset'])

                print("")

        except Exception as e:
            self.__print_error("__print_load_balancer_main", e)

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
    # print database db system
    ##########################################################################

    def __print_database_db_system_details(self, dbs):
        try:
            print(self.taba + dbs['name'])
            print(self.tabs + "AD      : " + dbs['availability_domain'])

            if 'cpu_core_count' in dbs:
                print(self.tabs + "Cores   : " + str(dbs['cpu_core_count']))

            if 'node_count' in dbs:
                if dbs['node_count']:
                    print(self.tabs + "Nodes   : " + str(dbs['node_count']))

            if 'version' in dbs:
                print(self.tabs + "Version : " + dbs['version'])

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
                    print(self.tabs + "Scan DNS: " + dbs['scan_dns'])

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
                    print(self.tabs + db_node)

                # db homes
                for db_home in dbs['db_homes']:
                    print(self.tabs + "Home    : " + db_home['home'])

                    # patches
                    for p in db_home['patches']:
                        print(self.tabs + self.tabs + " PT : " + p)

                    # databases
                    for db in db_home['databases']:
                        print(self.tabs + self.tabs + " DB : " + db['name'])

                        # print backups
                        for backup in db['backups']:
                            print(self.tabs + self.tabs + "      " + backup['name'] + " - " + backup['time'] + " - " + backup['size'])

        except Exception as e:
            self.__print_error("__print_database_db_system", e)

    ##########################################################################
    # print database db system
    ##########################################################################

    def __print_database_db_autonomous(self, dbs):
        try:
            for db in dbs:
                print(self.taba + db['name'])
                if 'cpu_core_count' in db:
                    print(self.tabs + "Cores   : " + str(db['cpu_core_count']))
                if 'data_storage_size_in_tbs' in db:
                    print(self.tabs + "Size TB : " + str(db['data_storage_size_in_tbs']))
                if 'db_name' in db:
                    print(self.tabs + "DB Name : " + db['db_name'])
                if 'time_created' in db:
                    print(self.tabs + "Created : " + db['time_created'])

                # print backups
                if db['backups']:
                    for backup in db['backups']:
                        print(self.tabs + self.tabs + "      " + backup['name'] + " - " + backup['time'])
                print("")

        except Exception as e:
            self.__print_error("__print_database_db_autonomous", e)

    ##########################################################################
    # database
    ##########################################################################

    def __print_database_main(self, list_databases):
        try:

            if len(list_databases) == 0:
                return

            if 'db_system' in list_databases:
                self.print_header("databases DB Systems", 2)
                self.__print_database_db_system(list_databases['db_system'])
                print("")

            if 'autonomous' in list_databases:
                self.print_header("Autonomous databases", 2)
                self.__print_database_db_autonomous(list_databases['autonomous'])
                print("")

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
                        print(self.tabs + str(job))

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

                if 'availability_domain' in instance and 'fault_domain' in instance:
                    print(self.tabs2 + "AD  : " + instance['availability_domain'] + " - " + instance['fault_domain'])

                if 'time_maintenance_reboot_due' in instance:
                    if instance['time_maintenance_reboot_due'] != "None":
                        print(self.tabs2 + "MRB : Maintenance Reboot Due " + instance['time_maintenance_reboot_due'])

                if 'image' in instance:
                    print(self.tabs2 + "Img : " + instance['image'])

                if 'boot_volume' in instance:
                    for bv in instance['boot_volume']:
                        print(self.tabs2 + "Boot: " + bv['desc'])

                if 'block_volume' in instance:
                    for bv in instance['block_volume']:
                        print(self.tabs2 + "Vol : " + bv['desc'])

                if 'vnic' in instance:
                    for vnic in instance['vnic']:
                        print(self.tabs2 + "VNIC: " + vnic['desc'])

                if 'console' in instance:
                    print(self.tabs2 + instance['console'])
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
    # print compute images
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
    # print compute boot volume
    ##########################################################################
    def __print_core_compute_boot_volume_backup(self, backups):

        try:
            if len(backups) == 0:
                return

            self.print_header("Boot Volume Backups", 2)
            prev_id = ""
            for backup in backups:
                if prev_id and prev_id != backup['boot_volume_id']:
                    print("")
                print(self.taba + backup['name'] + " - " + backup['desc'])
                print(self.tabs + self.tabs + "Type : " + backup['type'])
                print(self.tabs + self.tabs + "Size : " + backup['size'])
                prev_id = backup['boot_volume_id']

        except Exception as e:
            self.__print_error("__print_core_compute_boot_volume_backup", e)

    ##########################################################################
    # print compute block volume
    ##########################################################################
    def __print_core_compute_volume_backup(self, backups):

        try:
            if len(backups) == 0:
                return

            self.print_header("Block Volume Backups", 2)
            prev_id = ""
            for backup in backups:
                if prev_id and prev_id != backup['volume_id']:
                    print("")
                print(self.taba + backup['name'] + " - " + backup['desc'])
                print(self.tabs + self.tabs + "Type : " + backup['type'])
                print(self.tabs + self.tabs + "Size : " + backup['size'])
                prev_id = backup['volume_id']

        except Exception as e:
            self.__print_error("__print_core_compute_volume_backup", e)

    ##########################################################################
    # print compute block volume Groups
    ##########################################################################
    def __print_core_compute_volume_groups(self, volgroups):

        try:
            if len(volgroups) == 0:
                return

            self.print_header("Block Volume Groups", 2)
            for volgrp in volgroups:
                print(self.taba + volgrp['name'] + " - " + volgrp['size_in_gbs'] + "gb")
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

            if 'images' in data:
                self.__print_core_compute_images(data['images'])

            if 'boot_not_attached' in data:
                self.__print_core_compute_boot_vol_not_attached(data['boot_not_attached'])

            if 'volume_not_attached' in data:
                self.__print_core_compute_volume_not_attached(data['volume_not_attached'])

            if 'volume_group' in data:
                self.__print_core_compute_volume_groups(data['volume_group'])

            if 'boot_volume_backup' in data:
                self.__print_core_compute_boot_volume_backup(data['boot_volume_backup'])

            if 'volume_backup' in data:
                self.__print_core_compute_volume_backup(data['volume_backup'])

        except Exception as e:
            self.__print_error("__print_core_compute_main", e)

    ##########################################################################
    # Print Identity data
    ##########################################################################
    def __print_region_data(self, region_name, data):

        try:
            if not data:
                return
            self.print_header(region_name, 0)

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
                if 'email' in cdata:
                    self.__print_email_main(cdata['email'])
                if 'resource_management' in cdata:
                    self.__print_resource_management_main(cdata['resource_management'])

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

    summary_global_list = []
    summary_global_total = []

    ############################################
    # Init
    ############################################
    def __init__(self):
        pass

    ##########################################################################
    # print_main
    ##########################################################################
    def print_summary(self, data):

        try:

            for d in data:
                if 'type' in d:
                    if d['type'] == "region":
                        self.__summary_region_data(d['region'], d['data'])

            self.__summary_print_results(self.summary_global_total, "Summary Total", 0)

        except Exception as e:
            self.__print_error("print_summary", e)

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, msg, e):
        classname = type(self).__name__

        if isinstance(e, KeyError):
            print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + msg + ": " + str(e))

    ##########################################################################
    # Print header centered
    ##########################################################################
    def __summary_print_header(self, name, category):
        options = {0: 90, 1: 60, 2: 30, 3: 75}
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
    # print database autonumous
    ##########################################################################
    def __summary_database_db_autonomous(self, dbs):

        try:
            for db in dbs:
                if 'sum_info' in db and 'sum_count' in db:
                    self.summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_count'])})

                if 'sum_info_storage' in db and 'sum_size_tb' in db:
                    self.summary_global_list.append({'type': db['sum_info_storage'], 'size': float(db['sum_size_tb'])})

        except Exception as e:
            self.__print_error("__summary_database_db_autonomous", e)

    ##########################################################################
    # Database
    ##########################################################################

    def __summary_database_main(self, list_databases):
        try:

            if len(list_databases) == 0:
                return

            if 'db_system' in list_databases:
                self.__summary_database_db_system(list_databases['db_system'])

            if 'autonomous' in list_databases:
                self.__summary_database_db_autonomous(list_databases['autonomous'])

        except Exception as e:
            self.__print_error("__summary_database_main", e)

    ##########################################################################
    # Database db systems
    ##########################################################################
    def __summary_database_db_system(self, list_db_systems):

        try:
            nodes = 1
            for dbs in list_db_systems:
                if 'Exadata' not in dbs['sum_info']:
                    if 'node_count' in dbs:
                        if dbs['node_count'] is not None and dbs['node_count'] != 'None' and dbs['node_count'] != "":
                            nodes = dbs['node_count']

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
    # print self.__summary_core_compute_shape
    ##########################################################################
    def __summary_core_compute_instances(self, instances):

        try:
            if len(instances) == 0:
                return

            for instance in instances:
                self.summary_global_list.append({'type': (instance['sum_info'] + " - " + instance['sum_shape']), 'size': float(1)})

                if 'boot_volume' in instance:
                    self.__summary_core_size(instance['boot_volume'])

                if 'block_volume' in instance:
                    self.__summary_core_size(instance['block_volume'])

        except Exception as e:
            self.__print_error("__summary_core_compute_instances", e)

    ##########################################################################
    # print compute images
    ##########################################################################

    def __summary_core_size(self, objects):
        try:
            if len(objects) == 0:
                return

            for obj in objects:
                if 'sum_info' in obj and 'sum_size_gb' in obj:
                    if obj['sum_size_gb'] != '':
                        self.summary_global_list.append({'type': obj['sum_info'], 'size': float(obj['sum_size_gb'])})

        except Exception as e:
            self.__print_error("__summary_core_size", e)

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

            if 'boot_volume_backup' in data:
                self.__summary_core_size(data['boot_volume_backup'])

            if 'volume_backup' in data:
                self.__summary_core_size(data['volume_backup'])

            if 'boot_not_attached' in data:
                self.__summary_core_size(data['boot_not_attached'])

            if 'volume_not_attached' in data:
                self.__summary_core_size(data['volume_not_attached'])

        except Exception as e:
            self.__print_error("__summary_core_compute_main", e)

    ##########################################################################
    # Summary Group By
    # took the function frmo stackoverflow
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

                grouped_data = self.__summary_group_by("type", data)

                # add list to the total
                self.summary_global_total.extend(grouped_data)

                # sort and print
                for d in sorted(grouped_data, key=lambda i: i['type']):
                    print(d['type'].ljust(37) + " - " + str(round(d['size'])).rjust(10))

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

            # loop on compartments
            for cdata in data:
                self.summary_global_list = []

                compartment_header = ""
                if 'path' in cdata:
                    compartment_header = "Summary - Compartment " + cdata['path']

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

                # print results compartment
                self.__summary_print_results(self.summary_global_list, compartment_header, 3)

        except Exception as e:
            self.__print_error("__summary_region_data", e)
            raise
