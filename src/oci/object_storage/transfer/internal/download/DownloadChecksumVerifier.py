# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import hashlib
import hmac
import struct
import crc32c
from cryptography.exceptions import InternalError
from .. import md5 as MD5
from oci.fips import is_fips_mode


class Crc32cWrapper:
    def __init__(self, total_length):
        self.total_length = total_length
        self.polynomial = 0x82F63B78  # CRC32C reflected polynomial
        mat = [0] * 32
        mat[0] = self.polynomial
        for i in range(1, 32):
            mat[i] = 1 << (i - 1)
        self.M = mat
        self.accumulator = 0

    def __mat_vec_mul(self, mat, vec):
        result = 0
        for col in mat:
            if vec & 1:
                result ^= col
            vec >>= 1
        return result

    def __mat_sq(self, mat):
        return [self.__mat_vec_mul(mat, col) for col in mat]

    def update(self, chunk, offset):
        # For multipart downloads, each chunk’s CRC32C is shifted into its final position within the full object and
        # then XORed into an accumulator. This allows checksum verification to remain correct even when parts arrive
        # out of order. Adapted from https://stackoverflow.com/a/23126768.
        # For example:
        # Let M be the linear transformation matrix that represents feeding one zero bit into the CRC machine
        # (as in the stackoverflow discussion). Applying M repeatedly corresponds to appending zero bits to the data.
        # From the stackoverflow discussion we know if D = A || B, then:
        # CRC(D) = M^(len(B)) * CRC(A) XOR CRC(B) (here ^ is not XOR, but power i.e. raised to)
        # Then if D = A || B || C and X = B || C,
        # CRC(D) = M^(len(X)) * CRC(A) XOR CRC(X)
        #        = M^(len(B) + len(C)) * CRC(A) XOR M^(len(C)) * CRC(B) XOR CRC(C)
        #        = M^(len_after(A)) * CRC(A) XOR M^(len_after(B)) * CRC(B) XOR M^(len_after(C)) * CRC(C)
        # where len_after(chunk) is the number of bits that come after that chunk in the final concatenated stream.
        # Because XOR is commutative and associative, the chunks can be processed in any order: for each chunk,
        # we shift its CRC by the number of bits that come after it (using powers of M), then XOR it into the accumulator.
        # After all chunks have been added, the accumulator holds CRC(D), the CRC of the full content.

        length = len(chunk)
        chunk_crc = crc32c.crc32c(chunk)
        chunk_end = offset + length
        bits_after_chunk = 8 * (self.total_length - chunk_end)
        if bits_after_chunk == 0:
            self.accumulator ^= chunk_crc
        else:
            mat = self.M
            while bits_after_chunk:
                if bits_after_chunk & 1:
                    chunk_crc = self.__mat_vec_mul(mat, chunk_crc)
                mat = self.__mat_sq(mat)
                bits_after_chunk >>= 1
            self.accumulator ^= chunk_crc

    def digest(self):
        return struct.pack(">I", self.accumulator & 0xFFFFFFFF)


class DownloadChecksumVerifier:
    """
    Verifies the integrity of downloaded content using a checksum.

    This class incrementally computes a checksum over downloaded data and
    compares it to an expected checksum value. It supports CRC32C, SHA256, SHA384 and MD5.
    For CRC32C, a custom wrapper ~oci.object_storage.transfer.internal.download.Crc32cWrapper around crc32c lib is used.
    For MD5, FIPS mode is taken into account and an appropriate MD5 implementation is selected.

    :param: str algorithm: The algorithm (out of CRC32C, SHA256, SHA384 and MD5) to use to verify the integrity.
    :param: bytes expected_checksum_bytes: The expected checksum bytes.
    :param: int total_length: The total length of the downloaded data.
    """

    def __init__(self, algorithm, expected_checksum_bytes, total_length):
        self.algorithm = algorithm.lower()
        self.total_length = total_length
        self.expected_checksum_bytes = expected_checksum_bytes
        self._state = None
        if self.algorithm == "crc32c":
            self._state = Crc32cWrapper(total_length)
        else:
            if self.algorithm == "md5":
                if is_fips_mode():
                    try:
                        self._state = MD5.md5()
                    except InternalError:
                        self._state = hashlib.new("md5", usedforsecurity=False)
                else:
                    self._state = hashlib.md5()
            else:
                self._state = hashlib.new(self.algorithm)

    def update(self, data, offset=None):
        if self.algorithm == "crc32c":
            self._state.update(data, offset)
        else:
            self._state.update(data)

    def verify(self) -> bool:
        return hmac.compare_digest(self.expected_checksum_bytes, self._state.digest())

    def digest(self):
        return self._state.digest()

    def get_expected_checksum(self):
        return self.expected_checksum_bytes
