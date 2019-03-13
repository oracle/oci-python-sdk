#!/usr/bin/env python3
##########################################################################
# Copyright(c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# showocy.py
#
# @Created On  : Jul 25 2018
# @Last Updated: Mar 12 2019
# @author      : Adi Zohar
# @Version     : 3.0.5
#
# Supports Python 2.7 and above, Python 3 recommended
#
# coding: utf-8
#
##########################################################################
# OCI Report Tool SHOWOCI:
#
# require OCI read only user with OCI authentication:
#    ALLOW GROUP ReadOnlyUsers to read all-resources IN TENANCY
#
# config file should contain:
#     [DEFAULT]
#     user =         user_ocid
#     fingerprint =  fingerprint of the api ssh key
#     key_file =     the path to the private key
#     tenancy =      tenancy ocid
#     region =       region
##########################################################################
#
# Modules Included:
#    identity , virtual_network, compute , block_storage, file_storage
#    object_storage, database, load_balancer, email  , KMS
#    resource_management
#
# Modules Not Yet Covered:
#    ContainerEngine
#    Monitoring
#    Notifications
#
##########################################################################
from __future__ import print_function
import oci
import datetime
import argparse
import sys
import json

##########################################################################
# config file and proxy
##########################################################################
version = "3.0.5"
config_file = "~/.oci/config"
oci_min_version = "2.2.1"
ocid = False
oci_installed_version = oci.version.__version__

##########################################################################
# spaces for align
##########################################################################
tabs = ' ' * 4
taba = '--> '

##########################################################################
# dot dict
##########################################################################


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


##########################################################################
# get flags
##########################################################################
def get_flags(cmd):
    flag = ""
    if cmd.all:
        flag += "all "
    if cmd.allnoiam:
        flag += "all_no_iam "
    if cmd.compute:
        flag += "compute "
    if cmd.database:
        flag += "database "
    if cmd.email:
        flag += "email "
    if cmd.file:
        flag += "file "
    if cmd.identity:
        flag += "identity "
    if cmd.load:
        flag += "load "
    if cmd.kms:
        flag += "kms "
    if cmd.network:
        flag += "network "
    if cmd.object:
        flag += "object "
    if cmd.proxy:
        flag += "proxy "
    if cmd.compart:
        flag += "compartment "
    if cmd.region:
        flag += "region "
    if cmd.ocid:
        flag += "ocid "
    if cmd.noroot:
        flag += "noroot "
    if cmd.mgdcompart:
        flag += "MgdCompartment "
    if cmd.sumonly:
        flag += "summary "
    if cmd.orm:
        flag += "ResManagment "
    return flag


##########################################################################
# get short license model
##########################################################################
def get_license_type(license_type):

    if license_type == "LICENSE_INCLUDED":
        return "INCL"
    elif license_type == "BRING_YOUR_OWN_LICENSE":
        return "BYOL"
    else:
        return license_type


##########################################################################
# Print header centered
##########################################################################
def print_header(name, category):
    options = {0: 90, 1: 60, 2: 30, 3: 75}
    chars = int(options[category])
    print("")
    print('#' * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print('#' * chars)


##########################################################################
# Print Tenancy
##########################################################################
def print_identity_tenancy(tenancy):
    try:

        print_header("Tenancy", 1)
        print("Name        : " + tenancy['name'])
        print("OCID        : " + tenancy['id'])
        print("Home Region : " + tenancy['home_region_key'])
        print("Subs Region : " + tenancy['subscribe_regions'])
        print("")

    except Exception as e:
        print("Error in print_identity_users: " + str(e.args))
        pass


##########################################################################
# Print Identity Users
##########################################################################
def print_identity_users(users):
    try:
        print_header("Users", 2)

        for user in users:
            print(taba + user['name'])
            print(tabs + "Keys   : " + user['parameters'])
            print(tabs + "Groups : " + user['groups'])
            print("")

    except Exception as e:
        print("Error in print_identity_users: " + str(e.args))
        pass


##########################################################################
# Print Identity Groups
##########################################################################
def print_identity_groups(groups):
    try:
        print_header("Groups", 2)

        for group in groups:
            print(taba + group['name'].ljust(18, " ") + " : " + group['users'])

    except Exception as e:
        print("Error in print_identity_groups: " + str(e.args))
        pass

##########################################################################
# Print Identity Policies
##########################################################################


def print_identity_policies(policies_data):
    try:
        if not policies_data:
            return

        print_header("Policies", 2)

        for c in policies_data:
            policies = c['policies']
            if not policies:
                continue

            print(c['compartment_path'] + ":")
            for policy in policies:
                print("")
                print(taba + policy['name'] + ":")
                print(tabs + "\n    ".join(policy['statements']))

    except Exception as e:
        print("Error in print_identity_policies: " + str(e.args))
        pass


##########################################################################
# Print Identity Providers
##########################################################################
def print_identity_providers(identity_providers):

    try:

        if not identity_providers:
            return

        print_header("identity providers", 2)

        for ip in identity_providers:
            print(taba + ip['name'])
            print(tabs + "Desc      : " + ip['description'])
            print(tabs + "Type      : " + ip['product_type'])
            print(tabs + "Protocol  : " + ip['protocol'])
            print(tabs + "Redirect  : " + ip['redirect_url'])
            print(tabs + "Metadata  : " + ip['metadata_url'])
            for ig in ip['group_map']:
                print(tabs + "Group Map : " + ig)
        print("")

    except Exception as e:
        print("Error in print_identity_providers: " + str(e.args))
        pass

##########################################################################
# Print Dynamic Groups
##########################################################################


def print_identity_dynamic_groups(dynamic_groups):
    try:
        if not dynamic_groups:
            return
        print_header("Dynamic Groups", 2)

        for dg in dynamic_groups:
            print(taba + dg['name'])
            print(tabs + "Desc      :" + dg['description'])
            print(tabs + "Rules     :" + dg['matching_rule'])
        print("")

    except Exception as e:
        print("Error in print_identity_dynamic_groups: " + str(e.args))
        pass


##########################################################################
# Identity Module
##########################################################################
def print_identity_main(data):
    try:
        if 'tenancy' in data:
            print_identity_tenancy(data['tenancy'])
        if 'users' in data:
            print_identity_users(data['users'])
        if 'groups' in data:
            print_identity_groups(data['groups'])
        if 'dynamic_groups' in data:
            print_identity_dynamic_groups(data['dynamic_groups'])
        if 'policies' in data:
            print_identity_policies(data['policies'])
        if 'providers' in data:
            print_identity_providers(data['providers'])

    except Exception as e:
        print("Error in print_identity_data: " + str(e.args))
        pass

##########################################################################
# return compartment name
##########################################################################


def print_core_network_vcn_compartment(vcn_compartment, data_compartment):
    if vcn_compartment == data_compartment:
        return ""
    val = "  (Compartment=" + data_compartment + ")"
    return val

##########################################################################
# Print Network VCN Local Peering
##########################################################################


def print_core_network_vcn_subnet(subnets, vcn_compartment, data_compartment):
    try:
        for subnet in subnets:
            print("")
            print(tabs + "Subnet " + subnet['subnet'] + print_core_network_vcn_compartment(vcn_compartment, data_compartment))
            print(tabs + tabs + "Name    : " + subnet['name'])
            print(tabs + tabs + "DNS     : " + subnet['dns'])
            print(tabs + tabs + "DHCP    : " + subnet['dhcp_options'])
            print(tabs + tabs + "Route   : " + subnet['route'])
            for s in subnet['security_list']:
                print(tabs + tabs + "Sec List: " + s)

    except Exception as e:
        print("Error in print_core_network_vcn_subnet: " + str(e.args))
        pass

##########################################################################
# get DHCP options for DHCP_ID
##########################################################################


def print_core_network_vcn_dhcp_options(dhcp_options, vcn_compartment, data_compartment):
    try:
        for dhcp in dhcp_options:
            print("")
            print(tabs + "DHCP Options: " + dhcp['name'] + print_core_network_vcn_compartment(vcn_compartment, data_compartment))

            for opt in dhcp['opt']:
                print(tabs + tabs + opt)

    except Exception as e:
        print("Error in print_core_network_vcn_dhcp_options: " + str(e.args))
        pass

##########################################################################
# Print Network vcn security list
##########################################################################


def print_core_network_vcn_security_lists(sec_lists, vcn_compartment, data_compartment):
    try:
        if not sec_lists:
            return
        for sl in sec_lists:
            print("")
            print(tabs + "Sec List    : " + str(sl['name']) + print_core_network_vcn_compartment(vcn_compartment, data_compartment))
            if len(sl['sec_rules']) == 0:
                print(tabs + "            : Empty.")

            for slr in sl['sec_rules']:
                print(tabs + tabs + slr)

    except Exception as e:
        print("Error in print_core_network_vcn_security_lists: " + str(e.args))
        pass


########################################################################
# Print Network vcn Route Tables
##########################################################################
def print_core_network_vcn_route_tables(route_tables, vcn_compartment, data_compartment):
    try:
        if not route_tables:
            return
        for rt in route_tables:
            print("")
            print(tabs + "Route Table : " + rt['name'] + print_core_network_vcn_compartment(vcn_compartment, data_compartment))
            if 'route_rules' not in rt:
                print(tabs + tabs + "Route   : Empty.")
                return
            if len(rt['route_rules']) == 0:
                print(tabs + tabs + "Route   : Empty.")
                return

            for rl in rt['route_rules']:
                print(tabs + tabs + "Route   : " + str(rl))

    except Exception as e:
        print("Error in print_core_network_vcn_route_tables: " + str(e.args))
        pass


##########################################################################
# print network vcn
##########################################################################
def print_core_network_vcn(vcns):

    try:
        if len(vcns) == 0:
            return

        print_header("VCNs", 2)
        for vcn in vcns:
            print(taba + "VCN    " + vcn['name'])
            vcn_compartment = vcn['compartment']

            if 'data' in vcn:
                for data in vcn['data']:
                    if 'igw' in data:
                        if data['igw'] != "":
                            print(tabs + "Internet GW : " + data['igw'] + print_core_network_vcn_compartment(vcn_compartment, data['compartment']))

                for data in vcn['data']:
                    if 'sgw' in data:
                        if data['sgw'] != "":
                            print(tabs + "Service GW  : " + data['sgw'] + print_core_network_vcn_compartment(vcn_compartment, data['compartment']))

                for data in vcn['data']:
                    if 'nat' in data:
                        if data['nat'] != "":
                            print(tabs + "NAT GW      : " + data['nat'] + print_core_network_vcn_compartment(vcn_compartment, data['compartment']))

                for data in vcn['data']:
                    if 'drg_attached' in data:
                        if data['drg_attached'] != "":
                            print(tabs + "DRG Attached: " + data['drg_attached'] + print_core_network_vcn_compartment(vcn_compartment, data['compartment']))

                for data in vcn['data']:
                    if 'local_peering' in data:
                        for lpeer in data['local_peering']:
                            print(tabs + "Local Peer  : " + lpeer + print_core_network_vcn_compartment(vcn_compartment, data['compartment']))

                for data in vcn['data']:
                    if 'subnets' in data:
                        print_core_network_vcn_subnet(data['subnets'], vcn_compartment, data['compartment'])

                for data in vcn['data']:
                    if 'security_lists' in data:
                        print_core_network_vcn_security_lists(data['security_lists'], vcn_compartment, data['compartment'])

                for data in vcn['data']:
                    if 'route_tables' in data:
                        print_core_network_vcn_route_tables(data['route_tables'], vcn_compartment, data['compartment'])

                for data in vcn['data']:
                    if 'dhcp_options' in data:
                        print_core_network_vcn_dhcp_options(data['dhcp_options'], vcn_compartment, data['compartment'])

                    print("")

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except BaseException as e:
        print("Error in print_core_network_vcn: " + str(e.args))
        pass


##########################################################################
# print network drg
##########################################################################
def print_core_network_drg(drgs):

    try:
        if len(drgs) == 0:
            return

        print_header("DRGs", 2)
        for drg in drgs:
            print(taba + "DRG    " + drg)

    except Exception as e:
        print("Error in print_core_network_vcn: " + str(e.args))
        pass

##########################################################################
# print network remote peering
##########################################################################


def print_core_network_remote_peering(rpcs):

    try:
        if len(rpcs) == 0:
            return

        print_header("Remote Peering", 2)
        for rpc in rpcs:
            print(taba + "RPC    Id    : " + rpc['id'])
            print(tabs + "       PeerId: " + rpc['peer_id'])
            print(tabs + "       Name  : " + rpc['name'])
            print(tabs + "       DRG   : " + rpc['drg'])
            print(tabs + "       Status: " + rpc['peering_status'])
            print(tabs + "       Region: " + rpc['peer_region_name'])
            if (rpc['is_cross_tenancy_peering'] == "True"):
                print(tabs + "       Tenant: " + rpc['peer_tenancy_id'])

    except Exception as e:
        print("Error in print_core_network_vcn: " + str(e.args))
        pass
##########################################################################
# print network cpe
##########################################################################


def print_core_network_cpe(cpes):

    try:

        if len(cpes) == 0:
            return

        print_header("CPEs", 2)
        for cpe in cpes:
            print(taba + "CPE    " + cpe)

    except Exception as e:
        print("Error in print_core_network_cpe: " + str(e.args))
        pass

##########################################################################
# print network ipsec
##########################################################################


def print_core_network_ipsec(ipsecs):

    try:
        if len(ipsecs) == 0:
            return

        print_header("IPSec", 2)
        for ips in ipsecs:

            print(taba + "IPSEC  : " + ips['name'])
            print(tabs + "DRG    : " + ips['drg'])
            print(tabs + "CPE    : " + ips['cpe'])
            # get tunnel status
            for t in ips['tunnels']:
                print(tabs + "Tunnel : " + t['ip_address'] + " - " + t['status'] + " - " + t['status_date'])
            print(tabs + "Routes : " + "\n    Routes : ".join(ips['routes']))
            print("")

    except Exception as e:
        print("Error in print_core_network_ipsec: " + str(e.args))
        pass

##########################################################################
# print virtual cirtuicts
##########################################################################


def print_core_network_virtual_circuit(virtual_circuit):

    try:
        if len(virtual_circuit) == 0:
            return

        print_header("Virtual Circuits (FC)", 2)
        for vc in virtual_circuit:

            print(taba + "VC      : " + vc['name'] + " - " + vc['bandwidth_shape_name'] + " - " + vc['lifecycle_state'])
            print(tabs + "DRG     : " + vc['drg'])
            print(tabs + "BGP     : " + vc['bgp_management'] + " - " + vc['bgp_session_state'] + " - Cust ASN:" + vc['customer_bgp_asn'] + " - Ora ASN:" + vc['oracle_bgp_asn'])
            print(tabs + "PROVIDER: " + vc['provider_name'] + " - " + vc['provider_service_name'] + " - " + vc['provider_state'] + " - " + vc['service_type'])
            # get tunnel status
            for t in vc['cross_connect_mappings']:
                print(tabs + "CCMAP  : Cust : " + str(t['customer_bgp_peering_ip']) + " - Ora : " + str(t['oracle_bgp_peering_ip']) + " - VLAN " + str(t['vlan']))
            print("")

    except Exception as e:
        print("Error in print_core_network_virtual_circuit: " + str(e.args))
        pass


##########################################################################
# print network Main
##########################################################################
def print_core_network_main(data):
    try:
        if 'vcn' in data:
            print_core_network_vcn(data['vcn'])
        if 'drg' in data:
            print_core_network_drg(data['drg'])
        if 'cpe' in data:
            print_core_network_cpe(data['cpe'])
        if 'ipsec' in data:
            print_core_network_ipsec(data['ipsec'])
        if 'remote_peering' in data:
            print_core_network_remote_peering(data['remote_peering'])
        if 'virtual_circuit' in data:
            print_core_network_virtual_circuit(data['virtual_circuit'])

    except Exception as e:
        print("Error in print_core_network: " + str(e.args))
        pass


##########################################################################
# print load balancer backedset
##########################################################################
def print_load_balancer_backendset(backendset):

    try:
        for bs in backendset:
            print("")
            if 'backend_set' in bs:
                print(tabs + "backendSet : " + bs['backend_set'])
            if 'status' in bs:
                print(tabs + tabs + "Status : " + bs['status'])

            # list of backends
            if 'backends' in bs:
                for backend in bs['backends']:
                    print(tabs + tabs + "Backend: " + backend)
            if 'health_check' in bs:
                for health in bs['health_check']:
                    print(tabs + tabs + "H.Chk  : " + health)

            if 'session_persistence' in bs:
                print(tabs + tabs + "Cookie : " + bs['session_persistence'])

            if 'ssl_cert' in bs:
                print(tabs + tabs + "Cookie : " + bs['ssl_cert'])

    except Exception as e:
        print("Error in print_load_balancer_backendset: " + str(e.args))
        pass


##########################################################################
# print load balancer config
##########################################################################
def print_load_balancer_details(load_balance_obj):
    try:
        lb = load_balance_obj
        print(taba + "Name       : " + lb['name'])
        print(tabs + "Status     : " + lb['status'])

        # subnets
        if 'subnets' in lb:
            for subnet in lb['subnets']:
                print(tabs + "Subnet     : " + subnet)

        # ip_addresses
        if 'ips' in lb:
            for ip in lb['ips']:
                print(tabs + "IP         : " + ip)

        # listeners
        if 'listeners' in lb:
            if not lb['listeners']:
                print(tabs + "Listener   : None")
            for listener in lb['listeners']:
                print(tabs + "Listener   : " + listener)

        # Path route set - need to test -  TBD
        if 'path_route' in lb:
            for prs in lb['path_route']:
                print(tabs + "Path Route : " + prs['name'])
                if 'path_routes' in prs:
                    for p in prs['path_routes']:
                        print(tabs + "           : Backend: " + str(p.backend_set_name) + ',  Path: ' + p.path)

        # Hostnames
        if 'hostnames' in lb:
            for hostname in lb['hostnames']:
                print(tabs + "Hostname   : " + hostname)

    except Exception as e:
        print("Error in print_load_balancer_details: " + str(e.args))
        pass


##########################################################################
# Load Balancer
##########################################################################
def print_load_balancer_main(load_balancers):
    try:

        if len(load_balancers) == 0:
            return
        print_header("Load Balancers", 2)

        for load_balance_obj in load_balancers:
            if 'details' in load_balance_obj:
                print_load_balancer_details(load_balance_obj['details'])

            if 'backendset' in load_balance_obj:
                print_load_balancer_backendset(load_balance_obj['backendset'])

            print("")

    except Exception as e:
        print("Error in print_load_balancer_main: " + str(e.args))
        pass


##########################################################################
# print file systems mount targets
##########################################################################
def print_file_storage_mount_target(mount_targets):

    try:
        for mt in mount_targets:
            print(tabs + "Mount     : " + mt['mount'])

            for ip in mt['ips']:
                print(tabs + "Mount IP  : " + ip)

    except Exception as e:
        print("Error in print_file_storage_mount_target: " + str(e.args))
        pass

##########################################################################
# print file systems exports
##########################################################################


def print_file_storage_exports(exports):

    try:
        for export in exports:
            if 'path' in export:
                print(tabs + "Export    : " + export['path'])
            if 'exportset' in export:
                print(tabs + "ExportSet : " + export['exportset'])

            # Mount Target
            print_file_storage_mount_target(export['mount_targeet'])

    except Exception as e:
        print("Error in print_file_storage_exports: " + str(e.args))
        pass


##########################################################################
# File System
##########################################################################
def print_file_storage_main(file_systems):
    try:

        if len(file_systems) == 0:
            return
        print_header("File Storage", 2)

        # print details
        for fs in file_systems:
            if 'filesystem' in fs:
                print(taba + fs['filesystem'])
            print_file_storage_exports(fs['exports'])

            # snapshots
            if 'snapshots' in fs:
                for snap in fs['snapshots']:
                    print(tabs + "Snap  : " + snap)

            print("")

    except Exception as e:
        print("Error in print_file_storage_main: " + str(e.args))
        pass

##########################################################################
# File System
##########################################################################


def print_kms_vault_main(kms_vaults):
    try:

        if len(kms_vaults) == 0:
            return
        print_header("KMS", 2)

        # print details
        for vault in kms_vaults:
            if 'vault' in vault:
                print(taba + vault['vault'])

            # keys
            if 'keys' in vault:
                for key in vault['keys']:
                    print(tabs + "Key  : " + key)

            print("")

    except Exception as e:
        print("Error in print_kms_vault_main: " + str(e.args))
        pass

##########################################################################
# print database db system
##########################################################################


def print_database_db_system_details(dbs):
    try:
        print(taba + dbs['name'])
        print(tabs + "AD      : " + dbs['availability_domain'])
        if 'cpu_core_count' in dbs:
            print(tabs + "Cores   : " + str(dbs['cpu_core_count']))
        if 'node_count' in dbs:
            print(tabs + "Nodes   : " + str(dbs['node_count']))
        if 'version' in dbs:
            print(tabs + "Version : " + dbs['version'])
        if 'host' in dbs:
            print(tabs + "Host    : " + dbs['host'])
        if 'domain' in dbs:
            print(tabs + "Domain  : " + dbs['domain'])
        if 'cluster_name' in dbs:
            print(tabs + "Cluster : " + dbs['cluster_name'])
        if 'data' in dbs:
            print(tabs + "Data    : " + dbs['data'])
        if 'data_subnet' in dbs:
            print(tabs + "DataSub : " + dbs['data_subnet'])
        if 'backup_subnet' in dbs:
            print(tabs + "BackSub : " + dbs['backup_subnet'])
        if 'scan_dns' in dbs:
            print(tabs + "Scan DNS: " + dbs['scan_dns'])
        if 'scan_ips' in dbs:
            for ip in dbs['scan_ips']:
                print(tabs + "Scan Ips: " + ip)
        if 'vip_ips' in dbs:
            for ip in dbs['vip_ips']:
                print(tabs + "VIP Ips : " + ip)
        if 'listener_port' in dbs:
            print(tabs + "Port    : " + dbs['listener_port'])
        if 'patches' in dbs:
            for p in dbs['patches']:
                print(tabs + "Patches : " + p)

    except Exception as e:
        print("Error in print_database_db_system: " + str(e.args))
        pass

##########################################################################
# Database db systems
##########################################################################


def print_database_db_system(list_db_systems):

    try:
        for dbs in list_db_systems:
            print("")

            # db systems
            print_database_db_system_details(dbs)

            # db nodes
            for db_node in dbs['db_nodes']:
                print(tabs + db_node)

            # db homes
            for db_home in dbs['db_homes']:
                print(tabs + "Home    : " + db_home['home'])

                # patches
                for p in db_home['patches']:
                    print(tabs + tabs + " PT : " + p)

                # databases
                for db in db_home['databases']:
                    print(tabs + tabs + " DB : " + db['name'])

                    # print backups
                    for backup in db['backups']:
                        print(tabs + tabs + tabs + "      " + backup['name'] + " - " + backup['time'] + " - " + backup['size'])

    except Exception as e:
        print("Error in print_database_db_system: " + str(e.args))
        pass

##########################################################################
# print database db system
##########################################################################


def print_database_db_autonomous(dbs):
    try:
        for db in dbs:
            print(taba + db['name'])
            if 'cpu_core_count' in db:
                print(tabs + "Cores   : " + str(db['cpu_core_count']))
            if 'data_storage_size_in_tbs' in db:
                print(tabs + "Size TB : " + str(db['data_storage_size_in_tbs']))
            if 'db_name' in db:
                print(tabs + "DB Name : " + db['db_name'])
            if 'time_created' in db:
                print(tabs + "Created : " + db['time_created'])

    except Exception as e:
        print("Error in print_database_db_autonomous: " + str(e.args))
        pass
##########################################################################
# Database
##########################################################################


def print_database_main(list_databases):
    try:

        if len(list_databases) == 0:
            return

        if 'db_system' in list_databases:
            print_header("Databases DB Systems", 2)
            print_database_db_system(list_databases['db_system'])
            print("")

        if 'adwc' in list_databases:
            print_header("Autonomous DW", 2)
            print_database_db_autonomous(list_databases['adwc'])
            print("")

        if 'atp' in list_databases:
            print_header("Autonomous Database", 2)
            print_database_db_autonomous(list_databases['atp'])
            print("")

    except Exception as e:
        print("Error in print_database_main: " + str(e.args))
        pass

##########################################################################
# object storage
##########################################################################


def print_object_storage_main(objects):

    try:
        if len(objects) == 0:
            return
        print_header("Object Storage", 2)

        for obj in objects:
            print(taba + obj['desc'])

    except Exception as e:
        print("Error in print_object_storage_main: " + str(e.args))
        pass

##########################################################################
# Email
##########################################################################


def print_email_main(emails):

    try:
        if 'senders' not in emails and 'supp_list' not in emails:
            return

        print_header("EMails", 2)

        if 'senders' in emails:
            print(taba + "Approved Senders:")
            for val in emails['senders']:
                print(tabs + str(val))
            print("")

        if 'supp_list' in emails:
            print(taba + "Suppression List:")
            for val in emails['supp_list']:
                print(tabs + str(val))

    except Exception as e:
        print("Error in print_email_main: " + str(e.args))
        pass

##########################################################################
# resource Management
##########################################################################


def print_resource_management_main(resource_management):

    try:
        if len(resource_management) == 0:
            return

        print_header("Resource Management", 2)

        for val in resource_management:
            print(taba + str(val['stack_name']))
            if 'jobs' in val:
                for job in val['jobs']:
                    print(tabs + str(job))

            print("")

    except Exception as e:
        print("Error in print_resource_management_main: " + str(e.args))
        pass

##########################################################################
# print compute instances
##########################################################################


def print_core_compute_instances(instances):

    try:

        if len(instances) == 0:
            return

        print_header("Compute Instances", 2)
        for instance in instances:
            if 'name' in instance:
                print(taba + instance['name'])
            if 'availability_domain' in instance:
                print(tabs + "AD  : " + instance['availability_domain'])
            if 'fault_domain' in instance:
                print(tabs + "FD  : " + instance['fault_domain'])
            if 'time_maintenance_reboot_due' in instance:
                print(tabs + "MRB : Maintenance Reboot Due " + instance['time_maintenance_reboot_due'])

            if 'image' in instance:
                print(tabs + "Img : " + instance['image'])
            if 'boot_volume' in instance:
                for bv in instance['boot_volume']:
                    print(tabs + "Boot: " + bv['desc'])
            if 'block_volume' in instance:
                for bv in instance['block_volume']:
                    print(tabs + "Vol : " + bv['desc'])
            if 'vnic' in instance:
                for vnic in instance['vnic']:
                    print(tabs + "VNIC: " + vnic['desc'])
            if 'console' in instance:
                print(tabs + instance['console'])

            print("")
    except Exception as e:
        print("Error in print_core_compute_instances: " + str(e.args))
        pass


##########################################################################
# print compute images
##########################################################################
def print_core_compute_images(images):

    try:
        if len(images) == 0:
            return

        print_header("Compute Custom Images", 2)
        for image in images:
            print(taba + image['desc'])

    except Exception as e:
        print("Error in print_core_compute_images: " + str(e.args))
        pass

##########################################################################
# print compute images
##########################################################################


def print_core_compute_instance_pool(pools):

    try:
        if len(pools) == 0:
            return

        print_header("Compute Instance Pool", 2)
        for pool in pools:
            print(pool['name'])

    except Exception as e:
        print("Error in print_core_compute_instance_pool: " + str(e.args))
        pass

##########################################################################
# print compute images
##########################################################################


def print_core_compute_instance_configuration(configs):

    try:
        if len(configs) == 0:
            return

        print_header("Compute Inst Configuration", 2)
        for config in configs:
            print(config['name'])

    except Exception as e:
        print("Error in print_core_compute_instance_configuration: " + str(e.args))
        pass

##########################################################################
# print compute boot volume
##########################################################################


def print_core_compute_boot_volume_backup(backups):

    try:
        if len(backups) == 0:
            return

        print_header("Boot Volume Backups", 2)
        prev_id = ""
        for backup in backups:
            if prev_id and prev_id != backup['boot_volume_id']:
                print("")
            print(taba + backup['name'])
            print(tabs + tabs + "Name : " + backup['desc'])
            print(tabs + tabs + "Size : " + backup['size'])
            prev_id = backup['boot_volume_id']

    except Exception as e:
        print("Error in print_core_compute_boot_volume_backup: " + str(e.args))
        pass

##########################################################################
# print compute block volume
##########################################################################


def print_core_compute_volume_backup(backups):

    try:
        if len(backups) == 0:
            return

        print_header("Block Volume Backups", 2)
        prev_id = ""
        for backup in backups:
            if prev_id and prev_id != backup['volume_id']:
                print("")
            print(taba + backup['name'])
            print(tabs + tabs + "Name : " + backup['desc'])
            print(tabs + tabs + "Size : " + backup['size'])
            prev_id = backup['volume_id']

    except Exception as e:
        print("Error in print_core_compute_boot_volume_backup: " + str(e.args))
        pass

##########################################################################
# print Compute
##########################################################################


def print_core_compute_main(data):

    try:
        if len(data) == 0:
            return

        if 'instances' in data:
            print_core_compute_instances(data['instances'])

        if 'instance_configuration' in data:
            print_core_compute_instance_configuration(data['instance_configuration'])

        if 'instance_pool' in data:
            print_core_compute_instance_pool(data['instance_pool'])

        if 'images' in data:
            print_core_compute_images(data['images'])

        if 'boot_volume_backup' in data:
            print_core_compute_boot_volume_backup(data['boot_volume_backup'])

        if 'volume_backup' in data:
            print_core_compute_volume_backup(data['volume_backup'])

    except Exception as e:
        print("Error in print_compute_main: " + str(e.args))
        pass


##########################################################################
# Print Identity data
##########################################################################
def print_region_data(region_name, data):

    try:
        if not data:
            return
        print_header(region_name, 0)

        for cdata in data:
            if 'path' in cdata:
                print_header("Compartment " + cdata['path'], 1)
            if 'network' in cdata:
                print_core_network_main(cdata['network'])
            if 'compute' in cdata:
                print_core_compute_main(cdata['compute'])
            if 'database' in cdata:
                print_database_main(cdata['database'])
            if 'kms' in cdata:
                print_kms_vault_main(cdata['kms'])
            if 'object_storage' in cdata:
                print_object_storage_main(cdata['object_storage'])
            if 'file_storage' in cdata:
                print_file_storage_main(cdata['file_storage'])
            if 'load_balancer' in cdata:
                print_load_balancer_main(cdata['load_balancer'])
            if 'email' in cdata:
                print_email_main(cdata['email'])
            if 'resource_management' in cdata:
                print_resource_management_main(cdata['resource_management'])

    except Exception as e:
        raise Exception("Error in print_region_data: " + str(e.args))


##########################################################################
# Print showoci data
##########################################################################
def print_showoci_data(data):
    try:
        print_header(data['program'], 1)
        print("Config File    : " + data['config_file'])
        print("Config Profile : " + data['config_profile'])
        print("Version        : " + data['version'])
        print("Date/Time      : " + data['datetime'])
        print("Flags          : " + data['flags'])
        print("OCI SDK Ver    : " + data['oci_sdk_version'])
        if 'proxy' in data:
            print("Proxy         : " + data['proxy'])
        if 'joutfile' in data:
            print("JSON Out      : " + data['joutfile'])

        print("")

    except Exception as e:
        raise Exception("Error in print_showoci_data: " + str(e.args))

##########################################################################
# print_oci_main
##########################################################################


def print_oci_main(jsondata, print_version):
    try:
        for d in jsondata:
            if 'type' in d:
                if d['type'] == "showoci":
                    if print_version:
                        print_showoci_data(d['data'])
                elif d['type'] == "identity":
                    print_identity_main(d['data'])
                elif d['type'] == "region":
                    print_region_data(d['region'], d['data'])
                else:
                    print("Error Unknown Type in JSON file...")

    except Exception as e:
        raise Exception("Error in print_oci_main: " + str(e.args))

##########################################################################
# Load Balancer
##########################################################################


def summary_load_balancer_main(load_balancers):
    try:

        if len(load_balancers) == 0:
            return

        for load_balance_obj in load_balancers:
            if 'sum_info' in load_balance_obj:
                summary_global_list.append({'type': load_balance_obj['sum_info'], 'size': 1})

    except Exception as e:
        print("Error in summary_load_balancer_main: " + str(e.args))
        pass

##########################################################################
# File System
##########################################################################


def summary_file_storage_main(file_systems):
    try:

        if len(file_systems) == 0:
            return

        summary_core_size(file_systems)

    except Exception as e:
        print("Error in summary_file_storage_main: " + str(e.args))
        pass

##########################################################################
# object storage
##########################################################################


def summary_object_storage_main(objects):

    try:
        if len(objects) == 0:
            return

        summary_core_size(objects)

    except Exception as e:
        print("Error in summary_object_storage_main: " + str(e.args))
        pass

##########################################################################
# print database autonumous
##########################################################################


def summary_database_db_autonomous(dbs):
    try:
        for db in dbs:
            if 'sum_info' in db and 'sum_count' in db:
                summary_global_list.append({'type': db['sum_info'], 'size': float(db['sum_count'])})

            if 'sum_info_storage' in db and 'sum_size_tb' in db:
                summary_global_list.append({'type': db['sum_info_storage'], 'size': float(db['sum_size_tb'])})

    except Exception as e:
        print("Error in summary_database_db_autonomous: " + str(e.args))
        pass

##########################################################################
# Database
##########################################################################


def summary_database_main(list_databases):
    try:

        if len(list_databases) == 0:
            return

        if 'db_system' in list_databases:
            summary_database_db_system(list_databases['db_system'])

        if 'adwc' in list_databases:
            summary_database_db_autonomous(list_databases['adwc'])

        if 'atp' in list_databases:
            summary_database_db_autonomous(list_databases['atp'])

    except Exception as e:
        print("Error in summary_database_main: " + str(e.args))
        pass
##########################################################################
# Database db systems
##########################################################################


def summary_database_db_system(list_db_systems):

    try:
        nodes = 1
        for dbs in list_db_systems:
            if 'node_count' in dbs:
                if dbs['node_count'] is not None and dbs['node_count'] != 'None':
                    nodes = dbs['node_count']

            summary_global_list.append({'type': dbs['sum_info'], 'size': float(nodes)})

            if dbs['sum_size_gb'] is not None:
                if dbs['sum_size_gb'] != 'None':
                    summary_global_list.append({'type': dbs['sum_info_storage'], 'size': float(dbs['sum_size_gb'])})

            # db homes
            for db_home in dbs['db_homes']:
                for db in db_home['databases']:
                    summary_core_size(db['backups'])

    except Exception as e:
        print("Error in summary_database_db_system: " + str(e.args))
        pass

##########################################################################
# print summary_core_compute_shape
##########################################################################


def summary_core_compute_instances(instances):

    try:
        if len(instances) == 0:
            return

        for instance in instances:
            summary_global_list.append({'type': (instance['sum_info'] + " - " + instance['sum_shape']), 'size': float(1)})

            if 'boot_volume' in instance:
                summary_core_size(instance['boot_volume'])

            if 'block_volume' in instance:
                summary_core_size(instance['block_volume'])

    except Exception as e:
        print("Error in summary_core_compute_instances: " + str(e.args))
        pass


##########################################################################
# print compute images
##########################################################################
def summary_core_size(objects):

    try:
        if len(objects) == 0:
            return

        for obj in objects:
            if 'sum_info' in obj and 'sum_size_gb' in obj:
                if obj['sum_size_gb'] != '':
                    summary_global_list.append({'type': obj['sum_info'], 'size': float(obj['sum_size_gb'])})

    except Exception as e:
        print("Error in summary_core_compute_size: " + str(e.args))
        pass


##########################################################################
# summary Compute
##########################################################################
def summary_core_compute_main(data):

    try:
        if len(data) == 0:
            return

        if 'instances' in data:
            summary_core_compute_instances(data['instances'])

        if 'images' in data:
            summary_core_size(data['images'])

        if 'boot_volume_backup' in data:
            summary_core_size(data['boot_volume_backup'])

        if 'volume_backup' in data:
            summary_core_size(data['volume_backup'])

    except Exception as e:
        print("Error in summary_core_compute_main: " + str(e.args))
        pass

##########################################################################
# Summary Group By
# took the function frmo stackoverflow
##########################################################################


def summery_group_by(key, list_of_dicts):
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

##########################################################################
# Print summary  data
##########################################################################


def summary_print_results(data, header, header_size):

    if len(data) > 0:
        print_header(header, header_size)

        grouped_data = summery_group_by("type", data)

        # add list to the total
        summary_global_total.extend(grouped_data)

        # sort and print
        for d in sorted(grouped_data, key=lambda i: i['type']):
            print(d['type'].ljust(37) + " - " + str(round(d['size'])).rjust(10))

##########################################################################
# Print summary Identity data
##########################################################################


def summary_region_data(region_name, data):

    global summary_global_list

    try:
        if not data:
            return
        print_header("Summary - " + region_name, 0)

        # loop on compartments
        for cdata in data:
            summary_global_list = []

            compartment_header = ""
            if 'path' in cdata:
                compartment_header = "Summary - Compartment " + cdata['path']

            if 'compute' in cdata:
                summary_core_compute_main(cdata['compute'])
            if 'database' in cdata:
                summary_database_main(cdata['database'])
            if 'object_storage' in cdata:
                summary_object_storage_main(cdata['object_storage'])
            if 'file_storage' in cdata:
                summary_file_storage_main(cdata['file_storage'])
            if 'load_balancer' in cdata:
                summary_load_balancer_main(cdata['load_balancer'])

            # print results compartment
            summary_print_results(summary_global_list, compartment_header, 3)

    except Exception as e:
        raise Exception("Error in summary_region_data: " + str(e.args))

##########################################################################
# print_oci_main
##########################################################################


def summary_oci_main(jsondata, print_version):

    global summary_global_total
    summary_global_total = []

    try:

        for d in jsondata:
            if 'type' in d:
                if d['type'] == "region":
                    summary_region_data(d['region'], d['data'])

        summary_print_results(summary_global_total, "Summary Total", 0)

    except Exception as e:
        raise Exception("Error in summary_oci_main: " + str(e.args))

##########################################################################
# Print version
##########################################################################


def get_version(cmd):

    data = {
        'program': "showoci.py",
        'author': "Adi Zohar",
        'config_file': config_file,
        'config_profile': config_section,
        'version': version,
        'datetime': str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
        'flags': get_flags(cmd),
        'oci_sdk_version': oci_installed_version
    }
    if cmd.proxy:
        data['proxy'] = str(cmd.proxy)
    if cmd.joutfile:
        data['joutfile'] = str(cmd.joutfile)

    main_data = {}
    main_data['type'] = "showoci"
    main_data['data'] = data

    return main_data

##########################################################################
# Return nested compartments list
##########################################################################


##########################################################################
# Return compartments with root compartment
##########################################################################
def get_compartments_with_root(identity, tenancy, cmd):
    try:
        compartments = []

        # Build Compartments
        def build_compartments_nested(identity, cid, path):
            try:
                clists = oci.pagination.list_call_get_all_results(identity.list_compartments, cid).data

                if path != "":
                    path = path + " / "
                for c in clists:
                    if c.lifecycle_state == 'ACTIVE':
                        value = {}
                        value['id'] = str(c.id)
                        value['name'] = str(c.name)
                        value['path'] = path + str(c.name)
                        compartments.append(dotdict(value))
                        build_compartments_nested(identity, c.id, value['path'])

            except oci.exceptions.RequestException:
                raise
            except oci.exceptions.ServiceError:
                raise
            except Exception as e:
                raise Exception("Error in build_compartments_nested: " + str(e.args))

        # Add root compartment
        if not(cmd.noroot):
            value = {}
            value['id'] = str(tenancy.id)
            value['name'] = str(tenancy.name) + " (root)"
            value['path'] = value['name']
            compartments.append(dotdict(value))

        # Build the compartments
        build_compartments_nested(identity, tenancy.id, "")

        # if not filtered by compartment return
        if not cmd.compart:
            return compartments

        # Filtered by compartment
        print("    Filtered by Compartment=" + str(cmd.compart))

        # if filter by compartment, then reduce list
        c_compart = []
        for x in compartments:
            if cmd.compart in x.name:
                c_compart.append(x)
        return c_compart

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        raise Exception("Error in get_compartments_with_root:identity.list_compartments: " + str(e.args))

##########################################################################
# Get Tenancy
##########################################################################


def get_identity_tenancy(identity, tenancy):
    print("    Tenancy...")
    try:
        sub_regions = identity.list_region_subscriptions(tenancy.id).data

        data = {
            'name': tenancy.name,
            'id': tenancy.id,
            'home_region_key': tenancy.home_region_key,
            'subscribe_regions': ', '.join(x.region_name for x in sub_regions)
        }
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        raise Exception("Error in get_identity_tenancy: " + str(e.args))


##########################################################################
# Get Identity Users
##########################################################################
def get_identity_users(identity, tenancy):
    print("    Users...")
    try:
        users = oci.pagination.list_call_get_all_results(identity.list_users, tenancy.id).data
        groups = oci.pagination.list_call_get_all_results(identity.list_groups, tenancy.id).data
        data = []

        for user in users:
            user_group_memberships = oci.pagination.list_call_get_all_results(identity.list_user_group_memberships, tenancy.id, user_id=user.id).data

            group_users = []
            for ugm in user_group_memberships:
                group_users.append(next(item for item in groups if item.id == ugm.group_id).name)

            data.append({
                'name': user.name,
                'parameters':
                    "API = " + str(len(identity.list_api_keys(user.id).data)) +
                    "  Tokens = " + str(len(identity.list_auth_tokens(user.id).data)) +
                    "  Secret = " + str(len(identity.list_customer_secret_keys(user.id).data)) +
                    "  Swift = " + str(len(identity.list_swift_passwords(user.id).data)) +
                    "  SMTP  = " + str(len(identity.list_smtp_credentials(user.id).data)),
                'groups': ', '.join(x for x in group_users)
            })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_identity_users: " + str(e.args))
        pass

##########################################################################
# Print Identity Groups
##########################################################################


def get_identity_groups(identity, tenancy):
    print("    Groups...")
    try:
        users = identity.list_users(tenancy.id).data
        groups = identity.list_groups(tenancy.id).data
        data = []

        for group in groups:
            user_group_memberships = oci.pagination.list_call_get_all_results(identity.list_user_group_memberships, tenancy.id, group_id=group.id).data
            group_users = []
            for ugm in user_group_memberships:
                for item in users:
                    if item.id == ugm.user_id:
                        group_users.append(item.name)
            if len(group_users) > 0:
                data.append({'name': group.name, 'users': ', '.join(x for x in group_users)})
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_identity_groups: " + str(e.args))
        pass

##########################################################################
# Print Identity Policies
##########################################################################


def get_identity_policies(identity, tenancy, handle_managed_compartment, cmd):
    print("    Policies...")
    try:
        compartments = get_compartments_with_root(identity, tenancy, cmd)
        data = []

        for c in compartments:
            if c.name == "ManagedCompartmentForPaaS" and not handle_managed_compartment:
                continue

            policies = identity.list_policies(c.id).data

            if len(policies) > 0:
                dataval = {}
                datapol = []
                for policy in policies:
                    datapol.append({'name': policy.name, 'statements': policy.statements})
                dataval['compartment_name'] = "Compartment " + c.name
                dataval['compartment_path'] = "Compartment " + c.path
                dataval['policies'] = datapol
                data.append(dataval)

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_identity_policies: " + str(e.args))
        pass


##########################################################################
# Print Identity Providers
##########################################################################
def get_identity_providers(identity, tenancy):
    print("    Providers...")

    try:
        groups = oci.pagination.list_call_get_all_results(identity.list_groups, tenancy.id).data
        identity_providers = identity.list_identity_providers("SAML2", tenancy.id).data

        data = []

        for d in identity_providers:
            igm = oci.pagination.list_call_get_all_results(identity.list_idp_group_mappings, d.id).data

            # get the group data
            groupdata = []
            for ig in igm:
                groupdata.append(ig.idp_group_name + " <-> " + next(item for item in groups if item.id == ig.group_id).name)

            data.append({
                'name': d.name,
                'description': d.description,
                'product_type': d.product_type,
                'protocol': d.protocol,
                'redirect_url': d.redirect_url,
                'metadata_url': d.metadata_url,
                'group_map': groupdata
            })

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_identity_providers: " + str(e.args))
        pass

##########################################################################
# Print Dynamic Groups
##########################################################################


def get_identity_dynamic_groups(identity, tenancy):
    print("    Dynamic Groups...")
    try:
        dynamic_groups = oci.pagination.list_call_get_all_results(identity.list_dynamic_groups, tenancy.id).data
        data = []

        for dg in dynamic_groups:
            data.append({
                'name': dg.name,
                'description': dg.description,
                'matching_rule': dg.matching_rule
            })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in print_identity_dynamic_groups: " + str(e.args))
        pass


##########################################################################
# Identity Module
##########################################################################
def get_identity_main(identity, tenancy_id, handle_managed_compartment, cmd):
    try:
        print("Extracting Identity")
        data = {}
        tenancy = identity.get_tenancy(tenancy_id).data
        data['tenancy'] = get_identity_tenancy(identity, tenancy)
        data['users'] = get_identity_users(identity, tenancy)
        data['groups'] = get_identity_groups(identity, tenancy)
        data['dynamic_groups'] = get_identity_dynamic_groups(identity, tenancy)
        data['policies'] = get_identity_policies(identity, tenancy, handle_managed_compartment, cmd)
        data['providers'] = get_identity_providers(identity, tenancy)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in oci_identity: " + str(e.args))
        pass

##########################################################################
# Print Network VCN IGW
##########################################################################


def get_core_network_vcn_igw(core, compartment, vcn):
    try:
        list_internet_gateways = core.list_internet_gateways(compartment.id, vcn.id).data
        return str(', '.join(x.display_name for x in list_internet_gateways))

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_igw: " + str(e.args))
        pass

##########################################################################
# Print Network VCN NAT
##########################################################################


def get_core_network_vcn_nat(core, compartment, vcn):
    try:
        list_nat_gateways = core.list_nat_gateways(compartment.id, vcn_id=vcn.id).data
        ret = ""
        for nat in list_nat_gateways:
            ret += str(nat.display_name) + " - " + str(nat.nat_ip) + " ( " + str(nat.lifecycle_state) + " ) "
            if nat.block_traffic:
                ret += " - Blocked  "
        return ret

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return ""
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_nat: " + str(e.args))
        pass

##########################################################################
# Print Network VCN SGW
##########################################################################


def get_core_network_vcn_sgw(core, compartment, vcn):
    try:
        list_service_gateways = core.list_service_gateways(compartment.id, vcn_id=vcn.id).data
        return str(', '.join(x.display_name for x in list_service_gateways))

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return ""
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_sgw: " + str(e.args))
        pass


##########################################################################
# get dRG details
##########################################################################
def get_core_network_vcn_drg_details(core, drg_attachment):
    try:
        # get DRG name
        drg = core.get_drg(drg_attachment.drg_id).data
        retStr = drg.display_name

        # check if IPSEC
        list_ip_sec_connections = oci.pagination.list_call_get_all_results(core.list_ip_sec_connections, drg.compartment_id, drg_id=drg_attachment.drg_id).data
        if len(list_ip_sec_connections) > 0:
            retStr += " + IPSEC (" + str(len(list_ip_sec_connections)) + ")"

        # Check Remote Peering
        rpcs = core.list_remote_peering_connections(drg.compartment_id, drg_id=drg_attachment.drg_id).data
        if len(rpcs) > 0:
            retStr += " + Remote Peering (" + str(len(rpcs)) + ")"

        # check transit routing
        if drg_attachment.route_table_id is not None:
            retStr += " + Transit Route(" + str(get_core_network_route(core, drg_attachment.route_table_id) + ")")

        return retStr
    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return ""
        raise
    except Exception as e:
        print("Error get_core_network_drg_details get_core_network_vcn_drg_attached: " + str(e.args))
        pass

##########################################################################
# Print Network VCN DRG Attached
##########################################################################


def get_core_network_vcn_drg_attached(core, compartment, vcn):
    try:
        list_drg_attachments = core.list_drg_attachments(compartment.id, vcn_id=vcn.id).data
        data = []
        for da in list_drg_attachments:
            val = get_core_network_vcn_drg_details(core, da)
            data.append(val)
        return str(', '.join(x for x in data))

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_drg_attached: " + str(e.args))
        pass

##########################################################################
# Print Network VCN Local Peering
##########################################################################


def get_core_network_vcn_local_peering(core, compartment, vcn):
    try:
        local_peering_gateways = core.list_local_peering_gateways(compartment.id, vcn.id).data
        data = []
        for lpg in local_peering_gateways:
            routestr = ""
            if lpg.route_table_id is not None:
                routestr = " + Transit Route(" + str(get_core_network_route(core, lpg.route_table_id)) + ")"

            data.append(str(lpg.display_name) + " - " + str(lpg.peer_advertised_cidr) + " - " + str(lpg.peering_status) + routestr)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_local_peering: " + str(e.args))
        pass

##########################################################################
# Print Network VCN subnets
##########################################################################


def get_core_network_vcn_subnets(core, compartment, vcn):
    try:
        subnets = oci.pagination.list_call_get_all_results(core.list_subnets, compartment.id, vcn.id, sort_by="DISPLAYNAME").data
        data = []
        for subnet in subnets:
            sec_lists = []
            for s in subnet.security_list_ids:
                sec_lists.append(str(core.get_security_list(s).data.display_name))

            # If no Availability Domain, the subnet is regional
            availability_domain = str(subnet.availability_domain)
            if availability_domain == "None":
                availability_domain = "Regional"

            val = ({
                'subnet': str(subnet.cidr_block) + "  " + availability_domain + (" (Private) " if subnet.prohibit_public_ip_on_vnic else " (Public)"),
                'name': str(subnet.display_name),
                'dns': str(subnet.dns_label),
                'dhcp_options': str(core.get_dhcp_options(subnet.dhcp_options_id).data.display_name),
                'security_list': sec_lists,
                'route': str(core.get_route_table(subnet.route_table_id).data.display_name)
            })
            if ocid:
                val['id'] = str(subnet.id)
            data.append(val)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_subnets: " + str(e.args))
        pass

##########################################################################
# get_core_network_port_range
##########################################################################


def get_core_network_vcn_security_rule_port_range(name, port_range):

    if port_range is None:
        return ""

    if (port_range.min == port_range.max):
        return name + "(" + str(port_range.min) + ") "
    else:
        return name + "(" + str(port_range.min) + "-" + str(port_range.max) + ") "

##########################################################################
# get Network vcn security rule
##########################################################################


def get_core_network_vcn_security_rule(security_rule):
    line = ""
    if isinstance(security_rule, oci.core.models.EgressSecurityRule):
        line = "Dst: " + str(security_rule.destination).ljust(18)

    if isinstance(security_rule, oci.core.models.IngressSecurityRule):
        line = "Src: " + str(security_rule.source).ljust(18)

    # protocol
    if security_rule.protocol == "1":
        line += "ICMP "
    elif security_rule.protocol == "6":
        line += "TCP  "
    elif security_rule.protocol == "17":
        line += "UDP  "
    elif security_rule.protocol == "all":
        line += "ALL  "
    else:
        line += str(" Prt(" + str(security_rule.protocol) + "), ").ljust(20)

    # tcp options
    if security_rule.tcp_options is not None:
        line += get_core_network_vcn_security_rule_port_range("Src", security_rule.tcp_options.source_port_range)
        line += get_core_network_vcn_security_rule_port_range("Dst", security_rule.tcp_options.destination_port_range)

    # udp options
    if security_rule.udp_options is not None:
        line += get_core_network_vcn_security_rule_port_range("Src", security_rule.udp_options.source_port_range)
        line += get_core_network_vcn_security_rule_port_range("Dst", security_rule.udp_options.destination_port_range)

    # icmp options
    if security_rule.icmp_options is not None:
        icmp = security_rule.icmp_options
        line += ""
        if icmp.code is not None:
            line += str(icmp.code) + ","
        if icmp.type is not None:
            line += str(icmp.type)

    # Stateless
    if security_rule.is_stateless:
        line += " (Stateless) "

    return line

##########################################################################
# Print Network vcn security list
##########################################################################


def get_core_network_vcn_security_lists(core, compartment, vcn):
    try:
        sec_lists = oci.pagination.list_call_get_all_results(core.list_security_lists, compartment.id, vcn.id, sort_by="DISPLAYNAME").data
        data = []
        for sl in sec_lists:
            sec_rules = []

            for sli in sl.ingress_security_rules:
                sec_rules.append("Ingres  : " + get_core_network_vcn_security_rule(sli))

            for sle in sl.egress_security_rules:
                sec_rules.append("Egres   : " + get_core_network_vcn_security_rule(sle))

            data.append({'name': str(sl.display_name), 'sec_rules': sec_rules})

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_security_lists: " + str(e.args))
        pass

###########################################################################
# get Network vcn rouet table
##########################################################################


def get_core_network_vcn_route_rule(core, route_rule):

    try:
        rl = route_rule
        line = ""

        # get the name of the component from OCID 2nd id
        network_list = rl.network_entity_id.split(".")
        network_dest = ""
        if len(network_list) > 1:
            network_dest = str(network_list[1])

        # if privateip - get the IP
        if network_dest == "privateip":
            network_dest = get_core_network_private_ip(core, rl.network_entity_id)
            if network_dest is None:
                network_dest = "privateip (not exist)"

        # if rl.cidr_block is not None: line+=str(rl.cidr_block)+"  "
        line += "DST:" + str(rl.destination) + " --> " + str(network_dest)
        return line
    except Exception as e:
        print("Error in get_core_network_vcn_route_tables: " + str(e.args))
        pass

########################################################################
# Print Network vcn Route Tables
##########################################################################


def get_core_network_vcn_route_tables(core, compartment, vcn):
    try:
        route_tables = oci.pagination.list_call_get_all_results(core.list_route_tables, compartment.id, vcn.id, sort_by="DISPLAYNAME").data
        data = []

        for rt in route_tables:
            route_rules = []
            for rl in rt.route_rules:
                route_rules.append(str(get_core_network_vcn_route_rule(core, rl)))
            if len(route_rules) > 0:
                val = ({'name': str(rt.display_name)})
                val['route_rules'] = route_rules
                data.append(val)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_route_tables: " + str(e.args))
        pass

##########################################################################
# get DHCP options for DHCP_ID
##########################################################################


def get_core_network_vcn_dhcp_options_opt(dhcp_option):

    opt = dhcp_option
    retstr = ""

    # if type = oci.core.models.DhcpDnsOption
    if isinstance(opt, oci.core.models.DhcpDnsOption):
        retstr += str(opt.type).ljust(17) + ": " + opt.server_type
        if len(opt.custom_dns_servers) > 0:
            retstr += " - "
            for ip in opt.custom_dns_servers:
                retstr += ip + "  "

    # if type = oci.core.models.DhcpSearchDomainOption
    if isinstance(opt, oci.core.models.DhcpSearchDomainOption):
        if len(opt.search_domain_names) > 0:
            retstr += str(opt.type).ljust(17) + ": "
            for ip in opt.search_domain_names:
                retstr += ip + "  "

    return retstr


##########################################################################
# get DHCP options for DHCP_ID
##########################################################################
def get_core_network_vcn_dhcp_options(core, compartment, vcn):

    try:
        dhcp_options = oci.pagination.list_call_get_all_results(core.list_dhcp_options, compartment.id, vcn.id, sort_by="DISPLAYNAME").data
        data = []

        for dhcp in dhcp_options:
            dhcp_opt = []
            if dhcp.options is not None:
                for opt in dhcp.options:
                    dhcp_opt.append(get_core_network_vcn_dhcp_options_opt(opt))
            data.append({'name': str(dhcp.display_name), 'opt': dhcp_opt})
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_vcn_dhcp_options: " + str(e.args))
        pass


##########################################################################
# print network vcn
# loop on other compartments for vcn properties
##########################################################################
def get_core_network_vcn(core, curr_compartment, compartments):

    try:
        vcns = oci.pagination.list_call_get_all_results(core.list_vcns, curr_compartment.id, sort_by="DISPLAYNAME").data
        vcn_data = []

        for vcn in vcns:

            # run all compartments
            data = []
            for compartment in compartments:
                val = ({
                    'compartment': str(compartment.name),
                    'igw': get_core_network_vcn_igw(core, compartment, vcn),
                    'sgw': get_core_network_vcn_sgw(core, compartment, vcn),
                    'nat': get_core_network_vcn_nat(core, compartment, vcn),
                    'drg_attached': get_core_network_vcn_drg_attached(core, compartment, vcn),
                    'local_peering': get_core_network_vcn_local_peering(core, compartment, vcn),
                    'subnets': get_core_network_vcn_subnets(core, compartment, vcn),
                    'security_lists': get_core_network_vcn_security_lists(core, compartment, vcn),
                    'route_tables': get_core_network_vcn_route_tables(core, compartment, vcn),
                    'dhcp_options': get_core_network_vcn_dhcp_options(core, compartment, vcn)
                })

                if (val['igw'] or val['sgw'] or val['nat'] or val['drg_attached'] or val['local_peering'] or val['subnets'] or val['security_lists'] or val['route_tables'] or val['dhcp_options']):
                    data.append(val)

            # assign the data to the vcn
            vcn_data.append({'id': str(vcn.id),
                             'name': str(vcn.cidr_block) + " - " + str(vcn.display_name) + " - " + str(vcn.vcn_domain_name),
                             'compartment': str(curr_compartment.name),
                             'data': data
                             })
        return vcn_data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except BaseException as e:
        print("Error in get_core_network_vcn: " + str(e.args))
        pass


##########################################################################
# print network cpe
##########################################################################
def get_core_network_cpe(core, compartment):

    try:
        cpes = oci.pagination.list_call_get_all_results(core.list_cpes, compartment.id).data
        data = [str(cpe.display_name) + " - " + str(cpe.ip_address) for cpe in cpes]
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_cpe: " + str(e.args))
        pass

##########################################################################
# print network drg
##########################################################################


def get_core_network_drg(core, compartment):

    try:
        drgs = oci.pagination.list_call_get_all_results(core.list_drgs, compartment.id).data
        data = [str(drg.display_name) for drg in drgs]
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_drg: " + str(e.args))
        pass


##########################################################################
# print network remote peering
##########################################################################
def get_core_network_remote_peering(core, compartment):

    try:
        rpcs = oci.pagination.list_call_get_all_results(core.list_remote_peering_connections, compartment.id).data
        data = []
        for rpc in rpcs:
            drg = core.get_drg(rpc.drg_id).data
            data.append({
                'id': str(rpc.id),
                'peer_id': str(rpc.peer_id),
                'name': str(rpc.display_name),
                'drg': str(drg.display_name),
                'is_cross_tenancy_peering': str(rpc.is_cross_tenancy_peering),
                'peer_region_name': str(rpc.peer_region_name),
                'peer_tenancy_id': rpc.peer_tenancy_id,
                'peering_status': rpc.peering_status
            })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_remote_peering: " + str(e.args))
        pass

##########################################################################
# get network ipsec
##########################################################################


def get_core_network_ipsec(core, compartment):

    try:
        list_ip_sec_connections = oci.pagination.list_call_get_all_results(core.list_ip_sec_connections, compartment.id).data
        data = []

        for ips in list_ip_sec_connections:
            drg = core.get_drg(ips.drg_id).data
            cpe = core.get_cpe(ips.cpe_id).data
            ipss = core.get_ip_sec_connection_device_status(ips.id).data
            data_tun = []
            for tunnel in ipss.tunnels:
                data_tun.append({'ip_address': str(tunnel.ip_address),
                                 'status': str(tunnel.lifecycle_state),
                                 'status_date': tunnel.time_state_modified.strftime("%Y-%m-%d %H:%M")})
            data.append({
                'name': str(ips.display_name),
                'drg': str(drg.display_name),
                'cpe': str(cpe.display_name) + " - " + str(cpe.ip_address),
                'routes': ips.static_routes,
                'tunnels': data_tun
            })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_ipsec: " + str(e.args))
        pass


##########################################################################
# get network virtual_circuit
##########################################################################
def get_core_network_virtual_circuit(core, compartment):

    try:
        list_virtual_circuits = oci.pagination.list_call_get_all_results(core.list_virtual_circuits, compartment.id).data
        data = []

        for vc in list_virtual_circuits:
            drg = core.get_drg(vc.gateway_id).data
            data_cc = []
            for cc in vc.cross_connect_mappings:
                data_cc.append({'customer_bgp_peering_ip': str(cc.customer_bgp_peering_ip),
                                'oracle_bgp_peering_ip': str(cc.oracle_bgp_peering_ip),
                                'vlan': str(cc.vlan)})
            data.append({
                'name': str(vc.display_name),
                'bandwidth_shape_name': str(vc.bandwidth_shape_name),
                'bgp_management': str(vc.bgp_management),
                'bgp_session_state': str(vc.bgp_session_state),
                'customer_bgp_asn': str(vc.customer_bgp_asn),
                'drg': str(drg.display_name),
                'lifecycle_state': str(vc.lifecycle_state),
                'oracle_bgp_asn': str(vc.oracle_bgp_asn),
                'provider_name': str(vc.provider_name),
                'provider_service_name': str(vc.provider_service_name),
                'provider_state': str(vc.provider_state),
                'reference_comment': str(vc.reference_comment),
                'service_type': str(vc.service_type),
                'time_created': str(vc.time_created),
                'cross_connect_mappings': data_cc,
                'type': str(vc.type)
            })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_virtual_circuit: " + str(e.args))
        pass

##########################################################################
# print network fastconnect
##########################################################################


def get_core_network_fastconnect(core, compartment):

    try:
        fastconnects = oci.pagination.list_call_get_all_results(core.list_fast_connect_provider_services, compartment.id).data
        data = []

        for fc in fastconnects:
            data.append({
                'name': str(fc.description),
                'private_peering_bgp_management': str(fc.private_peering_bgp_management),
                'provider': str(fc.provider_name) + " - " + str(fc.provider_service_name),
                'public_peering_bgp_management': fc.public_peering_bgp_management,
                'type': fc.type
            })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_fastconnect: " + str(e.args))
        pass

##########################################################################
# get Network Subnet
##########################################################################


def get_core_network_subnet(virtual_network, subnet_id):
    try:
        subnet = virtual_network.get_subnet(subnet_id).data
        return_str = str(subnet.cidr_block) + "  " + str(subnet.display_name) + (" (Private) " if subnet.prohibit_public_ip_on_vnic else " (Public)")
        return return_str

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_subnet: " + str(e.args))
        pass

##########################################################################
# get Network Subnet
##########################################################################


def get_core_network_route(virtual_network, route_table_id):
    try:
        route = virtual_network.get_route_table(route_table_id).data
        return_str = str(route.display_name)
        return return_str

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_route: " + str(e.args))
        pass

##########################################################################
# get_core_network_private_ip
##########################################################################


def get_core_network_private_ip(virtual_network, private_ip_id):

    try:
        ip = virtual_network.get_private_ip(private_ip_id).data
        return (ip.ip_address + " - " + ip.display_name)

    except Exception:
        pass

##########################################################################
# print Core Network Vnic
##########################################################################


def get_core_network_vnic(virtual_network, vnic_id):
    try:
        if vnic_id is None:
            return ""
        vnic = virtual_network.get_vnic(vnic_id).data
        returnstr = (str(vnic.private_ip) + " (Priv) ")
        if vnic.public_ip is not None:
            returnstr += ", " + str(vnic.public_ip) + " (Pub) "
        if vnic.skip_source_dest_check:
            returnstr += ("- Skip=Y")
        if vnic.is_primary:
            returnstr + " - Primary "
        if vnic.subnet_id is not None:
            returnstr += ", Subnet " + virtual_network.get_subnet(vnic.subnet_id).data.display_name
        return returnstr

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_network_vnic: " + str(e.args))
        pass

##########################################################################
# Network
##########################################################################
#
# class oci.core.virtual_network_client.virtual_networkClient(config, **kwargs)
#
#    TBD Apis
#    list_allowed_peer_regions_for_remote_peering(**kwargs)
#    list_private_ips(**kwargs)
#    list_public_ips(scope, compartment_id, **kwargs)
#    list_cross_connect_groups(compartment_id, **kwargs)
#    list_cross_connect_locations(compartment_id, **kwargs)
#    list_cross_connects(compartment_id, **kwargs)
#    list_crossconnect_port_speed_shapes(compartment_id, **kwargs)
#
##########################################################################


def get_core_network_main(virtual_network, compartment, compartments):

    return_data = {}

    data = get_core_network_vcn(virtual_network, compartment, compartments)
    if len(data) > 0:
        return_data['vcn'] = data

    data = get_core_network_drg(virtual_network, compartment)
    if len(data) > 0:
        return_data['drg'] = data

    data = get_core_network_cpe(virtual_network, compartment)
    if len(data) > 0:
        return_data['cpe'] = data

    data = get_core_network_ipsec(virtual_network, compartment)
    if len(data) > 0:
        return_data['ipsec'] = data

    data = get_core_network_remote_peering(virtual_network, compartment)
    if len(data) > 0:
        return_data['remote_peering'] = data

    data = get_core_network_virtual_circuit(virtual_network, compartment)
    if len(data) > 0:
        return_data['virtual_circuit'] = data

    return return_data

##########################################################################
# get volume backup policy
##########################################################################


def get_core_block_volume_backup_policy(block_storage, volume_id):

    try:
        backupstr = ""
        backup_policy_assignments = block_storage.get_volume_backup_policy_asset_assignment(volume_id).data
        if len(backup_policy_assignments) > 0:
            backupstr = " Backup="
            for backup_policy_assignment in backup_policy_assignments:
                bp = block_storage.get_volume_backup_policy(backup_policy_assignment.policy_id).data
                backupstr += bp.display_name + " "
        return backupstr

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        # if backup to other region ignore
        if e.code == 'InvalidParameter':
            return []
        if e.code == 'TooManyRequests':
            return []
        raise
    except Exception as e:
        print("Error in get_core_block_volume_backup_policy: " + str(e.args))
        pass

##########################################################################
# print Core Block boot volume
##########################################################################


def get_core_block_volume_boot(block_storage, boot_volume_id, compartment_text):
    try:
        bv = block_storage.get_boot_volume(boot_volume_id).data
        backupstr = get_core_block_volume_backup_policy(block_storage, boot_volume_id)
        value = {
            'sum_info': 'Compute - Block Storage (gb)',
            'sum_size_gb': str(bv.size_in_gbs),
            'desc': (str(bv.size_in_gbs) + "gb - " + str(bv.display_name) + "  (" + bv.lifecycle_state + ")" + backupstr + compartment_text)
        }
        return value

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_block_boot_volume: " + str(e.args))
        pass

##########################################################################
# print Core Block Volume
##########################################################################


def get_core_block_volume(block_storage, volume_id, compartment_text):
    try:
        vol = block_storage.get_volume(volume_id).data

        # Volume Group - TBD - need to be tested including backup
        groupstr = ""
        if vol.volume_group_id is not None:
            groupstr = "- Group " + block_storage.get_volume_group(vol.volume_group_id).data.display_name
            groupbackup = get_core_block_volume_backup_policy(block_storage, vol.volume_group_id)
            if groupbackup is not None:
                groupstr += " Backup=" + groupbackup

        # vol backup
        backupstr = get_core_block_volume_backup_policy(block_storage, volume_id)

        # return
        return {
            'sum_info': 'Compute - Block Storage (gb)',
            'sum_size_gb': str(vol.size_in_gbs),
            'desc': (str(vol.size_in_gbs) + "gb - " + str(vol.display_name) + "  (" + vol.lifecycle_state + ")" + groupstr + backupstr + compartment_text)
        }

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_block_volume: " + str(e.args))
        pass

##########################################################################
# get compute boot volume
##########################################################################


def get_core_block_volume_boot_backup(block_storage, compartment):

    try:
        data = []
        backups = oci.pagination.list_call_get_all_results(block_storage.list_boot_volume_backups, compartment.id, lifecycle_state="AVAILABLE").data

        for backup in backups:
            value = {}
            backup_name = ""

            # add try except due to OCI TooManyRequests
            try:
                backup_name = str(block_storage.get_boot_volume(backup.boot_volume_id).data.display_name)
            except Exception:
                pass

            value['name'] = (backup_name + ", " + str(backup.type) + ", " + str(backup.source_type) + ", " +
                             str(backup.time_created)[0:16] + " - " + str(backup.expiration_time)[0:16])
            value['desc'] = (str(backup.display_name))
            value['size'] = (str(backup.size_in_gbs) + "gb " + ", Stored " + str(backup.unique_size_in_gbs) + "gb")
            value['sum_info'] = 'Object Storage - BV Backups (gb)'
            value['sum_size_gb'] = (str(backup.unique_size_in_gbs))
            value['boot_volume_id'] = str(backup.boot_volume_id)

            data.append(value)

        if len(data) > 0:
            return sorted(data, key=lambda k: k['name'])
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_compute_images: " + str(e.args))
        pass


##########################################################################
# get compute boot volume
##########################################################################
def get_core_block_volume_backup(block_storage, compartment):

    try:
        data = []
        backups = oci.pagination.list_call_get_all_results(block_storage.list_volume_backups, compartment.id, lifecycle_state="AVAILABLE").data

        for backup in backups:
            value = {}
            backup_name = ""
            # add try except due to OCI TooManyRequests
            try:
                backup_name = str(block_storage.get_volume(backup.volume_id).data.display_name)
            except Exception:
                pass

            value['name'] = (backup_name + ", " + str(backup.type) + ", " + str(backup.source_type) + ", " + str(backup.time_created)[0:16] + " - " + str(backup.expiration_time)[0:16])

            value['desc'] = (str(backup.display_name))
            value['size'] = (str(backup.size_in_gbs) + "gb " + ", Stored " + str(backup.unique_size_in_gbs) + "gb")
            value['sum_info'] = 'Object Storage - BV Backups (gb)'
            value['sum_size_gb'] = (str(backup.unique_size_in_gbs))
            value['volume_id'] = str(backup.volume_id)

            data.append(value)

        if len(data) > 0:
            return sorted(data, key=lambda k: k['name'])
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        if e.code == 'InvalidParameter':
            return []
        raise
    except Exception as e:
        print("Error in get_core_block_volume_block_backup: " + str(e.args))
        pass

##########################################################################
# print compute instances
##########################################################################


def get_core_compute_instances(compute, block_storage, virtual_network, compartment, compartments):

    try:
        instances = oci.pagination.list_call_get_all_results(compute.list_instances, compartment.id, sort_by="DISPLAYNAME").data
    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in print_core_compute_instances: " + str(e.args))
        pass

    data = []
    for instance in instances:
        if instance.lifecycle_state != "TERMINATED":
            inst = {}
            if ocid:
                inst['id'] = instance.id
            inst['name'] = ((instance.display_name) + " - " + str(instance.shape) + " - " + str(instance.lifecycle_state))
            inst['sum_info'] = 'Compute'
            inst['sum_shape'] = str(instance.shape)
            inst['availability_domain'] = str(instance.availability_domain)
            inst['fault_domain'] = str(instance.fault_domain)
            if instance.time_maintenance_reboot_due is not None:
                inst['time_maintenance_reboot_due'] = str(instance.time_maintenance_reboot_due)

            try:
                inst['image'] = str(compute.get_image(instance.image_id).data.display_name)
                if ocid:
                    inst['image_id'] = instance.image_id
            except BaseException:
                pass

            # boot volumes attachments
            try:
                bv = []
                for c in compartments:
                    comp_text = ""
                    if c.name != compartment.name:
                        comp_text = " (Compartment=" + c.name + ")"

                    for bva in compute.list_boot_volume_attachments(instance.availability_domain, c.id, instance_id=instance.id).data:
                        bvval = {}
                        if ocid:
                            bvval['id'] = bva.boot_volume_id
                        bvval = get_core_block_volume_boot(block_storage, bva.boot_volume_id, comp_text)
                        bv.append(bvval)
                inst['boot_volume'] = bv
            except BaseException:
                pass

            # Volumes attachements
            try:
                vol = []
                for c in compartments:
                    comp_text = ""
                    if c.name != compartment.name:
                        comp_text = " (Compartment=" + c.name + ")"

                    for va in oci.pagination.list_call_get_all_results(compute.list_volume_attachments, c.id, instance_id=instance.id).data:
                        if (va.lifecycle_state == "ATTACHED"):
                            bvval = {}
                            if ocid:
                                bvval['id'] = va.volume_id
                            bvval = get_core_block_volume(block_storage, va.volume_id, comp_text)
                            vol.append(bvval)
                inst['block_volume'] = vol
            except BaseException:
                pass

            # vnics attachements
            try:
                vnic = []
                for c in compartments:
                    comp_text = ""
                    if c.name != compartment.name:
                        comp_text = " (Compartment=" + c.name + ")"

                    for vna in compute.list_vnic_attachments(c.id, instance_id=instance.id).data:
                        if (vna.lifecycle_state == "ATTACHED"):
                            val = {}
                            if ocid:
                                val['id'] = vna.vnic_id
                            val['desc'] = (get_core_network_vnic(virtual_network, vna.vnic_id) + comp_text)
                            vnic.append(val)
                inst['vnic'] = vnic
            except BaseException:
                pass

            # console connections
            try:
                for icc in compute.list_instance_console_connections(compartment.id, instance_id=instance.id).data:
                    if (icc.lifecycle_state == "ACTIVE"):
                        if ocid:
                            inst['console_id'] = icc.id
                        inst['console'] = "Console Connection Active"
            except BaseException:
                pass
            data.append(inst)

    # return data
    return data

##########################################################################
# print compute images
##########################################################################


def get_core_compute_images(compute, compartment):

    try:
        data = []
        images = oci.pagination.list_call_get_all_results(compute.list_images, compartment.id, sort_by="DISPLAYNAME", lifecycle_state="AVAILABLE").data
        filtered_images = [i for i in images if i.base_image_id is not None]

        for image in filtered_images:
            value = {}
            value['desc'] = (str(image.display_name) + " - " + image.operating_system + " - " + str(round(image.size_in_mbs / 1024)) + "gb - Base:  " + compute.get_image(image.base_image_id).data.display_name)
            value['sum_info'] = 'Object Storage - Images (gb)'
            value['sum_size_gb'] = (str(image.size_in_mbs / 1024))
            if ocid:
                value['id'] = image.id
            data.append(value)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_core_compute_images: " + str(e.args))
        pass

##########################################################################
# print compute instance configuration
##########################################################################


def get_core_compute_instance_configuration(computeManage, compute, compartment):

    try:
        data = []
        # oci.core.models.InstanceConfigurationSummary
        configs = oci.pagination.list_call_get_all_results(computeManage.list_instance_configurations, compartment.id).data

        for config in configs:
            value = {}
            instdata = computeManage.get_instance_configuration(config.id).data
            value['name'] = str(config.display_name) + " - " + str(instdata.instance_details.launch_details.shape)
            data.append(value)

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_compute_instance_configuration: " + str(e.args))
        pass

##########################################################################
# print compute instance pool
# list_instance_pool_instances (instance_pool_id) - oci.core.models.InstanceSummary
# list_instance_pools
##########################################################################


def get_core_compute_instance_pool(computeManage, compute, compartment):

    try:
        data = []
        # oci.core.models.InstanceConfigurationSummary
        pools = oci.pagination.list_call_get_all_results(computeManage.list_instance_pools, compartment.id).data

        for pool in pools:
            value = {}
            value['name'] = str(pool.display_name) + " - " + str(pool.lifecycle_state) + " - Size: " + str(pool.size)
            value['instance_configuration_id'] = pool.instance_configuration_id
            data.append(value)

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_core_compute_instance_pool: " + str(e.args))
        pass


##########################################################################
# Compute
##########################################################################
#
# class oci.core.ComputeClient(config, **kwargs)
# TBD - list_volume_group_backups
# TBD - KMS
##########################################################################
def get_core_compute_main(compute, computeManage, block_storage, virtual_network, compartment, compartments):
    return_data = {}

    data = get_core_compute_instances(compute, block_storage, virtual_network, compartment, compartments)
    if len(data) > 0:
        return_data['instances'] = data

    data = get_core_compute_instance_configuration(computeManage, compute, compartment)
    if len(data) > 0:
        return_data['instance_configuration'] = data

    data = get_core_compute_instance_pool(computeManage, compute, compartment)
    if len(data) > 0:
        return_data['instance_pool'] = data

    data = get_core_compute_images(compute, compartment)
    if len(data) > 0:
        return_data['images'] = data

    data = get_core_block_volume_boot_backup(block_storage, compartment)
    if len(data) > 0:
        return_data['boot_volume_backup'] = data

    data = get_core_block_volume_backup(block_storage, compartment)
    if len(data) > 0:
        return_data['volume_backup'] = data

    return return_data

##########################################################################
# print database db nodes
##########################################################################


def get_database_db_nodes(database, virtual_network, dbs_id, compartment):

    try:
        data = []
        db_nodes = database.list_db_nodes(compartment.id, dbs_id).data

        nodeidstr = " "
        nodeid = 0
        for db_node in db_nodes:
            nodeid += 1

            if len(db_nodes) > 1:
                nodeidstr = str(nodeid)

            data.append("Node " + str(nodeidstr) + "  : " + str(db_node.hostname) + " - " + str(db_node.lifecycle_state) + " - " + get_core_network_vnic(virtual_network, db_node.vnic_id))

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_database_db_nodes: " + str(e.args))
        pass


##########################################################################
# print database Databases
##########################################################################
def get_database_db_databases(database, db_home_id, compartment):

    try:
        data = []
        dbs = oci.pagination.list_call_get_all_results(database.list_databases, compartment.id, db_home_id, sort_by="DBNAME").data

        for db in dbs:

            backupstr = " - AutoBck=N"
            if db.db_backup_config is not None:
                if db.db_backup_config.auto_backup_enabled:
                    backupstr = " - AutoBck=Y"

            pdb_name = ""
            if db.pdb_name is not None:
                pdb_name = db.pdb_name + " - "

            value = {'name':
                     (str(db.db_name) + " - " + str(db.db_unique_name) + " - " + pdb_name +
                      str(db.db_workload) + " - " +
                      str(db.character_set) + " - " + str(db.lifecycle_state) + backupstr)
                     }
            value['backups'] = get_database_db_backups(database, db.id)

            data.append(value)
        return data
    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_database_databases: " + str(e.args))
        pass


##########################################################################
# get db home patches
##########################################################################
def get_database_db_homes_patches(database, db_home_id):

    try:
        data = []
        dbps = oci.pagination.list_call_get_all_results(database.list_db_home_patches, db_home_id).data

        for dbp in dbps:
            data.append(str(dbp.description) + " - " + str(dbp.version) + " - " + str(dbp.time_released)[0:10] + " - Last Action: " + str(dbp.last_action))
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        # due to exadata
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        if e.code == 'IncorrectState':
            return []
        raise
    except Exception as e:
        print("Error in get_database_db_homes_patches: " + str(e.args))
        pass

##########################################################################
# print database db homes
##########################################################################


def get_database_db_homes(database, virtual_network, dbs_id, compartment):

    try:
        data = []
        db_homes = oci.pagination.list_call_get_all_results(database.list_db_homes, compartment.id, dbs_id).data

        for db_home in db_homes:
            data.append(
                {'home': str(db_home.display_name) + " - " + str(db_home.db_version),
                 'databases': get_database_db_databases(database, db_home.id, compartment),
                 'patches': get_database_db_homes_patches(database, db_home.id)
                 })

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_database_db_homes: " + str(e.args))
        pass

##########################################################################
# get db system patches
##########################################################################


def get_database_db_system_patches(database, dbs_id):

    try:
        data = []
        dbps = oci.pagination.list_call_get_all_results(database.list_db_system_patches, dbs_id).data

        for dbp in dbps:
            data.append(str(dbp.description) + " - " + str(dbp.version) + " - " + str(dbp.time_released)[0:10] + " - Last Action: " + str(dbp.last_action))
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        # due to exadata
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        if e.code == 'IncorrectState':
            return []
        raise
    except Exception as e:
        print("Error in get_database_db_system_patches: " + str(e.args))
        pass


##########################################################################
# print database db homes
##########################################################################
def get_database_db_system_scandns(scan_dns_record_id):
    try:
        # dnsentry=dns.get_zone(scan_dns_record_id)
        # return str(dnsentry.name)
        # TBD: find the SCANDNS based on scan_dns_record_id)
        return scan_dns_record_id

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_database_db_homes: " + str(e.args))
        pass

##########################################################################
# print database db system
##########################################################################


def get_database_db_system(database, virtual_network, dbs, compartment):

    data = {}
    data['name'] = (str(dbs.display_name) + " - " + str(dbs.shape) + " - " + str(dbs.lifecycle_state))
    data['sum_info'] = 'Database - ' + str(dbs.shape) + " - " + get_license_type(str(dbs.license_model))
    data['sum_info_storage'] = 'Database - Storage (gb)'
    data['sum_size_gb'] = str(dbs.data_storage_size_in_gbs)
    data['availability_domain'] = str(dbs.availability_domain)
    data['cpu_core_count'] = str(dbs.cpu_core_count)
    if dbs.node_count is not None:
        data['node_count'] = str(dbs.node_count)
    data['version'] = (str(dbs.version) + " - " + str(dbs.database_edition) + " - " + str(dbs.license_model))
    data['host'] = str(dbs.hostname)
    data['domain'] = str(dbs.domain)
    if dbs.cluster_name is not None:
        data['cluster_name'] = str(dbs.cluster_name)

    if dbs.data_storage_size_in_gbs is not None:
        data['data'] = str(dbs.data_storage_size_in_gbs) + "gb - " + str(dbs.data_storage_percentage) + "%"
    else:
        data['data'] = str(dbs.data_storage_percentage) + "%"

    data['data_subnet'] = str(get_core_network_subnet(virtual_network, dbs.subnet_id))
    if dbs.backup_subnet_id is not None:
        data['backup_subnet'] = str(get_core_network_subnet(virtual_network, dbs.backup_subnet_id))
    if dbs.scan_dns_record_id is not None:
        data['scan_dns'] = get_database_db_system_scandns(str(dbs.scan_dns_record_id))

    if dbs.scan_ip_ids is not None:
        scan_ips = []
        for scan_ip in dbs.scan_ip_ids:
            scan_ips.append(get_core_network_private_ip(virtual_network, scan_ip))
        data['scan_ips'] = scan_ips

    if dbs.vip_ids is not None:
        vip_ips = []
        for vipip in dbs.vip_ids:
            vip_ips.append(get_core_network_private_ip(virtual_network, vipip))
        data['vip_ips'] = vip_ips

    # Listener
    data['listener_port'] = str(dbs.listener_port)

    # db system patches
    data['patches'] = get_database_db_system_patches(database, dbs.id)

    return data

##########################################################################
# print database db backups
##########################################################################


def get_database_db_backups(database, dbid):

    try:
        data = []
        ssize = ""
        backups = oci.pagination.list_call_get_all_results(database.list_backups, database_id=dbid).data

        for backup in backups:
            bsize = "None"
            if backup.database_size_in_gbs:
                bsize = "{0:.1f}".format(round(backup.database_size_in_gbs, 1)) + "gb"
                ssize = "{0:.1f}".format(round(backup.database_size_in_gbs, 1))

            data.append(
                {'name': str(backup.display_name) + " - " + str(backup.type) + " - " + str(backup.lifecycle_state),
                 'time': str(backup.time_started)[0:16] + " - " + str(backup.time_ended)[0:16],
                 'size': bsize,
                 'sum_info': 'Object Storage - DB Backup (gb)',
                 'sum_size_gb': ssize
                 })
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_database_db_backups: " + str(e.args))
        pass


##########################################################################
# Database
##########################################################################
#
# class oci.database.DatabaseClient(config, **kwargs)
#
# Below APIs not yet done:
# list_db_home_patch_history_entries
# list_db_system_patch_history_entries
# list_data_guard_associations
#
##########################################################################
def get_database_db_systems(database, virtual_network, compartment):

    try:
        list_db_systems = oci.pagination.list_call_get_all_results(database.list_db_systems, compartment.id).data
        data = []

        for dbs in list_db_systems:
            value = {}
            if dbs.lifecycle_state != "TERMINATED":
                value = get_database_db_system(database, virtual_network, dbs, compartment)
                value['db_nodes'] = get_database_db_nodes(database, virtual_network, dbs.id, compartment)
                value['db_homes'] = get_database_db_homes(database, virtual_network, dbs.id, compartment)
                data.append(value)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound' or e.code == 'Forbidden':
            return []
        raise
    except Exception as e:
        print("Error in get_database_main: " + str(e.args))
        pass

##########################################################################
# print database db system
##########################################################################


def get_database_autonomous_details(dbs):

    data = {}
    data['name'] = (str(dbs.display_name) + " - " + str(dbs.license_model) + " - " + str(dbs.lifecycle_state))
    data['cpu_core_count'] = str(dbs.cpu_core_count)
    data['data_storage_size_in_tbs'] = str(dbs.data_storage_size_in_tbs)
    data['db_name'] = str(dbs.db_name)
    data['service_console_url'] = str(dbs.service_console_url)
    data['time_created'] = str(dbs.time_created)
    data['connection_strings'] = str(dbs.connection_strings)

    data['sum_info'] = "Autonoumous Database (OCPUs) - " + get_license_type(str(dbs.license_model))
    data['sum_count'] = str(dbs.cpu_core_count)
    data['sum_info_storage'] = "Autonoumous Database (tb)"
    data['sum_size_tb'] = str(dbs.data_storage_size_in_tbs)
    return data

##########################################################################
# Autonomous
##########################################################################
#
# class oci.database.DatabaseClient(config, **kwargs)
#
# Below APIs not yet done:
# list_autonomous_database_backups
# list_autonomous_data_warehouse_backups
#
##########################################################################


def get_database_autonomous_transaction(database, compartment):

    try:
        list_adwcs = oci.pagination.list_call_get_all_results(database.list_autonomous_databases, compartment.id, sort_by="DISPLAYNAME").data
        data = []

        for atp in list_adwcs:
            value = {}
            if atp.lifecycle_state != "TERMINATED" and atp.lifecycle_state != "UNAVAILABLE":
                value = get_database_autonomous_details(atp)
                data.append(value)
        return data

    except oci.exceptions.RequestException:
        pass
    except oci.exceptions.ServiceError:
        pass
    except Exception as e:
        print("Error in get_database_atp: " + str(e.args))
        pass

##########################################################################
# Autonomous
##########################################################################
#
# class oci.database.DatabaseClient(config, **kwargs)
#
# Below APIs not yet done:
# list_autonomous_database_backups
# list_autonomous_databases
# list_autonomous_data_warehouse_backups
#
##########################################################################


def get_database_autonomous_warehouse(database, compartment):

    try:
        list_adwcs = oci.pagination.list_call_get_all_results(database.list_autonomous_data_warehouses, compartment.id, sort_by="DISPLAYNAME").data
        data = []

        for adwc in list_adwcs:
            value = {}
            if adwc.lifecycle_state != "TERMINATED" and adwc.lifecycle_state != "UNAVAILABLE":
                value = get_database_autonomous_details(adwc)
                data.append(value)
        return data

    except oci.exceptions.RequestException:
        pass
    except oci.exceptions.ServiceError:
        pass
    except Exception as e:
        print("Error in get_database_autonomous_warehouse: " + str(e.args))
        pass

##########################################################################
# Database
##########################################################################


def get_database_main(database, virtual_network, compartment):

    return_data = {}

    data = get_database_db_systems(database, virtual_network, compartment)
    if data:
        if len(data) > 0:
            return_data['db_system'] = data

    data = get_database_autonomous_warehouse(database, compartment)
    if data:
        if len(data) > 0:
            return_data['adwc'] = data

    data = get_database_autonomous_transaction(database, compartment)
    if data:
        if len(data) > 0:
            return_data['atp'] = data

    return return_data

##########################################################################
# print file systems snapshot
##########################################################################


def get_file_storage_snapshots(file_storage, file_system_id):

    try:
        data = []
        snapshots = oci.pagination.list_call_get_all_results(file_storage.list_snapshots, file_system_id).data

        for snap in snapshots:
            data.append(str(snap.name) + " - " + snap.lifecycle_state)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound' or e.code == 'Forbidden':
            return []
        raise
    except Exception as e:
        print("Error in get_file_storage_snapshots: " + str(e.args))
        pass

##########################################################################
# print file systems mount targets
##########################################################################


def get_file_storage_mount_target(file_storage, virtual_network, export_set):

    try:
        mount_targets = oci.pagination.list_call_get_all_results(
            file_storage.list_mount_targets,
            export_set.compartment_id,
            export_set.availability_domain,
            export_set_id=export_set.id,
            sort_by="DISPLAYNAME").data
        data = []
        for mt in mount_targets:
            datamt = []
            for private_ip_id in mt.private_ip_ids:
                datamt.append(get_core_network_private_ip(virtual_network, private_ip_id))

            data.append({'mount': mt.display_name + " - Subnet: " + str(get_core_network_subnet(virtual_network, mt.subnet_id)) + " - " + export_set.lifecycle_state,
                         'ips': datamt})
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_file_storage_mount_target: " + str(e.args))
        pass

##########################################################################
# print file systems limits
##########################################################################


def get_file_storage_limits(export_set):
    try:
        file_details = ""
        bytes_details = ""
        max_fs_stat_bytes = export_set.max_fs_stat_bytes
        max_fs_stat_files = export_set.max_fs_stat_files

        # handle files:
        if int(max_fs_stat_files).bit_length() >= 63:
            file_details = "Files = 64bit"
        elif int(max_fs_stat_files).bit_length() == 31:
            file_details = "Files = 32bit"
        else:
            file_details = "Files = " + str(max_fs_stat_files)

        # handle bytes
        if int(max_fs_stat_bytes).bit_length() >= 63:
            bytes_details = "Size = Unlimited"
        else:
            bytes_details = "Size = " + str(int(max_fs_stat_bytes / 1024 / 1024 / 1024)) + "gb"

        return bytes_details + ", " + file_details
    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_file_storage_limits: " + str(e.args))
        pass

##########################################################################
# print file systems exports
##########################################################################


def get_file_storage_exports(file_storage, virtual_network, file_system_id):

    try:
        data = []
        exports = oci.pagination.list_call_get_all_results(file_storage.list_exports, file_system_id=file_system_id, sort_by="PATH").data

        for export in exports:
            dataval = {}
            dataval['path'] = str(export.path) + " - " + str(export.lifecycle_state)

            # list export sets
            export_set = file_storage.get_export_set(export.export_set_id).data
            dataval['exportset'] = str(export_set.display_name) + " - " + str(export_set.availability_domain) + " - " + \
                str(export_set.lifecycle_state) + " - Limits: " + get_file_storage_limits(export_set)

            # Mount Target
            dataval['mount_targeet'] = get_file_storage_mount_target(file_storage, virtual_network, export_set)
            data.append(dataval)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_file_storage_exports: " + str(e.args))
        pass

##########################################################################
# print file systems snapshot
##########################################################################


def get_file_storage_details(file_system):

    data = str(file_system.display_name) + " - "
    data += str(file_system.availability_domain) + " - "
    data += str(file_system.lifecycle_state) + " - "
    data += str(round(file_system.metered_bytes / 1024 / 1024 / 1024, 1)) + "gb metered"
    return data

##########################################################################
# File System
##########################################################################
#
# class oci.file_storage.FileStorageClient(config, **kwargs)
#
##########################################################################


def get_file_storage_main(file_storage, identity, virtual_network, compartment):
    try:
        data = []
        availability_domains = identity.list_availability_domains(compartment.id).data

        for ad in availability_domains:
            file_systems = file_storage.list_file_systems(compartment.id, ad.name).data

            # print details
            for fs in file_systems:
                dataval = {}
                dataval['filesystem'] = get_file_storage_details(fs)
                dataval['sum_info'] = 'File Storage (gb)'
                dataval['sum_size_gb'] = round(fs.metered_bytes / 1024 / 1024 / 1024, 3)
                dataval['snapshots'] = get_file_storage_snapshots(file_storage, fs.id)
                dataval['exports'] = get_file_storage_exports(file_storage, virtual_network, fs.id)
                data.append(dataval)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in oci_file_storage: " + str(e.args))
        pass

##########################################################################
# get_kms_vault_keys
##########################################################################


def get_kms_vault_keys(kms_keys, config, vault, compartment, compartments):
    try:
        data = []

        for c in compartments:
            comp_text = ""
            if c.name != compartment.name:
                comp_text = " (Compartment=" + c.name + ")"
            keys = kms_keys.list_keys(c.id).data

            for key in keys:
                if key.vault_id == vault.id:
                    data.append(str(key.display_name) + " - " + str(key.lifecycle_state) + comp_text)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_kms_vault_keys: " + str(e.args))
        pass

##########################################################################
# KMS
##########################################################################
#
# class oci.key_management.KmsManagementClient(config, **kwargs)
# class oci.key_management.KmsVaultClient(config, **kwargs)
#
##########################################################################


def get_kms_vault_main(kms_vault, config, compartment, compartments):
    try:
        data = []

        vaults = kms_vault.list_vaults(compartment.id).data

        for vault in vaults:  # print details
            dataval = {}
            dataval['vault'] = str(vault.display_name) + " - " + str(vault.vault_type) + " - " + str(vault.lifecycle_state)
            dataval['crypto_endpoint'] = str(vault.crypto_endpoint)
            dataval['management_endpoint'] = str(vault.management_endpoint)

            # get keys
            kms_keys = oci.key_management.KmsManagementClient(config, service_endpoint=vault.management_endpoint)
            kms_keys.base_client.session.proxies = kms_vault.base_client.session.proxies
            dataval['keys'] = get_kms_vault_keys(kms_keys, config, vault, compartment, compartments)

            data.append(dataval)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_kms_vault_main: " + str(e.args))
        pass

##########################################################################
# get pre auth request count
##########################################################################


def get_object_storage_preauthenticated_requests_count(object_storage, namespace_name, bucket_name):
    try:
        retstr = ""
        cnt = len(object_storage.list_preauthenticated_requests(namespace_name, bucket_name).data)

        if cnt > 0:
            retstr = " , " + str(cnt) + " Preauth Requests"
        return retstr

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'BucketNotFound':
            return ""
        raise
    except Exception as e:
        print("Error in get_object_storage_preauthenticated_requests_count: " + str(e.args))
        pass

##########################################################################
# get pre auth request count
##########################################################################


def get_object_storage_object_count(object_storage, namespace_name, bucket_name):
    try:
        bucket = object_storage.get_bucket(namespace_name, bucket_name, fields=['approximateCount', 'approximateSize']).data
        retstr = {}
        cnt = 0
        size = 0
        ssize = 0

        # get info from the approximate fields
        if bucket is not None:
            cnt = bucket.approximate_count
            size = bucket.approximate_size

        if cnt is not None and size is not None:
            scnt = cnt
            ssize = round(size / 1024 / 1024 / 1024, 1)

        retstr = {
            'objects': str(scnt).rjust(8),
            'size': str(ssize).rjust(8),
            'sum_size_gb': str(ssize),
            'sum_info': 'Object Storage - Buckets (gb)'
        }

        return retstr

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'BucketNotFound':
            return {'objects': "** No Permission ** ", 'size': "", 'sum_size_gb': "", 'sum_info': ""}
        raise
    except Exception as e:
        print("Error in get_object_storage_object_count: " + str(e.args))
        pass

##########################################################################
# get_object_lifecycle_policy
##########################################################################


def get_object_storage_object_lifecycle(object_storage, namespace_name, bucket_name):
    try:
        retstr = ""
        lp = object_storage.get_object_lifecycle_policy(namespace_name, bucket_name).data
        if lp:
            for l in lp.items:
                retstr += " , LifeCycle: " + str(l.name) + ", " + str(l.action) + ", " + str(l.time_amount) + " " + str(l.time_unit)

        return retstr

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        # the get_object_lifecycle_policy throw exception if no lifecycle exist
        if e.code == 'LifecyclePolicyNotFound':
            return ""
        if e.code == 'BucketNotFound':
            return ""
        raise
    except Exception as e:
        print("Error in get_object_storage_object_lifecycle: " + str(e.args))
        pass


##########################################################################
# Object Storage
##########################################################################
#
# class oci.object_storage.ObjectStorageClient(config, **kwargs)
#
##########################################################################
def get_object_storage_main(object_storage, compartment):
    try:
        data = []
        namespace_name = object_storage.get_namespace().data
        buckets = oci.pagination.list_call_get_all_results(object_storage.list_buckets, namespace_name, compartment.id).data

        # tbd buckets size
        for bucket in buckets:
            value = []
            value = get_object_storage_object_count(object_storage, namespace_name, bucket.name)
            value['name'] = str(bucket.name)
            value['preauthenticated_requests'] = get_object_storage_preauthenticated_requests_count(object_storage, namespace_name, bucket.name)
            value['object_lifecycle'] = get_object_storage_object_lifecycle(object_storage, namespace_name, bucket.name)
            value['desc'] = (
                str(bucket.name).ljust(24) + " - " +
                value['objects'] + " Objs , " +
                value['size'] + "gb (Approx)" +
                value['object_lifecycle'] +
                value['preauthenticated_requests']
            )
            data.append(value)
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NamespaceNotFound':
            return []
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_object_storage_main: " + str(e.args))
        pass

##########################################################################
# print load balancer backed
##########################################################################


def get_load_balancer_backend(backend, status):

    b = backend
    return (status + " - " + b.ip_address + ":" + str(b.port) + " - "
            "Backup=" + ("Y" if b.backup else "N") + ", " +
            "Drain=" + ("Y" if b.drain else "N") + ", " +
            "Offline=" + ("Y" if b.offline else "N") + ", " +
            "Weight=" + str(b.weight)
            )

##########################################################################
# print load balancer backed
##########################################################################


def get_load_balancer_bs_healthchecker(health_checker, line):

    h = health_checker
    if str(h.protocol) == "TCP":
        if line == 1:
            return ("interval(ms)=" + str(h.interval_in_millis) + ", " +
                    "Timeout(ms)=" + str(h.timeout_in_millis) + ", " +
                    "retries=" + str(h.retries))
        if line == 2:
            return (str(h.port) + "/" + h.protocol)

    # if HTTP
    if str(h.protocol) == "HTTP":
        if line == 1:
            return ("interval(ms)=" + str(h.interval_in_millis) + ", " +
                    "Timeout(ms)=" + str(h.timeout_in_millis) + ", " +
                    "retries=" + str(h.retries))
        if line == 2:
            return (str(h.port) + "/" + h.protocol + ", " +
                    "Code=" + str(h.return_code) + ", " +
                    "RegEx=" + str(h.response_body_regex) + ", " +
                    "url_path =" + str(h.url_path))

##########################################################################
# print load balancer backedset
##########################################################################


def get_load_balancer_backendset(load_balancer, load_balancer_id):

    try:
        data = []
        for bs in oci.pagination.list_call_get_all_results(load_balancer.list_backend_sets, load_balancer_id).data:
            status = load_balancer.get_backend_set_health(load_balancer_id, bs.name).data.status
            dataval = {}

            # check ssl config
            ssl_details = ""
            if bs.ssl_configuration is not None:
                ssl_details = " - Cert: " + str(bs.ssl_configuration.certificate_name)

            dataval['backend_set'] = str(bs.name) + " - " + str(bs.policy) + ssl_details
            dataval['status'] = str(status)

            # list of backends
            databck = []
            for backend in bs.backends:
                bh_status = load_balancer.get_backend_health(load_balancer_id, bs.name, backend.name).data.status
                databck.append(get_load_balancer_backend(backend, bh_status))

            dataval['backends'] = databck

            # Health Checker
            datahealth = []
            datahealth.append(get_load_balancer_bs_healthchecker(bs.health_checker, 1))
            datahealth.append(get_load_balancer_bs_healthchecker(bs.health_checker, 2))
            dataval['health_check'] = datahealth

            # session_persistence_configuration
            if bs.session_persistence_configuration is not None:
                dataval['session_persistence'] = str(bs.session_persistence_configuration.cookie_name) + ", " + "disable_fallback=" + \
                    ("Y" if bs.session_persistence_configuration.disable_fallback else "N")

            # ssl_configuration
            if bs.ssl_configuration is not None:
                dataval['ssl_cert'] = (str(bs.ssl_configuration.certificate_name) + ", " +
                                       "VerifyPeer=" + ("Y" if bs.ssl_configuration.verify_peer_certificate else "N") + ", " +
                                       "VerifyDepth=" + str(bs.ssl_configuration.verify_depth)
                                       )
            data.append(dataval)

        # return the data
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in print_load_balancer_backendset: " + str(e.args))
        pass


##########################################################################
# print load balancer config
##########################################################################
def get_load_balancer_details(virtual_network, load_balance_obj, status):
    try:
        data = {}
        lb = load_balance_obj
        data['name'] = str(lb.display_name) + " - " + str(lb.shape_name) + " - " + ("(Private)" if lb.is_private else "(Public)") + " - " + str(lb.lifecycle_state)
        data['status'] = str(status)

        # subnets
        datasub = []
        for subnet in lb.subnet_ids:
            datasub.append(get_core_network_subnet(virtual_network, subnet))
        data['subnets'] = datasub

        # ip_addresses
        dataips = []
        for ip in lb.ip_addresses:
            dataips.append(str(ip.ip_address) + " - " + ("Public" if ip.is_public else "Private"))
        data['ips'] = dataips

        # listeners
        datalis = []
        for listener in lb.listeners:
            lo = lb.listeners[listener]

            # check ssl config
            ssl_details = ""
            if lo.ssl_configuration is not None:
                ssl_details = " - Cert: " + str(lo.ssl_configuration.certificate_name)

            # add data
            datalis.append(listener + " - " + str(lo.port) + "/" + str(lo.protocol) + ssl_details + " - Default BS: " + str(lo.default_backend_set_name))
        data['listeners'] = datalis

        # Path route set - need to test -  TBD
        datapath = []
        for prs in lb.path_route_sets:
            pro = lb.path_route_sets[prs]
            datapath.append({'name': pro.name, 'path_routes': pro.path_routes})
        data['path_route'] = datapath

        # Hostnames
        datahosts = []
        for hostname in lb.hostnames:
            ho = lb.hostnames[hostname]
            datahosts.append(str(ho.name) + " - " + str(ho.hostname))
        data['hostnames'] = datahosts

        return data
    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_load_balancer_details: " + str(e.args))
        pass


##########################################################################
# Load Balancer
##########################################################################
#
# class oci.load_balancer.LoadBalancerClient(config, **kwargs)
#
##########################################################################
def get_load_balancer_main(load_balancer, virtual_network, compartment):
    try:
        data = []
        load_balancers = oci.pagination.list_call_get_all_results(load_balancer.list_load_balancers, compartment.id, sort_by="DISPLAYNAME").data

        for load_balance_obj in load_balancers:
            dataval = {}
            status = load_balancer.get_load_balancer_health(load_balance_obj.id).data.status
            dataval['sum_info'] = "Load Balancer " + str(load_balance_obj.shape_name)
            dataval['details'] = get_load_balancer_details(virtual_network, load_balance_obj, status)
            dataval['backendset'] = get_load_balancer_backendset(load_balancer, load_balance_obj.id)
            data.append(dataval)

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_load_balancer_main: " + str(e.args))
        pass

##########################################################################
# Load Balancer
##########################################################################
#
# class oci.resource_management.ResourceManagerClient(config, **kwargs)
#
##########################################################################


def get_resource_management_main(orm, compartment):
    try:
        data = []
        stacks = oci.pagination.list_call_get_all_results(orm.list_stacks, compartment_id=compartment.id, lifecycle_state="ACTIVE", sort_by="DISPLAYNAME").data

        # query the stacks
        for stack in stacks:
            dataval = {}
            dataval['stack_name'] = str(stack.display_name) + " - " + str(stack.description)

            # query jobs
            jobs = oci.pagination.list_call_get_all_results(orm.list_jobs, stack_id=stack.id, sort_by="TIMECREATED").data
            datajob = []
            for job in jobs:
                datajob.append(
                    str(job.display_name) + " - " +
                    str(job.operation).ljust(10) + " - " +
                    str(job.lifecycle_state).ljust(10) + " - " +
                    str(job.time_finished)[0:16]
                )

            # add the jobs to the array
            dataval['jobs'] = datajob
            data.append(dataval)

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_resource_management_main: " + str(e.args))
        pass


##########################################################################
# Email
##########################################################################
#
# class oci.email.EmailClient(config, **kwargs)
#
##########################################################################
def get_email_main(email, compartment, tenancy):
    try:
        senders = oci.pagination.list_call_get_all_results(email.list_senders, compartment.id, sort_by="EMAILADDRESS").data
        suppressions = []

        # suppressions is only valid in root compartment
        if compartment.id == tenancy.id:
            suppressions = email.list_suppressions(compartment.id).data

        if len(senders) == 0 and len(suppressions) == 0:
            return

        data = {}

        # Senders
        if len(senders) > 0:
            data_sender = []
            for sender in senders:
                data_sender.append(str(sender.email_address) + " - " + str(sender.lifecycle_state))
            data['senders'] = data_sender

        # Suppression
        if len(suppressions) > 0:
            data_supp = []
            for suppression in suppressions:
                data_supp.append(str(suppression.email_address) + " - " + str(suppression.reason))
            data['supp_list'] = data_supp

        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError as e:
        if e.code == 'NotAuthorized':
            return []
        if e.code == 'NotAuthorizedOrNotFound':
            return []
        raise
    except Exception as e:
        print("Error in get_email_main: " + str(e))
        pass

##########################################################################
# run on Region
##########################################################################


def get_oci_region_data(cmd, config, region_name):

    print("\nExtracting Region " + region_name)

    config["region"] = region_name

    try:
        virtual_network = oci.core.VirtualNetworkClient(config)
        compute = oci.core.ComputeClient(config)
        computeManage = oci.core.ComputeManagementClient(config)
        block_storage = oci.core.BlockstorageClient(config)
        file_storage = oci.file_storage.FileStorageClient(config)
        object_storage = oci.object_storage.ObjectStorageClient(config)
        database = oci.database.DatabaseClient(config)
        identity = oci.identity.IdentityClient(config)
        load_balancer = oci.load_balancer.LoadBalancerClient(config)
        email = oci.email.EmailClient(config)
        kms_vault = oci.key_management.KmsVaultClient(config)
        orm = oci.resource_manager.ResourceManagerClient(config)

        if cmd.proxy:
            identity       .base_client.session.proxies = {'https': cmd.proxy}
            virtual_network.base_client.session.proxies = {'https': cmd.proxy}
            compute        .base_client.session.proxies = {'https': cmd.proxy}
            computeManage  .base_client.session.proxies = {'https': cmd.proxy}
            block_storage  .base_client.session.proxies = {'https': cmd.proxy}
            file_storage   .base_client.session.proxies = {'https': cmd.proxy}
            object_storage .base_client.session.proxies = {'https': cmd.proxy}
            database       .base_client.session.proxies = {'https': cmd.proxy}
            load_balancer  .base_client.session.proxies = {'https': cmd.proxy}
            email          .base_client.session.proxies = {'https': cmd.proxy}
            kms_vault      .base_client.session.proxies = {'https': cmd.proxy}
            orm            .base_client.session.proxies = {'https': cmd.proxy}

        # load tenancy
        tenancy = identity.get_tenancy(config["tenancy"]).data

        # initialilze the jsob return variable
        ret_var = []

        # Loop on Compartments and call services
        compartments = get_compartments_with_root(identity, tenancy, cmd)

        for compartment in compartments:

            #  check if to skip ManagedCompartmentForPaaS
            if compartment.name == "ManagedCompartmentForPaaS" and not cmd.mgdcompart:
                continue

            print("    Compartment " + compartment.path + "...")
            data = {}
            data['compartment'] = compartment.name
            data['path'] = compartment.path
            has_data = False

            # run on network module
            if cmd.all or cmd.allnoiam or cmd.network:
                value = get_core_network_main(virtual_network, compartment, compartments)
                if value:
                    data['network'] = value
                    has_data = True

            # run on compute and block storage
            if cmd.all or cmd.allnoiam or cmd.compute:
                value = get_core_compute_main(compute, computeManage, block_storage, virtual_network, compartment, compartments)
                if value:
                    data['compute'] = value
                    has_data = True

            # run on database
            if cmd.all or cmd.allnoiam or cmd.database:
                value = get_database_main(database, virtual_network, compartment)
                if value:
                    data['database'] = value
                    has_data = True

            # run on file_storage
            if cmd.all or cmd.allnoiam or cmd.file:
                value = get_file_storage_main(file_storage, identity, virtual_network, compartment)
                if value:
                    data['file_storage'] = value
                    has_data = True

            # run on kms
            if cmd.all or cmd.allnoiam or cmd.kms:
                value = get_kms_vault_main(kms_vault, config, compartment, compartments)
                if value:
                    data['kms'] = value
                    has_data = True

            # run on object storage
            if cmd.all or cmd.allnoiam or cmd.object:
                value = get_object_storage_main(object_storage, compartment)
                if value:
                    data['object_storage'] = value
                    has_data = True

            # run on Load Balancer
            if cmd.all or cmd.allnoiam or cmd.load:
                value = get_load_balancer_main(load_balancer, virtual_network, compartment)
                if value:
                    data['load_balancer'] = value
                    has_data = True

            # run on Resource Management
            if cmd.all or cmd.allnoiam or cmd.orm:
                value = get_resource_management_main(orm, compartment)
                if value:
                    data['resource_management'] = value
                    has_data = True

            # email only supported @ US regions
            if (region_name == "us-ashburn-1" or region_name == "us-phoenix-1"):
                if cmd.all or cmd.allnoiam or cmd.email:
                    value = get_email_main(email, compartment, tenancy)
                    if value is not None:
                        data['email'] = value
                        has_data = True

            # add the data to main Variable
            if has_data:
                ret_var.append(data)

        print("")

        # return var
        return ret_var

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        print("Error in get_oci_region_data: " + str(e.args))
        pass

##########################################################################
# run on Region
##########################################################################


def get_oci_main_data(cmd, config):

    data = []

    # check if to loop the compartments
    # if one of the areas marked for extract
    run_on_compartments = (
        cmd.all or cmd.network or
        cmd.compute or cmd.database or
        cmd.file or cmd.object or
        cmd.load or cmd.email or cmd.allnoiam or cmd.kms or cmd.orm
    )

    # append version to json
    version_data = get_version(cmd)
    data.append(version_data)

    # print data
    print_showoci_data(version_data['data'])
    print_header("Start Extracting Data", 1)

    try:
        tenancy_id = config["tenancy"]

        # Load Identity
        identity = oci.identity.IdentityClient(config)
        if cmd.proxy:
            identity.base_client.session.proxies = {'https': cmd.proxy}

        # run identity
        if (cmd.all or cmd.identity):
            identity_data = {}
            identity_data['type'] = "identity"
            identity_data['data'] = get_identity_main(identity, tenancy_id, cmd.mgdcompart, cmd)
            data.append(identity_data)

        if run_on_compartments:
            # if filter by region - print message
            if cmd.region:
                print("Filtered by Region=" + str(cmd.region))

            # run on each subscribed region
            for region in identity.list_region_subscriptions(tenancy_id).data:

                # if filtered by region skip if not cmd.region
                if cmd.region and str(cmd.region) != str(region.region_name):
                    continue

                # execute the region
                value = get_oci_region_data(cmd, config, region.region_name)

                # if data returns, add to the json
                if value:
                    region_data = ({'type': "region", 'region': region.region_name, 'data': value})
                    data.append(region_data)

        # return the json data
        return data

    except oci.exceptions.RequestException:
        raise
    except oci.exceptions.ServiceError:
        raise
    except Exception as e:
        raise Exception("Error in get_oci_main_data: " + str(e))

##########################################################################
# set parser
##########################################################################


def set_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', action='store_true', default=False, dest='all', help='Print All Resources')
    parser.add_argument('-ani', action='store_true', default=False, dest='allnoiam', help='Print All Resources but identity')
    parser.add_argument('-n', action='store_true', default=False, dest='network', help='Print Network')
    parser.add_argument('-i', action='store_true', default=False, dest='identity', help='Print Identity')
    parser.add_argument('-c', action='store_true', default=False, dest='compute', help='Print Compute')
    parser.add_argument('-o', action='store_true', default=False, dest='object', help='Print Object Storage')
    parser.add_argument('-l', action='store_true', default=False, dest='load', help='Print Load Balancer')
    parser.add_argument('-k', action='store_true', default=False, dest='kms', help='Print Key Management')
    parser.add_argument('-d', action='store_true', default=False, dest='database', help='Print Database')
    parser.add_argument('-f', action='store_true', default=False, dest='file', help='Print File Storage')
    parser.add_argument('-e', action='store_true', default=False, dest='email', help='Print EMail')
    parser.add_argument('-rm', action='store_true', default=False, dest='orm', help='Print Resource management')
    parser.add_argument('-so', action='store_true', default=False, dest='sumonly', help='Print Summary Only')
    parser.add_argument('-ocid', action='store_true', default=False, dest='ocid', help='Include OCIDs in Json File')
    parser.add_argument('-mc', action='store_true', default=False, dest='mgdcompart', help='Include ManagedCompartmentForPaaS')
    parser.add_argument('-nr', action='store_true', default=False, dest='noroot', help='Not include root compartment')
    parser.add_argument('-t', default="", dest='profile', help='Config file section to use (tenancy profile)')
    parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
    parser.add_argument('-rg', default="", dest='region', help='Filter by Region')
    parser.add_argument('-cp', default="", dest='compart', help='Filter by Compartment')
    parser.add_argument('-cf', type=argparse.FileType('r'), dest='config', help="Config File, default=" + str(config_file))
    parser.add_argument('-jf', type=argparse.FileType('w'), dest='joutfile', help="Output to file   (JSON format)")
    parser.add_argument('-js', action='store_true', default=False, dest='joutscr', help="Output to screen (JSON format)")
    parser.add_argument('--version', action='version', version='%(prog)s ' + version)

    result = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        return None

    if not (result.all or result.allnoiam or result.network or result.identity or
            result.compute or result.object or result.kms or
            result.load or result.database or result.file or result.email or result.orm):
        print("")
        print("*************************************************************")
        print("*** You must choose at least one parameter for extract !! ***")
        print("*************************************************************")
        print("")
        parser.print_help()
        return None

    return result

##########################################################################
# execute_extract
##########################################################################


def execute_extract():

    # get parset cmd
    cmd = set_parser()
    if cmd is None:
        return

    # if include ocid - set main ocid param to true
    global ocid
    if cmd.ocid:
        ocid = True

    # get config file - use global parameter config_file
    global config_file
    if cmd.config:
        if cmd.config.name:
            config_file = cmd.config.name

    # config section - use global parameter config_section
    global config_section
    config_section = "DEFAULT"
    if cmd.profile:
        config_section = cmd.profile

    config = oci.config.from_file(config_file, config_section)

    # extract the data
    data = get_oci_main_data(cmd, config)

    # if write to json
    if cmd.joutfile:
        if cmd.joutfile.name:
            json_file_name = cmd.joutfile.name
            with open(json_file_name, 'w') as outfile:
                json.dump(data, outfile, indent=4, sort_keys=False)
            print("Data has been exported to " + json_file_name)

    # print to JSON screen
    elif cmd.joutscr:
        print(json.dumps(data, indent=4, sort_keys=False))

    # print summary only
    elif cmd.sumonly:
        summary_oci_main(data, False)

    # print default to screen
    else:
        print_oci_main(data, False)
        summary_oci_main(data, False)

##########################################################################
# check oci version
##########################################################################


def check_oci_version():

    # loop on digits
    for i, rl in zip(oci_installed_version.split("."), oci_min_version.split(".")):
        if i > rl:
            return True
        if i < rl:
            print("Error, OCI version required = " + oci_min_version + ", OCI Version installed=" + oci_installed_version)
            print("Aboting.")
            return False
    return True


##########################################################################
# Main
##########################################################################
if check_oci_version():
    execute_extract()
