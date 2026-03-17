## SHOWUSAGE - Oracle Cloud Infrastructure Usage and Cost Reporting Tool

SHOWUSAGE is a usage reporting tool which uses the Python SDK to extract usage and cost from your tenant. 
Authentication by User or Compute using instance principals, 
Output is printer friendly or to CSV Files.

**DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes, and rather OCI's official 
[cost analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm) 
and [usage reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm) features should be used instead.**

**Developed by Adi Zohar, 2021-2024**

## Modules Included:  
- oci.identity.IdentityClient
- oci.usage_api.UsageapiClient

## Executing using Cloud Shell:
```
1. install oci sdk package
   pip3 install --user oci

2. clone the oci sdk repo
   git clone https://github.com/oracle/oci-python-sdk

3. run showusage with delegation token
   cd oci-python-sdk/examples/showusage
   python3 showusage.py -dt -ds 2021-10-01 -days 10

4. run showusage with delegation token and csv output
   cd oci-python-sdk/examples/showusage
   python3 showusage.py -dt -ds 2021-10-01 -days 10 -csv
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
  -g GRANULARITY     Granularity DAILY or MONTHLY (Default DAILY)
  -report REPORT     Report Type = ALL / DATE / SERVICE / PRODUCT / REGION / RESOURCE / SPECIAL / TENANT / COMPARTMENT ( Default = ALL )
  -csv               Write to CSV files instead of output to the screen - usage_*.csv
```

## My Other Projects

- [ShowOCI](https://github.com/oracle/oci-python-sdk/tree/master/examples/showoci)

- [ShowSubscription](https://github.com/oracle/oci-python-sdk/tree/master/examples/showsubscription)

- [ShowRewards](https://github.com/oracle/oci-python-sdk/tree/master/examples/showrewards)

- [List Resources in Tenancy](https://github.com/oracle/oci-python-sdk/tree/master/examples/list_resources_in_tenancy)

- [Object Storage Tools](https://github.com/oracle/oci-python-sdk/tree/master/examples/object_storage)

- [Tag Resources in Tenanct](https://github.com/oracle/oci-python-sdk/tree/master/examples/tag_resources_in_tenancy)

- [Usage2ADW](https://github.com/oracle-samples/usage-reports-to-adw)

- [OCI Capacity Reporter](https://github.com/oracle/oci-python-sdk/tree/master/examples/oci_capacity_reporter)

## Below example of reports from demo tenancy (random costs generated)

```
########################################################################################################################
#                                                  Running Show Usage                                                  #
########################################################################################################################
Author          : Adi Zohar
Disclaimer      : This is not an official Oracle application,  It does not supported by Oracle, It should NOT be used for utilization calculation purposes !
                : Last 2 days may not be filled and should not be used
Machine         : test (x86_64)
App Version     : 2024.05.01
OCI SDK Version : 2.126.0
Python Version  : 3.9.13
Authentication  : Config File
Date/Time       : 2024-05-02 09:50:30
Command Line    : -ds 2024-03-01 -days 30
Start Date      : 03/01/2024
End Date        : 03/31/2024 Not Included

########################################################################################################################
#                                                    Fetching data                                                     #
########################################################################################################################

Connecting to Identity Service...

Tenant Name  : testtenant
Tenant Id    : ocid1.tenancy.oc1..xxxxxxxxxxxxx
Home Region  : us-ashburn-1

Connecting to UsageAPI Service...

#####################################################################################
#                     Daily Summary for 03/01/2024 - 03/30/2024                     #
#####################################################################################

Day                       Cost       Month-31           Year
=============== ============== ============== ==============
2024-03-01               310.1          9,614        113,200
2024-03-02               314.8          9,758        114,890
2024-03-03               316.8          9,821        115,633
2024-03-04               317.4          9,839        115,847
2024-03-05               325.7         10,095        118,862
2024-03-06               318.5          9,874        116,255
2024-03-07               315.2          9,773        115,066
2024-03-08               318.2          9,863        116,128
2024-03-09               317.2          9,834        115,789
2024-03-10               317.1          9,831        115,750
2024-03-11               317.1          9,830        115,743
2024-03-12               321.9          9,978        117,485
2024-03-13               321.7          9,974        117,438
2024-03-14               326.1         10,110        119,037
2024-03-15               324.6         10,063        118,486
2024-03-16               321.7          9,973        117,428
2024-03-17               322.4          9,995        117,680
2024-03-18               321.5          9,966        117,339
2024-03-19               321.8          9,975        117,450
2024-03-20               324.4         10,057        118,416
2024-03-21               333.3         10,331        121,643
2024-03-22               327.2         10,144        119,441
2024-03-23               325.9         10,104        118,962
2024-03-24               325.9         10,104        118,963
2024-03-25               327.6         10,155        119,562
2024-03-26               332.6         10,312        121,413
2024-03-27               459.1         14,232        167,575
2024-03-28               582.3         18,053        212,554
2024-03-29               582.3         18,052        212,546
2024-03-30               581.9         18,040        212,408
=============== ============== ============== ==============
Total                 10,572.6

#####################################################################################
#                 Product Summary for 03/01/2024 - 03/30/2024 in USD                #
#####################################################################################

Product                                                                Days      Quantity OSR Eligible         Cost     Month-31         Year
================================================================= ========= ============= ============ ============ ============ ============
B88317 - Virtual Machine Standard - X5 - 1.2XL                           30           0.0          0.0          0.0            0            0
B89738 - NoSQL Database Cloud Service - Provisioned Read Units           30           1.9          0.0          0.0            0            0
B88525 - DNS - Queries                                                   30           0.0          0.0          0.0            0            0
B89739 - NoSQL Database Cloud Service - Storage                          30           1.9          0.0          0.0            0            0
B108077 - Oracle Cloud Infrastructure Generative AI - Large Coher        30           0.6          0.0          0.0            0            0
B108080 - Oracle Cloud Infrastructure Generative AI - Llama2-70          30           1.0          0.0          0.0            0            0
B89737 - NoSQL Database Cloud Service - Provisioned Write Units          30           1.9          0.0          0.0            0            0
B92963 - MySQL Database Service - Standard - E3 - Memory                 30          30.4          0.1          0.1            0            1
B89643 - Oracle Integration - Standard - BYOL                            30           7.0          0.1          0.1            0            1
B92072 - API Calls                                                       30           0.0          0.1          0.1            0            1
B92024 - MySQL Database for HeatWave - Standard - Node per hour          30           0.3          0.1          0.1            0            1
B89057 - File Storage                                                    30          10.5          0.1          0.1            0            1
B92962 - MySQL Database Service - Standard - E3                          30           3.8          0.1          0.1            0            2
B90323 - Health Checks - Basic                                           30           1.9          0.1          0.1            0            2
B89644 - Oracle Integration - Enterprise - BYOL                          30          18.0          0.2          0.2            0            2
B88327 - Outbound Data Transfer for Volume Replica Zone 1                30          85.0          0.2          0.2            0            2
B89639 - Oracle Integration - Standard                                   30           9.0          0.2          0.2            0            3
B93000 - Infrequent Access Storage                                       30         121.8          0.2          0.2            0            3
B88167 - Oracle Identity Cloud - Standard - Active User Per Hour         30         308.0          0.4          0.4            0            4
B90453 - Oracle Autonomous Transaction Processing                        30           8.6          0.4          0.4            0            5
B91627 - Object Storage - Requests                                       30         157.9          0.5          0.5            1            6
B89640 - Oracle Integration - Enterprise                                 30          11.0          0.5          0.5            1            6
B90260 - Oracle Digital Assistance Cloud Service - Requests              30       5,500.0          0.6          0.6            1            7
B97385 - Standard - E5 - Memory                                          30         302.1          0.6          0.6            1            7
B96200 - Oracle Cloud Infrastructure - Database Management - Auto        30          70.2          1.8          1.8            2           21
B97384 - Standard - E5                                                   30          61.7          1.8          1.8            2           23
B89636 - Oracle Analytics Cloud - Professional - BYOL                    30         216.0          2.1          2.1            2           25
B92593 - Logging - Storage                                               30          79.0          3.5          3.5            4           42
B92426 - MySQL Database Service - Storage                                30       2,417.4          3.6          3.6            4           44
B92307 - Notebook Session - Compute - E3 - GB's Per Hour                 30      12,029.8          4.5          4.5            5           55
B92306 - Notebook Session - Compute - E3 - OCPU's Per Hour               30         751.9          4.7          4.7            5           57
B89040 - Oracle Autonomous Data Warehouse                                30         105.5          5.3          5.3            5           65
B88318 - Windows OS                                                      30       1,468.8          0.0          7.5            8           91
B88319 - Oracle Bare Metal Cloud - 100 Mbps Load Balancer                30       1,440.2          7.7          7.7            8           93
B90573 - Database Cloud Service - All Editions - BYOL                    30       2,192.8         12.7         12.7           13          155
B92092 - Key Management Service - Key Version Counts                     30          41.3         14.2         14.2           15          173
B92890 - Operations Insights for External Oracle Databases and Ho        30       1,440.0         21.6         21.6           22          263
B93031 - Flexible Load Balancer Bandwidth                                30     230,401.7         22.3         22.3           23          271
B88514 - Model Deployment - Compute - Standard2                          30       1,440.0         23.0         23.0           24          279
B93312 - Optimized - X9 - Memory                                         30      20,541.9         30.8         30.8           32          375
B89637 - Oracle Analytics Cloud - Enterprise - BYOL                      30       3,204.0         31.0         31.0           32          377
...
================================================================= ========= ============= ============ ============ ============ ============
Total                                                                                         10,565.1     10,572.6       10,925      128,633

#####################################################################################
#                 Region Summary for 03/01/2024 - 03/30/2024 in USD                 #
#####################################################################################

Region                         Days         Cost     Month-31         Year
========================= ========= ============ ============ ============
uk-london-1                      30        901.5          932       10,968
us-phoenix-1                     30      4,129.1        4,267       50,238
us-ashburn-1                     30      5,407.6        5,588       65,793
========================= ========= ============ ============ ============
Total                                   10,572.6       10,925      128,633

#####################################################################################
#                 Service Summary for 03/01/2024 - 03/30/2024 in USD                #
#####################################################################################

Service                                            Days      Quantity   OSR Eligible         Cost     Month-31         Year
============================================= ========= ============= ============== ============ ============ ============
DevOps Service                                       30           0.0            0.0          0.0            0            0
DNS                                                  30           0.0            0.0          0.0            0            0
Oracle Cloud Infrastructure Generative AI            30           1.6            0.0          0.0            0            0
NoSQL Database                                       30           5.8            0.0          0.0            0            0
Identity Cloud Service                               30          33.0            0.0          0.0            0            0
API Gateway                                          30           0.0            0.1          0.1            0            1
Virtual Cloud Network                                30          43.6            0.1          0.1            0            1
File Storage                                         30          10.5            0.1          0.1            0            1
Health Checks                                        30           1.9            0.1          0.1            0            2
Oracle Public Cloud Services - CLOUDCM               30         275.0            0.3          0.3            0            4
Digital Assistant                                    30       5,500.0            0.6          0.6            1            7
Integration Service                                  30          45.0            1.0          1.0            1           12
Key Management - Shard 3                             30           2.9            1.0          1.0            1           13
Key Management - Shard 4                             30           5.0            1.8          1.8            2           22
Key Management - Shard 2                             30           8.7            3.1          3.1            3           38
Logging                                              30          79.0            3.5          3.5            4           42
Key Management                                       30          24.7            8.2          8.2            8           99
Object Storage                                       30       1,207.4           24.1         24.1           25          293
Container Engine Service                             30       2,160.0           32.4         32.4           33          394
Full Stack Disaster Recovery Service                 30       3,600.0           46.1         46.1           48          561
Data Flow                                            30      28,205.8           85.0         85.0           88        1,034
Data Science                                         30      42,234.4           99.7         99.7          103        1,213
Visual Builder                                       30       2,160.4          100.2        100.2          104        1,219
MySQL                                                30      26,931.9          109.3        109.3          113        1,330
Database Management                                  30       3,717.7          147.7        147.7          153        1,796
Content Management                                   30           3.9          150.8        150.8          156        1,835
Load Balancer                                        30     232,562.0          191.8        191.8          198        2,333
Container Engine for Kubernetes                      30       2,596.8          259.7        259.7          268        3,159
Analytics                                            30       6,156.0          364.1        364.1          376        4,429
Operations Insights                                  30      10,604.0          408.7        408.7          422        4,973
Compute                                              30     203,237.9          601.5        609.0          629        7,410
Block Storage                                        30     180,246.4          690.9        690.9          714        8,406
Application Performance Monitoring                   30       3,599.0          979.2        979.2        1,012       11,913
Data Integration                                     30       6,488.0        1,297.6      1,297.6        1,341       15,787
Logging Analytics                                    30           3.9        1,435.5      1,435.5        1,483       17,465
Database                                             30     285,130.3        3,520.8      3,520.8        3,638       42,837
============================================= ========= ============= ============== ============ ============ ============
Total                                                                       10,565.1     10,572.6       10,925      128,633

#####################################################################################
#               ResourceId Summary for 03/01/2024 - 03/31/2024 in USD               #
#####################################################################################

Resource                                                                                                  Days      Quantity   OSR Eligible         Cost     Month-31         Year
==================================================================================================== ========= ============= ============== ============ ============ ============
orasenatdpltdevopsnetw02/oci-logs._apigateway.ocid1.compartment.oc1..aaaaaaaauwmdohskr2c6iscauwb6mow        30           0.0            0.0          0.0            0            0
orasenatdpltdevopsnetw02/oci-logs._flowlogs.ocid1.compartment.oc1..aaaaaaaabldey3l2ymkpjs7jlnpbcmadl        30           0.0            0.0          0.0            0            0
orasenatdpltdevopsnetw02/SaaSData_OSBucket                                                                  30           0.0            0.0          0.0            0            0
ocid1.datasciencejob.oc1.iad.xxx                                                                            30           0.0            0.0          0.0            0            0
orasenatdpltdevopsnetw02/demo-bucket                                                                        30           0.0            0.0          0.0            0            0
orasenatdpltdevopsnetw02/dataflow-logs                                                                      30           0.0            0.0          0.0            0            0
orasenatdpltdevopsnetw02/bucket-20220805-1420                                                               30           0.0            0.0          0.0            0            0
orasenatdpltdevopsnetw02/sec-test-new                                                                       30           0.0            0.0          0.0            0            0
...
==================================================================================================== ========= ============= ============== ============ ============ ============
Total                                                                                                                               1,583.5      1,584.7        9,825      115,686

#####################################################################################
#           Service, Region and Product for 03/01/2024 - 03/31/2024 in USD          #
#####################################################################################

Service,Region and Product                                                     Days      Quantity   OSR Eligible         Cost
========================================================================= ========= ============= ============== ============
API Gateway:us-ashburn-1:API Calls                                               30           0.0            0.0          0.0
API Gateway:us-phoenix-1:API Calls                                               30           0.0            0.0          0.0
Analytics:ca-toronto-1:Oracle Analytics Cloud - Enterprise                       30          18.0            2.2          2.2
Analytics:us-ashburn-1:Oracle Analytics Cloud - Enterprise                       30         300.0           36.3         36.3
Analytics:us-ashburn-1:Oracle Analytics Cloud - Enterprise - BYOL                30         258.0            2.5          2.5
Analytics:us-ashburn-1:Oracle Analytics Cloud - Professional - BYOL              30          36.0            0.3          0.3
Analytics:us-phoenix-1:Oracle Analytics Cloud - Enterprise                       30         138.0           16.7         16.7
Analytics:us-phoenix-1:Oracle Analytics Cloud - Enterprise - BYOL                30         276.0            2.7          2.7
...
Visual Builder:us-ashburn-1:Visual Builder - OCPU per hour                       30         239.9           11.1         11.1
Visual Builder:us-phoenix-1:Visual Builder - OCPU per hour                       30         120.0            5.6          5.6
========================================================================= ========= ============= ============== ============
Total                                                                                                    1,583.5      1,584.7

#####################################################################################
#               Compartment Summary for 03/01/2024 - 03/31/2024 in USD              #
#####################################################################################

Compartment                                                            Service                                      Days      Quantity   OSR Eligible         Cost     Month-31         Year
====================================================================== ======================================= ========= ============= ============== ============ ============ ============
tenant_root/Compartment1/compartment1_2                                Block Storage                                  30          49.6            0.2          0.2            2           23
tenant_root/Compartment1/compartment1_2                                Database                                       30           0.1            0.4          0.4            4           52
tenant_root/Compartment1/compartment1_2                                Block Storage                                  30         521.4            2.2          2.2           23          272
tenant_root/Compartment1/compartment1_2                                Compute                                        30       1,226.4            3.6          3.6           37          437
tenant_root/Compartment1/compartment1_2                                Database                                       30         757.9            2.9          2.9           30          356
tenant_root/Compartment1/compartment1_2                                File Storage                                   30           0.0            0.0          0.0            0            0
tenant_root/Compartment1/compartment1_2                                Key Management                                 30           0.2            0.1          0.1            1           16
tenant_root/Compartment1/compartment1_2                                Key Management - Shard 2                       30           0.4            0.3          0.3            3           31
tenant_root/Compartment1/compartment1_2                                Object Storage                                 30           0.6            0.0          0.0            0            2
tenant_root/Compartment1/compartment1_2                                Virtual Cloud Network                          30           0.0            0.0          0.0            0            0
...
tenant_root/Compartment2                                               API Gateway                                    30           0.0            0.0          0.0            0            0
tenant_root/Compartment2                                               Block Storage                                  30       1,023.8            4.2          4.2           43          507
tenant_root/Compartment2                                               Compute                                        30      14,545.5          312.5        312.5        3,229       38,023
tenant_root/Compartment2                                               Database                                       30       2,142.9           22.3         22.3          230        2,713
tenant_root/Compartment2                                               Database Management                            30         144.0            5.8          5.8           60          701
tenant_root/Compartment2                                               File Storage                                   30           0.0            0.0          0.0            0            0
tenant_root/Compartment2                                               Full Stack Disaster Recovery Service           30         144.0            1.8          1.8           19          224
tenant_root/Compartment2                                               Key Management                                 30           0.1            0.1          0.1            1            8
tenant_root/Compartment2                                               Load Balancer                                  30         792.0            0.9          0.9            9          108
tenant_root/Compartment2                                               Logging                                        30           3.0            0.1          0.1            2           18
tenant_root/Compartment2                                               NoSQL Database                                 30           0.3            0.0          0.0            0            0
tenant_root/Compartment2                                               Object Storage                                 30           3.9            0.1          0.1            1           12
tenant_root/Compartment2                                               Virtual Cloud Network                          30           1.3            0.0          0.0            0            0
====================================================================== ======================================= ========= ============= ============== ============ ============ ============
Total                                                                                                                                         1,379.9      1,381.0       14,271      168,027

```
