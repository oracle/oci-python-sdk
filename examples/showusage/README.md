## SHOWUSAGE - Oracle Cloud Infrastructure Usage and Cost Reporting Tool

SHOWUSAGE is a usage reporting tool which uses the Python SDK to extract usage and cost from your tenant. 
Authentication by User or Compute using instance principals, 
Output is printer friendly.

**DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes, and rather OCI's official 
[cost analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm) 
and [usage reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm) features should be used instead.**

**Developed by Adi Zohar, 2021**

## Modules Included:  
- oci.identity.IdentityClient            
- oci.usage_api.UsageapiClient   

## Executing using Cloud Shell:
```
1. install oci sdk package
   pip3 install --user oci

2. clone the oci sdk repo
   git clone https://github.com/oracle/oci-python-sdk

3. run showoci with delegation token
   cd oci-python-sdk/examples/showusage
   python3 showusage.py -dt -ds 2021-10-01
```

## Installation of Python 3 incase you don't have Python3 installed:
Please follow [Python Documentation](https://docs.python.org/3/using/index.html)

## Install OCI SDK Packages:
Please follow [Oracle Python SDK Documentation](https://github.com/oracle/oci-python-sdk)

## Setup connectivity using Instance Principals

```  
1. Login to your OCI Cloud console

2. Create new Dynamic Group : DynShowUsageGroup  
   Obtain Compute OCID and add rule - any {ALL {instance.id = 'ocid1.instance.oc1.xxxxxxxxxx'}}

3. Create new Policy: ShowUsgaeDynamicGroupPolicy with Statements:
   Allow dynamic group DynShowUsageGroup to inspect tenancies in tenancy
   Allow dynamic group DynShowUsageGroup to read usage-report in tenancy
```

## Setup connectivity using User

```  
1. Login to your OCI Cloud console

2. Create new group : ShowUsageGroup  

3. Create new Policy: ShowUsageGroupPolicy with Statements:
   Allow group ShowUsageGroup to inspect tenancies in tenancy
   Allow group ShowUsageGroup to read usage-report in tenancy

4. Create new User  : showuser.user -> Add to ShowUsageGroup group  

5. Config OCI config file - ~/.oci/config
   Please follow SDK config documentation - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm 
```

## Copy the Software
Download the showusage.py from this project  

Execute  

```
$ python3 showusage.py  

optional arguments:
  -h, --help         show this help message and exit
  -c CONFIG_FILE     OCI CLI Config file
  -t CONFIG_PROFILE  Config Profile inside the config file
  -p PROXY           Set Proxy (i.e. www-proxy-server.com:80)
  -ip                Use Instance Principals for Authentication
  -dt                Use Delegation Token for Authentication
  -ds DATE_START     Start Date - format YYYY-MM-DD
  -de DATE_END       End Date - format YYYY-MM-DD, (Not Inclusive)
  -days DAYS         Add Days Combined with Start Date (de is ignored if specified)
  -report REPORT     Report Type = PRODUCT / DAILY / ALL ( Default = ALL )


```

## Below example of reports from demo tenancy (random costs generated)

```
########################################################################################################################
#                                                  Running Show Usage                                                  #
########################################################################################################################
Author          : Adi Zohar
Disclaimer      : This is not an official Oracle application,  It does not supported by Oracle, It should NOT be used for utilization calculation purposes !
                : Last 2 days may not be filled and should not be used
Machine         : adiwrk (x86_64)
App Version     : 2021.10.07
OCI SDK Version : 2.45.1
Python Version  : 3.6.8
Authentication  : Config File
Date/Time       : 2021-10-07 12:57:15
Command Line    : -ds 2021-09-01 -de 2021-10-01
Start Date      : 09/01/2021
End Date        : 10/01/2021 Not Included

########################################################################################################################
#                                                    Fetching data                                                     #
########################################################################################################################

Connecting to Identity Service...

Tenant Name  : oraxxxxxxxxx
Tenant Id    : ocid1.tenancy.oc1..aaaaaaaaxtkkpxc5qwgpwx7y2wt5pinegyzea4uaxxxxxxxxxxxxxxxxxxx
Home Region  : us-ashburn-1

Connecting to UsageAPI Service...

#####################################################################################
#                     Daily Summary for 09/01/2021 - 09/30/2021                     #
#####################################################################################

Day                       Cost       Month-31           Year
=============== ============== ============== ==============
2021-09-01               118.8          3,681         43,346
2021-09-02               120.7          3,741         44,042
2021-09-03               118.0          3,658         43,068
2021-09-04               117.2          3,632         42,765
2021-09-05               117.1          3,630         42,743
2021-09-06               117.0          3,626         42,692
2021-09-07               120.0          3,719         43,783
2021-09-08               117.7          3,650         42,972
2021-09-09               117.5          3,642         42,886
2021-09-10               116.0          3,596         42,340
2021-09-11               115.7          3,587         42,229
2021-09-12               115.6          3,585         42,210
2021-09-13               118.3          3,668         43,183
2021-09-14               117.0          3,628         42,713
2021-09-15               117.2          3,633         42,779
2021-09-16               118.9          3,686         43,396
2021-09-17               118.1          3,660         43,097
2021-09-18               122.6          3,800         44,742
2021-09-19               122.0          3,782         44,532
2021-09-20               123.4          3,827         45,055
2021-09-21               643.5         19,947        234,863
2021-09-22               124.6          3,862         45,474
2021-09-23               125.5          3,889         45,794
2021-09-24               126.2          3,912         46,060
2021-09-25               724.8         22,470        264,570
2021-09-26               125.2          3,881         45,699
2021-09-27             3,300.2        102,307      1,204,587
2021-09-28               133.7          4,144         48,793
2021-09-29               131.5          4,076         47,994
2021-09-30               133.6          4,141         48,761
=============== ============== ============== ==============
Total                  7,937.5

#####################################################################################
#                  Product Summary for 09/01/2021 - 09/30/2021                      #
#####################################################################################

Product                                                                Days      Quantity         Cost     Month-31         Year
================================================================= ========= ============= ============ ============ ============
B89639 - Oracle Integration - Standard                                   30          38.0          0.9            1           11
B92602 - 10Mbps Load Balancer Bandwidth                                  30      12,731.8          1.3            1           15
B92963 - MySQL Database Service - Standard - E3 - Memory                 30         612.2          1.3            1           16
B92212 - Oracle Autonomous JSON Database                                 30           5.7          1.8            2           22
B89636 - Oracle Analytics Cloud - Professional - BYOL                    30         224.1          2.2            2           26
B90453 - Oracle Autonomous Transaction Processing                        30          44.0          2.2            2           27
B92307 - Standard - E3 - Memory                                          30       7,007.4          2.6            3           32
B92306 - Standard - E3                                                   30         461.7          2.9            3           35
B92962 - MySQL Database Service - Standard - E3                          30          76.5          2.9            3           35
B89630 - Oracle Analytics Cloud - Professional                           30          83.7          3.4            3           41
B91210 - Content and Experience Cloud Service - 5000 Assets              30           1.0          3.9            4           47
B92911 - Oracle APEX Application Development                             30          12.4          4.0            4           49
B92993 - Compute OCPU                                                    30          17.2          5.5            6           68
B93031 - Flexible Load Balancer Bandwidth                                30      62,144.3          6.2            6           76
B93082 - Database Management - External DB BYOL                          30         324.5          6.5            7           79
B89644 - Oracle Integration - Enterprise - BYOL                          30         766.0          7.4            8           90
B93312 - Optimized - X9 - Memory                                         30       7,200.0         10.8           11          131
B89164 - Oracle Security Monitoring and Compliance Cloud - Config        30         720.0         10.9           11          132
B92601 - 10Mbps Load Balancer Base                                       30       1,273.2         14.4           15          175
B88319 - Oracle Bare Metal Cloud - 100 Mbps Load Balancer                30       2,889.2         15.4           16          187
B89039 - Oracle Autonomous Data Warehouse - BYOL                         30       1,787.7         17.3           18          211
B89637 - Oracle Analytics Cloud - Enterprise - BYOL                      30       2,171.5         21.0           22          256
B91628 - Block Volume - Backup                                           30         893.0         22.5           23          274
B93426 - Database Management - Oracle Cloud Databases                    30         629.1         25.2           26          306
B90573 - Database Cloud Service - All Editions - BYOL                    30       4,439.9         25.8           27          314
B93114 - Standard - E4 - Memory                                          30      18,017.2         27.0           28          329
B89162 - Oracle Management Cloud - Enterprise Edition - 100 Entit        30         720.0         36.3           38          442
B89163 - Oracle Management Cloud - Log Analytics Edition - 300 Gi        30         720.0         36.3           38          442
B89165 - Oracle Security Monitoring and Compliance Cloud - Securi        30         720.0         36.3           38          442
B93113 - Standard - E4                                                   30       1,483.1         37.1           38          451
B93311 - Optimized - X9                                                  30         720.0         38.9           40          473
B89040 - Oracle Autonomous Data Warehouse                                30         789.4         39.8           41          484
B90455 - Oracle Autonomous Transaction Processing - Exadata Stora        30          12.4         54.9           57          668
B93030 - Flexible Load Balancer Base                                     30       6,214.4         70.2           73          854
B89631 - Oracle Analytics Cloud - Enterprise                             30         630.5         76.3           79          928
B89041 - Oracle Autonomous Data Warehouse - Exadata Storage              30          17.5         77.8           80          947
B89646 - Oracle Visual Builder Cloud Service - OCPU Per Hour             30       2,160.0        100.2          103        1,219
B92302 - Blockchain Platform Cloud Service - Standard                    30       1,440.0        309.6          320        3,767
B92637 - Content and Experience Cloud Service - 5000 Assets - BYO        30           3.0        361.3          373        4,396
B92598 - Data Integration - Workspace Usage                              30       2,160.0        432.0          446        5,256
B91962 - Block Volume - Performance Units                                30     265,057.8        450.6          466        5,482
B92941 - Application Performance Monitoring - Events Per Hour            30         720.0        468.0          484        5,694
B91961 - Block Volume - Storage                                          30      30,372.7        774.5          800        9,423
B92683 - Oracle Analytics - Enterprise                                   30       3,002.5      4,289.5        4,432       52,188
================================================================= ========= ============= ============ ============ ============
Total                                                                                          7,937.5        8,202       96,572

* Above costs are demo costs for the readme.

```
