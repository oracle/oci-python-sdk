## List Resources in Tenancy

Several utilities to help with producing reports from OCI

**DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes

**Developed by Adi Zohar, 2021**

## Executing using Cloud Shell:
```
    1. install oci sdk package
       pip3 install --user oci

    2. clone the oci sdk repo
       git clone https://github.com/oracle/oci-python-sdk

    3. Execute
       cd $HOME/oci-python-sdk/examples/list_resources_in_tenancy
       python3 list_all_ipsec_tunnels_in_tenancy.py -dt
       python3 list_all_virtual_circuits_in_tenancy.py -dt
       python3 list_compute_tags_in_tenancy.py -dt
       python3 list_dbsystem_with_maintenance_in_tenancy.py -dt
       python3 list_bv_backups_in_tenancy.py -dt
       python3 list_limits_per_compartments.py -dt

    4. Help with --help
```

## list_all_ipsec_tunnels_in_tenancy.py
Produce list of all ipsec tunnels in tenancy  - Useful when OCI published maintenance announcement of network components

```
usage: list_all_ipsec_tunnels_in_tenancy.py [-h] [-t CONFIG_PROFILE]
                                            [-p PROXY] [-ip] [-dt]

optional arguments:
  -h, --help         show this help message and exit
  -t CONFIG_PROFILE  Config file section to use (tenancy profile)
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
```

## list_all_virtual_circuits_in_tenancy.py 
Produce list of all Virtual Circuits (fastconnects) in tenancy - Useful when OCI published maintenance announcement of network components

```
usage: list_all_virtual_circuits_in_tenancy.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip] [-dt]

optional arguments:
  -h, --help         show this help message and exit
  -t CONFIG_PROFILE  Config file section to use (tenancy profile)
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
```

## list_bv_backups_in_tenancy.py
Produce list of all Boot and Block volume backups – Useful to produce backup list for Audit purposes

```
usage: list_bv_backups_in_tenancy.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip] [-dt]

optional arguments:
  -h, --help         show this help message and exit
  -t CONFIG_PROFILE  Config file section to use (tenancy profile)
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication

```

## list_compute_tags_in_tenancy.py
Produce list of compute with tags

```
usage: list_compute_tags_in_tenancy.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip] [-dt]

optional arguments:
  -h, --help         show this help message and exit
  -t CONFIG_PROFILE  Config file section to use (tenancy profile)
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
```

## list_dbsystem_with_maintenance_in_tenancy.py
Produce list of DB System and Exadata with maintenance details – Useful to alert when maintenance is due on the corresponding DB System or Exadata Infrastructure

```
usage: list_dbsystem_with_maintenance_in_tenancy.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip] [-dt]

optional arguments:
  -h, --help         show this help message and exit
  -t CONFIG_PROFILE  Config file section to use (tenancy profile)
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
```

## list_limits_per_compartments.py
Produce list of limits per compartment, can be extracted to screen or CSV and allow admin to monitor limits efficiency and request additional limits if required.

```
usage: list_limits_per_compartments.py [-h] [-c CONFIG_FILE]
                                       [-t CONFIG_PROFILE] [-p PROXY]
                                       [-rg FILTER_REGION] [-cp FILTER_COMP]
                                       [-sr FILTER_SERVICE] [-sc FILTER_SCOPE]
                                       [-ip] [-dt] [-js] [-csv CSV]

optional arguments:
  -h, --help          show this help message and exit
  -c CONFIG_FILE      OCI CLI Config file
  -t CONFIG_PROFILE   Config Profile inside the config file
  -p PROXY            Set Proxy (i.e. www-proxy-server.com:80)
  -rg FILTER_REGION   filter by region (i.e. us-ashburn-1)
  -cp FILTER_COMP     filter by compartment (i.e. production)
  -sr FILTER_SERVICE  filter by service (i.e. compute)
  -sc FILTER_SCOPE    filter by scope (i.e. AD,REGION,GLOBAL)
  -ip                 Use Instance Principals for Authentication
  -dt                 Use Delegation Token for Authentication
  -js                 print in JSON format
  -csv CSV            Output to CSV files, Input as file header

```