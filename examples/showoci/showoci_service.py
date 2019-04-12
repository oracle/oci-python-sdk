
##########################################################################
# Copyright(c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# showocy_service.py
#
# @Created On  : Mar 17 2019
# @Last Updated: Apr 14 2019
# @author      : Adi Zohar
# @Version     : 19.4.14
#
# Supports Python 2.7 and above, Python 3 recommended
#
# coding: utf-8
##########################################################################
# This file has ShowOCIService class, and ShowOCIFlags
#
# ShowOCIService - class has all OCI APIs , once called load_service_data(),
# it will load all the data to the "data" property
#
# ShowOCIFlags   - class has the flags for calling the service Classes
#
##########################################################################
from __future__ import print_function
import oci
import time


##########################################################################
# class ShowOCIService
##########################################################################
class ShowOCIFlags(object):
    # Read Flags
    read_identity = False
    read_network = False
    read_compute = False
    read_database = False
    read_file_storage = False
    read_object_storage = False
    read_load_balancer = False
    read_email_distribution = False
    read_resource_management = False
    read_containers = False
    read_streams = False
    read_ManagedCompartmentForPaaS = True
    read_root_compartment = True

    # filter flags
    filter_by_region = ""
    filter_by_compartment = ""

    # version, config files and proxy
    proxy = ""
    showoci_version = ""
    config_file = oci.config.DEFAULT_LOCATION
    config_section = oci.config.DEFAULT_PROFILE

    # flag if to run on compartment
    run_on_compartments = False

    ############################################
    # Init
    ############################################
    def __init__(self):
        pass

    ############################################
    # get run on compartments flag
    ############################################
    def is_loop_on_compartments(self):
        return (self.read_network or
                self.read_compute or
                self.read_database or
                self.read_file_storage or
                self.read_object_storage or
                self.read_load_balancer or
                self.read_email_distribution or
                self.read_resource_management or
                self.read_containers or
                self.read_streams)

    ############################################
    # check if to load basic network (vcn+subnets)
    ############################################
    def is_load_basic_network(self):
        return (self.read_network or
                self.read_compute or
                self.read_database or
                self.read_file_storage or
                self.read_load_balancer or
                self.read_containers)


##########################################################################
# class ShowOCIService
##########################################################################
class ShowOCIService(object):
    oci_compatible_version = "2.2.5"

    ##########################################################################
    # Global Constants
    ##########################################################################
    # print header options
    print_header_options = {0: 90, 1: 60, 2: 30, 3: 75}

    # Network Identifiers
    C_NETWORK = 'network'
    C_NETWORK_IPS = 'ipsec'
    C_NETWORK_VCN = 'vcn'
    C_NETWORK_SGW = 'sgw'
    C_NETWORK_NAT = 'nat'
    C_NETWORK_DRG = 'drg'
    C_NETWORK_DRG_AT = 'drg_attached'
    C_NETWORK_CPE = 'cpe'
    C_NETWORK_RPC = 'rpc'
    C_NETWORK_IGW = 'igw'
    C_NETWORK_LPG = 'lpg'
    C_NETWORK_SLIST = 'seclist'
    C_NETWORK_ROUTE = 'route'
    C_NETWORK_DHCP = 'dhcp'
    C_NETWORK_SUBNET = 'subnet'
    C_NETWORK_VC = 'virtualcircuit'
    C_NETWORK_PRIVATEIP = 'privateip'

    # Identity Identifiers
    C_IDENTITY = 'identity'
    C_IDENTITY_ADS = 'availability_domains'
    C_IDENTITY_USERS = 'users'
    C_IDENTITY_GROUPS = 'groups'
    C_IDENTITY_POLICIES = 'policies'
    C_IDENTITY_TENANCY = 'tenancy'
    C_IDENTITY_COMPARTMENTS = 'compartments'
    C_IDENTITY_REGIONS = 'regions'
    C_IDENTITY_PROVIDERS = 'providers'
    C_IDENTITY_DYNAMIC_GROUPS = 'dynamic_groups'
    C_IDENTITY_USERS_GROUPS_MEMBERSHIP = 'users_groups_membership'

    # Compute Identifiers
    C_COMPUTE = 'compute'
    C_COMPUTE_INST = 'instance'
    C_COMPUTE_INST_CONFIG = 'instance_config'
    C_COMPUTE_INST_POOL = 'instance_pool'
    C_COMPUTE_IMAGES = 'instance_image'
    C_COMPUTE_BOOT_VOL_ATTACH = 'instance_boot_vol_attach'
    C_COMPUTE_VOLUME_ATTACH = 'instance_volume_attach'
    C_COMPUTE_VNIC_ATTACH = 'instance_vnic_attach'

    # Block Storage Identifiers
    C_BLOCK = 'blockstorage'
    C_BLOCK_BOOT = 'boot'
    C_BLOCK_BOOTBACK = 'boot_back'
    C_BLOCK_VOL = 'volume'
    C_BLOCK_VOLBACK = 'volume_back'
    C_BLOCK_VOLGRP = 'volume_group'

    # Load Balancer Identifiers
    C_LB = 'loadbalancer'
    C_LB_LOAD_BALANCERS = 'load_balancers'
    C_LB_BACKEND_SETS = 'backend_sets'

    # Load Balancer Identifiers
    C_OS = 'objectstorage'
    C_OS_BUCKETS = 'buckets'

    # Load Balancer Identifiers
    C_ORM = 'resource_management'
    C_ORM_STACKS = 'stacks'

    # Emails
    C_EMAIL = 'email'
    C_EMAIL_SUPPRESSIONS = 'suppressions'
    C_EMAIL_SENDERS = 'senders'

    # File Storage
    C_FILE_STORAGE = 'file_storage'
    C_FILE_STORAGE_FILESYSTEMS = 'filesystems'
    C_FILE_STORAGE_MOUNTS = 'mounts'
    C_FILE_STORAGE_EXPORTS = 'exports'

    # database
    C_DATABASE = "database"
    C_DATABASE_DBSYSTEMS = "dbsystems"
    C_DATABASE_AUTONOMOUS = "autonomous"

    # container
    C_CONTAINER = "container"
    C_CONTAINER_CLUSTERS = "clusters"
    C_CONTAINER_NODE_POOLS = "nodepools"

    # streams
    C_STREAMS = "streams"
    C_STREAMS_STREAMS = "streams"

    # Error flag
    error = 0
    warning = 0

    ##########################################################################
    # Local Variables
    # data - hold the data data
    # flags - hold the extract flags
    ##########################################################################
    flags = None
    data = {}

    ##########################################################################
    # init class
    # Creates a new data object
    #
    # required:
    #    flags parameters - Class ShowOCIFlags
    #
    # Optional Parameters:
    #    config_file - config_File to authenticate to OCI
    #    config_section - section in the config file
    ##########################################################################
    def __init__(self, flags):

        if not isinstance(flags, ShowOCIFlags):
            raise TypeError("flags must be ShowOCIFlags class")

        # check OCI Compatible
        self.check_oci_version_compatible()

        # assign the flags variable
        self.flags = flags

        # initialize the oci config
        self.config = oci.config.from_file(flags.config_file, flags.config_section)

    ##########################################################################
    # load_data
    ##########################################################################
    def load_service_data(self):
        return self.__load_data_main()

    ##########################################################################
    # Print header centered
    ##########################################################################
    def print_header(self, name, category):
        chars = int(self.print_header_options[category])
        print("")
        print('#' * chars)
        print("#" + str(name).center(chars - 2, " ") + "#")
        print('#' * chars)

    ##########################################################################
    # return tenancy data
    ##########################################################################
    def get_tenancy(self):
        return self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY]

    ##########################################################################
    # return compartment data
    ##########################################################################
    def get_compartment(self):
        return self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]

    ##########################################################################
    # return availability domains
    ##########################################################################
    def get_availability_domains(self, region_name):
        ads = self.data[self.C_IDENTITY][self.C_IDENTITY_ADS]
        return [e for e in ads if e['region_name'] == region_name]

    ##########################################################################
    # return subnet
    ##########################################################################
    def get_network_subnet(self, subnet_id, detailed=False):
        try:
            result = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_SUBNET, 'id', subnet_id)
            if result != "":
                if detailed:
                    return result['name'] + ",  " + result['cidr_block'] + ", VCN (" + result['vcn_name'] + ")"
                else:
                    return result['name']
            return ""

        except Exception as e:
            self.__print_error("get_network_subnet", e)

    ##########################################################################
    # return identity data
    ##########################################################################
    def get_identity(self):
        return self.data[self.C_IDENTITY]

    ##########################################################################
    # return oci version
    ##########################################################################
    def get_oci_version(self):
        return oci.version.__version__

    ##########################################################################
    # check oci version
    ##########################################################################
    def check_oci_version_compatible(self):

        try:
            # loop on digits
            for i, rl in zip(self.get_oci_version().split("."), self.oci_compatible_version.split(".")):
                if i > rl:
                    return True
                if i < rl:
                    print("")
                    print("*********************************************************************")
                    print("Error, OCI version " + self.oci_compatible_version + " required !")
                    print("OCI Version installed = " + self.get_oci_version())
                    print("Aboting.")
                    print("*********************************************************************")
                    print("")
                    raise SystemExit

        except Exception as e:
            self.__print_error("check_oci_version_compatible", e)

    ##########################################################################
    # search unique items with multi parameters
    # parameters are
    # MODULE - data Module
    # SECTION - data Sub module
    # P1, v1 - param and value
    # p2, v2 - param and value - optional
    # p3, v3 - param and value - optional
    ##########################################################################

    def search_unique_item(self, module, section, p1, v1, p2=None, v2=None, p3=None, v3=None):
        try:
            result = self.search_multi_items(module, section, p1, v1, p2, v2, p3, v3)

            if not result:
                return None

            return result[0]

        except Exception as e:
            self.__print_error("search_unique_item", e)

    ##########################################################################
    # search multi items with multi parameters
    # parameters are
    # MODULE - data Module
    # SECTION - data Sub module
    # P1, v1 - param and value
    # p2, v2 - param and value - optional
    # p3, v3 - param and value - optional
    ##########################################################################

    def search_multi_items(self, module, section, p1, v1, p2=None, v2=None, p3=None, v3=None):
        try:
            if len(module) == 0 or len(section) == 0:
                return []

            # check if module exists
            if module not in self.data:
                return []

            # check if section exists
            if section not in self.data[module]:
                return []

            # assign data area to array
            array = self.data[module][section]

            # check parameters and search
            if p2 and v2 and p3 and v3:
                return [e for e in array if e[p1] == v1 and e[p2] == v2 and e[p3] == v3]

            # check parameters and search
            if p2 and v2:
                return [e for e in array if e[p1] == v1 and e[p2] == v2]

            return [e for e in array if e[p1] == v1]

        except Exception as e:
            self.__print_error("search_multi_items", e)

    ##########################################################################
    # initialize data key if not exist
    ##########################################################################
    def __initialize_data_key(self, module, section):
        if module not in self.data:
            self.data[module] = {}
        if section not in self.data[module]:
            self.data[module][section] = []

    ##########################################################################
    # print status message
    ##########################################################################
    def __load_print_status(self, msg):
        print("--> " + msg.ljust(25) + "<-- ", end="")

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
    # check service error to ignore
    ##########################################################################
    def __check_service_error(self, code):
        return 'auth' in str(code).lower() or code == 'Forbidden' or code == 'TooManyRequests' or 'notfound' in str(code).lower()

    ##########################################################################
    # check if managed paas compartment
    ##########################################################################
    def __if_managed_paas_compartment(self, name):
        return name == "ManagedCompartmentForPaaS"

    ##########################################################################
    # print count result
    ##########################################################################
    def __load_print_cnt(self, cnt, start_time):
        elapsed_time = time.time() - start_time
        print(" (" + str(int(cnt)) + ") - " + str(round(elapsed_time)) + " sec")

    ##########################################################################
    # print auth warning
    ##########################################################################
    def __load_print_auth_warning(self, special_char="a"):
        self.warning += 1
        print(special_char, end="")

    ##########################################################################
    # Main procedure to read data to the data
    ##########################################################################
    def __load_data_main(self):
        try:
            print("Guide: '.' Compartment, '+' VCN, '-' Subnets, 'a' - auth/notfound")

            # print filter by
            if self.flags.filter_by_region:
                print("Filtered by Region      = " + self.flags.filter_by_region)

            if self.flags.filter_by_compartment:
                print("Filtered by Compartment = " + self.flags.filter_by_compartment)

            print("")

            # load identity
            self.__load_identity_main()

            # check if data not loaded, abort
            if self.C_IDENTITY not in self.data:
                return False

            # check if need to loop on compartments
            # if the flags required data from regions
            if self.flags.is_loop_on_compartments():

                # run on each subscribed region
                tenancy = self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY]
                for region_name in tenancy['list_region_subscriptions']:

                    # if filtered by region skip if not cmd.region
                    if self.flags.filter_by_region and str(self.flags.filter_by_region) not in region_name:
                        continue

                    # load region into data
                    self.__load_oci_region_data(region_name)

            return True

        except Exception as e:
            self.__print_error("__load_data_main: ", e)
            raise

    ##########################################################################
    # run on Region
    ##########################################################################
    def __load_oci_region_data(self, region_name):

        # Assign Region to config file

        self.print_header("Region " + region_name, 2)
        self.config['region'] = region_name

        # load ADs
        if self.flags.is_load_basic_network():
            self.__load_identity_availability_domain(region_name)

        # Load Network
        if self.flags.is_load_basic_network():
            self.__load_core_network_main()

        # if load compute
        if self.flags.read_compute:
            self.__load_core_compute_main()

        # database
        if self.flags.read_database:
            self.__load_database_main()

        # load balancers
        if self.flags.read_load_balancer:
            self.__load_load_balancer_main()

        # object storage
        if self.flags.read_object_storage:
            self.__load_object_storage_main()

        # file storage - not exist in toronto yet
        if region_name != "ca-toronto-1":
            if self.flags.read_file_storage:
                self.__load_file_storage_main()

        # only available in US Regions
        if region_name == "us-ashburn-1" or region_name == "us-phoenix-1":

            # email distributions
            if self.flags.read_email_distribution:
                self.__load_email_main()

            # resource management - only at us for now
            if self.flags.read_resource_management:
                self.__load_resource_management_main()

            # if streams
            if self.flags.read_streams:
                self.__load_streams_main()

        # containers - not exist in toronto yet
        if region_name != "ca-toronto-1":
            if self.flags.read_containers:
                self.__load_container_main()

    ##########################################################################
    # Identity Module
    ##########################################################################
    def __load_identity_main(self):
        try:
            print("Identity...")

            # create identity object
            identity = oci.identity.IdentityClient(self.config)
            if self.flags.proxy:
                identity.base_client.session.proxies = {'https': self.flags.proxy}

            # get tenancy id from the config file
            tenancy_id = self.config["tenancy"]
            self.data[self.C_IDENTITY] = {}

            # loading main components - tenancy and compartments
            self.__load_identity_tenancy(identity, tenancy_id)
            self.__load_identity_compartments(identity)

            # if loading the full identity - load the rest
            if self.flags.read_identity:
                self.__load_identity_users_groups(identity, tenancy_id)
                self.__load_identity_dynamic_groups(identity, tenancy_id)
                self.__load_identity_policies(identity)
                self.__load_identity_providers(identity, tenancy_id)

            print("")
        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_identity_main: ", e)

    ##########################################################################
    # Load Tenancy
    ##########################################################################

    def __load_identity_tenancy(self, identity, tenancy_id):
        self.__load_print_status("Tenancy")
        start_time = time.time()

        try:
            tenancy = identity.get_tenancy(tenancy_id).data
            try:
                sub_regions = identity.list_region_subscriptions(tenancy.id).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                else:
                    raise

            data_subs = [str(es.region_name) for es in sub_regions]
            data = {
                'id': tenancy.id,
                'name': tenancy.name,
                'home_region_key': tenancy.home_region_key,
                'subscribe_regions': str(', '.join(x for x in data_subs)),
                'list_region_subscriptions': data_subs
            }
            self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY] = data
            self.__load_print_cnt(1, start_time)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            raise Exception("Error in __load_identity_tenancy: " + str(e.args))

    ##########################################################################
    # Load compartments
    ##########################################################################
    def __load_identity_compartments(self, identity):

        compartments = []
        self.__load_print_status("Compartments")
        start_time = time.time()

        try:
            # point to tenancy
            tenancy = self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY]

            # read all compartments to variable
            all_compartments = []
            try:
                all_compartments = oci.pagination.list_call_get_all_results(
                    identity.list_compartments,
                    tenancy['id'],
                    compartment_id_in_subtree=True
                ).data

            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                else:
                    raise

            ###################################################
            # Build Compartments
            # return nested compartment list
            ###################################################
            def build_compartments_nested(identity_client, cid, path):
                try:
                    compartment_list = [item for item in all_compartments if str(item.compartment_id) == str(cid)]

                    if path != "":
                        path = path + " / "

                    for c in compartment_list:
                        if c.lifecycle_state == oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                            cvalue = {'id': str(c.id), 'name': str(c.name), 'path': path + str(c.name)}
                            compartments.append(cvalue)
                            build_compartments_nested(identity_client, c.id, cvalue['path'])

                except Exception as error:
                    raise Exception("Error in build_compartments_nested: " + str(error.args))

            ###################################################
            # Add root compartment
            ###################################################
            if self.flags.read_root_compartment:
                value = {'id': tenancy['id'], 'name': tenancy['name'] + " (root)", 'path': "/ " + tenancy['name'] + " (root)"}
                compartments.append(value)

            # Build the compartments
            build_compartments_nested(identity, tenancy['id'], "")

            # sort the compartment
            sorted_compartments = sorted(compartments, key=lambda k: k['path'])

            # if not filtered by compartment return
            if not self.flags.filter_by_compartment:
                self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS] = sorted_compartments
                self.__load_print_cnt(len(compartments), start_time)
                return

            # if filter by compartment, then reduce list and return new list
            filtered_compart = []
            for x in sorted_compartments:
                if self.flags.filter_by_compartment in x['name']:
                    filtered_compart.append(x)

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS] = filtered_compart
            self.__load_print_cnt(len(filtered_compart), start_time)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            raise Exception("Error in __load_identity_compartments: " + str(e.args))

    ##########################################################################
    # Get Identity Users
    ##########################################################################

    def __load_identity_users_groups(self, identity, tenancy_id):
        datauser = []
        datagroup = []
        self.__load_print_status("Users and Groups")
        start_time = time.time()

        try:
            users = []
            groups = []
            identity_providers = []

            try:
                users = oci.pagination.list_call_get_all_results(identity.list_users, tenancy_id).data
                groups = oci.pagination.list_call_get_all_results(identity.list_groups, tenancy_id).data
                identity_providers = identity.list_identity_providers("SAML2", tenancy_id).data
            except oci.exceptions.ServiceError as item:
                if 'auth' in item.code.lower() or item.code == 'Forbidden':
                    self.__load_print_auth_warning()
                else:
                    raise

            members = []

            ##########################
            # add groups
            ##########################
            for group in groups:
                try:
                    user_group_memberships = oci.pagination.list_call_get_all_results(
                        identity.list_user_group_memberships, tenancy_id, group_id=group.id).data

                    group_users = []
                    for ugm in user_group_memberships:
                        members.append({'user_id': ugm.user_id, 'group_id': ugm.group_id})
                        for item in [str(item_var.name) for item_var in users if item_var.id == ugm.user_id]:
                            group_users.append(item)

                    if group_users:
                        datagroup.append({'id': group.id, 'name': group.name, 'users': ', '.join(x for x in group_users)})

                except oci.exceptions.ServiceError as error:
                    if 'auth' in error.code.lower() or error.code == 'Forbidden':
                        self.__load_print_auth_warning()
                        continue
                    raise

            # load to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_GROUPS] = datagroup

            ##########################
            # add users
            ##########################
            for user in users:

                group_users = []

                # find the group users
                for ugm in [e['group_id'] for e in members if user.id == e['user_id']]:
                    group_users.append(next(item for item in groups if item.id == ugm).name)

                # identity provider
                identity_provider_name = ""
                if user.identity_provider_id:
                    identity_provider_name = next(
                        item for item in identity_providers if item.id == user.identity_provider_id).name

                # add info
                datauser.append({
                    'id': user.id,
                    'name': str(user.name),
                    'description': str(user.description),
                    'is_mfa_activated': str(user.is_mfa_activated),
                    'lifecycle_state': str(user.lifecycle_state),
                    'time_created': str(user.time_created),
                    'identity_provider_id': str(user.identity_provider_id),
                    'identity_provider_name': str(identity_provider_name),
                    'groups': ', '.join(x for x in group_users)
                })

            # load to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_USERS] = datauser

            self.__load_print_cnt(len(datauser), start_time)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_identity_users_groups", e)

    ##########################################################################
    # Print Identity Policies
    ##########################################################################
    def __load_identity_policies(self, identity):
        data = []
        self.__load_print_status("Policies")
        start_time = time.time()

        try:
            compartments = self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]

            for c in compartments:
                if self.__if_managed_paas_compartment(c['name']) and not self.flags.read_ManagedCompartmentForPaaS:
                    continue

                try:
                    policies = identity.list_policies(c['id']).data

                    if policies:
                        datapol = []
                        for policy in policies:
                            datapol.append({'name': policy.name, 'statements': [str(e) for e in policy.statements]})
                        dataval = {'compartment_id': str(c['id']), 'compartment_name': "Compartment " + c['name'],
                                   'compartment_path': "Compartment " + c['path'], 'policies': datapol}
                        data.append(dataval)

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_POLICIES] = data
            self.__load_print_cnt(len(data), start_time)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_identity_policies", e)

    ##########################################################################
    # Print Identity Providers
    ##########################################################################
    def __load_identity_providers(self, identity, tenancy_id):
        data = []
        self.__load_print_status("Providers")
        start_time = time.time()

        try:
            groups = self.data[self.C_IDENTITY][self.C_IDENTITY_GROUPS]

            try:
                identity_providers = identity.list_identity_providers("SAML2", tenancy_id).data

                for d in identity_providers:

                    # get identity providers groups
                    try:
                        igm = oci.pagination.list_call_get_all_results(identity.list_idp_group_mappings, d.id).data

                        # get the group data
                        groupdata = []
                        for ig in igm:
                            for grp in groups:
                                if grp['id'] == ig.group_id:
                                    groupdata.append(ig.idp_group_name + " <-> " + grp['name'])

                        data.append({
                            'id': str(d.id),
                            'name': str(d.name),
                            'description': str(d.description),
                            'product_type': str(d.product_type),
                            'protocol': str(d.protocol),
                            'redirect_url': str(d.redirect_url),
                            'metadata_url': str(d.metadata_url),
                            'group_map': groupdata
                        })

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                else:
                    raise

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_PROVIDERS] = data
            self.__load_print_cnt(len(data), start_time)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_identity_providers", e)

    ##########################################################################
    # Print Dynamic Groups
    ##########################################################################
    def __load_identity_dynamic_groups(self, identity, tenancy_id):

        data = []
        self.__load_print_status("Dynamic Groups")
        start_time = time.time()

        try:
            dynamic_groups = []
            try:
                dynamic_groups = oci.pagination.list_call_get_all_results(identity.list_dynamic_groups, tenancy_id).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                else:
                    raise

            for dg in dynamic_groups:
                data.append({
                    'id': str(dg.id),
                    'name': str(dg.name),
                    'description': str(dg.description),
                    'matching_rule': str(dg.matching_rule)
                })

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_DYNAMIC_GROUPS] = data
            self.__load_print_cnt(len(data), start_time)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_identity_dynamic_groups", e)

    ##########################################################################
    # Load Identity Availability Domains
    ##########################################################################
    def __load_identity_availability_domain(self, region_name):

        try:
            print("Identity...")

            # create identity object
            identity = oci.identity.IdentityClient(self.config)
            if self.flags.proxy:
                identity.base_client.session.proxies = {'https': self.flags.proxy}

            self.__load_print_status("Availability Domains")
            start_time = time.time()

            # initalize the key
            self.__initialize_data_key(self.C_IDENTITY, self.C_IDENTITY_ADS)

            # get the domains
            availability_domains = []
            try:
                availability_domains = identity.list_availability_domains(self.config["tenancy"]).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                else:
                    raise

            data = []
            cnt = 0
            for ad in availability_domains:
                data.append({'region_name': region_name, 'id': str(ad.id), 'name': str(ad.name)})
                cnt += 1

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_ADS] += data

            # mark count
            self.__load_print_cnt(len(data), start_time)

            print("")

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_identity_availability_domains", e)

    ##########################################################################
    # Load all networks to data
    ##########################################################################
    #
    # class oci.core.virtual_network_client.virtual_networkClient(config, **kwargs)
    #
    #    TBD Apis
    #    list_allowed_peer_regions_for_remote_peering(**kwargs)
    #    list_private_ips(**kwargs) - this is performance issue running all subnets
    #    list_public_ips(scope, compartment_id, **kwargs)
    #    list_cross_connect_groups(compartment_id, **kwargs)
    #    list_cross_connect_locations(compartment_id, **kwargs)
    #    list_cross_connects(compartment_id, **kwargs)
    #    list_crossconnect_port_speed_shapes(compartment_id, **kwargs)
    #
    ##########################################################################
    def __load_core_network_main(self):

        try:
            print("Network...")

            # Open connectivity to OCI
            virtual_network = oci.core.VirtualNetworkClient(self.config)
            if self.flags.proxy:
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]

            # add the key to the network if not exists
            self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_VCN)
            self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SUBNET)

            # reference to network:
            network = self.data[self.C_NETWORK]

            # append the data for vcns
            vcns = self.__load_core_network_vcn(virtual_network, compartments)
            network[self.C_NETWORK_VCN] += vcns

            # append the data for subnets
            subnets = self.__load_core_network_subnet(virtual_network, compartments, network[self.C_NETWORK_VCN])
            network[self.C_NETWORK_SUBNET] += subnets

            # if to load all network resources
            if self.flags.read_network:
                # add the key to the network if not exists
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SGW)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_NAT)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DRG)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DRG_AT)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_CPE)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_IPS)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_RPC)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_VC)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_IGW)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_LPG)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_ROUTE)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SLIST)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DHCP)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_PRIVATEIP)

                # append the data
                network[self.C_NETWORK_SGW] += self.__load_core_network_sgw(virtual_network, compartments)
                network[self.C_NETWORK_NAT] += self.__load_core_network_nat(virtual_network, compartments)
                network[self.C_NETWORK_DRG] += self.__load_core_network_drg(virtual_network, compartments)
                network[self.C_NETWORK_DRG_AT] += self.__load_core_network_dra(virtual_network, compartments)
                network[self.C_NETWORK_CPE] += self.__load_core_network_cpe(virtual_network, compartments)
                network[self.C_NETWORK_IPS] += self.__load_core_network_ips(virtual_network, compartments)
                network[self.C_NETWORK_RPC] += self.__load_core_network_rpc(virtual_network, compartments)
                network[self.C_NETWORK_VC] += self.__load_core_network_vc(virtual_network, compartments)
                network[self.C_NETWORK_IGW] += self.__load_core_network_igw(virtual_network, compartments, vcns)
                network[self.C_NETWORK_LPG] += self.__load_core_network_lpg(virtual_network, compartments, vcns)
                network[self.C_NETWORK_SLIST] += self.__load_core_network_seclst(virtual_network, compartments, vcns)
                network[self.C_NETWORK_DHCP] += self.__load_core_network_dhcpop(virtual_network, compartments, vcns)

                routes = self.__load_core_network_routet(virtual_network, compartments, vcns)
                network[self.C_NETWORK_ROUTE] += routes
                network[self.C_NETWORK_PRIVATEIP] += self.__load_core_network_privateip(virtual_network, routes)

            print("")
        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_main", e)
            raise

    ##########################################################################
    # data network read vcns
    ##########################################################################
    def __load_core_network_vcn(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()
        try:

            self.__load_print_status("Virtual Cloud Networks")

            # loop on all compartments
            for compartment in compartments:

                vcns = []
                try:
                    vcns = oci.pagination.list_call_get_all_results(
                        virtual_network.list_vcns,
                        compartment['id'],
                        lifecycle_state=oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE,
                        sort_by="DISPLAYNAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on the array
                # vcn = oci.core.models.Vcn()
                for vcn in vcns:
                    val = {'id': str(vcn.id), 'name': str(vcn.cidr_block) + " - " + str(vcn.display_name) + " - " + str(vcn.vcn_domain_name),
                           'display_name': str(vcn.display_name),
                           'time_created': str(vcn.time_created), 'compartment_name': str(compartment['name']),
                           'defined_tags': [] if vcn.defined_tags is None else vcn.defined_tags,
                           'freeform_tags': [] if vcn.freeform_tags is None else vcn.freeform_tags,
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_vcn", e)
            return data

    ##########################################################################
    # data network read igw
    # igw requires vcn_id and compartment_id as parameters
    # therefore, need to loop on both which is performance issue
    # for Performance improvements, I check if the igw exist in the VCN compartment
    # first, if igw found, return it - only one igw can be assigned to vcn
    # if not, scan all compartments
    ##########################################################################
    def __load_core_network_igw(self, virtual_network, compartments, vcns):

        cnt = 0
        data = []
        start_time = time.time()

        try:

            self.__load_print_status("Internet Gateways")

            # loop on all vcns - vcn is must parameter
            for vcn in vcns:
                print("+", end="")
                foundIgw = False

                # check if igw in the vcn compartment
                igws = []
                try:
                    igws = virtual_network.list_internet_gateways(
                        vcn['compartment_id'], vcn['id'],
                        lifecycle_state=oci.core.models.InternetGateway.LIFECYCLE_STATE_AVAILABLE
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                    else:
                        raise

                # igw = oci.core.models.InternetGateway()
                for igw in igws:
                    val = {'id': str(igw.id), 'vcn_id': str(igw.vcn_id), 'name': str(igw.display_name),
                           'time_created': str(igw.time_created), 'compartment_name': vcn['compartment_name'],
                           'compartment_id': vcn['compartment_id'], 'region_name': str(self.config['region'])}
                    data.append(val)
                    foundIgw = True
                    cnt += 1

                # if found continue to next vcn and skip scanning all compartments
                if foundIgw:
                    continue

                # if not found before - loop on all compartments
                for compartment in compartments:

                    igws = []
                    try:
                        igws = virtual_network.list_internet_gateways(
                            compartment['id'], vcn['id'],
                            lifecycle_state=oci.core.models.InternetGateway.LIFECYCLE_STATE_AVAILABLE
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    for igw in igws:
                        val = {'id': str(igw.id), 'vcn_id': str(igw.vcn_id), 'name': str(igw.display_name),
                               'time_created': str(igw.time_created), 'compartment_name': str(compartment['name']),
                               'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}
                        data.append(val)
                        foundIgw = True
                        cnt += 1

                    # if found in this compartments, continue to next vcn
                    if foundIgw:
                        break

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_igw", e)
            return data

    ##########################################################################
    # data network lpg
    ##########################################################################
    def __load_core_network_lpg(self, virtual_network, compartments, vcns):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Local Peer GWs")

            # loop on all vcns - vcn is must parameter
            for vcn in vcns:
                print("+", end="")

                # iLoop on all compartments
                for compartment in compartments:

                    local_peering_gateways = []
                    try:
                        local_peering_gateways = virtual_network.list_local_peering_gateways(
                            compartment['id'],
                            vcn['id']
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            # self.__load_print_auth_warning()
                            # don't print "a" access due to issue with local peering GW service issue
                            continue
                        raise

                    # lpg = oci.core.models.LocalPeeringGateway()
                    for lpg in local_peering_gateways:
                        if lpg.lifecycle_state != oci.core.models.LocalPeeringGateway.LIFECYCLE_STATE_AVAILABLE:
                            continue

                        # get the cidr block of the peering
                        cidr = "" if lpg.peer_advertised_cidr is None else " - " + str(lpg.peer_advertised_cidr)

                        # add lpg info to data
                        val = {'id': str(lpg.id), 'vcn_id': str(lpg.vcn_id),
                               'name': str(lpg.peering_status).ljust(8) + " - " + str(lpg.display_name) + str(cidr),
                               'time_created': str(lpg.time_created), 'route_table_id': str(lpg.route_table_id),
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'defined_tags': [] if lpg.defined_tags is None else lpg.defined_tags,
                               'freeform_tags': [] if lpg.freeform_tags is None else lpg.freeform_tags,
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_lpg", e)
            return data

    ##########################################################################
    # data network lpg
    ##########################################################################
    def __load_core_network_rpc(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Remote Peer Conns")

            # iLoop on all compartments
            for compartment in compartments:

                rpcs = []
                try:
                    rpcs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_remote_peering_connections,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # rpc = oci.core.models.RemotePeeringConnection()
                for rpc in rpcs:
                    if rpc.lifecycle_state != oci.core.models.RemotePeeringConnection.LIFECYCLE_STATE_AVAILABLE:
                        continue

                    val = {'id': str(rpc.id), 'peer_id': str(rpc.peer_id), 'drg_id': str(rpc.drg_id),
                           'name': str(rpc.display_name), 'time_created': str(rpc.time_created),
                           'is_cross_tenancy_peering': str(rpc.is_cross_tenancy_peering),
                           'peer_region_name': str(rpc.peer_region_name), 'peer_tenancy_id': str(rpc.peer_tenancy_id),
                           'peering_status': str(rpc.peering_status), 'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1
            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_rpc", e)
            return data

    ##########################################################################
    # data network read route
    ##########################################################################
    def __load_core_network_routet(self, virtual_network, compartments, vcns):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Route Tables")

            # loop on all vcns - vcn is must parameter
            for vcn in vcns:
                print("+", end="")

                # iLoop on all compartments
                for compartment in compartments:

                    route_tables = []
                    try:
                        route_tables = oci.pagination.list_call_get_all_results(
                            virtual_network.list_route_tables,
                            compartment['id'],
                            vcn['id'],
                            lifecycle_state=oci.core.models.RouteTable.LIFECYCLE_STATE_AVAILABLE).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # loop on the routes
                    # rt = oci.core.models.RouteTable()
                    for rt in route_tables:
                        val = {'id': str(rt.id), 'vcn_id': str(rt.vcn_id), 'name': str(rt.display_name),
                               'time_created': str(rt.time_created),
                               'route_rules': [{'destination': str(es.destination), 'network_entity_id': str(es.network_entity_id)} for es in rt.route_rules],
                               'compartment_name': str(compartment['name']),
                               'defined_tags': [] if rt.defined_tags is None else rt.defined_tags,
                               'freeform_tags': [] if rt.freeform_tags is None else rt.freeform_tags,
                               'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_route", e)
            return data

    ##########################################################################
    # get DHCP options for DHCP_ID
    ##########################################################################
    def __load_core_network_dhcpop_opt(self, dhcp_option):

        retstr = ""
        try:
            opt = dhcp_option

            # if type = oci.core.models.DhcpDnsOption
            if isinstance(opt, oci.core.models.DhcpDnsOption):
                retstr += str(opt.type).ljust(17) + ": " + str(opt.server_type)
                if len(opt.custom_dns_servers) > 0:
                    retstr += " - "
                    for ip in opt.custom_dns_servers:
                        retstr += str(ip) + "  "

            # if type = oci.core.models.DhcpSearchDomainOption
            if isinstance(opt, oci.core.models.DhcpSearchDomainOption):
                if len(opt.search_domain_names) > 0:
                    retstr += str(opt.type).ljust(17) + ": "
                    for ip in opt.search_domain_names:
                        retstr += str(ip) + "  "

            return retstr

        except Exception as e:
            self.__print_error("__load_core_network_dhcpop_opt", e)
            return retstr

    ##########################################################################
    # data network read dhcp options
    ##########################################################################
    def __load_core_network_dhcpop(self, virtual_network, compartments, vcns):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("DHCP Options")

            # loop on all vcns - vcn is must parameter
            for vcn in vcns:
                print("+", end="")

                # iLoop on all compartments
                for compartment in compartments:

                    dhcp_options = []
                    try:
                        dhcp_options = oci.pagination.list_call_get_all_results(
                            virtual_network.list_dhcp_options,
                            compartment['id'],
                            vcn['id'],
                            lifecycle_state=oci.core.models.DhcpOptions.LIFECYCLE_STATE_AVAILABLE).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # loop on the routes
                    # dhcp = oci.core.models.DhcpOptions()
                    for dhcp in dhcp_options:

                        # Analyzing DHCP Option
                        dhcp_opt = []
                        if dhcp.options is not None:
                            for opt in dhcp.options:
                                dhcp_opt.append(self.__load_core_network_dhcpop_opt(opt))

                        # add route info to data
                        val = {'id': str(dhcp.id), 'vcn_id': str(dhcp.vcn_id), 'name': str(dhcp.display_name),
                               'time_created': str(dhcp.time_created), 'options': dhcp_opt,
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'defined_tags': [] if dhcp.defined_tags is None else dhcp.defined_tags,
                               'freeform_tags': [] if dhcp.freeform_tags is None else dhcp.freeform_tags,
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_dhcpop", e)
            return data

    ##########################################################################
    # __load_core_network_port_range
    ##########################################################################
    def __load_core_network_seclst_rule_port_range(self, name, port_range):

        if port_range is None:
            return ""

        if port_range.min == port_range.max:
            return name + "(" + str(port_range.min) + ") "
        else:
            return name + "(" + str(port_range.min) + "-" + str(port_range.max) + ") "

    ##########################################################################
    # get Network vcn security rule
    ##########################################################################
    def __load_core_network_seclst_rule(self, security_rule):
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
            line += self.__load_core_network_seclst_rule_port_range("Src", security_rule.tcp_options.source_port_range)
            line += self.__load_core_network_seclst_rule_port_range("Dst", security_rule.tcp_options.destination_port_range)

        # udp options
        if security_rule.udp_options is not None:
            line += self.__load_core_network_seclst_rule_port_range("Src", security_rule.udp_options.source_port_range)
            line += self.__load_core_network_seclst_rule_port_range("Dst", security_rule.udp_options.destination_port_range)

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
    # data network read security list
    ##########################################################################
    def __load_core_network_seclst(self, virtual_network, compartments, vcns):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Security Lists")

            # loop on all vcns - vcn is must parameter
            for vcn in vcns:
                print("+", end="")

                # iLoop on all compartments
                for compartment in compartments:

                    sec_lists = []
                    try:
                        sec_lists = oci.pagination.list_call_get_all_results(
                            virtual_network.list_security_lists,
                            compartment['id'],
                            vcn['id'],
                            lifecycle_state=oci.core.models.SecurityList.LIFECYCLE_STATE_AVAILABLE,
                            sort_by="DISPLAYNAME").data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # loop on the sec lists
                    # sl = oci.core.models.SecurityList
                    for sl in sec_lists:

                        # Sec Rules analyzer
                        sec_rules = []

                        for sli in sl.ingress_security_rules:
                            sec_rules.append(
                                {'is_stateless': str(sli.is_stateless),
                                 'protocol': str(sli.protocol),
                                 'desc': "Ingres  : " + self.__load_core_network_seclst_rule(sli)})

                        for sle in sl.egress_security_rules:
                            sec_rules.append(
                                {'is_stateless': str(sle.is_stateless),
                                 'protocol': str(sle.protocol),
                                 'desc': "Egres   : " + self.__load_core_network_seclst_rule(sle)})

                        # Add info
                        val = {'id': str(sl.id), 'vcn_id': str(sl.vcn_id), 'name': str(sl.display_name),
                               'time_created': str(sl.time_created), 'sec_rules': sec_rules,
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'defined_tags': [] if sl.defined_tags is None else sl.defined_tags,
                               'freeform_tags': [] if sl.freeform_tags is None else sl.freeform_tags,
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_seclst", e)
            return data

    ##########################################################################
    # data network read subnets
    ##########################################################################
    def __load_core_network_subnet(self, virtual_network, compartments, vcns):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Subnets")

            # loop on all vcns - vcn is must parameter
            for vcn in vcns:
                print("+", end="")

                # iLoop on all compartments
                for compartment in compartments:

                    subnets = []
                    try:
                        subnets = oci.pagination.list_call_get_all_results(
                            virtual_network.list_subnets,
                            compartment['id'],
                            vcn['id'],
                            lifecycle_state=oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE,
                            sort_by="DISPLAYNAME").data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # loop on the subnet
                    # subnet = oci.core.models.Subnet.
                    for subnet in subnets:
                        availability_domain = (str(subnet.availability_domain) if str(subnet.availability_domain) != "None" else "Regional")
                        val = {'id': str(subnet.id), 'vcn_id': str(subnet.vcn_id), 'vcn_name': vcn['display_name'],
                               'name': str(subnet.display_name), 'cidr_block': str(subnet.cidr_block),
                               'subnet': (str(subnet.cidr_block) + "  " + availability_domain + (" (Private) " if subnet.prohibit_public_ip_on_vnic else " (Public)")),
                               'time_created': str(subnet.time_created),
                               'security_list_ids': [str(es) for es in subnet.security_list_ids],
                               'dhcp_options_id': str(subnet.dhcp_options_id),
                               'route_table_id': str(subnet.route_table_id), 'dns_label': str(subnet.dns_label),
                               'defined_tags': [] if subnet.defined_tags is None else subnet.defined_tags,
                               'freeform_tags': [] if subnet.freeform_tags is None else subnet.freeform_tags,
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_slist", e)
            return data

    ##########################################################################
    # data network read sgw
    ##########################################################################
    def __load_core_network_sgw(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Service Gateways")

            # loop on all compartments
            for compartment in compartments:

                sgws = []
                try:
                    sgws = oci.pagination.list_call_get_all_results(
                        virtual_network.list_service_gateways,
                        compartment['id'],
                        lifecycle_state=oci.core.models.ServiceGateway.LIFECYCLE_STATE_AVAILABLE
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on all sgws
                # sgw = oci.core.models.ServiceGateway
                for sgw in sgws:
                    val = {'id': str(sgw.id), 'vcn_id': str(sgw.vcn_id), 'name': str(sgw.display_name),
                           'time_created': str(sgw.time_created),
                           'services': str(', '.join(x.service_name for x in sgw.services)),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'defined_tags': [] if sgw.defined_tags is None else sgw.defined_tags,
                           'freeform_tags': [] if sgw.freeform_tags is None else sgw.freeform_tags,
                           'region_name': str(self.config['region'])}

                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_sgw", e)
            return data

    ##########################################################################
    # data network read sgw
    ##########################################################################
    def __load_core_network_nat(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("NAT Gateways")

            # loop on all compartments
            for compartment in compartments:
                # natgw will throw error if run on Paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                natgws = []
                try:
                    natgws = oci.pagination.list_call_get_all_results(
                        virtual_network.list_nat_gateways,
                        compartment['id'],
                        lifecycle_state=oci.core.models.NatGateway.LIFECYCLE_STATE_AVAILABLE
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on all sgws
                # nat = oci.core.models.NatGateway.
                for nat in natgws:
                    val = {'id': str(nat.id), 'vcn_id': str(nat.vcn_id), 'name': str(nat.display_name) + " - " + str(nat.nat_ip),
                           'time_created': str(nat.time_created),
                           'defined_tags': [] if nat.defined_tags is None else nat.defined_tags,
                           'freeform_tags': [] if nat.freeform_tags is None else nat.freeform_tags,
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}

                    if nat.block_traffic:
                        val['name'] += " - Blocked"
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_nat", e)
            return data

    ##########################################################################
    # data network read drg attachment
    ##########################################################################
    def __load_core_network_dra(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Dynamic Routing GW Attch")

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_drg_attachments,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.DrgAttachment
                for arr in arrs:
                    if arr.lifecycle_state == oci.core.models.DrgAttachment.LIFECYCLE_STATE_ATTACHED:
                        val = {'id': str(arr.id), 'vcn_id': str(arr.vcn_id), 'drg_id': str(arr.drg_id),
                               'time_created': str(arr.time_created), 'route_table_id': str(arr.route_table_id),
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_dra", e)
            return data

    ##########################################################################
    # data network read drg
    ##########################################################################
    def __load_core_network_drg(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Dynamic Routing GWs")

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_drgs,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.Drg
                for arr in arrs:
                    if arr.lifecycle_state == oci.core.models.Drg.LIFECYCLE_STATE_AVAILABLE:
                        val = {'id': str(arr.id), 'name': str(arr.display_name), 'time_created': str(arr.time_created),
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_drg", e)
            return data

    ##########################################################################
    # data network read cpes
    ##########################################################################
    def __load_core_network_cpe(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Customer Prem Equipments")

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_cpes,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.Cpe
                for arr in arrs:
                    val = {'id': str(arr.id), 'name': str(arr.display_name) + " - " + str(arr.ip_address),
                           'time_created': str(arr.time_created), 'compartment_name': str(compartment['name']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_cpe", e)
            return data

    ##########################################################################
    # query private ip
    ##########################################################################
    def __load_core_network_single_privateip(self, virtual_network, ip_id):

        try:
            arr = virtual_network.get_private_ip(ip_id).data

            if arr:
                return str(arr.ip_address) + " - " + str(arr.display_name)
            return ""

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                pass
            raise
        except Exception as e:
            self.__print_error("__get_core_network_privateip", e)
            return ""

    ##########################################################################
    # __load_core_network_privateip
    ##########################################################################
    def __load_core_network_privateip(self, virtual_network, routes):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Routed Private IPs")

            # loop on all routes with private ips
            for route in routes:
                for rl in route['route_rules']:
                    if 'privateip' not in rl['network_entity_id']:
                        continue

                    # get the list
                    arr = None
                    try:
                        arr = virtual_network.get_private_ip(rl['network_entity_id']).data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    print("-", end="")

                    if arr is None:
                        continue

                    val = {'id': str(arr.id), 'name': str(arr.ip_address) + " - " + str(arr.display_name),
                           'time_created': str(arr.time_created), 'availability_domain': str(arr.availability_domain),
                           'hostname_label': str(arr.hostname_label), 'is_primary': str(arr.is_primary),
                           'ip_address': str(arr.ip_address), 'subnet_id': str(arr.subnet_id),
                           'compartment_id': str(arr.compartment_id), 'vnic_id': str(arr.vnic_id),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_privateip", e)
            return data

    ##########################################################################
    # data network read fastconnect
    ##########################################################################
    def __load_core_network_vc(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Virtual Circuits")

            # loop on all compartments
            for compartment in compartments:
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_virtual_circuits,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.VirtualCircuit
                for arr in arrs:

                    # get the cross connect mapping
                    data_cc = []
                    for cc in arr.cross_connect_mappings:
                        data_cc.append({'customer_bgp_peering_ip': str(cc.customer_bgp_peering_ip),
                                        'oracle_bgp_peering_ip': str(cc.oracle_bgp_peering_ip), 'vlan': str(cc.vlan)})

                    val = {'id': str(arr.id), 'name': str(arr.display_name),
                           'bandwidth_shape_name': str(arr.bandwidth_shape_name),
                           'bgp_management': str(arr.bgp_management), 'bgp_session_state': str(arr.bgp_session_state),
                           'customer_bgp_asn': str(arr.customer_bgp_asn), 'drg_id': str(arr.gateway_id),
                           'lifecycle_state': str(arr.lifecycle_state), 'oracle_bgp_asn': str(arr.oracle_bgp_asn),
                           'provider_name': str(arr.provider_name),
                           'provider_service_name': str(arr.provider_service_name),
                           'provider_state': str(arr.provider_state), 'reference_comment': str(arr.reference_comment),
                           'service_type': str(arr.service_type), 'cross_connect_mappings': data_cc,
                           'type': str(arr.type), 'time_created': str(arr.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_vc", e)
            return data

    ##########################################################################
    # data network read ipsec
    ##########################################################################
    def __load_core_network_ips(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("IPSEC tunnels")

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_ip_sec_connections,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.IPSecConnection.
                for arr in arrs:
                    if arr.lifecycle_state == oci.core.models.IPSecConnection.LIFECYCLE_STATE_AVAILABLE:

                        # get tunnel info
                        data_tun = []
                        try:
                            ipss = virtual_network.get_ip_sec_connection_device_status(arr.id).data
                            for tunnel in ipss.tunnels:
                                data_tun.append(
                                    {'ip_address': str(tunnel.ip_address), 'status': str(tunnel.lifecycle_state),
                                     'status_date': tunnel.time_state_modified.strftime("%Y-%m-%d %H:%M")})
                        except Exception:
                            pass

                        val = {'id': str(arr.id), 'name': str(arr.display_name), 'drg_id': str(arr.drg_id),
                               'cpe_id': str(arr.cpe_id), 'time_created': str(arr.time_created),
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'region_name': str(self.config['region']),
                               'static_routes': [str(es) for es in arr.static_routes], 'tunnels': data_tun}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_network_ips", e)
            return data

    ##########################################################################
    # __load_core_compute_block_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.core.ComputeClient(config, **kwargs)
    # class oci.core.BlockstorageClient(config, **kwargs)
    # class oci.core.ComputeManagementClient(config, **kwargs)
    # class oci.core.VirtualNetworkClient(config, **kwargs)
    ##########################################################################
    def __load_core_compute_main(self):

        try:
            print("Compute...")

            # BlockstorageClient
            block_storage = oci.core.BlockstorageClient(self.config)
            if self.flags.proxy:
                block_storage.base_client.session.proxies = {'https': self.flags.proxy}

            # ComputeManagementClient
            compute_manage = oci.core.ComputeManagementClient(self.config)
            if self.flags.proxy:
                compute_manage.base_client.session.proxies = {'https': self.flags.proxy}

            # ComputeClient
            compute_client = oci.core.ComputeClient(self.config)
            if self.flags.proxy:
                compute_client.base_client.session.proxies = {'https': self.flags.proxy}

            # virtual_network - for vnics
            virtual_network = oci.core.VirtualNetworkClient(self.config)
            if self.flags.proxy:
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key to the network if not exists
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_INST)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_IMAGES)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_BOOT_VOL_ATTACH)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_VOLUME_ATTACH)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_VNIC_ATTACH)

            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_INST_CONFIG)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_INST_POOL)

            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOLGRP)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_BOOT)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_BOOTBACK)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOL)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOLBACK)

            # reference to compute
            compute = self.data[self.C_COMPUTE]
            block = self.data[self.C_BLOCK]

            # append the data
            compute[self.C_COMPUTE_INST] += self.__load_core_compute_instances(compute_client, compartments)
            compute[self.C_COMPUTE_IMAGES] += self.__load_core_compute_images(compute_client, compartments)
            compute[self.C_COMPUTE_BOOT_VOL_ATTACH] += self.__load_core_compute_boot_vol_attach(compute_client, compartments)
            compute[self.C_COMPUTE_VOLUME_ATTACH] += self.__load_core_compute_vol_attach(compute_client, compartments)
            compute[self.C_COMPUTE_VNIC_ATTACH] += self.__load_core_compute_vnic_attach(compute_client, virtual_network, compartments)
            compute[self.C_COMPUTE_INST_CONFIG] += self.__load_core_compute_inst_config(compute_client, compute_manage, block_storage, compartments)
            compute[self.C_COMPUTE_INST_POOL] += self.__load_core_compute_inst_pool(compute_manage, compartments)

            print("")
            print("Block Storage...")

            block[self.C_BLOCK_VOLGRP] += self.__load_core_block_volume_group(block_storage, compartments)
            block[self.C_BLOCK_BOOT] += self.__load_core_block_boot(block_storage, compartments)
            block[self.C_BLOCK_BOOTBACK] += self.__load_core_block_boot_backup(block_storage, compartments)
            block[self.C_BLOCK_VOL] += self.__load_core_block_volume(block_storage, compartments)
            block[self.C_BLOCK_VOLBACK] += self.__load_core_block_volume_backup(block_storage, compartments)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                print("")
                pass
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_main", e)

    ##########################################################################
    # data compute read instances
    ##########################################################################
    def __load_core_compute_instances(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Instances")

            # loop on all compartments
            for compartment in compartments:

                # read instances and console connections
                arrs = []
                consoles = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        compute.list_instances,
                        compartment['id'],
                        sort_by="DISPLAYNAME"
                    ).data

                    consoles = oci.pagination.list_call_get_all_results(
                        compute.list_instance_console_connections,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.Instance()
                for arr in arrs:
                    if (arr.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_TERMINATED or
                            arr.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_PROVISIONING or
                            arr.lifecycle_state == oci.core.models.Instance.LIFECYCLE_STATE_TERMINATING):
                        continue

                    # load data
                    val = {'id': str(arr.id), 'display_name': str(arr.display_name), 'shape': str(arr.shape),
                           'lifecycle_state': str(arr.lifecycle_state),
                           'availability_domain': str(arr.availability_domain), 'fault_domain': str(arr.fault_domain),
                           'time_created': str(arr.time_created),
                           'time_maintenance_reboot_due': str(arr.time_maintenance_reboot_due),
                           'image_id': str(arr.image_id), 'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region']),
                           'console_id': "", 'console': "", 'console_connection_string': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'console_vnc_connection_string': "", 'image': "Not Found"}

                    # check image name
                    try:
                        val['image'] = str(compute.get_image(arr.image_id).data.display_name)
                    except Exception:
                        pass

                    # check console connections enabled
                    for icc in consoles:
                        if str(icc.instance_id) == str(arr.id) and str(icc.lifecycle_state) == oci.core.models.InstanceConsoleConnection.LIFECYCLE_STATE_ACTIVE:
                            val['console_id'] = str(icc.id)
                            val['console'] = "Console Connection Active"
                            val['console_connection_string'] = icc.connection_string
                            val['console_vnc_connection_string'] = icc.vnc_connection_string

                    # add data to array

                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_instances", e)
            return data

    ##########################################################################
    # data compute read images
    ##########################################################################
    def __load_core_compute_images(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Images")

            # loop on all compartments
            for compartment in compartments:

                images = []
                try:
                    images = oci.pagination.list_call_get_all_results(
                        compute.list_images,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.Image.LIFECYCLE_STATE_AVAILABLE
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                # filter the array to only cutomer images
                arrs = [i for i in images if i.base_image_id is not None]
                print(".", end="")

                # loop on array
                # arr = oci.core.models.Image.
                for arr in arrs:
                    val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                           'base_image_id': str(arr.base_image_id),
                           'time_created': str(arr.time_created),
                           'operating_system': str(arr.operating_system),
                           'size_in_gbs': str(round(arr.size_in_mbs / 1024)),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'base_image_name': str(compute.get_image(arr.base_image_id).data.display_name)}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_images", e)
            return data

    ##########################################################################
    # data compute read images
    ##########################################################################
    def __load_core_compute_inst_config(self, compute, compute_manage, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Instance Configurations")

            # loop on all compartments
            for compartment in compartments:

                # cannot query ManagedCompartmentForPaaS
                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                configs = []
                try:
                    configs = oci.pagination.list_call_get_all_results(
                        compute_manage.list_instance_configurations,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # config = oci.core.models.InstanceConfigurationSummary
                for config in configs:
                    val = {'id': str(config.id), 'time_created': str(config.time_created),
                           'name': str(config.display_name), 'compute_shape': "", 'compute_source': "",
                           'compute_display_name': "", 'block_volumes': "", 'secondary_vnics': "",
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}

                    # get info on the instance details
                    # arr = oci.core.models.InstanceConfiguration
                    arr = compute_manage.get_instance_configuration(config.id).data

                    # instance_detail = oci.core.models.ComputeInstanceDetails
                    if arr.instance_details:
                        instance_detail = arr.instance_details

                        # if instance_detail is ComputeInstanceDetails
                        if isinstance(instance_detail, oci.core.models.ComputeInstanceDetails):

                            # launch Details
                            if instance_detail.launch_details:
                                launch_details = instance_detail.launch_details

                                # check if instance is InstanceConfigurationLaunchInstanceDetails
                                if isinstance(launch_details, oci.core.models.InstanceConfigurationLaunchInstanceDetails):

                                    val['compute_shape'] = str(launch_details.shape)
                                    val['compute_display_name'] = str(launch_details.display_name)
                                    if instance_detail.block_volumes:
                                        val['block_volumes'] = len(instance_detail.block_volumes)
                                    if instance_detail.secondary_vnics:
                                        val['secondary_vnics'] = len(instance_detail.secondary_vnics)

                                    # check source details type
                                    if launch_details.source_details:
                                        source_details = launch_details.source_details

                                        # if InstanceConfigurationInstanceSourceViaImageDetails
                                        if isinstance(source_details, oci.core.models.InstanceConfigurationInstanceSourceViaImageDetails):
                                            if source_details.image_id:
                                                try:
                                                    val['compute_source'] = "Image: " + str(compute.get_image(source_details.image_id).data.display_name)
                                                except oci.exceptions.ServiceError as e:
                                                    if self.__check_service_error(e.code):
                                                        val['compute_source'] = "Image"

                                        # if InstanceConfigurationInstanceSourceViaBootVolumeDetails
                                        if isinstance(source_details, oci.core.models.InstanceConfigurationInstanceSourceViaBootVolumeDetails):
                                            if source_details.boot_volume_id:
                                                try:
                                                    bootvol = block_storage.get_boot_volume(source_details.boot_volume_id)
                                                    if bootvol:
                                                        val['compute_source'] = "Boot Volume: " + bootvol['display_name']
                                                except oci.exceptions.ServiceError as e:
                                                    if self.__check_service_error(e.code):
                                                        val['compute_source'] = "Boot Volume"

                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_inst_config", e)
            return data

    ##########################################################################
    # data compute read images
    ##########################################################################
    def __load_core_compute_inst_pool(self, compute_manage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Instance Pools")

            # loop on all compartments
            for compartment in compartments:

                # cannot query ManagedCompartmentForPaaS
                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                pools = []
                try:
                    pools = oci.pagination.list_call_get_all_results(
                        compute_manage.list_instance_pools,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")
                # config = oci.core.models.InstancePoolSummary
                for config in pools:
                    val = {'id': str(config.id), 'time_created': str(config.time_created),
                           'display_name': str(config.display_name),
                           'availability_domains': str(', '.join(str(x) for x in config.availability_domains)),
                           'lifecycle_state': str(config.lifecycle_state), 'size': str(config.size),
                           'instance_configuration_id': str(config.instance_configuration_id),
                           'instance_configuration_name': "", 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    inst_config = self.search_unique_item(self.C_COMPUTE, self.C_COMPUTE_INST_CONFIG, 'id', str(config.instance_configuration_id))
                    if inst_config:
                        val['instance_configuration_name'] = inst_config['name'] + " - " + inst_config['compute_shape']

                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_inst_pool", e)
            return data

    ##########################################################################
    # data compute read boot volume attached
    ##########################################################################
    def __load_core_compute_boot_vol_attach(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Boot Volumes Attached")

            # loop on all compartments
            for compartment in compartments:
                print(".", end="")

                # loop on all ads
                ads = self.get_availability_domains(self.config['region'])

                for ad in ads:

                    arrs = []
                    try:
                        arrs = oci.pagination.list_call_get_all_results(
                            compute.list_boot_volume_attachments,
                            ad['name'],
                            compartment['id']
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # loop on array
                    # arr = oci.core.models.BootVolumeAttachment
                    for arr in arrs:
                        val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                               'boot_volume_id': str(arr.boot_volume_id), 'instance_id': str(arr.instance_id),
                               'lifecycle_state': str(arr.lifecycle_state), 'time_created': str(arr.time_created),
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_boot_vol_attach", e)
            return data

    ##########################################################################
    # data compute read volume attached
    ##########################################################################
    def __load_core_compute_vol_attach(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Volumes Attached")

            # loop on all compartments
            for compartment in compartments:
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        compute.list_volume_attachments,
                        compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.VolumeAttachment
                for arr in arrs:
                    val = {'id': str(arr.id), 'display_name': str(arr.display_name), 'volume_id': str(arr.volume_id),
                           'instance_id': str(arr.instance_id), 'lifecycle_state': str(arr.lifecycle_state),
                           'time_created': str(arr.time_created), 'attachment_type': str(arr.attachment_type),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_vol_attach", e)
            return data

    ##########################################################################
    # print Core Network Vnic
    ##########################################################################

    def __load_core_compute_vnic(self, virtual_network, vnic_id):
        try:
            if vnic_id is None:
                return ""

            # get the vnic
            vnic = virtual_network.get_vnic(vnic_id).data

            # search the subnet
            subnet_name = ""
            subnet = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_SUBNET, 'id', str(vnic.subnet_id))
            if subnet:
                subnet_name = (", Subnet (" + subnet['name'] + " " + subnet['cidr_block'] + "), VCN (" + subnet[
                    'vcn_name'] + ")")

            # check vnic information
            returnstr = (str(vnic.private_ip) + " (Prv)")
            if vnic.public_ip is not None:
                returnstr += ", " + str(vnic.public_ip) + " (Pub)"

            # if source dest
            if vnic.skip_source_dest_check:
                returnstr += " - Skip=Y"

            # if primary
            if vnic.is_primary:
                returnstr += " - Primary "

            # subnet
            returnstr += subnet_name
            return returnstr

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return ""
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_vnic", e)

    ##########################################################################
    # data compute read volume attached
    ##########################################################################
    def __load_core_compute_vnic_attach(self, compute, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Vnics Attached")

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(compute.list_vnic_attachments,
                                                                    compartment['id']).data
                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.VnicAttachment
                for arr in arrs:
                    if str(arr.lifecycle_state) != oci.core.models.VnicAttachment.LIFECYCLE_STATE_ATTACHED:
                        continue

                    val = {'id': str(arr.id), 'display_name': str(arr.display_name), 'vnic_id': str(arr.vnic_id),
                           'vnic_name': self.__load_core_compute_vnic(virtual_network, arr.vnic_id),
                           'instance_id': str(arr.instance_id), 'time_created': str(arr.time_created),
                           'nic_index': str(arr.nic_index), 'subnet_id': str(arr.subnet_id),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_vnic_attach", e)
            return data

    ##########################################################################
    # get volume backup policy
    ##########################################################################
    def __load_core_block_volume_backup_policy(self, block_storage, volume_id):

        try:
            backupstr = ""
            backup_policy_assignments = block_storage.get_volume_backup_policy_asset_assignment(volume_id).data

            if backup_policy_assignments:
                for backup_policy_assignment in backup_policy_assignments:
                    bp = block_storage.get_volume_backup_policy(backup_policy_assignment.policy_id).data
                    backupstr += bp.display_name + " "
            return backupstr

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code) or e.code == 'InvalidParameter' or e.code == 'TooManyRequests':
                return ""
            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_backup_policy", e)

    ##########################################################################
    # data compute read boot volume
    ##########################################################################
    def __load_core_block_boot(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Boot Volumes")

            # reference to volgroups
            volgroups = self.data[self.C_BLOCK][self.C_BLOCK_VOLGRP]

            # loop on all compartments
            for compartment in compartments:
                print(".", end="")

                # loop on all ads
                availability_domains = self.get_availability_domains(self.config['region'])
                for ad in availability_domains:

                    boot_volumes = []
                    try:
                        boot_volumes = oci.pagination.list_call_get_all_results(
                            block_storage.list_boot_volumes,
                            ad['name'],
                            compartment['id']
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # loop on array
                    # arr = oci.core.models.BootVolume.
                    for arr in boot_volumes:

                        val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                               'size_in_gbs': str(arr.size_in_gbs), 'time_created': str(arr.time_created),
                               'kms_key_id': str(arr.kms_key_id), 'volume_group_id': str(arr.volume_group_id),
                               'volume_group_name': "", 'availability_domain': str(arr.availability_domain),
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'region_name': str(self.config['region']),
                               'backup_policy': self.__load_core_block_volume_backup_policy(block_storage, str(arr.id)),
                               'lifecycle_state': str(arr.lifecycle_state)}

                        # find vol group name
                        for volgrp in volgroups:
                            if str(arr.volume_group_id) == volgrp['id']:
                                val['volume_group_name'] = volgrp['display_name']

                        # check boot volume backup policy
                        data.append(val)
                        cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_block_boot", e)
            return data

    ##########################################################################
    # data compute read block volume
    ##########################################################################
    def __load_core_block_volume(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Block Volumes")

            # reference to volgroups
            volgroups = self.data[self.C_BLOCK][self.C_BLOCK_VOLGRP]

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        block_storage.list_volumes, compartment['id'],
                        sort_by="DISPLAYNAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.Volume.
                for arr in arrs:

                    val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                           'size_in_gbs': str(arr.size_in_gbs), 'time_created': str(arr.time_created),
                           'kms_key_id': str(arr.kms_key_id), 'volume_group_id': str(arr.volume_group_id),
                           'volume_group_name': "", 'availability_domain': str(arr.availability_domain),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region']),
                           'backup_policy': self.__load_core_block_volume_backup_policy(block_storage, str(arr.id)),
                           'lifecycle_state': str(arr.lifecycle_state)}

                    # find vol group name
                    for volgrp in volgroups:
                        if str(arr.volume_group_id) == volgrp['id']:
                            val['volume_group_name'] = volgrp['display_name']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume", e)
            return data

    ##########################################################################
    # data compute read block volume group
    ##########################################################################
    def __load_core_block_volume_group(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Block Volume Groups")

            # loop on all compartments
            for compartment in compartments:

                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                # retrieve the data from oci
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        block_storage.list_volume_groups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.VolumeGroup.LIFECYCLE_STATE_AVAILABLE).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        print(".", end="")
                        # don't cound it as error, it is showing error on old tenancies
                        # self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.VolumeGroup.
                for arr in arrs:
                    val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                           'size_in_gbs': str(arr.size_in_gbs), 'time_created': str(arr.time_created),
                           'volume_ids': [str(a) for a in arr.volume_ids], 'compartment_name': str(compartment['name']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_group", e)
            return data

    ##########################################################################
    # data compute read boot volume backups
    ##########################################################################
    def __load_core_block_boot_backup(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Boot Volumes Backups")

            # loop on all compartments
            for compartment in compartments:

                boot_volume_backups = []
                try:
                    boot_volume_backups = oci.pagination.list_call_get_all_results(
                        block_storage.list_boot_volume_backups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.BootVolumeBackup.LIFECYCLE_STATE_AVAILABLE
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.core.models.BootVolumeBackup
                for arr in boot_volume_backups:
                    val = {'id': str(arr.id), 'boot_volume_id': str(arr.boot_volume_id), 'type': str(arr.type),
                           'source_type': str(arr.source_type), 'time_created': str(arr.time_created),
                           'display_name': str(arr.display_name), 'size_in_gbs': str(arr.size_in_gbs),
                           'unique_size_in_gbs': str(arr.unique_size_in_gbs),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region']), 'backup_name': "Not Found",
                           'backup_lifecycle_state': "", 'expiration_time': str(arr.expiration_time)}

                    # add the rest

                    if val['expiration_time'] == "None":
                        val['expiration_time'] = "Keep"

                    # get the backup name
                    backup_name_arr = self.search_unique_item(self.C_BLOCK, self.C_BLOCK_BOOT, 'id',
                                                              str(arr.boot_volume_id))
                    if backup_name_arr:
                        val['backup_name'] = backup_name_arr['display_name']
                        val['backup_lifecycle_state'] = backup_name_arr['lifecycle_state']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_block_boot_backup", e)
            return data

    ##########################################################################
    # data compute read block volume backups
    ##########################################################################
    def __load_core_block_volume_backup(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Block Volumes Backups")

            # loop on all compartments
            for compartment in compartments:

                volume_backups = []
                try:
                    volume_backups = oci.pagination.list_call_get_all_results(
                        block_storage.list_volume_backups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.VolumeBackup.LIFECYCLE_STATE_AVAILABLE).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                # loop on array
                # arr = oci.core.models.VolumeBackup
                for arr in volume_backups:

                    # add the rest
                    val = {'id': str(arr.id), 'volume_id': str(arr.volume_id), 'backup_name': "Not Found", 'type': str(arr.type),
                           'source_type': str(arr.source_type), 'time_created': str(arr.time_created), 'display_name': str(arr.display_name),
                           'size_in_gbs': str(arr.size_in_gbs), 'unique_size_in_gbs': str(arr.unique_size_in_gbs), 'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region']), 'backup_lifecycle_state': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'expiration_time': "Keep" if arr.expiration_time is None else str(arr.expiration_time)}

                    # get the backup name
                    backup_name_arr = self.search_unique_item(self.C_BLOCK, self.C_BLOCK_VOL, 'id', str(arr.volume_id))
                    if backup_name_arr:
                        val['backup_name'] = backup_name_arr['display_name']
                        val['backup_lifecycle_state'] = backup_name_arr['lifecycle_state']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_backup", e)
            return data

    ##########################################################################
    # __load_core_compute_block_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.load_balancer.LoadBalancerClient(config, **kwargs)
    #
    ##########################################################################
    def __load_load_balancer_main(self):

        try:
            print("Load Balancer...")

            # LoadBalancerClient
            load_balancer = oci.load_balancer.LoadBalancerClient(self.config)
            if self.flags.proxy:
                load_balancer.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key to the network if not exists
            self.__initialize_data_key(self.C_LB, self.C_LB_LOAD_BALANCERS)
            self.__initialize_data_key(self.C_LB, self.C_LB_BACKEND_SETS)

            # reference to compute
            lb = self.data[self.C_LB]

            # append the data
            lb[self.C_LB_LOAD_BALANCERS] += self.__load_load_balancers(load_balancer, compartments)
            lb[self.C_LB_BACKEND_SETS] += self.__load_load_balancer_backendset(load_balancer)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_load_balancer_main", e)

    ##########################################################################
    # data load load balancers
    ##########################################################################
    def __load_load_balancers(self, load_balancer, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Load Balancers")

            # loop on all compartments
            for compartment in compartments:

                load_balancers = []
                try:
                    load_balancers = oci.pagination.list_call_get_all_results(
                        load_balancer.list_load_balancers,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.load_balancer.models.LoadBalancer.LIFECYCLE_STATE_ACTIVE).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.load_balancer.models.LoadBalancer
                for arr in load_balancers:

                    # get LB health
                    status = ""
                    try:
                        status = load_balancer.get_load_balancer_health(arr.id).data.status
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            pass
                        else:
                            raise

                    # add the rest
                    val = {'id': str(arr.id), 'shape_name': str(arr.shape_name), 'display_name': str(arr.display_name), 'is_private': str(arr.is_private),
                           'status': str(status),
                           'ip_addresses': [(str(ip.ip_address) + " - " + ("Public" if ip.is_public else "Private")) for ip in arr.ip_addresses], 'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region']), 'subnet_ids': []}

                    # subnets
                    if arr.subnet_ids:
                        val['subnet_ids'] = [str(a) for a in arr.subnet_ids]

                    # listeners
                    datalis = []
                    for listener in arr.listeners:
                        lo = arr.listeners[listener]
                        value = {'id': str(listener), 'port': str(lo.port), 'protocol': str(lo.protocol),
                                 'default_backend_set_name': str(lo.default_backend_set_name), 'ssl_configuration': ""}

                        # check ssl config
                        if lo.ssl_configuration:
                            value['ssl_configuration'] = str(lo.ssl_configuration.certificate_name)

                        # path_route_set_name
                        value['path_route_set_name'] = []
                        if lo.path_route_set_name:
                            value['path_route_set_name'] = str(lo.path_route_set_name)

                        # rule_set_names
                        value['rule_set_names'] = []
                        if lo.rule_set_names:
                            value['rule_set_names'] = [str(a) for a in lo.rule_set_names]

                        # host names
                        value['hostname_names'] = []
                        if lo.hostname_names:
                            value['hostname_names'] = [str(a) for a in lo.hostname_names]

                        # add data
                        datalis.append(value)

                    val['listeners'] = datalis

                    # Path route set
                    datapath = []
                    for prs in arr.path_route_sets:
                        pro = arr.path_route_sets[prs]
                        datapath.append({'name': pro.name, 'path_routes': pro.path_routes})
                    val['path_route'] = datapath

                    # Hostnames
                    datahosts = []
                    for hostname in arr.hostnames:
                        ho = arr.hostnames[hostname]
                        datahosts.append(str(ho.name) + " - " + str(ho.hostname))
                    val['hostnames'] = datahosts

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_load_balancers", e)
            return data

    ##########################################################################
    # data compute read boot volume backups
    ##########################################################################
    def __load_load_balancer_backendset(self, load_balancer):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Backend Sets")

            # get the load balancers for this regions
            region_name = str(self.config['region'])
            load_balancers = self.search_multi_items(self.C_LB, self.C_LB_LOAD_BALANCERS, 'region_name', region_name)

            # loop on all load balancers
            for lb in load_balancers:
                load_balancer_id = lb['id']
                region_name = lb['region_name']

                # get backend set and status
                backend_sets = []
                try:
                    backend_sets = oci.pagination.list_call_get_all_results(
                        load_balancer.list_backend_sets,
                        load_balancer_id
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                # print next load balancer
                print("L", end="")

                # loop on backendsets
                # bs = oci.load_balancer.models.BackendSet
                for bs in backend_sets:

                    # get status
                    status = ""
                    try:
                        status = load_balancer.get_backend_set_health(load_balancer_id, bs.name).data.status
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            pass
                        raise

                    # check ssl config
                    ssl_details = ""
                    if bs.ssl_configuration is not None:
                        ssl_details = str(bs.ssl_configuration.certificate_name)

                    # copy load balancer info
                    dataval = {'load_balancer_id': load_balancer_id, 'compartment_name': lb['compartment_name'], 'compartment_id': lb['compartment_id'],
                               'region_name': lb['region_name'], 'name': str(bs.name), 'policy': str(bs.policy), 'ssl_configuration': ssl_details,
                               'status': str(status)}

                    ############################
                    # list of backends
                    ############################
                    databck = []
                    for backend in bs.backends:
                        bh_status = ""

                        # Check Status
                        try:
                            bh_status = load_balancer.get_backend_health(load_balancer_id, bs.name,
                                                                         backend.name).data.status
                        except oci.exceptions.ServiceError as e:
                            if self.__check_service_error(e.code):
                                pass
                            raise

                        # add details
                        bval = {'name': str(backend.name), 'status': str(bh_status),
                                'ip_address': str(backend.ip_address), 'port': str(backend.port),
                                'backup': str(backend.backup), 'drain': str(backend.drain),
                                'offline': str(backend.offline), 'weight': str(backend.weight)}
                        databck.append(bval)
                    dataval['backends'] = databck

                    # Health Checker
                    h = bs.health_checker
                    datahealth = {'protocol': str(h.protocol), 'interval_in_millis': str(h.interval_in_millis),
                                  'timeout_in_millis': str(h.timeout_in_millis), 'retries': str(h.retries),
                                  'port': str(h.port), 'return_code': str(h.return_code),
                                  'response_body_regex': str(h.response_body_regex), 'url_path': str(h.url_path)}
                    dataval['health_checker'] = datahealth

                    # session_persistence_configuration
                    dataval['session_persistence'] = ""
                    if bs.session_persistence_configuration is not None:
                        dataval['session_persistence'] = str(bs.session_persistence_configuration.cookie_name) + ", " + "disable_fallback=" + ("Y" if bs.session_persistence_configuration.disable_fallback else "N")

                    # ssl_configuration
                    dataval['ssl_cert'] = ""
                    if bs.ssl_configuration is not None:
                        dataval['ssl_cert'] = (str(bs.ssl_configuration.certificate_name) + ", VerifyPeer=" + ("Y" if bs.ssl_configuration.verify_peer_certificate else "N") + ", " + "VerifyDepth=" + str(bs.ssl_configuration.verify_depth))

                    # add data
                    data.append(dataval)

                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_load_balancer_backendset", e)
            return data

    ##########################################################################
    # __load_object_storage_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.object_storage.ObjectStorageClient(config, **kwargs)
    #
    ##########################################################################
    def __load_object_storage_main(self):

        try:
            print("Object Storage...")

            # LoadBalancerClient
            object_storage = oci.object_storage.ObjectStorageClient(self.config)
            if self.flags.proxy:
                object_storage.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_OS, self.C_OS_BUCKETS)

            # reference to object storage
            os = self.data[self.C_OS]

            # append the data
            os[self.C_OS_BUCKETS] += self.__load_object_storage_buckets(object_storage, compartments)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_object_storage_main", e)

    ##########################################################################
    # data load load balancers
    ##########################################################################
    def __load_object_storage_buckets(self, object_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Buckets")

            # loop on all compartments
            for compartment in compartments:

                buckets = []
                try:
                    namespace_name = object_storage.get_namespace().data
                    buckets = oci.pagination.list_call_get_all_results(
                        object_storage.list_buckets,
                        namespace_name, compartment['id']
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # loop on array
                # arr = oci.object_storage.models.BucketSummary
                for arr in buckets:
                    val = {'name': str(arr.name), 'time_created': str(arr.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region']), 'public_access_type': "", 'storage_tier': "",
                           'approximate_count': "", 'approximate_size': "", 'object_lifecycle': "",
                           'preauthenticated_requests': "", 'size_gb': ""}

                    ###############################
                    # get more info
                    ###############################
                    try:
                        bucket = object_storage.get_bucket(namespace_name, str(arr.name), fields=['approximateCount', 'approximateSize']).data

                        if bucket:
                            val['public_access_type'] = str(bucket.public_access_type)
                            val['storage_tier'] = str(bucket.storage_tier)
                            objcnt = bucket.approximate_count
                            size = bucket.approximate_size

                            # check if size if not empty
                            if objcnt is not None and size is not None:
                                val['approximate_count'] = str('{:9,.0f}'.format(objcnt))
                                val['approximate_size'] = str('{:9,.1f}'.format(round(size / 1024 / 1024 / 1024, 1)))
                                val['size_gb'] = str(round(size / 1024 / 1024 / 1024, 1))

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                        else:
                            raise

                    ###############################
                    # get object lifecycle
                    ###############################
                    lp = None
                    try:
                        lp = object_storage.get_object_lifecycle_policy(namespace_name, str(arr.name)).data
                    except oci.exceptions.ServiceError as e:
                        if e.code == "LifecyclePolicyNotFound":
                            pass
                        elif self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                        else:
                            raise

                    if lp:
                        for l in lp.items:
                            val['object_lifecycle'] += " , LifeCycle: " + str(l.name) + ", " + str(
                                l.action) + ", " + str(l.time_amount) + " " + str(l.time_unit)

                    ###############################
                    # get preauthenticated_requests
                    ###############################
                    pre = None
                    try:
                        pre = object_storage.list_preauthenticated_requests(namespace_name, str(arr.name)).data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                        else:
                            raise

                    if pre:
                        val['preauthenticated_requests'] = str(len(pre))

                    data.append(val)
                    cnt += 1

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_object_storage_buckets", e)
            return data

    ##########################################################################
    # __load_resource_management_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.resource_management.ResourceManagerClient(config, **kwargs)
    #
    ##########################################################################
    def __load_resource_management_main(self):

        try:
            print("Resource Management...")

            # LoadBalancerClient
            orm = oci.resource_manager.ResourceManagerClient(self.config)
            if self.flags.proxy:
                orm.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_ORM, self.C_ORM_STACKS)

            # reference to orm
            os = self.data[self.C_ORM]

            # append the data
            os[self.C_ORM_STACKS] += self.__load_resource_management_stacks(orm, compartments)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_resource_management_main", e)

    ##########################################################################
    # __load_resource_management_stacks
    ##########################################################################
    def __load_resource_management_stacks(self, orm, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Stacks")

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                stacks = []
                try:
                    stacks = oci.pagination.list_call_get_all_results(
                        orm.list_stacks, compartment_id=compartment['id'],
                        lifecycle_state=oci.resource_manager.models.Stack.LIFECYCLE_STATE_ACTIVE,
                        sort_by="DISPLAYNAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # query the stacks
                # stack = oci.resource_manager.models.Stack
                for stack in stacks:
                    val = {'id': str(stack.id), 'display_name': str(stack.display_name),
                           'description': str(stack.description), 'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region']),
                           'defined_tags': [] if stack.defined_tags is None else stack.defined_tags,
                           'freeform_tags': [] if stack.freeform_tags is None else stack.freeform_tags,
                           'time_created': str(stack.time_created)}

                    # check jobs
                    try:
                        jobs = oci.pagination.list_call_get_all_results(orm.list_jobs, stack_id=stack.id,
                                                                        sort_by="TIMECREATED").data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                        else:
                            raise

                    # query jobs
                    datajob = []
                    for job in jobs:
                        jobval = {'id': str(job.id), 'display_name': str(job.display_name),
                                  'operation': str(job.operation), 'lifecycle_state': str(job.lifecycle_state),
                                  'time_finished': str(job.time_finished), 'time_created': str(job.time_created)}
                        datajob.append(jobval)

                    # add the jobs to the array
                    val['jobs'] = datajob

                    # add the stacks
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_resource_management_stacks", e)
            return data

    ##########################################################################
    # __load_email_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.email.EmailClient(config, **kwargs)
    #
    ##########################################################################
    def __load_email_main(self):

        try:
            print("Email Notifications...")

            # EmailClient
            email_client = oci.email.EmailClient(self.config)
            if self.flags.proxy:
                email_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_EMAIL, self.C_EMAIL_SENDERS)
            self.__initialize_data_key(self.C_EMAIL, self.C_EMAIL_SUPPRESSIONS)

            # reference to orm
            email = self.data[self.C_EMAIL]

            # append the data
            email[self.C_EMAIL_SENDERS] += self.__load_email_senders(email_client, compartments)
            email[self.C_EMAIL_SUPPRESSIONS] += self.__load_email_suppressions(email_client, compartments)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_email_main", e)

    ##########################################################################
    # data load load __load_email_senders
    ##########################################################################
    def __load_email_senders(self, email, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Senders")

            # loop on all compartments
            for compartment in compartments:

                senders = []
                try:
                    senders = oci.pagination.list_call_get_all_results(
                        email.list_senders, compartment['id'],
                        sort_by="EMAILADDRESS"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # query the stacks
                # sender = oci.email.models.Sender
                for sender in senders:
                    val = {'id': str(sender.id), 'email_address': str(sender.email_address),
                           'lifecycle_state': str(sender.lifecycle_state), 'time_created': str(sender.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'defined_tags': [] if sender.defined_tags is None else sender.defined_tags,
                           'freeform_tags': [] if sender.freeform_tags is None else sender.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_email_senders", e)
            return data

    ##########################################################################
    # data load load __load_email_suppressions
    ##########################################################################
    def __load_email_suppressions(self, email, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Suppressions")

            # loop on all compartments
            for compartment in compartments:

                # suppressions is only valid in root compartment
                if compartment['id'] != str(self.config['tenancy']):
                    print(".", end="")
                    continue

                suppressions = []
                try:
                    suppressions = email.list_suppressions(compartment['id']).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # query the stacks
                # supp = oci.email.models.SuppressionSummary
                for supp in suppressions:
                    val = {'id': str(supp.id), 'email_address': str(supp.email_address),
                           'time_created': str(supp.time_created), 'reason': str(supp.reason),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_email_suppressions", e)
            return data

    ##########################################################################
    # __load_file_storage_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.file_storage.FileStorageClient(config, **kwargs)
    #
    ##########################################################################
    def __load_file_storage_main(self):

        try:
            print("File Storage...")

            # LoadBalancerClient
            file_storage = oci.file_storage.FileStorageClient(self.config)
            if self.flags.proxy:
                file_storage.base_client.session.proxies = {'https': self.flags.proxy}

            virtual_network = oci.core.VirtualNetworkClient(self.config)
            if self.flags.proxy:
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_FILE_STORAGE, self.C_FILE_STORAGE_FILESYSTEMS)
            self.__initialize_data_key(self.C_FILE_STORAGE, self.C_FILE_STORAGE_EXPORTS)
            self.__initialize_data_key(self.C_FILE_STORAGE, self.C_FILE_STORAGE_MOUNTS)

            # reference to orm
            fs = self.data[self.C_FILE_STORAGE]

            # append the data
            fs[self.C_FILE_STORAGE_FILESYSTEMS] += self.__load_file_storage_filesystems(file_storage, compartments)
            fs[self.C_FILE_STORAGE_EXPORTS] += self.__load_file_storage_exports(file_storage, compartments)
            fs[self.C_FILE_STORAGE_MOUNTS] += self.__load_file_storage_mount_targets(file_storage, virtual_network,
                                                                                     compartments)

            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_main", e)

    ##########################################################################
    # __load_file_storage_filesystems
    ##########################################################################
    def __load_file_storage_filesystems(self, file_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("File Systems")

            # get availability domains
            availability_domains = self.get_availability_domains(self.config['region'])

            # loop on all compartments
            for compartment in compartments:
                print(".", end="")

                for ad in availability_domains:

                    file_systems = []
                    try:
                        file_systems = oci.pagination.list_call_get_all_results(
                            file_storage.list_file_systems,
                            compartment['id'], ad['name'],
                            lifecycle_state=oci.file_storage.models.FileSystemSummary.LIFECYCLE_STATE_ACTIVE,
                            sort_by="DISPLAYNAME"
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # query the stacks
                    # fs = oci.file_storage.models.FileSystemSummary.
                    for fs in file_systems:
                        val = {'id': str(fs.id), 'display_name': str(fs.display_name),
                               'time_created': str(fs.time_created), 'availability_domain': str(fs.availability_domain),
                               'size_gb': str(round(int(fs.metered_bytes) / 1024 / 1024 / 1024, 1)),
                               'metered_bytes': str(fs.metered_bytes), 'snapshots': [],
                               'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}

                        # add snapshots to the file systems
                        try:
                            snapshots = oci.pagination.list_call_get_all_results(
                                file_storage.list_snapshots,
                                str(fs.id),
                                lifecycle_state=oci.file_storage.models.SnapshotSummary.LIFECYCLE_STATE_ACTIVE
                            ).data

                            for snap in snapshots:
                                sval = {'id': str(snap.id), 'name': str(snap.name), 'time_created': str(snap.time_created)}
                                val['snapshots'].append(sval)
                        except oci.exceptions.ServiceError as e:
                            if self.__check_service_error(e.code):
                                continue
                            else:
                                raise

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_filesystems", e)
            return data

    ##########################################################################
    # __load_file_storage_mount_targets
    ##########################################################################
    def __load_file_storage_mount_targets(self, file_storage, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Mount Targets")

            # loop on all compartments
            for compartment in compartments:
                print(".", end="")

                # get availability domains
                availability_domains = self.get_availability_domains(self.config['region'])
                for ad in availability_domains:

                    mount_targets = []
                    try:
                        mount_targets = oci.pagination.list_call_get_all_results(
                            file_storage.list_mount_targets,
                            compartment['id'], ad['name'],
                            lifecycle_state=oci.file_storage.models.MountTargetSummary.LIFECYCLE_STATE_ACTIVE,
                            sort_by="DISPLAYNAME").data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                            continue
                        raise

                    # query the stacks
                    # mt = oci.file_storage.models.MountTargetSummary
                    for mt in mount_targets:
                        val = {'id': str(mt.id), 'display_name': str(mt.display_name),
                               'export_set_id': str(mt.export_set_id), 'time_created': str(mt.time_created),
                               'availability_domain': str(mt.availability_domain), 'private_ip_ids': [],
                               'subnet_id': str(mt.subnet_id), 'compartment_name': str(compartment['name']),
                               'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}

                        # get private ips
                        for e in mt.private_ip_ids:
                            ip_address = self.__load_core_network_single_privateip(virtual_network, e)
                            val['private_ip_ids'].append(ip_address)

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_mount_targets", e)
            return data

    ##########################################################################
    # __load_file_storage_exports
    ##########################################################################
    def __load_file_storage_exports(self, file_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Exports")

            # loop on all compartments
            for compartment in compartments:
                print(".", end="")

                exports = []
                try:
                    exports = oci.pagination.list_call_get_all_results(
                        file_storage.list_exports,
                        compartment_id=compartment['id'],
                        lifecycle_state=oci.file_storage.models.ExportSummary.LIFECYCLE_STATE_ACTIVE,
                        sort_by="PATH"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                # query the export
                # es = oci.file_storage.models.ExportSummary
                for es in exports:
                    val = {'id': str(es.id), 'export_set_id': str(es.export_set_id),
                           'file_system_id': str(es.file_system_id), 'path': str(es.path),
                           'time_created': str(es.time_created), 'export_set': []}

                    # export set
                    try:
                        exp = file_storage.get_export_set(es.export_set_id).data
                        if exp:
                            valexp = {'id': str(exp.id), 'compartment_id': str(exp.compartment_id),
                                      'availability_domain': str(exp.availability_domain),
                                      'display_name': str(exp.display_name),
                                      'lifecycle_state': str(exp.lifecycle_state),
                                      'max_fs_stat_bytes': str(exp.max_fs_stat_bytes),
                                      'max_fs_stat_files': str(exp.max_fs_stat_files),
                                      'time_created': str(exp.time_created), 'vcn_id': str(exp.vcn_id)}
                            val['export_set'] = valexp

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            continue
                        else:
                            raise

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_exports", e)
            return data

    ##########################################################################
    # __load_database_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.database.DatabaseClient(config, **kwargs)
    # class oci.core.VirtualNetworkClient(config, **kwargs)
    #
    ##########################################################################
    def __load_database_main(self):

        try:
            print("Database...")

            # LoadBalancerClient
            database_client = oci.database.DatabaseClient(self.config)
            if self.flags.proxy:
                database_client.base_client.session.proxies = {'https': self.flags.proxy}

            virtual_network = oci.core.VirtualNetworkClient(self.config)
            if self.flags.proxy:
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_DBSYSTEMS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_AUTONOMOUS)

            # reference to orm
            db = self.data[self.C_DATABASE]

            # append the data
            db[self.C_DATABASE_DBSYSTEMS] += self.__load_database_dbsystems(database_client, virtual_network, compartments)
            db[self.C_DATABASE_AUTONOMOUS] += self.__load_database_autonomouns(database_client, compartments)

            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_database_main", e)

    ##########################################################################
    # __load_database_dbsystems
    ##########################################################################
    def __load_database_dbsystems(self, database_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("DB Systems")

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                print(".", end="")

                # list db system
                list_db_systems = []
                try:
                    list_db_systems = oci.pagination.list_call_get_all_results(
                        database_client.list_db_systems,
                        compartment['id'],
                        sort_by="DISPLAYNAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    else:
                        raise

                # loop on the db systems
                # dbs = oci.database.models.DbSystemSummary
                for dbs in list_db_systems:
                    if dbs.lifecycle_state == oci.database.models.DbSystemSummary.LIFECYCLE_STATE_TERMINATED:
                        continue

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'shape': str(dbs.shape),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'data_storage_size_in_gbs': "" if dbs.data_storage_size_in_gbs is None else str(dbs.data_storage_size_in_gbs),
                             'availability_domain': str(dbs.availability_domain),
                             'cpu_core_count': str(dbs.cpu_core_count),
                             'node_count': ("" if dbs.node_count is None else str(dbs.node_count)),
                             'version': str(dbs.version),
                             'hostname': str(dbs.hostname),
                             'domain': str(dbs.domain),
                             'data_storage_percentage': str(dbs.data_storage_percentage),
                             'data_subnet': self.get_network_subnet(str(dbs.subnet_id)),
                             'backup_subnet': "" if dbs.backup_subnet_id is None else self.get_network_subnet(str(dbs.backup_subnet_id)),
                             'scan_dns_record_id': "" if dbs.scan_dns_record_id is None else str(dbs.scan_dns_record_id),
                             'listener_port': str(dbs.listener_port),
                             'cluster_name': "" if dbs.cluster_name is None else str(dbs.cluster_name),
                             'database_edition': str(dbs.database_edition),
                             'compartment_name': str(compartment['name']),
                             'compartment_id': str(compartment['id']),
                             'time_created': str(dbs.time_created),
                             'region_name': str(self.config['region']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'patches': self.__load_database_dbsystems_patches(database_client, dbs.id),
                             'db_nodes': self.__load_database_dbsystems_dbnodes(database_client, virtual_network, dbs.id, compartment),
                             'db_homes': self.__load_database_dbsystems_dbhomes(database_client, virtual_network, dbs.id, compartment)}

                    # license model
                    if dbs.license_model == oci.database.models.DbSystem.LICENSE_MODEL_LICENSE_INCLUDED:
                        value['license_model'] = "INCL"
                    elif dbs.license_model == oci.database.models.DbSystem.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(dbs.license_model)

                    # Edition
                    if dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_ENTERPRISE_EDITION:
                        value['database_edition_short'] = "EE"
                    elif dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE:
                        value['database_edition_short'] = "XP"
                    elif dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE:
                        value['database_edition_short'] = "HP"
                    elif dbs.database_edition == oci.database.models.DbSystem.DATABASE_EDITION_STANDARD_EDITION:
                        value['database_edition_short'] = "SE"
                    else:
                        value['database_edition_short'] = dbs.database_edition

                    # scan IPs
                    value['scan_ips'] = []
                    if dbs.scan_ip_ids is not None:
                        scan_ips = []
                        for scan_ip in dbs.scan_ip_ids:
                            scan_ips.append(self.__load_core_network_single_privateip(virtual_network, scan_ip))
                        value['scan_ips'] = scan_ips

                    # VIPs
                    value['vip_ips'] = []
                    if dbs.vip_ids is not None:
                        vip_ips = []
                        for vipip in dbs.vip_ids:
                            vip_ips.append(self.__load_core_network_single_privateip(virtual_network, vipip))
                        value['vip_ips'] = vip_ips

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbnodes
    ##########################################################################
    def __load_database_dbsystems_dbnodes(self, database_client, virtual_network, dbs_id, compartment):

        data = []
        try:
            db_nodes = database_client.list_db_nodes(compartment['id'], dbs_id).data

            # db_node = oci.database.models.DbNodeSummary
            for db_node in db_nodes:
                data.append(
                    {'id': str(db_node.id),
                     'hostname': str(db_node.hostname),
                     'fault_domain': str(db_node.fault_domain),
                     'lifecycle_state': str(db_node.lifecycle_state),
                     'vnic_id': str(db_node.vnic_id),
                     'vnic_name': self.__load_core_compute_vnic(virtual_network, str(db_node.vnic_id)),
                     'software_storage_size_in_gb': str(db_node.software_storage_size_in_gb)})

            # add to main data
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_dbnodes", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbhomes
    ##########################################################################
    def __load_database_dbsystems_dbhomes(self, database_client, virtual_network, dbs_id, compartment):

        data = []
        try:
            db_homes = oci.pagination.list_call_get_all_results(database_client.list_db_homes, compartment['id'], dbs_id).data

            # db_home = oci.database.models.DbHomeSummary
            for db_home in db_homes:
                data.append(
                    {'id': str(db_home.id),
                     'display_name': str(db_home.display_name),
                     'compartment_id': str(db_home.compartment_id),
                     'last_patch_history_entry_id': str(db_home.last_patch_history_entry_id),
                     'lifecycle_state': str(db_home.lifecycle_state),
                     'db_system_id': str(db_home.db_system_id),
                     'db_version': str(db_home.db_version),
                     'time_created': str(db_home.time_created),
                     'databases': self.__load_database_dbsystems_dbhomes_databases(database_client, db_home.id, compartment),
                     'patches': self.__load_database_dbsystems_home_patches(database_client, db_home.id)})

            # add to main data
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning("h")
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_dbhomess", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbhomes_databases
    ##########################################################################

    def __load_database_dbsystems_dbhomes_databases(self, database_client, db_home_id, compartment):

        data = []
        try:
            dbs = oci.pagination.list_call_get_all_results(
                database_client.list_databases,
                compartment['id'],
                db_home_id,
                sort_by="DBNAME"
            ).data

            # db = oci.database.models.DatabaseSummary
            for db in dbs:
                if db.lifecycle_state == oci.database.models.DatabaseSummary.LIFECYCLE_STATE_TERMINATED:
                    continue

                value = {'id': str(db.id),
                         'compartment_id': str(db.compartment_id),
                         'character_set': str(db.character_set),
                         'ncharacter_set': str(db.ncharacter_set),
                         'db_home_id': str(db.db_home_id),
                         'db_name': str(db.db_name),
                         'pdb_name': "" if db.pdb_name is None else str(db.pdb_name),
                         'db_workload': str(db.db_workload),
                         'db_unique_name': str(db.db_unique_name),
                         'lifecycle_details': str(db.lifecycle_details),
                         'lifecycle_state': str(db.lifecycle_state),
                         'defined_tags': [] if db.defined_tags is None else db.defined_tags,
                         'freeform_tags': [] if db.freeform_tags is None else db.freeform_tags,
                         'time_created': str(db.time_created),
                         'auto_backup_enabled': False}

                if db.db_backup_config is not None:
                    if db.db_backup_config.auto_backup_enabled:
                        value['auto_backup_enabled'] = True

                value['backups'] = self.__load_database_dbsystems_db_backups(database_client, db.id)
                value['dataguard'] = self.__load_database_dbsystems_db_dg(database_client, db.id)
                data.append(value)

            # add to main data
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning("d")
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_dbhomes_databases", e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_home_patches(self, database_client, dbhome_id):

        data = []
        try:
            dbps = oci.pagination.list_call_get_all_results(database_client.list_db_home_patches, dbhome_id).data

            for dbp in dbps:
                data.append({'id': dbp.id, 'description': str(dbp.description), 'version': str(dbp.version), 'time_released': str(dbp.time_released),
                             'last_action': str(dbp.last_action)})
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_home_patches", e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_patches(self, database_client, dbs_id):

        data = []
        try:
            dbps = oci.pagination.list_call_get_all_results(database_client.list_db_system_patches, dbs_id).data

            for dbp in dbps:
                data.append({'id': dbp.id, 'description': str(dbp.description),
                             'version': str(dbp.version), 'time_released': str(dbp.time_released),
                             'last_action': str(dbp.last_action)})
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_patches", e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_db_backups(self, database_client, db_id):

        data = []
        try:
            backups = oci.pagination.list_call_get_all_results(database_client.list_backups, database_id=db_id).data

            for backup in backups:
                data.append(
                    {'id': str(backup.id),
                     'display_name': str(backup.display_name),
                     'type': str(backup.type),
                     'lifecycle_state': str(backup.lifecycle_state),
                     'time_started': str(backup.time_started),
                     'time_ended': str(backup.time_ended),
                     'database_size_in_gbs': "" if backup.database_size_in_gbs is None else str(backup.database_size_in_gbs)
                     })
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_patches", e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_db_dg(self, database_client, db_id):

        data = []
        try:
            dgs = oci.pagination.list_call_get_all_results(database_client.list_data_guard_associations, database_id=db_id).data

            # dg = oci.database.models.DataGuardAssociationSummary
            for dg in dgs:
                if dg.lifecycle_state == oci.database.models.DataGuardAssociationSummary.LIFECYCLE_STATE_TERMINATED or dg.lifecycle_state == oci.database.models.DataGuardAssociationSummary.LIFECYCLE_STATE_FAILED:
                    continue

                val = ({'id': str(dg.id),
                        'database_id': str(dg.database_id),
                        'db_name': "",
                        'role': str(dg.role),
                        'peer_role': str(dg.peer_role),
                        'lifecycle_state': str(dg.lifecycle_state),
                        'peer_database_id': str(dg.peer_database_id),
                        'peer_data_guard_association_id': str(dg.peer_data_guard_association_id),
                        'apply_rate': str(dg.apply_rate),
                        'apply_lag': str(dg.apply_lag),
                        'protection_mode': str(dg.protection_mode),
                        'transport_type': str(dg.transport_type),
                        'time_created': str(dg.time_created)})

                # get db name
                try:
                    database = database_client.get_database(dg.peer_database_id).data
                    dbsystem = database_client.get_db_system(dg.peer_db_system_id).data
                    if database and dbsystem:
                        val['db_name'] = str(dbsystem.display_name) + ":" + str(database.db_unique_name)
                except oci.exceptions.ServiceError as e:
                    if not self.__check_service_error(e.code):
                        raise

                # add the data
                data.append(val)

            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_db_dg", e)
            return data

    ##########################################################################
    # __load_database_autonomouns
    ##########################################################################
    def __load_database_autonomouns(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Autonomous Databases")

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    print(".", end="")
                    continue

                print(".", end="")

                list_autos = []
                try:
                    list_autos = oci.pagination.list_call_get_all_results(
                        database_client.list_autonomous_databases,
                        compartment['id'],
                        sort_by="DISPLAYNAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    else:
                        raise

                # loop on auto
                # dbs = oci.database.models.AutonomousDatabaseSummary
                for dbs in list_autos:
                    value = {}
                    if dbs.lifecycle_state == oci.database.models.AutonomousDatabaseSummary.LIFECYCLE_STATE_TERMINATED or dbs.lifecycle_state == oci.database.models.AutonomousDatabaseSummary.LIFECYCLE_STATE_UNAVAILABLE:
                        continue

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'data_storage_size_in_tbs': str(dbs.data_storage_size_in_tbs),
                             'db_name': str(dbs.db_name),
                             'cpu_core_count': str(dbs.cpu_core_count),
                             'sum_count': ("0" if dbs.lifecycle_state == oci.database.models.AutonomousDatabaseSummary.LIFECYCLE_STATE_STOPPED else str(dbs.cpu_core_count)),
                             'db_version': str(dbs.db_version),
                             'service_console_url': str(dbs.service_console_url),
                             'connection_strings': str(dbs.connection_strings),
                             'time_created': str(dbs.time_created),
                             'compartment_name': str(compartment['name']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'region_name': str(self.config['region']),
                             'backups': self.__load_database_autonomouns_backups(database_client, dbs.id)}

                    # license model
                    if dbs.license_model == oci.database.models.AutonomousDatabaseSummary.LICENSE_MODEL_LICENSE_INCLUDED:
                        value['license_model'] = "INCL"
                    elif dbs.license_model == oci.database.models.AutonomousDatabaseSummary.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(dbs.license_model)

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_autonomouns", e)
            return data

    ##########################################################################
    # __load_database_autonomouns_backups
    ##########################################################################
    def __load_database_autonomouns_backups(self, database_client, db_id):

        data = []
        try:
            backups = oci.pagination.list_call_get_all_results(
                database_client.list_autonomous_database_backups,
                autonomous_database_id=db_id,
                sort_by="TIMECREATED"
            ).data

            # backup = oci.database.models.AutonomousDatabaseBackupSummary
            for backup in backups:
                if backup.lifecycle_state == oci.database.models.AutonomousDatabaseBackupSummary.LIFECYCLE_STATE_DELETED:
                    continue

                data.append(
                    {'id': str(backup.id),
                     'display_name': str(backup.display_name),
                     'is_automatic': str(backup.is_automatic),
                     'type': str(backup.type),
                     'lifecycle_state': str(backup.lifecycle_state),
                     'lifecycle_details': str(backup.lifecycle_details),
                     'time_started': str(backup.time_started),
                     'time_ended': str(backup.time_ended)
                     })
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_database_autonomouns_backups", e)
            return data

    ##########################################################################
    # __load_container_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.container_engine.ContainerEngineClient(config, **kwargs)
    #
    ##########################################################################
    def __load_container_main(self):

        try:
            print("Containers...")

            # ContainerEngineClient
            container_client = oci.container_engine.ContainerEngineClient(self.config)
            if self.flags.proxy:
                container_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_CONTAINER, self.C_CONTAINER_CLUSTERS)
            self.__initialize_data_key(self.C_CONTAINER, self.C_CONTAINER_NODE_POOLS)

            # reference to orm
            cp = self.data[self.C_CONTAINER]

            # append the data
            cp[self.C_CONTAINER_CLUSTERS] += self.__load_container_clusters(container_client, compartments)
            cp[self.C_CONTAINER_NODE_POOLS] += self.__load_container_node_pools(container_client, compartments)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_container_main", e)

    ##########################################################################
    # __load_container_node_pools
    ##########################################################################
    def __load_container_node_pools(self, container_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Node Pools")

            # loop on all compartments
            for compartment in compartments:

                try:
                    list_clusters = oci.pagination.list_call_get_all_results(
                        container_client.list_node_pools, compartment['id'],
                        sort_by="NAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # arr = oci.container_engine.models.NodePoolSummary
                for arr in list_clusters:

                    val = {'id': str(arr.id),
                           'name': str(arr.name),
                           'cluster_id': str(arr.cluster_id),
                           'node_image_id': str(arr.node_image_id),
                           'kubernetes_version': str(arr.kubernetes_version),
                           'node_image_name': str(arr.node_image_name),
                           'node_shape': str(arr.node_shape),
                           'quantity_per_subnet': str(arr.quantity_per_subnet),
                           'subnet_ids': [subnets for subnets in arr.subnet_ids],
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_container_node_pools", e)
            return data

    ##########################################################################
    # __load_container_clusters
    ##########################################################################
    def __load_container_clusters(self, container_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            self.__load_print_status("Clusters")

            # loop on all compartments
            for compartment in compartments:

                try:
                    list_clusters = oci.pagination.list_call_get_all_results(
                        container_client.list_clusters, compartment['id'],
                        sort_by="NAME"
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # arr = oci.container_engine.models.ClusterSummary
                for arr in list_clusters:
                    if arr.lifecycle_state == oci.container_engine.models.ClusterSummary.LIFECYCLE_STATE_DELETED:
                        continue

                    val = {'id': str(arr.id), 'name': str(arr.name),
                           'lifecycle_state': str(arr.lifecycle_state),
                           'vcn_id': str(arr.vcn_id),
                           'kubernetes_version': str(arr.kubernetes_version),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_container_clusters", e)
            return data

    ##########################################################################
    # __load_streams_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.streaming.StreamAdminClient(config, **kwargs)
    #
    ##########################################################################
    def __load_streams_main(self):

        try:
            print("Streams...")

            # StreamAdminClient
            stream_client = oci.streaming.StreamAdminClient(self.config)
            if self.flags.proxy:
                stream_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_STREAMS, self.C_STREAMS_STREAMS)

            # reference to stream
            stream = self.data[self.C_STREAMS]

            # append the data
            stream[self.C_STREAMS_STREAMS] += self.__load_streams_streams(stream_client, compartments)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_streams_main", e)

    ##########################################################################
    # __load_streams_streams
    ##########################################################################
    def __load_streams_streams(self, stream_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            self.__load_print_status("Streams")

            # loop on all compartments
            for compartment in compartments:

                streams = []
                try:
                    streams = oci.pagination.list_call_get_all_results(
                        stream_client.list_streams, compartment['id'],
                        sort_by="NAME",
                        lifecycle_state=oci.streaming.models.StreamSummary.LIFECYCLE_STATE_ACTIVE
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                print(".", end="")

                # stream = oci.streaming.models.StreamSummary
                for stream in streams:
                    val = {'id': str(stream.id), 'name': str(stream.name),
                           'partitions': str(stream.partitions), 'time_created': str(stream.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'messages_endpoint': str(stream.messages_endpoint),
                           'defined_tags': [] if stream.defined_tags is None else stream.defined_tags,
                           'freeform_tags': [] if stream.freeform_tags is None else stream.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_cnt(cnt, start_time)
            return data

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_streams_streams", e)
            return data
