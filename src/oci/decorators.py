# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from .util import Sentinel

import functools
from oci._vendor import six


missing = Sentinel("Missing")


def wrap_init_to_set_state_from_kwargs(init_fn):
    @functools.wraps(init_fn)
    def init(self, **kwargs):
        init_fn(self)
        for attr_name in six.iterkeys(self.swagger_types):
            value = kwargs.pop(attr_name, missing)
            if value is not missing:
                setattr(self, attr_name, value)

        if kwargs:
            raise TypeError('Unrecognized keyword arguments: {}'.format(', '.join(six.iterkeys(kwargs))))

    return init


# This decorator is intended to be applied at the class level on model classes so that their state can be instantiated
# at creation time via keyword arguments.
#
# This decorator assumes that the model class has a swagger_types attribute which describes all of its available attributes to
# be set and that the keyword arguments passed match these attribute names. No type checking is currently done.
#
# Additionally, providing unrecognized keyword arguments (i.e. they do not match any swagger_type defined attribute) will result in
# a TypeError being thrown.
def init_model_state_from_kwargs(original_cls):
    original_cls.__init__ = wrap_init_to_set_state_from_kwargs(original_cls.__init__)
    return original_cls
