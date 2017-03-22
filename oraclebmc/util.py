# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import datetime
import json
import pytz
import six
try:
    # PY3+
    import collections.abc as abc
except ImportError:
    # PY2
    import collections as abc

missing_attr = object()


def to_dict(obj):
    """Helper to flatten models into dicts for rendering.

    The following conversions are applied:

    * datetime.date, datetime.datetime, datetime.time
      are converted into ISO8601 UTC strings
    """
    # Shortcut strings so they don't count as Iterables
    if isinstance(obj, six.string_types):
        return obj
    elif isinstance(obj, (datetime.datetime, datetime.time)):
        # always use UTC
        if not obj.tzinfo:
            obj = pytz.utc.localize(obj)
        if isinstance(obj, datetime.datetime):
            # only datetime.datetime takes a separator
            return obj.isoformat(sep="T")
        return obj.isoformat()
    elif isinstance(obj, datetime.date):
        # datetime.date doesn't have a timezone
        return obj.isoformat()
    elif isinstance(obj, abc.Mapping):
        return {k: to_dict(v) for k, v in six.iteritems(obj)}
    elif isinstance(obj, abc.Iterable):
        return [to_dict(v) for v in obj]
    # Not a string, datetime, dict, list, or model - return directly
    elif not hasattr(obj, "swagger_types"):
        return obj

    # Collect attrs from obj according to swagger_types into a dict
    as_dict = {}
    for key in six.iterkeys(obj.swagger_types):
        value = getattr(obj, key, missing_attr)
        if value is not missing_attr:
            as_dict[key] = to_dict(value)
    return as_dict


def formatted_flat_dict(model):
    """Returns a string of the model flattened as a dict, sorted"""
    as_dict = to_dict(model)
    return json.dumps(
        as_dict,
        indent=2,
        sort_keys=True
    )


class Sentinel(object):
    """Named singletons for clear docstrings.
    Also used to differentiate an explicit param of None from a lack of argument.

    .. code-block:: pycon

        >>> missing = Sentinel("Missing", False)
        >>> also_missing = Sentinel("Missing", False)
        >>> assert missing is also_missing
        >>> repr(missing)
        <Missing>
        >>> assert bool(missing) is False
    """
    _symbols = {}

    def __new__(cls, name, truthy=True):
        sentinel = Sentinel._symbols.get(name, None)
        if sentinel is None:
            sentinel = Sentinel._symbols[name] = super(Sentinel, cls).__new__(cls)
        elif sentinel.truthy is not truthy:
            raise ValueError("Tried to get existing Sentinel {!r} with wrong truthy value".format(sentinel))
        return sentinel

    def __init__(self, name, truthy=True):
        self.name = name
        self.truthy = truthy

    def __repr__(self):
        # Sentinel("Missing") -> <Missing>
        return "<{}>".format(self.name)

    def __bool__(self):
        return self.truthy
    # PY2 Compatibility
    __nonzero__ = __bool__
