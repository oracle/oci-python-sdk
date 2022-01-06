# coding: utf-8
# Modified Work: Copyright (c) 2018, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Original Work: Copyright (c) 2018 Character Encoding Detector contributors.  https://github.com/chardet

from .charsetgroupprober import CharSetGroupProber
from .hebrewprober import HebrewProber
from .langbulgarianmodel import (ISO_8859_5_BULGARIAN_MODEL,
                                 WINDOWS_1251_BULGARIAN_MODEL)
from .langgreekmodel import ISO_8859_7_GREEK_MODEL, WINDOWS_1253_GREEK_MODEL
from .langhebrewmodel import WINDOWS_1255_HEBREW_MODEL
# from .langhungarianmodel import (ISO_8859_2_HUNGARIAN_MODEL,
#                                  WINDOWS_1250_HUNGARIAN_MODEL)
from .langrussianmodel import (IBM855_RUSSIAN_MODEL, IBM866_RUSSIAN_MODEL,
                               ISO_8859_5_RUSSIAN_MODEL, KOI8_R_RUSSIAN_MODEL,
                               MACCYRILLIC_RUSSIAN_MODEL,
                               WINDOWS_1251_RUSSIAN_MODEL)
from .langthaimodel import TIS_620_THAI_MODEL
from .langturkishmodel import ISO_8859_9_TURKISH_MODEL
from .sbcharsetprober import SingleByteCharSetProber


class SBCSGroupProber(CharSetGroupProber):
    def __init__(self):
        super(SBCSGroupProber, self).__init__()
        hebrew_prober = HebrewProber()
        logical_hebrew_prober = SingleByteCharSetProber(WINDOWS_1255_HEBREW_MODEL,
                                                        False, hebrew_prober)
        # TODO: See if using ISO-8859-8 Hebrew model works better here, since
        #       it's actually the visual one
        visual_hebrew_prober = SingleByteCharSetProber(WINDOWS_1255_HEBREW_MODEL,
                                                       True, hebrew_prober)
        hebrew_prober.set_model_probers(logical_hebrew_prober,
                                        visual_hebrew_prober)
        # TODO: ORDER MATTERS HERE. I changed the order vs what was in master
        #       and several tests failed that did not before. Some thought
        #       should be put into the ordering, and we should consider making
        #       order not matter here, because that is very counter-intuitive.
        self.probers = [
            SingleByteCharSetProber(WINDOWS_1251_RUSSIAN_MODEL),
            SingleByteCharSetProber(KOI8_R_RUSSIAN_MODEL),
            SingleByteCharSetProber(ISO_8859_5_RUSSIAN_MODEL),
            SingleByteCharSetProber(MACCYRILLIC_RUSSIAN_MODEL),
            SingleByteCharSetProber(IBM866_RUSSIAN_MODEL),
            SingleByteCharSetProber(IBM855_RUSSIAN_MODEL),
            SingleByteCharSetProber(ISO_8859_7_GREEK_MODEL),
            SingleByteCharSetProber(WINDOWS_1253_GREEK_MODEL),
            SingleByteCharSetProber(ISO_8859_5_BULGARIAN_MODEL),
            SingleByteCharSetProber(WINDOWS_1251_BULGARIAN_MODEL),
            # TODO: Restore Hungarian encodings (iso-8859-2 and windows-1250)
            #       after we retrain model.
            # SingleByteCharSetProber(ISO_8859_2_HUNGARIAN_MODEL),
            # SingleByteCharSetProber(WINDOWS_1250_HUNGARIAN_MODEL),
            SingleByteCharSetProber(TIS_620_THAI_MODEL),
            SingleByteCharSetProber(ISO_8859_9_TURKISH_MODEL),
            hebrew_prober,
            logical_hebrew_prober,
            visual_hebrew_prober,
        ]
        self.reset()
