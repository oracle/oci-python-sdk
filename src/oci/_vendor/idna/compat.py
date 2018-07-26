# coding: utf-8
# Modified Work: Copyright (c) 2018, 2018, Oracle and/or its affiliates. All rights reserved.
# Copyright (c) 2013-2018, Kim Davies. All rights reserved.

from .core import *
from .codec import *

def ToASCII(label):
    return encode(label)

def ToUnicode(label):
    return decode(label)

def nameprep(s):
    raise NotImplementedError("IDNA 2008 does not utilise nameprep protocol")

