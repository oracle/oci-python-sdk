# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import io
import hashlib
import base64
import struct
import crc32c
from .buffered_part_reader import BufferedPartReader


class CRC32CHash:

    def __init__(self, data=b""):
        self._checksum = 0
        if data:
            self.update(data)

    def update(self, data):
        self._checksum = crc32c.crc32c(data, self._checksum)

    def digest(self):
        return struct.pack(">I", self._checksum & 0xFFFFFFFF)

    def hexdigest(self):
        return self.digest().hex()


def get_crc32c_hash_object(data=b""):
    if hasattr(crc32c, "CRC32CHash"):
        return crc32c.CRC32CHash(data)
    return CRC32CHash(data)


class Checksum:
    """
    Additional checksum class, supports "CRC32C", "SHA256", "SHA384" in addition to MD5
    Stores the user provided additional checksum, and if computation is required from SDK.
    Provides methods to compute above checksums.
    """
    READ_BUFFER_SIZE = 8 * 1024
    CONTENT_CRC32C = "opc_content_crc32c"
    CONTENT_SHA256 = "opc_content_sha256"
    CONTENT_SHA384 = "opc_content_sha384"
    LIST_CONTENT_ALGO = [CONTENT_CRC32C, CONTENT_SHA256, CONTENT_SHA384]
    CRC32C = "CRC32C"
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    ALGO_CONTENT_MAP = {CRC32C: CONTENT_CRC32C,
                        SHA256: CONTENT_SHA256,
                        SHA384: CONTENT_SHA384}

    def __init__(self, checksum_algorithm, computation_required=True):
        """
        :param checksum_algorithm: Name of additional checksum algorithm
        :param computation_required: True, if user has not provided opc_content_* value
        """
        self._checksum_algorithm = checksum_algorithm.upper()
        self.is_computation_required = computation_required

    def get_checksum_algorithm(self):
        """
        :return: Name of additional checksum algorithm
        """
        return self._checksum_algorithm

    def calculate_checksum(self, data):
        """
        Does checksum calculation as per self._checksum_algorithm on provided data
        :param data: Data of file.
        :return: Checksum value.
        """
        if self._checksum_algorithm == self.CRC32C:
            return self.calculate_crc32c_checksum(data)
        if self._checksum_algorithm == self.SHA256:
            return self.calculate_sha256_checksum(data)
        if self._checksum_algorithm == self.SHA384:
            return self.calculate_sha384_checksum(data)

    def get_opc_content_param(self):
        """
        :return: opc_content_<algo> . Here algo will be self._checksum_algorithm.
        """
        return self.ALGO_CONTENT_MAP[self._checksum_algorithm]

    def calculate_crc32c_checksum(self, data):
        """
        Calculate crc32c checksum on data
        """
        crc32c_hash = get_crc32c_hash_object()
        crc32c_hash.update(data)
        return base64.b64encode(crc32c_hash.digest()).decode("utf-8").strip()

    def calculate_sha256_checksum(self, data):
        """
        Calculate shs256 checksum on data
        """
        sha256 = hashlib.sha256()
        sha256.update(data)
        return base64.b64encode(sha256.digest()).decode("utf-8").strip()

    def calculate_sha384_checksum(self, data):
        """
        Calculate sha384 checksum on data
        """
        sha384 = hashlib.sha384()
        sha384.update(data)
        return base64.b64encode(sha384.digest()).decode("utf-8").strip()

    def get_checksum_obj(self):
        """
        Get checksum object depending upon which algorithm is set in
        self._checksum_algorithm. Will be used while calculating checksum.
        """

        if self._checksum_algorithm == self.CRC32C:
            crc32c_hash = get_crc32c_hash_object()
            return crc32c_hash
        if self._checksum_algorithm == self.SHA256:
            sha256_hash = hashlib.sha256()
            return sha256_hash
        if self._checksum_algorithm == self.SHA384:
            sha384_hash = hashlib.sha384()
            return sha384_hash

    def read_file_and_calculate_checksum(self, file_path, offset, chunk_size):
        """
        Read the given file for given sized bytes and calculates checksum

        :param file_path: file path
        :param offset: starting offset
        :param chunk_size: chunk size
        :return: Calculated checksum of the algorithm as per self._checksum_algorithm
        """

        additional_cksum_obj = self.get_checksum_obj()

        with io.open(file_path, mode='rb') as f:
            bpr = BufferedPartReader(f, offset, chunk_size)
            while True:
                part = bpr.read(self.READ_BUFFER_SIZE)
                if part == b'':
                    break
                additional_cksum_obj.update(part)

        checksum_value = []
        checksum_value.append(base64.b64encode(additional_cksum_obj.digest()).decode("utf-8").strip())

        return checksum_value[0]
