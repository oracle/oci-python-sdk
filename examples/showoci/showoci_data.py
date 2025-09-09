##########################################################################
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# showoci_data.py
#
# @author: Adi Zohar
# @contributors: Olaf Heimburger
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
# This file has ShowOCIData class
# it used the ShowOCIService class and generate JSON structure as output
##########################################################################
from __future__ import print_function
from showoci_service import ShowOCIService, ShowOCIFlags
import sys


class ShowOCIData(object):
    version = "25.08.26"

    ############################################
    # ShowOCIService - Service object to query
    # OCI resources and run searches
    ###########################################
    service = None
    error = 0
    error_array = []

    # OCI Processed data
    data = []

    ############################################
    # Init
    ############################################
    def __init__(self, flags):

        # check if not instance fo ShowOCIFlags
        if not isinstance(flags, ShowOCIFlags):
            raise TypeError("flags must be Flags class")

        # initiate service object
        self.service = ShowOCIService(flags)

        # Initiate data list everytime class is instantiated
        self.data = []

        # if exclude list requested
        if flags.excludelist:
            self.service.generate_exclude_list()

    ############################################
    # get service data
    ############################################
    def get_service_data(self):

        return self.service.data

    ############################################
    # get tenancy data
    ############################################
    def get_tenancy_data(self):

        return self.service.get_tenancy()

    ############################################
    # call service to load data
    ############################################
    def load_service_data(self):

        return self.service.load_service_data()

    ##########################################################################
    # process_oci_data
    ##########################################################################
    def process_oci_data(self):

        try:

            # run identity
            identity_data = {'type': "identity", 'data': self.service.get_identity()}
            self.data.append(identity_data)

            # run on budgets module
            if self.service.flags.read_budgets:
                budgets_data = {'type': "budgets", 'data': self.service.get_budgets()}
                self.data.append(budgets_data)

            # run on announcement module
            if self.service.flags.read_announcement:
                announcement_data = {'type': "announcement", 'data': self.service.get_announcement()}
                self.data.append(announcement_data)

            # run on security_scores module
            if self.service.flags.read_security:
                security_scores_data = {'type': "security_scores", 'data': self.service.get_security_scores()}
                self.data.append(security_scores_data)

            # run on compartments
            if self.service.flags.is_loop_on_compartments:

                # pointer to Tenancy in cache
                tenancy = self.service.get_tenancy()

                # run on each subscribed region
                for region_name in tenancy['list_region_subscriptions']:

                    # check if filter by region
                    if not self.service.oci_region_name_filter(region_name):
                        continue

                    # limits services which regional but not compartment
                    limits_data = []
                    if self.service.flags.read_limits:
                        limits_data = self.__get_limits_main(region_name)

                    # execute the region
                    value = self.__get_oci_region_data(region_name)

                    # if data returns, add to the json
                    if value or limits_data:
                        region_data = ({'type': "region", 'region': region_name, 'data': value, 'limits': limits_data})
                        self.data.append(region_data)

            # Append Error Array
            self.error_array += self.service.error_array
            error_data = {'type': "errors", 'data': self.error_array}
            self.data.append(error_data)

            # return the json data
            return self.data

        except Exception as e:
            raise Exception("Error in process_oci_data: " + str(e))

    ##########################################################################
    # Print version
    ##########################################################################
    def get_showoci_config(self, cmdline, start_time):

        data = {
            'program': "showoci.py",
            'author': "Adi Zohar",
            'contributors': "Olaf Heimburger",
            'disclaimer1': "This is not an official Oracle application, it is not supported by Oracle. It should NOT be used for utilization calculation purposes.",
            'disclaimer2': "If you run into issues using this, please file an issue at https://github.com/oracle/oci-python-sdk/issues rather than contacting support",
            'config_file': self.service.flags.config_file,
            'config_profile': self.service.flags.config_section,
            'connection_timeout': self.service.flags.connection_timeout,
            'read_timeout': self.service.flags.read_timeout,
            'use_instance_principals': self.service.flags.use_instance_principals,
            'use_delegation_token': self.service.flags.use_delegation_token,
            'use_security_token': self.service.flags.use_security_token,
            'version': self.service.flags.showoci_version,
            'override_tenant_id': self.service.flags.filter_by_tenancy_id,
            'datetime': start_time,
            'machine': self.service.flags.machine,
            'python': self.service.flags.python,
            'threads': "False" if self.service.flags.skip_threads else "True with " + str(self.service.flags.threads) + " threads",
            'cmdline': cmdline,
            'oci_sdk_version': self.service.get_oci_version()
        }

        main_data = {'type': "showoci", 'data': data}

        # add oci config to main data
        self.data.append(main_data)
        return main_data

    ##########################################################################
    # get service error flag
    ##########################################################################
    def get_service_errors(self):
        return self.service.error

    ##########################################################################
    # get service warnings flag
    ##########################################################################
    def get_service_warnings(self):
        return self.service.warning

    ##########################################################################
    # get service reboot migration
    ##########################################################################
    def get_service_reboot_migration(self):

        return self.service.reboot_migration_counter

    ##########################################################################
    # get service reboot migration
    ##########################################################################
    def get_service_dbsystem_maintenance(self):

        return self.service.dbsystem_maintenance

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, e):
        try:
            classname = type(self).__name__
            caller_function = sys._getframe(1).f_code.co_name

            if isinstance(e, KeyError):
                print("\nError in " + classname + ":" + caller_function + ": KeyError " + str(e.args))
            else:
                print("\nError in " + classname + ":" + caller_function + ": " + str(e))

            self.error += 1
            self.__add_to_error_array(classname, caller_function, "", e)

        except Exception as e:
            print("\nError in __print_error " + str(e))

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
    # run on Region
    ##########################################################################
    def __get_oci_region_data(self, region_name):

        ret_var = []
        print("\nProcessing Region " + region_name)

        try:

            # Loop on Compartments and call services
            compartments = self.service.get_compartments()

            # Loop on all relevant compartments
            print("\nProcessing...")
            for compartment in compartments:

                #  check if to skip ManagedCompartmentForPaaS
                if compartment['name'] == "ManagedCompartmentForPaaS" and not self.service.flags.read_ManagedCompartmentForPaaS:
                    continue

                print("    Compartment " + compartment['path'] + "...")
                data = {
                    'compartment_id': compartment['id'],
                    'compartment_name': compartment['name'],
                    'compartment': compartment['name'],
                    'path': compartment['path']
                }
                has_data = False

                # run on network module
                if self.service.flags.read_network:
                    value = self.__get_core_network_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['network'] = value
                            has_data = True

                # run on compute and block storage
                if self.service.flags.read_compute:
                    value = self.__get_core_compute_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['compute'] = value
                            has_data = True

                # run on database
                if self.service.flags.read_database:
                    value = self.__get_database_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['database'] = value
                            has_data = True

                # run on file_storage
                if self.service.flags.read_file_storage:
                    value = self.__get_file_storage_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['file_storage'] = value
                            has_data = True

                # run on object storage
                if self.service.flags.read_object_storage:
                    value = self.__get_object_storage_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['object_storage'] = value
                            has_data = True

                # run on Load Balancer
                if self.service.flags.read_load_balancer:
                    value = self.__get_load_balancer_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['load_balancer'] = value
                            has_data = True

                # run on Network Load Balancer
                if self.service.flags.read_load_balancer:
                    value = self.__get_load_balancer_network_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['network_load_balancer'] = value
                            has_data = True

                # run on Resource Management
                if self.service.flags.read_resource_management:
                    value = self.__get_resource_management_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['resource_management'] = value
                            has_data = True

                # run on fsdr use the Resource Management flag
                if self.service.flags.read_resource_management:
                    value = self.__get_fsdr_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['fsdr'] = value
                            has_data = True

                # email
                if self.service.flags.read_email_distribution:
                    value = self.__get_email_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['email'] = value
                            has_data = True

                # container
                if self.service.flags.read_containers:
                    value = self.__get_container_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['containers'] = value
                            has_data = True

                # streams queues
                if self.service.flags.read_streams_queues:
                    value = self.__get_streams_queues_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['streams_queues'] = value
                            has_data = True

                # monitoring
                if self.service.flags.read_monitoring_notifications:
                    value = self.__get_monitoring_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['monitoring'] = value
                            has_data = True

                # notifications
                if self.service.flags.read_monitoring_notifications:
                    value = self.__get_notifications_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['notifications'] = value
                            has_data = True

                # edge services
                if self.service.flags.read_edge:
                    value = self.__get_load_edge_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['edge_services'] = value
                            has_data = True

                # quotas services
                if self.service.flags.read_limits:
                    value = self.__get_quotas_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['quotas'] = value
                            has_data = True

                # paas native services
                if self.service.flags.read_paas_native:
                    value = self.__get_paas_native_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['paas_services'] = value
                            has_data = True

                # security and logging services
                if self.service.flags.read_security:
                    value = self.__get_security_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['security'] = value
                            has_data = True

                # data ai
                if self.service.flags.read_data_ai:
                    value = self.__get_data_ai_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['data_ai'] = value
                            has_data = True

                if self.service.flags.read_function:
                    value = self.__get_functions_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['functions'] = value
                            has_data = True

                if self.service.flags.read_api:
                    value = self.__get_apigateway_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['apigateways'] = value
                            has_data = True

                if self.service.flags.read_announcement:
                    value = self.__get_announcement_detailed(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['announcement_detailed'] = value
                            has_data = True

                # add the data to main Variable
                if has_data:
                    ret_var.append(data)

            print("")

            # return var
            return ret_var

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # Print Network VCN NAT
    ##########################################################################
    def __get_core_network_vcn_nat(self, vcn_id):
        data = []
        try:
            list_nat_gateways = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_NAT, 'vcn_id', vcn_id)
            for arr in list_nat_gateways:
                value = {'id': arr['id'],
                         'name': arr['name'],
                         'display_name': arr['display_name'],
                         'nat_ip': arr['nat_ip'],
                         'compartment_name': arr['compartment_name'],
                         'compartment_path': arr['compartment_path'],
                         'compartment_id': arr['compartment_id'],
                         'time_created': arr['time_created'],
                         'block_traffic': arr['block_traffic'],
                         'defined_tags': arr['defined_tags'],
                         'freeform_tags': arr['freeform_tags']}

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get Network VCN igw
    ##########################################################################

    def __get_core_network_vcn_igw(self, vcn_id):
        data = []
        try:
            list_igws = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_IGW, 'vcn_id', vcn_id)
            for arr in list_igws:
                value = {'id': arr['id'],
                         'name': arr['name'],
                         'vcn_id': arr['vcn_id'],
                         'is_enabled': arr['is_enabled'],
                         'route_table_id': arr['route_table_id'],
                         'route_table': "",
                         'compartment_name': arr['compartment_name'],
                         'compartment_path': arr['compartment_path'],
                         'compartment_id': arr['compartment_id'],
                         'time_created': arr['time_created'],
                         'defined_tags': arr['defined_tags'],
                         'freeform_tags': arr['freeform_tags']}

                # check route table
                if value['route_table_id'] != "None":
                    route_table = self.__get_core_network_route(value['route_table_id'])
                    value['route_table'] = route_table

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get Network VCN SGW
    ##########################################################################

    def __get_core_network_vcn_sgw(self, vcn_id):
        data = []
        try:

            list_service_gateways = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_SGW, 'vcn_id', vcn_id)
            for arr in list_service_gateways:
                value = {'id': arr['id'],
                         'name': arr['name'],
                         'services': arr['services'],
                         'compartment_name': arr['compartment_name'],
                         'compartment_path': arr['compartment_path'],
                         'compartment_id': arr['compartment_id'],
                         'route_table_id': arr['route_table_id'],
                         'route_table': "",
                         'transit': "",
                         'block_traffic': arr['block_traffic'],
                         'time_created': arr['time_created'],
                         'defined_tags': arr['defined_tags'],
                         'freeform_tags': arr['freeform_tags']}

                # check route table
                if value['route_table_id'] != "None":
                    route_table = self.__get_core_network_route(value['route_table_id'])
                    value['route_table'] = route_table
                    value['transit'] = " + Transit Route(" + route_table + ")"

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get dRG details
    ##########################################################################

    def __get_core_network_vcn_drg_details(self, drg_attachment):
        retStr = ""
        name = ""
        route_table = ""
        try:
            drg_id = drg_attachment['drg_id']

            # get DRG name
            drg = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DRG, 'id', drg_id)
            if drg:
                name = drg['name']
                retStr = drg['name']

            # check if IPSEC
            list_ip_sec_connections = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_IPS, 'drg_id', drg_id)
            if len(list_ip_sec_connections) > 0:
                retStr += " + IPSEC (" + str(len(list_ip_sec_connections)) + ")"

            # check if Virtual Circuits
            list_virtual_circuits = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_VC, 'drg_id', drg_id)
            if len(list_virtual_circuits) > 0:
                retStr += " + Fastconnect (" + str(len(list_virtual_circuits)) + ")"

            # Check Remote Peering
            rpcs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_RPC, 'drg_id', drg_id)
            if len(rpcs) > 0:
                retStr += " + Remote Peering (" + str(len(rpcs)) + ")"

            # check transit routing
            if drg_attachment['route_table_id'] != "None" and drg_attachment['route_table_id'] != "":
                route_table = str(self.__get_core_network_route(drg_attachment['route_table_id']))
                retStr += " + Transit Route(" + route_table + ")"

            return retStr, name, route_table

        except Exception as e:
            self.__print_error(e)
            return retStr, name

    ##########################################################################
    # get Network VCN DRG Attached
    ##########################################################################

    def __get_core_network_vcn_drg_attached(self, vcn_id):
        data = []
        try:

            list_drg_attachments = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DRG_AT, 'vcn_id', vcn_id)
            for da in list_drg_attachments:
                val, display_name, route_table = self.__get_core_network_vcn_drg_details(da)
                value = {'id': da['id'],
                         'drg_id': da['drg_id'],
                         'display_name': da['display_name'],
                         'route_table_id': da['route_table_id'],
                         'route_table': route_table,
                         'drg_route_table_id': da['drg_route_table_id'],
                         'drg_route_table': self.__get_core_network_drg_route(da['drg_route_table_id']),
                         'export_drg_route_distribution_id': da['export_drg_route_distribution_id'],
                         'name': val,
                         'compartment_name': da['compartment_name'],
                         'compartment_path': da['compartment_path'],
                         'compartment_id': da['compartment_id'],
                         'time_created': da['time_created']}
                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_core_network_vcn_local_peering
    ##########################################################################
    def __get_core_network_vcn_local_peering(self, vcn_id):
        data = []
        try:
            local_peering_gateways = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_LPG, 'vcn_id', vcn_id)
            for lpg in local_peering_gateways:
                routestr = ""
                route_table = ""
                if lpg['route_table_id'] != "None":
                    route_table = str(self.__get_core_network_route(lpg['route_table_id']))
                    routestr = " + Transit Route(" + route_table + ")"

                value = {'id': lpg['id'],
                         'name': (lpg['name'] + routestr),
                         'display_name': (lpg['display_name']),
                         'compartment_id': lpg['compartment_id'],
                         'compartment_name': lpg['compartment_name'],
                         'compartment_path': lpg['compartment_path'],
                         'time_created': lpg['time_created'],
                         'route_table_id': lpg['route_table_id'],
                         'route_table_name': route_table,
                         'route_table': routestr,
                         'vcn_id': lpg['vcn_id'],
                         'peering_status': lpg['peering_status'],
                         'peer_id': lpg['peer_id'],
                         'peer_name': self.__get_core_network_local_peering(lpg['peer_id']),
                         'peer_advertised_cidr': lpg['peer_advertised_cidr'],
                         'peer_advertised_cidr_details': lpg['peer_advertised_cidr_details'],
                         'is_cross_tenancy_peering': lpg['is_cross_tenancy_peering']
                         }
                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Print Network VCN subnets
    ##########################################################################

    def __get_core_network_vcn_subnets(self, vcn_id):
        data = []
        try:
            subnets = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_SUBNET, 'vcn_id', vcn_id)
            if not subnets:
                return data

            for subnet in subnets:

                # get the list of private_ips
                private_ips = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_SUBNET_PIP, 'subnet_id', subnet['id'])

                # get the list of security lists
                sec_lists = []
                if 'security_list_ids' in subnet:
                    for s in subnet['security_list_ids']:
                        sl = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_SLIST, 'id', s)
                        if sl:
                            sec_lists.append(sl['name'])

                # Get the route and dhcp options
                route_name = ""
                if 'route_table_id' in subnet:
                    route_name_arr = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_ROUTE, 'id', subnet['route_table_id'])
                    if route_name_arr:
                        route_name = route_name_arr['name']

                dhcp_options = ""
                if 'dhcp_options_id' in subnet:
                    dhcp_options_arr = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DHCP, 'id', subnet['dhcp_options_id'])
                    if dhcp_options_arr:
                        dhcp_options = dhcp_options_arr['name']

                val = ({
                    'id': subnet['id'],
                    'subnet': subnet['subnet'],
                    'name': subnet['name'],
                    'cidr_block': subnet['cidr_block'],
                    'availability_domain': subnet['availability_domain'],
                    'public_private': subnet['public_private'],
                    'dns': subnet['dns_label'],
                    'compartment_name': subnet['compartment_name'],
                    'compartment_path': subnet['compartment_path'],
                    'compartment_id': subnet['compartment_id'],
                    'dhcp_options': dhcp_options,
                    'dhcp_options_id': subnet['dhcp_options_id'],
                    'security_list': sec_lists,
                    'security_list_ids': subnet['security_list_ids'],
                    'route': route_name,
                    'route_table_id': subnet['route_table_id'],
                    'time_created': subnet['time_created'],
                    'defined_tags': subnet['defined_tags'],
                    'freeform_tags': subnet['freeform_tags'],
                    'private_ips': private_ips,
                    'logs': self.service.get_logging_log(subnet['id'])
                })
                data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_core_network_vcn_vlans
    ##########################################################################
    def __get_core_network_vcn_dns_resolver(self, vcn_id):
        resolvers = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DNS_RESOLVERS, 'vcn_id', vcn_id)
        return resolvers

    ##########################################################################
    # __get_core_network_vcn_vlans
    ##########################################################################

    def __get_core_network_vcn_vlans(self, vcn_id):
        data = []
        try:
            vlans = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_VLAN, 'vcn_id', vcn_id)
            if not vlans:
                return data

            for vlan in vlans:

                # get the list of NSGs
                nsgs = []
                if 'nsg_ids' in vlan:
                    for nsg in vlan['nsg_ids']:
                        nsg_obj = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_NSG, 'id', nsg)
                        if nsg_obj:
                            nsgs.append(nsg_obj['name'])

                # Get the route and dhcp options
                route_name = ""
                if 'route_table_id' in vlan:
                    route_name_arr = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_ROUTE, 'id', vlan['route_table_id'])
                    if route_name_arr:
                        route_name = route_name_arr['name']

                val = ({
                    'id': vlan['id'],
                    'vlan': vlan['vlan'],
                    'availability_domain': vlan['availability_domain'],
                    'cidr_block': vlan['cidr_block'],
                    'vlan_tag': vlan['vlan_tag'],
                    'display_name': vlan['display_name'],
                    'time_created': vlan['time_created'],
                    'lifecycle_state': vlan['lifecycle_state'],
                    'compartment_name': vlan['compartment_name'],
                    'compartment_path': vlan['compartment_path'],
                    'compartment_id': vlan['compartment_id'],
                    'nsg': nsgs,
                    'nsg_ids': vlan['nsg_ids'],
                    'route': route_name,
                    'route_table_id': vlan['route_table_id'],
                    'defined_tags': vlan['defined_tags'],
                    'freeform_tags': vlan['freeform_tags'],
                    'region_name': vlan['region_name']
                })
                data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Print Network vcn security list
    ##########################################################################

    def __get_core_network_vcn_security_lists(self, vcn_id):
        data = []
        try:
            sec_lists = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_SLIST, 'vcn_id', vcn_id)
            for sl in sec_lists:
                data.append({
                    'id': sl['id'],
                    'name': sl['name'],
                    'compartment_name': sl['compartment_name'],
                    'compartment_path': sl['compartment_path'],
                    'compartment_id': sl['compartment_id'],
                    'sec_rules': sl['sec_rules'],
                    'time_created': sl['time_created'],
                    'defined_tags': sl['defined_tags'],
                    'freeform_tags': sl['freeform_tags']
                })

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Print Network vcn security groups
    ##########################################################################
    def __get_core_network_vcn_security_groups(self, vcn_id):
        data = []
        try:
            nsgs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_NSG, 'vcn_id', vcn_id)
            for nsg in nsgs:
                value = {
                    'id': nsg['id'],
                    'name': nsg['name'],
                    'compartment_name': nsg['compartment_name'],
                    'compartment_path': nsg['compartment_path'],
                    'compartment_id': nsg['compartment_id'],
                    'sec_rules': [],
                    'vnics': nsg['vnics'],
                    'time_created': nsg['time_created'],
                    'defined_tags': nsg['defined_tags'],
                    'freeform_tags': nsg['freeform_tags']
                }

                if 'sec_rules' in nsg:
                    for sec_rule in nsg['sec_rules']:
                        valsec = sec_rule

                        #########################################################################
                        # if need to find NSG OCID and replace the DESC String with value
                        # source
                        #########################################################################
                        if valsec['source_type'] == "NETWORK_SECURITY_GROUP":
                            result = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_NSG, 'id', valsec['source'])
                            if result:
                                valsec['source_name'] = result['name']
                                valsec['desc'] = valsec['desc'].replace(self.service.C_NETWORK_NSG_REPTEXT, result['name'].ljust(17))
                            else:
                                # if not found place the OCID instead of name
                                valsec['source_name'] = "Not Found"
                                valsec['desc'] = valsec['desc'].replace(self.service.C_NETWORK_NSG_REPTEXT, valsec['source'])

                        #########################################################################
                        # if need to find NSG OCID and replace the DESC String with value
                        # Destination
                        #########################################################################
                        if valsec['destination_type'] == "NETWORK_SECURITY_GROUP":
                            result = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_NSG, 'id', valsec['destination'])
                            if result:
                                valsec['destination_name'] = result['name']
                                valsec['desc'] = valsec['desc'].replace(self.service.C_NETWORK_NSG_REPTEXT, result['name'].ljust(17))
                            else:
                                # if not found place the OCID instead of name
                                valsec['destination_name'] = "Not Found"
                                valsec['desc'] = valsec['desc'].replace(self.service.C_NETWORK_NSG_REPTEXT, valsec['destination'])

                        # add to the value sec rules array
                        value['sec_rules'].append(valsec)

                # add to data
                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ###########################################################################
    # get Network vcn rouet table
    ##########################################################################
    def __get_core_network_vcn_route_rule(self, route_rule):

        line = ""
        try:
            if route_rule is None:
                return "None"

            # assign the line for return value
            if route_rule['destination']:
                line = "DST:" + route_rule['destination'].ljust(18)[0:18] + " --> "

            # check network ocid
            network_ocid = route_rule['network_entity_id']
            if network_ocid is None:
                return line + "None"

            # get the name of the component from OCID 2nd id
            network_list = network_ocid.split(".")
            network_dest = ""
            if len(network_list) > 1:
                network_dest = str(network_list[1])

            # if network_dest is empty
            if not network_dest:
                return line + "None"

            # if no ocid
            if network_ocid == "None" or network_ocid == "":
                return line + network_dest

            # if privateip - get the IP
            if network_dest == "privateip":
                network_dest = self.__get_core_network_private_ip(network_ocid)
                if network_dest == "" or network_dest is None:
                    network_dest = "privateip (not exist)"

            # if internetgateway - get the destination name
            if network_dest == "internetgateway":
                network_dest = "IGW"

            # if DRG - get the destination name
            if network_dest == "drg":
                network_dest = self.__get_core_network_drg_name(network_ocid)
                if network_dest == "":
                    network_dest = "DRG (Not Exist)"

            # if natgateway
            if network_dest == "natgateway":
                network_dest = "NATGW"

            # if servicegateway - get the service and sgw name
            if network_dest == "servicegateway":
                network_dest = "SGW"
                result = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_SGW, 'id', network_ocid)
                if result:
                    network_dest = "SGW" + " " + result['name']

            # if localpeeringgateway - get the destination name
            if network_dest == "localpeeringgateway":
                network_dest = self.__get_core_network_local_peering(network_ocid)
                if network_dest == "":
                    network_dest = "LPG (not exist)"

            # return value
            return line + network_dest

        except Exception as e:
            self.__print_error(e)
            return line

    ########################################################################
    # Print Network vcn Route Tables
    ##########################################################################

    def __get_core_network_vcn_route_tables(self, vcn_id):
        data = []
        try:
            route_tables = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_ROUTE, 'vcn_id', vcn_id)

            for rt in route_tables:
                route_rules = []
                for rl in rt['route_rules']:
                    route_rules.append(
                        {'network_entity_id': rl['network_entity_id'],
                         'destination': rl['destination'],
                         'cidr_block': rl['cidr_block'],
                         'destination_type': rl['destination_type'],
                         'description': rl['description'],
                         'desc': self.__get_core_network_vcn_route_rule(rl)
                         })

                # add route
                val = {'id': rt['id'],
                       'name': rt['name'],
                       'compartment_name': rt['compartment_name'],
                       'compartment_path': rt['compartment_path'],
                       'compartment_id': rt['compartment_id'],
                       'time_created': rt['time_created'],
                       'route_rules': route_rules}
                data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get DHCP options for DHCP_ID
    ##########################################################################
    def __get_core_network_vcn_dhcp_options(self, vcn_id):

        data = []
        try:
            dhcp_options = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DHCP, 'vcn_id', vcn_id)

            for dhcp in dhcp_options:
                data.append({
                    'id': dhcp['id'],
                    'name': dhcp['name'],
                    'compartment_name': dhcp['compartment_name'],
                    'compartment_path': dhcp['compartment_path'],
                    'compartment_id': dhcp['compartment_id'],
                    'time_created': dhcp['time_created'],
                    'opt': dhcp['options']
                })
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print network vcn
    # loop on other compartments for vcn properties
    ##########################################################################
    def __get_core_network_vcn(self, region_name, compartment):

        vcn_data = []
        try:
            vcns = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_VCN, 'region_name', region_name, 'compartment_id', compartment['id'])

            for vcn in vcns:

                # get details for all components
                val = {'igw': self.__get_core_network_vcn_igw(vcn['id']),
                       'sgw': self.__get_core_network_vcn_sgw(vcn['id']),
                       'nat': self.__get_core_network_vcn_nat(vcn['id']),
                       'drg_attached': self.__get_core_network_vcn_drg_attached(vcn['id']),
                       'local_peering': self.__get_core_network_vcn_local_peering(vcn['id']),
                       'subnets': self.__get_core_network_vcn_subnets(vcn['id']),
                       'vlans': self.__get_core_network_vcn_vlans(vcn['id']),
                       'dns_resolvers': self.__get_core_network_vcn_dns_resolver(vcn['id']),
                       'security_lists': self.__get_core_network_vcn_security_lists(vcn['id']),
                       'security_groups': self.__get_core_network_vcn_security_groups(vcn['id']),
                       'route_tables': self.__get_core_network_vcn_route_tables(vcn['id']),
                       'dhcp_options': self.__get_core_network_vcn_dhcp_options(vcn['id'])}

                # assign the data to the vcn
                main_data = {
                    'id': vcn['id'],
                    'name': vcn['name'],
                    'display_name': vcn['display_name'],
                    'cidr_block': "",
                    'cidr_blocks': vcn['cidr_blocks'],
                    'ipv6_private_cidr_blocks': vcn['ipv6_private_cidr_blocks'],
                    'ipv6_cidr_blocks': vcn['ipv6_cidr_blocks'],
                    'byoipv6_cidr_blocks': vcn['byoipv6_cidr_blocks'],
                    'default_dhcp_options_id': vcn['default_dhcp_options_id'],
                    'default_route_table_id': vcn['default_route_table_id'],
                    'default_security_list_id': vcn['default_security_list_id'],
                    'dns_label': vcn['dns_label'],
                    'vcn_domain_name': vcn['vcn_domain_name'],
                    'compartment_name': str(compartment['name']),
                    'compartment_path': str(compartment['path']),
                    'compartment_id': str(compartment['id']),
                    'defined_tags': vcn['defined_tags'],
                    'freeform_tags': vcn['freeform_tags'],
                    'drg_route_table_id': "",
                    'drg_route_name': "",
                    'route_table_id': "",
                    'route_table': "",
                    'data': val
                }

                if val['drg_attached']:
                    da = val['drg_attached'][0]
                    main_data['drg_route_table_id'] = da['drg_route_table_id']
                    main_data['drg_route_name'] = da['drg_route_table']
                    main_data['route_table_id'] = da['route_table_id']
                    main_data['route_table'] = da['route_table']

                vcn_data.append(main_data)
            return vcn_data

        except BaseException as e:
            self.__print_error(e)
            return vcn_data

    ##########################################################################
    # print network cpe
    ##########################################################################
    def __get_core_network_cpe(self, region_name, compartment):
        data = []
        try:
            cpes = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_CPE, 'region_name', region_name, 'compartment_id', compartment['id'])
            return cpes

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print network fw
    ##########################################################################
    def __get_core_network_firewall(self, region_name, compartment):
        data = []
        try:
            nfw = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_FIREWALL, 'region_name', region_name, 'compartment_id', compartment['id'])
            return nfw

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print network fw policies
    ##########################################################################
    def __get_core_network_firewall_policies(self, region_name, compartment):
        data = []
        try:
            nfw = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_FIREWALL_POLICY, 'region_name', region_name, 'compartment_id', compartment['id'])
            return nfw

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print network drg
    ##########################################################################
    def __get_core_network_drg(self, region_name, compartment):

        data = []
        try:
            drgs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DRG, 'region_name', region_name, 'compartment_id', compartment['id'])
            for drg in drgs:
                drg_id = drg['id']
                val = {
                    'id': drg['id'],
                    'name': drg['name'],
                    'time_created': drg['time_created'],
                    'redundancy': drg['redundancy'],
                    'compartment_name': drg['compartment_name'],
                    'compartment_path': drg['compartment_path'],
                    'compartment_id': drg['compartment_id'],
                    'defined_tags': drg['defined_tags'],
                    'freeform_tags': drg['freeform_tags'],
                    'region_name': drg['region_name'],
                    'drg_route_tables': drg['drg_route_tables'],
                    'ip_sec_connections': self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_IPS, 'drg_id', drg_id),
                    'virtual_circuits': self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_VC, 'drg_id', drg_id),
                    'remote_peerings': self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_RPC, 'drg_id', drg_id),
                    'vcns': []
                }

                # Add VCNs
                drg_attachments = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DRG_AT, 'drg_id', drg_id)
                for da in drg_attachments:
                    if da['vcn_id']:
                        vcn = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_VCN, 'id', da['vcn_id'])
                        if vcn:
                            vcn['drg_route_table_id'] = da['drg_route_table_id']
                            vcn['drg_route_table'] = self.__get_core_network_drg_route(da['drg_route_table_id'])
                            vcn['route_table_id'] = da['route_table_id']
                            vcn['route_table'] = self.__get_core_network_route(da['route_table_id'])
                            val['vcns'].append(vcn)

                data.append(val)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get drg route
    ##########################################################################
    def __get_core_network_drg_route(self, drg_route_table_id):
        try:
            route = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DRG_RT, 'id', drg_route_table_id)
            if route:
                if 'display_name' in route:
                    return route['display_name']
            return ""

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get dRG details
    ##########################################################################

    def __get_core_network_drg_name(self, drg_id):
        try:
            # get DRG name
            drg = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DRG, 'id', drg_id)
            if drg:
                return "DRG - " + drg['name'] + " (" + drg['redundancy'] + ")"
            return ""

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get cpe name
    ##########################################################################

    def __get_core_network_cpe_name(self, cpe_id):
        try:
            # get DRG name
            cpe = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_CPE, 'id', cpe_id)
            if cpe:
                return "CPE - " + cpe['name']

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get vcn name
    ##########################################################################
    def __get_core_network_vcn_name(self, vcn_id):
        try:
            # get DRG name
            vcn = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_VCN, 'id', vcn_id)
            if vcn:
                return vcn['name']

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get rfc name
    ##########################################################################
    def __get_core_network_rpc_name(self, rpc_id):
        try:
            # get DRG name
            rpc = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_RPC, 'id', rpc_id)
            if rpc:
                if 'name' in rpc:
                    return rpc['name']
            return ""

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get Subnet Name
    ##########################################################################
    def __get_core_network_subnet_name(self, subnet_id):
        try:

            subnet = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_SUBNET, 'id', subnet_id)
            if subnet:
                return (subnet['name'] + " " + subnet['cidr_block'] + ", VCN (" + subnet['vcn_name'] + ")")
            else:
                return ""

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get Subnet Names
    # 12/1/2024 - Keeping string to avoid breaking json
    ##########################################################################
    def __get_core_network_subnet_names(self, subnet_ids):
        try:
            ret_val = []
            for subnet in subnet_ids:
                ret_val.append(self.__get_core_network_subnet_name(subnet))
            return ret_val
        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # print network remote peering
    ##########################################################################
    def __get_core_network_remote_peering(self, region_name, compartment):

        data = []
        try:
            rpcs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_RPC, 'region_name', region_name, 'compartment_id', compartment['id'])
            for rpc in rpcs:
                drg_name = self.__get_core_network_drg_name(rpc['drg_id'])
                main_data = {
                    'id': str(rpc['id']),
                    'peer_id': str(rpc['peer_id']),
                    'name': str(rpc['name']),
                    'drg': drg_name,
                    'drg_id': rpc['drg_id'],
                    'is_cross_tenancy_peering': str(rpc['is_cross_tenancy_peering']),
                    'peer_region_name': str(rpc['peer_region_name']),
                    'peer_rfc_name': self.__get_core_network_rpc_name(rpc['peer_id']),
                    'peer_tenancy_id': rpc['peer_tenancy_id'],
                    'peering_status': rpc['peering_status'],
                    'compartment_id': rpc['compartment_id'],
                    'compartment_name': rpc['compartment_name'],
                    'compartment_path': rpc['compartment_path'],
                    'region_name': rpc['region_name'],
                    'drg_route_table_id': rpc['drg_route_table_id'],
                    'drg_route_table': rpc['drg_route_table']
                }

                data.append(main_data)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get network ipsec
    ##########################################################################
    def __get_core_network_ipsec(self, region_name, compartment):

        data = []
        try:
            list_ip_sec_connections = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_IPS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for ips in list_ip_sec_connections:
                drg = self.__get_core_network_drg_name(ips['drg_id'])
                cpe = self.__get_core_network_cpe_name(ips['cpe_id'])
                main_data = {
                    'id': ips['id'],
                    'name': ips['name'],
                    'drg': drg,
                    'drg_id': ips['drg_id'],
                    'cpe': cpe,
                    'cpe_id': ips['cpe_id'],
                    'cpe_local_identifier': ips['cpe_local_identifier'],
                    'cpe_local_identifier_type': ips['cpe_local_identifier_type'],
                    'routes': ips['static_routes'],
                    'tunnels': ips['tunnels'],
                    'defined_tags': ips['defined_tags'],
                    'freeform_tags': ips['freeform_tags'],
                    'time_created': ips['time_created'],
                    'compartment_id': ips['compartment_id'],
                    'compartment_name': ips['compartment_name'],
                    'compartment_path': ips['compartment_path'],
                    'region_name': ips['region_name'],
                    'drg_route_table_id': ips['drg_route_table_id'],
                    'drg_route_table': ips['drg_route_table'],
                    'logs': self.service.get_logging_log(ips['id'])
                }

                data.append(main_data)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get network virtual_circuit
    ##########################################################################
    def __get_core_network_virtual_circuit(self, region_name, compartment):

        data = []
        try:
            list_virtual_circuits = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_VC, 'region_name', region_name, 'compartment_id', compartment['id'])

            for vc in list_virtual_circuits:
                drg = self.__get_core_network_drg_name(vc['drg_id'])
                main_data = {
                    'id': str(vc['id']),
                    'name': str(vc['name']),
                    'bandwidth_shape_name': str(vc['bandwidth_shape_name']),
                    'bgp_management': str(vc['bgp_management']),
                    'bgp_session_state': str(vc['bgp_session_state']),
                    'bgp_ipv6_session_state': vc['bgp_ipv6_session_state'],
                    'bgp_admin_state': vc['bgp_admin_state'],
                    'is_bfd_enabled': vc['is_bfd_enabled'],
                    'customer_asn': vc['customer_asn'],
                    'gateway_id': vc['gateway_id'],
                    'provider_service_id': vc['provider_service_id'],
                    'provider_service_key_name': vc['provider_service_key_name'],
                    'routing_policy': vc['routing_policy'],
                    'public_prefixes': vc['public_prefixes'],
                    'region': vc['region'],
                    'customer_bgp_asn': str(vc['customer_bgp_asn']),
                    'drg': drg,
                    'drg_id': vc['drg_id'],
                    'lifecycle_state': str(vc['lifecycle_state']),
                    'oracle_bgp_asn': str(vc['oracle_bgp_asn']),
                    'provider_name': str(vc['provider_name']),
                    'provider_service_name': str(vc['provider_service_name']),
                    'provider_state': str(vc['provider_state']),
                    'reference_comment': str(vc['reference_comment']),
                    'service_type': str(vc['service_type']),
                    'time_created': str(vc['time_created']),
                    'cross_connect_mappings': vc['cross_connect_mappings'],
                    'type': str(vc['type']),
                    'compartment_id': vc['compartment_id'],
                    'compartment_name': vc['compartment_name'],
                    'compartment_path': vc['compartment_path'],
                    'defined_tags': vc['defined_tags'],
                    'freeform_tags': vc['freeform_tags'],
                    'region_name': vc['region_name'],
                    'drg_route_table_id': vc['drg_route_table_id'],
                    'drg_route_table': vc['drg_route_table'],
                    'logs': self.service.get_logging_log(vc['id'])
                }

                # find Attachment for the Virtual Circuit
                drg_attachment = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DRG_AT, 'virtual_cirtcuit_id', vc['id'])
                if drg_attachment:
                    main_data['drg_route_table_id'] = drg_attachment['drg_route_table_id']
                    main_data['drg_route_table'] = self.__get_core_network_drg_route(drg_attachment['drg_route_table_id'])

                data.append(main_data)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Print Network VCN Local Peering
    ##########################################################################

    def __get_core_network_local_peering(self, local_peering_id):
        try:
            result = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_LPG, 'id', local_peering_id)
            if result:
                if 'name' in result:
                    return result['name']
            return ""

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get Network route
    ##########################################################################
    def __get_core_network_route(self, route_table_id):
        try:
            route = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_ROUTE, 'id', route_table_id)
            if route:
                if 'name' in route:
                    return route['name']
            return ""

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # self.__get_core_network_private_ip
    ##########################################################################
    def __get_core_network_private_ip(self, private_ip_id):

        try:
            result = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_PRIVATEIP, 'id', private_ip_id)
            if result:
                if 'name' in result:
                    return result['name']
            return " Not Exist"

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # Network Main
    ##########################################################################
    def __get_core_network_main(self, region_name, compartment):

        return_data = {}
        try:

            data = self.__get_core_network_vcn(region_name, compartment)
            if len(data) > 0:
                return_data['vcn'] = data

            data = self.__get_core_network_drg(region_name, compartment)
            if len(data) > 0:
                return_data['drg'] = data

            data = self.__get_core_network_cpe(region_name, compartment)
            if len(data) > 0:
                return_data['cpe'] = data

            data = self.__get_core_network_ipsec(region_name, compartment)
            if len(data) > 0:
                return_data['ipsec'] = data

            data = self.__get_core_network_remote_peering(region_name, compartment)
            if len(data) > 0:
                return_data['remote_peering'] = data

            data = self.__get_core_network_virtual_circuit(region_name, compartment)
            if len(data) > 0:
                return_data['virtual_circuit'] = data

            data = self.__get_core_network_firewall(region_name, compartment)
            if len(data) > 0:
                return_data['network_firewall'] = data

            data = self.__get_core_network_firewall_policies(region_name, compartment)
            if len(data) > 0:
                return_data['network_firewall_policies'] = data

            return return_data

        except Exception as e:
            self.__print_error(e)
            return return_data

    ##########################################################################
    # get volume backup policy
    ##########################################################################
    def __get_core_block_volume_backup_policy(self, block_storage, volume_id):

        try:
            backupstr = ""
            backup_policy_assignments = block_storage.get_volume_backup_policy_asset_assignment(volume_id).data
            if len(backup_policy_assignments) > 0:
                backupstr = " Backup="
                for backup_policy_assignment in backup_policy_assignments:
                    bp = block_storage.get_volume_backup_policy(backup_policy_assignment.policy_id).data
                    backupstr += bp.display_name + " "
            return backupstr

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get Core Block boot volume
    ##########################################################################
    def __get_core_block_volume_boot(self, bva, compartment_name):
        try:
            value = {}
            comp_text = ""
            volume_group = ""
            encrypted = ""

            # get block volume
            bv = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_BOOT, 'id', bva['boot_volume_id'])
            if bv:

                # check if different compartment
                if bv['compartment_name'] != compartment_name:
                    comp_text = " (Compartment=" + bv['compartment_name'] + ")"

                if bv['volume_group_name']:
                    volume_group = " - Group " + bv['volume_group_name']

                if bva['is_pv_encryption_in_transit_enabled']:
                    encrypted = " - TransitEncrypted=" + bva['is_pv_encryption_in_transit_enabled']

                value = {
                    'id': bv['id'],
                    'sum_info': 'Compute - Block Storage (GB)',
                    'sum_size_gb': bv['size_in_gbs'],
                    'size': bv['size_in_gbs'],
                    'desc': (str(bv['size_in_gbs']) + "GB - " + str(bv['display_name']) + " (" + bv['vpus_per_gb'] + " vpus) " + bv['backup_policy'] + volume_group + comp_text + encrypted),
                    'backup_policy': bv['backup_policy'],
                    'vpus_per_gb': bv['vpus_per_gb'],
                    'volume_group_name': bv['volume_group_name'],
                    'compartment_name': bv['compartment_name'],
                    'compartment_path': bv['compartment_path'],
                    'is_hydrated': bv['is_hydrated'],
                    'encryption_in_transit_type': bva['encryption_in_transit_type'],
                    'is_pv_encryption_in_transit_enabled': bva['is_pv_encryption_in_transit_enabled'],
                    'is_auto_tune_enabled': bv['is_auto_tune_enabled'],
                    'auto_tuned_vpus_per_gb': bv['auto_tuned_vpus_per_gb'],
                    'time_created': bv['time_created'],
                    'display_name': bv['display_name'],
                    'bv_volume_replicas': bv['bv_volume_replicas'],
                    'autotune_policies': bv['autotune_policies'],
                    'kms_key_id': bv['kms_key_id'],
                    'kms_key_name': self.__get_vault_key_name(bv['kms_key_id']),
                    'image_id': bv['image_id'],
                    'defined_tags': bv['defined_tags'],
                    'freeform_tags': bv['freeform_tags']
                }
            return value

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get Core Block boot volume
    ##########################################################################

    def __get_core_block_volume(self, bva, compartment_name):
        try:
            value = {}
            comp_text = ""
            volume_group = ""
            encrypted = ""

            # get block volume
            bv = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_VOL, 'id', bva['volume_id'])
            if bv:

                # check if different compartment
                if bv['compartment_name'] != compartment_name:
                    comp_text = " (Compartment=" + bv['compartment_name'] + ")"

                if bv['volume_group_name']:
                    volume_group = " - Group " + bv['volume_group_name']

                if bva['is_pv_encryption_in_transit_enabled']:
                    encrypted = " - TransitEncrypted=" + bva['is_pv_encryption_in_transit_enabled']

                value = {
                    'id': bv['id'],
                    'sum_info': 'Compute - Block Storage (GB)',
                    'sum_size_gb': bv['size_in_gbs'],
                    'desc': (str(bv['size_in_gbs']) + "GB - " + str(bv['display_name']) + " (" + bv['vpus_per_gb'] + " vpus) " + bv['backup_policy'] + volume_group + comp_text + encrypted),
                    'time_created': bv['time_created'],
                    'compartment_name': bv['compartment_name'],
                    'compartment_path': bv['compartment_path'],
                    'compartment_id': bv['compartment_id'],
                    'backup_policy': bv['backup_policy'],
                    'display_name': bv['display_name'],
                    'vpus_per_gb': bv['vpus_per_gb'],
                    'volume_group_name': bv['volume_group_name'],
                    'is_hydrated': bv['is_hydrated'],
                    'size': str(bv['size_in_gbs']),
                    'is_read_only': str(bva['is_read_only']),
                    'is_shareable': str(bva['is_shareable']),
                    'is_pv_encryption_in_transit_enabled': str(bva['is_pv_encryption_in_transit_enabled']),
                    'attachment_type': str(bva['attachment_type']),
                    'is_multipath': str(bva['is_multipath']),
                    'is_auto_tune_enabled': bv['is_auto_tune_enabled'],
                    'auto_tuned_vpus_per_gb': bv['auto_tuned_vpus_per_gb'],
                    'iscsi_login_state': str(bva['iscsi_login_state']),
                    'bv_volume_replicas': bv['bv_volume_replicas'],
                    'autotune_policies': bv['autotune_policies'],
                    'kms_key_id': bv['kms_key_id'],
                    'kms_key_name': self.__get_vault_key_name(bv['kms_key_id']),
                    'defined_tags': bv['defined_tags'],
                    'freeform_tags': bv['freeform_tags']
                }
            return value

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # get compute boot volume or volume
    ##########################################################################
    def __get_core_block_volume_boot_backup(self, region_name, compartment, volume_name, service_name):

        data = []
        try:
            backups = self.service.search_multi_items(self.service.C_BLOCK, service_name, 'region_name', region_name, 'compartment_id', compartment['id'])

            for backup in backups:
                value = {}

                if backup['backup_lifecycle_state'] != "AVAILABLE":
                    value['name'] = backup['backup_name'] + " (Source " + backup['backup_lifecycle_state'] + ")"
                else:
                    value['name'] = backup['backup_name']

                value['desc'] = backup['display_name']
                value['type'] = backup['type'][0:4] + ", " + backup['source_type'][0:6] + ", " + backup['time_created'][0:16] + " -> " + backup['expiration_time'][0:16]
                value['size'] = (str(backup['size_in_gbs']).rjust(3) + "GB " + ", Stored " + str(backup['unique_size_in_gbs']).rjust(3) + "GB")
                value['sum_info'] = 'Object Storage - BV Backups (GB)'
                value['sum_size_gb'] = backup['unique_size_in_gbs']
                value['volume_type'] = volume_name
                value['volume_id'] = backup['volume_id']
                value['source_name'] = backup['backup_name']
                value['backup_type'] = backup['type']
                value['kms_key_id'] = backup['kms_key_id']
                value['kms_key_name'] = self.__get_vault_key_name(backup['kms_key_id'])
                value['schedule_type'] = backup['source_type']
                value['time_created'] = backup['time_created'][0:16]
                value['expiration_time'] = backup['expiration_time'][0:16]
                value['unique_size_in_gbs'] = backup['unique_size_in_gbs']
                value['size_in_gbs'] = backup['size_in_gbs']
                value['compartment_name'] = backup['compartment_name']
                value['compartment_path'] = backup['compartment_path']
                value['id'] = backup['id']

                data.append(value)

            if len(data) > 0:
                return sorted(data, key=lambda k: k['name'])
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get block volume which not attached
    ##########################################################################
    def __get_core_block_volume_not_attached(self, region_name, compartment):

        data = []
        try:
            volumes = self.service.search_multi_items(self.service.C_BLOCK, self.service.C_BLOCK_VOL, 'region_name', region_name, 'compartment_id', compartment['id'])
            volattc = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_VOLUME_ATTACH, 'region_name', region_name)

            # loop on volumes
            for vol in volumes:
                found = False

                # loop on vol attached to check if exist
                for att in volattc:
                    if att['volume_id'] == vol['id'] and att['lifecycle_state'] == 'ATTACHED':
                        found = True
                        break

                # if not found, add
                if not found:

                    # append to the list
                    volume_group = ""
                    if vol['volume_group_name']:
                        volume_group = " - Group " + vol['volume_group_name']

                    value = {
                        'id': vol['id'],
                        'display_name': vol['display_name'],
                        'availability_domain': vol['availability_domain'],
                        'size': vol['size_in_gbs'],
                        'backup_policy': vol['backup_policy'],
                        'compartment_name': compartment['name'],
                        'compartment_path': compartment['path'],
                        'volume_group_name': vol['volume_group_name'],
                        'vpus_per_gb': vol['vpus_per_gb'],
                        'kms_key_id': vol['kms_key_id'],
                        'kms_key_name': self.__get_vault_key_name(vol['kms_key_id']),
                        'bv_volume_replicas': vol['bv_volume_replicas'],
                        'sum_info': 'Compute - Block Storage (GB)',
                        'sum_size_gb': vol['size_in_gbs'],
                        'defined_tags': vol['defined_tags'],
                        'freeform_tags': vol['freeform_tags'],
                        'desc': ((str(vol['size_in_gbs']) + "GB").ljust(7) + " - " + str(vol['display_name']).ljust(20)[0:19] + " - " + vol['availability_domain'] + " - " + vol['time_created'][0:16] + volume_group)
                    }

                    data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get block boot which not attached
    ##########################################################################
    def __get_core_block_boot_not_attached(self, region_name, compartment):

        data = []
        try:
            volumes = self.service.search_multi_items(self.service.C_BLOCK, self.service.C_BLOCK_BOOT, 'region_name', region_name, 'compartment_id', compartment['id'])
            volattc = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_BOOT_VOL_ATTACH, 'region_name', region_name)

            # loop on volumes
            for vol in volumes:
                found = False

                # loop on vol attached to check if exist
                for att in volattc:
                    if att['boot_volume_id'] == vol['id']:
                        found = True
                        break

                # if not found, add
                if not found:

                    # append to the list
                    volume_group = ""
                    if vol['volume_group_name']:
                        volume_group = " - Group " + vol['volume_group_name']

                    value = {
                        'id': vol['id'],
                        'display_name': vol['display_name'],
                        'availability_domain': vol['availability_domain'],
                        'size': vol['size_in_gbs'],
                        'kms_key_id': vol['kms_key_id'],
                        'kms_key_name': self.__get_vault_key_name(vol['kms_key_id']),
                        'bv_volume_replicas': vol['bv_volume_replicas'],
                        'backup_policy': vol['backup_policy'],
                        'vpus_per_gb': vol['vpus_per_gb'],
                        'compartment_name': compartment['name'],
                        'compartment_path': compartment['path'],
                        'volume_group_name': vol['volume_group_name'],
                        'sum_info': 'Compute - Block Storage (GB)',
                        'sum_size_gb': vol['size_in_gbs'],
                        'defined_tags': vol['defined_tags'],
                        'freeform_tags': vol['freeform_tags'],
                        'desc': ((str(vol['size_in_gbs']) + "GB").ljust(7) + " - " + str(vol['display_name']).ljust(26)[0:25] + " - " + vol['availability_domain'] + " - " + vol['time_created'][0:16] + volume_group)
                    }

                    data.append(value)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get compute boot volume
    ##########################################################################
    def __get_core_block_volume_groups(self, region_name, compartment):

        data = []
        try:
            volgroups = self.service.search_multi_items(self.service.C_BLOCK, self.service.C_BLOCK_VOLGRP, 'region_name', region_name, 'compartment_id', compartment['id'])

            for vplgrp in volgroups:
                value = {
                    'id': vplgrp['id'],
                    'name': vplgrp['display_name'],
                    'size_in_gbs': vplgrp['size_in_gbs'],
                    'compartment_name': str(vplgrp['compartment_name']),
                    'compartment_path': str(vplgrp['compartment_path']),
                    'volumes': [],
                    'bv_volume_replicas': vplgrp['bv_volume_replicas'],
                    'is_hydrated': vplgrp['is_hydrated'],
                    'time_created': vplgrp['time_created'],
                    'defined_tags': vplgrp['defined_tags'],
                    'freeform_tags': vplgrp['freeform_tags']
                }

                for vol_id in vplgrp['volume_ids']:
                    vol = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_VOL, 'id', vol_id)

                    # if Not a volume, try boot volume
                    if vol is None:
                        vol = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_BOOT, 'id', vol_id)

                    # if None continue
                    if vol is None:
                        continue

                    value['volumes'].append({
                        'id': vol['id'],
                        'display_name': vol['display_name'],
                        'desc': vol['display_name'] + " - " + vol['size_in_gbs'] + 'GB'
                    })

                data.append(value)

            if len(data) > 0:
                return sorted(data, key=lambda k: k['name'])
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print compute instances
    ##########################################################################
    def __get_core_compute_instances(self, region_name, compartment):

        data = []
        try:
            instances = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_INST, 'region_name', region_name, 'compartment_id', compartment['id'])

            for instance in instances:

                # fix the shape image for the summary
                sum_shape = ""
                sum_flex = ""
                if instance['image'] == "Not Found" or instance['image'] == "Custom" or "Oracle-Linux" in instance['image']:
                    sum_shape = instance['image_os'][0:35]
                elif 'Windows-Server' in instance['image']:
                    sum_shape = instance['image'][0:19]
                elif instance['image_os'] == "PaaS Image":
                    sum_shape = "PaaS Image - " + instance['display_name'].split("|", 2)[1] if len(instance['display_name'].split("|", 2)) >= 2 else instance['image_os']
                elif instance['image_os'] == "Windows":
                    sum_shape = "Windows-" + instance['image'][0:25]
                else:
                    sum_shape = instance['image'][0:35]

                if 'Flex' in instance['shape']:
                    sum_flex = "." + str(int(instance['shape_ocpu']))

                inst = {
                    'id': instance['id'],
                    'name': instance['shape'] + " - " + instance['display_name'] + " - " + instance['lifecycle_state'],
                    'sum_info': 'Compute',
                    'sum_shape': str(instance['shape'].replace("Flex", "F") + sum_flex).ljust(22, ' ')[0:21] + " - " + sum_shape,
                    'availability_domain': instance['availability_domain'],
                    'fault_domain': instance['fault_domain'],
                    'time_maintenance_reboot_due': str(instance['time_maintenance_reboot_due']),
                    'image': instance['image'], 'image_id': instance['image_id'],
                    'image_os': instance['image_os'],
                    'shape': instance['shape'],
                    'shape_ocpu': instance['shape_ocpu'],
                    'shape_memory_gb': instance['shape_memory_gb'],
                    'shape_storage_tb': instance['shape_storage_tb'],
                    'shape_gpu_description': instance['shape_gpu_description'],
                    'shape_gpus': instance['shape_gpus'],
                    'shape_local_disk_description': instance['shape_local_disk_description'],
                    'shape_local_disks': instance['shape_local_disks'],
                    'shape_max_vnic_attachments': instance['shape_max_vnic_attachments'],
                    'shape_networking_bandwidth_in_gbps': instance['shape_networking_bandwidth_in_gbps'],
                    'shape_processor_description': instance['shape_processor_description'],
                    'shape_baseline_ocpu_utilization': instance['shape_baseline_ocpu_utilization'],
                    'shape_local_disks_total_size_in_gbs': instance['shape_local_disks_total_size_in_gbs'],
                    'display_name': instance['display_name'],
                    'compartment_name': instance['compartment_name'],
                    'compartment_path': instance['compartment_path'],
                    'compartment_id': instance['compartment_id'],
                    'lifecycle_state': instance['lifecycle_state'],
                    'console_id': instance['console_id'], 'console': instance['console'],
                    'time_created': instance['time_created'],
                    'agent_is_management_disabled': instance['agent_is_management_disabled'],
                    'agent_is_monitoring_disabled': instance['agent_is_monitoring_disabled'],
                    'are_all_plugins_disabled': instance['are_all_plugins_disabled'],
                    'agent_plugin_config': instance['agent_plugin_config'],
                    'agent_plugin_status': instance['agent_plugin_status'],
                    'defined_tags': instance['defined_tags'],
                    'freeform_tags': instance['freeform_tags'],
                    'metadata': instance['metadata'],
                    'extended_metadata': instance['extended_metadata'],
                    'is_live_migration_preferred': instance['is_live_migration_preferred'],
                    'recovery_action': instance['recovery_action'],
                    'launch_boot_volume_type': instance['launch_boot_volume_type'],
                    'launch_firmware': instance['launch_firmware'],
                    'launch_network_type': instance['launch_network_type'],
                    'launch_remote_data_volume_type': instance['launch_remote_data_volume_type'],
                    'launch_is_pv_encryption_in_transit_enabled': instance['launch_is_pv_encryption_in_transit_enabled'],
                    'launch_is_consistent_volume_naming_enabled': instance['launch_is_consistent_volume_naming_enabled'],
                    'are_legacy_imds_endpoints_disabled': instance['are_legacy_imds_endpoints_disabled'],
                    'platform_type': instance['platform_type'],
                    'platform_is_secure_boot_enabled': instance['platform_is_secure_boot_enabled'],
                    'platform_is_trusted_platform_module_enabled': instance['platform_is_trusted_platform_module_enabled'],
                    'platform_is_measured_boot_enabled': instance['platform_is_measured_boot_enabled'],
                    'platform_is_memory_encryption_enabled': instance['platform_is_memory_encryption_enabled'],
                    'capacity_reservation_id': instance['capacity_reservation_id'],
                    'dedicated_vm_host_id': instance['dedicated_vm_host_id'],
                    'ipxe_script': instance['ipxe_script'],
                    'launch_mode': instance['launch_mode'],
                    'is_cross_numa_node': instance['is_cross_numa_node'],
                    'licensing_configs': instance['licensing_configs'],
                    'logs': self.service.get_logging_log(instance['id'])
                }

                # boot volumes attachments
                boot_vol_attachement = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_BOOT_VOL_ATTACH, 'instance_id', instance['id'])

                bv = []
                for bva in boot_vol_attachement:
                    bvval = self.__get_core_block_volume_boot(bva, instance['compartment_name'])
                    if 'display_name' in bvval:
                        bv.append(bvval)

                inst['boot_volume'] = bv

                # Volumes attachements
                block_vol_attaches = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_VOLUME_ATTACH, 'instance_id', instance['id'])

                bvol = []
                for bvola in block_vol_attaches:
                    if bvola['lifecycle_state'] == "ATTACHED":
                        bvval = self.__get_core_block_volume(bvola, instance['compartment_name'])
                        if 'display_name' in bvval:
                            bvol.append(bvval)

                inst['block_volume'] = bvol

                # vnic attachements
                vnicas = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_VNIC_ATTACH, 'instance_id', instance['id'])

                vnicdata = []
                fqdn = ""
                for vnic in vnicas:

                    # handle compartment
                    comp_text = ""
                    if vnic['compartment_name'] != compartment['name']:
                        comp_text = " (Compartment=" + vnic['compartment_name'] + ")"

                    if 'vnic_details' in vnic:
                        if 'name' in vnic['vnic_details']:
                            val = {
                                'id': vnic['vnic_id'],
                                'desc': vnic['vnic_details']['name'] + str(comp_text),
                                'details': vnic['vnic_details']
                            }
                            if vnic['vnic_details'] and 'internal_fqdn' in vnic['vnic_details']:
                                if vnic['vnic_details']['internal_fqdn']:
                                    fqdn = vnic['vnic_details']['internal_fqdn']
                            if 'ip_addresses' in vnic['vnic_details']:
                                val['ip_addresses'] = vnic['vnic_details']['ip_addresses']

                            vnicdata.append(val)

                inst['vnic'] = vnicdata

                # if user has inspect, display_name is empty, then take it from the vnic fqdn
                if instance['display_name'] == 'None' and fqdn:
                    host_name = str(fqdn.split(".")[0])
                    inst['name'] = instance['shape'] + " - " + host_name + " - " + instance['lifecycle_state']
                    inst['display_name'] = host_name

                # add instance to data
                data.append(inst)

            # return data
            return data

        except BaseException as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Get compute images
    ##########################################################################
    def __get_core_compute_images(self, region_name, compartment):

        data = []
        try:
            images = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_IMAGES, 'region_name', region_name, 'compartment_id', compartment['id'])

            for image in images:
                value = {'id': image['id'],
                         'desc': image['display_name'].ljust(24) + " - " + image['operating_system'] + " - " + image['size_in_gbs'].rjust(3) + "GB - Base:  " + image['base_image_name'],
                         'sum_info': 'Object Storage - Images (GB)',
                         'sum_size_gb': image['size_in_gbs'],
                         'sum_count_info': "Compute - Images (Count)",
                         'sum_count_size': "1",
                         'time_created': image['time_created'],
                         'defined_tags': image['defined_tags'],
                         'freeform_tags': image['freeform_tags'],
                         'compartment_name': image['compartment_name'],
                         'compartment_path': image['compartment_path'],
                         'compartment_id': image['compartment_id']
                         }
                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Get compute images
    ##########################################################################
    def __get_core_compute_capacity_reservation(self, region_name, compartment):

        data = []
        try:
            array = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_CAPACITY_RESERVATION, 'region_name', region_name, 'compartment_id', compartment['id'])

            for arr in array:
                value = {'id': arr['id'],
                         'display_name': arr['display_name'],
                         'lifecycle_state': arr['lifecycle_state'],
                         'availability_domain': arr['availability_domain'],
                         'is_default_reservation': arr['is_default_reservation'],
                         'time_created': arr['time_created'],
                         'reserved_instance_count': arr['reserved_instance_count'],
                         'used_instance_count': arr['used_instance_count'],
                         'instances': arr['instances'],
                         'config': arr['config'],
                         'sum_size_gb': arr['reserved_instance_count'],
                         'sum_info': "Compute - Capacity Reservation Instances",
                         'defined_tags': arr['defined_tags'],
                         'freeform_tags': arr['freeform_tags'],
                         'compartment_name': arr['compartment_name'],
                         'compartment_path': arr['compartment_path'],
                         'compartment_id': arr['compartment_id']
                         }
                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print compute instance configuration
    ##########################################################################
    def __get_core_compute_instance_configuration(self, region_name, compartment):

        data = []
        try:
            configs = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_INST_CONFIG, 'region_name', region_name, 'compartment_id', compartment['id'])

            for config in configs:

                # add block volumes if not 0
                block_volumes = ""
                if config['block_volumes'] and config['block_volumes'] != "0":
                    block_volumes = " - " + config['block_volumes'] + " Block Volumes"

                # add secondary_vnics if not 0
                secondary_vnics = ""
                if config['secondary_vnics'] and config['secondary_vnics'] != "0":
                    secondary_vnics = " - " + config['secondary_vnics'] + " Secondary vnics"

                value = {'id': config['id'], 'name': config['name'],
                         'shape': config['compute_shape'] + block_volumes + secondary_vnics,
                         'source': config['compute_source']}
                data.append(value)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get compute instance pool
    ##########################################################################
    def __get_core_compute_instance_pool(self, region_name, compartment):

        data = []
        try:

            pools = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_INST_POOL, 'region_name', region_name, 'compartment_id', compartment['id'])

            for pool in pools:
                value = {'id': pool['id'], 'availability_domains': pool['availability_domains'],
                         'name': str(pool['display_name']) + " - " + str(pool['lifecycle_state']) + " - Size: " + str(
                             pool['size']), 'instance_configuration_id': pool['instance_configuration_id'],
                         'instance_configuration_name': pool['instance_configuration_name']}
                data.append(value)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get compute autoscaling
    ##########################################################################
    def __get_core_compute_autoscaling(self, region_name, compartment):

        data = []
        try:

            autos = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_AUTOSCALING, 'region_name', region_name, 'compartment_id', compartment['id'])

            for auto in autos:
                value = {'id': auto['id'],
                         'name': str(auto['display_name']) + " (" + ("ENABLED" if auto['is_enabled'] else "DISABLED") + ")",
                         'time_created': auto['time_created'],
                         'compartment_name': auto['compartment_name'],
                         'compartment_path': auto['compartment_path'],
                         'compartment_id': auto['compartment_id'],
                         'resource_id': auto['resource_id'],
                         'resource_name': auto['resource_name'],
                         'resource_type': auto['resource_type'],
                         'policies': auto['policies']
                         }
                data.append(value)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Compute
    ##########################################################################
    #
    # TBD - list_volume_group_backups
    ##########################################################################

    def __get_core_compute_main(self, region_name, compartment):
        return_data = {}

        try:

            data = self.__get_core_compute_instances(region_name, compartment)
            if len(data) > 0:
                return_data['instances'] = data

            data = self.__get_core_compute_images(region_name, compartment)
            if len(data) > 0:
                return_data['images'] = data

            data = self.__get_core_compute_capacity_reservation(region_name, compartment)
            if len(data) > 0:
                return_data['capacity_reservation'] = data

            data = self.__get_core_compute_instance_configuration(region_name, compartment)
            if len(data) > 0:
                return_data['instance_configuration'] = data

            data = self.__get_core_compute_instance_pool(region_name, compartment)
            if len(data) > 0:
                return_data['instance_pool'] = data

            data = self.__get_core_compute_autoscaling(region_name, compartment)
            if len(data) > 0:
                return_data['autoscaling'] = data

            data = self.__get_core_block_volume_groups(region_name, compartment)
            if len(data) > 0:
                return_data['volume_groups'] = data

            data = self.__get_core_block_boot_not_attached(region_name, compartment)
            if len(data) > 0:
                return_data['boot_not_attached'] = data

            data = self.__get_core_block_volume_not_attached(region_name, compartment)
            if len(data) > 0:
                return_data['volume_not_attached'] = data

            data = self.__get_core_block_volume_boot_backup(region_name, compartment, 'boot_volume', self.service.C_BLOCK_BOOTBACK)
            if len(data) > 0:
                return_data['boot_volume_backup'] = data

            data = self.__get_core_block_volume_boot_backup(region_name, compartment, 'volume', self.service.C_BLOCK_VOLBACK)
            if len(data) > 0:
                return_data['volume_backup'] = data

            data = self.__get_core_block_volume_boot_backup(region_name, compartment, 'volume_group', self.service.C_BLOCK_VOLGRPBACK)
            if len(data) > 0:
                return_data['volume_group_backup'] = data

            return return_data

        except Exception as e:
            self.__print_error(e)
            return return_data

    ##########################################################################
    # print database db nodes
    ##########################################################################
    def __get_database_db_nodes(self, db_nodes):

        data = []
        try:
            for db_node in db_nodes:

                ip_desc = ""
                nsg_names = ""
                nsg_ids = ""
                if 'host_ip' in db_node:
                    if db_node['host_ip']:
                        ip_desc = " - " + db_node['host_ip']

                if 'vnic_details' in db_node:

                    if 'dbdesc' in db_node['vnic_details'] and not ip_desc:
                        ip_desc = " - " + db_node['vnic_details']['dbdesc']

                    if 'nsg_names' in db_node['vnic_details']:
                        nsg_names = db_node['vnic_details']['nsg_names']

                    if 'nsg_ids' in db_node['vnic_details']:
                        nsg_ids = db_node['vnic_details']['nsg_ids']

                value = {
                    'desc': "",
                    'software_storage_size_in_gb': db_node['software_storage_size_in_gb'],
                    'lifecycle_state': db_node['lifecycle_state'],
                    'hostname': db_node['hostname'],
                    'nsg_ids': nsg_ids,
                    'nsg_names': nsg_names,
                    'vnic_id': db_node['vnic_id'],
                    'backup_vnic_id': db_node['backup_vnic_id'],
                    'vnic_details': db_node['vnic_details'],
                    'backup_vnic_details': db_node['backup_vnic_details'],
                    'maintenance_type': db_node['maintenance_type'],
                    'time_maintenance_window_start': db_node['time_maintenance_window_start'],
                    'time_maintenance_window_end': db_node['time_maintenance_window_end'],
                    'fault_domain': db_node['fault_domain'],
                    'cpu_core_count': db_node['cpu_core_count'],
                    'memory_size_in_gbs': db_node['memory_size_in_gbs'],
                    'db_node_storage_size_in_gbs': db_node['db_node_storage_size_in_gbs'],
                    'db_server_id': str(db_node['db_server_id']),
                    'db_server_name': "",
                    # Added 4/5/2024
                    'host_ip_id': db_node['host_ip_id'],
                    'host_ip': db_node['host_ip'],
                    'backup_ip_id': db_node['backup_ip_id'],
                    'backup_ip': db_node['backup_ip'],
                    'vnic2_id': db_node['vnic2_id'],
                    'vnic2_details': db_node['vnic2_details'],
                    'backup_vnic2_id': db_node['backup_vnic2_id'],
                    'backup_vnic2_details': db_node['backup_vnic2_details'],
                    'time_created': db_node['time_created'],
                    'defined_tags': db_node['defined_tags'],
                    'freeform_tags': db_node['freeform_tags']
                }

                # get db server name
                dbserver_info = ""
                if db_node['db_server_id']:
                    dbserver = self.service.search_unique_item(self.service.C_DATABASE, self.service.C_DATABASE_EXACC_DBSERVERS, 'id', db_node['db_server_id'])
                    if dbserver:
                        value['db_server_name'] = dbserver['display_name']
                        dbserver_info = " (" + dbserver['display_name'] + ")"

                # cpu + mem
                cpu_info = ""
                if db_node['cpu_core_count']:
                    cpu_info = " - Cores: " + db_node['cpu_core_count']
                if db_node['memory_size_in_gbs']:
                    cpu_info += " - Mem: " + db_node['memory_size_in_gbs']
                if db_node['db_node_storage_size_in_gbs']:
                    cpu_info += " - Disk: " + db_node['db_node_storage_size_in_gbs']

                lifecycle = (" - " + str(db_node['lifecycle_state'])) if db_node['lifecycle_state'] else ""
                fault_domain = ("" if db_node['fault_domain'] == "" else " - " + str(db_node['fault_domain']))

                # desc
                value['desc'] = str(db_node['hostname']) + dbserver_info + lifecycle + cpu_info + ip_desc + fault_domain + " - " + db_node['time_created']

                data.append(value)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_db_databases
    ##########################################################################
    def __get_database_db_databases(self, dbs):

        data = []
        try:

            for db in dbs:

                backupstr = (" - AutoBck=Y" if db['auto_backup_enabled'] else " - AutoBck=N")
                pdb_name = db['pdb_name'] + " - " if db['pdb_name'] else ""
                value = {
                    'name': (
                        str(db['db_name']) + " - " + str(db['db_unique_name']) + " - " +
                        pdb_name +
                        str(db['db_workload']) + " - " +
                        str(db['character_set']) + " - " +
                        str(db['ncharacter_set']) + " - " +
                        str(db['lifecycle_state']) + backupstr
                    ),
                    'backups': self.__get_database_db_backups(db['backups']) if 'backups' in db else [],
                    'pdbs': self.__get_database_db_pdbs(db['pdbs']) if 'pdbs' in db else [],
                    'time_created': db['time_created'],
                    'defined_tags': db['defined_tags'],
                    'dataguard': self.__get_database_db_dataguard(db['dataguard']),
                    'freeform_tags': db['freeform_tags'],
                    'db_name': db['db_name'],
                    'pdb_name': pdb_name,
                    'db_workload': db['db_workload'],
                    'character_set': db['character_set'],
                    'ncharacter_set': db['ncharacter_set'],
                    'db_unique_name': db['db_unique_name'],
                    'lifecycle_state': db['lifecycle_state'],
                    'auto_backup_enabled': db['auto_backup_enabled'],
                    'connection_strings_cdb': db['connection_strings_cdb'],
                    'source_database_point_in_time_recovery_timestamp': db['source_database_point_in_time_recovery_timestamp'],
                    'kms_key_id': db['kms_key_id'],
                    'kms_key_name': self.__get_vault_key_name(db['kms_key_id']),
                    'vault_id': db['vault_id'],
                    'last_backup_timestamp': db['last_backup_timestamp'],
                    'id': db['id'],
                    # Added 11/15/2024
                    'kms_key_version_id': db['kms_key_version_id'],
                    'key_store_id': db['key_store_id'],
                    'key_store_wallet_name': db['key_store_wallet_name'],
                    'last_failed_backup_timestamp': db['last_failed_backup_timestamp'],
                    'last_backup_duration_in_seconds': db['last_backup_duration_in_seconds'],
                    'db_backup_config': db['db_backup_config']
                }

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __get_database_db_patches(self, patches):

        data = []
        try:
            for dbp in patches:
                data.append(str(dbp['description']) + " - " + str(dbp['version']) + " - " + str(dbp['time_released'])[0:10] + " - Last Action: " + str(dbp['last_action']))
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get db system patches history
    ##########################################################################
    def __get_database_db_patches_history(self, patches_history):

        data = []
        try:
            for dbp in patches_history:
                data.append(str(dbp['description']) + " - " + str(dbp['lifecycle_state']) + " - " + str(dbp['time_started'])[0:10] + " - " + str(dbp['time_ended'])[0:10] + " - Last Action: " + str(dbp['action']))
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print database db backups
    ##########################################################################
    def __get_database_db_backups(self, backups):

        data = []
        try:

            for backup in backups:
                bsize = ""
                if backup['database_size_in_gbs']:
                    bsize = "{0:.1f}".format(round(float(backup['database_size_in_gbs']), 1)) + "GB"

                data.append(
                    {
                        'name': str(backup['display_name']) + " - " + str(backup['type']) + " - " + str(backup['lifecycle_state']),
                        'time': str(backup['time_started'])[0:16] + " - " + str(backup['time_ended'])[0:16],
                        'size': bsize,
                        'id': backup['id'],
                        'display_name': backup['display_name'],
                        'lifecycle_state': backup['lifecycle_state'],
                        'availability_domain': backup['availability_domain'],
                        'database_edition': backup['database_edition'],
                        'shape': backup['shape'],
                        'version': backup['version'],
                        'kms_key_id': backup['kms_key_id'],
                        'kms_key_name': self.__get_vault_key_name(backup['kms_key_id']),
                        'kms_key_version_id': backup['kms_key_version_id'],
                        'vault_id': backup['vault_id'],
                        'type': backup['type'],
                        # The database size in gbs is not bakcup size, empty the backup size
                        # 'sum_info': 'Object Storage - DB Backup (GB)',
                        'sum_size_gb': "",
                        'database_size_in_gbs': bsize,
                        'database_id': backup['database_id'],
                        'compartment_id': backup['compartment_id'],
                        'compartment_name': backup['compartment_name'],
                        'compartment_path': backup['compartment_path'],
                        'region_name': backup['region_name']})
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print database db pdbs
    ##########################################################################
    def __get_database_db_pdbs(self, pdbs):

        data = []
        try:

            for pdb in pdbs:
                data.append(
                    {
                        'id': pdb['id'],
                        'name': pdb['pdb_name'],
                        'desc': pdb['pdb_name'] + " " + pdb['open_mode'],
                        'lifecycle_state': pdb['lifecycle_state'],
                        'open_mode': pdb['open_mode'],
                        'connection_strings': pdb['connection_strings'],
                        'is_restricted': pdb['is_restricted'],
                        'management_status': pdb['management_status'],
                        'is_refreshable_clone': pdb['is_refreshable_clone'],
                        'time_created': pdb['time_created'],
                        'defined_tags': pdb['defined_tags'],
                        'freeform_tags': pdb['freeform_tags']})
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_db_homes
    ##########################################################################
    def __get_database_db_homes(self, db_homes):

        data = []
        try:
            for db_home in db_homes:
                data.append(
                    {'id': str(db_home['id']),
                     'home': str(db_home['display_name']) + " - " + str(db_home['db_version']),
                     'home_name': str(db_home['display_name']),
                     'home_version': str(db_home['db_version']),
                     'databases': self.__get_database_db_databases(db_home['databases']),
                     'patches': self.__get_database_db_patches(db_home['patches']),
                     'patches_history': self.__get_database_db_patches_history(db_home['patches_history'])
                     })

            # add to main data
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_db_dataguard
    ##########################################################################
    def __get_database_db_dataguard(self, dataguards):

        data = []
        try:
            for dg in dataguards:

                # add data
                data.append(
                    {'id': str(dg['id']),
                     'database_id': str(dg['database_id']),
                     'peer_name': str(dg['db_name']),
                     'lifecycle_state': str(dg['lifecycle_state']),
                     'peer_data_guard_association_id': str(dg['peer_data_guard_association_id']),
                     'name': "Dataguard: " + dg['role'] + ", " + dg['protection_mode'] + " (" + dg['transport_type'] + "), Peer DB: " + dg['db_name'],
                     'apply_rate': str(dg['apply_rate']),
                     'apply_lag': str(dg['apply_lag']),
                     'peer_role': str(dg['peer_role']),
                     'protection_mode': str(dg['protection_mode']),
                     'transport_type': str(dg['transport_type']),
                     'time_created': str(dg['time_created']),
                     })

            # add to main data
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Exadata Infra
    ##########################################################################
    def __get_database_db_exadata(self, region_name, compartment):

        data = []
        try:
            list_exas = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXADATA, 'region_name', region_name, 'compartment_id', compartment['id'])

            for dbs in list_exas:
                config_str = ' D' + dbs['compute_count'] + 'S' + dbs['storage_count'] if dbs['compute_count'] else ""
                value = {
                    'id': dbs['id'],
                    'display_name': dbs['display_name'],
                    'shape': dbs['shape'],
                    'shape_ocpu': dbs['shape_ocpu'],
                    'shape_memory_gb': dbs['shape_memory_gb'],
                    'shape_storage_tb': dbs['shape_storage_tb'],
                    'version': dbs['version'],
                    'lifecycle_state': dbs['lifecycle_state'],
                    'lifecycle_details': dbs['lifecycle_details'],
                    'availability_domain': dbs['availability_domain'],
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
                    'customer_contacts': dbs['customer_contacts'],
                    'defined_file_system_configurations': dbs['defined_file_system_configurations'],
                    # End Added 7/29/2024
                    'compute_count': dbs['compute_count'],
                    'storage_count': dbs['storage_count'],
                    'total_storage_size_in_gbs': dbs['total_storage_size_in_gbs'],
                    'available_storage_size_in_gbs': dbs['available_storage_size_in_gbs'],
                    'compartment_name': dbs['compartment_name'],
                    'compartment_path': dbs['compartment_path'],
                    'compartment_id': dbs['compartment_id'],
                    'time_created': dbs['time_created'],
                    'last_maintenance_run': dbs['last_maintenance_run'],
                    'next_maintenance_run': dbs['next_maintenance_run'],
                    'maintenance_window': dbs['maintenance_window'],
                    'defined_tags': dbs['defined_tags'],
                    'freeform_tags': dbs['freeform_tags'],
                    'region_name': dbs['region_name'],
                    'name': dbs['display_name'] + " - " + dbs['shape'] + config_str + " - " + dbs['lifecycle_state'],
                    'sum_info': 'Database ExaCS Infra - ' + dbs['shape'] + config_str,
                    'sum_info_storage': 'Database - Storage (GB)',
                    'sum_size_gb': dbs['total_storage_size_in_gbs'],
                    'data': str(dbs['available_storage_size_in_gbs']) + "GB",
                    'db_servers': [] if not dbs['db_servers'] else sorted(dbs['db_servers'], key=lambda i: i['desc']),
                    'vm_clusters': [],
                    'adb_clusters': self.__get_database_adb_dedicated(region_name, compartment, dbs['id'])
                }

                list_vms = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXADATA_VMS, 'region_name', region_name, 'cloud_exadata_infrastructure_id', dbs['id'])
                if list_vms:
                    for vm in list_vms:
                        db_nodes = self.__get_database_db_nodes(vm['db_nodes'])
                        valvm = {
                            'id': vm['id'],
                            'cluster_name': vm['cluster_name'],
                            'hostname': vm['hostname'],
                            'compartment_id': vm['compartment_id'],
                            'availability_domain': vm['availability_domain'],
                            'data_subnet_id': vm['data_subnet_id'],
                            'data_subnet': vm['data_subnet'],
                            'data_subnet_name': vm['data_subnet_name'],
                            'data_vcn_name': vm['data_vcn_name'],
                            'backup_subnet_id': vm['backup_subnet_id'],
                            'backup_subnet': vm['backup_subnet'],
                            'backup_subnet_name': vm['backup_subnet_name'],
                            'backup_vcn_name': vm['backup_vcn_name'],
                            'nsg_ids': vm['nsg_ids'],
                            'nsg_names': vm['nsg_names'],
                            'backup_network_nsg_ids': vm['backup_network_nsg_ids'],
                            'backup_network_nsg_names': vm['backup_network_nsg_names'],
                            'last_update_history_entry_id': vm['last_update_history_entry_id'],
                            'shape': vm['shape'],
                            'listener_port': vm['listener_port'],
                            'lifecycle_state': vm['lifecycle_state'],
                            'node_count': vm['node_count'],
                            'storage_size_in_gbs': vm['storage_size_in_gbs'],
                            'display_name': vm['display_name'],
                            'time_created': vm['time_created'],
                            'lifecycle_details': vm['lifecycle_details'],
                            'time_zone': vm['time_zone'],
                            'domain': vm['domain'],
                            'cpu_core_count': vm['cpu_core_count'],
                            'data_storage_percentage': vm['data_storage_percentage'],
                            'is_local_backup_enabled': vm['is_local_backup_enabled'],
                            'is_sparse_diskgroup_enabled': vm['is_sparse_diskgroup_enabled'],
                            'gi_version': vm['gi_version'],
                            'gi_version_date': vm['gi_version_date'],
                            'system_version': vm['system_version'],
                            'system_version_date': vm['system_version_date'],
                            'ssh_public_keys': vm['ssh_public_keys'],
                            'license_model': vm['license_model'],
                            'disk_redundancy': vm['disk_redundancy'],
                            'scan_ip_ids': vm['scan_ip_ids'],
                            'scan_ips': vm['scan_ips'],
                            'vip_ids': vm['vip_ids'],
                            'vip_ips': vm['vip_ips'],
                            'scan_dns_record_id': vm['scan_dns_record_id'],
                            # Added 7/29/2024
                            'subscription_id': vm['subscription_id'],
                            'is_diagnostics_events_enabled': vm['is_diagnostics_events_enabled'],
                            'is_health_monitoring_enabled': vm['is_health_monitoring_enabled'],
                            'is_incident_logs_enabled': vm['is_incident_logs_enabled'],
                            'gi_software_image_id': vm['gi_software_image_id'],
                            'scan_listener_port_tcp_ssl': vm['scan_listener_port_tcp_ssl'],
                            'scan_listener_port_tcp': vm['scan_listener_port_tcp'],
                            'file_system_configuration_details': vm['file_system_configuration_details'],
                            # End Added 7/29/2024
                            'defined_tags': vm['defined_tags'],
                            'freeform_tags': vm['freeform_tags'],
                            'sum_info': 'Database ExaCS VMCluster - ' + dbs['shape'] + " - " + vm['license_model'],
                            'sum_info_storage': 'Database - Storage (GB)',
                            'sum_size_gb': vm['storage_size_in_gbs'],
                            'patches': self.__get_database_db_patches(vm['patches']),
                            'db_homes': self.__get_database_db_homes(vm['db_homes']),
                            'db_nodes': [] if not db_nodes else sorted(db_nodes, key=lambda i: i['desc']),
                            'scan_dns_name': vm['scan_dns_name'],
                            'zone_id': vm['zone_id'],
                            'compartment_name': vm['compartment_name'],
                            'compartment_path': vm['compartment_path'],
                            'region_name': vm['region_name']
                        }
                        value['vm_clusters'].append(valvm)

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Exacc Infra
    ##########################################################################
    def __get_database_db_exacc(self, region_name, compartment):

        data = []
        try:
            list_exas = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXACC, 'region_name', region_name, 'compartment_id', compartment['id'])

            for dbs in list_exas:
                config_str = ' D' + dbs['compute_count'] + 'S' + dbs['activated_storage_count'] if dbs['compute_count'] else ""
                value = {
                    'id': dbs['id'],
                    'display_name': dbs['display_name'],
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
                    'storage_count': dbs['storage_count'],
                    'additional_storage_count': dbs['additional_storage_count'],
                    'activated_storage_count': dbs['activated_storage_count'],
                    'compute_count': dbs['compute_count'],
                    'cloud_control_plane_server1': dbs['cloud_control_plane_server1'],
                    'cloud_control_plane_server2': dbs['cloud_control_plane_server2'],
                    'netmask': dbs['netmask'],
                    'gateway': dbs['gateway'],
                    'admin_network_cidr': dbs['admin_network_cidr'],
                    'infini_band_network_cidr': dbs['infini_band_network_cidr'],
                    'corporate_proxy': dbs['corporate_proxy'],
                    'dns_server': dbs['dns_server'],
                    'ntp_server': dbs['ntp_server'],
                    'time_created': dbs['time_created'],
                    'lifecycle_state': dbs['lifecycle_state'],
                    'lifecycle_details': dbs['lifecycle_details'],
                    'csi_number': dbs['csi_number'],
                    'maintenance_slo_status': dbs['maintenance_slo_status'],
                    'last_maintenance_run': dbs['last_maintenance_run'],
                    'next_maintenance_run': dbs['next_maintenance_run'],
                    'maintenance_window': dbs['maintenance_window'],
                    'defined_tags': dbs['defined_tags'],
                    'freeform_tags': dbs['freeform_tags'],
                    'contacts': dbs['contacts'],
                    'compartment_name': dbs['compartment_name'],
                    'compartment_path': dbs['compartment_path'],
                    'compartment_id': dbs['compartment_id'],
                    'region_name': dbs['region_name'],
                    'sum_info': 'Database ExaCC Infra - ' + dbs['shape'],
                    'sum_info_storage': 'Database - Storage (GB)',
                    'sum_size_gb': dbs['max_data_storage_in_t_bs'],
                    'vm_clusters': [],
                    'adb_clusters': self.__get_database_db_exacc_adb_dedicated(region_name, compartment, dbs['id']),
                    'db_servers': [] if not dbs['db_servers'] else sorted(dbs['db_servers'], key=lambda i: i['desc']),
                    'name': dbs['display_name'] + " - " + dbs['shape'] + config_str + " - " + dbs['lifecycle_state']
                }

                list_vms = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXACC_VMS, 'region_name', region_name, 'exadata_infrastructure_id', dbs['id'])
                if list_vms:
                    for vm in list_vms:
                        db_nodes = self.__get_database_db_nodes(vm['db_nodes'])
                        valvm = {
                            'id': vm['id'],
                            'last_patch_history_entry_id': vm['last_patch_history_entry_id'],
                            'lifecycle_state': vm['lifecycle_state'],
                            'display_name': vm['display_name'],
                            'time_created': vm['time_created'],
                            'lifecycle_details': vm['lifecycle_details'],
                            'time_zone': vm['time_zone'],
                            'is_local_backup_enabled': vm['is_local_backup_enabled'],
                            'exadata_infrastructure_id': vm['exadata_infrastructure_id'],
                            'is_sparse_diskgroup_enabled': vm['is_sparse_diskgroup_enabled'],
                            'vm_cluster_network_id': vm['vm_cluster_network_id'],
                            'cpus_enabled': vm['cpus_enabled'],
                            'memory_size_in_gbs': vm['memory_size_in_gbs'],
                            'db_node_storage_size_in_gbs': vm['db_node_storage_size_in_gbs'],
                            'data_storage_size_in_tbs': vm['data_storage_size_in_tbs'],
                            'shape': vm['shape'],
                            'gi_version': vm['gi_version'],
                            'gi_version_date': vm['gi_version_date'],
                            'system_version': vm['system_version'],
                            'system_version_date': vm['system_version_date'],
                            'license_model': vm['license_model'],
                            'defined_tags': vm['defined_tags'],
                            'freeform_tags': vm['freeform_tags'],
                            'sum_info': 'Database ExaCC VMCluster - ' + dbs['shape'] + " - " + vm['license_model'],
                            'sum_info_storage': 'Database - Storage (GB)',
                            'sum_size_gb': vm['db_node_storage_size_in_gbs'],
                            'patches': self.__get_database_db_patches(vm['patches']),
                            'db_homes': self.__get_database_db_homes(vm['db_homes']),
                            'db_nodes': [] if not db_nodes else sorted(db_nodes, key=lambda i: i['desc']),
                            'compartment_name': vm['compartment_name'],
                            'compartment_path': vm['compartment_path'],
                            'compartment_id': vm['compartment_id'],
                            'region_name': vm['region_name']
                        }
                        value['vm_clusters'].append(valvm)

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # ExaCC Autonomous Dedicated Infra
    ##########################################################################
    def __get_database_db_exacc_adb_dedicated(self, region_name, compartment, infra_id):

        data = []
        try:

            # Fetch the vmclusters
            vms = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXACC_ADB_VMS, 'region_name', region_name, 'exadata_infrastructure_id', infra_id)
            for vm in vms:
                vmval = {
                    'id': vm['id'],
                    'display_name': vm['display_name'],
                    'description': vm['description'],
                    'last_update_history_entry_id': vm['last_update_history_entry_id'],
                    'lifecycle_state': vm['lifecycle_state'],
                    'lifecycle_details': vm['lifecycle_details'],
                    'time_created': vm['time_created'],
                    'time_zone': vm['time_zone'],
                    'shape': vm['shape'],
                    'exadata_infrastructure_id': vm['exadata_infrastructure_id'],
                    'vm_cluster_network_id': vm['vm_cluster_network_id'],
                    'is_local_backup_enabled': vm['is_local_backup_enabled'],
                    'cpus_enabled': vm['cpus_enabled'],
                    'ocpus_enabled': vm['ocpus_enabled'],
                    'available_cpus': vm['available_cpus'],
                    'total_container_databases': vm['total_container_databases'],
                    'memory_per_oracle_compute_unit_in_gbs': vm['memory_per_oracle_compute_unit_in_gbs'],
                    'cpu_core_count_per_node': vm['cpu_core_count_per_node'],
                    'autonomous_data_storage_size_in_tbs': vm['autonomous_data_storage_size_in_tbs'],
                    'memory_size_in_gbs': vm['memory_size_in_gbs'],
                    'db_node_storage_size_in_gbs': vm['db_node_storage_size_in_gbs'],
                    'data_storage_size_in_tbs': vm['data_storage_size_in_tbs'],
                    'data_storage_size_in_gbs': vm['data_storage_size_in_gbs'],
                    'available_data_storage_size_in_tbs': vm['available_data_storage_size_in_tbs'],
                    'available_container_databases': vm['available_container_databases'],
                    'reclaimable_cpus': vm['reclaimable_cpus'],
                    'available_autonomous_data_storage_size_in_tbs': vm['available_autonomous_data_storage_size_in_tbs'],
                    'scan_listener_port_tls': vm['scan_listener_port_tls'],
                    'scan_listener_port_non_tls': vm['scan_listener_port_non_tls'],
                    'is_mtls_enabled': vm['is_mtls_enabled'],
                    'defined_tags': vm['defined_tags'],
                    'freeform_tags': vm['freeform_tags'],
                    'compute_model': vm['compute_model'],
                    'sum_info': 'Database ExaCC ADB VM ' + vm['license_model'],
                    'sum_info_storage': 'Database - Storage (GB)',
                    'sum_size_gb': vm['db_node_storage_size_in_gbs'],
                    'compartment_name': vm['compartment_name'],
                    'compartment_path': vm['compartment_path'],
                    'compartment_id': vm['compartment_id'],
                    'region_name': vm['region_name'],
                    'containers': []
                }

                # fetch the containers
                containers = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_ADB_D_CONTAINERS, 'autonomous_vm_cluster_id', vm['id'])
                for ct in containers:
                    ct['name'] = ct['display_name'] + " (" + ct['lifecycle_state'] + "), " + ct['db_version'] + ", Patch Model : " + ct['patch_model']
                    ct['databases'] = []

                    # Add Databases
                    databases = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_ADB_DATABASE, 'autonomous_container_database_id', ct['id'])
                    for arr in databases:
                        db = self.__get_database_adb_database_info(arr)
                        db['sum_info'] = "Autonomous Database Dedicated " + str(db['db_workload']) + " (" + db['compute_model'] + "s) - " + vm['license_model']
                        db['sum_info_stopped'] = "Stopped Autonomous Database Dedicated " + str(db['db_workload']) + " (Count) - " + vm['license_model']
                        db['sum_info_count'] = "Autonomous Database Dedicated " + str(db['db_workload']) + " (Count) - " + vm['license_model']
                        db['sum_info_storage'] = "Autonomous Database Dedicated (TB)"
                        ct['databases'].append(db)

                    # Add containers
                    vmval['containers'].append(ct)

                # add the clusters to the infra
                data.append(vmval)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Database Systems
    ##########################################################################
    def __get_database_db_systems(self, region_name, compartment):

        data = []
        try:
            list_db_systems = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_DBSYSTEMS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for dbs in list_db_systems:
                value = {
                    'id': dbs['id'],
                    'name': dbs['display_name'] + " - " + dbs['shape'] + " - " + dbs['lifecycle_state'],
                    'shape': dbs['shape'],
                    'shape_ocpu': dbs['shape_ocpu'],
                    'shape_memory_gb': dbs['shape_memory_gb'],
                    'shape_storage_tb': dbs['shape_storage_tb'],
                    'display_name': dbs['display_name'],
                    'lifecycle_state': dbs['lifecycle_state'],
                    'sum_info': 'Database ' + dbs['database_edition_short'] + " - " + dbs['shape'] + " - " + dbs['license_model'],
                    'sum_info_storage': 'Database - Storage (GB)',
                    'sum_size_gb': dbs['data_storage_size_in_gbs'],
                    'database_edition': dbs['database_edition'],
                    'database_edition_short': dbs['database_edition_short'],
                    'license_model': dbs['license_model'],
                    'database_version': dbs['version'],
                    'availability_domain': dbs['availability_domain'],
                    'cpu_core_count': dbs['cpu_core_count'],
                    'node_count': dbs['node_count'],
                    'version': (dbs['version'] + " - ") if dbs['version'] != "None" else "" + ((dbs['database_edition'] + " - ") if dbs['database_edition'] != "None" else "") + dbs['license_model'],
                    'version_only': dbs['version'],
                    'version_date': dbs['version_date'],
                    'host': dbs['hostname'],
                    'domain': dbs['domain'],
                    'data_subnet_id': dbs['data_subnet_id'],
                    'data_subnet': dbs['data_subnet'],
                    'data_subnet_name': dbs['data_subnet_name'],
                    'data_vcn_name': dbs['data_vcn_name'],
                    'backup_subnet_id': dbs['backup_subnet_id'],
                    'backup_subnet': dbs['backup_subnet'],
                    'backup_subnet_name': dbs['backup_subnet_name'],
                    'backup_vcn_name': dbs['backup_vcn_name'],
                    'scan_dns': dbs['scan_dns_record_id'],
                    'scan_ips': dbs['scan_ips'],
                    'data_storage_size_in_gbs': dbs['data_storage_size_in_gbs'],
                    'reco_storage_size_in_gb': dbs['reco_storage_size_in_gb'],
                    'sparse_diskgroup': dbs['sparse_diskgroup'],
                    'storage_management': dbs['storage_management'],
                    'vip_ips': dbs['vip_ips'],
                    'zone_id': dbs['zone_id'],
                    'scan_dns_name': dbs['scan_dns_name'],
                    'compartment_name': dbs['compartment_name'],
                    'compartment_path': dbs['compartment_path'],
                    'compartment_id': dbs['compartment_id'],
                    'cluster_name': dbs['cluster_name'],
                    'time_created': dbs['time_created'],
                    'defined_tags': dbs['defined_tags'],
                    'freeform_tags': dbs['freeform_tags'],
                    'listener_port': dbs['listener_port'],
                    'last_maintenance_run': dbs['last_maintenance_run'],
                    'next_maintenance_run': dbs['next_maintenance_run'],
                    'maintenance_window': dbs['maintenance_window'],
                    'nsg_ids': dbs['nsg_ids'],
                    'nsg_ids_names': dbs['nsg_ids_names'],
                    'backup_network_nsg_ids': dbs['backup_network_nsg_ids'],
                    'backup_network_nsg_ids_names': dbs['backup_network_nsg_ids_names'],
                    'fault_domains': dbs['fault_domains'],
                    'memory_size_in_gbs': dbs['memory_size_in_gbs'],
                    'storage_volume_performance_mode': dbs['storage_volume_performance_mode'],
                    'time_zone': dbs['time_zone'],
                    'kms_key_id': dbs['kms_key_id'],
                    'kms_key_name': self.__get_vault_key_name(dbs['kms_key_id']),
                    'os_version': dbs['os_version'],
                    'disk_redundancy': dbs['disk_redundancy'],
                    'point_in_time_data_disk_clone_timestamp': dbs['point_in_time_data_disk_clone_timestamp'],
                    'patches': self.__get_database_db_patches(dbs['patches']),
                    'db_homes': self.__get_database_db_homes(dbs['db_homes']),
                    'db_nodes': self.__get_database_db_nodes(dbs['db_nodes'])
                }

                if dbs['data_storage_size_in_gbs']:
                    value['data'] = str(dbs['data_storage_size_in_gbs']) + "GB - " + str(dbs['data_storage_percentage']) + "%" + (" - " + dbs['storage_management'] if dbs['storage_management'] else "") + (" - Reco: " + dbs['reco_storage_size_in_gb'] + "GB" if dbs['reco_storage_size_in_gb'] else "")
                else:
                    value['data'] = str(dbs['data_storage_percentage']) + "%" + (" - " + dbs['storage_management'] if dbs['storage_management'] else "")

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Database All Backups
    ##########################################################################
    def __get_database_db_all_backups(self, region_name, compartment):

        data = []
        try:
            list_db_backups = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_BACKUPS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for backup in list_db_backups:
                ssize = ""
                if backup['database_size_in_gbs']:
                    ssize = "{0:.1f}".format(round(float(backup['database_size_in_gbs']), 1))

                data.append(
                    {
                        'name': str(backup['display_name']) + " - " + str(backup['type']) + " - " + str(backup['lifecycle_state']),
                        'time': str(backup['time_started'])[0:16] + " - " + str(backup['time_ended'])[0:16],
                        'size': "",
                        'id': backup['id'],
                        'display_name': backup['display_name'],
                        'standalone': backup['standalone'],
                        'lifecycle_state': backup['lifecycle_state'],
                        'availability_domain': backup['availability_domain'],
                        'database_edition': backup['database_edition'],
                        'shape': backup['shape'],
                        'version': backup['version'],
                        'kms_key_id': backup['kms_key_id'],
                        'kms_key_name': self.__get_vault_key_name(backup['kms_key_id']),
                        'kms_key_version_id': backup['kms_key_version_id'],
                        'vault_id': backup['vault_id'],
                        'type': backup['type'],
                        'database_id': backup['database_id'],
                        'database_size_in_gbs': ssize,
                        'compartment_name': backup['compartment_name'],
                        'compartment_path': backup['compartment_path'],
                        'compartment_id': backup['compartment_id'],
                        'region_name': backup['region_name']
                    })
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print database db backups
    ##########################################################################
    def __get_database_adb_databases_backups(self, backups):

        data = []
        try:

            for backup in backups:
                backup_type = "Automatic Backup, " if backup['is_automatic'] else "Manual Backup   , "
                data.append(
                    {
                        'name': backup_type + str(backup['display_name']) + " - " + str(backup['type']) + " - " + str(backup['lifecycle_state']),
                        'time': str(backup['time_started'])[0:16] + " - " + str(backup['time_ended'])[0:16],
                        'display_name': backup['display_name'],
                        'lifecycle_state': backup['lifecycle_state'],
                        'type': backup['type'],
                        'id': backup['id'],
                        'kms_key_id': backup['kms_key_id'],
                        'kms_key_name': self.__get_vault_key_name(backup['kms_key_id']),
                        'vault_id': backup['vault_id'],
                        'is_automatic': backup['is_automatic']
                    }
                )
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Autonomous db info
    ##########################################################################
    def __get_database_adb_database_info(self, dbs):

        try:
            freemsg = ",  FreeTier" if dbs['is_free_tier'] else ""
            freesum = "Free " if dbs['is_free_tier'] else ""
            role = (" - " + dbs['role']) if dbs['role'] else ""
            open_mode = (" - " + dbs['open_mode']) if dbs['open_mode'] else ""
            lifecycle = (" - " + dbs['lifecycle_state']) if dbs['lifecycle_state'] else ""
            autoscale = (" AutoScale" if dbs['is_auto_scaling_enabled'] else "")
            compute_count = str(dbs['compute_count']) + " " + dbs['compute_model']
            value = {
                'id': str(dbs['id']),
                'name': str(dbs['db_name']) + " (" + (str(dbs['display_name']) + ") - " + str(dbs['license_model']) + open_mode + role + lifecycle + " (" + compute_count + autoscale + ") - " + dbs['db_workload'] + " - " + dbs['db_type'] + freemsg),
                'display_name': dbs['display_name'],
                'license_model': dbs['license_model'],
                'lifecycle_state': dbs['lifecycle_state'],
                'cpu_core_count': str(dbs['cpu_core_count']),
                'data_storage_size_in_tbs': str(dbs['data_storage_size_in_tbs']),
                'db_name': str(dbs['db_name']),
                'compartment_name': str(dbs['compartment_name']),
                'compartment_path': str(dbs['compartment_path']),
                'compartment_id': str(dbs['compartment_id']),
                'service_console_url': str(dbs['service_console_url']),
                'time_created': str(dbs['time_created'])[0:16],
                'connection_strings': str(dbs['connection_strings']),
                'connection_urls': str(dbs['connection_urls']),
                'sum_info': "Autonomous Database " + freesum + str(dbs['db_workload']) + " " + dbs['compute_model'] + " - " + dbs['license_model'],
                'sum_info_stopped': "Stopped Autonomous Database " + freesum + str(dbs['db_workload']) + " (Count) - " + dbs['license_model'],
                'sum_info_count': "Autonomous Database " + freesum + str(dbs['db_workload']) + " (Count) - " + dbs['license_model'],
                'sum_count': str(dbs['compute_count']),
                'sum_info_storage': "Autonomous Database " + freesum + "(TB)",
                'sum_size_tb': str(dbs['data_storage_size_in_tbs']),
                'whitelisted_ips': dbs['whitelisted_ips'],
                'is_auto_scaling_enabled': dbs['is_auto_scaling_enabled'],
                'db_workload': dbs['db_workload'],
                'is_dedicated': dbs['is_dedicated'],
                'db_version': dbs['db_version'],
                'subnet_id': dbs['subnet_id'],
                'subnet_name': "",
                'data_safe_status': dbs['data_safe_status'],
                'time_maintenance_begin': dbs['time_maintenance_begin'],
                'time_maintenance_end': dbs['time_maintenance_end'],
                'nsg_ids': dbs['nsg_ids'],
                'nsg_names': [],
                'private_endpoint': dbs['private_endpoint'],
                'private_endpoint_label': dbs['private_endpoint_label'],
                'defined_tags': dbs['defined_tags'],
                'freeform_tags': dbs['freeform_tags'],
                'is_free_tier': dbs['is_free_tier'],
                'is_preview': dbs['is_preview'],
                'infrastructure_type': dbs['infrastructure_type'],
                'time_deletion_of_free_autonomous_database': dbs['time_deletion_of_free_autonomous_database'],
                'time_reclamation_of_free_autonomous_database': dbs['time_reclamation_of_free_autonomous_database'],
                'system_tags': dbs['system_tags'],
                'time_of_last_switchover': dbs['time_of_last_switchover'],
                'time_of_last_failover': dbs['time_of_last_failover'],
                'failed_data_recovery_in_seconds': dbs['failed_data_recovery_in_seconds'],
                'available_upgrade_versions': dbs['available_upgrade_versions'],
                'standby_lag_time_in_seconds': dbs['standby_lag_time_in_seconds'],
                'standby_lifecycle_state': dbs['standby_lifecycle_state'],
                'autonomous_container_database_id': dbs['autonomous_container_database_id'],
                'is_data_guard_enabled': dbs['is_data_guard_enabled'],
                'peer_db_ids': dbs['peer_db_ids'],
                'time_data_guard_role_changed': dbs['time_data_guard_role_changed'],
                'time_local_data_guard_enabled': dbs['time_local_data_guard_enabled'],
                'dataguard_region_type': dbs['dataguard_region_type'],
                'customer_contacts': dbs['customer_contacts'],
                'supported_regions_to_clone_to': dbs['supported_regions_to_clone_to'],
                'kms_key_id': dbs['kms_key_id'],
                'kms_key_name': self.__get_vault_key_name(dbs['kms_key_id']),
                'vault_id': dbs['vault_id'],
                'key_store_wallet_name': dbs['key_store_wallet_name'],
                'key_store_id': dbs['key_store_id'],
                'in_memory_percentage': dbs['in_memory_percentage'],
                'role': dbs['role'],
                'in_memory_area_in_gbs': dbs['in_memory_area_in_gbs'],
                'memory_per_oracle_compute_unit_in_gbs': dbs['memory_per_oracle_compute_unit_in_gbs'],
                'next_long_term_backup_time_stamp': dbs['next_long_term_backup_time_stamp'],
                'compute_model': dbs['compute_model'],
                'compute_count': dbs['compute_count'],
                'backup_retention_period_in_days': dbs['backup_retention_period_in_days'],
                'total_backup_storage_size_in_gbs': dbs['total_backup_storage_size_in_gbs'],
                'data_storage_size_in_gbs': dbs['data_storage_size_in_gbs'],
                'used_data_storage_size_in_gbs': dbs['used_data_storage_size_in_gbs'],
                'used_data_storage_size_in_tbs': dbs['used_data_storage_size_in_tbs'],
                'is_refreshable_clone': dbs['is_refreshable_clone'],
                'time_of_last_refresh': dbs['time_of_last_refresh'],
                'time_of_last_refresh_point': dbs['time_of_last_refresh_point'],
                'time_of_next_refresh': dbs['time_of_next_refresh'],
                'open_mode': dbs['open_mode'],
                'refreshable_status': dbs['refreshable_status'],
                'refreshable_mode': dbs['refreshable_mode'],
                'permission_level': dbs['permission_level'],
                'is_local_data_guard_enabled': dbs['is_local_data_guard_enabled'],
                'is_remote_data_guard_enabled': dbs['is_remote_data_guard_enabled'],
                'is_mtls_connection_required': dbs['is_mtls_connection_required'],
                'time_until_reconnect_clone_enabled': dbs['time_until_reconnect_clone_enabled'],
                'is_auto_scaling_for_storage_enabled': dbs['is_auto_scaling_for_storage_enabled'],
                'allocated_storage_size_in_tbs': dbs['allocated_storage_size_in_tbs'],
                'actual_used_data_storage_size_in_tbs': dbs['actual_used_data_storage_size_in_tbs'],
                'database_edition': dbs['database_edition'],
                'local_disaster_recovery_type': dbs['local_disaster_recovery_type'],
                'disaster_recovery_region_type': dbs['disaster_recovery_region_type'],
                'time_disaster_recovery_role_changed': dbs['time_disaster_recovery_role_changed'],
                'are_primary_whitelisted_ips_used': dbs['are_primary_whitelisted_ips_used'],
                'autonomous_maintenance_schedule_type': dbs['autonomous_maintenance_schedule_type'],
                'character_set': dbs['character_set'],
                'ncharacter_set': dbs['ncharacter_set'],
                'database_management_status': dbs['database_management_status'],
                'is_access_control_enabled': dbs['is_access_control_enabled'],
                'is_reconnect_clone_enabled': dbs['is_reconnect_clone_enabled'],
                'kms_key_lifecycle_details': dbs['kms_key_lifecycle_details'],
                'kms_key_version_id': dbs['kms_key_version_id'],
                'local_adg_auto_failover_max_data_loss_limit': dbs['local_adg_auto_failover_max_data_loss_limit'],
                'operations_insights_status': dbs['operations_insights_status'],
                'provisionable_cpus': dbs['provisionable_cpus'],
                'source_id': dbs['source_id'],
                'standby_whitelisted_ips': dbs['standby_whitelisted_ips'],
                'backups': self.__get_database_adb_databases_backups(dbs['backups'])
            }

            # subnet
            if dbs['subnet_id'] != 'None':
                value['subnet_name'] = self.__get_core_network_subnet_name(dbs['subnet_id'])

            # get the nsg names
            if dbs['nsg_ids']:
                for nsg in dbs['nsg_ids']:
                    nsg_obj = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_NSG, 'id', nsg)
                    if nsg_obj:
                        value['nsg_names'].append(nsg_obj['name'])

            return value

        except Exception as e:
            self.__print_error(e)
            return {}

    ##########################################################################
    # Autonomous
    ##########################################################################
    def __get_database_adb_databases(self, region_name, compartment):

        data = []
        try:
            list_autos = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_ADB_DATABASE, 'region_name', region_name, 'compartment_id', compartment['id'])

            for dbs in list_autos:

                # if dedicated skip, it will be under containers
                if dbs['is_dedicated']:
                    continue

                data.append(self.__get_database_adb_database_info(dbs))
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Exascale Vaults
    ##########################################################################
    def __get_database_exascale_vaults(self, region_name, compartment):

        data = []
        try:
            list_exascale_vaults = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXASCALE_VAULT, 'region_name', region_name, 'compartment_id', compartment['id'])
            for vault in list_exascale_vaults:

                list_vms = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXASCALE_VMS, 'region_name', region_name, 'exascale_db_storage_vault_id', vault['id'])
                if list_vms:
                    for vm in list_vms:
                        db_nodes = self.__get_database_db_nodes(vm['db_nodes'])
                        valvm = vm
                        valvm['sum_info'] = 'Database Exascale VMCluster - ' + vm['license_model']
                        valvm['sum_size_gb'] = vm['enabled_e_cpu_count']
                        valvm['db_homes'] = self.__get_database_db_homes(vm['db_homes'])
                        valvm['db_nodes'] = [] if not db_nodes else sorted(db_nodes, key=lambda i: i['desc'])

                        vault['vm_clusters'].append(valvm)

                # search for vm_clusters
                data.append(vault)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Autonomous Dedicated Infra
    ##########################################################################
    def __get_database_adb_dedicated(self, region_name, compartment, infra_id):

        data = []
        try:

            # Fetch the vmclusters
            vms = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_ADB_D_VMS, 'region_name', region_name, 'cloud_exadata_infrastructure_id', infra_id)
            for vm in vms:
                vmval = {
                    'id': vm['id'],
                    'display_name': vm['display_name'],
                    'availability_domain': vm['availability_domain'],
                    'description': vm['description'],
                    'subnet_id': vm['subnet_id'],
                    'subnet_name': vm['subnet_name'],
                    'subnet_name_full': vm['subnet_name_full'],
                    'vcn_name': vm['vcn_name'],
                    'nsg_ids': vm['nsg_ids'],
                    'nsg_names': vm['nsg_names'],
                    'last_update_history_entry_id': vm['last_update_history_entry_id'],
                    'lifecycle_state': vm['lifecycle_state'],
                    'time_created': vm['time_created'],
                    'time_updated': vm['time_updated'],
                    'cluster_time_zone': vm['cluster_time_zone'],
                    'lifecycle_details': vm['lifecycle_details'],
                    'shape': vm['shape'],
                    'node_count': vm['node_count'],
                    'data_storage_size_in_tbs': vm['data_storage_size_in_tbs'],
                    'data_storage_size_in_gbs': vm['data_storage_size_in_gbs'],
                    'cpu_core_count': vm['cpu_core_count'],
                    'ocpu_count': vm['ocpu_count'],
                    'cpu_core_count_per_node': vm['cpu_core_count_per_node'],
                    'memory_size_in_gbs': vm['memory_size_in_gbs'],
                    'license_model': vm['license_model'],
                    'cloud_exadata_infrastructure_id': vm['cloud_exadata_infrastructure_id'],
                    'hostname': vm['hostname'],
                    'domain': vm['domain'],
                    'is_dedicated': True,
                    'available_cpus': vm['available_cpus'],
                    'reclaimable_cpus': vm['reclaimable_cpus'],
                    'available_container_databases': vm['available_container_databases'],
                    'total_container_databases': vm['total_container_databases'],
                    'available_autonomous_data_storage_size_in_tbs': vm['available_autonomous_data_storage_size_in_tbs'],
                    'autonomous_data_storage_size_in_tbs': vm['autonomous_data_storage_size_in_tbs'],
                    'db_node_storage_size_in_gbs': vm['db_node_storage_size_in_gbs'],
                    'memory_per_oracle_compute_unit_in_gbs': vm['memory_per_oracle_compute_unit_in_gbs'],
                    'maintenance_window': vm['maintenance_window'],
                    'last_maintenance_run': vm['last_maintenance_run'],
                    'next_maintenance_run': vm['next_maintenance_run'],
                    'defined_tags': vm['defined_tags'],
                    'freeform_tags': vm['freeform_tags'],
                    'compartment_name': vm['compartment_name'],
                    'compartment_path': vm['compartment_path'],
                    'compartment_id': vm['compartment_id'],
                    'region_name': vm['region_name'],
                    'compute_model': vm['compute_model'],
                    'is_mtls_enabled_vm_cluster': vm['is_mtls_enabled_vm_cluster'],
                    'scan_listener_port_tls': vm['scan_listener_port_tls'],
                    'scan_listener_port_non_tls': vm['scan_listener_port_non_tls'],
                    'time_database_ssl_certificate_expires': vm['time_database_ssl_certificate_expires'],
                    'time_ords_certificate_expires': vm['time_ords_certificate_expires'],
                    'containers': []}

                # fetch the containers
                containers = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_ADB_D_CONTAINERS, 'cloud_autonomous_vm_cluster_id', vm['id'])
                for ct in containers:
                    ct['name'] = ct['display_name'] + " (" + ct['lifecycle_state'] + "), " + ct['db_version'] + ", Patch Model : " + ct['patch_model']
                    ct['databases'] = []

                    # Add Databases
                    databases = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_ADB_DATABASE, 'autonomous_container_database_id', ct['id'])
                    for arr in databases:
                        db = self.__get_database_adb_database_info(arr)
                        db['sum_info'] = "Autonomous Database Dedicated " + str(db['db_workload']) + " (" + db['compute_model'] + "s) - " + vm['license_model']
                        db['sum_info_stopped'] = "Stopped Autonomous Database Dedicated " + str(db['db_workload']) + " (Count) - " + vm['license_model']
                        db['sum_info_count'] = "Autonomous Database Dedicated " + str(db['db_workload']) + " (Count) - " + vm['license_model']
                        db['sum_info_storage'] = "Autonomous Database Dedicated (TB)"
                        ct['databases'].append(db)

                    # Add containers
                    vmval['containers'].append(ct)

                # add the clusters to the infra
                data.append(vmval)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_nosql
    ##########################################################################
    def __get_database_nosql(self, region_name, compartment):

        data = []
        try:
            list_tables = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_NOSQL, 'region_name', region_name, 'compartment_id', compartment['id'])
            if list_tables:
                data = list_tables
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_mysql
    ##########################################################################
    def __get_database_mysql(self, region_name, compartment):

        data = []
        try:
            mysql = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_MYSQL, 'region_name', region_name, 'compartment_id', compartment['id'])
            if mysql:
                for dbs in mysql:

                    # Add backup
                    backups = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_MYSQL_BACKUPS, 'region_name', region_name, 'db_system_id', dbs['id'])
                    if backups:
                        dbs['backups'] = backups

                    # Add subnet
                    if dbs['subnet_id'] != 'None':
                        dbs['subnet_name'] = self.__get_core_network_subnet_name(dbs['subnet_id'])
                    else:
                        dbs['subnet_name'] = ""
                    data.append(dbs)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_mysql_standalone_backups
    ##########################################################################
    def __get_database_mysql_standalone_backups(self, region_name, compartment):

        data = []
        try:
            backups = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_MYSQL_BACKUPS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if backups:
                for bck in backups:

                    # check if db_system_id exist, if exist skip
                    dbs = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_MYSQL, 'region_name', region_name, 'id', bck['db_system_id'])
                    if dbs:
                        continue

                    data.append(bck)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_postgresql
    ##########################################################################
    def __get_database_postgresql(self, region_name, compartment):

        data = []
        try:
            pg = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_POSTGRESQL, 'region_name', region_name, 'compartment_id', compartment['id'])
            if pg:
                for dbs in pg:

                    # Add backup
                    backups = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_POSTGRESQL_BACKUPS, 'region_name', region_name, 'db_system_id', dbs['id'])
                    if backups:
                        dbs['backups'] = backups

                    # Add subnet
                    if dbs['network_subnet_id']:
                        dbs['network_subnet_name'] = self.__get_core_network_subnet_name(dbs['network_subnet_id'])
                    else:
                        dbs['network_subnet_name'] = ""
                    data.append(dbs)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_postgresql_standalone_backups
    ##########################################################################
    def __get_database_postgresql_standalone_backups(self, region_name, compartment):

        data = []
        try:
            backups = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_POSTGRESQL_BACKUPS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if backups:
                for bck in backups:

                    # check if db_system_id exist, if exist skip
                    dbs = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_POSTGRESQL, 'region_name', region_name, 'id', bck['db_system_id'])
                    if dbs:
                        continue

                    data.append(bck)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_software_images
    ##########################################################################
    def __get_database_software_images(self, region_name, compartment):

        data = []
        try:
            database_software_images = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_SOFTWARE_IMAGES, 'region_name', region_name, 'compartment_id', compartment['id'])
            return database_software_images

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_goldengate
    ##########################################################################
    def __get_database_goldengate(self, region_name, compartment):

        return_data = {}
        data = []
        try:
            data = self.__get_database_goldengate_deployments(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['gg_deployments'] = data

            data = self.__get_database_goldengate_db_registration(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['gg_db_registration'] = data

            return return_data

        except Exception as e:
            self.__print_error(e)
            return return_data

    ##########################################################################
    # __get_database_gg_deployments
    ##########################################################################
    def __get_database_goldengate_deployments(self, region_name, compartment):

        data = []
        try:
            database_gg_deployments = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_GG_DEPLOYMENTS, 'region_name', region_name, 'compartment_id', compartment['id'])
            return database_gg_deployments

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_announcement_detailed
    ##########################################################################
    def __get_announcement_detailed(self, region_name, compartment):

        data = []
        try:
            data = self.service.search_multi_items(self.service.C_ANNOUNCEMENT, self.service.C_ANNOUNCEMENT_DETAILED, 'region_name', region_name, 'compartment_id', compartment['id'])
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # __get_database_gg_db_registration
    ##########################################################################
    def __get_database_goldengate_db_registration(self, region_name, compartment):

        data = []
        try:
            database_gg_db_registrations = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_GG_DB_REGISTRATION, 'region_name', region_name, 'compartment_id', compartment['id'])
            return database_gg_db_registrations

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Database
    ##########################################################################
    def __get_database_main(self, region_name, compartment):

        return_data = {}
        try:

            # DB System
            data = self.__get_database_db_systems(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['db_system'] = data

            # DB Backups
            data = self.__get_database_db_all_backups(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['db_all_backups'] = data

            data = self.__get_database_db_exadata(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['exadata_infrastructure'] = data

            data = self.__get_database_exascale_vaults(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['exascale'] = data

            data = self.__get_database_db_exacc(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['exacc_infrastructure'] = data

            data = self.__get_database_adb_databases(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['autonomous'] = data

            data = self.__get_database_nosql(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['nosql'] = data

            data = self.__get_database_mysql(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['mysql'] = data

            data = self.__get_database_mysql_standalone_backups(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['mysql_standalone_backups'] = data

            data = self.__get_database_postgresql(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['postgresql'] = data

            data = self.__get_database_postgresql_standalone_backups(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['postgresql_standalone_backups'] = data

            data = self.__get_database_software_images(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['software_images'] = data

            data = self.__get_database_goldengate(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['goldengate'] = data

            # external CDB
            data = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXTERNAL_CDB, 'region_name', region_name, 'compartment_id', compartment['id'])
            if data:
                if len(data) > 0:
                    return_data['db_external_cdb'] = data

            # external PDB
            data = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXTERNAL_PDB, 'region_name', region_name, 'compartment_id', compartment['id'])
            if data:
                if len(data) > 0:
                    return_data['db_external_pdb'] = data

            # external Non-PDB
            data = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_EXTERNAL_NONPDB, 'region_name', region_name, 'compartment_id', compartment['id'])
            if data:
                if len(data) > 0:
                    return_data['db_external_nonpdb'] = data

            # Data Safe
            data = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_DATASAFE, 'region_name', region_name, 'compartment_id', compartment['id'])
            if data and len(data) > 0:

                # add resource name
                for db in data:
                    for tg in db['targets']:
                        for asst in tg['associated_resource_ids']:
                            name = self.service.get_resource_name_by_id(asst)
                            if name:
                                tg['associated_resource_names'].append(name)

                return_data["datasafe"] = data

            return return_data

        except Exception as e:
            self.__print_error(e)
            return return_data

    ##########################################################################
    # print file systems mount targets
    ##########################################################################
    def __get_file_storage_mount_target(self, export_set_id):

        data = []
        try:
            mount_targets = self.service.search_multi_items(self.service.C_FILE_STORAGE, self.service.C_FILE_STORAGE_MOUNTS, 'export_set_id', export_set_id)
            for mt in mount_targets:
                val = {'id': mt['id'],
                       'mount': str(mt['display_name']) + ", Subnet: " + self.service.get_network_subnet(mt['subnet_id'], True),
                       'display_name': str(mt['display_name']),
                       'subnet_id': str(mt['subnet_id']),
                       'private_ip_ids': mt['private_ip_ids']}
                data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print file systems limits
    ##########################################################################
    def __get_file_storage_limits(self, export_set):
        try:
            file_details = ""
            bytes_details = ""
            max_fs_stat_bytes = export_set['max_fs_stat_bytes']
            max_fs_stat_files = export_set['max_fs_stat_files']

            # handle files:
            if int(max_fs_stat_files).bit_length() >= 63:
                file_details = "Files (64bit)"
            elif int(max_fs_stat_files).bit_length() == 31:
                file_details = "Files (32bit)"
            else:
                file_details = "Files (" + str(max_fs_stat_files) + ")"

            # handle bytes
            if int(max_fs_stat_bytes).bit_length() >= 63:
                bytes_details = "Size (Unlimited)"
            else:
                bytes_details = "Size (" + str(round(int(max_fs_stat_bytes) / 1024 / 1024 / 1024)) + "GB)"

            return bytes_details + ", " + file_details
        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # print file systems exports
    ##########################################################################
    def __get_file_storage_exports(self, file_system_id):

        try:
            data = []
            exports = self.service.search_multi_items(self.service.C_FILE_STORAGE, self.service.C_FILE_STORAGE_EXPORTS, 'file_system_id', file_system_id)

            for export in exports:
                dataval = {
                    'id': export['id'],
                    'file_system_id': export['file_system_id'],
                    'time_created': export['time_created'],
                    'path': export['path'],
                    'exportset': "",
                    'options': []}

                # export set
                if export['export_set']:
                    exp = export['export_set']
                    dataval['exportset'] = str(exp['display_name']) + ", " + str(exp['availability_domain']) + ", Limits: " + self.__get_file_storage_limits(exp)
                    dataval['display_name'] = str(exp['display_name'])
                    dataval['availability_domain'] = str(exp['availability_domain'])
                    for opt in exp['options']:
                        v = {}
                        for k in opt.keys():
                            v[k] = opt[k]
                        dataval['options'].append(v)
                # Mount Target
                dataval['mount_target'] = self.__get_file_storage_mount_target(export['export_set_id'])
                data.append(dataval)
            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # File System
    ##########################################################################
    #
    # class oci.file_storage.FileStorageClient(config, **kwargs)
    #
    ##########################################################################

    def __get_file_storage_main(self, region_name, compartment):
        data = []
        try:
            file_systems = self.service.search_multi_items(self.service.C_FILE_STORAGE, self.service.C_FILE_STORAGE_FILESYSTEMS, 'region_name', region_name, 'compartment_id', compartment['id'])

            # handle file systems
            for fs in file_systems:
                dataval = {'id': fs['id'],
                           'filesystem': fs['display_name'] + " - " + fs['availability_domain'] + " - " + fs['size_gb'] + "GB metered",
                           'time_created': fs['time_created'],
                           'display_name': fs['display_name'],
                           'availability_domain': fs['availability_domain'],
                           'size_gb': fs['size_gb'],
                           'sum_info': 'File Storage (GB)',
                           'sum_size_gb': fs['size_gb'],
                           'snapshots': [e['name'] + " - " + e['time_created'][0:16] for e in fs['snapshots']],
                           'defined_tags': fs['defined_tags'],
                           'freeform_tags': fs['freeform_tags'],
                           'compartment_name': fs['compartment_name'],
                           'compartment_path': fs['compartment_path'],
                           'compartment_id': fs['compartment_id'],
                           'kms_key_id': fs['kms_key_id'],
                           'kms_key_name': self.__get_vault_key_name(fs['kms_key_id']),
                           'region_name': region_name,
                           'exports': self.__get_file_storage_exports(fs['id'])}
                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Object Storage
    ##########################################################################
    #
    # class oci.object_storage.ObjectStorageClient(config, **kwargs)
    #
    ##########################################################################

    def __get_object_storage_main(self, region_name, compartment):
        data = []
        try:

            buckets = self.service.search_multi_items(self.service.C_OS, self.service.C_OS_BUCKETS, 'region_name', region_name, 'compartment_id', compartment['id'])

            # tbd buckets size
            for bucket in buckets:
                value = {'name': bucket['name'],
                         'objects': bucket['approximate_count'],
                         'time_created': bucket['time_created'],
                         'size': bucket['approximate_size'],
                         'sum_size_gb': bucket['size_gb'],
                         'sum_info': 'Object Storage - Buckets (GB)',
                         'count': bucket['count'],
                         'preauthenticated_requests': bucket['preauthenticated_requests'],
                         'object_lifecycle': bucket['object_lifecycle'],
                         'compartment_id': bucket['compartment_id'],
                         'compartment_name': bucket['compartment_name'],
                         'compartment_path': bucket['compartment_path'],
                         'region_name': bucket['region_name'],
                         'namespace_name': bucket['namespace_name'],
                         'public_access_type': bucket['public_access_type'],
                         'storage_tier': bucket['storage_tier'],
                         'object_events_enabled': bucket['object_events_enabled'],
                         'kms_key_id': bucket['kms_key_id'],
                         'kms_key_name': self.__get_vault_key_name(bucket['kms_key_id']),
                         'object_lifecycle_policy_etag': bucket['object_lifecycle_policy_etag'],
                         'replication_enabled': bucket['replication_enabled'],
                         'is_read_only': bucket['is_read_only'],
                         'versioning': bucket['versioning'],
                         'auto_tiering': bucket['auto_tiering'],
                         'id': bucket['id'],
                         'defined_tags': bucket['defined_tags'],
                         'freeform_tags': bucket['freeform_tags'],
                         'error_message': bucket['error_message'],
                         'archival_state': bucket['archival_state'],
                         'logs': self.service.get_logging_log(bucket['name'])
                         }

                replication_enabled = ", Replication" if value['replication_enabled'] == "True" else ""
                object_events_enabled = ", Events" if value['object_events_enabled'] == "True" else ""
                is_read_only = ", ReadOnly" if value['is_read_only'] == "True" else ""
                log_enabled = ", Log Enabled" if value['logs'] else ""
                versioning = ", Versioning" if value['versioning'] == "Enabled" else ""
                object_lifecycle = ", LifeCycle: " + value['object_lifecycle'] if value['object_lifecycle'] else ""
                auto_tiering = ", AutoTier" if value['auto_tiering'] != "Disabled" else ""

                value['desc'] = (
                    bucket['name'].ljust(30)[0:30] + " - " +
                    value['objects'] + " Objs , " +
                    value['size'] + "GB (Approx)" +
                    log_enabled + auto_tiering + versioning + replication_enabled + is_read_only + object_events_enabled +
                    object_lifecycle
                )

                data.append(value)
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print load balancer backed
    ##########################################################################
    def __get_load_balancer_bs_healthchecker(self, health_checker, line):

        try:
            h = health_checker
            if str(h['protocol']) == "TCP" or str(h['protocol']) == "UDP":
                if line == 1:
                    return (h['protocol'] + ", interval(ms)=" + str(h['interval_in_millis']) + ", " +
                            "Timeout(ms)=" + str(h['timeout_in_millis']) + ", " +
                            "retries=" + str(h['retries']))
                if line == 2:
                    return str(h['port']) + "/" + h['protocol']

            # if HTTP
            if str(h['protocol']) == "HTTP" or str(h['protocol']) == "HTTPS":
                if line == 1:
                    return (h['protocol'] + ", interval(ms)=" + str(h['interval_in_millis']) + ", " +
                            "Timeout(ms)=" + str(h['timeout_in_millis']) + ", " +
                            "retries=" + str(h['retries']))
                if line == 2:
                    return (str(h['port']) + "/" + h['protocol'] + ", " +
                            "Code=" + str(['return_code']) + ", " +
                            "RegEx=" + str(h['response_body_regex']) + ", " +
                            "url_path =" + str(h['url_path']))
        except Exception as e:
            self.__print_error(e)
            return ""

    ##########################################################################
    # get load balancer backedset
    ##########################################################################
    def __get_load_balancer_backendset(self, load_balancer_id):

        data = []
        try:

            backendsets = self.service.search_multi_items(self.service.C_LB, self.service.C_LB_BACKEND_SETS, 'load_balancer_id', load_balancer_id)

            for bs in backendsets:
                dataval = bs
                dataval['status'] = bs['status'].ljust(4)[0:4]
                dataval['status_full'] = bs['status']

                # Health Checker
                datahealth = bs['health_checker']
                datahealth['desc1'] = self.__get_load_balancer_bs_healthchecker(bs['health_checker'], 1)
                datahealth['desc2'] = self.__get_load_balancer_bs_healthchecker(bs['health_checker'], 2)
                dataval['health_check'] = datahealth

                data.append(dataval)

            # return the data
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print load balancer config
    ##########################################################################
    def __get_load_balancer_details(self, load_balance_obj):
        data = {}
        try:
            lb = load_balance_obj
            flexible = (str(lb['shape_min_mbps']) + "mbps:" + str(lb['shape_max_mbps']) + "mbps - ") if lb['shape_min_mbps'] else ""
            data = {
                'id': str(lb['id']),
                'name': str(lb['display_name']) + " - " + str(lb['shape_name']) + " - " + flexible + ("(Private)" if lb['is_private'] else "(Public)"),
                'status': lb['status'],
                'shape_name': lb['shape_name'],
                'shape_min_mbps': lb['shape_min_mbps'],
                'shape_max_mbps': lb['shape_max_mbps'],
                'display_name': lb['display_name'],
                'is_private': lb['is_private'],
                'ips': lb['ip_addresses'],
                'path_route': lb['path_route'],
                'nsg_ids': lb['nsg_ids'],
                # 'nsg_names': lb['nsg_names'],
                'nsg_names': self.service.get_network_nsg_names_from_ids(lb['nsg_ids']),
                'hostnames': [x['info'] for x in lb['hostnames']],
                'rule_sets': lb['rule_sets'],
                'compartment_name': lb['compartment_name'],
                'compartment_path': lb['compartment_path'],
                'compartment_id': lb['compartment_id'],
                'subnet_ids': lb['subnet_ids'],
                'time_created': lb['time_created'],
                'defined_tags': lb['defined_tags'],
                'freeform_tags': lb['freeform_tags'],
                'certificates': lb['certificates'],
                'ssl_cipher_suites': lb['ssl_cipher_suites'],
                'routing_policies': lb['routing_policies']
            }

            # subnets
            datasub = []
            for subnet in lb['subnet_ids']:
                subnet_name = self.service.get_network_subnet(subnet, True)
                if subnet_name:
                    if subnet_name != "":
                        datasub.append(subnet_name)
            data['subnets'] = datasub

            # listeners
            datalis = []
            for lo in lb['listeners']:
                value = {
                    'ssl_configuration': str(lo['ssl_configuration']),
                    'port': str(lo['port']) + "/" + str(lo['protocol']),
                    'default_backend_set_name': str(lo['default_backend_set_name']),
                    'path_route_set_name': lo['path_route_set_name'],
                    'rule_set_names': lo['rule_set_names'],
                    'id': lo['id'],
                    'desc': (lo['id'].ljust(20) + " - " + str(lo['port']) + "/" + str(lo['protocol']) + " - BS: " + str(lo['default_backend_set_name']) + ("" if lo['ssl_configuration'] == "" else " - Cert: " + str(lo['ssl_configuration'])))
                }

                # hostnames
                datahost = []
                for hostname in lo['hostname_names']:
                    for hostname_master in lb['hostnames']:
                        if hostname == hostname_master['name']:
                            datahost.append(hostname_master['desc'])
                value['hostname_names'] = datahost
                datalis.append(value)
            data['listeners'] = datalis

            return data
        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Load Balancer
    ##########################################################################
    def __get_load_balancer_main(self, region_name, compartment):

        data = []
        try:
            load_balancers = self.service.search_multi_items(self.service.C_LB, self.service.C_LB_LOAD_BALANCERS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for load_balance_obj in load_balancers:
                dataval = {
                    'sum_info': "Load Balancer " + str(load_balance_obj['shape_name']),
                    'details': self.__get_load_balancer_details(load_balance_obj),
                    'backendset': self.__get_load_balancer_backendset(load_balance_obj['id']),
                    'logs': self.service.get_logging_log(load_balance_obj['id'])
                }
                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # get load balancer backedset network
    ##########################################################################
    def __get_load_balancer_backendset_network(self, load_balancer_id):

        data = []
        try:

            backendsets = self.service.search_multi_items(self.service.C_LB, self.service.C_LB_NETWORK_BACKEND_SETS, 'load_balancer_id', load_balancer_id)

            for bs in backendsets:
                dataval = bs
                dataval['status'] = bs['status'].ljust(4)[0:4]
                dataval['status_full'] = bs['status']

                # Health Checker
                datahealth = bs['health_checker']
                datahealth['desc1'] = self.__get_load_balancer_bs_healthchecker(bs['health_checker'], 1)
                datahealth['desc2'] = self.__get_load_balancer_bs_healthchecker(bs['health_checker'], 2)
                dataval['health_check'] = datahealth

                data.append(dataval)

            # return the data
            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # print load balancer config
    ##########################################################################
    def __get_load_balancer_network_details(self, load_balance_obj):
        data = {}
        try:
            lb = load_balance_obj
            data['id'] = str(lb['id'])
            data['name'] = str(lb['display_name']) + " - " + str(lb['shape_name']) + " - " + ("(Private)" if lb['is_private'] else "(Public)")
            data['status'] = lb['status']
            data['display_name'] = lb['display_name']
            data['time_created'] = lb['time_created']
            data['time_updated'] = lb['time_updated']
            data['is_preserve_source_destination'] = lb['is_preserve_source_destination']
            data['nlb_ip_version'] = lb['nlb_ip_version']
            data['is_symmetric_hash_enabled'] = lb['is_symmetric_hash_enabled']
            data['is_private'] = lb['is_private']
            data['ips'] = lb['ip_addresses']
            data['nsg_ids'] = lb['nsg_ids']
            # data['nsg_names'] = lb['nsg_names']
            data['nsg_names'] = self.service.get_network_nsg_names_from_ids(lb['nsg_ids'])
            data['compartment_name'] = lb['compartment_name']
            data['compartment_path'] = lb['compartment_path']
            data['compartment_id'] = lb['compartment_id']
            data['subnet_id'] = lb['subnet_id']
            data['subnet_name'] = lb['subnet_name']
            data['defined_tags'] = lb['defined_tags']
            data['freeform_tags'] = lb['freeform_tags']

            # listeners
            datalis = []
            for lo in lb['listeners']:
                value = {
                    'port': str(lo['port']) + "/" + str(lo['protocol']),
                    'id': str(lo['id']),
                    'default_backend_set_name': str(lo['default_backend_set_name']),
                    'desc': (lo['id'].ljust(20) + " - " + str(lo['port']) + "/" + str(lo['protocol']) + " - BS: " + str(lo['default_backend_set_name'])),
                    'csvname': (lo['id'] + " - " + str(lo['port']) + "/" + str(lo['protocol']) + " - BS: " + str(lo['default_backend_set_name']))
                }
                datalis.append(value)
            data['listeners'] = datalis

            return data
        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Network Load Balancer
    ##########################################################################
    def __get_load_balancer_network_main(self, region_name, compartment):

        data = []
        try:
            load_balancers = self.service.search_multi_items(self.service.C_LB, self.service.C_LB_NETWORK_LOAD_BALANCERS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for load_balance_obj in load_balancers:
                dataval = {'sum_info': "Network Load Balancer",
                           'details': self.__get_load_balancer_network_details(load_balance_obj),
                           'backendset': self.__get_load_balancer_backendset_network(load_balance_obj['id'])}
                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # resource Management
    ##########################################################################
    def __get_resource_management_main(self, region_name, compartment):
        data = []
        try:
            stacks = self.service.search_multi_items(self.service.C_ORM, self.service.C_ORM_STACKS, 'region_name', region_name, 'compartment_id', compartment['id'])

            # query the stacks
            for stack in stacks:
                dataval = {'id': str(stack['id']),
                           'stack_name': str(stack['display_name']) + " - " + str(stack['description']),
                           'display_name': stack['display_name'],
                           'description': stack['description'],
                           'jobs': stack['jobs'],
                           'compartment_id': stack['compartment_id'],
                           'compartment_name': stack['compartment_name'],
                           'compartment_path': stack['compartment_path'],
                           'region_name': stack['region_name'],
                           'time_created': stack['time_created'],
                           'defined_tags': stack['defined_tags'],
                           'freeform_tags': stack['freeform_tags']}

                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error(e)
            return data

    ##########################################################################
    # Email
    ##########################################################################
    def __get_email_main(self, region_name, compartment):
        try:
            senders = self.service.search_multi_items(self.service.C_EMAIL, self.service.C_EMAIL_SENDERS, 'region_name', region_name, 'compartment_id', compartment['id'])
            suppressions = self.service.search_multi_items(self.service.C_EMAIL, self.service.C_EMAIL_SUPPRESSIONS, 'region_name', region_name, 'compartment_id', compartment['id'])

            if not senders and not suppressions:
                return

            data = {}

            # Senders
            if senders:
                data_sender = []
                for sender in senders:
                    data_sender.append(str(sender['email_address']) + " - " + str(sender['lifecycle_state']))
                data['senders'] = data_sender

            # Suppression
            if len(suppressions) > 0:
                data_supp = []
                for suppression in suppressions:
                    data_supp.append(str(suppression['email_address']) + " - " + str(suppression['reason']))
                data['supp_list'] = data_supp

            # add compartment details
            data['compartment_name'] = compartment['name']
            data['compartment_path'] = compartment['path']
            data['compartment_id'] = compartment['id']
            data['region_name'] = region_name

            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # Containers
    ##########################################################################
    def __get_container_main(self, region_name, compartment):
        try:
            containers = self.service.search_multi_items(self.service.C_CONTAINER, self.service.C_CONTAINER_CLUSTERS, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = []
            if containers:
                for container in containers:
                    val = {'id': container['id'],
                           'name': container['name'],
                           'sum_info': "OKE Clusters",
                           'sum_size_gb': str("1"),
                           'lifecycle_state': container['lifecycle_state'],
                           'kubernetes_version': container['kubernetes_version'],
                           'compartment_name': container['compartment_name'],
                           'compartment_path': container['compartment_path'],
                           'compartment_id': container['compartment_id'],
                           'region_name': container['region_name'],
                           'endpoint_is_public_ip_enabled': container['endpoint_is_public_ip_enabled'],
                           'endpoint_nsg_ids': container['endpoint_nsg_ids'],
                           'endpoint_nsg_names': container['endpoint_nsg_names'],
                           'endpoint_subnet_id': container['endpoint_subnet_id'],
                           'endpoint_subnet_name': container['endpoint_subnet_name'],
                           'option_lb_ids': container['option_lb_ids'],
                           'option_network_pods_cidr': container['option_network_pods_cidr'],
                           'option_network_services_cidr': container['option_network_services_cidr'],
                           'option_is_kubernetes_dashboard_enabled': container['option_is_kubernetes_dashboard_enabled'],
                           'option_is_tiller_enabled': container['option_is_tiller_enabled'],
                           'option_is_pod_security_policy_enabled': container['option_is_pod_security_policy_enabled'],
                           'time_created': container['time_created'],
                           'time_deleted': container['time_deleted'],
                           'time_updated': container['time_updated'],
                           'created_by_user_id': container['created_by_user_id'],
                           'deleted_by_user_id': container['deleted_by_user_id'],
                           'updated_by_user_id': container['updated_by_user_id'],
                           'endpoint_kubernetes': container['endpoint_kubernetes'],
                           'endpoint_public_endpoint': container['endpoint_public_endpoint'],
                           'endpoint_private_endpoint': container['endpoint_private_endpoint'],
                           'endpoint_vcn_hostname_endpoint': container['endpoint_vcn_hostname_endpoint'],
                           'available_kubernetes_upgrades': container['available_kubernetes_upgrades'],
                           'defined_tags': container['defined_tags'],
                           'freeform_tags': container['freeform_tags'],
                           'vcn_id': container['vcn_id'],
                           'node_pools': [],
                           'vcn_name': self.__get_core_network_vcn_name(container['vcn_id'])}

                    # add the node pools
                    nodes = self.service.search_multi_items(self.service.C_CONTAINER, self.service.C_CONTAINER_NODE_POOLS, 'cluster_id', container['id'])
                    for np in nodes:
                        nval = {
                            'id': np['id'],
                            'name': np['name'],
                            'node_image_id': np['node_image_id'],
                            'node_image_name': np['node_image_name'],
                            'kubernetes_version': np['kubernetes_version'],
                            'node_shape': np['node_shape'],
                            'quantity_per_subnet': np['quantity_per_subnet'],
                            'node_shape_mem_gb': np['node_shape_mem_gb'],
                            'node_shape_ocpus': np['node_shape_ocpus'],
                            'node_source_type': np['node_source_type'],
                            'node_source_name': np['node_source_name'],
                            'defined_tags': np['defined_tags'],
                            'freeform_tags': np['freeform_tags'],
                            'compartment_name': np['compartment_name'],
                            'compartment_path': np['compartment_path'],
                            'compartment_id': np['compartment_id'],
                            'subnet_ids': np['subnet_ids'],
                            'subnets': self.__get_core_network_subnet_names(np['subnet_ids'])
                        }

                        val['node_pools'].append(nval)

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # Streams
    ##########################################################################
    def __get_streams_queues_main(self, region_name, compartment):
        try:
            data = {}
            streams = self.service.search_multi_items(self.service.C_STREAMS, self.service.C_STREAMS_STREAMS, 'region_name', region_name, 'compartment_id', compartment['id'])
            queues = self.service.search_multi_items(self.service.C_STREAMS, self.service.C_STREAMS_QUEUES, 'region_name', region_name, 'compartment_id', compartment['id'])

            # if streams add it
            if streams:
                data['streams'] = streams

            # if queues add it
            if queues:
                data['queues'] = queues

            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # functions
    ##########################################################################
    def __get_functions_main(self, region_name, compartment):
        try:
            functions_apps = self.service.search_multi_items(self.service.C_FUNCTION, self.service.C_FUNCTION_APPLICATIONS, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = []
            if functions_apps:
                for fn in functions_apps:
                    val = {
                        'id': fn['id'],
                        'display_name': fn['display_name'],
                        'lifecycle_state': fn['lifecycle_state'],
                        'subnet_ids': fn['subnet_ids'],
                        'subnets': self.__get_core_network_subnet_names(fn['subnet_ids']),
                        'network_security_group_ids': fn['network_security_group_ids'],
                        'network_security_group_names': fn['network_security_group_names'],
                        'shape': fn['shape'],
                        'trace_config_is_enabled': fn['trace_config_is_enabled'],
                        'trace_config_domain_id': fn['trace_config_domain_id'],
                        'image_policy_is_enabled': fn['image_policy_is_enabled'],
                        'time_created': fn['time_created'],
                        'time_updated': fn['time_updated'],
                        'defined_tags': fn['defined_tags'],
                        'freeform_tags': fn['freeform_tags'],
                        'functions': fn['functions'],
                        'compartment_name': fn['compartment_name'],
                        'compartment_path': fn['compartment_path'],
                        'compartment_id': fn['compartment_id'],
                        'region_name': fn['region_name']
                    }

                    # subnets
                    for sub in fn['subnet_ids']:
                        val['subnets'].append(self.__get_core_network_subnet_name(sub))

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # __get_apigateway_main
    ##########################################################################
    def __get_apigateway_main(self, region_name, compartment):
        try:
            apigs = self.service.search_multi_items(self.service.C_API, self.service.C_API_GATEWAYS, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = []
            if apigs:
                for ap in apigs:
                    val = ap

                    # deployments
                    apidep = self.service.search_multi_items(self.service.C_API, self.service.C_API_DEPLOYMENT, 'region_name', region_name, 'gateway_id', val['id'])
                    if apidep:
                        for apid in apidep:
                            vald = apid
                            vald['logs'] = self.service.get_logging_log(vald['id'])

                            # add deployment to apigw
                            val['deployments'].append(vald)

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # __get_fsdr_main
    ##########################################################################
    def __get_fsdr_main(self, region_name, compartment):
        try:
            fsdr = self.service.search_multi_items(self.service.C_FSDR, self.service.C_FSDR_PROTECTION_GROUPS, 'region_name', region_name, 'compartment_id', compartment['id'])
            return fsdr

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # monitoring
    ##########################################################################
    def __get_monitoring_main(self, region_name, compartment):
        try:
            alarms = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_ALARMS, 'region_name', region_name, 'compartment_id', compartment['id'])
            events = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_EVENTS, 'region_name', region_name, 'compartment_id', compartment['id'])
            agents = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_AGENTS, 'region_name', region_name, 'compartment_id', compartment['id'])
            advisor_recommendations = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_ADVISOR_RECOMMENDATIONS, 'region_name', region_name, 'compartment_id', compartment['id'])
            advisor_resource_actions = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_ADVISOR_RESOURCE_ACTIONS, 'region_name', region_name, 'compartment_id', compartment['id'])
            db_managements = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_DB_MANAGEMENT, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = {}
            # if events add it
            if events:
                data['events'] = []
                for event in events:
                    for action in event['actions']:
                        if action['action_type'] == 'ONS':
                            action['dest_name'] = self.__get_notification_topic_name(action['dest_id'])
                        if action['action_type'] == 'OSS':
                            action['dest_name'] = self.__get_streaming_stream_name(action['dest_id'])
                        if action['action_type'] == 'FAAS':
                            action['dest_name'] = self.__get_function_name(action['dest_id'])
                    data['events'].append(event)

            # if agents add it
            if agents:
                data['agents'] = agents

            # if advisors add it
            if advisor_recommendations:
                data['advisor_recommendations'] = advisor_recommendations

            if advisor_resource_actions:
                data['advisor_resource_actions'] = advisor_resource_actions

            # if db_managements add it
            if db_managements:
                data['db_managements'] = db_managements

            # if events add it
            if alarms:
                data['alarms'] = []
                for alarm in alarms:
                    val = alarm
                    val['destinations_names'] = []

                    # find the topics
                    for dest in alarm['destinations']:
                        if dest:
                            val['destinations_names'].append(self.__get_notification_topic_name(dest))

                    data['alarms'].append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # get topic name
    ##########################################################################
    def __get_notification_topic_name(self, topic_id):
        try:
            topic = self.service.search_unique_item(self.service.C_NOTIFICATIONS, self.service.C_NOTIFICATIONS_TOPICS, 'topic_id', topic_id)
            if topic:
                if topic['description'] != 'None':
                    return topic['name'] + " - " + topic['description']
                else:
                    return topic['name']
            return topic_id
        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # get stream name
    ##########################################################################
    def __get_streaming_stream_name(self, stream_id):
        try:
            stream = self.service.search_unique_item(self.service.C_STREAMS, self.service.C_STREAMS_STREAMS, 'id', stream_id)
            if stream:
                return stream['name']
            return stream_id
        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # get function name
    ##########################################################################
    def __get_function_name(self, function_id):
        try:
            function = self.service.search_unique_item(self.service.C_FUNCTION, self.service.C_FUNCTION_FUNCTIONS, 'id', function_id)
            if function:
                return function['display_name']
            return function_id
        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # notifications
    ##########################################################################
    def __get_notifications_main(self, region_name, compartment):
        try:
            topics = self.service.search_multi_items(self.service.C_NOTIFICATIONS, self.service.C_NOTIFICATIONS_TOPICS, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = []
            if topics:
                for topic in topics:
                    val = {'topic_id': topic['topic_id'],
                           'name': topic['name'],
                           'description': topic['description'],
                           'time_created': topic['time_created'],
                           'etag': topic['etag'],
                           'api_endpoint': topic['api_endpoint'],
                           'defined_tags': topic['defined_tags'],
                           'freeform_tags': topic['freeform_tags'],
                           'compartment_name': topic['compartment_name'],
                           'compartment_path': topic['compartment_path'],
                           'compartment_id': topic['compartment_id'],
                           'region_name': topic['region_name'],
                           'subscriptions': self.service.search_multi_items(self.service.C_NOTIFICATIONS, self.service.C_NOTIFICATIONS_SUBSCRIPTIONS, 'topic_id', topic['topic_id'])
                           }

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # edge
    ##########################################################################
    def __get_load_edge_main(self, region_name, compartment):

        try:
            healthcheck_http = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_HEALTHCHECK_HTTP, 'region_name', region_name, 'compartment_id', compartment['id'])
            healthcheck_ping = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_HEALTHCHECK_PING, 'region_name', region_name, 'compartment_id', compartment['id'])
            dns_zone = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_DNS_ZONE, 'region_name', region_name, 'compartment_id', compartment['id'])
            dns_steering = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_DNS_STEERING, 'region_name', region_name, 'compartment_id', compartment['id'])
            waas_policies = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_WAAS_POLICIES, 'region_name', region_name, 'compartment_id', compartment['id'])
            waf = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_WAF, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = {}
            if len(healthcheck_http) > 0 or len(healthcheck_ping) > 0:
                data['healthcheck'] = {'http': healthcheck_http, 'ping': healthcheck_ping}

            if dns_zone:
                data['dns_zone'] = dns_zone

            if dns_steering:
                data['dns_steering'] = dns_steering

            if waas_policies:
                data['waas_policies'] = waas_policies

            if waf:
                data['waf'] = waf

            return data

        except Exception as e:
            self.__print_error(e)
            return []

    ##########################################################################
    # Limits
    ##########################################################################
    def __get_limits_main(self, region_name):
        try:
            limits = self.service.search_multi_items(self.service.C_LIMITS, self.service.C_LIMITS_SERVICES, 'region_name', region_name)

            if limits:
                return limits

            return

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # Quotas
    ##########################################################################
    def __get_quotas_main(self, region_name, compartment):
        try:
            quotas = self.service.search_multi_items(self.service.C_LIMITS, self.service.C_LIMITS_QUOTAS, 'region_name', region_name, 'compartment_id', compartment['id'])

            if quotas:
                return quotas
            return

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # PaaS Native
    ##########################################################################
    def __get_paas_native_main(self, region_name, compartment):
        try:
            paas_services = {}

            # oic
            oic = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_OIC, 'region_name', region_name, 'compartment_id', compartment['id'])
            if oic:
                paas_services['oic'] = oic

            # oac
            oac = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_OAC, 'region_name', region_name, 'compartment_id', compartment['id'])
            if oac:
                paas_services['oac'] = oac

            # oce
            oce = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_OCE, 'region_name', region_name, 'compartment_id', compartment['id'])
            if oce:
                paas_services['oce'] = oce

            # oce
            vb = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_VB, 'region_name', region_name, 'compartment_id', compartment['id'])
            if vb:
                paas_services['vb'] = vb

            # ocvs
            ocvs = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_OCVS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if ocvs:
                paas_services['ocvs'] = ocvs

            # devops
            devops = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_DEVOPS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if devops:
                paas_services['devops'] = devops

            # opensearch
            open_search = self.service.search_multi_items(self.service.C_PAAS_NATIVE, self.service.C_PAAS_NATIVE_OPEN_SEARCH, 'region_name', region_name, 'compartment_id', compartment['id'])
            if open_search:
                paas_services['open_search'] = open_search

            return paas_services

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # get key name
    ##########################################################################
    def __get_vault_key_name(self, key_id):

        data = ""
        try:
            if key_id:
                key = self.service.search_unique_item(self.service.C_SECURITY, self.service.C_SECURITY_KEYS, 'id', key_id)
                if key:
                    data = key['name']
            return data

        except Exception as e:
            self.__print_error(e)

    ##########################################################################
    # Security and Logging
    ##########################################################################

    def __get_security_main(self, region_name, compartment):
        try:
            security_services = {}

            # cloud guard Main
            cg = self.service.search_multi_items(self.service.C_SECURITY, self.service.C_SECURITY_CLOUD_GUARD, 'region_name', region_name, 'compartment_id', compartment['id'])
            if cg:
                security_services['cloud_guard'] = cg

            # bastions
            bs = self.service.search_multi_items(self.service.C_SECURITY, self.service.C_SECURITY_BASTION, 'region_name', region_name, 'compartment_id', compartment['id'])
            if bs:
                security_services['bastions'] = bs

            # logging
            log = self.service.search_multi_items(self.service.C_SECURITY, self.service.C_SECURITY_LOGGING, 'region_name', region_name, 'compartment_id', compartment['id'])
            if log:
                security_services['logging'] = log

            # logging unified agents
            logua = self.service.search_multi_items(self.service.C_SECURITY, self.service.C_SECURITY_LOGGING_UA, 'region_name', region_name, 'compartment_id', compartment['id'])
            if log:
                security_services['logging_unified_agents'] = logua

            # kms_vaults
            vaults = self.service.search_multi_items(self.service.C_SECURITY, self.service.C_SECURITY_VAULTS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if vaults:
                security_services['kms_vaults'] = vaults

            # kms_keys
            keys = self.service.search_multi_items(self.service.C_SECURITY, self.service.C_SECURITY_KEYS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if keys:
                security_services['kms_keys'] = keys

            # certificate
            certificates = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_CERTIFICATES, 'region_name', region_name, 'compartment_id', compartment['id'])
            if certificates:
                for crt in certificates:
                    assoc = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_ASSOCIATIONS, 'region_name', region_name, 'certificates_resource_id', crt['id'])
                    if assoc:
                        crt['associated_resource_ids'] = ','.join(x['associated_resource_id'] for x in assoc)
                        crt['associated_resource_names'] = ','.join(self.service.get_resource_name_by_id(x['associated_resource_id']) for x in assoc)
                security_services['certificates'] = certificates

            # certificate associations
            certificate_associations = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_ASSOCIATIONS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if certificate_associations:
                security_services['certificate_associations'] = certificate_associations

            # certificate ca bundle
            certificate_ca_bundles = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_CA_BUNDLES, 'region_name', region_name, 'compartment_id', compartment['id'])
            if certificate_ca_bundles:
                for crt in certificate_ca_bundles:
                    assoc = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_ASSOCIATIONS, 'region_name', region_name, 'certificates_resource_id', crt['id'])
                    if assoc:
                        crt['associated_resource_ids'] = ','.join(x['associated_resource_id'] for x in assoc)
                        crt['associated_resource_names'] = ','.join(self.service.get_resource_name_by_id(x['associated_resource_id']) for x in assoc)
                security_services['certificate_ca_bundles'] = certificate_ca_bundles

            # certificate authorities
            certificate_authorities = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_AUTHORITIES, 'region_name', region_name, 'compartment_id', compartment['id'])
            if certificate_authorities:
                for crt in certificate_authorities:
                    assoc = self.service.search_multi_items(self.service.C_CERTIFICATE, self.service.C_CERTIFICATE_ASSOCIATIONS, 'region_name', region_name, 'certificates_resource_id', crt['id'])
                    if assoc:
                        crt['associated_resource_ids'] = ','.join(x['associated_resource_id'] for x in assoc)
                        crt['associated_resource_names'] = ','.join(self.service.get_resource_name_by_id(x['associated_resource_id']) for x in assoc)
                security_services['certificate_authorities'] = certificate_authorities

            return security_services

        except Exception as e:
            self.__print_error(e)
            pass

    ##########################################################################
    # Data AI
    ##########################################################################
    def __get_data_ai_main(self, region_name, compartment):
        try:
            data_ai = {}

            # oda
            oda = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_ODA, 'region_name', region_name, 'compartment_id', compartment['id'])
            if oda:
                data_ai['oda'] = oda

            # bds
            bds = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_BDS, 'region_name', region_name, 'compartment_id', compartment['id'])
            if bds:
                data_ai['bds'] = bds

            # data science
            ds = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_SCIENCE, 'region_name', region_name, 'compartment_id', compartment['id'])
            if ds:
                data_ai['data_science'] = ds

            # Data Flow
            df = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_FLOW, 'region_name', region_name, 'compartment_id', compartment['id'])
            if df:
                data_ai['data_flow'] = df

            # Data Catalog
            dc = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_CATALOG, 'region_name', region_name, 'compartment_id', compartment['id'])
            if dc:
                data_ai['data_catalog'] = dc

            # Data Integration
            di = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_DI, 'region_name', region_name, 'compartment_id', compartment['id'])
            if di:
                data_ai['data_integration'] = di

            # Gen AI
            genai = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_GENAI, 'region_name', region_name, 'compartment_id', compartment['id'])
            if genai:
                data_ai['genai'] = genai

            # Gen AI Agent
            genai_agent = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_GENAI_AGENT, 'region_name', region_name, 'compartment_id', compartment['id'])
            if genai_agent:
                data_ai['genai_agent'] = genai_agent

            # Gen AI Agent KB
            genai_agent_kb = self.service.search_multi_items(self.service.C_DATA_AI, self.service.C_DATA_AI_GENAI_AGENT_KB, 'region_name', region_name, 'compartment_id', compartment['id'])
            if genai_agent_kb:
                data_ai['genai_agent_kb'] = genai_agent_kb

            return data_ai

        except Exception as e:
            self.__print_error(e)
            pass
