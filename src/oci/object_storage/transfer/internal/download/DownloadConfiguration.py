# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.object_storage.transfer.constants import MEBIBYTE
from oci.retry.retry import (RetryStrategyBuilder, VALID_BACKOFF_TYPES, BACKOFF_DECORRELATED_JITTER_VALUE)


DOWNLOAD_MANAGER_RETRYABLE_STATUSES_AND_CODES = {
    -1: [],
    409: ["ConcurrentObjectUpdate"],
    429: [],
    404: [],
    416: []
}


class DownloadConfiguration(object):
    """
    An object of this class is used to specify the download parameters to the Download Manager

    :param bool allow_multipart: If True, then multipart download if feasible, will be done. If False, then
        multipart download will not be done in any case. Default is True.

    :param int part_size_in_bytes: The size of a part that will be downloaded. This is also the smallest amount of
        bytes that will be downloaded. That is if the file size exceeds this threshold, then multipart download will
        be done, respecting the do_multipart variable. Default is 5 MB

    :param int num_download_threads: The number of threads that will be used to download the file. This value will
        be overwritten in accordance with the do_multipart variable and the file size and part_size_in_bytes. Small
        files will be downloaded in a single thread. Note that the parent thread won't be counted in this. Default
        is 3

    :param int pause_wait_in_seconds: The number of seconds to make a download thread sleep while being paused state
        before polling for the state again. Default is 2

    :param int max_retries: The maximum number of retries that will be performed on the download thread. Each thread
        will attempt to download the file until it reaches the maximum number of retries in case of failures. The
        first download attempt is also counted as a retry. So max_retries equals the maximum number of times
        download will be tried. Default is 3

    :param int initial_backoff_seconds: The initial backoff time in seconds before the first retry. Defaults to 1 second.

    :param int max_backoff_seconds: The maximum backoff time in seconds between retries. Defaults to 30 seconds

    :param int retry_exponential_growth_factor: For exponential backoff with jitter, the exponent which we will raise to
        the power of the number of attempts. If not provided, this value defaults to 2

    :param int decorrelated_jitter:
        The random De-correlated jitter value in seconds (default 1) to be used when using the backoff_type
        BACKOFF_DECORRELATED_JITTER_VALUE

    :param str backoff_type:
        The type of backoff we want to do (e.g. full jitter). The convenience constants in this retry module: ``BACKOFF_DECORRELATED_JITTER_VALUE``,
        ``BACKOFF_FULL_JITTER_VALUE``,`BACKOFF_EQUAL_JITTER_VALUE``, and ``BACKOFF_FULL_JITTER_EQUAL_ON_THROTTLE_VALUE`` can be used as values here.
        If no value is specified then the value ``BACKOFF_DECORRELATED_JITTER_VALUE`` will be used. This will use exponential backoff and a
        random de-correlated jitter.

    """

    def __init__(self,
                 allow_multipart=True,
                 part_size_in_bytes=5 * MEBIBYTE,
                 num_download_threads=3,
                 pause_wait_in_seconds=2,
                 max_retries=3,
                 initial_backoff_seconds=1,
                 max_backoff_seconds=30,
                 retry_exponential_growth_factor=2,
                 decorrelated_jitter=1,
                 backoff_type=BACKOFF_DECORRELATED_JITTER_VALUE,
                 ):

        self.allow_multipart = allow_multipart
        self.set_allow_multipart(allow_multipart)
        self.num_download_threads = num_download_threads
        self.set_num_download_threads(num_download_threads)
        self.part_size_in_bytes = part_size_in_bytes
        self.set_part_size_in_bytes(part_size_in_bytes)
        self.pause_wait_in_seconds = pause_wait_in_seconds
        self.set_pause_wait_in_seconds(pause_wait_in_seconds)
        self.max_retries = max_retries
        self.set_max_retries(max_retries)
        self.initial_backoff_seconds = initial_backoff_seconds
        self.set_initial_backoff(initial_backoff_seconds)
        self.max_backoff_seconds = max_backoff_seconds
        self.set_max_backoff(initial_backoff_seconds, max_backoff_seconds)
        self.retry_exponential_growth_factor = retry_exponential_growth_factor
        self.set_retry_exponential_growth_factor(retry_exponential_growth_factor)
        self.decorrelated_jitter = decorrelated_jitter
        self.set_decorrelated_jitter(decorrelated_jitter)
        self.backoff_type = backoff_type
        self.set_backoff_type(backoff_type)

    def set_allow_multipart(self, allow_multipart):
        if not isinstance(allow_multipart, bool):
            raise TypeError(f"Invalid type for allow_multipart: expected bool, got {type(allow_multipart).__name__}")

        self.allow_multipart = allow_multipart

    def set_part_size_in_bytes(self, part_size_in_bytes):
        if not isinstance(part_size_in_bytes, int):
            raise TypeError(f"Invalid type for part_size_in_bytes: expected int, got {type(part_size_in_bytes).__name__}")
        if part_size_in_bytes <= 0:
            raise ValueError(f"Invalid value for part_size_in_bytes: expected > 0, got {part_size_in_bytes}")
        self.part_size_in_bytes = part_size_in_bytes

    def set_num_download_threads(self, num_download_threads):
        if not isinstance(num_download_threads, int):
            raise TypeError(
                f"Invalid type for num_download_threads: expected int, got {type(num_download_threads).__name__}")
        if num_download_threads <= 1:
            raise ValueError(f"Invalid value for num_download_threads: expected > 1, got {num_download_threads}")

        self.num_download_threads = num_download_threads

    def set_pause_wait_in_seconds(self, pause_wait_in_seconds):
        if not isinstance(pause_wait_in_seconds, int):
            raise TypeError(
                f"Invalid type for pause_wait_in_seconds: expected int, got {type(pause_wait_in_seconds).__name__}")
        if pause_wait_in_seconds <= 0:
            raise ValueError(f"Invalid value for pause_wait_in_seconds: expected > 0, got {pause_wait_in_seconds}")

        self.pause_wait_in_seconds = pause_wait_in_seconds

    def set_max_retries(self, max_retries):
        if not isinstance(max_retries, int):
            raise TypeError(
                f"Invalid type for max_retries: expected int, got {type(max_retries).__name__}")
        if max_retries < 1:
            raise ValueError(f"Invalid value for max_retries: expected >= 1, got {max_retries}")

        self.max_retries = max_retries

    def set_initial_backoff(self, initial_backoff_seconds):
        if not isinstance(initial_backoff_seconds, int):
            raise TypeError(
                f"Invalid type for initial_backoff_seconds: expected int, got {type(initial_backoff_seconds).__name__}")
        if initial_backoff_seconds < 1:
            raise ValueError(f"Invalid value for initial_backoff_seconds: expected >= 1, got {initial_backoff_seconds}")

        self.initial_backoff_seconds = initial_backoff_seconds

    def set_max_backoff(self, initial_backoff_seconds, max_backoff_seconds):
        if not isinstance(max_backoff_seconds, int):
            raise TypeError(
                f"Invalid type for max_backoff_seconds: expected int, got {type(max_backoff_seconds).__name__}")
        if max_backoff_seconds < initial_backoff_seconds:
            raise ValueError(
                f"Invalid value for max_backoff_seconds: expected >= initial backoff ({initial_backoff_seconds}), "
                f"got {max_backoff_seconds}")

        self.max_backoff_seconds = max_backoff_seconds

    def set_retry_exponential_growth_factor(self, retry_exponential_growth_factor):
        if not isinstance(retry_exponential_growth_factor, int):
            raise TypeError(
                f"Invalid type for retry_exponential_growth_factor: expected int, got {type(retry_exponential_growth_factor).__name__}")

        self.retry_exponential_growth_factor = retry_exponential_growth_factor

    def set_decorrelated_jitter(self, decorrelated_jitter):
        if not isinstance(decorrelated_jitter, int):
            raise TypeError(
                f"Invalid type for decorrelated_jitter: expected int, got {type(decorrelated_jitter).__name__}"
            )

        self.decorrelated_jitter = decorrelated_jitter

    def set_backoff_type(self, backoff_type):
        if not isinstance(backoff_type, str):
            raise TypeError(
                f"Invalid type for backoff_type: expected str, got {type(backoff_type).__name__}"
            )
        if backoff_type not in VALID_BACKOFF_TYPES:
            raise ValueError(
                f"Invalid backoff_type: expected one of {VALID_BACKOFF_TYPES}, got {backoff_type}"
            )

        self.backoff_type = backoff_type

    def get_allow_multipart(self):
        return self.allow_multipart

    def get_max_retries(self):
        return self.max_retries

    def get_pause_wait_in_seconds(self):
        return self.pause_wait_in_seconds

    def get_num_download_threads(self):
        return self.num_download_threads

    def get_max_backoff(self):
        return self.max_backoff_seconds

    def get_initial_backoff(self):
        return self.initial_backoff_seconds

    def get_part_size_in_bytes(self):
        return self.part_size_in_bytes

    def get_retry_exponential_growth_factor(self):
        return self.retry_exponential_growth_factor

    def get_decorrelated_jitter(self):
        return self.decorrelated_jitter

    def get_backoff_type(self):
        return self.backoff_type

    def make_retry_strategy(self):
        """
        If the user doesn't provide a retry strategy (from oci.retry.retry), then a custom retry strategy is built out
        of the parameters provided in the DownloadConfiguration. This function is used to make that custom retry
        strategy. The retries occur if one or more of the following occur:
        1) Timeout
        2) Connection error
        3) Unknown client exception: status == -1
        4) Server exception: status >= 500
        5) Potential edge case: status == 409
        6) Object is changed in the object storage during a retry == 416 or 404
        """
        return RetryStrategyBuilder(
            max_attempts=self.get_max_retries(),
            service_error_retry_config=DOWNLOAD_MANAGER_RETRYABLE_STATUSES_AND_CODES,
            retry_base_sleep_time_seconds=self.get_initial_backoff(),
            retry_exponential_growth_factor=self.get_retry_exponential_growth_factor(),
            retry_max_wait_between_calls_seconds=self.get_max_backoff(),
            decorrelated_jitter=self.get_decorrelated_jitter(),
            backoff_type=self.get_backoff_type(),
        ).get_retry_strategy()
