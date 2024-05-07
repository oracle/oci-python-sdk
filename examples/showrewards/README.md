## SHOWREWARDS - Oracle Cloud Infrastructure subscruption reporting

SHOWREWARDS is a support rewards reporting tool which uses the Python SDK to extract tenant subscription and support rewards.
Authentication by User or Compute using instance principals,

**DISCLAIMER - This is not an official Oracle application,  It does not supported by Oracle Support.

**Developed by Adi Zohar, 2024-2024**

## Modules Included:
- oci.identity.IdentityClient
- OrganizationSubscriptionClient
- oci.usage.RewardsClient

## Executing using Cloud Shell:
```
1. install oci sdk package
   pip3 install --user oci

2. clone the oci sdk repo
   git clone https://github.com/oracle/oci-python-sdk

3. run showrewards.py with delegation token
   cd oci-python-sdk/examples/showrewards
   python3 showrewards.py -dt
```

## Installation of Python 3 incase you don't have Python3 installed:
Please follow [Python Documentation](https://docs.python.org/3/using/index.html)

## Install OCI SDK Packages:
Please follow [Oracle Python SDK Documentation](https://github.com/oracle/oci-python-sdk)

## Setup connectivity using Instance Principals

```
1. Login to your OCI Cloud console

2. Create new Dynamic Group : DynShowRewardsGroup  
   Obtain Compute OCID and add rule - any {ALL {instance.id = 'ocid1.instance.oc1.xxxxxxxxxx'}}

3. Create new Policy: DynShowRewardsGroupPolicy with Statements:
   Allow dynamic group DynShowRewardsGroup to inspect tenancies in tenancy
   Allow dynamic group DynShowRewardsGroup to inspect organizations-subscription in tenancy
   Allow dynamic group DynShowRewardsGroup to read support-rewards in tenancy
```

## Setup connectivity using User

```  
1. Login to your OCI Cloud console

2. Create new group : ShowRewardsGroup  

3. Create new Policy: ShowRewardsGroupPolicy with Statements:
   Allow group ShowRewardsGroup to inspect tenancies in tenancy
   Allow group ShowRewardsGroup to inspect organizations-subscription in tenancy
   Allow group ShowRewardsGroup to read support-rewards in tenancy

4. Create new User  : showrewards.user -> Add to ShowRewardsGroup group  

5. Config OCI config file - ~/.oci/config
   Please follow SDK config documentation - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm 
```

## Copy the Software
Download the showrewards.py from this project  

Execute  

```
$ python3 showrewards.py  

optional arguments:
  -h, --help         show this help message and exit
  -c CONFIG_FILE     OCI CLI Config file
  -t CONFIG_PROFILE  Config Profile inside the config file
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
  -include_products  Include products per rewards for JSON file only
  -f FILE            Output to file (as json)
  -csv               Write to CSV files - rewards.csv, redemption.csv, reward_products.csv if -include_products specificed
```

## My Other Projects

- [ShowOCI](https://github.com/oracle/oci-python-sdk/tree/master/examples/showoci)

- [ShowSubscription](https://github.com/oracle/oci-python-sdk/tree/master/examples/showsubscription)

- [ShowRewards](https://github.com/oracle/oci-python-sdk/tree/master/examples/showrewards)

- [List Resources in Tenancy](https://github.com/oracle/oci-python-sdk/tree/master/examples/list_resources_in_tenancy)

- [Object Storage Tools](https://github.com/oracle/oci-python-sdk/tree/master/examples/object_storage)

- [Tag Resources in Tenancy](https://github.com/oracle/oci-python-sdk/tree/master/examples/tag_resources_in_tenancy)

- [Usage2ADW](https://github.com/oracle-samples/usage-reports-to-adw)


## Below example of reports from demo tenancy (random info generated)

```
########################################################################################################################
#                                                 Running Show Rewards                                                 #
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
#                                 Reward Redemptions                                #
#####################################################################################

time_invoiced        : 2023-05-22 00:00
time_redeemed        : 2023-05-24 18:08
redemption_email     : test@tests.com
redemption_code      : 8888888-9999999-0000000-111111111111
invoice_number       : 12345678
invoice_currency     : USD
invoice_total_amount : None
redeemed_rewards     :       32,000
base_rewards         :       32,000
fx_rate              :            1

#####################################################################################
#           Reward Monthly Summary for 2023-05-01 00:00 - 2023-05-31 23:59          #
#####################################################################################

time_rewards_expired    : 2024-06-30 23:59
time_rewards_earned     : 2023-06-01 00:00
usage_period_key        : 12345567
is_manual               : False
usage_amount            :       64,200
eligible_usage_amount   :       64,000
ineligible_usage_amount :          200
available_rewards       :       16,000
redeemed_rewards        :            0
earned_rewards          :       16,000

#####################################################################################
#                                   Reward Summary                                  #
#####################################################################################

tenancy_id              : ocid1.tenancy.oc1..xxx
subscription_id         : 12344566
currency                : USD
redemption_code         : 8888888-9999999-0000000-111111111111
rewards_rate            :           25
total_rewards_available :      200,000


```
