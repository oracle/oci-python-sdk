## Tag Resources in Tenancy

Tag Resources in Tenancy is a tool to help you tag resources easily, it uses the OCI Python SDK. 
It covers the below OCI components, 
Authentication by User or Compute using instance principals, 
Output can be printer friendly, Summary or JSON.

**Developed by Adi Zohar, Nov 2020**

## Modules Included:  
- oci.core.VirtualNetworkClient          
- oci.core.ComputeClient                 
- oci.core.BlockstorageClient            
- oci.object_storage.ObjectStorageClient 
- oci.database.DatabaseClient            
- oci.load_balancer.LoadBalancerClient   
- oci.identity.IdentityClient

** DISCLAIMER – This is not an official Oracle application

## Executing using Cloud Shell:
```
1. install oci sdk package
   pip3 install --user oci

2. clone the oci sdk repo
   git clone https://github.com/oracle/oci-python-sdk

3. run with delegation token
   cd oci-python-sdk/examples/tag_resources_in_tenancy
   python3 tag_resources_in_tenancy.py --help
```

## OCI Authentication using User - Privilges can be aligned accordingly
Required OCI IAM user with manage privileges to the compartment you aim to tag

```
ALLOW GROUP ReadOnlyUsers to manage all-resources IN TENANCY
```

## Installation of Python 3 incase you don't have Python3 installed:
Please follow Python Documentation - https://docs.python.org/3/using/index.html

## Install oci SDK Packages:
Please follow Oracle Python SDK Documentation - https://github.com/oracle/oci-python-sdk

## Copy the Software
Download the tag_resources_in_tenancy.py from this project  

Execute  

```
$ python3 tag_resources_in_tenancy.py --help

usage: tag_resources_in_tenancy.py [-h] [-t CONFIG_PROFILE] [-p PROXY]
                                   [-cp COMPARTMENT] [-rg REGION] [-ip] [-dt]
                                   [-tag TAG]
                                   [-action {add_defined,add_free,del_defined,del_free,list}]
                                   [-output {list,json,summary}]

optional arguments:
  -h, --help            show this help message and exit
  -t CONFIG_PROFILE     Config file section to use (tenancy profile)
  -p PROXY              Set Proxy (i.e. www-proxy-server.com:80)
  -cp COMPARTMENT       Filter by Compartment Name or Id
  -rg REGION            Filter by Region Name
  -ip                   Use Instance Principals for Authentication
  -dt                   Use Delegation Token for Authentication
  -tag TAG              Tag in format - namespace.key=value or key=value
  -action {add_defined,add_free,del_defined,del_free,list}
                        Action Type
  -output {list,json,summary}
                        Output type, default=summary
```

## Example Execution for adding defined Tags:
```
python3 tag_resources_in_tenancy.py -action add_defined -tag BillingNS.Division=TEST -cp TestCompartment -rg us-ashburn-1 

Connecting to Identity Service...
Loading Compartments...
    Total 1 compartments loaded.

##########################################################################################
#                                  Running Tag Conpute                                   #
##########################################################################################
Written By Adi Zohar, Nov 2020
Starts at 2020-11-16 21:15:20
Command Line  : -action add_defined -tag BillingNS.Division=TEST -cp TestCompartment -rg us-ashburn-1 
Tag Namespace : BillingNS
Tag Key       : Division
Tag Value     : TEST
Tenant Name   : test_tenant
Tenant Id     : ocid1.tenancy.oc1..aaaaaaaaxxxxxxxxxx


Reading Tag Namespaces...
   Found Tag Namespace 'BillingNS', id = ocid1.tagnamespace.oc1..aaaaaaaaxgdcknccy4dsmr7s64iafc6s6rznnc2bvitxxxxxxxxxxxx
   Found Tag Key 'Division', id = ocid1.tagdefinition.oc1..aaaaaaaaxpbe55t574ezmwrgw5qbbwvkrm2r7k6lo4cxcxxxxxxxxxxxxx

Processing Regions...

Region us-ashburn-1...
    Compartment TestCompartment
        Instances              - 2     Tag Added = 0         Tag Exist = 2
        Boot Volumes           - 2     Tag Added = 0         Tag Exist = 2
        Boot Volumes Backups   - 22    Tag Added = 0         Tag Exist = 22
        Block Volumes          - 1     Tag Added = 0         Tag Exist = 1
        Block Volumes Backups  - (-)
        Volume Groups          - (-)
        Volume Groups Backup   - (-)
        Network VCNs           - 2     Tag Added = 0         Tag Exist = 2
        Network Subnets        - 3     Tag Added = 0         Tag Exist = 3
        Network CPEs           - (-)
        Network DHCPs          - 2     Tag Added = 0         Tag Exist = 2
        Network IGWs           - 1     Tag Added = 0         Tag Exist = 1
        Network IPSECs         - (-)
        Network LPGs           - 2     Tag Added = 0         Tag Exist = 2
        Network NATGWs         - 2     Tag Added = 0         Tag Exist = 2
        Network NSGs           - 2     Tag Added = 0         Tag Exist = 2
        Network RPGs           - 1     Tag Added = 0         Tag Exist = 1
        Network Routes         - 4     Tag Added = 0         Tag Exist = 4
        Network SLs            - 2     Tag Added = 0         Tag Exist = 2
        Network SGWs           - 1     Tag Added = 0         Tag Exist = 1
        Network VCircuit       - (-)
        Load Balancers         - 1     Tag Added = 0         Tag Exist = 1
        DB DB Systems          - (-)
        DB Autonomous          - 1     Tag Added = 0         Tag Exist = 1
        Object Storage Buckets - 5     Tag Added = 5         Tag Exist = 0

##########################################################################################
#                                     Output as List                                     #
##########################################################################################
us-ashburn-1 | TestCompartment   | Instances              | adiwin               | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Boot Volumes           | adiwin (Boot Volume) | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Boot Volumes           | adiwork (Boot Volume)| Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Block Volumes          | adiwork-100g         | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network VCNs           | vcnspoke             | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network VCNs           | vcn                  | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network Subnets        | privsub              | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network Subnets        | pubsub               | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network IGWs           | igw                  | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network LPGs           | hubtospoke           | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network LPGs           | spoketohub           | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network NATGWs         | nat                  | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network NATGWs         | NATGW                | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network NSGs           | port80only           | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network NSGs           | vcn_nsg              | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network RPGs           | null                 | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network Routes         | route.lpg            | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Network SGWs           | sgw                  | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Load Balancers         | lb                   | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | DB Autonomous          | ADI_USAGE_19C        | Exist   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Object Storage Buckets | AuditBucket          | Added   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Object Storage Buckets | FlowLogs             | Added   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Object Storage Buckets | shared               | Added   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Object Storage Buckets | test_restore         | Added   |  | BillingNS.Division=TEST
us-ashburn-1 | TestCompartment   | Object Storage Buckets | usage_cost_bucket    | Added   |  | BillingNS.Division=TEST

##########################################################################################
#                            Completed at 2020-11-16 21:15:37                            #
##########################################################################################

```
## Example Execution for adding freeform tags:
```
python3 tag_resources_in_tenancy.py -cp cpTest -rg ashbu -tag "Prog=Test Space" -action add_free

Connecting to Identity Service...
Loading Compartments...
    Total 1 compartments loaded.

##########################################################################################
#                                  Running Tag Conpute                                   #
##########################################################################################
Written By Adi Zohar, Nov 2020
Starts at 2020-11-16 21:34:13
Command Line  : -cp cpTest -rg ashbu -tag Prog=Test Space -action add_free
Tag Key       : Prog
Tag Value     : Test Space
Tenant Name   : TestTenant
Tenant Id     : ocid1.tenancy.oc1..aaaaaaaaxtkkpxc5qwgpwx7y2wt5pinegyzea4uacnmck7ixxxxxx


Processing Regions...

Region us-ashburn-1...
    Compartment cpTest
        Instances              - 2     Tag Added = 2         Tag Exist = 0
        Boot Volumes           - 2     Tag Added = 2         Tag Exist = 0
        Boot Volumes Backups   - 22    Tag Added = 22        Tag Exist = 0
        Block Volumes          - 1     Tag Added = 1         Tag Exist = 0
        Block Volumes Backups  - (-)
        Volume Groups          - (-)
        Volume Groups Backup   - (-)
        Network VCNs           - 2     Tag Added = 2         Tag Exist = 0
        Network Subnets        - 3     Tag Added = 3         Tag Exist = 0
        Network CPEs           - (-)
        Network DHCPs          - 2     Tag Added = 2         Tag Exist = 0
        Network IGWs           - 1     Tag Added = 1         Tag Exist = 0
        Network IPSECs         - (-)
        Network LPGs           - 2     Tag Added = 2         Tag Exist = 0
        Network NATGWs         - 2     Tag Added = 2         Tag Exist = 0
        Network NSGs           - 2     Tag Added = 2         Tag Exist = 0
        Network RPGs           - 1     Tag Added = 1         Tag Exist = 0
        Network Routes         - 4     Tag Added = 4         Tag Exist = 0
        Network SLs            - 2     Tag Added = 2         Tag Exist = 0
        Network SGWs           - 1     Tag Added = 1         Tag Exist = 0
        Network VCircuit       - (-)
        Load Balancers         - 1     Tag Added = 1         Tag Exist = 0
        DB DB Systems          - (-)
        DB Autonomous          - 1     Tag Added = 1         Tag Exist = 0
        Object Storage Buckets - 5     Tag Added = 5         Tag Exist = 0

##########################################################################################
#                                     Output as List                                     #
##########################################################################################
us-ashburn-1 | cpTest    | Instances              | adiwin               | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Instances              | adiwork              | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Boot Volumes           | adiwin (Boot Volume) | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Boot Volumes           | adiwork (Boot Volume)| Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Block Volumes          | adiwork-100g         | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network VCNs           | vcnspoke             | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network VCNs           | vcn                  | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network Subnets        | privsubspoke         | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network Subnets        | privsub              | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network Subnets        | pubsub               | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network IGWs           | igw                  | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network LPGs           | hubtospoke           | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network LPGs           | spoketohub           | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network NATGWs         | nat                  | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network NATGWs         | NATGW                | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network NSGs           | port80only           | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network NSGs           | vcn_nsg              | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network RPGs           | null                 | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network Routes         | route.lpg            | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Network SGWs           | sgw                  | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Load Balancers         | lb                   | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | DB Autonomous          | ADI_USAGE_19C        | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Object Storage Buckets | AuditBucket          | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Object Storage Buckets | FlowLogs             | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Object Storage Buckets | shared               | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Object Storage Buckets | test_restore         | Added   | Prog=Test Space 
us-ashburn-1 | cpTest    | Object Storage Buckets | usage_cost_bucket    | Added   | Prog=Test Space 

##########################################################################################
#                            Completed at 2020-11-16 21:34:45                            #
##########################################################################################


```
