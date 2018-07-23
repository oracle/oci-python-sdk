# coding: utf-8
# Modified Work: Copyright (c) 2018, 2018, Oracle and/or its affiliates. All rights reserved.
# Original Work: Copyright (c) 2018 Character Encoding Detector contributors.  https://github.com/chardet

from .charsetprober import CharSetProber
from .codingstatemachine import CodingStateMachine
from .enums import LanguageFilter, ProbingState, MachineState
from .escsm import (HZ_SM_MODEL, ISO2022CN_SM_MODEL, ISO2022JP_SM_MODEL,
                    ISO2022KR_SM_MODEL)


class EscCharSetProber(CharSetProber):
    """
    This CharSetProber uses a "code scheme" approach for detecting encodings,
    whereby easily recognizable escape or shift sequences are relied on to
    identify these encodings.
    """

    def __init__(self, lang_filter=None):
        super(EscCharSetProber, self).__init__(lang_filter=lang_filter)
        self.coding_sm = []
        if self.lang_filter & LanguageFilter.CHINESE_SIMPLIFIED:
            self.coding_sm.append(CodingStateMachine(HZ_SM_MODEL))
            self.coding_sm.append(CodingStateMachine(ISO2022CN_SM_MODEL))
        if self.lang_filter & LanguageFilter.JAPANESE:
            self.coding_sm.append(CodingStateMachine(ISO2022JP_SM_MODEL))
        if self.lang_filter & LanguageFilter.KOREAN:
            self.coding_sm.append(CodingStateMachine(ISO2022KR_SM_MODEL))
        self.active_sm_count = None
        self._detected_charset = None
        self._detected_language = None
        self._state = None
        self.reset()

    def reset(self):
        super(EscCharSetProber, self).reset()
        for coding_sm in self.coding_sm:
            if not coding_sm:
                continue
            coding_sm.active = True
            coding_sm.reset()
        self.active_sm_count = len(self.coding_sm)
        self._detected_charset = None
        self._detected_language = None

    @property
    def charset_name(self):
        return self._detected_charset

    @property
    def language(self):
        return self._detected_language

    def get_confidence(self):
        if self._detected_charset:
            return 0.99
        else:
            return 0.00

    def feed(self, byte_str):
        for c in byte_str:
            for coding_sm in self.coding_sm:
                if not coding_sm or not coding_sm.active:
                    continue
                coding_state = coding_sm.next_state(c)
                if coding_state == MachineState.ERROR:
                    coding_sm.active = False
                    self.active_sm_count -= 1
                    if self.active_sm_count <= 0:
                        self._state = ProbingState.NOT_ME
                        return self.state
                elif coding_state == MachineState.ITS_ME:
                    self._state = ProbingState.FOUND_IT
                    self._detected_charset = coding_sm.get_coding_state_machine()
                    self._detected_language = coding_sm.language
                    return self.state

        return self.state
