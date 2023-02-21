# showoci - Oracle Cloud Infrastructure Reporting Tool

## How To Manual

SHOWOCI is a reporting tool which uses the Python SDK to extract list of resources from your tenant. 
It covers most of OCI components, 
Authentication by User or Compute using instance principals, 
Output can be printer friendly, CSV files or JSON file.

**DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes, and rather OCI's official 
[cost analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm) 
and [usage reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm) features should be used instead.**

**Developed by Adi Zohar, 2018-2023**

## Content
[1. Step by Step installation Guide on OCI VM](#1-step-by-step-installation-guide-on-oci-vm)

[2. How to Upgrade or install showoci code](#2-how-to-upgrade-or-install-showoci-from-adi-zohar-github)

[3. How to Upgrade OCI SDK drivers](#3-how-to-upgrade-oci-sdk-drivers)


## 1. Step by Step installation Guide on OCI VM

### 1.1 Deploy VM Compute instance to run the python script
```
OCI -> Menu -> Compute -> Instances
Create Instance
--> Name = ShowOCIVM
--> Image = Oracle Linux 7
--> Shape = Any Shape
--> Choose your network VCN and Subnet (any type of VCN and Subnet)
--> Assign public IP -  Optional if on public subnet
--> Add your public SSH key
--> Press Create

Copy Instance Info:
--> Compute OCID to be used for Dynamic Group Permission
--> Compute IP
```

### 1.2. Create Dynamic Group for Instance Principles

```
OCI -> Menu -> Identity -> Dynamic Groups -> Create Dynamic Group
--> Name = ShowOCIDynamicGroup 
--> Desc = Dynamic Group for the showoci VM
--> Rule 1 = ANY { instance.id = 'OCID_Of_Step_1_Instance' }
```

### 1.3. Create Policy to allow the Dynamic Group to run showoci report

```
OCI -> Menu -> Identity -> Policies
Choose Root Compartment
Create Policy
--> Name = showociPolicy
--> Desc = Allow Dynamic Group ShowOCIDynamicGroup to extract tenant information using showoci
--> Statement = allow dynamic-group ShowOCIDynamicGroup to read all-resources in tenancy   
```

### 1.4. Login to Linux Machine

```
Using the SSH key you provided, SSH to the linux machine from step #1
ssh opc@UsageVM
```

### 1.5. Install Python 3, GIT and OCI packages

```
sudo yum install -y python3 git
sudo pip3 install --upgrade oci oci-cli oracledb
```

Test instance principle is working using oci-cli
```
oci os ns get --auth instance_principal
```

### 1.6. Clone the OCI SDK Repo from Git Hub or install using bash file

Clone from OCI SDK Repo and Create symbolink link

```
git clone https://github.com/oracle/oci-python-sdk
ln -s oci-python-sdk/examples/showoci .
```

Or Install using Bash

```
bash -c "$(curl -L https://raw.githubusercontent.com/adizohar/showoci/master/showoci_upgrade.sh)"    
```

### 1.7. Execute the python script - showoci.py

```
cd showoci
python3 showoci.py -ip -ani
```

## 2. How to upgrade or install showoci from Adi Zohar github

Run on OCI VM:
```
bash -c "$(curl -L https://raw.githubusercontent.com/adizohar/showoci/master/showoci_upgrade.sh)"    
```

## 3. How to upgrade OCI SDK drivers

```
python3 -m pip install --upgrade oci oci-cli oracledb pip
```

## License
```

Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl
or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
