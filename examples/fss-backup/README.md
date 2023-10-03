# FSS Backup Process

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

Backup is accomplished using the Python script fss_backup.py

The script attempts to be self-documenting, ie run it with no arguments for basic help or `-h` for actual help:

```bash
./fss_backup.py 
usage: fss_backup.py [-h] [-v] [-fs FSSOCID] -fc FSSCOMPARTMENT -oc OSSCOMPARTMENT -r REMOTE -ad AVAILABILITYDOMAIN -m MOUNTIP [-pr PROFILE]
                     [-ty TYPE] [--dryrun] [--serversidecopy] [-t THRESHOLD]
fss_backup.py: error: the following arguments are required: -fc/--fsscompartment, -oc/--osscompartment, -r/--remote, -ad/--availabilitydomain, -m/--mountip
```
or
```
/fss_backup.py -h
usage: fss_backup.py [-h] [-v] [-fs FSSOCID] -fc FSSCOMPARTMENT -oc OSSCOMPARTMENT -r REMOTE -ad AVAILABILITYDOMAIN -m MOUNTIP [-pr PROFILE]
                     [-ty TYPE] [--dryrun] [--serversidecopy] [-t THRESHOLD]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -fs FSSOCID, --fssocid FSSOCID
                        FSS Compartment OCID of doing a single FS
  -fc FSSCOMPARTMENT, --fsscompartment FSSCOMPARTMENT
                        FSS Compartment OCID
  -oc OSSCOMPARTMENT, --osscompartment OSSCOMPARTMENT
                        OSS Backup Comaprtment OCID
  -r REMOTE, --remote REMOTE
                        Named rclone remote for that user. ie oci:
  -ad AVAILABILITYDOMAIN, --availabilitydomain AVAILABILITYDOMAIN
                        AD for FSS usage. Such as dDzb:US-ASHBURN-AD-1
  -m MOUNTIP, --mountip MOUNTIP
                        Mount Point IP to use.
  -pr PROFILE, --profile PROFILE
                        OCI Profile name (if not default)
  -ty TYPE, --type TYPE
                        Type: daily(def), weekly, monthly
  --dryrun              Dry Run - print what it would do
  --serversidecopy      For weekly/monthly only - copies directly from latest daily backup, not source FSS
  -t THRESHOLD, --threshold THRESHOLD
                        GB threshold - do not back up share if more than this
```

The script using rclone internally, which is fully documented at rclone.org

All output is given to the local shell, and in the case of cron, it is best to collect all output from STDERR and STDOUT to a single file 

## About OSS Object Storage

Using OSS is great - nearly unlimited cheap storage.  By using a versioned bucket, the script ensures that the daily incremental backups are simply maintaned and only new and changed files are added.  rclone uses a checksum to determine if it needs to copy anything, so if you run daily incrementals, they will not take up more space unless anything is changed.  The versioned bucket will then keep track of previous file versions to choos from, in the case of a single file restore.

For weekly and monthly backups, the folder created is unique using a timestamp, which results in a full copy being sent up (takes much longer)

Finally, this process enables Object Lifecycle Policies to delete older copies, based on retention rules.  See below.

## About rclone

It's amazing.  All of the logic around "to copy or not copy" is there.  This script simply wraps it with the smarts to grab the correct file system and prep it for the copy.

## Script Pseudocode

List FSS - for each
- Create FSS Snapshot based on type of backup
- Mount it read only to be safe
- Rclone the contents of the share out to OSS with metadata (inlcudes ACL and owner/group info)
- Delete FSS Snapshot (clean up)
- Unmount the share (clean up)

End Loop

If you specify `-fs` then the loop is a single iteration.

## Required to Install

- rclone (latest)
- OCI CLI (latest)
- python3 (latest)

## Configuring

Set up the OCI command line with an API Key that has access to an OCI user in a group, where that group can access both File Shares (FSS) and Object Storage(OSS) in the compartments you want to operate in.  Tenancy Admin will always be able to run it.

OCI CLI should work with the root user.  For example, if set up properly,
```
root prompt:>> oci os ns get
{
  "data": "tenancy01"
}
```

Set up rclone with an S3 Remote (OCI OSS tested, but others may work).  Use `rclone config show` to see what you have, and note that the trailing `:` character is going to be needed to run the command.  

An example:
```
prompt:>> rclone config show
[oci-oss]
type = s3
provider = Other
access_key_id = YYY
secret_access_key = XXX=
endpoint = https://orasenatdpltintegration01.compat.objectstorage.us-ashburn-1.oraclecloud.com
acl = private
```
In this case, use the script with `-r oci-oss:`

Finally, you must be running as root or sudo with no password.
Create the following directory, to be used a temporary local mount:
```bash
root prompt:>> mkdir /mnt/temp-backup
``` 

## Listing the File Systems
Since the OCI CLI is set up as it must be, to test it before the script runs, Run an FSS List to see if you get results.  Grab the OCID for the compartment where the FSS Filesystems live.

```bash
oci fs file-system list -c ocid1.compartment.oc1..xxx --availability-domain UWQV:US-ASHBURN-AD-3 --query 'data[].{AD:"availability-domain",NAME:"display-name",SIZE:"metered-bytes",OCID:id}'  --output table
+----------------------+------------------+---------------------------------------------------------------------------+-----------+
| AD                   | NAME             | OCID                                                                      | SIZE      |
+----------------------+------------------+-----------------------------------------------+-----------+
| UWQV:US-ASHBURN-AD-3 | /fss-filesystem2 | ocid1.filesystem.oc1.iad.xxx | 17408     |
| UWQV:US-ASHBURN-AD-3 | /fss-filesystem1 | ocid1.filesystem.oc1.iad.yyy | 156101120 |
+----------------------+------------------+---------------------------------------------------------------------------+-----------+
```

These OCIDs can be used later on, if you want to run a single File System.

## Running the Script

There are only 5 required arguments, the rest are optional. See above for help.  The most basic command is below, this will use a type of daily (incremental).  Given the compartment for FSS, the script will iterate and perform the backups on ALL File Systems in the compartment.

Required:
- -fc Compartment OCID where Filesystems live
- -oc Compartment OCID where object bucket backups will go
- -r RCLONE remote - must be defined by OS user (rclone config show).  And include colon (ie oci-oss:)
- -ad Availability domain of FSS (see example)
- -m Mount Point IP - will be used as temporary read only mount

```
root prompt:>> ./fss_backup.py -fc ocid1.compartment.oc1..fss.compartment.ocid -oc ocid1.compartment.oc1..yyy.oss.bucket.compartment.ocid -r oci-oss: -m 10.0.1.83 -ad UWQV:US-ASHBURN-AD-3
```

To limit it to a single File system, pass in `-fs -fs ocid1.filesystem.oc1.iad.my.filesystem.ocid`

To run in verbose mode, pass in `-v`

Most helpful, before running for real, add `--dryrun` to have it print what it would do, while doing nothing.

To change the Backup type to Full and do a weekly or monthly, add `--type weekly` or `--type monthly`.  In these cases, a full backups is created of the File System in the object store.  Both weekly and monthly imply a daily backup as well, so they are used in lieu of daily.

Example with weekly backup of single File System, verbose mode:
```bash
prompt:>> ./fss_backup.py -fc ocid1.compartment.oc1..xxxxxxfss.comp.ocid -oc ocid1.compartment.oc1..xxxxxoss.comp.ocid -r oci-oss:  -m 10.0.1.83 -ad UWQV:US-ASHBURN-AD-3 -fs ocid1.filesystem.oc1.iad.xxxxxfss.filesystem.ocid --type weekly -v
```

## Optional Parameters 


This section covers the options that can be added to the script.

### Dry Run

Add `--dry-run` to print what the script will do, without actually doing anything.

### Server Side copy
For weekly or monthly backups you can specify `--serversidecopy` with the command and RCLONE will not copy the backup from the FSS Source.  Rather, it will copy the daily backup (latest version of each file) directly using OSS to OSS copy - in theory, this saves transfer time.  It also does a copy with no integrity checking, as that has already been done as part of the daily incremental, which has always just occurred.

Example:
```bash
prompt:>>  ./fss_backup.py -fc ocid1.compartment.oc1..fss.comp.ocid -oc ocid1.compartment.oc1..oss.comp.ocid -r oci-oss:  -m 10.0.1.83 -ad UWQV:US-ASHBURN-AD-3  --type weekly --serversidecopy

...output...
2022/08/08 15:25:45 INFO  : 10000files/file-1015: Copied (server-side copy)
...output...
```

### Threshold

You can specify a threshold in GB.  If specified, the script will skip FSS Shares where the metered-bytes (size) is larger than the value.  For example, adding `-t 20` will only backup shares less than 20GB.

Example:
```bash
prompt:>> ./fss_backup.py -fc ocid1.compartment.oc1..fss.comp.ocid -oc ocid1.compartment.oc1..oss.comp.ocid -r oci-oss:  -m 10.0.1.83 -ad UWQV:US-ASHBURN-AD-3  --type daily -t 4
...output...
File System is 6.49 GB.  Threshold is 4 GB.  Skipping
...output...
```

### Sort Smallest to Largest

Add `-s` or `--sortbytes` to the command to sort the file systems that will be backed up by size, smallest to largest.  This way the smaller ones will get done first.  Combine with `-t X` as above to be able to back up smallest first and stop at a specific size.  Perhaps take largest shares individually or separate otherwise.

### Verbose

Add `-v` to have the script do verbose output.  This also sends RCLONE a verbose instruction to pring debugging when it runs.  NOT recommended for cron.

## Crontab

Using standard Crontab, run the script directly:

```
0 18 * * * /root/fss_backup/fss_backup.py <bunch of params> >> /root/fss_backup/fss_backup_cron_output.log 2>&1
```

Or run an intermediate script, such as when you need to backup multiple shares but not all within a compartment.  The intermediate script might look like this:

```
#! /bin/bash

echo "*********************************"
date

# File system1
/root/code/fss_backup.py -fc <FSS Compartment OCID> -oc <OSS Bucket OCID> -r oci-oss: -m <FSS Mount IP> -ad UWQV:US-ASHBURN-AD-3 --type weekly -v

# Filesystem2
#./fss_backup.py <bunch of params>

date
echo "*********************************"
```

Cron itself would then look like this (daily at 6pm):
```
0 18 * * * /root/fss_backup/cronjob.sh >> /root/fss_backup/cron_output.log 2>&1
```

### Cron Strategy
The strategy could be to do daily backups on Mon-Thu, and then a weekly backup on Friday.  For Monthly, that can be in lieu of a weekly.  The cron tab could look like this:

```
0 18 * * 1-4 <daily backup>
0 18 * * 5 [ $(date +"\%m") -eq $(date -d 7days +"\%m") ] && <weekly backup>
0 18 * * 5 [ $(date +"\%m") -ne $(date -d 7days +"\%m") ] && <monthly backup>
```

## Object Lifecycle

Default and reasonable rules for OSS Lifecycle will prevent the backups from collecting forever and costing more money than they should.  There is a JSON here with some decent starting points.  Add it to the bucket that is created during the script:

Lifecycle script
```
prompt:>> oci os object-lifecycle-policy put --from-json file://lifecycle_rules_14_60_180.json --bucket-name <name of bucket> 
WARNING: Updates to items will replace any existing values. Are you sure you want to continue? [y/N]: y
{
    JSON
}
```
You can add `--force` to prevent the prompt, for example in a script to "bulk-replace" the rules for a list of buckets.  To generate a list of buckets, grab the Compartment OCID where the buckets are, and run something like this:
```
prompt:>> oci os bucket list --compartment-id ocid1.compartment.oc1..comp..where.buckets.are --query 'data[].name' --output table
+--------------------------+
| Column1                  |
+--------------------------+
| fss-filesystem1_backup   |
| fss-filesystem2_backup   |
| fss-filesystem3_backup   |
| ...                      |
+--------------------------+
```
