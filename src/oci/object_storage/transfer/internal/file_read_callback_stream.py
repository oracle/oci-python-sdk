# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


class FileReadCallbackStream:
    def __init__(self, file, progress_callback):
        self.progress_callback = progress_callback
        self.file = file
        self.mode = file.mode

    # this is used by 'requests' to determine the Content-Length header using fstat
    def fileno(self):
        return self.file.fileno()

    def read(self, n):
        self.progress_callback(n)
        return self.file.read(n)
