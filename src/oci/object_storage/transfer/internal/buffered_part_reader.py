# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import io


class BufferedPartReader(io.IOBase):
    def __init__(self, file_object, start, size):
        """
        Build an object that will act like a BufferedReader object,
        but constrained to a predetermined part of the file_object.

        :param file_object: A file opened for reading in binary mode.
        :param start: Start of the part within the file_object
        :param size: Ideal size of the part.  This will be set
                     to the number of bytes remaining in the
                     file if there aren't enough bytes remaining.
        """
        self.file = file_object
        self.bytes_read = 0
        self.start = start

        # Seek to the end of the file to see how many bytes remain
        # from the start of the part.
        self.file.seek(0, io.SEEK_END)
        self.size = min(self.file.tell() - self.start, size)

        # Reset the pointer to the start of the part.
        self.file.seek(start, io.SEEK_SET)

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Seek within the part.  This is similar to the standard seek, except
        that io.SEEK_SET is the start of the part and io.SEEK_END is the
        end of the part.

        :param offset: Offset in bytes from location determined by the whence value
        :param whence: io.SEEK_END and io.SEEK_SET are supported.
        """
        if whence == io.SEEK_END:
            self.file.seek(self.start + self.size + offset, io.SEEK_SET)
        elif whence == io.SEEK_SET:
            self.file.seek(self.start + offset, io.SEEK_SET)
        else:
            raise RuntimeError("Unhandled whence value: {}".format(whence))

    def tell(self):
        """
        Determine where the file pointer is relative to the start of the part.

        :return: Relative position in the part
        """
        return self.file.tell() - self.start

    def read(self, n):
        """
        Read data from the part, but make the end of the part look like
        the end of file has been reached.

        :param n: Bytes to read
        :return: Memoryview of the bytes read from the part
        """
        buf = bytearray(n)
        read = 0
        if self.bytes_read < self.size:
            read = self.file.readinto(buf)
            self.bytes_read += read
            # Check to see if the current buffer contains bytes that come from
            # the next part.
            if self.bytes_read > self.size:
                # Subtract the number of excess bytes from the bytes read.
                read -= self.bytes_read - self.size

        # Wrap the bytearray in a memoryview because the Python 2.7 implementation
        # of Requests needs a memoryview, buffer or byte string.
        return memoryview(buf[:read])
