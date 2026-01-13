# coding: utf-8
# Modified Work: Copyright (c) 2018, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Copyright (c) 2013-2024, Kim Davies and contributors. All rights reserved.

from .core import (
    IDNABidiError,
    IDNAError,
    InvalidCodepoint,
    InvalidCodepointContext,
    alabel,
    check_bidi,
    check_hyphen_ok,
    check_initial_combiner,
    check_label,
    check_nfc,
    decode,
    encode,
    ulabel,
    uts46_remap,
    valid_contextj,
    valid_contexto,
    valid_label_length,
    valid_string_length,
)
from .intranges import intranges_contain
from .package_data import __version__

__all__ = [
    "__version__",
    "IDNABidiError",
    "IDNAError",
    "InvalidCodepoint",
    "InvalidCodepointContext",
    "alabel",
    "check_bidi",
    "check_hyphen_ok",
    "check_initial_combiner",
    "check_label",
    "check_nfc",
    "decode",
    "encode",
    "intranges_contain",
    "ulabel",
    "uts46_remap",
    "valid_contextj",
    "valid_contexto",
    "valid_label_length",
    "valid_string_length",
]
