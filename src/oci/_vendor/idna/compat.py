# coding: utf-8
# Modified Work: Copyright (c) 2018, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Copyright (c) 2013-2024, Kim Davies and contributors. All rights reserved.

from typing import Any, Union

from .core import decode, encode


def ToASCII(label: str) -> bytes:
    return encode(label)


def ToUnicode(label: Union[bytes, bytearray]) -> str:
    return decode(label)


def nameprep(s: Any) -> None:
    raise NotImplementedError("IDNA 2008 does not utilise nameprep protocol")
