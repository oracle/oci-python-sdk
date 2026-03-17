# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import six
import time
import multiprocessing
from enum import Enum
from oci.exceptions import DownloadTerminated, DownloadFailedIncorrectDownloadSize


class DownloadState(Enum):
    DOWNLOADING = 0
    PAUSED = 1
    TERMINATED = 2


class DownloadThread(object):
    """
    The main class whose methods the threads use to perform the downloads and write to the stream.

    :param: DownloadManager download_manager: The download manger object

    :param: DownloadConfiguration download_configuration: The download configuration object

    :param: ObjectStorageClient object_storage_client: The object storage client

    :param: str namespace_name: The namespace name

    :param: str bucket_name: The bucket name

    :param: str object_name: The object name

    :param: bytestream stream: The stream to write into

    :param: int bytes_downloaded: The bytes downloaded so far before invoking this.

    :param: int object_size: The total size of the download in bytes, including the bytes already downloaded

    :param function progress_callback: (optional)
                    This function is used to update the progress bar of the download operation.
                    The arguments that it takes are (total_bytes_downloaded_so_far, total_bytes_to_download)

    :param any start_byte: (optional)
        The byte in the content of the object from which to start the download. The default value is 0

    :param any end_byte: (optional)
        The byte in the content of the object from which to stop the download. The default value is the last byte of the
        object.
        Note: Both the start_byte and end_byte are included in the download.

    :param: bool did_some_parts_fail: True if some parts fail to download.

    :param: dict failed_parts: A dictionary filled with all the failed parts. Key: Failed part, Value: Error
        {(start_byte, end_byte) : error, (start_byte, end_byte): error,...}

    :param str version_id: (optional)
        VersionId used to identify a particular version of the object

    :param str if_match: (optional)
        The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches
        the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST
        requests will upload the resource.

    :param str if_none_match: (optional)
        The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does
        not match the ETag of the existing resource, the request returns the expected response. If the ETag
        matches the ETag of the existing resource, the request returns an HTTP 304 status without a response
        body.

    :param str opc_client_request_id: (optional)
        The client request ID for tracing.


    :param str opc_sse_customer_algorithm: (optional)
        The optional header that specifies \"AES256\" as the encryption algorithm. For more information, see
        `Using Your Own Keys for Server-Side Encryption`__.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

    :param str opc_sse_customer_key: (optional)
        The optional header that specifies the base64-encoded 256-bit encryption key to use to encrypt or
        decrypt the data. For more information, see
        `Using Your Own Keys for Server-Side Encryption`__.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

    :param str opc_sse_customer_key_sha256: (optional)
        The optional header that specifies the base64-encoded SHA256 hash of the encryption key. This
        value is used to check the integrity of the encryption key. For more information, see
        `Using Your Own Keys for Server-Side Encryption`__.

        __ https://docs.cloud.oracle.com/Content/Object/Tasks/usingyourencryptionkeys.htm

    :param str http_response_content_disposition: (optional)
        Specify this query parameter to override the value of the Content-Disposition response header in the
        GetObject response.

    :param str http_response_cache_control: (optional)
        Specify this query parameter to override the Cache-Control response header in the GetObject
        response.

    :param str http_response_content_type: (optional)
        Specify this query parameter to override the Content-Type response header in the GetObject response.

    :param str http_response_content_language: (optional)
        Specify this query parameter to override the Content-Language response header in the GetObject
        response.

    :param str http_response_content_encoding: (optional)
        Specify this query parameter to override the Content-Encoding response header in the GetObject
        response.

    :param str http_response_expires: (optional)
        Specify this query parameter to override the Expires response header in the GetObject response.

    :param obj retry_strategy: (optional)
        A retry strategy to apply to this specific operation/call. This will override any retry strategy
        set at the client-level.

        This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation
        uses :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` as default if no retry strategy is provided.
        The specifics of the default retry strategy are described
        `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        To have this operation explicitly not perform any retries, pass an instance of
        :py:class:`~oci.retry.NoneRetryStrategy`.

    :param bool allow_control_chars: (optional)
        allow_control_chars is a boolean to indicate whether or not this request should allow control
        characters in the response object.
        By default, the response will not allow control characters in strings
    """
    def __init__(self,
                 download_manager,
                 download_config,
                 object_storage_client,
                 namespace_name,
                 bucket_name,
                 object_name,
                 stream,
                 bytes_downloaded,
                 object_size,
                 progress_callback=None,
                 start_byte=0,
                 end_byte=None,
                 **kwargs
                 ):
        self.download_manager = download_manager
        self.download_config = download_config
        self.object_storage_client = object_storage_client
        self.namespace_name = namespace_name
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.stream = stream
        self.stream_original_start = self.stream.tell()
        self.bytes_downloaded = bytes_downloaded
        self.object_size = object_size
        self.progress_callback = progress_callback
        self.start_byte = start_byte
        self.end_byte = end_byte
        self.did_some_parts_fail = False
        self.failed_parts = {}

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "version_id",
            "if_match",
            "if_none_match",
            "opc_client_request_id",
            "opc_sse_customer_algorithm",
            "opc_sse_customer_key",
            "opc_sse_customer_key_sha256",
            "http_response_content_disposition",
            "http_response_cache_control",
            "http_response_content_type",
            "http_response_content_language",
            "http_response_content_encoding",
            "http_response_expires"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                f"get_object got unknown kwargs: {extra_kwargs!r}")

        self.header_args = kwargs

    def get_start_bytes(self):
        # Get the start bytes of the parts
        start_byte = self.start_byte
        while start_byte <= self.end_byte:
            yield start_byte
            start_byte += self.download_config.part_size_in_bytes

    def get_response(self):
        # Get the response from the multipart get operation
        if self.did_some_parts_fail:
            return -1

        return self.bytes_downloaded

    def get_part_with_start_byte(self, part_start_byte):
        # This is overwritten by the SequentialDownloader and ParallelDownloader.
        # This performs the get operation for the specific part.
        pass

    def write_part_to_stream(self, part_content, part_start_byte):
        # This is overwritten by the SequentialDownloader and ParallelDownloader.
        # This writes the content for the response of the get operation of the part into the stream.
        pass


class SequentialDownloader(DownloadThread):

    def __init__(self,
                 download_manager,
                 download_config,
                 object_storage_client,
                 namespace_name,
                 bucket_name,
                 object_name,
                 stream,
                 bytes_downloaded,
                 object_size,
                 progress_callback=None,
                 start_byte=0,
                 end_byte=None,
                 **kwargs
                 ):
        super(SequentialDownloader, self).__init__(download_manager, download_config, object_storage_client,
                                                   namespace_name, bucket_name, object_name, stream, bytes_downloaded,
                                                   object_size, progress_callback, start_byte,
                                                   end_byte, **kwargs)

    def write_part_to_stream(self, part_content, part_start_byte):
        stream_start = self.stream_original_start + part_start_byte - self.start_byte
        self.stream.seek(stream_start)
        self.stream.write(part_content)
        stream_end = self.stream.tell()
        self.callback(stream_end - stream_start)
        return stream_end - stream_start

    def callback(self, downloaded_bytes):
        self.bytes_downloaded += downloaded_bytes
        total_bytes_downloaded = self.bytes_downloaded

        if self.progress_callback:
            self.progress_callback(total_bytes_downloaded, self.object_size)

    def get_part_with_start_byte(self, part_start_byte):

        while self.download_manager.state == DownloadState.PAUSED:
            time.sleep(self.download_config.pause_wait_in_seconds)

        if self.download_manager.state == DownloadState.TERMINATED:
            self.stream.seek(0)
            self.stream.truncate()
            self.stream.close()

            raise DownloadTerminated("Download canceled, Thread Stopped")

        if self.end_byte:
            part_end_byte = min(self.end_byte, part_start_byte + self.download_config.part_size_in_bytes - 1)
        else:
            part_end_byte = part_start_byte + self.download_config.part_size_in_bytes - 1

        object_storage_client = self.object_storage_client
        range_header = f"bytes={part_start_byte}-{part_end_byte}"

        if 'retry_strategy' not in self.header_args:
            self.header_args['retry_strategy'] = self.download_config.make_retry_strategy()

        try:
            response = object_storage_client.get_object(self.namespace_name, self.bucket_name, self.object_name,
                                                        range=range_header, **self.header_args)
            part_content = response.data.content
            response.data.close()
            part_size_in_bytes = part_end_byte - part_start_byte + 1
            if part_size_in_bytes > 0:
                bytes_written = self.write_part_to_stream(part_content, part_start_byte)
                if bytes_written != part_size_in_bytes:
                    self.did_some_parts_fail = True
                    self.failed_parts[(part_start_byte, part_end_byte)] = DownloadFailedIncorrectDownloadSize(
                        bytes_written, part_size_in_bytes
                    )

        except Exception as e:
            self.did_some_parts_fail = True
            self.failed_parts[(part_start_byte, part_end_byte)] = e


class ParallelDownloader(DownloadThread):
    def __init__(self,
                 download_manager,
                 download_config,
                 object_storage_client,
                 namespace_name,
                 bucket_name,
                 object_name,
                 stream,
                 bytes_downloaded,
                 object_size,
                 progress_callback=None,
                 start_byte=0,
                 end_byte=None,
                 **kwargs
                 ):
        super(ParallelDownloader, self).__init__(download_manager, download_config, object_storage_client,
                                                 namespace_name, bucket_name, object_name, stream, bytes_downloaded,
                                                 object_size, progress_callback,
                                                 start_byte, end_byte, **kwargs)

        self.stream_lock = multiprocessing.Lock()
        self.callback_lock = multiprocessing.Lock()
        self.failed_parts_lock = multiprocessing.Lock()

    def write_part_to_stream(self, part_content, part_start_byte):
        with self.stream_lock:
            stream_start = self.stream_original_start + part_start_byte - self.start_byte
            self.stream.seek(stream_start)
            self.stream.write(part_content)
            stream_end = self.stream.tell()
            self.callback(stream_end - stream_start)
            return stream_end - stream_start

    def callback(self, downloaded_bytes):
        with self.callback_lock:
            self.bytes_downloaded += downloaded_bytes
            total_bytes_downloaded = self.bytes_downloaded

        if self.progress_callback:
            self.progress_callback(total_bytes_downloaded, self.object_size)

    def get_part_with_start_byte(self, part_start_byte):
        while self.download_manager.state == DownloadState.PAUSED:
            time.sleep(self.download_config.pause_wait_in_seconds)
        if self.download_manager.state == DownloadState.TERMINATED:
            self.stream.seek(0)
            self.stream.truncate()
            self.stream.close()
            raise DownloadTerminated("Download canceled, Thread Stopped")

        if self.end_byte:
            part_end_byte = min(self.end_byte, part_start_byte + self.download_config.part_size_in_bytes - 1)
        else:
            part_end_byte = part_start_byte + self.download_config.part_size_in_bytes - 1

        object_storage_client = self.object_storage_client
        range_header = f"bytes={part_start_byte}-{part_end_byte}"

        if 'retry_strategy' not in self.header_args:
            self.header_args['retry_strategy'] = self.download_config.make_retry_strategy()

        try:
            response = object_storage_client.get_object(self.namespace_name, self.bucket_name, self.object_name,
                                                        range=range_header, **self.header_args)
            part_content = response.data.content
            response.data.close()
            part_size_in_bytes = part_end_byte - part_start_byte + 1
            if part_size_in_bytes > 0:
                bytes_written = self.write_part_to_stream(part_content, part_start_byte)
                if bytes_written != part_size_in_bytes:
                    with self.failed_parts_lock:
                        self.did_some_parts_fail = True
                        self.failed_parts[(part_start_byte, part_end_byte)] = DownloadFailedIncorrectDownloadSize(
                            bytes_written, part_size_in_bytes
                        )

        except Exception as e:

            with self.failed_parts_lock:
                self.did_some_parts_fail = True
                self.failed_parts[(part_start_byte, part_end_byte)] = e
