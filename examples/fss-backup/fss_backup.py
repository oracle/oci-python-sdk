##########################################################################
# fss_backup.py
#
# @author: Andrew Gregory, June 2022
#
# Supports Python 3
#
# This script is designed to create Object-storage-based backups of OCI FileSystems
# The intent is that users would run this via cron, and it will create a synchronized
# copy of the filesystem using rclone out on OSS.  The notion of a "daily"
# backup uses the concpet of object versioning, whilst a "weekly" or "monthly" is a point-in-time
# cut and is immutable.
# When used in conjunction with Object Lifecycle Rules, it can create automatic self-maintaining
# replicas of the file system in a non-FSS manner.
#
##########################################################################
# Application Command line parameters
#
#   -h, --help            show this help message and exit
#   -v, --verbose         increase output verbosity
#   -fs FSSOCID, --fssocid FSSOCID
#                         FSS Compartment OCID of doing a single FS
#   -fc FSSCOMPARTMENT, --fsscompartment FSSCOMPARTMENT
#                         FSS Compartment OCID
#   -oc OSSCOMPARTMENT, --osscompartment OSSCOMPARTMENT
#                         OSS Backup Comaprtment OCID
#   -r REMOTE, --remote REMOTE
#                         Named rclone remote for that user. ie oci:
#   -ad AVAILABILITYDOMAIN, --availabilitydomain AVAILABILITYDOMAIN
#                         AD for FSS usage. Such as dDzb:US-ASHBURN-AD-1
#   -m MOUNTOCID, --mountocid MOUNTOCID
#                         Mount Point OCID to use.
#   -pr PROFILE, --profile PROFILE
#                         OCI Profile name (if not default)
#   -ty TYPE, --type TYPE
#                         Type: daily(def), weekly, monthly
#   --dryrun              Dry Run - print what it would do
#   -ssc, --serversidecopy
#                         For weekly/monthly only - copies directly from latest daily backup, not source FSS
#   -s, --sortbytes       Sort by byte size of FSS, smallest to largest (smaller FS backed up first
#   -t THRESHOLD, --threshold THRESHOLD
#                         GB threshold - do not back up share if more than this
#
#
##########################################################################

import time
import datetime
import os
import signal
import subprocess
import multiprocessing
import argparse
import sys
import oci
import logging

#######################################
# CONSTANTS
SNAPSHOT_NAME = "FSS-dailyBackup"

# File system temporary Mount Point
TEMP_MOUNT = "/mnt/temp-backup"

# Threshold GB (Don't back up if > this)
THRESHOLD_GB = sys.maxsize

# Number of cores (like nproc)
CORE_COUNT = multiprocessing.cpu_count()

# Define globally but set later
verbose = False

#######################################
# SUB ROUTINES


def extract_bytes(file_system):
    """Pull out file system byte count"""
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(file_system.metered_bytes)
    except KeyError:
        return 0


def cleanup_file_snapshot(fs_client, fs_ocid):
    """Use API to attempt bucket creation"""

    # Use API to attempt bucket creation
    snapshots = fs_client.list_snapshots(file_system_id=fs_ocid)
    for snap in snapshots.data:
        if snap.name == SNAPSHOT_NAME:
            logging.debug(f"Deleting old Snapshot {SNAPSHOT_NAME} with OCID: {snap.id}")
            file_storage_client.delete_snapshot(snapshot_id=snap.id)
            logging.debug("Sleeping 5sec to allow deletion to complete")
            time.sleep(5)
            return


def cleanup_temporary_mount(named_mount):
    """Quietly ensures we have a clean mount point"""
    try:
        if named_mount:
            # Try to unmount named mount first if set
            command = f'{"sudo " if use_sudo else ""}umount -f {named_mount}'
            logging.debug(f"Running OS Command: {command}")
            subprocess.run(command, shell=True, check=True)

        # Try to unmount generic mount first if nothing else
        command = f'{"sudo " if use_sudo else ""}umount -f {TEMP_MOUNT}'
        logging.debug(f"Running OS Command: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.debug(f"OS: umount failed with {err} but this is ok")


def ensure_temporary_mount():
    """If mount doesn't exist"""
    if not os.path.isdir(TEMP_MOUNT):
        # Attempt create and fail if we cannot
        try:
            os.makedirs(TEMP_MOUNT)
        except Exception as ex:
            # Raise because if we cannot, we should kill the script immediately
            raise ex


def ensure_backup_bucket(oss_client, bucket) -> bool:
    """Check bucket status - create if necessary"""
    try:
        object_storage_client.get_bucket(namespace_name=namespace_name, bucket_name=bucket)
        logging.debug(f"Bucket {bucket} found")
    except oci.exceptions.ServiceError:
        logging.debug(f"Bucket {bucket} not found - creating")
        if not dry_run:
            # Fix for bucket creation error - try and catch oci.exceptions.ServiceError
            try:
                # Create a new bucket
                oss_client.create_bucket(
                    namespace_name=namespace_name,
                    create_bucket_details=oci.object_storage.models.CreateBucketDetails(
                        name=bucket,
                        compartment_id=oss_compartment_ocid,
                        storage_tier="Standard",
                        object_events_enabled=True,
                        versioning="Enabled"
                    )
                )
            except oci.exceptions.ServiceError as ex:
                logging.error(f"Unable to create backup bucket {bucket}: {ex.message}")
                return False
        else:
            logging.info(f"Dry Run: Would have created bucket {bucket} in compartment {oss_compartment_ocid}")
    # True means we are ok to proceed
    return True


def get_suitable_export(file_storage_client, virtual_network_client, mt_ocid, fs_ocid):
    """Grab the list of exports from MT and iterate. Pick one with the right mount IP and return it"""

    mount_target = file_storage_client.get_mount_target(mount_target_id=mt_ocid)
    mount_ip = virtual_network_client.get_private_ip(private_ip_id=mount_target.data.private_ip_ids[0])
    logging.debug(f"MT IP: {mount_ip.data.ip_address} ID {mount_target.data.id}")

    # Iterate And grab first suitable export
    exports = file_storage_client.list_exports(export_set_id=mount_target.data.export_set_id)
    for export in exports.data:
        if export.file_system_id == fs_ocid:
            logging.debug(f"MT {mount_ip.data.ip_address} Found {export.id} with path {export.path}")
            return f"{mount_ip.data.ip_address}:{export.path}"
    # Nothing suitable
    raise ValueError("Cannot find any matching exports")


def signal_handler(signum, frame):
    logging.warning(f"Caught signal {signum} from OS.  Cleaning up file mount before exit.")
    cleanup_temporary_mount(None)
    print("Exit")
    exit(1)


######################################
#  MAIN ROUTINE

# Define Signal Handler for cleanup
signal.signal(signal.SIGINT, signal_handler)
logging.info("Created Signal Handler for ^C")

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-fs", "--fssocid", help="FSS Compartment OCID of doing a single FS")
parser.add_argument("-fc", "--fsscompartment", help="FSS Compartment OCID", required=True)
parser.add_argument("-oc", "--osscompartment", help="OSS Backup Comaprtment OCID", required=True)
parser.add_argument("-r", "--remote", help="Named rclone remote for that user.  ie oci:", required=True)
parser.add_argument("-ad", "--availabilitydomain",
                    help="AD for FSS usage.  Such as dDzb:US-ASHBURN-AD-1",
                    required=True)
parser.add_argument("-m", "--mountocid", help="Mount Point OCID to use.", required=True)
parser.add_argument("-pr", "--profile", type=str, help="OCI Profile name (if not default)")
parser.add_argument("-ty", "--type", type=str, help="Type: daily(def), weekly, monthly", default="daily")
parser.add_argument("--dryrun", help="Dry Run - print what it would do", action="store_true")
parser.add_argument("-ssc", "--serversidecopy",
                    help="For weekly/monthly only - copies directly from latest daily backup, not source FSS",
                    action="store_true")
parser.add_argument("-s", "--sortbytes",
                    help="Sort by byte size of FSS, smallest to largest (smaller FS backed up first",
                    action="store_true")
parser.add_argument("-t", "--threshold", help="GB threshold - do not back up share if more than this", type=int)
parser.add_argument("-su", "--usesudo", help="Attempt to run mount/umount with sudo - requires /etc/sudoers", action="store_true")
args = parser.parse_args()

# Process arguments
verbose = args.verbose
use_sudo = args.usesudo
dry_run = args.dryrun
server_side_copy = args.serversidecopy
sort_bytes = args.sortbytes

# Default(None) or named
profile = args.profile

# FSS Compartment OCID
fss_compartment_ocid = args.fsscompartment if args.fsscompartment else None

# FSS Single OCID
fss_ocid = args.fssocid if args.fssocid else None

# OSS Compartment OCID
oss_compartment_ocid = args.osscompartment if args.osscompartment else None

# Mount IP
mt_ocid = args.mountocid

# RCLONE Remote
rclone_remote = args.remote

# Type (daily, weekly, monthly)
backup_type = args.type

# Availability Domain
fss_avail_domain = args.availabilitydomain

# FSS Threshold
threshold_gb = args.threshold if args.threshold else THRESHOLD_GB

# Set the log level to DEBUG or INFO
if verbose:
    logging.getLogger().setLevel(logging.DEBUG)
else:
    logging.getLogger().setLevel(logging.INFO)

# Define OSS client and Namespace
if profile:
    config = oci.config.from_file(profile_name=profile)
else:
    config = oci.config.from_file()

# Sleep for a few seconds before beginning
time.sleep(5)

# Create Clients and prepare

object_storage_client = oci.object_storage.ObjectStorageClient(config)
file_storage_client = oci.file_storage.FileStorageClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)
namespace_name = object_storage_client.get_namespace().data

# Try to see if mount is there and clean - die if not (raise unchecked)

# If we can't have the mount, die
try:
    ensure_temporary_mount()
except FileExistsError as exc:
    logging.critical(f"FATAL: No way to use mount point {TEMP_MOUNT}: {exc}")
    exit(1)

# Now clean it up if it is mounted
cleanup_temporary_mount(None)

# Explain what we are doing
if backup_type in ['weekly', 'monthly']:
    logging.info(f'Performing Daily Incremental Backup AND {backup_type} using {"Server-Side Copy" if server_side_copy else "Rclone Copy"} method')
else:
    logging.info('Performing Daily Incremental Backup')

# Print threshold if set
if threshold_gb < sys.maxsize:
    # This means it was set to anything
    logging.info(f"GB Threshold set to {threshold_gb} GB - will skip any FS larger than this")

# Set Start timer
start = time.time()

# Main loop - list File Shares

# For listing, if the fss_ocid is set to a single FS, only do that in the filter
# Else get all shares
if fss_ocid:
    shares = file_storage_client.list_file_systems(compartment_id=fss_compartment_ocid,
                                                   availability_domain=fss_avail_domain,
                                                   id=fss_ocid,
                                                   lifecycle_state="ACTIVE")
else:
    shares = file_storage_client.list_file_systems(compartment_id=fss_compartment_ocid,
                                                   availability_domain=fss_avail_domain,
                                                   lifecycle_state="ACTIVE")

# At this point iterate the list (even if single)
logging.info(f'{f"Using {fss_ocid} in" if fss_ocid else "Iterating filesystems in"} Compartment: \
{fss_compartment_ocid}.  Count: {len(shares.data)}')

# Sort by smallest to largest
if sort_bytes:
    logging.debug("Sorting FSS List smallest to largest")
    shares.data.sort(key=extract_bytes)

for share in shares.data:
    logging.info(f"Share name: {share.display_name} Size: {round(share.metered_bytes/(1024*1024*1024), 2)} GB")
    backup_bucket_name = share.display_name.strip("/") + "_backup"
    # Check size and skip this filesystem if it exceeds threshold
    if (share.metered_bytes > (threshold_gb * 1024 * 1024 * 1024)):
        logging.debug(f"File System is {round(share.metered_bytes/(1024*1024*1024), 2)} GB.  Threshold is {threshold_gb} GB.  Skipping")
        continue

    # Ensure that the bucket is there, create otherwise
    bucket_exists = ensure_backup_bucket(oss_client=object_storage_client,
                                         bucket=backup_bucket_name)

    # For for no available bucket
    if not bucket_exists:
        # Move on
        logging.warning(f"Bucket {backup_bucket_name} is not available for share {share.display_name}. Continuing.")
        continue
    # Try mount and rclone, it not, clean up snapshot
    try:    # Overall
        # Call the helper to get export path and mount
        # Get export path
        try:
            # Don't need to try here, but just in case, try and raise
            mount_path = get_suitable_export(file_storage_client, virtual_network_client,
                                             mt_ocid=mt_ocid, fs_ocid=share.id)
            logging.debug(f"Using the following mount path: {mount_path}")
        except ValueError as exc:
            logging.error("No Suitable Mount point. Continue to next share")
            logging.debug(exc)
            continue

        # Call out to OS to mount RO - try to continue if fail
        try:
            if not dry_run:
                logging.debug(f'OS: {"sudo " if use_sudo else ""}mount -r {mount_path} {TEMP_MOUNT}')
                subprocess.run([f'{"sudo" if use_sudo else ""}', "mount", "-r", f"{mount_path}", f"{TEMP_MOUNT}"], shell=False, check=True)
            else:
                logging.info(f'Dry Run: {"sudo " if use_sudo else ""}mount -r {mount_path} {TEMP_MOUNT}')
        except IOError as exc:
            logging.error(f"Unable to mount {mount_path} to {TEMP_MOUNT}. Continue to next share")
            logging.debug(exc)
            continue

        # FSS Snapshot (for clean backup) - only do it is the mount was successful
        try:    # Catch API Error
            if not dry_run:
                # Try to delete FSS Snapshot - ok if it fails
                cleanup_file_snapshot(fs_client=file_storage_client, fs_ocid=share.id)

                logging.debug(f"Creating FSS Snapshot: {SNAPSHOT_NAME} via API")
                snapstart = time.time()
                snapshot = file_storage_client.create_snapshot(
                    create_snapshot_details=oci.file_storage.models.CreateSnapshotDetails(
                        file_system_id=share.id,
                        name=SNAPSHOT_NAME)
                )
                snapend = time.time()
                logging.debug(f"FSS Snapshot time(ms): {(snapend - snapstart):.2f}s OCID: {snapshot.data.id}")
            else:
                logging.info(f"Dry Run: Create FSS Snapshot {SNAPSHOT_NAME} via API")

            # Define remote path on OSS
            remote_path = f"{rclone_remote}{backup_bucket_name}/{SNAPSHOT_NAME}"
            additional_copy_name = f"FSS-{backup_type}Backup-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
            additional_remote_path = f"{rclone_remote}{backup_bucket_name}/{additional_copy_name}"

            logging.debug(f"Using Remote Path (rclone_remote:bucket/snapshot): {rclone_remote}{backup_bucket_name}/{SNAPSHOT_NAME}")

            # Call out to rclone it
            # Additional flags to consider
            # --s3-disable-checksum  only for large objects, avoid md5sum which is slow
            # --checkers = Core Count * 2
            try:
                if not dry_run:
                    logging.debug(f"Calling rclone with rclone sync --stats 5m -v --metadata --max-backlog 999999 --links \
                        --s3-chunk-size=16M --s3-upload-concurrency={CORE_COUNT} --transfers={CORE_COUNT} \
                        --checkers={CORE_COUNT*2} /mnt/temp-backup/.snapshot/{SNAPSHOT_NAME} {remote_path}")

                    # Try / catch so as to not kill the process
                    try:
                        completed = subprocess.run(["rclone", "sync", f'{"-vv" if verbose else "-v"}', "--metadata", "--max-backlog", "999999", "--links",
                                                    "--s3-chunk-size=16M", "--stats", "5m", f"--s3-upload-concurrency={CORE_COUNT}", f"--transfers={CORE_COUNT}", f"--checkers={CORE_COUNT*3}",
                                                    f"/mnt/temp-backup/.snapshot/{SNAPSHOT_NAME}", f"{remote_path}"], shell=False, check=True)
                        logging.debug(f"RCLONE output: {completed.stdout}")
                    except subprocess.CalledProcessError:
                        logging.warning("RCLONE ERROR: Continue processing")

                    # Additional Backup if weekly or monthly selected.  Options are Direct Copy or Server Side Copy
                    if backup_type in ['weekly', 'monthly']:
                        if server_side_copy:
                            logging.debug(f'Creating additional {backup_type} backup called {additional_copy_name}. Implemented as rclone server side copy')
                            logging.debug(f"Calling rclone with rclone copy --stats 5m -v --no-check-dest--transfers={CORE_COUNT*2} --checkers={CORE_COUNT*2} {remote_path} {additional_remote_path}")
                            # Try / catch so as to not kill the process
                            try:
                                # 2x transfers since server-side
                                # Also, since integrity check, don't check dest
                                completed = subprocess.run(["rclone", "copy", "--stats", "5m", f'{"-vv" if verbose else "-v"}', "--no-check-dest", f"--transfers={CORE_COUNT*2}", f"--checkers={CORE_COUNT*3}",
                                                            f"{remote_path}", f"{additional_remote_path}"], shell=False, check=True)
                                logging.debug(f"RCLONE output: {completed.stdout}")
                            except subprocess.CalledProcessError:
                                logging.warning("RCLONE ERROR: Continue processing")
                        else:
                            # Direct Copy
                            logging.debug(f'Creating additional {backup_type} backup called {additional_copy_name}. Implemented \
                                as rclone Direct Copy from FSS (full)')
                            logging.debug(f"Calling rclone with rclone sync --stats 5m -v --metadata --max-backlog 999999 --links \
                                --s3-chunk-size=16M --s3-upload-concurrency={CORE_COUNT} --transfers={CORE_COUNT} \
                                    --checkers={CORE_COUNT*2} /mnt/temp-backup/.snapshot/{SNAPSHOT_NAME} {additional_remote_path}")

                            # Try / catch so as to not kill the process
                            try:
                                # Still do integrity check (md5sum)
                                completed = subprocess.run(["rclone", "copy", "--stats", "5m", f'{"-vv" if verbose else "-v"}', "--metadata", "--max-backlog", "999999", "--links",
                                                            "--s3-chunk-size=16M", f"--s3-upload-concurrency={CORE_COUNT}", f"--transfers={CORE_COUNT}", f"--checkers={CORE_COUNT*3}",
                                                            f"/mnt/temp-backup/.snapshot/{SNAPSHOT_NAME}", f"{additional_remote_path}"], shell=False, check=True)
                                logging.debug(f"RCLONE output: {completed.stdout}")
                            except subprocess.CalledProcessError as exc:
                                logging.warning(f"RCLONE ERROR: {exc}. Continue processing")

                else:
                    if type in ['weekly', 'monthly']:
                        if server_side_copy:
                            logging.info(f"Dry Run: rclone copy -v {remote_path} {additional_remote_path}")
                        else:
                            logging.info(f"Dry Run: rclone sync --progress --metadata --max-backlog 999999 --links \
        --transfers={CORE_COUNT} --checkers={CORE_COUNT*2} /mnt/temp-backup/.snapshot/{SNAPSHOT_NAME} {remote_path}")

            except subprocess.CalledProcessError as exc:
                logging.warning("RClonefailed. Continue processing to remove snapshot")
                logging.debug(exc)

            # Delete Snapshot - no need to keep at this point
            if not dry_run:
                logging.debug(f"Deleting Snapshot from FSS. Name: {snapshot.data.name} OCID:{snapshot.data.id}")
                try:
                    file_storage_client.delete_snapshot(snapshot_id=snapshot.data.id)
                except Exception as ex:
                    logging.warning(f"Deletion of FSS Snapshot failed.  Please record OCID: {snapshot.data.id} and delete manually.")
                    logging.debug(ex)
            else:
                logging.info(f"Dry Run: Delete Snapshot from FSS: {SNAPSHOT_NAME}")
        # Catching API errors from snapshot creation/deletion
        except oci.exceptions.RequestException as exc:
            logging.error("API Failed. Continue to cleanup mount")
            logging.debug(exc)
        except ValueError as exc:
            logging.error("No Export. Continue processing")
            logging.debug(exc)

        # Unmount File System (Cleanup)
        try:
            if not dry_run:
                cleanup_temporary_mount(mount_path)
            else:
                logging.info(f"Dry Run: umount -f {mount_path}")
        except IOError as exc:
            logging.warning("Unable to unmount. Continue to next share")
            logging.debug(exc)

        # End of main routine
        # Catch exceptions
    except Exception as exc:
        logging.warning("ERROR: Generic Exception. Continue processing")
        logging.debug(exc)
end = time.time()
logging.info(f"Finished | Time taken: {(end - start):.2f}s")
