# showoci
# README.md, last updated 3/13/2019
### Oracle Cloud Infrastructure Reporting Tool

##### Generate OCI resources of your tenancy using Python OCI SDK  

##### Modules Included:  
- oci.core.VirtualNetworkClient          
- oci.core.ComputeClient                 
- oci.core.ComputeManagementClient       
- oci.core.BlockstorageClient            
- oci.file_storage.FileStorageClient     
- oci.object_storage.ObjectStorageClient 
- oci.database.DatabaseClient            
- oci.identity.IdentityClient            
- oci.load_balancer.LoadBalancerClient   
- oci.email.EmailClient                  
- oci.key_management.KmsVaultClient    

##### Required OCI IAM user with read only privileges:  
##### Inspect privilege will have some limitations especially on object storage sizes
```
ALLOW GROUP ReadOnlyUsers to read all-resources IN TENANCY  
```
##### ** DISCLAIMER – This is not official Oracle application

## Installation Guide for Python 3.7.2 with OCI SDK  

### Installation on Windows  

Download Python 3.7.2 - https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe  

```
setup.exe
pip install oci oci-cli  
```
### Installation on Mac using Brew
```
brew install python3
pip3 install oci oci-cli 
```

### Installation on OCI VM with Oracle Linux 7  

##### Login as opc and install python3 locally  
```
sudo yum -y install gcc libffi-devel openssl-devel python-devel sqlite-devel 
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz  
tar zxf Python-3.7.2.tgz  
cd Python-3.7.2
./configure --prefix=$HOME/python --enable-loadable-sqlite-extensions  
make  
make install  
cd $HOME  
```

##### Add python to path  
```
echo 'export PATH=$HOME/python/bin:$PATH' >> ~/.bash_profile  
echo 'export PYTHONPATH=$HOME/python' >> ~/.bash_profile  
source ~/.bash_profile  
```

##### Check  
```
which python3  
```

##### install oci and oci-cli  
```
pip3 install --upgrade pip  
pip3 install oci oci-cli  
```

## Setup OCI CLI connectivity  

##### Cloud: login to your OCI Cloud
```  
1. Create new group : ReadOnlyGroup  
2. Create new Policy: ReadOnlyGroupPolicy with Statement - ALLOW GROUP ReadOnlyGroup to read all-resources IN TENANCY  
3. Create new User  : readonly.user -> Add to ReadOnlyGroup group  
```

#### Config OCI  
##### Unix: Login as opc
```  
oci setup config  
--> config location - /home/opc/.oci/config  
--> Enter a user OCID - copy from the created user   
--> Enter a tenancy OCID - copy from the oci cloud  
--> Region - choose the main region  
--> Do you want to generate a new RSA key pair? Y  

Copy the /home/opc/.oci/oci_api_key_public.pem and add it to the OCI User under API Key  
```

##### Test it:  
```
$ oci os ns get  
{  
  "data": "tenant_name_xxx"  
}  
```

Download the showoci.py from this project  

##### Execute  

```
$ ./showoci.py  

usage: showoci [-h] [-a] [-ani] [-n] [-i] [-c] [-o] [-l] [-k] [-d] [-f] [-e]
               [-so] [-mc] [-nr] [-t PROFILE] [-p PROXY] [-rg REGION]
               [-cp COMPART] [-cf CONFIG] [-jf JOUTFILE] [-js] [--version]

optional arguments:
  -h, --help    show this help message and exit
  -a            Print All Resources
  -ani          Print All Resources but identity
  -n            Print Network
  -i            Print Identity
  -c            Print Compute
  -o            Print Object Storage
  -l            Print Load Balancer
  -k            Print Key Management
  -d            Print Database
  -f            Print File Storage
  -e            Print EMail
  -so           Print Summary Only
  -mc           Include ManagedCompartmentForPaaS
  -nr           Not include root compartment
  -t PROFILE    Config file section to use (tenancy profile)
  -p PROXY      Set Proxy (i.e. www-proxy-server:80)
  -rg REGION    Filter by Region
  -cp COMPART   Filter by Compartment
  -cf CONFIG    Config File, default=~/.oci/config
  -jf JOUTFILE  Output to file (JSON format)
  -js           Output to screen (JSON format)
  --version     show program's version number and exit

```

## Below example of reports from few tenancies  

```
############################################################
#                  Start Extracting Data                   #
############################################################
Extracting Identity
    Tenancy...
    Users...
    Groups...
    Dynamic Groups...
    Policies...
    Providers...

Extracting Region us-ashburn-1
    Compartment gse00015259 (root)...
    Compartment Adi...
    Compartment Adi / Dev...
    Compartment Adi / Dev / DevA...
    Compartment Adi / Dev / DevB...
    Compartment Adi / Prod...
    Compartment NetworkCompartment...

Extracting Region us-phoenix-1
    Compartment gse00015259 (root)...
    Compartment Adi...
    Compartment Adi / Dev...
    Compartment Adi / Dev / DevA...
    Compartment Adi / Dev / DevB...
    Compartment Adi / Prod...
    Compartment NetworkCompartment...

############################################################
#                         Tenancy                          #
############################################################
Name        - CUST
OCID        - ocid1.tenancy.oc1..aaaaaaaae5u57gqxs5qas5f33qnge63sdoi7s2ji6bk5slscblmxxxxxxx
Home Region - IAD
Subs Region - us-ashburn-1, us-phoenix-1

##############################
#           Users            #
##############################
--> adi.zohar
    Keys   = API = 0  Tokens = 0  Secret = 0  Swift = 0  SMTP  = 0
    Groups = Administrators 

--> adi_ocicli
    Keys   = API = 1  Tokens = 1  Secret = 0  Swift = 1  SMTP  = 0
    Groups = Administrators 

--> adi_terraform
    Keys   = API = 1  Tokens = 1  Secret = 1  Swift = 1  SMTP  = 1
    Groups = Administrators 

##############################
#           Groups           #
##############################
--> Administrators       : adi.zohar  
--> DBAdmin              : 
--> demousers            : api.user  
--> ObjectAdmins         : pocuser  
--> ReadOnlyUsers        : 


##############################
#       Dynamic Groups       #
##############################
--> AdiDynamicGroup
    Desc      :Description
    Rules     :any {ALL {instance.compartment.id = 'Demo'}}

##############################
#          Policies          #
##############################

Compartment Demo:

--> Demo
    Allow group demousers to manage all-resources in compartment Demo
      Allow service PSM to inspect vcns in compartment Demo
      Allow service PSM to use subnets in compartment Demo
      Allow service PSM to use vnics in compartment Demo
      Allow service PSM to manage security-lists in compartment Demo

Compartment gse00000000 (root):

--> ObjectPolicy:
    Allow group ObjectAdmins to manage buckets in tenancy
    Allow group ObjectAdmins to manage objects in tenancy

--> ReadOnlyPolicy:
    ALLOW GROUP ReadOnlyUsers to read all-resources IN TENANCY

--> Tenant Admin Policy:
    ALLOW GROUP Administrators to manage all-resources IN TENANCY

##############################
#     identity providers     #
##############################
--> OracleIdentityCloudService
    Desc      :Oracle identity cloud service added during account creation
    Type      :IDCS
    Protocol  :SAML2
    Redirect  :https://idcs-7520d863a50f4e9ca469bcxxxxxxxxx.identity.oraclecloud.com/fed/v1/idp/sso
    Metadata  :https://idcs-7520d863a50f4e9ca469bxxxxxxxxxx.identity.oraclecloud.com
    Group Map :DemoUsers <-> demousers
    Group Map :OCI_Administrators <-> Administrators

##########################################################################################
#                                  Region us-ashburn-1                                   #
##########################################################################################

############################################################
#              Compartment gse00015259 (root)              #
############################################################

##############################
#       Object Storage       #
##############################
--> AACBucket            -        2 Objs ,     0.00gb
--> ADIDB_Backup         -        0 Objs ,     0.00gb
--> DBaaSBackup          -      132 Objs ,     1.20gb
--> TestBucket1          -        0 Objs ,     0.00gb , 2 Preauth Requests
--> TestBucket2          -        0 Objs ,     0.00gb

##############################
#           EMails           #
##############################
--> Suppression List:
    suppression@oracle.com - MANUAL
    noreply@oracle.com - MANUAL

############################################################
#                   Compartment Network                    #
############################################################

##############################
#            VCNs            #
##############################
--> VCN    10.1.0.0/24 - vcn - vcn.oraclevcn.com
    Internet GW : igw
    Service GW  : sgw
    NAT GW      : NAT - 129.213.173.125 ( AVAILABLE )
    DRG Attached: drg + Remote Peering (1)
    Local Peer  : lpg - 10.2.0.0/24 - PEERED

    Subnet 10.1.0.0/26  fHBa:US-ASHBURN-AD-1 (Public)
        Name    : sub1
        DNS     : sub1
        DHCP    : Default DHCP Options for vcn
        Route   : Default Route Table for vcn
        Sec List: Default Security List for vcn

    Subnet 10.1.0.128/27  fHBa:US-ASHBURN-AD-2 (Public)
        Name    : sub2
        DNS     : sub2
        DHCP    : Default DHCP Options for vcn
        Route   : Default Route Table for vcn
        Sec List: Default Security List for vcn

    Sec List    : Default Security List for vcn
        Ingres  : Src: 0.0.0.0/0         TCP  Dst(22)
        Egres   : Dst: 0.0.0.0/0         ALL

    Route Table : Default Route Table for vcn
        Route   : DST:oci-iad-objectstorage --> servicegateway
        Route   : DST:0.0.0.0/0 --> internetgateway

    DHCP Options: Default DHCP Options for vcn
        DomainNameServer : VcnLocalPlusInternet
        SearchDomain     : vcn.oraclevcn.com

--> VCN    10.2.0.0/24 - vcnpeer - vcnpeer.oraclevcn.com
    Service GW  : sgw
    Local Peer  : lpgpeer - 10.1.0.0/24 - PEERED

    Subnet 10.2.0.0/26  fHBa:US-ASHBURN-AD-1 (Public)
        Name    : sub1
        DNS     : sub1
        DHCP    : Default DHCP Options for vcnpeer
        Route   : Default Route Table for vcnpeer
        Sec List: Default Security List for vcnpeer

    Sec List    : Default Security List for vcnpeer
        Ingres  : Src: 0.0.0.0/0         TCP  Dst(22)
        Ingres  : Src: 0.0.0.0/0         ICMP 4,3
        Ingres  : Src: 10.2.0.0/24       ICMP 3
        Egres   : Dst: 0.0.0.0/0         ALL

    DHCP Options: Default DHCP Options for vcnpeer
        DomainNameServer : VcnLocalPlusInternet
        SearchDomain     : vcnpeer.oraclevcn.com

##############################
#            DRGs            #
##############################
--> DRG    drg

##############################
#            CPEs            #
##############################
--> CPE    CUST GR CPE1 - 16.17.18.19
--> CPE    CUST GR CPE2 - 12.13.14.15

##############################
#           IPSec            #
##############################
--> IPSEC  : CUST GR VPN1
    DRG    : CUST Cloud DRG
    CPE    : CUST GR CPE1 - 100.200.100.200
    Tunnel : 16.17.18.19 UP
    Tunnel : 12.13.14.15 UP
    Routes : 0.0.0.0/0

##############################
#       Remote Peering       #
##############################
--> RPC    Id    : ocid1.remotepeeringconnection.oc1.iad.aaaaaaaavvulhrxdlmlnusfus67ilttz3qbyy4cucmck3o7rswll4x5azkha
           PeerId: ocid1.remotepeeringconnection.oc1.phx.aaaaaaaa6vbbgmamanroam4rn6hmdfsg6l3565v57fwhbu3qgply7w3ggqea
           Name  : AdiRemotePeer
           DRG   : drg
           Status: PEERED
           Region: us-phoenix-1

############################################################
#                    Compartment Oracle                    #
############################################################

##############################
#     Compute Instances      #
##############################
--> CUST TEST - VM.Standard2.1 - RUNNING
    AD  : cWKV:US-ASHBURN-AD-2
    Img : Oracle-Linux-7.5-2018.06.14-0
    Boot: 47gb - CUST TEST (Boot Volume)  (AVAILABLE)
    Vol : 100gb - VM001_2nd_100Cold  (AVAILABLE)
    Vol : 100gb - VM002_DATA_100  (AVAILABLE) Backup=bronze 
    Vnic: 10.99.3.2 (Priv), None (Pub)  - Primary

--> OCLSVM001 - VM.Standard2.2 - RUNNING
    AD  : cWKV:US-ASHBURN-AD-2
    Img : Oracle-Linux-7.5-2018.06.14-0
    Boot: 47gb - OCLSVM001 (Boot Volume)  (AVAILABLE)
    Vol : 100gb - VM001_DATA_100  (AVAILABLE)
    Vol : 150gb - VM001_FRM_150  (AVAILABLE)
    Vnic: 10.99.3.4 (Priv), None (Pub)  - Primary

--> OCLSVR2 - VM.Standard2.2 - RUNNING
    AD  : cWKV:US-ASHBURN-AD-2
    Img : Windows-Server-2012-R2-Standard-Edition-VM-Gen2-2018.05.21-0
    Boot: 256gb - dr2no (Boot Volume)  (AVAILABLE)
    Vol : 150gb - dr2noBV1  (AVAILABLE)
    Vnic: 172.27.130.2 (Priv), 129.146.165.108 (Pub)  - Primary

##############################
# Compute Inst Configuration #
##############################
AdiInstanceConfig - VM.Standard2.1
InstanceConfig - VM.Standard1.1

##############################
#   Compute Instance Pool    #
##############################
Adi-Instance-Pool - RUNNING - Size: 1

##############################
#   Compute Custom Images    #
##############################
--> AdiZoharImage - Oracle Linux - 47gb - Base:  Oracle-Linux-7.5-2018.06.14-0

##############################
#    Boot Volume Backups     #
##############################
--> demohost (Boot Volume), FULL, MANUAL, 2018-07-25 03:12 - None
        Name : demohost_backup
        Size : 47gb , Stored 14gb
--> demohost (Boot Volume), INCREMENTAL, SCHEDULED, 2018-08-01 16:27 - 2019-08-01 23:07
        Name : Auto-backup for 2018-08-01 04:00:00 via policy: bronze
        Size : 47gb , Stored 1gb
--> demohost (Boot Volume), INCREMENTAL, SCHEDULED, 2018-09-01 07:50 - 2019-09-01 14:30
        Name : Auto-backup for 2018-09-01 04:00:00 via policy: bronze
        Size : 47gb , Stored 1gb
--> demohost (Boot Volume), INCREMENTAL, SCHEDULED, 2018-10-01 09:02 - 2019-10-01 15:42
        Name : Auto-backup for 2018-10-01 04:00:00 via policy: bronze
        Size : 47gb , Stored 1gb
--> demohost (Boot Volume), INCREMENTAL, SCHEDULED, 2018-11-01 09:07 - 2019-11-01 15:47
        Name : Auto-backup for 2018-11-01 04:00:00 via policy: bronze
        Size : 47gb , Stored 10gb

##############################
#    Block Volume Backups    #
##############################
--> Adi_50G, FULL, MANUAL, 2018-10-22 02:52 - None
        Name : Adi_Backup_50G
        Size : 50gb , Stored 1gb
--> Adi_50G, INCREMENTAL, SCHEDULED, 2018-11-01 04:40 - 2019-11-01 11:20
        Name : Auto-backup for 2018-11-01 04:00:00 via policy: bronze
        Size : 50gb , Stored 1gb

##############################
#         Databases          #
##############################
--> ADIDB02 - VM.Standard1.1 - AVAILABLE
    AD      : fHBa:US-ASHBURN-AD-3
    Cores   : 1
    Nodes   : 1
    Version : 18.3.0.0.180717 - ENTERPRISE_EDITION_EXTREME_PERFORMANCE - BRING_YOUR_OWN_LICENSE
    Host    : dbhost
    Domain  : sub3.vcn.oraclevcn.com
    Data    : 256gb - 80%
    DataSub : 10.1.0.192/27  sub3 (Public)
    Scan DNS: ocid1.vcndnsrecord.oc1.iad.abuwcljszsvrzlpytvykn4oqoskub6qqebk4wkpkesfa7gdgvf2nomqyrclq
    Port    : 1521
    Patches : Jul 2018 18c Db System patch - 18.3.0.0.180717 - 2018-07-30 - Last Action: APPLY
    Node    : dbhost - AVAILABLE - 10.1.0.196 (Priv) , 129.213.32.183 (Pub) , Subnet sub3
    Home    : dbhome20181026162225 - 18.2.0.0.180417
         PT : Apr 2018 18c Database patch - 18.2.0.0.180417 - 2018-04-25 - Last Action: None
         PT : Jul 2018 18c Database patch - 18.3.0.0.180717 - 2018-07-30 - Last Action: None
         DB : ADIDB02 - ADIDB02_iad3n9 - OLTP - AL32UTF8 - AVAILABLE - AutoBck=Y
                  Automatic Backup - INCREMENTAL - FAILED - 2018-11-02 05:25 - 2018-11-02 05:39 - None
                  Automatic Backup - INCREMENTAL - ACTIVE - 2018-11-01 05:25 - 2018-11-01 05:39 - 3.5gb
                  Automatic Backup - INCREMENTAL - ACTIVE - 2018-10-31 05:25 - 2018-10-31 05:46 - 3.5gb
                  Automatic Backup - INCREMENTAL - ACTIVE - 2018-10-30 05:24 - 2018-10-30 05:30 - 3.4gb
                  Automatic Backup - INCREMENTAL - ACTIVE - 2018-10-29 05:26 - 2018-10-29 05:34 - 3.3gb
                  Automatic Backup - INCREMENTAL - ACTIVE - 2018-10-28 05:25 - 2018-10-28 05:34 - 3.2gb
                  Automatic Backup - INCREMENTAL - ACTIVE - 2018-10-27 05:25 - 2018-10-27 05:46 - 3.0gb

--> npappdb - BM.DenseIO1.36 - AVAILABLE
    AD      : iQAs:US-ASHBURN-AD-2
    Cores   : 4
    Version : 12.2.0.1.180116 - ENTERPRISE_EDITION_HIGH_PERFORMANCE - LICENSE_INCLUDED
    Host    : npappdb
    Domain  : dbnp.phxvcn.oraclevcn.com
    Data(gb): None - 80%
    DataSub : 172.27.131.128/26  DBNP (Public)
    Port    : 1521
    Node    : npappdb - AVAILABLE - 172.27.131.130 (Priv), 129.146.127.159 (Pub)  - Primary
    Home 1  : 12.1.0.2             - OraDB12102_home3
            : cnvcdb - cnvcdb - cnvcdbDEFAULTPDB - DSS - US7ASCII - AVAILABLE - AutoBck=N
    Home 2  : 12.1.0.2.180116      - npappdb-dbhome01
            : gldcdb - gldcdb_phx2vp - None - OLTP - AL32UTF8 - AVAILABLE - AutoBck=N
    Home 3  : 12.1.0.2             - OraDB12102_home10
            : qualcdb - qualcdb - qualcdbDEFAULTPDB - OLTP - US7ASCII - AVAILABLE - AutoBck=N

--> npdb - Exadata.Half2.184 - AVAILABLE
    AD      : qFAY:US-ASHBURN-AD-1
    Cores   : 184
    Version : 18.0.0.0.0 - ENTERPRISE_EDITION_EXTREME_PERFORMANCE - BRING_YOUR_OWN_LICENSE
    Host    : dbnp-lg255
    Domain  : db.vnp.oraclevcn.com
    Cluster : crs
    Data(gb): None - 80%
    DataSub : 10.90.2.0/26  db (Private)
    BackSub : 10.90.2.64/26  dbback (Private)
    Scan Ips: 10.90.2.10 - dbnp-lg255-scan-0
    Scan Ips: 10.90.2.11 - dbnp-lg255-scan-1
    Scan Ips: 10.90.2.12 - dbnp-lg255-scan-2
    VIP Ids : 10.90.2.6 - dbnp-lg2551-vip
    VIP Ids : 10.90.2.7 - dbnp-lg2552-vip
    VIP Ids : 10.90.2.8 - dbnp-lg2553-vip
    VIP Ids : 10.90.2.9 - dbnp-lg2554-vip
    Port    : 1521
    Node 1  : dbnp-lg2551 - AVAILABLE - 10.90.2.2 (Priv), None (Pub)  - Primary
    Node 2  : dbnp-lg2553 - AVAILABLE - 10.90.2.4 (Priv), None (Pub)  - Primary
    Node 3  : dbnp-lg2554 - AVAILABLE - 10.90.2.5 (Priv), None (Pub)  - Primary
    Node 4  : dbnp-lg2552 - AVAILABLE - 10.90.2.3 (Priv), None (Pub)  - Primary
    Home 1  : 11.2.0.4 - dbhome20180703145724
            : OADEV - OADEV_iad1g9 - None - OLTP - AL32UTF8 - AVAILABLE - AutoBck=N
    Home 2  : 18.0.0.0 - dbhome20180702145427
            : db18 - db18_iad1z4 - None - OLTP - AL32UTF8 - AVAILABLE - AutoBck=N


##############################
#       Object Storage       #
##############################
--> AdiTest              -        1 Objs ,     0.00gb , LifeCycle: LifecycleRule, ARCHIVE, 30 DAYS

##############################
#        File Storage        #
##############################
--> fs-9846 - cWKV:US-ASHBURN-AD-1 - ACTIVE - 0.0gb metered
    Export    : /fss/OracleBackup - ACTIVE
    Export Set: OracleBackup - export set - cWKV:US-ASHBURN-AD-1 - ACTIVE
    Mount     : OracleBackup - Subnet: 10.99.2.0/24  Production (Private) ACTIVE
    Mount IP  : 10.99.2.4 - privateip20180719175445

##############################
#       Load Balancers       #
##############################
--> Name       : cnvlb - 100Mbps - (Private) - ACTIVE
    Status     : OK
    Subnet     : 172.27.131.0/25  EBSNP (Public)
    IP         : 172.27.131.13 - Private
    Listener   : cnvappl - 8010/HTTP
    Listener   : cvnappl1 - 80/HTTP
    Hostname   : cnvapph - cnvapp
    backendSet : cnvlbbs - ROUND_ROBIN
        Status : OK
        Backend: OK - 172.27.131.6:8000 - Backup=N, Drain=N, Offline=N, Weight=1
        Backend: OK - 172.27.131.5:8000 - Backup=N, Drain=N, Offline=N, Weight=1
        H.Chk  : interval(ms)=10000, Timeout(ms)=3000, 8000/HTTP, 
        H.Chk  : retries=3, Code=200, RegEx=.*, url_path =/index.html
        Cookie : cnvebslb, disable_fallback=N

--> Name       : PublicLB_DS - 100Mbps - (Public) - ACTIVE
    Status     : CRITICAL
    Subnet     : 10.0.4.0/24  LB_SUBNET1 (Public)
    Subnet     : 10.0.5.0/24  LB_SUBNET2 (Public)
    IP         : 10.20.30.40 - Public
    Listener   : LB_Listener - 80/HTTP
    backendSet : Backend_Webservers - ROUND_ROBIN
        Status : CRITICAL
        Backend: CRITICAL - 10.0.0.2:80 - Backup=N, Drain=N, Offline=N, Weight=1
        Backend: CRITICAL - 10.0.1.2:80 - Backup=N, Drain=N, Offline=N, Weight=1
        H.Chk  : interval(ms)=10000, Timeout(ms)=3000, 80/HTTP,
        H.Chk  : retries=3, Code=200, RegEx=.*, url_path =/

##############################
#           E-Mail           #
##############################
--> Approved Senders:
    adi.test@abc.com - ACTIVE
    adi.zohar@efg.com - ACTIVE
    
##############################
#    Resource Management     #
##############################
--> StackSimpleVCN - Sub Compartment and VCN Creation
    ormjob20190303213446 - DESTROY    - SUCCEEDED  - 2019-03-04 02:39
    ormjob20190303212919 - APPLY      - SUCCEEDED  - 2019-03-04 02:33
    ormjob20190303211757 - PLAN       - SUCCEEDED  - 2019-03-04 02:21

##########################################################################################
#                                 Summary - us-ashburn-1                                 #
##########################################################################################

###########################################################################
#                      Summary - Compartment generic                      #
###########################################################################
Compute - Block Storage (gb)          -       3547
Compute - VM.Standard1.1              -          1
Compute - VM.Standard2.1              -          7
Compute - VM.Standard2.4              -          1
Object Storage - BV Backups (gb)      -       1276
Object Storage - Buckets (gb)         -        216

###########################################################################
#                        Summary - Compartment npdb                       #
###########################################################################
Database - Exadata.Half2.184          -          1
Object Storage - Buckets (gb)         -       6152

###########################################################################
#                       Summary - Compartment npebs                       #
###########################################################################
Compute - Block Storage (gb)          -      14121
Compute - VM.Standard2.1              -         16
Compute - VM.Standard2.2              -         28
Compute - VM.Standard2.4              -          6
Compute - VM.Standard2.8              -          5
File Storage (gb)                     -       2617
Load Balancer 100Mbps                 -         10
Object Storage - BV Backups (gb)      -       2806
Object Storage - Images (gb)          -       1862

##########################################################################################
#                                     Summary Total                                      #
##########################################################################################
Compute - Block Storage (gb)          -      17668
Compute - VM.Standard1.1              -          1
Compute - VM.Standard2.1              -         23
Compute - VM.Standard2.2              -         28
Compute - VM.Standard2.4              -          7
Compute - VM.Standard2.8              -          5
Database - Exadata.Half2.184          -          1
File Storage (gb)                     -       2617
Load Balancer 100Mbps                 -         10
Object Storage - BV Backups (gb)      -       4082
Object Storage - Buckets (gb)         -       6368
Object Storage - Images (gb)          -       1862
```
  

