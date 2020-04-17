# coding: utf-8
# Modified Work: Copyright (c) 2018, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Original Work: Copyright (c) 2018 Character Encoding Detector contributors.  https://github.com/chardet

from .mbcharsetprober import MultiByteCharSetProber
from .codingstatemachine import CodingStateMachine
from .chardistribution import GB2312DistributionAnalysis
from .mbcssm import GB2312_SM_MODEL

class GB2312Prober(MultiByteCharSetProber):
    def __init__(self):
        super(GB2312Prober, self).__init__()
        self.coding_sm = CodingStateMachine(GB2312_SM_MODEL)
        self.distribution_analyzer = GB2312DistributionAnalysis()
        self.reset()

    @property
    def charset_name(self):
        return "GB2312"

    @property
    def language(self):
        return "Chinese"
