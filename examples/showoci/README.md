# showoci
##### README.md, last updated 4/2/2019
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
- oci.container_engine.ContainerEngineClient

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

### Installation on OCI VM with Oracle Cloud Developer Image
##### All Installed, just run the config below

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

############################################################
#                        showoci.py                        #
############################################################
Config File    : ~/.oci/config
Config Profile : adi
Version        : 19.4.2
Date/Time      : 2019-04-03 00:00:04
Comand Line    : -t adi -a
OCI SDK Ver    : 2.2.1

############################################################
#                 Load OCI data to Memory                  #
############################################################
Load Guide - '.' Compartment, '+' VCN, '-' Subnets

Identity...
--> Tenancy                  <--  (1) - 0 sec
--> Compartments             <--  (12) - 0 sec

##############################
#    Region us-ashburn-1     #
##############################
Identity...
--> Availability Domains     <--  (3) - 0 sec

Network...
--> Virtual Cloud Networks   <-- ............ (5) - 1 sec
--> Subnets                  <-- +++++ (54) - 7 sec
--> Service Gateways         <-- ............ (1) - 1 sec
--> NAT Gateways             <-- ............ (0) - 0 sec
--> Dynamic Routing GWs      <-- ............ (3) - 2 sec
--> Dynamic Routing GW Attch <-- ............ (3) - 1 sec
--> Customer Prem Equipments <-- ............ (1) - 1 sec
--> IPSEC tunnels            <-- ............ (0) - 1 sec
--> Remote Peer Conns        <-- ............ (1) - 1 sec
--> Virtual Circuits         <-- ............ (2) - 1 sec
--> Internet Gateways        <-- +++++ (3) - 4 sec
--> Local Peer GWs           <-- +++++ (0) - 5 sec
--> Security Lists           <-- +++++ (61) - 5 sec
--> DHCP Options             <-- +++++ (8) - 5 sec
--> Route Tables             <-- +++++ (66) - 6 sec
--> Routed Private IPs       <--  (0) - 0 sec

Compute...
--> Instances                <-- ............ (146) - 21 sec
--> Images                   <-- ............ (33) - 5 sec
--> Boot Volumes Attached    <-- ............ (146) - 5 sec
--> Volumes Attached         <-- ............ (120) - 8 sec
--> Vnics Attached           <-- ............ (146) - 22 sec
--> Instance Configurations  <-- ............ (0) - 1 sec
--> Instance Pools           <-- ............ (0) - 1 sec

Block Storage...
--> Block Volume Groups      <-- ............ (0) - 1 sec
--> Boot Volumes             <-- ............ (157) - 13 sec
--> Boot Volumes Backups     <-- ............ (7) - 1 sec
--> Block Volumes            <-- ............ (164) - 15 sec
--> Block Volumes Backups    <--  (344) - 1 sec

Database...
--> DB Systems               <-- ............ (3) - 17 sec
--> Autonomous Databases     <-- ............ (0) - 4 sec

Load Balancer...
--> Load Balancers           <-- ............ (18) - 5 sec
--> Backend Sets             <-- LLLLLLLLLLLL (26) - 49 sec

Object Storage...
--> Buckets                  <-- ............ (4) - 3 sec

File Storage...
--> File Systems             <-- ............ (5) - 1 sec
--> Exports                  <-- ............ (8) - 0 sec
--> Mount Targets            <-- ............ (7) - 2 sec

Email Notifications...
--> Senders                  <-- ............ (0) - 21 sec
--> Suppressions             <-- ............ (0) - 2 sec

Resource Management...
--> Stacks                   <-- ............ (0) - 2 sec


############################################################
#                  Start Processing Data                   #
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
    Groups = Administrators 

--> adi_ocicli
    Groups = Administrators 

--> adi_terraform
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
--> RPC    Name  : AdiRemotePeer
           DRG   : drg
           Status: PEERED
		   Peer  : PhxRemotePeer - us-phoenix-1

############################################################
#                    Compartment Oracle                    #
############################################################

##############################
#     Compute Instances      #
##############################

--> VM.Standard1.1 - demohost - RUNNING
        AD  : fHBa:US-ASHBURN-AD-1 - FAULT-DOMAIN-2
        Img : Oracle-Linux-7.5-2018.06.14-0
        Boot: 47gb - demohost (Boot Volume) bronze  - Group AdiVol1
        VNIC: 10.1.0.2 (Prv), 129.213.148.40 (Pub) - Primary , Subnet (sub1 10.1.0.0/26), VCN (vcn)
        Console Connection Active

--> VM.Standard2.1 - inst-hari6-Adi-Instance-Pool - RUNNING
        AD  : fHBa:US-ASHBURN-AD-3 - FAULT-DOMAIN-3
        Img : Oracle-Linux-7.5-2018.10.16-0
        Boot: 47gb - inst-hari6-Adi-Instance-Pool (Boot Volume) 
        VNIC: 10.1.0.204 (Prv), 129.213.110.160 (Pub) - Primary , Subnet (sub3 10.1.0.192/27), VCN (vcn)

##############################
# Compute Inst Configuration #
##############################

--> AdiInstanceConfig
        Shape : VM.Standard2.1
        Image : Oracle-Linux-7.5-2018.10.16-0

--> InstanceConfig
        Shape : VM.Standard1.1
        Image : Oracle-Linux-7.5-2018.06.14-0


##############################
#   Compute Instance Pool    #
##############################
--> Adi-Instance-Pool - RUNNING - Size: 1
        ADs   : fHBa:US-ASHBURN-AD-3, fHBa:US-ASHBURN-AD-2
        Config: AdiInstanceConfig - VM.Standard2.1

##############################
#   Compute Custom Images    #
##############################
--> adi_custom_image1 - Oracle Linux - 47gb - Base:  Oracle-Linux-7.4-2018.01.10-0
--> adi_custom_image2 - Oracle Linux - 47gb - Base:  Oracle-Linux-7.4-2018.01.10-0

##############################
#  Block Boot Not Attached   #
##############################
--> 47gb    - BOOTNOTATT (Boot Volume)  - jjZD:US-ASHBURN-AD-3 - 2018-07-09 16:21

##############################
#    Boot Volume Backups     #
##############################
--> demohost (Boot Volume),  - Auto-backup for 2018-08-01 04:00:00 via policy: bronze
        Type : INCREMENTAL, SCHEDULED, 2018-08-01 16:27 -> 2019-08-01 23:07
        Size : 47gb , Stored 1gb
--> demohost (Boot Volume),  - Auto-backup for 2018-09-01 04:00:00 via policy: bronze
        Type : INCREMENTAL, SCHEDULED, 2018-09-01 07:50 -> 2019-09-01 14:30
        Size : 47gb , Stored 1gb

##############################
#    Block Volume Backups    #
##############################
--> Adi_50G ( Source TERMINATED ) - Adi_Backup_50G
        Type : FULL, MANUAL, 2018-10-22 02:52 -> Keep
        Size : 50gb , Stored 1gb
--> Adi_50G ( Source TERMINATED ) - Auto-backup for 2018-11-01 04:00:00 via policy: bronze
        Type : INCREMENTAL, SCHEDULED, 2018-11-01 04:40 -> 2019-11-01 11:20
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
    Export Set: OracleBackup - export set - cWKV:US-ASHBURN-AD-1 - VCN (vcn)
    Mount     : OracleBackup - Subnet: 10.99.2.0/24  Production (Private) , VCN (vcn)
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

##############################
#         Containers         #
##############################
--> INFA1 - ACTIVE - v1.11.5
    VCN   : 10.0.0.0/16 - oke-vcn-quick-INFA1-20190306173914 - infa1.oraclevcn.com
    Node  : pool1 - Oracle-Linux-7.5 - VM.Standard2.1
            oke-subnet-quick-INFA1-20190306173914-dKrR:US-ASHBURN-AD-2 10.0.11.0/24, VCN (oke-vcn-quick-INFA1-20190306173914)
            oke-subnet-quick-INFA1-20190306173914-dKrR:US-ASHBURN-AD-1 10.0.10.0/24, VCN (oke-vcn-quick-INFA1-20190306173914)
            oke-subnet-quick-INFA1-20190306173914-dKrR:US-ASHBURN-AD-3 10.0.12.0/24, VCN (oke-vcn-quick-INFA1-20190306173914)

--> K8S Cluster - ACTIVE - v1.11.5
    VCN   : 10.0.0.0/16 - oke-vcn-quick-K8S Cluster-20190306130828 - k8scluster.oraclevcn.com
    Node  : pool1 - Oracle-Linux-7.5 - VM.Standard2.1
            oke-subnet-quick-K8S Cluster-20190306130828-dKrR:US-ASHBURN-AD-3 10.0.12.0/24, VCN (oke-vcn-quick-K8S Cluster-20190306130828)
            oke-subnet-quick-K8S Cluster-20190306130828-dKrR:US-ASHBURN-AD-2 10.0.11.0/24, VCN (oke-vcn-quick-K8S Cluster-20190306130828)
            oke-subnet-quick-K8S Cluster-20190306130828-dKrR:US-ASHBURN-AD-1 10.0.10.0/24, VCN (oke-vcn-quick-K8S Cluster-20190306130828)
			
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
  
## Below example JSON report on us-ashburn-1 region, compartment Adi without identity 

```

> showoci -t gse00015259 -ani -js -rg us-ashburn-1 -cp Adi

############################################################
#                        showoci.py                        #
############################################################
Config File    : ~/.oci/config
Config Profile : gse00015259
Version        : 19.4.2
Date/Time      : 2019-04-05 08:14:53
Comand Line    : -t gse00015259 -ani -js -rg us-ashburn-1 -cp Adi
OCI SDK Ver    : 2.2.1


############################################################
#                 Load OCI data to Memory                  #
############################################################
Load Guide - '.' Compartment, '+' VCN, '-' Subnets
Filtered by Region      = us-ashburn-1
Filtered by Compartment = Adi

Identity...
--> Tenancy                  <--  (1) - 0 sec
--> Compartments             <--  (1) - 0 sec


##############################
#    Region us-ashburn-1     #
##############################
Identity...
--> Availability Domains     <--  (3) - 0 sec

Network...
--> Virtual Cloud Networks   <-- . (3) - 0 sec
--> Subnets                  <-- +++ (6) - 0 sec
--> Service Gateways         <-- . (2) - 0 sec
--> NAT Gateways             <-- . (1) - 0 sec
--> Dynamic Routing GWs      <-- . (2) - 0 sec
--> Dynamic Routing GW Attch <-- . (2) - 0 sec
--> Customer Prem Equipments <-- . (0) - 0 sec
--> IPSEC tunnels            <-- . (0) - 0 sec
--> Remote Peer Conns        <-- . (1) - 0 sec
--> Virtual Circuits         <-- . (0) - 0 sec
--> Internet Gateways        <-- +++ (3) - 0 sec
--> Local Peer GWs           <-- +++ (2) - 0 sec
--> Security Lists           <-- +++ (3) - 0 sec
--> DHCP Options             <-- +++ (3) - 0 sec
--> Route Tables             <-- +++ (6) - 0 sec
--> Routed Private IPs       <--  (0) - 0 sec

Compute...
--> Instances                <-- . (3) - 2 sec
--> Images                   <-- . (1) - 0 sec
--> Boot Volumes Attached    <-- . (3) - 0 sec
--> Volumes Attached         <-- . (0) - 0 sec
--> Vnics Attached           <-- . (3) - 6 sec
--> Instance Configurations  <-- . (2) - 0 sec
--> Instance Pools           <-- . (1) - 0 sec

Block Storage...
--> Block Volume Groups      <-- . (1) - 0 sec
--> Boot Volumes             <-- . (8) - 1 sec
--> Boot Volumes Backups     <-- . (11) - 0 sec
--> Block Volumes            <-- . (2) - 0 sec
--> Block Volumes Backups    <--  (6) - 0 sec

Database...
--> DB Systems               <-- . (2) - 5 sec
--> Autonomous Databases     <-- . (0) - 1 sec

Load Balancer...
--> Load Balancers           <-- . (1) - 0 sec
--> Backend Sets             <-- L (1) - 0 sec

Object Storage...
--> Buckets                  <-- . (2) - 0 sec

File Storage...
--> File Systems             <-- . (1) - 0 sec
--> Exports                  <-- . (1) - 0 sec
--> Mount Targets            <-- . (1) - 0 sec

Email Notifications...
--> Senders                  <-- . (1) - 2 sec
--> Suppressions             <-- . (0) - 0 sec

Resource Management...
--> Stacks                   <-- . (0) - 0 sec


############################################################
#                  Start Processing Data                   #
############################################################

Processing Region us-ashburn-1

Processing...
    Compartment Adi...

[
    {
        "type": "showoci",
        "data": {
            "program": "showoci.py",
            "author": "Adi Zohar",
            "config_file": "~/.oci/config",
            "config_profile": "gse00015259",
            "version": "19.4.2",
            "datetime": "2019-04-05 08:14:53",
            "cmdline": "-t gse00015259 -ani -js -rg us-ashburn-1 -cp Adi",
            "oci_sdk_version": "2.2.1"
        }
    },
    {
        "type": "region",
        "region": "us-ashburn-1",
        "data": [
            {
                "compartment": "Adi",
                "path": "Adi",
                "network": {
                    "vcn": [
                        {
                        {
                            "id": "ocid1.vcn.oc1.iad.aaaaaaaao2fz5lgsvyph2egdljbcb34p4ifsswl3hsiwbepczkq4rzornzgq",
                            "name": "10.1.0.0/24 - vcn - vcn.oraclevcn.com",
                            "compartment": "Adi",
                            "data": {
                                "igw": [
                                    {
                                        "id": "ocid1.internetgateway.oc1.iad.aaaaaaaapc4gu6wsmna3f6ttsujezjw76ayiuhznjrouy554r2nxe47ahimq",
                                        "name": "igw",
                                        "compartment": "Adi"
                                    }
                                ],
                                "sgw": [
                                    {
                                        "id": "ocid1.servicegateway.oc1.iad.aaaaaaaaybkhf6yqhhvxy4xtubf2ez4av2cyz7lpsjzllwlhozoeooltozva",
                                        "name": "sgw",
                                        "services": "OCI IAD Object Storage",
                                        "compartment": "Adi",
                                        "defined_tags": {},
                                        "freeform_tags": {}
                                    }
                                ],
                                "nat": [
                                    {
                                        "id": "ocid1.natgateway.oc1.iad.aaaaaaaa75umb5y5yldihawp7324xidataspcq4hdv746vpfzf5scygzamwq",
                                        "name": "NAT - 129.213.173.125",
                                        "compartment": "Adi",
                                        "defined_tags": {},
                                        "freeform_tags": {
                                            "ENV": "Dev"
                                        }
                                    }
                                ],
                                "drg_attached": [
                                    {
                                        "id": "ocid1.drgattachment.oc1.iad.aaaaaaaasfb4eaoxvglzhesefpb77spstqn5hn7a42gki2tgofjmqblmcfqa",
                                        "drg_id": "ocid1.drg.oc1.iad.aaaaaaaadnf4ljd7mxb2zsatdcai3xrwuo3kqqrcm6ad7e4iprmkiukkc56q",
                                        "name": "drg + Remote Peering (1) + Transit Route(TransitRoute)",
                                        "compartment": "Adi"
                                    }
                                ],
                                "local_peering": [
                                    {
                                        "id": "ocid1.localpeeringgateway.oc1.iad.aaaaaaaatjy2jbwm6kzmaame44lkitdgemam4ydvr43mdds7pmheur75powa",
                                        "name": "PEERED   - lpg - 10.2.0.0/24 + Transit Route(TransitLPGRoute)",
                                        "compartment": "Adi"
                                    }
                                ],
                                "subnets": [
                                    {
                                        "id": "ocid1.subnet.oc1.iad.aaaaaaaadtzjjq7s3byjaerrscksaqsbjv377rivwdneta5p3qyytbtvjjna",
                                        "subnet": "10.1.0.0/26  fHBa:US-ASHBURN-AD-1 (Public)",
                                        "name": "sub1",
                                        "dns": "sub1",
                                        "compartment": "Adi",
                                        "dhcp_options": "Default DHCP Options for vcn",
                                        "security_list": [
                                            "Default Security List for vcn"
                                        ],
                                        "route": "Default Route Table for vcn",
                                        "defined_tags": {},
                                        "freeform_tags": {}
                                    },
                                    {
                                        "id": "ocid1.subnet.oc1.iad.aaaaaaaawirhmbaj37wnknc3oomapllkqawlfgihh3u47dux56n4mjst7mmq",
                                        "subnet": "10.1.0.128/27  fHBa:US-ASHBURN-AD-2 (Private) ",
                                        "name": "sub2",
                                        "dns": "sub2",
                                        "compartment": "Adi",
                                        "dhcp_options": "Default DHCP Options for vcn",
                                        "security_list": [
                                            "Default Security List for vcn"
                                        ],
                                        "route": "sub2RT",
                                        "defined_tags": {},
                                        "freeform_tags": {}
                                    },
                                    {
                                        "id": "ocid1.subnet.oc1.iad.aaaaaaaa7uaacvuaooovyym734ckungwjhrxcpt4uahqgjotl5llb3c32goq",
                                        "subnet": "10.1.0.192/27  fHBa:US-ASHBURN-AD-3 (Public)",
                                        "name": "sub3",
                                        "dns": "sub3",
                                        "compartment": "Adi",
                                        "dhcp_options": "Default DHCP Options for vcn",
                                        "security_list": [
                                            "Default Security List for vcn"
                                        ],
                                        "route": "Default Route Table for vcn",
                                        "defined_tags": {},
                                        "freeform_tags": {}
                                    }
                                ],
                                "security_lists": [
                                    {
                                        "id": "ocid1.securitylist.oc1.iad.aaaaaaaaoakzxl7uqi3ttwgxtpvi5i5qldquliqvq5zsnkuzws5654xa5gqq",
                                        "name": "Default Security List for vcn",
                                        "compartment": "Adi",
                                        "sec_rules": [
                                            "Ingres  : Src: 0.0.0.0/0         TCP  Dst(22) ",
                                            "Ingres  : Src: 0.0.0.0/0         TCP  Dst(443) ",
                                            "Ingres  : Src: 0.0.0.0/0         TCP  Dst(3389) ",
                                            "Ingres  : Src: 0.0.0.0/0         TCP  Dst(10000) ",
                                            "Ingres  : Src: 0.0.0.0/0         TCP  Dst(8888) ",
                                            "Ingres  : Src: 0.0.0.0/0         ICMP 4,3",
                                            "Ingres  : Src: 10.1.0.0/24       ICMP 3",
                                            "Ingres  : Src: 10.1.0.0/25       ALL  ",
                                            "Ingres  : Src: 10.1.0.0/24       TCP  Dst(1521) ",
                                            "Ingres  : Src: 10.1.0.0/26       TCP  Dst(8000) ",
                                            "Ingres  : Src: 10.1.0.0/26       TCP  Dst(22) ",
                                            "Egres   : Dst: 0.0.0.0/0         ALL  ",
                                            "Egres   : Dst: 10.1.0.0/26       TCP  Dst(8000) ",
                                            "Egres   : Dst: 10.1.0.0/26       TCP  Dst(22) "
                                        ],
                                        "defined_tags": {},
                                        "freeform_tags": {}
                                    }
                                ],
                                "route_tables": [
                                    {
                                        "id": "ocid1.routetable.oc1.iad.aaaaaaaaaxdtkjepzgj2cihuntrbhjuafvmvxxugsvr6cf4aior5g5ic6wlq",
                                        "name": "sub2RT",
                                        "compartment": "Adi",
                                        "route_rules": [
                                            "DST:0.0.0.0/0          --> NATGW",
                                            "DST:oci-iad-objectstor --> SGWsgw"
                                        ]
                                    },
                                    {
                                        "id": "ocid1.routetable.oc1.iad.aaaaaaaa2zmlosrshnuje3tkwqu43poxkeklz2nxp7tfhvvk6d3c7hrjz4ka",
                                        "name": "TransitLPGRoute",
                                        "compartment": "Adi",
                                        "route_rules": [
                                            "DST:0.0.0.0/0          --> DRG - drg"
                                        ]
                                    },
                                    {
                                        "id": "ocid1.routetable.oc1.iad.aaaaaaaap4gb7abeof2crm42zuiwhdxlyvncnetlmrlgwypxzfd323hm6fva",
                                        "name": "TransitRoute",
                                        "compartment": "Adi",
                                        "route_rules": [
                                            "DST:10.0.0.0/8         --> PEERED   - lpg - 10.2.0.0/24"
                                        ]
                                    },
                                    {
                                        "id": "ocid1.routetable.oc1.iad.aaaaaaaalz3hby6vrio3a4qdgafyophdaw4r353sbn2pipawzwgf7kbmklhq",
                                        "name": "Default Route Table for vcn",
                                        "compartment": "Adi",
                                        "route_rules": [
                                            "DST:oci-iad-objectstor --> SGWsgw",
                                            "DST:0.0.0.0/0          --> IGW"
                                        ]
                                    }
                                ],
                                "dhcp_options": [
                                    {
                                        "id": "ocid1.dhcpoptions.oc1.iad.aaaaaaaab52dro2y3yuuvsdbb4qco3v3wcfmvxfhxregft2z5ig5pgcjkgia",
                                        "name": "Default DHCP Options for vcn",
                                        "compartment": "Adi",
                                        "opt": [
                                            "DomainNameServer : VcnLocalPlusInternet",
                                            "SearchDomain     : vcn.oraclevcn.com  "
                                        ]
                                    }
                                ]
                            }
                        }
                    ],
                    "remote_peering": [
                        {
                            "id": "ocid1.remotepeeringconnection.oc1.iad.aaaaaaaavvulhrxdlmlnusfus67ilttz3qbyy4cucmck3o7rswll4x5azkha",
                            "peer_id": "ocid1.remotepeeringconnection.oc1.phx.aaaaaaaa6vbbgmamanroam4rn6hmdfsg6l3565v57fwhbu3qgply7w3ggqea",
                            "name": "AdiRemotePeer",
                            "drg": "DRG - drg",
                            "is_cross_tenancy_peering": "False",
                            "peer_region_name": "us-phoenix-1",
                            "peer_rfc_name": "",
                            "peer_tenancy_id": "ocid1.tenancy.oc1..aaaaaaaae5u57gqxs5qas5f33qnge63sdoi7s2ji6bk5slscblmwr4zvq47q",
                            "peering_status": "PEERED"
                        }
                    ]
                },
                "compute": {
                    "instances": [
                        {
                            "id": "ocid1.instance.oc1.iad.abuwcljrnehdqvc5zfdsifecjly7gm5sbmmt27s4pmjowygs7yginuweo4cq",
                            "name": "VM.Standard1.1 - demohost - RUNNING",
                            "sum_info": "Compute",
                            "sum_shape": "VM.Standard1.1",
                            "availability_domain": "fHBa:US-ASHBURN-AD-1",
                            "fault_domain": "FAULT-DOMAIN-2",
                            "time_maintenance_reboot_due": "None",
                            "image": "Oracle-Linux-7.5-2018.06.14-0",
                            "image_id": "ocid1.image.oc1.iad.aaaaaaaazq7xlunevyn3cf4wppcx2j53eb26pnnc4ukqtfj4tbjjcklnhpaa",
                            "console_id": "ocid1.instanceconsoleconnection.oc1.iad.abuwcljrqsvip6aimwz4sjpn5igc4za5ljn7bvkkrgi56kzefbsugui6hy3a",
                            "console": "Console Connection Active",
                            "defined_tags": {
                                "Project": {
                                    "Prod": "ProdValue",
                                    "Billing": "billing_value"
                                }
                            },
                            "freeform_tags": {
                                "Project": "Basic",
                                "Tag2Key": "12345",
                                "Tag1Key": "Hello"
                            },
                            "boot_volume": [
                                {
                                    "sum_info": "Compute - Block Storage (gb)",
                                    "sum_size_gb": "47",
                                    "desc": "47gb - demohost (Boot Volume) bronze  - Group AdiVol1",
                                    "defined_tags": {},
                                    "freeform_tags": {}
                                }
                            ],
                            "block_volume": [],
                            "vnic": [
                                {
                                    "id": "ocid1.vnic.oc1.iad.abuwcljrxkl6sbhcb7bnvwjwfa6g57r7tnx2kndf3la3w6rvwmcx7h45x3cq",
                                    "desc": "10.1.0.2 (Prv), 129.213.148.40 (Pub) - Primary , Subnet (sub1 10.1.0.0/26), VCN (vcn)"
                                }
                            ]
                        },
                        {
                            "id": "ocid1.instance.oc1.iad.abuwcljs3lrcsidis54oztczwhszmoebigeflbugzifdhzi7fxxgzceklliq",
                            "name": "VM.Standard2.1 - inst-hari6-Adi-Instance-Pool - RUNNING",
                            "sum_info": "Compute",
                            "sum_shape": "VM.Standard2.1",
                            "availability_domain": "fHBa:US-ASHBURN-AD-3",
                            "fault_domain": "FAULT-DOMAIN-3",
                            "time_maintenance_reboot_due": "None",
                            "image": "Oracle-Linux-7.5-2018.10.16-0",
                            "image_id": "ocid1.image.oc1.iad.aaaaaaaageeenzyuxgia726xur4ztaoxbxyjlxogdhreu3ngfj2gji3bayda",
                            "console_id": "",
                            "console": "",
                            "defined_tags": {},
                            "freeform_tags": {
                                "oci:compute:instanceconfiguration": "ocid1.instanceconfiguration.oc1.iad.aaaaaaaasfmvtaywv3kfo6ysr6en4jb3zyojzlqvbsthoew2wxw6fmv7ku6a",
                                "oci:compute:instancepool": "ocid1.instancepool.oc1.iad.aaaaaaaaril5efiy3qyvrtnikkj6spcnh4tuhxpkfvaqod7d4emhxnhr66iq"
                            },
                            "boot_volume": [
                                {
                                    "sum_info": "Compute - Block Storage (gb)",
                                    "sum_size_gb": "47",
                                    "desc": "47gb - inst-hari6-Adi-Instance-Pool (Boot Volume) ",
                                    "defined_tags": {},
                                    "freeform_tags": {}
                                }
                            ],
                            "block_volume": [],
                            "vnic": [
                                {
                                    "id": "ocid1.vnic.oc1.iad.abuwcljsnflxogipkhh3zxw4anlc5wz5nwdgo37yeialami5d42dtc4sfdta",
                                    "desc": "10.1.0.204 (Prv), 129.213.110.160 (Pub) - Primary , Subnet (sub3 10.1.0.192/27), VCN (vcn)"
                                }
                            ]
                        }
                    ],
                    "images": [
                        {
                            "id": "ocid1.image.oc1.iad.aaaaaaaabpmf3pirefc3fnjg4zkai2jr2kuhwacvp4ezz5bgjtfs2epoabxq",
                            "desc": "AdiZoharImage - Oracle Linux - 47gb - Base:  Oracle-Linux-7.5-2018.06.14-0",
                            "sum_info": "Object Storage - Images (gb)",
                            "sum_size_gb": "47",
                            "defined_tags": {},
                            "freeform_tags": {}
                        }
                    ],
                    "instance_configuration": [
                        {
                            "id": "ocid1.instanceconfiguration.oc1.iad.aaaaaaaasfmvtaywv3kfo6ysr6en4jb3zyojzlqvbsthoew2wxw6fmv7ku6a",
                            "name": "AdiInstanceConfig",
                            "shape": "VM.Standard2.1",
                            "source": "Image: Oracle-Linux-7.5-2018.10.16-0"
                        },
                        {
                            "id": "ocid1.instanceconfiguration.oc1.iad.aaaaaaaav4viydth43w76yn4ez53hkl6nn3tstrnqd3f6xua6kzlxsqayira",
                            "name": "InstanceConfig",
                            "shape": "VM.Standard1.1",
                            "source": "Image: Oracle-Linux-7.5-2018.06.14-0"
                        }
                    ],
                    "instance_pool": [
                        {
                            "id": "ocid1.instancepool.oc1.iad.aaaaaaaaril5efiy3qyvrtnikkj6spcnh4tuhxpkfvaqod7d4emhxnhr66iq",
                            "availability_domains": "fHBa:US-ASHBURN-AD-3, fHBa:US-ASHBURN-AD-2",
                            "name": "Adi-Instance-Pool - RUNNING - Size: 1",
                            "instance_configuration_id": "ocid1.instanceconfiguration.oc1.iad.aaaaaaaasfmvtaywv3kfo6ysr6en4jb3zyojzlqvbsthoew2wxw6fmv7ku6a",
                            "instance_configuration_name": "AdiInstanceConfig - VM.Standard2.1"
                        }
                    ],
                    "volume_groups": [
                        {
                            "id": "ocid1.volumegroup.oc1.iad.abuwcljryt4rgn2swkngoeegwmja4flv7xbzh5seczoihjpf5srkhrbrersa",
                            "name": "AdiVol1",
                            "size_in_gbs": "97",
                            "compartment_name": "Adi",
                            "volumes": [
                                "test_vol - 50gb",
                                "demohost (Boot Volume) - 47gb"
                            ],
                            "defined_tags": {},
                            "freeform_tags": {}
                        }
                    ],
                    "boot_not_attached": [
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "47",
                            "desc": "47gb    - Clone1                    - fHBa:US-ASHBURN-AD-1 - 2018-10-22 02:50"
                        },
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "47",
                            "desc": "47gb    - demolkq (Boot Volume)     - fHBa:US-ASHBURN-AD-1 - 2019-03-18 17:02"
                        },
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "47",
                            "desc": "47gb    - LKQ_CLONE                 - fHBa:US-ASHBURN-AD-1 - 2019-03-18 17:08"
                        },
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "47",
                            "desc": "47gb    - temp1 (Boot Volume)       - fHBa:US-ASHBURN-AD-2 - 2019-02-20 15:11"
                        },
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "50",
                            "desc": "50gb    - Clone_50G                 - fHBa:US-ASHBURN-AD-3 - 2018-10-22 02:58"
                        }
                    ],
                    "volume_not_attached": [
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "50",
                            "desc": "50gb    - test_vol            - fHBa:US-ASHBURN-AD-1 - 2019-03-23 02:39 - Group AdiVol1"
                        },
                        {
                            "sum_info": "Compute - Block Storage (gb)",
                            "sum_size_gb": "50",
                            "desc": "50gb    - Adi_50G             - fHBa:US-ASHBURN-AD-3 - 2018-10-22 02:49"
                        }
                    ],
                    "boot_volume_backup": [
                        {
                            "name": "demohost (Boot Volume), ",
                            "desc": "Auto-backup for 2018-08-01 04:00:00 via policy: bronze",
                            "type": "INCREMENTAL, SCHEDULED, 2018-08-01 16:27 -> 2019-08-01 23:07",
                            "size": "47gb , Stored 1gb",
                            "sum_info": "Object Storage - BV Backups (gb)",
                            "sum_size_gb": "1",
                            "boot_volume_id": "ocid1.bootvolume.oc1.iad.abuwcljro5qzmdkv5ybu3ztsziceircahpo5jgpkl3hbk5axvdajc6lccb3q"
                        },
                        {
                            "name": "demohost (Boot Volume), ",
                            "desc": "Auto-backup for 2018-09-01 04:00:00 via policy: bronze",
                            "type": "INCREMENTAL, SCHEDULED, 2018-09-01 07:50 -> 2019-09-01 14:30",
                            "size": "47gb , Stored 1gb",
                            "sum_info": "Object Storage - BV Backups (gb)",
                            "sum_size_gb": "1",
                            "boot_volume_id": "ocid1.bootvolume.oc1.iad.abuwcljro5qzmdkv5ybu3ztsziceircahpo5jgpkl3hbk5axvdajc6lccb3q"
                        },
                        {
                            "name": "demohost (Boot Volume), ",
                            "desc": "Auto-backup for 2018-10-01 04:00:00 via policy: bronze",
                            "type": "INCREMENTAL, SCHEDULED, 2018-10-01 09:02 -> 2019-10-01 15:42",
                            "size": "47gb , Stored 1gb",
                            "sum_info": "Object Storage - BV Backups (gb)",
                            "sum_size_gb": "1",
                            "boot_volume_id": "ocid1.bootvolume.oc1.iad.abuwcljro5qzmdkv5ybu3ztsziceircahpo5jgpkl3hbk5axvdajc6lccb3q"
                        },
                        {
                            "name": "demohost (Boot Volume), ",
                            "desc": "Auto-backup for 2018-11-01 04:00:00 via policy: bronze",
                            "type": "INCREMENTAL, SCHEDULED, 2018-11-01 09:07 -> 2019-11-01 15:47",
                            "size": "47gb , Stored 10gb",
                            "sum_info": "Object Storage - BV Backups (gb)",
                            "sum_size_gb": "10",
                            "boot_volume_id": "ocid1.bootvolume.oc1.iad.abuwcljro5qzmdkv5ybu3ztsziceircahpo5jgpkl3hbk5axvdajc6lccb3q"
                        },
                    ],
                    "volume_backup": [
                        {
                            "name": "Adi_50G ( Source TERMINATED )",
                            "desc": "Adi_Backup_50G",
                            "type": "FULL, MANUAL, 2018-10-22 02:52 -> Keep",
                            "size": "50gb , Stored 1gb",
                            "sum_info": "Object Storage - BV Backups (gb)",
                            "sum_size_gb": "1",
                            "volume_id": "ocid1.volume.oc1.iad.abuwcljsu2ryf2ddayczbsdyd2w4kpt2nxgtnvb6th625td3x72qn5cmmy2a"
                        },
                        {
                            "name": "Adi_50G ( Source TERMINATED )",
                            "desc": "Auto-backup for 2018-11-01 04:00:00 via policy: bronze",
                            "type": "INCREMENTAL, SCHEDULED, 2018-11-01 04:40 -> 2019-11-01 11:20",
                            "size": "50gb , Stored 1gb",
                            "sum_info": "Object Storage - BV Backups (gb)",
                            "sum_size_gb": "1",
                            "volume_id": "ocid1.volume.oc1.iad.abuwcljsu2ryf2ddayczbsdyd2w4kpt2nxgtnvb6th625td3x72qn5cmmy2a"
                        }
                    ]
                },
                "database": {
                    "db_system": [
                        {
                            "id": "ocid1.dbsystem.oc1.iad.abuwcljsgudxgprvd2anozhpkdnfcll6suhjmrfus5o6nkxoanckfyzavaga",
                            "name": "ADIDB02 - VM.Standard1.1 - AVAILABLE",
                            "sum_info": "Database - VM.Standard1.1 - BYOL",
                            "sum_info_storage": "Database - Storage (gb)",
                            "sum_size_gb": "256",
                            "availability_domain": "fHBa:US-ASHBURN-AD-3",
                            "cpu_core_count": "1",
                            "node_count": "1",
                            "version": "18.3.0.0.180717 - ENTERPRISE_EDITION_EXTREME_PERFORMANCE - BYOL",
                            "host": "dbhost",
                            "domain": "sub3.vcn.oraclevcn.com",
                            "data_subnet": "sub3",
                            "backup_subnet": "",
                            "scan_dns": "ocid1.vcndnsrecord.oc1.iad.abuwcljszsvrzlpytvykn4oqoskub6qqebk4wkpkesfa7gdgvf2nomqyrclq",
                            "scan_ips": [],
                            "vip_ips": [],
                            "patches": [
                                "Jan 2019 18c Db System patch - 18.5.0.0.190115 - 2019-02-20 - Last Action: PRECHECK"
                            ],
                            "listener_port": "1521",
                            "db_homes": [
                                {
                                    "id": "ocid1.dbhome.oc1.iad.abuwcljsxzdxx7sigwnrbaewekdpsrcfcd3mrwcvput6zyialrdrpm5r6xla",
                                    "home": "dbhome20181026162225 - 18.3.0.0.180717",
                                    "databases": [
                                        {
                                            "name": "ADIDB02 - ADIDB02_iad3n9 -  - OLTP - AL32UTF8 - AVAILABLE - AutoBck=N",
                                            "backups": [
                                                {
                                                    "name": "Automatic Backup - INCREMENTAL - FAILED",
                                                    "time": "2019-04-05 05:25 - 2019-04-05 05:27",
                                                    "size": "None",
                                                    "sum_info": "Object Storage - DB Backup (gb)",
                                                    "sum_size_gb": ""
                                                },
                                                {
                                                    "name": "Automatic Backup - INCREMENTAL - ACTIVE",
                                                    "time": "2019-01-15 05:25 - 2019-01-15 05:40",
                                                    "size": "6.0gb",
                                                    "sum_info": "Object Storage - DB Backup (gb)",
                                                    "sum_size_gb": "6.0"
                                                }
                                            ],
                                            "defined_tags": {},
                                            "freeform_tags": {}
                                        }
                                    ],
                                    "patches": [
                                        "Jan 2019 18c Database patch - 18.5.0.0.190115 - 2019-02-20 - Last Action: None",
                                        "Oct 2018 18c Database patch - 18.4.0.0.181016 - 2019-01-10 - Last Action: PRECHECK",
                                        "Jul 2018 18c Database patch - 18.3.0.0.180717 - 2018-07-30 - Last Action: APPLY"
                                    ]
                                }
                            ],
                            "db_nodes": [
                                "Node    : dbhost - AVAILABLE - 10.1.0.196 (Prv), 129.213.32.183 (Pub) - Primary , Subnet (sub3 10.1.0.192/27), VCN (vcn) - FAULT-DOMAIN-3"
                            ],
                            "cluster_name": "",
                            "defined_tags": {},
                            "freeform_tags": {},
                            "data": "256gb - 80%"
                        }
                    ]
                },
                "file_storage": [
                    {
                        "id": "ocid1.filesystem.oc1.iad.aaaaaaaaaaaaiovnnfqwillqojxwiotjmfsc2ylefuyqaaaa",
                        "filesystem": "FileSystem-20190203-2217 - fHBa:US-ASHBURN-AD-1 - 0.0gb metered",
                        "sum_info": "File Storage (gb)",
                        "sum_size_gb": "0.0",
                        "snapshots": [],
                        "exports": [
                            {
                                "id": "ocid1.export.oc1.iad.aaaaacvippxhavcjnfqwillqojxwiotjmfsc2ylefuyqaaaa",
                                "file_system_id": "ocid1.filesystem.oc1.iad.aaaaaaaaaaaaiovnnfqwillqojxwiotjmfsc2ylefuyqaaaa",
                                "time_created": "2019-02-03 22:18:03.034000+00:00",
                                "path": "/FileSystem-20190203-2217",
                                "exportset": "MountTarget-20190203-2217 - export set, fHBa:US-ASHBURN-AD-1, Limits: Size (Unlimited), Files (64bit)",
                                "mount_target": [
                                    {
                                        "id": "ocid1.mounttarget.oc1.iad.aaaaacvippxhavjxnfqwillqojxwiotjmfsc2ylefuyqaaaa",
                                        "mount": "MountTarget-20190203-2217, Subnet: sub1,  10.1.0.0/26, VCN (vcn)",
                                        "private_ip_ids": [
                                            "10.1.0.25 - privateip20190203221806"
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "object_storage": [
                    {
                        "name": "AdiTest",
                        "objects": "        1",
                        "size": "      0.0",
                        "sum_size_gb": "0.0",
                        "sum_info": "Object Storage - Buckets (gb)",
                        "preauthenticated_requests": "",
                        "object_lifecycle": " , LifeCycle: LifecycleRule, ARCHIVE, 30 DAYS",
                        "desc": "AdiTest                  -         1 Objs ,       0.0gb (Approx) , LifeCycle: LifecycleRule, ARCHIVE, 30 DAYS"
                    }
                ],
                "load_balancer": [
                    {
                        "sum_info": "Load Balancer 100Mbps",
                        "details": {
                            "id": "ocid1.loadbalancer.oc1.iad.aaaaaaaas25ybf66cnqmis5lxfdi72ey7jl7c4ifski3a5n7ewpdd2jy5dzq",
                            "name": "adi_test_lb - 100Mbps - (Private)",
                            "status": "OK",
                            "ips": [
                                "10.1.0.17 - Private"
                            ],
                            "path_route": [],
                            "hostnames": [],
                            "subnets": [
                                "sub1,  10.1.0.0/26, VCN (vcn)"
                            ],
                            "listeners": []
                        },
                        "backendset": [
                            {
                                "backend_set": "adi_bs - ROUND_ROBIN",
                                "status": "OK  ",
                                "session_persistence": "",
                                "ssl_cert": "",
                                "backends": [
                                    "OK   - 10.1.0.2:22 - Backup=N, Drain=N, Offline=N, Weight=1"
                                ],
                                "health_check": [
                                    "interval(ms)=30000, Timeout(ms)=3000, retries=3",
                                    "22/TCP"
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

##########################################################################################
#                     Completed Successfully at 2019-04-05 08:15:16                      #
##########################################################################################

```
