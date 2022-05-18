## Object Storage Utilities

Object Storage Manipulation Tool allow customer to handle millions of object storage objects with simple scripts 

**DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes

**Developed by Adi Zohar, 2021-2022**

## Executing using Cloud Shell:
```
    1. install oci sdk package
       pip3 install --user oci

    2. clone the oci sdk repo
       git clone https://github.com/oracle/oci-python-sdk

    3. Execute
       cd $HOME/oci-python-sdk/examples/object_storage
       python3 object_storage_bulk_copy.py    -dt -parameters...
       python3 object_storage_bulk_delete.py  -dt -parameters...
       python3 object_storage_bulk_restore.py -dt -parameters...
       python3 object_storage_list_objects.py -dt -parameters...
       python3 object_storage_bulk_rename.py -dt -parameters...
```

## object_storage_bulk_copy.py
Bulk Copy objects between buckets / tenants / regions

```
usage: object_storage_bulk_copy.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip]
                                   [-dt] [-c CONFIG_FILE] [-sb SOURCE_BUCKET]
                                   [-sr SOURCE_REGION] [-sn SOURCE_NAMESPACE]
                                   [-sp SOURCE_PREFIX_INCLUDE]
                                   [-se SOURCE_PREFIX_EXCLUDE]
                                   [-db DESTINATION_BUCKET]
                                   [-dr DESTINATION_REGION]
                                   [-dn DESTINATION_NAMESPACE] [-ig]

optional arguments:
  -h, --help                 show this help message and exit
  -t CONFIG_PROFILE          Config file section to use (tenancy profile)
  -p PROXY                   Set Proxy (i.e. www-proxy-server.com:80)
  -ip                        Use Instance Principals for Authentication
  -dt                        Use Delegation Token for Authentication
  -c CONFIG_FILE             Config File (default=~/.oci/config)
  -sb SOURCE_BUCKET          Source Bucket Name
  -sr SOURCE_REGION          Source Region (Default current connection)
  -sn SOURCE_NAMESPACE       Source Namespace (Default current connection)
  -sp SOURCE_PREFIX_INCLUDE  Source Prefix Include
  -se SOURCE_PREFIX_EXCLUDE  Source Prefix Exclude
  -db DESTINATION_BUCKET     Destination Bucket Name
  -dr DESTINATION_REGION     Destination Region
  -dn DESTINATION_NAMESPACE  Destination Namespace (Default current connection)
  -ig                        Ignore Check if files exist at Destination
```

## object_storage_bulk_delete
Bulk delete bucket objects from a bucket with option to filter

```
usage: object_storage_bulk_delete.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip]
                                     [-dt] [-c CONFIG_FILE]
                                     [-sb SOURCE_BUCKET] [-sp SOURCE_PREFIX]
                                     [-se SOURCE_PREFIX_EXCLUDE] 
                                     [-sn SOURCE_NAMESPACE]
                                     [-exclude_dirs] [-sr SOURCE_REGION]

optional arguments:
  -h, --help                 show this help message and exit
  -t CONFIG_PROFILE          Config file section to use (tenancy profile)
  -p PROXY                   Set Proxy (i.e. www-proxy-server.com:80)
  -ip                        Use Instance Principals for Authentication
  -dt                        Use Delegation Token for Authentication
  -c CONFIG_FILE             Config File (default=~/.oci/config)
  -sb SOURCE_BUCKET          Source Bucket Name
  -sp SOURCE_PREFIX          Source Prefix Include
  -se SOURCE_PREFIX_EXCLUDE  Source Prefix Exclude
  -sn SOURCE_NAMESPACE       Source Namespace (Default current connection)
  -exclude_dirs              Exclude Directories
  -sr SOURCE_REGION          Source Region
```

## object_storage_bulk_restore
Bulk restore objects that in archive state
```
usage: object_storage_bulk_restore.py [-h] [-t CONFIG_PROFILE] [-p PROXY]
                                      [-ip] [-dt] [-c CONFIG_FILE]
                                      [-sb SOURCE_BUCKET]
                                      [-sp SOURCE_PREFIX_INCLUDE]
                                      [-sr SOURCE_REGION] 
                                      [-sn SOURCE_NAMESPACE]

optional arguments:
  -h, --help                show this help message and exit
  -t CONFIG_PROFILE         Config file section to use (tenancy profile)
  -p PROXY                  Set Proxy (i.e. www-proxy-server.com:80)
  -ip                       Use Instance Principals for Authentication
  -dt                       Use Delegation Token for Authentication
  -c CONFIG_FILE            Config File (default=~/.oci/config)
  -sb SOURCE_BUCKET         Source Bucket Name
  -sp SOURCE_PREFIX_INCLUDE Source Prefix Include
  -sn SOURCE_NAMESPACE       Source Namespace (Default current connection)
  -sr SOURCE_REGION         Source Region
```

## object_storage_list_objects
Bulk list bucket objects or produce summary

```
usage: object_storage_list_objects.py [-h] [-t CONFIG_PROFILE] [-p PROXY]
                                      [-ip] [-dt] [-c CONFIG_FILE]
                                      [-sb SOURCE_BUCKET] [-sp SOURCE_PREFIX]
                                      [-se SOURCE_PREFIX_EXCLUDE]
                                      [-sn SOURCE_NAMESPACE]
                                      [-sr SOURCE_REGION] [-exclude_dirs]
                                      [-f FILE] [-co]

optional arguments:
  -h, --help                 show this help message and exit
  -t CONFIG_PROFILE          Config file section to use (tenancy profile)
  -p PROXY                   Set Proxy (i.e. www-proxy-server.com:80)
  -ip                        Use Instance Principals for Authentication
  -dt                        Use Delegation Token for Authentication
  -c CONFIG_FILE             Config File (default=~/.oci/config)
  -sb SOURCE_BUCKET          Source Bucket Name
  -sp SOURCE_PREFIX          Source Prefix Include
  -se SOURCE_PREFIX_EXCLUDE  Source Prefix Exclude
  -sr SOURCE_REGION          Source Region
  -sn SOURCE_NAMESPACE       Source Namespace (Default current connection)
  -exclude_dirs              Exclude Directories
  -f FILE                    Output to file (as csv)
  -co                        Count only files and size
```

## object_storage_bulk_rename.py
Bulk rename bucket objects, can be used to move objects to a "virtual" folder as well
```
usage: object_storage_bulk_rename.py [-h] [-t CONFIG_PROFILE] [-p PROXY] [-ip]
                                     [-dt] [-c CONFIG_FILE]
                                     [-sb SOURCE_BUCKET]
                                     [-sp SOURCE_PREFIX_INCLUDE]
                                     [-sr SOURCE_REGION]
                                     [-sn SOURCE_NAMESPACE]
                                     [-textrem TEXT_REMOVE]
                                     [-textadd TEXT_APPEND]

optional arguments:
  -h, --help                 show this help message and exit
  -t CONFIG_PROFILE          Config file section to use (tenancy profile)
  -p PROXY                   Set Proxy (i.e. www-proxy-server.com:80)
  -ip                        Use Instance Principals for Authentication
  -dt                        Use Delegation Token for Authentication
  -c CONFIG_FILE             Config File (default=~/.oci/config)
  -sb SOURCE_BUCKET          Source Bucket Name
  -sp SOURCE_PREFIX_INCLUDE  Source Prefix Include
  -sr SOURCE_REGION          Source Region
  -sn SOURCE_NAMESPACE       Source Namespace (Default current connection)
  -textrem TEXT_REMOVE       text remove prefix (can be used to remove folder)
  -textadd TEXT_APPEND       text append prefix (can be used to add folder)
```