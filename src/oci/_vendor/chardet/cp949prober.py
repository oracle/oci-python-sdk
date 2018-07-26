# coding: utf-8
# Modified Work: Copyright (c) 2018, 2018, Oracle and/or its affiliates. All rights reserved.
# Original Work: Copyright (c) 2018 Character Encoding Detector contributors.  https://github.com/chardet

from .chardistribution import EUCKRDistributionAnalysis
from .codingstatemachine import CodingStateMachine
from .mbcharsetprober import MultiByteCharSetProber
from .mbcssm import CP949_SM_MODEL


class CP949Prober(MultiByteCharSetProber):
    def __init__(self):
        super(CP949Prober, self).__init__()
        self.coding_sm = CodingStateMachine(CP949_SM_MODEL)
        # NOTE: CP949 is a superset of EUC-KR, so the distribution should be
        #       not different.
        self.distribution_analyzer = EUCKRDistributionAnalysis()
        self.reset()

    @property
    def charset_name(self):
        return "CP949"

    @property
    def language(self):
        return "Korean"
