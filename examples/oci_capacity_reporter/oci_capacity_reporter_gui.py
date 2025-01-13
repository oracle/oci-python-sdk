# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

###########################################################################################
# oci_capacity_reporter_gui.py
#
# @author: Derek T. Chambers-Boucher, May 21 2024
# @contributors: Adi Zohar
#
# Supports Python 3
###########################################################################################
# Info:
#
# A simple, tkinter-based UI using the OCI Python SDK that allows the user to
# inspect available shapes within their OCI tenant and generate available
# capacity reports based on the caller's OCI config definition and current limits
# see https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm) for more information.
#
###########################################################################################
# Application Command line parameters
#
#   -c config    - OCI CLI Config
#   -t profile   - profile inside the config file
#   -p proxy     - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip          - Use Instance Principals for Authentication
#
###########################################################################################
# Connectivity:
#    Using User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#       OCI user part of CapacityReporterGroup group with below Policy rules:
#          Allow group CapacityReporterGroup to inspect tenancies in tenancy
#          Allow group CapacityReporterGroup to inspect compartments in tenancy
#          Allow group CapacityReporterGroup to inspect instances in tenancy
#          Allow group CapacityReporterGroup to manage compute-capacity-reports in tenancy
###########################################################################################
# Modules Included:
# - oci.identity.IdentityClient
# - oci.core.ComputeClient
#
# APIs Used:
# - IdentityClient.get_tenancy               - Policy TENANCY_INSPECT
# - IdentityClient.list_region_subscriptions - Policy TENANCY_INSPECT
# - IdentityClient.list_availability_domains - Policy COMPARTMENT_INSPECT
# - ComputeClient.list_shapes - Policy INSTANCE_INSPECT
# - ComputeClient.create_compute_capacity_report - Policy COMPUTE_CAPACITY_REPORT_CREATE
###########################################################################################

import datetime
import argparse
import platform
import oci
import json
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import messagebox


##########################################################################
# class OCICapacityReporter
##########################################################################
class OCICapacityReporter(object):
    version = "24.05.21"

    # Class Screen Sizes
    TK_SHAPE_LIST_HEIGHT = 30
    TK_INFO_TEXT_WIDTH = 140

    # Class Parameters
    regions = []
    allShapes = []
    allADs = []
    config = {}
    signer = None
    proxy = None
    tenancy = None
    tenancy_id = ""
    tenancy_home_region = ""

    # Screen Components
    master = None
    regionVar = None
    adListBox = None
    shapeListBox = None
    infoTextBox = None
    tenantInfoTextBox = None

    ##########################################################################
    # init class
    # Creates a new data object
    ##########################################################################
    def __init__(self):
        pass

    ##########################################################################
    # main execution
    ##########################################################################
    def execute(self):
        self.main_input()
        self.getSubscribedRegions()
        self.main_ui_setup()
        self.setTenantInfoBox()
        self.master.mainloop()
        print("Good Bye.\n")

    ##########################################################################
    # Get the currently subscribed regions
    # Choosing an unsubscribed region will cause an Authentication Exception
    ##########################################################################
    def getSubscribedRegions(self):

        print("\nConnecting to Identity Service...\n")
        identity_client = oci.identity.IdentityClient(self.config, signer=self.signer)
        if self.proxy:
            identity_client.base_client.session.proxies = {'https': self.proxy}

        self.tenancy = identity_client.get_tenancy(self.tenancy_id).data
        regionList = identity_client.list_region_subscriptions(self.tenancy_id).data

        # Get Home Region
        for reg in regionList:
            if reg.is_home_region:
                self.tenancy_home_region = str(reg.region_name)

        print("Tenant Name  : " + str(self.tenancy.name))
        print("Tenant Id    : " + self.tenancy.id)
        print("Home Region  : " + self.tenancy_home_region)

        # Produce Region List
        self.regions = [r.region_name for r in regionList]
        self.regions.sort()
        print(f"\nLoaded {len(self.regions)} regions.")

    ##########################################################################
    # Get the selected region and set it in the OCI configuration
    ##########################################################################
    def get_region(self, *arg):
        selectedRegion = str(self.regionVar.get())
        self.change_region(selectedRegion)

    ##########################################################################
    # Simple error messaging
    ##########################################################################
    def error_handler(self, error):
        messagebox.showerror('Error', str(error), parent=self.master)
        print(str(error))

    ##########################################################################
    # Change selected region
    ##########################################################################
    def change_region(self, region):
        try:
            # Set Region
            self.config["region"] = region
            identity_client = oci.identity.IdentityClient(self.config, signer=self.signer)
            if self.proxy:
                identity_client.base_client.session.proxies = {'https': self.proxy}

            # Call list_availability_domains
            availability_domains = identity_client.list_availability_domains(compartment_id=self.tenancy_id).data
            availability_domains_names = [ad.name for ad in availability_domains]

            # Set ADs on Screen
            var = tk.Variable(value=availability_domains_names)
            self.adListBox.selection_clear(0, tk.END)
            self.shapeListBox.selection_clear(0, tk.END)
            self.adListBox.configure(listvariable=var)
            self.allADs = availability_domains_names
            self.get_shapes()
            print(f"Set region to '{region}' with {len(availability_domains_names)} ADs")

        except oci.exceptions.ServiceError as e:
            self.error_handler(e)
        except Exception as e:
            self.error_handler(e)

    ##########################################################################
    # Get shapes available in region for tenancy
    ##########################################################################
    def get_shapes(self, ad=None):
        try:
            core_client = oci.core.ComputeClient(self.config, signer=self.signer)
            if self.proxy:
                core_client.base_client.session.proxies = {'https': self.proxy}

            # Call list_shapes
            self.allShapes = core_client.list_shapes(compartment_id=self.tenancy_id, availability_domain=ad).data

            # Sort Unique the shapes
            listShapes = [s.shape for s in self.allShapes]
            UniqueShapes = list(set(listShapes))
            UniqueShapes.sort()
            var = tk.Variable(value=UniqueShapes)
            self.shapeListBox.configure(listvariable=var)
            print(f"Loaded {len(UniqueShapes)} shapes" + (f" for AD {ad}" if ad else ""))

        except Exception as e:
            self.error_handler(e)

    ##########################################################################
    # Extract the shape object details from the returned list
    ##########################################################################
    def get_shape_details(self, selShape):
        return list(filter(lambda x: x.shape == selShape, self.allShapes))[0]

    ##########################################################################
    # Set the text in the infoTextBox Widget
    ##########################################################################
    def setInfoTextBox(self, content=None):
        self.infoTextBox.configure(state='normal')
        self.infoTextBox.delete(1.0, tk.END)
        if content:
            self.infoTextBox.insert(tk.INSERT, str(content))
        self.infoTextBox.configure(state='disabled')

    ##########################################################################
    # Set the text in the Tenant Info
    ##########################################################################
    def setTenantInfoBox(self):
        val = "Tenant Name        : " + self.tenancy.name + "\n"
        val += "Tenant Id          : " + self.tenancy.id + "\n"
        val += "Home Region        : " + self.tenancy_home_region + "\n"
        val += "Subscribed Regions : " + ','.join(x for x in self.regions)
        self.tenantInfoTextBox.configure(state='normal')
        self.tenantInfoTextBox.insert(tk.INSERT, val)

    ##########################################################################
    # Get the selected shape details
    ##########################################################################
    def get_shape_info(self, displayShapeDetails=True):
        try:
            selShape = self.shapeListBox.get(self.shapeListBox.curselection())
            if displayShapeDetails:
                shape_details = self.get_shape_details(selShape)
                self.setInfoTextBox(shape_details)
            return selShape
        except Exception as e:
            self.error_handler(e)

    ##########################################################################
    # Generate the Capacity Report for the selected shape
    ##########################################################################
    def getCapacityReport(self):

        shape_details = self.get_shape_info(displayShapeDetails=False)
        shape = self.get_shape_details(shape_details)
        ocpus = None
        mem = None
        nvme = None

        print(f"Running capacity report for {str(shape.shape)}")

        reportstring = "Availability for Shape: " + str(shape.shape)
        flexreportstring = ""

        # Check if Flex Shape
        if 'Flex' in shape.shape:
            if "DenseIO" not in shape.shape:
                minOCPU = shape.ocpu_options.min
                maxOCPU = shape.ocpu_options.max
                maxShapeMem = shape.memory_options.max_in_g_bs
                minMemPerOCPU = shape.memory_options.min_per_ocpu_in_gbs
                maxMemPerOCPU = shape.memory_options.max_per_ocpu_in_gbs
            elif "DenseIO.E4" in shape.shape:
                minOCPU = 8
                maxOCPU = 32
                maxShapeMem = 512
                minMemPerOCPU = 16
                maxMemPerOCPU = 16
            elif "DenseIO.E5" in shape.shape:
                minOCPU = 8
                maxOCPU = 48
                maxShapeMem = 576
                minMemPerOCPU = 12
                maxMemPerOCPU = 12

            ocpuLabelText = "Number of OCPUs (" + str(minOCPU) + " - " + str(maxOCPU) + "):"

            ocpus = simpledialog.askinteger("Flex Shape Capacity Configuration", ocpuLabelText, parent=self.master, minvalue=minOCPU, maxvalue=maxOCPU)

            if ocpus:
                memCalc = maxMemPerOCPU * ocpus
                maxConfigMem = maxShapeMem if memCalc > maxShapeMem else (memCalc)
                minConfigMem = minMemPerOCPU * ocpus

                memLabelText = "Amount of Memory (" + str(minConfigMem) + " - " + str(maxConfigMem) + "):"
                mem = simpledialog.askinteger("Flex Shape Capacity Configuration", memLabelText, parent=self.master, minvalue=minConfigMem, maxvalue=maxConfigMem)
                if mem:
                    flexreportstring = " with " + str(ocpus) + " OCPU and " + str(mem) + " GB mem"
                else:
                    raise ValueError("Flex shapes require a configuration of ocpus and mem.")
            else:
                raise ValueError("Flex shapes require a configuration of ocpus and mem.")

        # DenseIO Flex shapes are another exceptional use case. There are specific,
        # fixed configurations that are acceptable.
        if ("DenseIO" in shape.shape) and ("Flex" in shape.shape):
            if "E4" in shape.shape:
                # E4 OCPU count can be 8, 16 or 32
                # and mem as 128, 256, 512 respectively
                # and an nvme drive for every 8 OCPUs
                factorE4 = ((ocpus - 1) // 8) + 1
                if factorE4 == 3:
                    # DenseIO.E4.Flex cannot have 24 OCPUs
                    factorE4 = 4
                ocpus = factorE4 * 8
                mem = factorE4 * 128
                nvme = factorE4
            elif "E5" in shape.shape:
                # E5 OCPU count can be 8, 16, 24, 32, 40, 48
                # and mem 96, 192, 288, 384, 480, 576 respectively
                # and an nvme drive for every 8 OCPUs
                factorE5 = ((ocpus - 1) // 8) + 1
                ocpus = factorE5 * 8
                mem = factorE5 * 96
                nvme = factorE5

            flexreportstring = " with " + str(ocpus) + " OCPU, " + str(mem) + " GB mem and " + str(nvme) + " NVME"

        reportstring += flexreportstring + "\n\n"

        # Get selected ADs
        report_time = ""
        is_data_available = False

        # Iterate through selected ADs and generate capacity report
        for a in self.allADs:
            report = self.getCapacityDetails(shape=shape.shape, ad=a, ocpu=ocpus, mem=mem, nvme=nvme)

            if report:
                is_data_available = True
                report_time = str(report.time_created)

                for sa in report.shape_availabilities:
                    fd = str(sa.fault_domain)
                    status = str(sa.availability_status)
                    if sa.available_count:
                        reportstring += str('{:>14}'.format(sa.available_count)) + " available"
                    else:
                        reportstring += "  " + status.rjust(22)

                    reportstring += " in "
                    reportstring += report.availability_domain + ":"
                    reportstring += (fd if fd != "None" else "ACROSS ALL FAULT DOMAINS") + "\n"

                reportstring += "\n"

        # Display capacity report in infoTextBox
        if is_data_available:
            reportstring += "Time created: " + report_time[0:16] + "\n"
            self.setInfoTextBox(reportstring)

    ##########################################################################
    # Get Capacity Report
    ##########################################################################
    def getCapacityDetails(self, shape, ad, ocpu=None, mem=None, nvme=None):

        # Send the request to service, some parameters are not required, see API doc for more info
        try:
            shapeConfig = None
            if (ocpu and mem and nvme):
                print(f"Running Capacity Report {ad} on {shape} with {str(ocpu)} OCPUs, {str(mem)} Memory and {str(nvme)} NVME")
                shapeConfig = oci.core.models.CapacityReportInstanceShapeConfig(ocpus=float(ocpu), memory_in_gbs=float(mem), nvmes=float(nvme))

            elif (ocpu and mem):
                print(f"Running Capacity Report {ad} on {shape} with {str(ocpu)} OCPUs, {str(mem)} Memory")
                shapeConfig = oci.core.models.CapacityReportInstanceShapeConfig(ocpus=float(ocpu), memory_in_gbs=float(mem))

            core_client = oci.core.ComputeClient(self.config, signer=self.signer)
            if self.proxy:
                core_client.base_client.session.proxies = {'https': self.proxy}

            # Create create_compute_capacity_report_details Object
            create_compute_capacity_report_details = oci.core.models.CreateComputeCapacityReportDetails(
                compartment_id=self.tenancy_id,
                availability_domain=ad,
                shape_availabilities=[
                    oci.core.models.CreateCapacityReportShapeAvailabilityDetails(
                        instance_shape=shape,
                        instance_shape_config=shapeConfig
                    ),
                    oci.core.models.CreateCapacityReportShapeAvailabilityDetails(
                        instance_shape=shape,
                        fault_domain="FAULT-DOMAIN-1",
                        instance_shape_config=shapeConfig
                    ),
                    oci.core.models.CreateCapacityReportShapeAvailabilityDetails(
                        instance_shape=shape,
                        fault_domain="FAULT-DOMAIN-2",
                        instance_shape_config=shapeConfig
                    ),
                    oci.core.models.CreateCapacityReportShapeAvailabilityDetails(
                        instance_shape=shape,
                        fault_domain="FAULT-DOMAIN-3",
                        instance_shape_config=shapeConfig
                    )
                ])

            # run report
            create_compute_capacity_report_response = core_client.create_compute_capacity_report(
                create_compute_capacity_report_details
            ).data

            return create_compute_capacity_report_response

        except oci.exceptions.ServiceError as e:
            self.setInfoTextBox(json.dumps(e.message, indent='3'))
            print(json.dumps(e.message, indent='3'))

    ##########################################################################
    # on Get Capacity Button
    ##########################################################################
    def on_get_capacity(self):
        try:
            self.getCapacityReport()
        except ValueError as e:
            self.error_handler(e)

    ##########################################################################
    # on AD selection get shapes
    ##########################################################################
    def onADSelect(self, eventAD):
        try:
            w = eventAD.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            self.shapeListBox.selection_clear(0, tk.END)
            self.setInfoTextBox("Please select shape to continue.")
        except IndexError:
            value = None
        finally:
            self.get_shapes(value)

    ##########################################################################
    # on Shape selection get shape details
    ##########################################################################
    def onShapeSelect(self, eventShape):
        self.get_shape_info(displayShapeDetails=True)

    ##########################################################################
    # Create signer for Authentication
    # Input - config_profile and is_instance_principals
    # Output - config and signer objects
    ##########################################################################
    def create_signer(self, config_file, config_profile, is_instance_principals, is_security_token):

        # if instance principals authentications
        if is_instance_principals:
            try:
                signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
                config = {'region': signer.region, 'tenancy': signer.tenancy_id}
                return config, signer

            except Exception:
                self.print_header("Error obtaining instance principals certificate, aborting", 0)
                raise SystemExit

        elif is_security_token:
            try:
                # create signer from config and security token
                config = oci.config.from_file(
                    (config_file if config_file else oci.config.DEFAULT_LOCATION),
                    (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
                )
                security_token_file = config.get("security_token_file")
                token = None
                with open(security_token_file, 'r') as f:
                    token = f.read()
                private_key = oci.signer.load_private_key_from_file(config['key_file'])
                signer = oci.auth.signers.SecurityTokenSigner(token, private_key)
                return config, signer

            except Exception as e:
                print("*********************************************************************")
                print("* Error Authenticating using config file and Security Token         *")
                print("* " + str(e))
                print("* Aborting.                                                         *")
                print("*********************************************************************")
                print('')
                raise SystemExit

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
    # Print header centered
    ##########################################################################
    def print_header(self, name, category):
        options = {0: 120, 1: 100, 2: 90, 3: 85}
        chars = int(options[category])
        print("")
        print('#' * chars)
        print("#" + name.center(chars - 2, " ") + "#")
        print('#' * chars)

    ##########################################################################
    # Main Input
    ##########################################################################
    def main_input(self):
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS, formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=150))
        parser.add_argument('-c', default="", dest='config_file', help='OCI CLI Config file')
        parser.add_argument('-t', default="", dest='config_profile', help='Config Profile inside the config file')
        parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
        parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
        parser.add_argument('-is', action='store_true', default=False, dest='is_security_token', help='Use Config and Security Token')
        cmd = parser.parse_args()

        # Start print time info
        self.print_header("OCI Capacity Reporter", 0)

        print("Author          : Derek T. Chambers-Boucher")
        print("Contributer     : Adi Zohar")
        print("Disclaimer      : This is not an official Oracle application,  It does not supported by Oracle, It should NOT be used for utilization calculation purposes !")
        print("Machine         : " + platform.node() + " (" + platform.machine() + ")")
        print("App Version     : " + self.version)
        print("OCI SDK Version : " + oci.version.__version__)
        print("Python Version  : " + platform.python_version())
        print("Authentication  : Config File")
        print("Date/Time       : " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print("Command Line    : " + ' '.join(x for x in sys.argv[1:]))

        self.proxy = cmd.proxy
        self.config, self.signer = self.create_signer(cmd.config_file, cmd.config_profile, cmd.is_instance_principals, cmd.is_security_token)
        self.tenancy_id = self.config["tenancy"]

    ##########################################################################
    # Main UI
    ##########################################################################
    def main_ui_setup(self):

        print("Initiating GUI...\n")

        # creating main tkinter window/toplevel
        self.master = tk.Tk()
        self.master.title('OCI Capacity Reporter')

        # create the region combobox
        self.listADs = tk.Variable()
        self.listShapes = tk.Variable()
        self.regionVar = tk.StringVar()

        # this will create a label widget
        l1 = tk.Label(self.master, text="Region:")
        l2 = tk.Label(self.master, text="ADs:")
        l3 = tk.Label(self.master, text="Shapes:")
        l4 = tk.Label(self.master, text="Tenant Info:")
        l5 = tk.Label(self.master, text="Shape / Capacity Info:")

        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.grid(row=0, column=0, sticky='w', pady=2)
        l2.grid(row=2, column=0, sticky='w', pady=2)
        l3.grid(row=4, column=0, sticky='w', pady=2)
        l4.grid(row=0, column=1, sticky='w', pady=2)
        l5.grid(row=4, column=1, sticky='w', pady=2)

        # region widget
        self.regionChooser = ttk.Combobox(self.master, width=18, textvariable=self.regionVar)
        self.regionChooser['values'] = self.regions
        self.regionChooser['state'] = 'readonly'
        self.regionVar.trace_add('write', self.get_region)

        # entry widgets:
        self.adListBox = tk.Listbox(self.master, listvariable=self.listADs, height=3, bd=1, selectmode='single')
        self.adListBox.configure(exportselection=False)
        self.shapeListBox = tk.Listbox(self.master, listvariable=self.listShapes, bd=1, height=self.TK_SHAPE_LIST_HEIGHT, yscrollcommand=True)
        self.shapeListBox.configure(exportselection=False)
        self.infoTextBox = scrolledtext.ScrolledText(self.master, width=self.TK_INFO_TEXT_WIDTH, bd=2, relief=tk.RAISED)
        self.tenantInfoTextBox = scrolledtext.ScrolledText(self.master, height=2, width=self.TK_INFO_TEXT_WIDTH, bd=2, relief=tk.RAISED)

        # this will arrange entry widgets
        self.regionChooser.grid(row=1, column=0, sticky='w')
        self.adListBox.grid(row=3, column=0, sticky='w', pady=2, padx=2)
        self.shapeListBox.grid(row=5, column=0, sticky='nw', pady=2, padx=2)
        self.infoTextBox.grid(row=5, column=1, sticky='nsew', pady=2, padx=2, rowspan=3, columnspan=20)
        self.tenantInfoTextBox.grid(row=1, column=1, sticky='nsew', pady=2, padx=2, rowspan=3, columnspan=20)

        # bind actions to widgets and buttons
        ttk.Button(self.master, text='Get Shape Info', command=self.get_shape_info).grid(row=8, column=0, pady=2, padx=2)
        ttk.Button(self.master, text='Get Capacity Report', command=self.on_get_capacity).grid(row=8, column=1, pady=2, padx=2)
        ttk.Button(self.master, text='Exit', command=self.master.destroy).grid(row=8, column=2, pady=2, padx=2)
        self.adListBox.bind('<<ListboxSelect>>', self.onADSelect)
        self.shapeListBox.bind('<<ListboxSelect>>', self.onShapeSelect)

        self.regionChooser.set(self.config["region"])
        self.master.eval('tk::PlaceWindow . center')

        self.setInfoTextBox("Please choose Availability Domain or Change Region to continue.")


##########################################################################
# Main
##########################################################################
cls = OCICapacityReporter()
cls.execute()
