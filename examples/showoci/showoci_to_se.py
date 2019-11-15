#!/usr/bin/env python3
###########################################################################
# Copyright(c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# showoci_to_se.py
#
# @author base: Adi Zohar
#
# Supports Python 3 and above
#
# coding: utf-8
#
# convert showoci JSON to simple JSON format
# to allow user to convert showoci JSON to simple format
#
##########################################################################
# usage: showoci_to_se.py [-h] [-i INPUT] [-o OUTPUT] [-s]
#
# optional arguments:
#   -h, --help  show this help message and exit
#   -i INPUT    Input JSON File
#   -o OUTPUT   Output JSON File
#   -s          Output to screen (JSON format)
#
# Example Execution:
# $ showoci_to_se.py -i showoci.json -o simple.json
#
##########################################################################
# ShowOCI2SE class
##########################################################################
from __future__ import print_function
import json
import argparse
import sys


#######################################################################################################################
# This section has ShowOCI2SE class
# it accept data as JSON format and compile short JSON
#######################################################################################################################
class ShowOCI2SE(object):

    ############################################
    # class variables
    ############################################
    outdata = []

    ############################################
    # interator for the classes as requested by
    # Xuan
    ############################################
    NetworkVcnId = 0
    NetworkCpeId = 0
    NetworkDrgId = 0
    NetworkIPSecId = 0
    NetworkRPCId = 0
    NetworkVCId = 0
    NetworkSubnetId = 0
    NetworkSecListId = 0
    NetworkSecGroupId = 0
    NetworkDHCPId = 0
    NetworkRouteId = 0
    DatabaseId = 0
    ComputeId = 0
    LoadBalancerId = 0
    ResourceManagementId = 0
    StreamId = 0
    EmailId = 0
    ContainerId = 0
    MonitorId = 0
    NotificationId = 0
    EdgeHealthHttpId = 0
    EdgeHealthPingId = 0
    QuotaId = 0
    FileStorageId = 0
    LoadBalancerListenerId = 0
    LoadBalancerBackendsetId = 0
    BucketId = 0

    ############################################
    # Init
    ############################################
    def __init__(self):
        pass

    ##########################################################################
    # generate_csv
    ##########################################################################
    def convert_json(self, data):

        try:
            for d in data:
                if 'type' in d:

                    if d['type'] == "identity":
                        self.__convert_identity_main(d['data'])

                    elif d['type'] == "region":
                        self.__convert_region_data(d['region'], d['data'])

                    else:
                        continue

            # return
            return self.outdata

        except Exception as e:
            raise Exception("Error in convert_json: " + str(e.args))

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
    # check if managed paas compartment
    ##########################################################################
    def __if_managed_paas_compartment(self, name):
        return name == "ManagedCompartmentForPaaS"

    ##########################################################################
    # Identity Groups
    ##########################################################################
    def __convert_identity_tenancy(self, tenancy):
        try:
            data = {'type': 'Tenancy',
                    'name': tenancy['name'],
                    'id': tenancy['id'],
                    'subscribe_regions': tenancy['subscribe_regions'],
                    'home_region_key': tenancy['home_region_key']}
            self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_identity_compartmentss", e)

    ##########################################################################
    # Identity Groups
    ##########################################################################
    def __convert_identity_compartments(self, compartments):
        try:
            for c in compartments:
                data = {'class': 'Compartment', 'name': c['name'], 'path': c['path']}
                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_identity_compartments", e)

    ##########################################################################
    # Identity Groups
    ##########################################################################
    def __convert_identity_groups(self, groups):
        try:
            for group in groups:
                for user in group['users'].split(','):

                    data = {'type': 'IdentityGroup', 'group_name': group['name'], 'user_name': user}

                    self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_identity_groups", e)

    ##########################################################################
    # convert Identity Policies
    ##########################################################################
    def __convert_identity_policies(self, policies_data):
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
                        self.outdata.append({'type': 'IdentityPolicy', 'compartment': c['compartment_path'], 'policy_name': policy['name'], 'seq': seq, 'statement': statement})

        except Exception as e:
            self.__print_error("__convert_identity_policies", e)

    ##########################################################################
    # convert Identity Module
    ##########################################################################
    def __convert_identity_main(self, data):
        try:
            if 'tenancy' in data:
                self.__convert_identity_tenancy(data['tenancy'])

            if 'compartments' in data:
                self.__convert_identity_compartments(data['compartments'])

            if 'groups' in data:
                self.__convert_identity_groups(data['groups'])

            if 'policies' in data:
                self.__convert_identity_policies(data['policies'])

        except Exception as e:
            self.__print_error("__convert_identity_main", e)

    ##########################################################################
    # convert Network Subnets
    ##########################################################################
    def __convert_core_network_vcn_subnet(self, region_name, subnets, vcn):
        try:
            for subnet in subnets:
                self.NetworkSubnetId += 1
                data = {'class': 'NetworkSubnet' + str(self.NetworkSubnetId),
                        'region_name': region_name,
                        'vcn_id': vcn['id'],
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': vcn['cidr_block'],
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_id': vcn['compartment_id'],
                        'subnet_id': subnet['id'],
                        'subnet_name': subnet['name'],
                        'subnet_cidr': subnet['cidr_block'],
                        'availability_domain': subnet['availability_domain'],
                        'subnet_compartment': subnet['compartment_name'],
                        'subnet_compartment_id': subnet['compartment_id'],
                        'public_private': subnet['public_private'],
                        'dhcp_options': subnet['dhcp_options'],
                        'route': subnet['route'],
                        'security_list': str(', '.join(x for x in subnet['security_list'])),
                        'dns': subnet['dns']}
                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_core_network_vcn_subnet", e)

    ##########################################################################
    # Print Network vcn security list
    ##########################################################################
    def __convert_core_network_vcn_security_lists(self, region_name, sec_lists, vcn):
        try:
            if not sec_lists:
                return

            for sl in sec_lists:
                if len(sl['sec_rules']) == 0:
                    self.NetworkSecListId += 1
                    data = {'class': 'NetworkSecList' + str(self.NetworkSecListId),
                            'region_name': region_name,
                            'vcn_id': vcn['id'],
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_id': vcn['compartment_id'],
                            'sec_name': sl['name'],
                            'sec_id': sl['id'],
                            'sec_compartment': sl['compartment_name'],
                            'sec_compartment_id': sl['compartment_id'],
                            'time_created': sl['time_created'][0:16],
                            'sec_protocol': "",
                            'sec_is_stateless': "",
                            'sec_source': "",
                            'sec_src_port_min': "",
                            'sec_src_port_max': "",
                            'sec_destination': "",
                            'sec_dst_port_min': "",
                            'sec_dst_port_max': "",
                            'sec_icmp_code': "",
                            'sec_icmp_type': ""}
                    self.outdata.append(data)

                else:
                    self.NetworkSecListId += 1
                    for slr in sl['sec_rules']:
                        data = {'class': 'NetworkSecList' + str(self.NetworkSecListId),
                                'region_name': region_name,
                                'vcn_id': vcn['id'],
                                'vcn_name': vcn['display_name'],
                                'vcn_cidr': vcn['cidr_block'],
                                'vcn_compartment': vcn['compartment_name'],
                                'vcn_compartment_id': vcn['compartment_id'],
                                'sec_name': sl['name'],
                                'sec_id': sl['id'],
                                'sec_compartment': sl['compartment_name'],
                                'sec_compartment_id': sl['compartment_id'],
                                'time_created': sl['time_created'][0:16],
                                'sec_protocol': slr['protocol_name'],
                                'sec_is_stateless': slr['is_stateless'],
                                'sec_source': slr['source'],
                                'sec_src_port_min': slr['src_port_min'],
                                'sec_src_port_max': slr['src_port_max'],
                                'sec_destination': slr['destination'],
                                'sec_dst_port_min': slr['dst_port_min'],
                                'sec_dst_port_max': slr['dst_port_max'],
                                'sec_icmp_code': slr['icmp_code'],
                                'sec_icmp_type': slr['icmp_type']
                                }
                        self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_core_network_vcn_security_lists", e)

    ##########################################################################
    # Print Network vcn security groups
    ##########################################################################

    def __convert_core_network_vcn_security_groups(self, region_name, sec_groups, vcn):
        try:
            if not sec_groups:
                return

            for sl in sec_groups:
                if len(sl['sec_rules']) == 0:
                    self.NetworkSecGroupId += 1
                    data = {'class': 'NetworkSecGroup' + str(self.NetworkSecGroupId),
                            'region_name': region_name,
                            'vcn_id': vcn['id'],
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_id': vcn['compartment_id'],
                            'sec_id': sl['id'],
                            'sec_name': sl['name'],
                            'sec_compartment': sl['compartment_name'],
                            'sec_compartment_id': sl['compartment_id'],
                            'time_created': sl['time_created'][0:16],
                            'sec_description': "",
                            'sec_direction': "",
                            'sec_protocol': "",
                            'sec_is_stateless': "",
                            'sec_is_valid': "",
                            'sec_destination': "",
                            'sec_destination_name': "",
                            'sec_destination_type': "",
                            'sec_source': "",
                            'sec_source_name': "",
                            'sec_source_type': "",
                            'sec_src_port_min': "",
                            'sec_src_port_max': "",
                            'sec_dst_port_min': "",
                            'sec_dst_port_max': "",
                            'sec_icmp_code': "",
                            'sec_icmp_type': ""}

                    self.outdata.append(data)

                else:
                    self.NetworkSecListId += 1
                    for slr in sl['sec_rules']:
                        data = {'class': 'NetworkSecGroup' + str(self.NetworkSecListId),
                                'region_name': region_name,
                                'vcn_id': vcn['id'],
                                'vcn_name': vcn['display_name'],
                                'vcn_cidr': vcn['cidr_block'],
                                'vcn_compartment': vcn['compartment_name'],
                                'vcn_compartment_id': vcn['compartment_id'],
                                'sec_id': sl['id'],
                                'sec_name': sl['name'],
                                'sec_compartment': sl['compartment_name'],
                                'sec_compartment_id': sl['compartment_id'],
                                'time_created': sl['time_created'],
                                'sec_description': slr['description'],
                                'sec_direction': slr['direction'],
                                'sec_protocol': slr['protocol_name'],
                                'sec_is_stateless': slr['is_stateless'],
                                'sec_is_valid': slr['is_valid'],
                                'sec_destination': slr['destination'],
                                'sec_destination_name': slr['destination_name'],
                                'sec_destination_type': slr['destination_type'],
                                'sec_source': slr['source'],
                                'sec_source_name': slr['source_name'],
                                'sec_source_type': slr['source_type'],
                                'sec_src_port_min': slr['src_port_min'],
                                'sec_src_port_max': slr['src_port_max'],
                                'sec_dst_port_min': slr['dst_port_min'],
                                'sec_dst_port_max': slr['dst_port_max'],
                                'sec_icmp_code': slr['icmp_code'],
                                'sec_icmp_type': slr['icmp_type'],
                                }
                        self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_core_network_vcn_security_lists", e)

    ##########################################################################
    # convert DHCP options for DHCP_ID
    ##########################################################################

    def __convert_core_network_vcn_dhcp_options(self, region_name, dhcp_options, vcn):
        try:
            for dhcp in dhcp_options:
                self.NetworkDHCPId += 1
                data = {'class': 'NetworkDHCP' + str(self.NetworkDHCPId),
                        'region_name': region_name,
                        'vcn_id': vcn['id'],
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': vcn['cidr_block'],
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_id': vcn['compartment_id'],
                        'dhcp_name': dhcp['name'],
                        'option_1': "",
                        'option_2': "",
                        'dhcp_compartment': dhcp['compartment_name'],
                        'dhcp_compartment_id': dhcp['compartment_id'],
                        'time_created': dhcp['time_created'][0:16]}

                seq = 0
                for opt in dhcp['opt']:
                    seq += 1
                    opt_str = "option_" + str(seq)
                    data[opt_str] = opt

                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_core_network_vcn_dhcp_options", e)

    ########################################################################
    # convert Network vcn Route Tables
    ##########################################################################
    def __convert_core_network_vcn_route_tables(self, region_name, route_tables, vcn):
        try:
            if not route_tables:
                return

            for rt in route_tables:

                if len(rt['route_rules']) == 0:
                    self.NetworkRouteId += 1
                    data = {'class': 'NetworkRoute' + str(self.NetworkRouteId),
                            'region_name': region_name,
                            'vcn_id': vcn['id'],
                            'vcn_name': vcn['display_name'],
                            'vcn_cidr': vcn['cidr_block'],
                            'vcn_compartment': vcn['compartment_name'],
                            'vcn_compartment_id': vcn['compartment_id'],
                            'route_name': rt['name'],
                            'route_compartment': rt['compartment_name'],
                            'route_compartment_id': rt['compartment_id'],
                            'destination': "",
                            'route': "Empty",
                            'time_created': rt['time_created'][0:16]}
                    self.outdata.append(data)

                else:
                    for rl in rt['route_rules']:
                        self.NetworkRouteId += 1
                        data = {'class': 'NetworkRoute' + str(self.NetworkRouteId),
                                'region_name': region_name,
                                'vcn_id': vcn['id'],
                                'vcn_name': vcn['display_name'],
                                'vcn_cidr': vcn['cidr_block'],
                                'vcn_compartment': vcn['compartment_name'],
                                'vcn_compartment_id': vcn['compartment_id'],
                                'route_name': rt['name'],
                                'route_ocid': rt['id'],
                                'route_compartment': rt['compartment_name'],
                                'route_compartment_id': rt['compartment_id'],
                                'network_entity_id': rl['network_entity_id'],
                                'destination': rl['destination'],
                                'route': rl['desc'],
                                'time_created': rt['time_created'][0:16]}
                        self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_core_network_vcn_route_tables", e)

    ##########################################################################
    # convert network vcn
    ##########################################################################
    def __convert_core_network_vcn(self, region_name, vcns):

        try:
            if len(vcns) == 0:
                return

            for vcn in vcns:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(vcn['compartment_name']):
                    continue

                igw = ""
                igw_id = ""
                sgw = ""
                sgw_id = ""
                nat = ""
                nat_id = ""
                drg = ""
                lpg = ""

                if 'igw' in vcn['data']:
                    igw = str(', '.join(x['name'] for x in vcn['data']['igw']))
                    igw_id = str(', '.join(x['id'] for x in vcn['data']['igw']))

                if 'sgw' in vcn['data']:
                    sgw = str(', '.join(x['name'] + " " + x['services'] for x in vcn['data']['sgw']))
                    sgw_id = str(', '.join(x['id'] for x in vcn['data']['sgw']))

                if 'nat' in vcn['data']:
                    nat = str(', '.join(x['name'] for x in vcn['data']['nat']))
                    nat_id = str(', '.join(x['id'] for x in vcn['data']['nat']))

                if 'drg_attached' in vcn['data']:
                    drg = str(', '.join(x['name'] for x in vcn['data']['drg_attached']))

                if 'local_peering' in vcn['data']:
                    lpg = vcn['data']['local_peering']

                self.NetworkVcnId += 1
                data = {'class': 'NetworkVcn' + str(self.NetworkVcnId),
                        'region_name': region_name,
                        'vcn_name': vcn['display_name'],
                        'vcn_cidr': vcn['cidr_block'],
                        'vcn_compartment': vcn['compartment_name'],
                        'vcn_compartment_id': vcn['compartment_id'],
                        'vcn_id': vcn['id'],
                        'internet_gateway': igw,
                        'igw_id': igw_id,
                        'service_gateway': sgw,
                        'service_gateway_id': sgw_id,
                        'nat': nat,
                        'nat_id': nat_id,
                        'drg': drg,
                        'local_peering': lpg
                        }
                self.outdata.append(data)

                # get subnet related data
                if 'subnets' in vcn['data']:
                    self.__convert_core_network_vcn_subnet(region_name, vcn['data']['subnets'], vcn)

                if 'security_lists' in vcn['data']:
                    self.__convert_core_network_vcn_security_lists(region_name, vcn['data']['security_lists'], vcn)

                if 'security_groups' in vcn['data']:
                    self.__convert_core_network_vcn_security_groups(region_name, vcn['data']['security_groups'], vcn)

                if 'route_tables' in vcn['data']:
                    self.__convert_core_network_vcn_route_tables(region_name, vcn['data']['route_tables'], vcn)

                if 'dhcp_options' in vcn['data']:
                    self.__convert_core_network_vcn_dhcp_options(region_name, vcn['data']['dhcp_options'], vcn)

        except BaseException as e:
            self.__print_error("__convert_core_network_vcn", e)

    ##########################################################################
    # convert network cpe
    ##########################################################################
    def __convert_core_network_cpe(self, region_name, cpes):

        try:
            if len(cpes) == 0:
                return

            for cpe in cpes:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(cpe['compartment_name']):
                    continue

                self.NetworkCpeId += 1
                data = {'class': "NetworkCpe" + str(self.NetworkCpeId),
                        'region_name': region_name,
                        'display_name': cpe['display_name'],
                        'ip_address': cpe['ip_address'],
                        'time_created': cpe['time_created'],
                        'compartment_name': cpe['compartment_name'],
                        'compartment_id': cpe['compartment_id']
                        }
                data.update(cpe)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_core_network_cpe", e)

    ##########################################################################
    # convert network drg
    ##########################################################################
    def __convert_core_network_drg(self, region_name, drgs):

        try:
            if len(drgs) == 0:
                return

            for drg in drgs:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(drg['compartment_name']):
                    continue

                self.NetworkDrgId += 1
                data = {'class': "NetworkDrg" + str(self.NetworkDrgId)}
                data.update(drg)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_core_network_drg", e)

    ##########################################################################
    # convert network ipsec
    ##########################################################################

    def __convert_core_network_ipsec(self, region_name, ipsecs):

        try:
            if len(ipsecs) == 0:
                return

            for ipsec in ipsecs:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(ipsec['compartment_name']):
                    continue

                self.NetworkIPSecId += 1
                data = {'class': "NetworkIPSec" + str(self.NetworkIPSecId)}
                data.update(ipsec)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_core_network_ipsec", e)

    ##########################################################################
    # convert virtual circuit
    ##########################################################################

    def __convert_core_network_virtual_circuit(self, region_name, virtual_circuits):

        try:
            if len(virtual_circuits) == 0:
                return

            for virtual_circuit in virtual_circuits:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(virtual_circuit['compartment_name']):
                    continue

                self.NetworkVCId += 1
                data = {'class': "NetworkVC" + str(self.NetworkVCId)}
                data.update(virtual_circuit)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_core_network_virtual_circuit", e)

    ##########################################################################
    # convert network ipsec
    ##########################################################################

    def __convert_core_network_remote_peering(self, region_name, remote_peerings):

        try:
            if len(remote_peerings) == 0:
                return

            for remote_peering in remote_peerings:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(remote_peering['compartment_name']):
                    continue

                self.NetworkRPCId += 1
                data = {'class': "NetworkRPC" + str(self.NetworkRPCId)}
                data.update(remote_peering)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_core_network_remote_peering", e)

    ##########################################################################
    # convert network Main
    ##########################################################################
    def __convert_core_network_main(self, region_name, data):
        try:
            if 'vcn' in data:
                self.__convert_core_network_vcn(region_name, data['vcn'])
            if 'cpe' in data:
                self.__convert_core_network_cpe(region_name, data['cpe'])
            if 'drg' in data:
                self.__convert_core_network_drg(region_name, data['drg'])
            if 'ipsec' in data:
                self.__convert_core_network_ipsec(region_name, data['ipsec'])
            if 'virtual_circuit' in data:
                self.__convert_core_network_virtual_circuit(region_name, data['virtual_circuit'])
            if 'remote_peering' in data:
                self.__convert_core_network_remote_peering(region_name, data['remote_peering'])

        except Exception as e:
            self.__print_error("__convert_core_network_main", e)

    ##########################################################################
    # convert database db systems
    ##########################################################################
    def __convert_database_db_system(self, region_name, list_db_systems):

        try:
            for dbs in list_db_systems:

                for db_home in dbs['db_homes']:

                    for db in db_home['databases']:
                        self.DatabaseId += 1
                        data = {'class': 'Database' + str(self.DatabaseId),
                                'region_name': region_name,
                                'availability_domain': dbs['availability_domain'],
                                'compartment_name': dbs['compartment_name'],
                                'compartment_id': dbs['compartment_id'],
                                'status': dbs['lifecycle_state'],
                                'type': "DBSystem",
                                'name': dbs['display_name'],
                                'shape': dbs['shape'],
                                'cpu_core_count': dbs['cpu_core_count'],
                                'db_storage_gb': dbs['sum_size_gb'],
                                'shape_ocpus': dbs['shape_ocpu'],
                                'memory_gb': dbs['shape_memory_gb'],
                                'local_storage_tb': dbs['shape_storage_tb'],
                                'license_model': dbs['license_model'],
                                'node_count': len(dbs['db_nodes']),
                                'database': db['name'],
                                'database_version': dbs['database_version'],
                                'database_edition': dbs['database_edition'],
                                'database_edition_short': dbs['database_edition_short'],
                                'host': dbs['host'],
                                'domain': dbs['domain'],
                                'data_subnet': dbs['data_subnet'],
                                'data_subnet_id': dbs['data_subnet_id'],
                                'backup_subnet': dbs['backup_subnet'],
                                'backup_subnet_id': ("" if dbs['backup_subnet_id'] == "None" else dbs['backup_subnet_id']),
                                'scan_ips': str(', '.join(x for x in dbs['scan_ips'])),
                                'vip_ips': str(', '.join(x for x in dbs['vip_ips'])),
                                'cluster_name': dbs['cluster_name'],
                                'time_created': dbs['time_created'][0:16],
                                'db_nodes': str(', '.join(x['desc'] for x in dbs['db_nodes'])),
                                'nsg_names': str(', '.join(x['nsg_names'] for x in dbs['db_nodes']))
                                }
                        self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_database_db_system", e)

    ##########################################################################
    # convert database db system
    ##########################################################################

    def __convert_database_db_autonomous(self, region_name, databases):
        try:
            for dbs in databases:
                self.DatabaseId += 1
                data = {'class': 'Database' + str(self.DatabaseId),
                        'region_name': region_name,
                        'availability_domain': "",
                        'compartment_name': dbs['compartment_name'],
                        'compartment_id': dbs['compartment_id'],
                        'status': dbs['lifecycle_state'],
                        'type': "Autonomous" + dbs['db_workload'],
                        'name': dbs['display_name'], 'shape': "",
                        'cpu_core_count': dbs['cpu_core_count'],
                        'db_storage_gb': str(int(dbs['data_storage_size_in_tbs']) * 1024),
                        'shape_ocpus': "",
                        'memory_gb': "",
                        'local_storage_tb': "",
                        'node_count': "",
                        'database': dbs['db_name'],
                        'version_license_model': dbs['license_model'],
                        'domain': "",
                        'data_subnet': "",
                        'data_subnet_id': "",
                        'backup_subnet': "",
                        'backup_subnet_id': "",
                        'scan_ips': "",
                        'vip_ips': "",
                        'cluster_name': "",
                        'time_created': dbs['time_created'],
                        'db_nodes': ""}
                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_database_db_autonomous", e)

    ##########################################################################
    # database
    ##########################################################################

    def __convert_database_main(self, region_name, list_databases):
        try:

            if len(list_databases) == 0:
                return

            if 'db_system' in list_databases:
                self.__convert_database_db_system(region_name, list_databases['db_system'])

            if 'autonomous' in list_databases:
                self.__convert_database_db_autonomous(region_name, list_databases['autonomous'])

        except Exception as e:
            self.__print_error("__print_database_main", e)

    ##########################################################################
    # convert compute instances
    ##########################################################################
    def __convert_core_compute_instances(self, region_name, instances):

        try:

            if len(instances) == 0:
                return

            for instance in instances:
                self.ComputeId += 1
                data = {'class': 'Compute' + str(self.ComputeId),
                        'region_name': region_name,
                        'availability_domain': instance['availability_domain'],
                        'compartment_name': instance['compartment_name'],
                        'compartment_id': instance['compartment_id'],
                        'server_name': instance['display_name'],
                        'Status': instance['lifecycle_state'],
                        'Type': instance['image_os'],
                        'image': instance['image'],
                        'image_id': instance['image_id'],
                        'fault_domain': instance['fault_domain'],
                        'primary_vcn': "",
                        'primary_subnet': "",
                        'shape': instance['shape'],
                        'ocpus': instance['shape_ocpu'],
                        'memory_gb': instance['shape_memory_gb'],
                        'local_storage_tb': instance['shape_storage_tb'],
                        'public_ips': str(', '.join(x['details']['public_ip'] for x in instance['vnic'])),
                        'private_ips': str(', '.join(x['details']['private_ip'] for x in instance['vnic'])),
                        'subnet_ids': [x['details']['subnet_id'] for x in instance['vnic']],
                        'time_created': instance['time_created'][0:16],
                        'boot_volume': "",
                        'boot_volume_size_gb': "",
                        'boot_volume_b_policy': "",
                        'block_volumes': "",
                        'block_volumes_size_gb': "",
                        'block_volumes_b_policy': ""
                        }

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

                if 'block_volume' in instance:
                    for bv in instance['block_volume']:
                        data['block_volumes'] = str(', '.join(x['display_name'] for x in instance['block_volume']))
                        data['block_volumes_size_gb'] = str('+ '.join(x['size'] for x in instance['block_volume']))
                        data['block_volumes_b_policy'] = str(', '.join(x['backup_policy'] for x in instance['block_volume']))

                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_core_compute_instances", e)

    ##########################################################################
    # convert Compute
    ##########################################################################
    def __convert_core_compute_main(self, region_name, data):

        try:
            if len(data) == 0:
                return

            if 'instances' in data:
                self.__convert_core_compute_instances(region_name, data['instances'])

        except Exception as e:
            self.__print_error("__convert_core_compute_main", e)

    ##########################################################################
    # convert object storage
    ##########################################################################
    def __convert_bucket_main(self, region_name, buckets):
        try:
            for bucket in buckets:
                self.BucketId += 1
                data = {
                    'class': 'Bucket' + str(self.BucketId),
                    'name': bucket['name'],
                    'objects': bucket['objects'],
                    'size': bucket['sum_size_gb'],
                    'preauthenticated_requests': bucket['preauthenticated_requests'],
                    'object_lifecycle': bucket['object_lifecycle'],
                    'compartment_id': bucket['compartment_id'],
                    'compartment_name': bucket['compartment_name'],
                    'region_name': bucket['region_name'],
                    'namespace_name': bucket['namespace_name'],
                }
                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_bucket_main", e)

    ##########################################################################
    # convert load balancer config
    ##########################################################################
    def __convert_load_balancer_details(self, region_name, load_balance_obj):
        try:
            lb = load_balance_obj['details']

            # load balancer
            self.LoadBalancerId += 1
            data = {'class': 'LoadBalancer' + str(self.LoadBalancerId),
                    'region_name': region_name,
                    'compartment_name': lb['compartment_name'],
                    'compartment_id': lb['compartment_id'],
                    'loadBalancer_id': lb['id'],
                    'loadBalancer_name': lb['display_name'],
                    'status': lb['status'],
                    'shape': lb['shape_name'],
                    'type': ("Private" if lb['is_private'] else "Public"),
                    'ip_addresses': str(', '.join(x for x in lb['ips'])),
                    'subnets': str(', '.join(x for x in lb['subnets'])),
                    'subnet_ids': lb['subnet_ids'],
                    'nsg_ids': lb['nsg_ids'],
                    'nsg_names': lb['nsg_names'],
                    'hostnames': lb['hostnames'],
                    'path_route': lb['path_route']
                    }
            self.outdata.append(data)

            # listeners
            if 'listeners' in lb:

                # if no listener
                if not lb['listeners']:
                    self.LoadBalancerListenerId += 1
                    data = {'class': 'LoadBalancerListener' + str(self.LoadBalancerListenerId),
                            'region_name': region_name,
                            'compartment_name': lb['compartment_name'],
                            'compartment_id': lb['compartment_id'],
                            'loadBalancer_name': lb['display_name'],
                            'loadBalancer_id': lb['id'],
                            'listener_port': "No Listener",
                            'listener_def_bs': "",
                            'listener_ssl': "",
                            'listener_path': "",
                            'listener_rule': "",
                            'listener_host': "",
                            }
                    self.outdata.append(data)

                # look over the listeners
                for listener in lb['listeners']:
                    self.LoadBalancerListenerId += 1
                    data = {'class': 'LoadBalancerListener' + str(self.LoadBalancerListenerId),
                            'region_name': region_name,
                            'compartment_name': lb['compartment_name'],
                            'compartment_id': lb['compartment_id'],
                            'loadBalancer_name': lb['display_name'],
                            'loadBalancer_id': lb['id'],
                            'listener_port': listener['port'],
                            'listener_def_bs': listener['default_backend_set_name'],
                            'listener_ssl': listener['ssl_configuration'],
                            'listener_host': str(', '.join(x for x in listener['hostname_names'])),
                            'listener_path': listener['path_route_set_name'],
                            'listener_rule': str(', '.join(x for x in listener['rule_set_names'])),
                            }
                    self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_load_balancer_details", e)

    ##########################################################################
    # convert load balancer backedset
    ##########################################################################
    def __convert_load_balancer_backendset(self, region_name, load_balance_obj):

        try:
            lb = load_balance_obj['details']
            backendset = load_balance_obj['backendset']

            for bs in backendset:

                self.LoadBalancerBackendsetId += 1
                data = {'class': 'LoadBalancerBackendset' + str(self.LoadBalancerBackendsetId),
                        'region_name': region_name,
                        'compartment_name': lb['compartment_name'],
                        'compartment_id': lb['compartment_id'],
                        'loadBalancer_id': lb['id'],
                        'loadBalancer_name': lb['display_name'],
                        'backendset': backendset
                        }
                self.outdata.append(data)

        except Exception as e:
            self.__print_error("__convert_load_balancer_backendset", e)

    ##########################################################################
    # Load Balancer
    ##########################################################################

    def __convert_load_balancer_main(self, region_name, load_balancers):
        try:

            if len(load_balancers) == 0:
                return

            for load_balance_obj in load_balancers:
                if 'details' in load_balance_obj:
                    self.__convert_load_balancer_details(region_name, load_balance_obj)

                if 'backendset' in load_balance_obj:
                    self.__convert_load_balancer_backendset(region_name, load_balance_obj)

        except Exception as e:
            self.__print_error("__convert_load_balancer_main", e)

    ##########################################################################
    # convert file storage
    ##########################################################################
    def __convert_file_storage_main(self, region_name, file_storages):

        try:
            if len(file_storages) == 0:
                return

            for file_storage in file_storages:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(file_storage['compartment_name']):
                    continue

                self.FileStorageId += 1
                data = {'class': "FileStorage" + str(self.FileStorageId)}
                data.update(file_storage)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_file_storage_main", e)

    ##########################################################################
    # convert resource management
    ##########################################################################
    def __convert_resource_management_main(self, region_name, rms):

        try:
            if len(rms) == 0:
                return

            for rm in rms:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(rm['compartment_name']):
                    continue

                self.ResourceManagementId += 1
                data = {'class': "ResourceManagement" + str(self.ResourceManagementId)}
                data.update(rm)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_resource_management_main", e)

    ##########################################################################
    # convert stream
    ##########################################################################
    def __convert_streams_main(self, region_name, streams):

        try:
            if len(streams) == 0:
                return

            for stream in streams:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(stream['compartment_name']):
                    continue

                self.StreamId += 1
                data = {'class': "Stream" + str(self.StreamId)}
                data.update(stream)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_streams_main", e)

    ##########################################################################
    # convert email
    ##########################################################################
    def __convert_email_main(self, region_name, emails):

        try:
            if len(emails) == 0:
                return

            for email in emails:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(email['compartment_name']):
                    continue

                self.EmailId += 1
                data = {'class': "Email" + str(self.EmailId)}
                data.update(email)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_email_main", e)

    ##########################################################################
    # convert container
    ##########################################################################
    def __convert_container_main(self, region_name, containers):

        try:
            if len(containers) == 0:
                return

            for container in containers:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(container['compartment_name']):
                    continue

                self.ContainerId += 1
                data = {'class': "Container" + str(self.ContainerId)}
                data.update(container)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_container_main", e)

    ##########################################################################
    # convert monitoring
    ##########################################################################
    def __convert_monitoring_main(self, region_name, monitors):

        try:
            if len(monitors) == 0:
                return

            for monitor in monitors:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(monitor['compartment_name']):
                    continue

                self.MonitorId += 1
                data = {'class': "Monitor" + str(self.MonitorId)}
                data.update(monitor)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_monitoring_main", e)

    ##########################################################################
    # convert notifications
    ##########################################################################
    def __convert_notifications_main(self, region_name, notifications):

        try:
            if len(notifications) == 0:
                return

            for notification in notifications:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(notification['compartment_name']):
                    continue

                self.NotificationId += 1
                data = {'class': "Notification" + str(self.NotificationId)}
                data.update(notification)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_notifications_main", e)

    ##########################################################################
    # convert Edge
    ##########################################################################
    def __convert_edge_services_main(self, region_name, edges):

        try:

            if 'healthcheck' in edges:
                healthcheck = edges['healthcheck']

                # Add http
                if 'http' in healthcheck:
                    for http in healthcheck['http']:
                        self.EdgeHealthHttpId += 1
                        data = {'class': "EdgeHealthHttp" + str(self.EdgeHealthHttpId)}
                        data.update(http)
                        self.outdata.append(data)

                # Add ping
                if 'ping' in healthcheck:
                    for ping in healthcheck['ping']:
                        self.EdgeHealthHttpId += 1
                        data = {'class': "EdgeHealthPing" + str(self.EdgeHealthPingId)}
                        data.update(ping)
                        self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_edge_services_main", e)

    ##########################################################################
    # convert quotas
    ##########################################################################
    def __convert_quotas_main(self, region_name, quotas):

        try:
            if len(quotas) == 0:
                return

            for quota in quotas:

                # don't extract managed compartment
                if self.__if_managed_paas_compartment(quota['compartment_name']):
                    continue

                self.QuotaId += 1
                data = {'class': "Quota" + str(self.QuotaId)}
                data.update(quota)

                # add details
                self.outdata.append(data)

        except BaseException as e:
            self.__print_error("__convert_quotas_main", e)

    ##########################################################################
    # convert Identity data
    ##########################################################################
    def __convert_region_data(self, region_name, data):

        try:
            if not data:
                return

            for cdata in data:
                if 'network' in cdata:
                    self.__convert_core_network_main(region_name, cdata['network'])
                if 'compute' in cdata:
                    self.__convert_core_compute_main(region_name, cdata['compute'])
                if 'database' in cdata:
                    self.__convert_database_main(region_name, cdata['database'])
                if 'load_balancer' in cdata:
                    self.__convert_load_balancer_main(region_name, cdata['load_balancer'])
                if 'object_storage' in cdata:
                    self.__convert_bucket_main(region_name, cdata['object_storage'])
                if 'file_storage' in cdata:
                    self.__convert_file_storage_main(region_name, cdata['file_storage'])
                if 'resource_management' in cdata:
                    self.__convert_resource_management_main(region_name, cdata['resource_management'])
                if 'streams' in cdata:
                    self.__convert_streams_main(region_name, cdata['streams'])
                if 'email' in cdata:
                    self.__convert_email_main(region_name, cdata['email'])
                if 'containers' in cdata:
                    self.__convert_container_main(region_name, cdata['containers'])
                if 'monitoring' in cdata:
                    self.__convert_monitoring_main(region_name, cdata['monitoring'])
                if 'notifications' in cdata:
                    self.__convert_notifications_main(region_name, cdata['notifications'])
                if 'edge_services' in cdata:
                    self.__convert_edge_services_main(region_name, cdata['edge_services'])
                if 'quotas' in cdata:
                    self.__convert_quotas_main(region_name, cdata['quotas'])

        except Exception as e:
            self.__print_error("__convert_region_data", e)
            raise


##########################################################################
# execute_convert
##########################################################################
def execute_convert():

    # get parset cmd
    cmd = set_parser_arguments()
    if cmd is None:
        return

    ############################################
    # load JSON File
    ############################################
    input_data = load_from_json_file(cmd.input.name)

    ############################################
    # create data instance
    ############################################
    data = ShowOCI2SE()

    ############################################
    # convert
    ############################################
    output_data = data.convert_json(input_data)

    ############################################
    # if print service to screen
    ############################################
    if cmd.screen:
        print(json.dumps(output_data, indent=4, sort_keys=False))

    ############################################
    # if print service to file
    ############################################
    if cmd.output:
        if cmd.output.name:
            write_to_json_file(cmd.output.name, output_data)


##########################################################################
# set parser
##########################################################################
def set_parser_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=argparse.FileType('r'), dest='input', help="Input JSON File")
    parser.add_argument('-o', type=argparse.FileType('w'), dest='output', help="Output JSON File")
    parser.add_argument('-s', action='store_true', default=False, dest='screen', help="Output to screen (JSON format)")

    result = parser.parse_args()

    if len(sys.argv) < 3:
        parser.print_help()
        return None

    return result


############################################
# write data to json file
############################################
def write_to_json_file(file_name, data):

    try:
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False)

        print("Exported Simple JSON to " + file_name)

    except Exception as e:
        raise Exception("Error in print_to_json_file: " + str(e.args))


############################################
# load data to json file
############################################
def load_from_json_file(file_name):

    try:
        with open(file_name) as json_file:
            data = json.load(json_file)
            print("\nLoaded Source " + file_name)
            return data

    except Exception as e:
        raise Exception("Error in load_from_json_file: " + str(e.args))


##########################################################################
# Main
##########################################################################
execute_convert()
