# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import io
import six
import math
import time
import warnings
from multiprocessing.dummy import Pool
from oci.object_storage.transfer.internal.download.DownloadThread import (ParallelDownloader, SequentialDownloader,
                                                                          DownloadState)
from oci.exceptions import (ResumableDownloadException, DownloadTerminated, DownloadFailedIncorrectDownloadSize)


class DownloadManager(object):
    def __init__(self, download_config, object_storage_client, state=DownloadState.DOWNLOADING):
        """
        The DownloadManager constructor provides methods to get an object, store it to a file (given a path) or store it
        to a stream from the object storage. It splits large downloads into multiple parts to make retires smarter and
        downloads faster.

        :param DownloadConfiguration download_config: The download configuration

        :param oci.object_storage_config.ObjectStorageClient object_storage_client: The object storage client

        :param DownloadManger.DownloadState state: The state of the download manager. This governs the state of the
            download. This can be any from the enum
            ~oci.object_storage.transfer.internal.download.DownloadThread.DownloadState, namely DownloadState.DOWNLOADING,
            DownloadState.PAUSED, DownloadState.TERMINATED.
        """
        self.download_config = download_config
        self.object_storage_client = object_storage_client
        self.state = state

    def get_object(self,
                   namespace_name,
                   bucket_name,
                   object_name,
                   start_byte=0,
                   end_byte=None,
                   **kwargs):
        """
                Gets the metadata and body of an object and returns a response. If both start_byte and end_byte are None, then the metadata and
                content of the full object (of unknown size) is returned. Raises exceptions on failure. If only start_byte is
                given, then the end_byte is taken as the last byte of the object being downloaded. If only end_byte is
                given, then the start_byte is the first byte of the object. A ~oci.exceptions.ServiceError is raised if
                the object is unavailable or the range is wrong. If some unexpected keyword arguments are encountered,
                then a ValueError exception is raised.

                :param str namespace_name: (required)
                    The Object Storage namespace used for the request.

                :param str bucket_name: (required)
                    The name of the bucket. Avoid entering confidential information.
                    Example: `my-new-bucket1`

                :param str object_name: (required)
                    The name of the object. Avoid entering confidential information.
                    Example: `test/object1.log`

                :param str version_id: (optional)
                    VersionId used to identify a particular version of the object

                :param str if_match: (optional)
                    The entity tag (ETag) to match with the ETag of an existing resource. If the specified ETag matches
                    the ETag of the existing resource, GET and HEAD requests will return the resource and PUT and POST
                    requests will upload the resource.

                :param str if_none_match: (optional)
                    The entity tag (ETag) to avoid matching. Wildcards ('*') are not allowed. If the specified ETag does
                    not match the ETag of the existing resource, the request returns the expected response. If the ETag
                    matches the ETag of the existing resource, the request returns an HTTP 304 status without a response body.

                :param str opc_client_request_id: (optional)
                    The client request ID for tracing.

                :param any start_byte: (optional)
                    The byte in the content of the object from which to start the download.

                :param any end_byte: (optional)
                    The byte in the content of the object from which to stop the download.
                    Note: Both the start_byte and end_byte are included in the download.

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

                :return: A :class:`~oci.response.Response` object with data of type stream
                :rtype: :class:`~oci.response.Response`
                """

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

        if start_byte is not None:
            if end_byte is not None:
                range_header = f"bytes={start_byte}-{end_byte}"
            else:
                range_header = f"bytes={start_byte}-"
        else:
            if end_byte is not None:
                range_header = f"bytes=0-{end_byte}"
            else:
                range_header = None

        if range_header == "bytes=0-":
            # This is necessary as this means getting the whole object and this range header will give errors if the
            # object is of size 0 bytes
            range_header = None

        object_storage_client = self.object_storage_client

        if 'retry_strategy' not in kwargs:
            kwargs['retry_strategy'] = self.download_config.make_retry_strategy()

        try:
            response = object_storage_client.get_object(namespace_name=namespace_name,
                                                        bucket_name=bucket_name,
                                                        object_name=object_name,
                                                        range=range_header,
                                                        **kwargs)
            return response
        except Exception as e:
            raise e

    def get_object_to_bytes(self,
                            namespace_name,
                            bucket_name,
                            object_name,
                            progress_callback=None,
                            start_byte=0,
                            end_byte=None,
                            **kwargs):

        """
        This function is very similar to get_object. However, there is automatic multipart download and smart retries.
        If some unexpected keyword arguments are encountered, then a ValueError exception is raised.
        :param str namespace_name: (required)
                    The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param function progress_callback: (optional)
            This function is used to update the progress bar of the download operation.
            The arguments that it takes are (total_bytes_downloaded_so_far, total_bytes_to_download)

        :param any start_byte: (optional)
            The byte in the content of the object from which to start the download.

        :param any end_byte: (optional)
            The byte in the content of the object from which to stop the download.
            Note: Both the start_byte and end_byte are included in the download.

        :return: A :class:`~oci.response.Response` object with data of type io.BytesIO()
        :rtype: :class:`~oci.response.Response`
        """

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

        stream = io.BytesIO()
        response = self.get_object_to_stream(namespace_name, bucket_name, object_name, stream, progress_callback,
                                             start_byte, end_byte, **kwargs)
        response.data = stream.getvalue()
        return response

    def get_object_to_text(self,
                           namespace_name,
                           bucket_name,
                           object_name,
                           progress_callback=None,
                           start_byte=0,
                           end_byte=None,
                           encoding='utf-8',
                           **kwargs):

        """This function is similar to the get_object_to_bytes function, but it will also decode the content and return
        the response object. If some unexpected keyword arguments are encountered, then a ValueError exception is
        raised.

        :param str namespace_name: (required)
                    The Object Storage namespace used for the request.

        :param str bucket_name: (required)
            The name of the bucket. Avoid entering confidential information.
            Example: `my-new-bucket1`

        :param str object_name: (required)
            The name of the object. Avoid entering confidential information.
            Example: `test/object1.log`

        :param function progress_callback: (optional)
            This function is used to update the progress bar of the download operation.
            The arguments that it takes are (total_bytes_downloaded_so_far, total_bytes_to_download)

        :param any start_byte: (optional)
            The byte in the content of the object from which to start the download.

        :param any end_byte: (optional)
            The byte in the content of the object from which to stop the download.
            Note: Both the start_byte and end_byte are included in the download.

        :param str encoding: (optional) The default value of encoding is 'utf-8'.

        :return: A :class:`~oci.response.Response` object with decoded data.
        :rtype: :class:`~oci.response.Response`
        """
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

        response = self.get_object_to_bytes(namespace_name, bucket_name, object_name, progress_callback, start_byte,
                                            end_byte, **kwargs)
        response.data = response.data.decode(encoding)

        return response

    def get_object_to_path(self,
                           namespace_name,
                           bucket_name,
                           object_name,
                           destination_path=None,
                           progress_callback=None,
                           start_byte=0,
                           end_byte=None,
                           **kwargs
                           ):
        """
                Puts the content of the object into the file specified by the path.
                If all went well, it returns a response object where the data is None (as it is already written to
                disk). Connection is closed. Else, there are three types of exceptions that can be raised.
                ResumableDownloadException is raised when some parts from a multipart download failed. These parts are
                as an attribute of the exception. The user can use these only retry these parts as the rest of the parts
                would already be written. Hence, it is advised to use this method in a try and except block.
                The file addressed by destination_path will be created if it does not exist. An empty file will be
                created even if the download failed or was cancelled. If the destination path is not specified then a
                file name "download_"+object_name is created in the directory the program was executed in.
                A ~oci.exceptions.ServiceError is raised if the object is unavailable or the range is wrong.
                The integrity of the download is verified by checking if the downloaded bytes (i.e. the number of bytes
                written into the file) is the same as the object size. If this fails, then an
                ~oci.exceptions.DownloadFailedIncorrectDownloadSize exception is raised. If some unexpected keyword
                arguments are encountered, then a ValueError exception is raised.

                :param str namespace_name: (required)
                    The Object Storage namespace used for the request.

                :param str bucket_name: (required)
                    The name of the bucket. Avoid entering confidential information.
                    Example: `my-new-bucket1`

                :param str object_name: (required)
                    The name of the object. Avoid entering confidential information.
                    Example: `test/object1.log`

                :param str destination_path: (required)
                    The path of the file where the object's content must be stored.

                :param function progress_callback: (optional)
                    This function is used to update the progress bar of the download operation.
                    The arguments that it takes are (total_bytes_downloaded_so_far, total_bytes_to_download)

                :param any start_byte: (optional)
                    The byte in the content of the object from which to start the download.

                :param any end_byte: (optional)
                    The byte in the content of the object from which to stop the download.
                    Note: Both the start_byte and end_byte are included in the download.

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

                :return: A :tuple:(int bytes downloaded, `~oci.response.Response` object with data of type None)
                :rtype: :tuple:(int, `~oci.response.Response`)
                """
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

        if destination_path is None:
            destination_path = "download_" + object_name

        with io.open(destination_path, 'wb') as out_stream:
            bytes_written, response = self.get_object_to_stream(namespace_name, bucket_name, object_name, out_stream,
                                                                progress_callback, start_byte, end_byte, **kwargs)
        return bytes_written, response

    def get_object_to_stream(self,
                             namespace_name,
                             bucket_name,
                             object_name,
                             stream,
                             progress_callback=None,
                             start_byte=0,
                             end_byte=None,
                             **kwargs
                             ):
        """
        This function gets the object and dumps the object data into the provided stream. Other behaviour is similar to
        get_object_to_path. If some unexpected keyword arguments are encountered, then a ValueError exception is raised.

        :return: A :tuple:(int bytes downloaded, `~oci.response.Response` object with data of type None)
        :rtype: :tuple:(int, `~oci.response.Response`)
        """
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

        if 'retry_strategy' not in kwargs:
            kwargs['retry_strategy'] = self.download_config.make_retry_strategy()

        download_config = self.download_config
        do_multithread = download_config.get_allow_multipart()

        if download_config.get_num_download_threads() > 1:
            if not stream.seekable():  # Check if the stream is seekable or not
                warnings.warn("The stream provided is not seekable. Performing single threaded download")
                do_multithread = False

        if (start_byte is not None) and (end_byte is not None):
            if download_config.get_part_size_in_bytes() > (end_byte - start_byte + 1):
                do_multithread = False

        response = self.get_object(namespace_name, bucket_name, object_name, start_byte, end_byte, **kwargs)

        object_size_in_bytes = int(response.headers['Content-Length'])

        if object_size_in_bytes == 0:
            return 0, response

        if not do_multithread:
            try:
                bytes_downloaded = 0

                for chunk in response.data.iter_content(chunk_size=download_config.get_part_size_in_bytes()):
                    while self.state == DownloadState.PAUSED:
                        time.sleep(self.download_config.get_pause_wait_in_seconds())
                    if self.state == DownloadState.TERMINATED:
                        stream.seek(0)
                        stream.truncate()
                        raise DownloadTerminated("Download canceled, Thread Stopped")

                    start = stream.tell()
                    stream.write(chunk)
                    end = stream.tell()
                    bytes_downloaded += (end - start)
                    if progress_callback:
                        progress_callback(bytes_downloaded,
                                          object_size_in_bytes)
                response.data = None

                # Perform a simple integrity check by seeing if the total bytes downloaded are what we need.
                if bytes_downloaded != object_size_in_bytes:
                    raise DownloadFailedIncorrectDownloadSize(bytes_downloaded,
                                                              object_size_in_bytes)
                return bytes_downloaded, response

            except Exception as e:
                raise e

        else:
            # Now we need to identify the right start and end offset values for the first part. We need it to find the
            # right number of byte to download. We also need to set the end_byte if None appropriately as the
            # object_size_in_bytes will not have the full object's size in bytes. It will change if the user specifies
            # a start offset.

            if start_byte is None:
                if end_byte is None:
                    first_part_start_offset = 0
                    # The first part can be bigger than the total object if the object is small. Here the last byte of
                    # the first part can either be the last byte of the object or the appropriate value for a part.
                    first_part_end_offset = min(object_size_in_bytes - 1, download_config.part_size_in_bytes - 1)
                    # Set the end_byte to the last byte of the object. The end_byte is different from the
                    # first_part_end_offset
                    end_byte = object_size_in_bytes - 1
                else:
                    first_part_start_offset = 0
                    # Here the last byte of the first part can be the object's last byte, the last requested byte or the
                    # appropriate value for a part.
                    first_part_end_offset = min(object_size_in_bytes - 1, end_byte,
                                                download_config.part_size_in_bytes - 1)
            else:
                if end_byte is None:
                    first_part_start_offset = start_byte
                    # Here the last byte of the first part can be the object's last byte (content length + start_byte),
                    # or the appropriate value of a part.
                    first_part_end_offset = min(start_byte + object_size_in_bytes - 1,
                                                start_byte + download_config.part_size_in_bytes - 1)
                    # Since the object size returned is less than the actual by the start byte requested, we add it.
                    end_byte = object_size_in_bytes - 1 + start_byte

                else:
                    first_part_start_offset = start_byte
                    # Here the last byte of the first part can be the object's last byte (content length + start_byte),
                    # the requested last byte, or the appropriate value of a part.
                    first_part_end_offset = min(start_byte + object_size_in_bytes - 1, end_byte,
                                                start_byte + download_config.part_size_in_bytes - 1)

            bytes_to_download = min(object_size_in_bytes, first_part_end_offset - first_part_start_offset + 1)

            kwargs["if_match"] = response.headers['ETag']

            stream_start = stream.tell()
            stream.write(next(response.data.iter_content(chunk_size=bytes_to_download)))
            stream_end = stream.tell()

            bytes_downloaded = stream_end - stream_start

            if progress_callback:
                progress_callback(bytes_downloaded, object_size_in_bytes)
            response.data = None

            if first_part_end_offset >= end_byte:

                # Perform a simple integrity check by seeing if the total bytes downloaded are what we need.
                if bytes_downloaded != object_size_in_bytes:
                    raise DownloadFailedIncorrectDownloadSize(bytes_downloaded,
                                                              object_size_in_bytes)

                return bytes_downloaded, response
            else:
                total_bytes_downloaded = self.__get_in_parts_to_stream(namespace_name, bucket_name, object_name, stream,
                                                                       bytes_downloaded, object_size_in_bytes,
                                                                       progress_callback, first_part_end_offset + 1,
                                                                       end_byte, **kwargs)

                # Perform a simple integrity check by seeing if the total bytes downloaded are what we need.
                if total_bytes_downloaded != object_size_in_bytes:
                    raise DownloadFailedIncorrectDownloadSize(total_bytes_downloaded,
                                                              object_size_in_bytes)

                return total_bytes_downloaded, response

    def __get_in_parts_to_stream(self,
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

        """
        A private function called by get_object_to_stream if multipart download is to be done.
        Returns a response object with data of type None.  A ~oci.exceptions.ServiceError is raised if the object is
        unavailable or the range is wrong. A ~oci.exceptions.ResumableDownloadException occurs when some parts fail to
        download. These parts are present in the exception raised. If some
        unexpected keyword arguments are encountered, then a ValueError exception is raised.

        :return: An integer. It returns the number of bytes downloaded into the stream.
        :rtype: int
        """
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

        download_config = self.download_config
        num_parts = math.ceil((end_byte - start_byte + 1) / download_config.part_size_in_bytes)
        num_actual_threads = min(num_parts, download_config.get_num_download_threads())

        if num_actual_threads > 1:
            parallel_downloader = ParallelDownloader(self, download_config, self.object_storage_client, namespace_name,
                                                     bucket_name, object_name, stream, bytes_downloaded, object_size,
                                                     progress_callback,
                                                     start_byte, end_byte, **kwargs)

            with Pool(processes=num_actual_threads) as pool:
                pool.map(parallel_downloader.get_part_with_start_byte, parallel_downloader.get_start_bytes())

            total_bytes_downloaded = parallel_downloader.get_response()

            if total_bytes_downloaded == -1:
                raise ResumableDownloadException(namespace_name,
                                                 bucket_name,
                                                 object_name,
                                                 parallel_downloader.failed_parts  # Failed parts has the failed and the
                                                                                   # exception raised.
                                                 )
            else:
                return total_bytes_downloaded

        else:
            sequential_downloader = SequentialDownloader(self, download_config, self.object_storage_client,
                                                         namespace_name, bucket_name, object_name, stream,
                                                         bytes_downloaded, object_size,
                                                         progress_callback, start_byte, end_byte, **kwargs)

            for part in sequential_downloader.get_start_bytes():
                sequential_downloader.get_part_with_start_byte(part)

            total_bytes_downloaded = sequential_downloader.get_response()

            if total_bytes_downloaded == -1:
                raise ResumableDownloadException(namespace_name,
                                                 bucket_name,
                                                 object_name,
                                                 sequential_downloader.failed_parts
                                                 # Failed parts has the failed and the
                                                 # exception raised.
                                                 )
            else:
                return total_bytes_downloaded

    def resume_parts_to_path_multithread(self, namespace_name, bucket_name, object_name, parts, destination_path,
                                         **kwargs):
        """
        This method used to download a set of parts into the same offset into the file at `destination_path`. For
        example part (100,600) will be written into the file from the 100th byte. This is usually used to download the
        failed parts in a multipart download. If some parts again fail to download and is captured, then a
        ~oci.exceptions.ResumableDownloadException exception is raised. The integrity of the download is verified by
        checking if the downloaded bytes (i.e. the number of bytes written into the file) is the same as the object
        size. If this fails, then an ~oci.exceptions.DownloadFailedIncorrectDownloadSize exception is raised. If some
        unexpected keyword arguments are encountered, then a ValueError exception is raised. It returns the number of
        bytes downloaded into the stream.


        :param: str namespace_name: (required)
            The namespace name.
        :param: str bucket_name: (required)
            The bucket name.
        :param: str object_name: (required)
            The object name.
        :param: iterable parts: (required)
            A list of the parts to download. It should of the form ((start_byte,end_byte),
            (start_byte,end_byte),...).
        :param: str destination_path: (required)
            The destination path.

        :return: An integer. It returns the number of bytes downloaded into the stream.
        :rtype: int
        """
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

        with io.open(destination_path, "r+b") as out_stream:
            return self.resume_parts_to_stream_multithread(namespace_name, bucket_name, object_name, parts, out_stream,
                                                           **kwargs)

    def resume_parts_to_stream_multithread(self, namespace_name, bucket_name, object_name, parts, stream, **kwargs):
        """
        This method used to download a set of parts into the same offset into the stream. For example
        part (100,600) will be written into the file from the 100th byte. This is usually used to download the failed
        parts in a multipart download. If some parts again fail to download and is captured, then a
        ~oci.exceptions.ResumableDownloadException exception is raised. The integrity of the download is verified by
        checking if the downloaded bytes (i.e. the number of bytes written into the file) is the same as the object
        size. If this fails, then an ~oci.exceptions.DownloadFailedIncorrectDownloadSize exception is raised. If some
        unexpected keyword arguments are encountered, then a ValueError exception is raised. It returns the number of
        bytes downloaded into the stream.


        :param: str namespace_name: (required)
            The namespace name.
        :param: str bucket_name: (required)
            The bucket name.
        :param: str object_name: (required)
            The object name.
        :param: iterable parts: (required)
            A list of the parts to download. It should of the form [(start_byte,end_byte),
            (start_byte,end_byte),...].
        :param: bytestream stream: (required)
            The destination stream.

        :return: An integer. It returns the number of bytes downloaded into the stream.
        :rtype: int
        """
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

        total_size = sum([part[1] - part[0] + 1 for part in parts])
        num_threads = min(self.download_config.get_num_download_threads(), len(parts))

        if num_threads == 0:
            return 0

        parallel_downloader = ParallelDownloader(
            self, self.download_config, self.object_storage_client,
            namespace_name, bucket_name, object_name, stream, 0, total_size, **kwargs
        )

        with Pool(processes=num_threads) as pool:
            pool.map(parallel_downloader.get_part_with_start_byte, self.__get_start_byte_from_parts(parts))

        total_bytes_downloaded = parallel_downloader.get_response()

        if total_bytes_downloaded == -1:
            raise ResumableDownloadException(namespace_name,
                                             bucket_name,
                                             object_name,
                                             parallel_downloader.failed_parts
                                             )

        if total_bytes_downloaded != total_size:
            raise DownloadFailedIncorrectDownloadSize(total_bytes_downloaded,
                                                      total_size)
        else:
            return total_bytes_downloaded

    def __get_start_byte_from_parts(self, parts):
        """
        Private helper function to yield the start byte from an iterable of parts

        :param: iterable parts - A list of the parts to download of the form [(start_byte,end_byte),
            (start_byte,end_byte),...].
        """
        for part in parts:
            yield part[0]
