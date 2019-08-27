##########################################################################
# Copyright(c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# showoci_data.py
#
# @author: Adi Zohar
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


class ShowOCIData(object):

    ############################################
    # ShowOCIService - Service object to query
    # OCI resources and run searches
    ###########################################
    service = None
    error = 0

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

    ############################################
    # get service data
    ############################################
    def get_service_data(self):

        return self.service.data

    ############################################
    # call service to load data
    ############################################
    def load_service_data(self):

        return self.service.load_service_data()

    ##########################################################################
    # get_oci_main_data
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

            # run on compartments
            if self.service.flags.is_loop_on_compartments:

                # pointer to Tenancy in cache
                tenancy = self.service.get_tenancy()

                # run on each subscribed region
                for region_name in tenancy['list_region_subscriptions']:

                    # if filtered by region skip if not cmd.region
                    if self.service.flags.filter_by_region and self.service.flags.filter_by_region not in region_name:
                        continue

                    limits_data = []
                    # limits services which regional but not compartment
                    if self.service.flags.read_limits:
                        limits_data = self.__get_limits_main(region_name)

                    # execute the region
                    value = self.__get_oci_region_data(region_name)

                    # if data returns, add to the json
                    if value or limits_data:
                        region_data = ({'type': "region", 'region': region_name, 'data': value, 'limits': limits_data})
                        self.data.append(region_data)

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
            'config_file': self.service.flags.config_file,
            'config_profile': self.service.flags.config_section,
            'use_instance_principals': self.service.flags.use_instance_principals,
            'version': self.service.flags.showoci_version,
            'datetime': start_time,
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
    # get service error flag
    ##########################################################################
    def get_service_warnings(self):

        return self.service.warning

    ##########################################################################
    # get service reboot migration
    ##########################################################################
    def get_service_reboot_migration(self):

        return self.service.reboot_migration_counter

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
    # run on Region
    ##########################################################################
    def __get_oci_region_data(self, region_name):

        ret_var = []
        print("\nProcessing Region " + region_name)

        try:

            # Loop on Compartments and call services
            compartments = self.service.get_compartment()

            # Loop on all relevant compartments
            print("\nProcessing...")
            for compartment in compartments:

                #  check if to skip ManagedCompartmentForPaaS
                if compartment['name'] == "ManagedCompartmentForPaaS" and not self.service.flags.read_ManagedCompartmentForPaaS:
                    continue

                print("    Compartment " + compartment['path'] + "...")
                data = {'compartment': compartment['name'], 'path': compartment['path']}
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

                # run on Resource Management
                if self.service.flags.read_resource_management:
                    value = self.__get_resource_management_main(region_name, compartment)
                    if value:
                        if len(value) > 0:
                            data['resource_management'] = value
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

                # streams
                if self.service.flags.read_streams:
                    value = self.__get_streams_main(region_name, compartment)
                    if value is not None:
                        if len(value) > 0:
                            data['streams'] = value
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

                # add the data to main Variable
                if has_data:
                    ret_var.append(data)

            print("")

            # return var
            return ret_var

        except Exception as e:
            self.__print_error("get_oci_region_data", e)

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
                         'compartment': arr['compartment_name'],
                         'time_created': arr['time_created'],
                         'defined_tags': arr['defined_tags'],
                         'freeform_tags': arr['freeform_tags']}

                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_nat", e)
            return data

    ##########################################################################
    # get Network VCN igw
    ##########################################################################

    def __get_core_network_vcn_igw(self, vcn_id):
        data = []
        try:
            list_igws = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_IGW, 'vcn_id', vcn_id)
            for arr in list_igws:
                value = {'id': arr['id'], 'name': arr['name'], 'compartment': arr['compartment_name'], 'time_created': arr['time_created']}
                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_igw", e)
            return data

    ##########################################################################
    # get Network VCN SGW
    ##########################################################################

    def __get_core_network_vcn_sgw(self, vcn_id):
        data = []
        try:

            list_service_gateways = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_SGW, 'vcn_id', vcn_id)
            for arr in list_service_gateways:
                value = {'id': arr['id'], 'name': arr['name'], 'services': arr['services'],
                         'compartment': arr['compartment_name'], 'time_created': arr['time_created'], 'defined_tags': arr['defined_tags'], 'freeform_tags': arr['freeform_tags']}
                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_sgw", e)
            return data

    ##########################################################################
    # get dRG details
    ##########################################################################

    def __get_core_network_vcn_drg_details(self, drg_attachment):
        retStr = ""
        try:
            drg_id = drg_attachment['drg_id']

            # get DRG name
            drg = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DRG, 'id', drg_id)
            if drg:
                retStr = drg['name']

            # check if IPSEC
            list_ip_sec_connections = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_IPS, 'drg_id', drg_id)
            if len(list_ip_sec_connections) > 0:
                retStr += " + IPSEC (" + str(len(list_ip_sec_connections)) + ")"

            # Check Remote Peering
            rpcs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_RPC, 'drg_id', drg_id)
            if len(rpcs) > 0:
                retStr += " + Remote Peering (" + str(len(rpcs)) + ")"

            # check transit routing
            if drg_attachment['route_table_id'] != "None":
                retStr += " + Transit Route(" + str(self.__get_core_network_route(drg_attachment['route_table_id']) + ")")

            return retStr

        except Exception as e:
            self.__print_error("__get_core_network_vcn_drg_details", e)
            return retStr

    ##########################################################################
    # get Network VCN DRG Attached
    ##########################################################################

    def __get_core_network_vcn_drg_attached(self, vcn_id):
        data = []
        try:

            list_drg_attachments = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DRG_AT, 'vcn_id', vcn_id)
            for da in list_drg_attachments:
                val = self.__get_core_network_vcn_drg_details(da)
                value = {'id': da['id'], 'drg_id': da['drg_id'], 'name': val, 'compartment': da['compartment_name'], 'time_created': da['time_created']}
                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_drg_attached", e)
            return data

    ##########################################################################
    # Print Network VCN Local Peering
    ##########################################################################
    def __get_core_network_vcn_local_peering(self, vcn_id):
        data = []
        try:
            local_peering_gateways = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_LPG, 'vcn_id', vcn_id)
            for lpg in local_peering_gateways:
                routestr = ""
                if lpg['route_table_id'] != "None":
                    routestr = " + Transit Route(" + str(self.__get_core_network_route(lpg['route_table_id'])) + ")"

                value = {'id': lpg['id'], 'name': (lpg['name'] + routestr), 'compartment': lpg['compartment_name'], 'time_created': lpg['time_created']}
                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_local_peering", e)
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
                    'compartment': subnet['compartment_name'],
                    'dhcp_options': dhcp_options,
                    'security_list': sec_lists,
                    'route': route_name,
                    'time_created': subnet['time_created'],
                    'defined_tags': subnet['defined_tags'],
                    'freeform_tags': subnet['freeform_tags']
                })
                data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_subnets", e)
            return data
            pass

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
                    'compartment': sl['compartment_name'],
                    'sec_rules': sl['sec_rules'],
                    'time_created': sl['time_created'],
                    'defined_tags': sl['defined_tags'],
                    'freeform_tags': sl['freeform_tags']
                })

            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_security_lists", e)
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
                    'compartment': nsg['compartment_name'],
                    'sec_rules': [],
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
            self.__print_error("__get_core_network_vcn_security_lists", e)
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
            self.__print_error("__get_core_network_vcn_route_rule", e)
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
                    route_rules.append({'network_entity_id': rl['network_entity_id'], 'destination': rl['destination'], 'desc': self.__get_core_network_vcn_route_rule(rl)})

                # add route
                val = {'id': rt['id'], 'name': rt['name'], 'compartment': rt['compartment_name'], 'time_created': rt['time_created'],
                       'route_rules': route_rules}
                data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_route_tables", e)
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
                    'compartment': dhcp['compartment_name'],
                    'time_created': dhcp['time_created'],
                    'opt': dhcp['options']
                })
            return data

        except Exception as e:
            self.__print_error("__get_core_network_vcn_dhcp_options", e)
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
                       'security_lists': self.__get_core_network_vcn_security_lists(vcn['id']),
                       'security_groups': self.__get_core_network_vcn_security_groups(vcn['id']),
                       'route_tables': self.__get_core_network_vcn_route_tables(vcn['id']),
                       'dhcp_options': self.__get_core_network_vcn_dhcp_options(vcn['id'])}

                # assign the data to the vcn
                vcn_data.append({'id': vcn['id'], 'name': vcn['name'], 'display_name': vcn['display_name'], 'cidr_block': vcn['cidr_block'], 'compartment': str(compartment['name']), 'data': val})
            return vcn_data

        except BaseException as e:
            self.__print_error("__get_core_network_vcn", e)
            return vcn_data

    ##########################################################################
    # print network cpe
    ##########################################################################
    def __get_core_network_cpe(self, region_name, compartment):
        data = []
        try:
            cpes = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_CPE, 'region_name', region_name, 'compartment_id', compartment['id'])
            data = [cpe['name'] for cpe in cpes]
            return data

        except Exception as e:
            self.__print_error("__get_core_network_cpe", e)
            return data

    ##########################################################################
    # print network drg
    ##########################################################################
    def __get_core_network_drg(self, region_name, compartment):

        data = []
        try:
            drgs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_DRG, 'region_name', region_name, 'compartment_id', compartment['id'])
            data = [drg['name'] for drg in drgs]
            return data

        except Exception as e:
            self.__print_error("__get_core_network_drg", e)
            return data

    ##########################################################################
    # get dRG details
    ##########################################################################

    def __get_core_network_drg_name(self, drg_id):
        try:
            # get DRG name
            drg = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_DRG, 'id', drg_id)
            if drg:
                return "DRG - " + drg['name']
            return ""

        except Exception as e:
            self.__print_error("__get_core_network_drg_name", e)

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
            self.__print_error("__get_core_network_cpe_name", e)

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
            self.__print_error("__get_core_network_vcn_name", e)

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
            self.__print_error("__get_core_network_rpc_name", e)

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
            self.__print_error("__get_core_network_subnet_name", e)

    ##########################################################################
    # print network remote peering
    ##########################################################################
    def __get_core_network_remote_peering(self, region_name, compartment):

        data = []
        try:
            rpcs = self.service.search_multi_items(self.service.C_NETWORK, self.service.C_NETWORK_RPC, 'region_name', region_name, 'compartment_id', compartment['id'])
            for rpc in rpcs:
                drg_name = self.__get_core_network_drg_name(rpc['drg_id'])
                data.append({
                    'id': str(rpc['id']),
                    'peer_id': str(rpc['peer_id']),
                    'name': str(rpc['name']),
                    'drg': drg_name,
                    'is_cross_tenancy_peering': str(rpc['is_cross_tenancy_peering']),
                    'peer_region_name': str(rpc['peer_region_name']),
                    'peer_rfc_name': self.__get_core_network_rpc_name(rpc['peer_id']),
                    'peer_tenancy_id': rpc['peer_tenancy_id'],
                    'peering_status': rpc['peering_status']
                })
            return data

        except Exception as e:
            self.__print_error("__get_core_network_remote_peering", e)
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
                data.append({
                    'id': ips['id'],
                    'name': ips['name'],
                    'drg': drg,
                    'cpe': cpe,
                    'routes': ips['static_routes'],
                    'tunnels': ips['tunnels'],
                    'defined_tags': ips['defined_tags'],
                    'time_created': ips['time_created'],
                    'freeform_tags': ips['freeform_tags']
                })
            return data

        except Exception as e:
            self.__print_error("__get_core_network_ipsec", e)
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
                data.append({
                    'id': str(vc['id']),
                    'name': str(vc['name']),
                    'bandwidth_shape_name': str(vc['bandwidth_shape_name']),
                    'bgp_management': str(vc['bgp_management']),
                    'bgp_session_state': str(vc['bgp_session_state']),
                    'customer_bgp_asn': str(vc['customer_bgp_asn']),
                    'drg': drg,
                    'lifecycle_state': str(vc['lifecycle_state']),
                    'oracle_bgp_asn': str(vc['oracle_bgp_asn']),
                    'provider_name': str(vc['provider_name']),
                    'provider_service_name': str(vc['provider_service_name']),
                    'provider_state': str(vc['provider_state']),
                    'reference_comment': str(vc['reference_comment']),
                    'service_type': str(vc['service_type']),
                    'time_created': str(vc['time_created']),
                    'cross_connect_mappings': vc['cross_connect_mappings'],
                    'type': str(vc['type'])
                })
            return data

        except Exception as e:
            self.__print_error("__get_core_network_virtual_circuit", e)
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
            self.__print_error("__get_core_network_local_peering", e)

    ##########################################################################
    # get Network Subnet
    ##########################################################################

    def __get_core_network_route(self, route_table_id):
        try:
            route = self.service.search_unique_item(self.service.C_NETWORK, self.service.C_NETWORK_ROUTE, 'id', route_table_id)
            if route:
                if 'name' in route:
                    return route['name']
            return ""

        except Exception as e:
            self.__print_error("__get_core_network_route", e)

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
            self.__print_error("__get_core_network_private_ip", e)

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

            return return_data

        except Exception as e:
            self.__print_error("__get_core_network_main", e)
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
            self.__print_error("__get_core_block_volume_backup_policy", e)

    ##########################################################################
    # get Core Block boot volume
    ##########################################################################

    def __get_core_block_volume_boot(self, boot_volume_id, compartment_name):
        try:
            value = {}
            comp_text = ""
            volume_group = ""

            # get block volume
            bv = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_BOOT, 'id', boot_volume_id)
            if bv:

                # check if different compartment
                if bv['compartment_name'] != compartment_name:
                    comp_text = " (Compartment=" + bv['compartment_name'] + ")"

                if bv['volume_group_name']:
                    volume_group = " - Group " + bv['volume_group_name']

                value = {
                    'sum_info': 'Compute - Block Storage (gb)',
                    'sum_size_gb': bv['size_in_gbs'],
                    'desc': (str(bv['size_in_gbs']) + "gb - " + str(bv['display_name']) + " " + bv['backup_policy'] + volume_group + comp_text),
                    'backup_policy': "None" if bv['backup_policy'] == "" else bv['backup_policy'],
                    'time_created': bv['time_created'],
                    'display_name': bv['display_name'],
                    'defined_tags': bv['defined_tags'],
                    'freeform_tags': bv['freeform_tags']
                }
            return value

        except Exception as e:
            self.__print_error("__get_core_block_volume_boot", e)

    ##########################################################################
    # get Core Block boot volume
    ##########################################################################

    def __get_core_block_volume(self, volume_id, compartment_name):
        try:
            value = {}
            comp_text = ""
            volume_group = ""

            # get block volume
            bv = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_VOL, 'id', volume_id)
            if bv:

                # check if different compartment
                if bv['compartment_name'] != compartment_name:
                    comp_text = " (Compartment=" + bv['compartment_name'] + ")"

                if bv['volume_group_name']:
                    volume_group = " - Group " + bv['volume_group_name']

                value = {
                    'sum_info': 'Compute - Block Storage (gb)',
                    'sum_size_gb': bv['size_in_gbs'],
                    'desc': (str(bv['size_in_gbs']) + "gb - " + str(bv['display_name']) + bv['backup_policy'] + volume_group + comp_text),
                    'time_created': bv['time_created'],
                    'backup_policy': "None" if bv['backup_policy'] == "" else bv['backup_policy'],
                    'display_name': bv['display_name'],
                    'size': str(bv['size_in_gbs']),
                    'defined_tags': bv['defined_tags'],
                    'freeform_tags': bv['freeform_tags']
                }
            return value

        except Exception as e:
            self.__print_error("__get_core_block_volume", e)

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
                value['size'] = (str(backup['size_in_gbs']).rjust(3) + "gb " + ", Stored " + str(backup['unique_size_in_gbs']).rjust(3) + "gb")
                value['sum_info'] = 'Object Storage - BV Backups (gb)'
                value['sum_size_gb'] = (str(backup['unique_size_in_gbs']))
                value[volume_name] = str(backup[volume_name])
                value['id'] = str(backup[volume_name])

                data.append(value)

            if len(data) > 0:
                return sorted(data, key=lambda k: k['name'])
            return data

        except Exception as e:
            self.__print_error("__get_core_block_volume_boot_backup", e)
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
                    if att['volume_id'] == vol['id']:
                        found = True
                        break

                # if not found, add
                if not found:

                    # append to the list
                    volume_group = ""
                    if vol['volume_group_name']:
                        volume_group = " - Group " + vol['volume_group_name']

                    value = {
                        'sum_info': 'Compute - Block Storage (gb)',
                        'sum_size_gb': vol['size_in_gbs'],
                        'desc': ((str(vol['size_in_gbs']) + "gb").ljust(7) + " - " + str(vol['display_name']).ljust(20)[0:19] + " - " + vol['availability_domain'] + " - " + vol['time_created'][0:16] + volume_group)
                    }

                    data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_block_volume_not_attached", e)
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
                        'sum_info': 'Compute - Block Storage (gb)',
                        'sum_size_gb': vol['size_in_gbs'],
                        'desc': ((str(vol['size_in_gbs']) + "gb").ljust(7) + " - " + str(vol['display_name']).ljust(26)[0:25] + " - " + vol['availability_domain'] + " - " + vol['time_created'][0:16] + volume_group)
                    }

                    data.append(value)

            return data

        except Exception as e:
            self.__print_error("__get_core_block_boot_not_attached", e)
            return data

    ##########################################################################
    # get compute boot volume
    ##########################################################################
    def __get_core_block_volume_groups(self, region_name, compartment):

        data = []
        try:
            volgroups = self.service.search_multi_items(self.service.C_BLOCK, self.service.C_BLOCK_VOLGRP, 'region_name', region_name, 'compartment_id', compartment['id'])

            for vplgrp in volgroups:
                value = {'id': vplgrp['id'], 'name': vplgrp['display_name'], 'size_in_gbs': vplgrp['size_in_gbs'],
                         'compartment_name': str(vplgrp['compartment_name']), 'volumes': [],
                         'time_created': vplgrp['time_created'],
                         'defined_tags': vplgrp['defined_tags'],
                         'freeform_tags': vplgrp['freeform_tags']}

                # check volumes
                for vol_id in vplgrp['volume_ids']:
                    vol = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_VOL, 'id', vol_id)
                    if vol:
                        value['volumes'].append(vol['display_name'] + " - " + vol['size_in_gbs'] + "gb")

                # check boot vol
                for vol_id in vplgrp['volume_ids']:
                    vol = self.service.search_unique_item(self.service.C_BLOCK, self.service.C_BLOCK_BOOT, 'id', vol_id)
                    if vol:
                        value['volumes'].append(vol['display_name'] + " - " + vol['size_in_gbs'] + "gb")

                data.append(value)

            if len(data) > 0:
                return sorted(data, key=lambda k: k['name'])
            return data

        except Exception as e:
            self.__print_error("__get_core_block_volume_groups", e)
            return data

    ##########################################################################
    # print compute instances
    ##########################################################################
    def __get_core_compute_instances(self, region_name, compartment):

        data = []
        try:
            instances = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_INST, 'region_name', region_name, 'compartment_id', compartment['id'])

            for instance in instances:
                inst = {'id': instance['id'], 'name': instance['shape'] + " - " + instance['display_name'] + " - " + instance['lifecycle_state'],
                        'sum_info': 'Compute',
                        'sum_shape': instance['image_os'][0:14] + " - " + instance['shape'],
                        'availability_domain': instance['availability_domain'],
                        'fault_domain': instance['fault_domain'],
                        'time_maintenance_reboot_due': str(instance['time_maintenance_reboot_due']),
                        'image': instance['image'], 'image_id': instance['image_id'],
                        'image_os': instance['image_os'],
                        'shape': instance['shape'],
                        'shape_ocpu': instance['shape_ocpu'],
                        'shape_memory_gb': instance['shape_memory_gb'],
                        'shape_storage_tb': instance['shape_storage_tb'],
                        'display_name': instance['display_name'],
                        'compartment_name': instance['compartment_name'],
                        'lifecycle_state': instance['lifecycle_state'],
                        'console_id': instance['console_id'], 'console': instance['console'],
                        'time_created': instance['time_created'],
                        'defined_tags': instance['defined_tags'], 'freeform_tags': instance['freeform_tags']}

                # boot volumes attachments
                boot_vol_attachement = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_BOOT_VOL_ATTACH, 'instance_id', instance['id'])

                bv = []
                for bva in boot_vol_attachement:
                    bvval = {'id': bva['boot_volume_id']}
                    bvval = self.__get_core_block_volume_boot(bva['boot_volume_id'], instance['compartment_name'])
                    if 'display_name' in bvval:
                        bv.append(bvval)

                inst['boot_volume'] = bv

                # Volumes attachements
                block_vol_attaches = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_VOLUME_ATTACH, 'instance_id', instance['id'])

                bvol = []
                for bvola in block_vol_attaches:
                    if bvola['lifecycle_state'] == "ATTACHED":
                        bvval = {'id': bvola['volume_id']}
                        bvval = self.__get_core_block_volume(bvola['volume_id'], instance['compartment_name'])
                        if 'display_name' in bvval:
                            bvol.append(bvval)

                inst['block_volume'] = bvol

                # vnic attachements
                vnicas = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_VNIC_ATTACH, 'instance_id', instance['id'])

                vnicdata = []
                for vnic in vnicas:

                    # handle compartment
                    comp_text = ""
                    if vnic['compartment_name'] != compartment['name']:
                        comp_text = " (Compartment=" + vnic['compartment_name'] + ")"

                    val = {'id': vnic['vnic_id'], 'desc': vnic['vnic_details']['display_name'] + str(comp_text), 'details': vnic['vnic_details']}
                    vnicdata.append(val)

                inst['vnic'] = vnicdata

                # add instance to data
                data.append(inst)

            # return data
            return data

        except BaseException as e:
            self.__print_error("__get_core_compute_instances", e)
            return data

    ##########################################################################
    # print compute images
    ##########################################################################
    def __get_core_compute_images(self, region_name, compartment):

        data = []
        try:
            images = self.service.search_multi_items(self.service.C_COMPUTE, self.service.C_COMPUTE_IMAGES, 'region_name', region_name, 'compartment_id', compartment['id'])

            for image in images:
                value = {'id': image['id'],
                         'desc': image['display_name'].ljust(24) + " - " + image['operating_system'] + " - " + image[
                             'size_in_gbs'].rjust(3) + "gb - Base:  " + image['base_image_name'],
                         'sum_info': 'Object Storage - Images (gb)', 'sum_size_gb': image['size_in_gbs'],
                         'time_created': image['time_created'],
                         'defined_tags': image['defined_tags'], 'freeform_tags': image['freeform_tags']}
                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_core_compute_images", e)
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
            self.__print_error("__get_core_compute_instance_configuration", e)
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
            self.__print_error("__get_core_compute_instance_pool", e)
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
                         'compartment_id': auto['compartment_id'],
                         'resource_id': auto['resource_id'],
                         'resource_name': auto['resource_name'],
                         'resource_type': auto['resource_type'],
                         'policies': auto['policies']
                         }
                data.append(value)

            return data

        except Exception as e:
            self.__print_error("__get_core_compute_autoscaling", e)
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

            data = self.__get_core_block_volume_boot_backup(region_name, compartment, 'boot_volume_id', self.service.C_BLOCK_BOOTBACK)
            if len(data) > 0:
                return_data['boot_volume_backup'] = data

            data = self.__get_core_block_volume_boot_backup(region_name, compartment, 'volume_id', self.service.C_BLOCK_VOLBACK)
            if len(data) > 0:
                return_data['volume_backup'] = data

            return return_data

        except Exception as e:
            self.__print_error("__get_core_compute_main", e)
            return return_data

    ##########################################################################
    # print database db nodes
    ##########################################################################
    def __get_database_db_nodes(self, db_nodes):

        data = []
        try:
            nodeidstr = " "
            nodeid = 0
            for db_node in db_nodes:
                nodeid += 1

                if len(db_nodes) > 1:
                    nodeidstr = str(nodeid)

                vnic_desc = ""
                nsg_names = ""
                nsg_ids = ""
                if 'vnic_details' in db_node:
                    if 'dbdesc' in db_node['vnic_details']:
                        vnic_desc = db_node['vnic_details']['dbdesc']

                    if 'nsg_names' in db_node['vnic_details']:
                        nsg_names = db_node['vnic_details']['nsg_names']

                    if 'nsg_ids' in db_node['vnic_details']:
                        nsg_ids = db_node['vnic_details']['nsg_ids']

                value = {'desc': "Node " + str(nodeidstr) + "  : " + str(db_node['hostname']) + " - " + str(db_node['lifecycle_state']) + " - " + str(vnic_desc + ("" if db_node['fault_domain'] == "None" else " - " + str(db_node['fault_domain']))),
                         'software_storage_size_in_gb': db_node['software_storage_size_in_gb'],
                         'lifecycle_state': db_node['lifecycle_state'],
                         'hostname': db_node['hostname'],
                         'nsg_names': nsg_names,
                         'nsg_ids': nsg_ids,
                         'vnic_details': db_node['vnic_details'],
                         'fault_domain': ("" if db_node['fault_domain'] == "None" else db_node['fault_domain'])
                         }

                data.append(value)

            return data

        except Exception as e:
            self.__print_error("__get_database_db_nodes", e)
            return data

    ##########################################################################
    # print database Databases
    ##########################################################################
    def __get_database_db_databases(self, dbs):

        data = []
        try:

            for db in dbs:

                backupstr = (" - AutoBck=N" if db['auto_backup_enabled'] else " - AutoBck=Y")
                pdb_name = "" if db['pdb_name'] else db['pdb_name'] + " - "
                value = {'name': (str(db['db_name']) + " - " + str(db['db_unique_name']) + " - " + pdb_name +
                                  str(db['db_workload']) + " - " +
                                  str(db['character_set']) + " - " + str(db['lifecycle_state']) + backupstr),
                         'backups': self.__get_database_db_backups(db['backups']),
                         'time_created': db['time_created'],
                         'defined_tags': db['defined_tags'],
                         'dataguard': self.__get_database_db_dataguard(db['dataguard']),
                         'freeform_tags': db['freeform_tags'],
                         'db_name': db['db_name'],
                         'pdb_name': pdb_name,
                         'db_workload': db['db_workload'],
                         'character_set': db['character_set'],
                         'db_unique_name': db['db_unique_name'],
                         'lifecycle_state': db['lifecycle_state'],
                         'id': db['id']
                         }

                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_database_db_databases", e)
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
            self.__print_error("__get_database_db_patches", e)
            return data

    ##########################################################################
    # print database db backups
    ##########################################################################
    def __get_database_db_backups(self, backups):

        data = []
        try:

            for backup in backups:
                bsize = "None"
                ssize = ""
                if backup['database_size_in_gbs']:
                    bsize = "{0:.1f}".format(round(float(backup['database_size_in_gbs']), 1)) + "gb"
                    ssize = "{0:.1f}".format(round(float(backup['database_size_in_gbs']), 1))

                data.append(
                    {'name': str(backup['display_name']) + " - " + str(backup['type']) + " - " + str(backup['lifecycle_state']),
                     'time': str(backup['time_started'])[0:16] + " - " + str(backup['time_ended'])[0:16],
                     'size': bsize,
                     'sum_info': 'Object Storage - DB Backup (gb)',
                     'sum_size_gb': ssize
                     })
            return data

        except Exception as e:
            self.__print_error("__get_database_db_backups", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbnodes
    ##########################################################################
    def __get_database_db_homes(self, db_homes):

        data = []
        try:
            for db_home in db_homes:
                data.append(
                    {'id': str(db_home['id']),
                     'home': str(db_home['display_name']) + " - " + str(db_home['db_version']),
                     'databases': self.__get_database_db_databases(db_home['databases']),
                     'patches': self.__get_database_db_patches(db_home['patches'])
                     })

            # add to main data
            return data

        except Exception as e:
            self.__print_error("__get_database_db_homes", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbnodes
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
            self.__print_error("__get_database_db_dataguard", e)
            return data

    ##########################################################################
    # Database
    ##########################################################################
    #
    # class oci.database.DatabaseClient(config, **kwargs)
    #
    # Below APIs not yet done (TBD):
    # list_db_home_patch_history_entries
    # list_db_system_patch_history_entries
    # list_data_guard_associations
    #
    ##########################################################################
    def __get_database_db_systems(self, region_name, compartment):

        data = []
        try:
            list_db_systems = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_DBSYSTEMS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for dbs in list_db_systems:
                value = {'id': dbs['id'], 'name': dbs['display_name'] + " - " + dbs['shape'] + " - " + dbs['lifecycle_state'],
                         'shape': dbs['shape'],
                         'shape_ocpu': dbs['shape_ocpu'],
                         'shape_memory_gb': dbs['shape_memory_gb'],
                         'shape_storage_tb': dbs['shape_storage_tb'],
                         'display_name': dbs['display_name'],
                         'lifecycle_state': dbs['lifecycle_state'],
                         'sum_info': 'Database ' + dbs['database_edition_short'] + " - " + dbs['shape'] + " - " + dbs['license_model'], 'sum_info_storage': 'Database - Storage (gb)',
                         'sum_size_gb': dbs['data_storage_size_in_gbs'],
                         'availability_domain': dbs['availability_domain'],
                         'cpu_core_count': dbs['cpu_core_count'],
                         'node_count': dbs['node_count'],
                         'version': dbs['version'] + " - " + dbs['database_edition'] + " - " + dbs['license_model'],
                         'host': dbs['hostname'],
                         'domain': dbs['domain'],
                         'data_subnet': dbs['data_subnet'],
                         'data_subnet_id': dbs['data_subnet_id'],
                         'backup_subnet': dbs['backup_subnet'],
                         'backup_subnet_id': dbs['backup_subnet_id'],
                         'scan_dns': dbs['scan_dns_record_id'],
                         'scan_ips': dbs['scan_ips'],
                         'vip_ips': dbs['vip_ips'],
                         'compartment_name': dbs['compartment_name'],
                         'patches': self.__get_database_db_patches(dbs['patches']),
                         'listener_port': dbs['listener_port'],
                         'db_homes': self.__get_database_db_homes(dbs['db_homes']),
                         'db_nodes': self.__get_database_db_nodes(dbs['db_nodes']),
                         'cluster_name': dbs['cluster_name'],
                         'time_created': dbs['time_created'],
                         'defined_tags': dbs['defined_tags'],
                         'freeform_tags': dbs['freeform_tags']}

                if dbs['data_storage_size_in_gbs']:
                    value['data'] = str(dbs['data_storage_size_in_gbs']) + "gb - " + str(dbs['data_storage_percentage']) + "%"
                else:
                    value['data'] = str(dbs['data_storage_percentage']) + "%"

                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_database_db_systems", e)
            return data

    ##########################################################################
    # print database db backups
    ##########################################################################
    def __get_database_autonomous_backups(self, backups):

        data = []
        try:

            for backup in backups:
                backup_type = "Automatic Backup, " if backup['is_automatic'] else "Manual Backup   , "
                data.append(
                    {'name': backup_type + str(backup['display_name']) + " - " + str(backup['type']) + " - " + str(backup['lifecycle_state']),
                     'time': str(backup['time_started'])[0:16] + " - " + str(backup['time_ended'])[0:16]})
            return data

        except Exception as e:
            self.__print_error("__get_database_autonomous_backups", e)
            return data

    ##########################################################################
    # Autonomous
    ##########################################################################
    def __get_database_autonomous_databases(self, region_name, compartment):

        data = []
        try:
            list_autos = self.service.search_multi_items(self.service.C_DATABASE, self.service.C_DATABASE_AUTONOMOUS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for dbs in list_autos:
                value = {'id': str(dbs['id']), 'name': (str(dbs['display_name']) + " - " + str(dbs['license_model']) + " - " + str(dbs['lifecycle_state']) + " (" + str(dbs['sum_count']) + " OCPUs" + (" AutoScale" if dbs['is_auto_scaling_enabled'] else "") + ") - " + dbs['db_workload']),
                         'display_name': dbs['display_name'],
                         'license_model': dbs['license_model'],
                         'lifecycle_state': dbs['lifecycle_state'],
                         'cpu_core_count': str(dbs['cpu_core_count']),
                         'data_storage_size_in_tbs': str(dbs['data_storage_size_in_tbs']),
                         'db_name': str(dbs['db_name']),
                         'compartment_name': str(dbs['compartment_name']),
                         'service_console_url': str(dbs['service_console_url']),
                         'time_created': str(dbs['time_created'])[0:16],
                         'connection_strings': str(dbs['connection_strings']),
                         'sum_info': "Autonomous Database " + str(dbs['db_workload']) + " (OCPUs) - " + dbs['license_model'],
                         'sum_count': str(dbs['sum_count']),
                         'sum_info_storage': "Autonomous Database (tb)",
                         'sum_size_tb': str(dbs['data_storage_size_in_tbs']), 'backups': self.__get_database_autonomous_backups(dbs['backups']),
                         'whitelisted_ips': dbs['whitelisted_ips'],
                         'is_auto_scaling_enabled': dbs['is_auto_scaling_enabled'],
                         'db_workload': dbs['db_workload'],
                         'defined_tags': dbs['defined_tags'], 'freeform_tags': dbs['freeform_tags']}

                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_database_autonomous_databases", e)
            return data

    ##########################################################################
    # Database
    ##########################################################################
    def __get_database_main(self, region_name, compartment):

        return_data = {}
        try:

            data = self.__get_database_db_systems(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['db_system'] = data

            data = self.__get_database_autonomous_databases(region_name, compartment)
            if data:
                if len(data) > 0:
                    return_data['autonomous'] = data

            return return_data

        except Exception as e:
            self.__print_error("__get_database_main", e)
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
                       'private_ip_ids': mt['private_ip_ids']}
                data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_file_storage_mount_target", e)
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
                bytes_details = "Size (" + str(round(int(max_fs_stat_bytes) / 1024 / 1024 / 1024)) + "gb)"

            return bytes_details + ", " + file_details
        except Exception as e:
            self.__print_error("__get_file_storage_limits", e)
            pass

    ##########################################################################
    # print file systems exports
    ##########################################################################
    def __get_file_storage_exports(self, file_system_id):

        try:
            data = []
            exports = self.service.search_multi_items(self.service.C_FILE_STORAGE, self.service.C_FILE_STORAGE_EXPORTS, 'file_system_id', file_system_id)

            for export in exports:
                dataval = {'id': export['id'], 'file_system_id': export['file_system_id'],
                           'time_created': export['time_created'], 'path': export['path'], 'exportset': ""}

                # export set
                if export['export_set']:
                    exp = export['export_set']
                    dataval['exportset'] = str(exp['display_name']) + ", " + str(exp['availability_domain']) + ", Limits: " + self.__get_file_storage_limits(exp)

                # Mount Target
                dataval['mount_target'] = self.__get_file_storage_mount_target(export['export_set_id'])
                data.append(dataval)
            return data

        except Exception as e:
            self.__print_error("__get_file_storage_exports", e)
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
                           'filesystem': fs['display_name'] + " - " + fs['availability_domain'] + " - " + fs[
                               'size_gb'] + "gb metered", 'sum_info': 'File Storage (gb)', 'sum_size_gb': fs['size_gb'],
                           'snapshots': [e['name'] + " - " + e['time_created'][0:16] for e in fs['snapshots']],
                           'exports': self.__get_file_storage_exports(fs['id'])}
                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error("oci_file_storage: ", e)
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
                value = {'name': bucket['name'], 'objects': bucket['approximate_count'],
                         'size': bucket['approximate_size'], 'sum_size_gb': bucket['size_gb'],
                         'sum_info': 'Object Storage - Buckets (gb)',
                         'preauthenticated_requests': bucket['preauthenticated_requests'],
                         'object_lifecycle': bucket['object_lifecycle']}

                value['desc'] = (
                    bucket['name'].ljust(24) + " - " +
                    value['objects'] + " Objs , " +
                    value['size'] + "gb (Approx)" +
                    value['object_lifecycle'] +
                    value['preauthenticated_requests']
                )

                data.append(value)
            return data

        except Exception as e:
            self.__print_error("__get_object_storage_main", e)
            return data

    ##########################################################################
    # print load balancer backed
    ##########################################################################
    def __get_load_balancer_bs_healthchecker(self, health_checker, line):

        try:
            h = health_checker
            if str(h['protocol']) == "TCP":
                if line == 1:
                    return ("TCP, interval(ms)=" + str(h['interval_in_millis']) + ", " +
                            "Timeout(ms)=" + str(h['timeout_in_millis']) + ", " +
                            "retries=" + str(h['retries']))
                if line == 2:
                    return str(h['port']) + "/" + h['protocol']

            # if HTTP
            if str(h['protocol']) == "HTTP":
                if line == 1:
                    return ("HTTP, interval(ms)=" + str(h['interval_in_millis']) + ", " +
                            "Timeout(ms)=" + str(h['timeout_in_millis']) + ", " +
                            "retries=" + str(h['retries']))
                if line == 2:
                    return (str(h['port']) + "/" + h['protocol'] + ", " +
                            "Code=" + str(['return_code']) + ", " +
                            "RegEx=" + str(h['response_body_regex']) + ", " +
                            "url_path =" + str(h['url_path']))
        except Exception as e:
            self.__print_error("__get_load_balancer_bs_healthchecker", e)
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

                # Health Checker
                datahealth = bs['health_checker']
                datahealth['desc1'] = self.__get_load_balancer_bs_healthchecker(bs['health_checker'], 1)
                datahealth['desc2'] = self.__get_load_balancer_bs_healthchecker(bs['health_checker'], 2)
                dataval['health_check'] = datahealth

                data.append(dataval)

            # return the data
            return data

        except Exception as e:
            self.__print_error("__get_load_balancer_backendset", e)
            return data

    ##########################################################################
    # print load balancer config
    ##########################################################################

    def __get_load_balancer_details(self, load_balance_obj):
        data = {}
        try:
            lb = load_balance_obj
            data['id'] = str(lb['id'])
            data['name'] = str(lb['display_name']) + " - " + str(lb['shape_name']) + " - " + ("(Private)" if lb['is_private'] else "(Public)")
            data['status'] = lb['status']
            data['shape_name'] = lb['shape_name']
            data['display_name'] = lb['display_name']
            data['is_private'] = lb['is_private']
            data['ips'] = lb['ip_addresses']
            data['path_route'] = lb['path_route']
            data['nsg_ids'] = lb['nsg_ids']
            data['nsg_names'] = lb['nsg_names']
            data['hostnames'] = [x['desc'] for x in lb['hostnames']]
            data['compartment_name'] = lb['compartment_name']
            data['subnet_ids'] = lb['subnet_ids']

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
            self.__print_error("__get_load_balancer_details", e)
            return data

    ##########################################################################
    # Load Balancer
    ##########################################################################
    def __get_load_balancer_main(self, region_name, compartment):

        data = []
        try:
            load_balancers = self.service.search_multi_items(self.service.C_LB, self.service.C_LB_LOAD_BALANCERS, 'region_name', region_name, 'compartment_id', compartment['id'])

            for load_balance_obj in load_balancers:
                dataval = {'sum_info': "Load Balancer " + str(load_balance_obj['shape_name']),
                           'details': self.__get_load_balancer_details(load_balance_obj),
                           'backendset': self.__get_load_balancer_backendset(load_balance_obj['id'])}
                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error("__get_load_balancer_main", e)
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
                           'time_created': stack['time_created'],
                           'defined_tags': stack['defined_tags'], 'freeform_tags': stack['freeform_tags']}

                # query jobs
                datajob = []
                for job in stack['jobs']:
                    datajob.append(
                        str(job['display_name']) + " - " +
                        str(job['operation']).ljust(10) + " - " +
                        str(job['lifecycle_state']).ljust(10) + " - " +
                        str(job['time_finished'])[0:16]
                    )

                # add the jobs to the array
                dataval['jobs'] = datajob
                data.append(dataval)

            return data

        except Exception as e:
            self.__print_error("__get_resource_management_main", e)
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

            return data

        except Exception as e:
            self.__print_error("__get_email_main", e)
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
                           'lifecycle_state': container['lifecycle_state'],
                           'kubernetes_version': container['kubernetes_version'],
                           'compartment_name': container['compartment_name'],
                           'node_pools': [],
                           'vcn_name': self.__get_core_network_vcn_name(container['vcn_id'])}

                    # add the node pools
                    nodes = self.service.search_multi_items(self.service.C_CONTAINER, self.service.C_CONTAINER_NODE_POOLS, 'cluster_id', container['id'])
                    for np in nodes:
                        nval = {'id': np['id'], 'name': np['name'], 'node_image_id': np['node_image_id'], 'node_image_name': np['node_image_name'],
                                'kubernetes_version': np['kubernetes_version'], 'node_shape': np['node_shape'],
                                'quantity_per_subnet': np['quantity_per_subnet'], 'compartment_name': np['compartment_name'], 'subnets': []}

                        # subnets
                        for sub in np['subnet_ids']:
                            nval['subnets'].append(self.__get_core_network_subnet_name(sub))
                        val['node_pools'].append(nval)

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_container_main", e)
            pass

    ##########################################################################
    # Streams
    ##########################################################################
    def __get_streams_main(self, region_name, compartment):
        try:
            streams = self.service.search_multi_items(self.service.C_STREAMS, self.service.C_STREAMS_STREAMS, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = []
            if streams:
                for stream in streams:
                    val = {'id': stream['id'],
                           'name': stream['name'],
                           'partitions': stream['partitions'],
                           'time_created': stream['time_created'],
                           'messages_endpoint': stream['messages_endpoint'],
                           'defined_tags': stream['defined_tags'],
                           'freeform_tags': stream['freeform_tags'],
                           'compartment_name': stream['compartment_name']}

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_streams_main", e)
            pass

    ##########################################################################
    # monitoring
    ##########################################################################
    def __get_monitoring_main(self, region_name, compartment):
        try:
            alarms = self.service.search_multi_items(self.service.C_MONITORING, self.service.C_MONITORING_ALARMS, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = []
            if alarms:
                for alarm in alarms:
                    val = {'id': alarm['id'],
                           'display_name': alarm['display_name'],
                           'metric_compartment_id': alarm['metric_compartment_id'],
                           'namespace': alarm['namespace'],
                           'query': alarm['query'],
                           'is_enabled': alarm['is_enabled'],
                           'destinations': alarm['destinations'],
                           'destinations_names': [],
                           'severity': alarm['severity'],
                           'defined_tags': alarm['defined_tags'],
                           'freeform_tags': alarm['freeform_tags'],
                           'compartment_name': alarm['compartment_name']}

                    # find the topics
                    for dest in alarm['destinations']:
                        topic = self.service.search_unique_item(self.service.C_NOTIFICATIONS, self.service.C_NOTIFICATIONS_TOPICS, 'topic_id', dest)
                        if topic:
                            val['destinations_names'].append(topic['name'] + " - " + topic['description'])

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_monitoring_main", e)
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
                           'subscriptions': self.service.search_multi_items(self.service.C_NOTIFICATIONS, self.service.C_NOTIFICATIONS_SUBSCRIPTIONS, 'topic_id', topic['topic_id'])
                           }

                    data.append(val)
            return data

        except Exception as e:
            self.__print_error("__get_notifications_main", e)
            pass

    ##########################################################################
    # edge
    ##########################################################################
    def __get_load_edge_main(self, region_name, compartment):

        try:
            healthcheck_http = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_HEALTHCHECK_HTTP, 'region_name', region_name, 'compartment_id', compartment['id'])
            healthcheck_ping = self.service.search_multi_items(self.service.C_EDGE, self.service.C_EDGE_HEALTHCHECK_PING, 'region_name', region_name, 'compartment_id', compartment['id'])

            data = {}
            if len(healthcheck_http) > 0 or len(healthcheck_ping) > 0:
                data['healthcheck'] = {'http': healthcheck_http, 'ping': healthcheck_ping}
            return data

        except Exception as e:
            self.__print_error("__get_load_edge_main", e)
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
            self.__print_error("__get_limits_main", e)
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
            self.__print_error("__get_quotas_main", e)
            pass
