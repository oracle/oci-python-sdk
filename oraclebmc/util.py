import datetime
import json
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
        # always UTC
        as_utc = obj.replace(tzinfo=datetime.timezone.utc)
        if isinstance(obj, datetime.datetime):
            # only datetime.datetime takes a separator
            return as_utc.isoformat(sep="T")
        return as_utc.isoformat()
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
