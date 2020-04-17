# coding: utf-8
# Modified Work: Copyright (c) 2018, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Copyright (c) 2013-2018, Kim Davies. All rights reserved.

from .core import encode, decode, alabel, ulabel, IDNAError
import codecs
import re

_unicode_dots_re = re.compile(u'[\u002e\u3002\uff0e\uff61]')

class Codec(codecs.Codec):

    def encode(self, data, errors='strict'):

        if errors != 'strict':
            raise IDNAError("Unsupported error handling \"{0}\"".format(errors))

        if not data:
            return "", 0

        return encode(data), len(data)

    def decode(self, data, errors='strict'):

        if errors != 'strict':
            raise IDNAError("Unsupported error handling \"{0}\"".format(errors))

        if not data:
            return u"", 0

        return decode(data), len(data)

class IncrementalEncoder(codecs.BufferedIncrementalEncoder):
    def _buffer_encode(self, data, errors, final):
        if errors != 'strict':
            raise IDNAError("Unsupported error handling \"{0}\"".format(errors))

        if not data:
            return ("", 0)

        labels = _unicode_dots_re.split(data)
        trailing_dot = u''
        if labels:
            if not labels[-1]:
                trailing_dot = '.'
                del labels[-1]
            elif not final:
                # Keep potentially unfinished label until the next call
                del labels[-1]
                if labels:
                    trailing_dot = '.'

        result = []
        size = 0
        for label in labels:
            result.append(alabel(label))
            if size:
                size += 1
            size += len(label)

        # Join with U+002E
        result = ".".join(result) + trailing_dot
        size += len(trailing_dot)
        return (result, size)

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, data, errors, final):
        if errors != 'strict':
            raise IDNAError("Unsupported error handling \"{0}\"".format(errors))

        if not data:
            return (u"", 0)

        # IDNA allows decoding to operate on Unicode strings, too.
        if isinstance(data, unicode):
            labels = _unicode_dots_re.split(data)
        else:
            # Must be ASCII string
            data = str(data)
            unicode(data, "ascii")
            labels = data.split(".")

        trailing_dot = u''
        if labels:
            if not labels[-1]:
                trailing_dot = u'.'
                del labels[-1]
            elif not final:
                # Keep potentially unfinished label until the next call
                del labels[-1]
                if labels:
                    trailing_dot = u'.'

        result = []
        size = 0
        for label in labels:
            result.append(ulabel(label))
            if size:
                size += 1
            size += len(label)

        result = u".".join(result) + trailing_dot
        size += len(trailing_dot)
        return (result, size)


class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

def getregentry():
    return codecs.CodecInfo(
        name='idna',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    )
