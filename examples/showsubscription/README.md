## SHOWSUBSCRIPTION - Oracle Cloud Infrastructure subscruption reporting

SHOWSUBSCRIPTION is a subscription reporting tool which uses the Python SDK to extract tenant subscription and commit.
Authentication by User or Compute using instance principals,

**DISCLAIMER - This is not an official Oracle application,  It does not supported by Oracle Support.

**Developed by Adi Zohar, 2021-2024**

## Modules Included:
- oci.onesubscription.OrganizationSubscriptionClient
- oci.onesubscription.CommitmentClient
- oci.onesubscription.SubscribedServiceClient

## Executing using Cloud Shell:
```
1. install oci sdk package
   pip3 install --user oci

2. clone the oci sdk repo
   git clone https://github.com/oracle/oci-python-sdk

3. run showsubscription.py with delegation token
   cd oci-python-sdk/examples/showsubscription
   python3 showsubscription.py -dt
```

## Installation of Python 3 incase you don't have Python3 installed:
Please follow [Python Documentation](https://docs.python.org/3/using/index.html)

## Install OCI SDK Packages:
Please follow [Oracle Python SDK Documentation](https://github.com/oracle/oci-python-sdk)

## Setup connectivity using Instance Principals

```
1. Login to your OCI Cloud console

2. Create new Dynamic Group : DynShowSubscriptionGroup  
   Obtain Compute OCID and add rule - any {ALL {instance.id = 'ocid1.instance.oc1.xxxxxxxxxx'}}

3. Create new Policy: DynShowSubscriptionGroupPolicy with Statements:
   Allow dynamic group DynShowSubscriptionGroup to inspect tenancies in tenancy
   Allow dynamic group DynShowSubscriptionGroup to inspect subscribed-services in tenancy
   Allow dynamic group DynShowSubscriptionGroup to inspect organizations-subscription in tenancy
```

## Setup connectivity using User

```  
1. Login to your OCI Cloud console

2. Create new group : ShowSubscriptionGroup  

3. Create new Policy: ShowSubscriptionGroupPolicy with Statements:
   Allow group ShowSubscriptionGroup to inspect tenancies in tenancy
   Allow group ShowSubscriptionGroup to inspect subscribed-services in tenancy
   Allow group ShowSubscriptionGroup to inspect organizations-subscription in tenancy

4. Create new User  : showsubscription.user -> Add to ShowSubscriptionGroup group  

5. Config OCI config file - ~/.oci/config
   Please follow SDK config documentation - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm 
```

## Copy the Software
Download the showsubscription.py from this project  

Execute  

```
$ python3 showsubscription.py  

optional arguments:
  -h, --help         show this help message and exit
  -c CONFIG_FILE     OCI CLI Config file
  -t CONFIG_PROFILE  Config Profile inside the config file
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
  -all_services      All Services (Default Universal Credit)
  -all_statuses      All Subscription Statuses (Default ACTIVE)
  -f FILE            Output to file (as json)
```

## My Other Projects

- [ShowOCI](https://github.com/oracle/oci-python-sdk/tree/master/examples/showoci)

- [ShowUsage](https://github.com/oracle/oci-python-sdk/tree/master/examples/showusage)

- [ShowRewards](https://github.com/oracle/oci-python-sdk/tree/master/examples/showrewards)

- [List Resources in Tenancy](https://github.com/oracle/oci-python-sdk/tree/master/examples/list_resources_in_tenancy)

- [Object Storage Tools](https://github.com/oracle/oci-python-sdk/tree/master/examples/object_storage)

- [Tag Resources in Tenancy](https://github.com/oracle/oci-python-sdk/tree/master/examples/tag_resources_in_tenancy)

- [Usage2ADW](https://github.com/oracle-samples/usage-reports-to-adw)

## Below example of reports from demo tenancy (random info generated)

```
########################################################################################################################
#                                              Running Show Subscription                                               #
########################################################################################################################
Author          : Adi Zohar
Disclaimer      : This is not an official Oracle application, It does not supported by Oracle !
Machine         : temp-mac (arm64)
App Version     : 2024.03.01
OCI SDK Version : 2.123.0
Python Version  : 3.10.6
Authentication  : Config File
Date/Time       : 2024-03-01 22:17:15
Command Line    : -t DEFAULT
Service Filter  : UCC
Status  Filter  : ACTIVE

########################################################################################################################
#                                                    Fetching data                                                     #
########################################################################################################################

Connecting to Identity Service...

Tenant Name  : test_tenant
Tenant Id    : ocid1.tenancy.oc1..aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Home Region  : us-ashburn-1

####################################################################################################
#                                        Universal Credits                                         #
####################################################################################################

Id           : 12345678
Service Name : Universal Credits
Currency     : USD
Time Start   : 2023-01-01 00:00
Time End     : 2025-12-31 23:59
Status       : ACTIVE
Total Value  : 100

#####################################################################################
#                  B88206 - Oracle PaaS and IaaS Universal Credits                  #
#####################################################################################
status                  : ACTIVE
subscription_id         : 12345678
id                      : 12345678
time_start              : 2023-01-01 00:00
time_end                : 2025-12-31 23:59
term_value              : 3
admin_email             : abc@test.com
buyer_email             : abc@test.com
agreement_id            : 100000000000
agreement_name          : US-CSA-12345678
time_agreement_end      : 2025-01-01 23:59
bill_to_customer        : The Company
end_user_customer       : The Company
service_to_customer     : The Company
billing_frequency       : Annual in Advance / Monthly Usage
csi                     : 12345678
operation_type          : REPLENISH
order_type              : CLOUD SERVICES
order_number            : 12345678
payment_method          : PO Number
payment_number          : 12345678
pricing_model           : Annual
product_number          : B88206
product_name            : Oracle PaaS and IaaS Universal Credits
is_payg                 :
is_having_usage         : True
is_variable_commitment  : True
original_promo_amount   :
funded_allocation_value :
line_net_amount         : 1000
total_value             : 1000
used_amount             :  100
available_amount        :  900
--> Commit              : 2023-01-01 - 2023-12-31, Total:      1000  Used:      1000  Available:            0  Funded:
--> Commit              : 2024-01-01 - 2024-12-31, Total:      1000  Used:       900  Available:          100  Funded:
--> Commit              : 2025-01-01 - 2025-12-31, Total:      1000  Used:         0  Available:         1000  Funded:

```
