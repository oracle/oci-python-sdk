# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import oci
import sys
import time
from oci.object_storage import UploadManager
from oci.object_storage.transfer.constants import MEBIBYTE
from oci.object_storage.transfer.internal.download.DownloadConfiguration import DownloadConfiguration
from oci.object_storage.transfer.internal.download.DownloadManager import DownloadManager
from oci.object_storage.transfer.internal.download.DownloadThread import DownloadState
from oci.retry.retry import NoneRetryStrategy, BACKOFF_FULL_JITTER_VALUE
from oci.exceptions import ResumableDownloadException, DownloadTerminated


def upload_progress_callback(bytes_uploaded):
    print(f"{bytes_uploaded} additional bytes uploaded")


def on_press(key, download_manager):
    try:
        if key.char == 'p':
            if download_manager.state == 0:
                print("Download Paused!\n")
                download_manager.state = 1
                return

            if download_manager.state == 1:
                print("Download Resumed!\n")
                download_manager.state = 0
                return

        if key.char == 'q':
            print("Terminating Download!\n")
            download_manager.state = -1
            return

    except AttributeError:
        pass


def print_progress_bar(downloaded_bytes, total_bytes, bar_length=60):
    if (total_bytes == 0):
        print(f"Starting Download\n[{'#' * 0 + '-' * (bar_length - 0)}] {0 * 100:.2f}%")
    else:
        progress = downloaded_bytes / total_bytes
        block = int(round(bar_length * progress))
        progress_bar = f"[{'#' * block + '-' * (bar_length - block)}] {progress * 100:.2f}%"

        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
        print(f"Downloading: {downloaded_bytes}/{total_bytes} bytes\n{progress_bar}")
        sys.stdout.flush()


if __name__ == '__main__':
    """
    This example program works as follows.
    1) First we upload an object to an existing bucket.
    2) Then we download it.
    3) While the download is in progress, press p on the keyboard to pause the download and p again to resume, q to
    cancel the download.
    # Please note that while the download is in progress don't type else where as the key presses will be registered as
    pause or terminate signals.

    Below are the parameters that are to be filled. Running this program in the terminal is good option as the download
    progress is seen better that way.

    PLEASE NOTE THAT THIS EXAMPLE USES pynput (pip install pynput) so it is advisable to re install all packages in the
    requirements.txt.

    Use `diff uploaded_file_name downloaded_file_name` in the terminal to check if the uploaded and downloaded files are
    the same.

    The Progress call back can add significant delays to the overall download speed.

    Fill the following parameters:
    """
    namespace = "bm2ywytyr7us"  # Put your namespace
    bucket_name = "bucket-20240527-1635"  # Put your bucket name
    object_name = "11MB_dummy.txt"  # Put your object name or leave it as it is.
    upload_filename = r'11MB_dummy.txt'
    download2path = r'down_11MB_dummy.txt'
    file_size_in_mebibytes = 11
    part_size = int(1 * MEBIBYTE)
    num_connections = 4

    print(f"Part size is {part_size} MB")
    print(f"Number of connections is {num_connections}")

    object_storage_client_config = oci.config.from_file()

    compartment_id = object_storage_client_config["tenancy"]
    object_storage = oci.object_storage.ObjectStorageClient(object_storage_client_config)

    # create example file to upload
    sample_content = b'a'
    with open(upload_filename, 'wb') as f:
        while f.tell() < MEBIBYTE * file_size_in_mebibytes:
            f.write(sample_content * MEBIBYTE)

    print(f"Uploading new object {object_name!r}")

    start_time = time.time()
    upload_manager = UploadManager(object_storage, allow_parallel_uploads=True, parallel_process_count=num_connections)
    response = upload_manager.upload_file(
        namespace, bucket_name, object_name, upload_filename, part_size=part_size)

    end_time = time.time()
    print("Time taken to upload file: ", end_time - start_time)

    download_configuration = DownloadConfiguration(allow_multipart=True, num_download_threads=num_connections,
                                                   part_size_in_bytes=part_size, max_retries=1,
                                                   backoff_type=BACKOFF_FULL_JITTER_VALUE)

    download_manager = DownloadManager(download_configuration, object_storage, DownloadState.DOWNLOADING)

    print_progress_bar(0, 0)

    start = time.time()
    retry_strategy = NoneRetryStrategy()
    try:
        bytes_written, down_response = download_manager.get_object_to_path(namespace, bucket_name, object_name,
                                                                           download2path,
                                                                           progress_callback=print_progress_bar)
        end = time.time()
        print("--------------------------------------------------------")
        print("Download Headers:\n", down_response.headers)
        print("Download took {} seconds".format(end - start))
        os.remove(upload_filename)
        os.remove(download2path)

    except Exception as e:
        exception = e
        while True:
            if isinstance(exception, ResumableDownloadException):
                print("Failed parts: ", exception.failed_parts)
                ans = (input(
                    "Retry the failed parts parallely using resume_parts_to_path_multithread() method? [y/n] ").strip().lower())

                if ans == "y":
                    try:
                        _ = download_manager.resume_parts_to_path_multithread(namespace, bucket_name, object_name,
                                                                              list(exception.failed_parts.keys()),
                                                                              download2path)
                        os.remove(upload_filename)
                        os.remove(download2path)
                        break  # Exit the loop after retrying
                    except ResumableDownloadException as e:
                        print("ResumableDownloadException occurred again.")
                        exception = e
                        continue
                    except Exception as retry_exception:
                        raise retry_exception
                        # Exit the loop if an unexpected exception occurs during retry
                else:
                    break  # Exit the loop if the user chooses not to retry
            elif isinstance(exception, DownloadTerminated):
                print("Download was terminated")
                break
            else:
                raise exception
