# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from .util import Sentinel

import six


missing = Sentinel("Missing")


# This decorator is intended to be applied at the class level on model classes so that their state can be instantiated
# at creation time via keyword arguments.
#
# This decorator assumes that the model class has a swagger_types attribute which describes all of its available attributes to
# be set and that the keyword arguments passed match these attribute names. No type checking is currently done.
#
# Additionally, providing unrecognized keyword arguments (i.e. they do not match any swagger_type defined attribute) will result in
# a TypeError being thrown.
def init_model_state_from_kwargs(original_cls):
    class InitModelStateFromKwargsWrappedClass(original_cls):
        def __init__(self, **kwargs):
            super(InitModelStateFromKwargsWrappedClass, self).__init__()

            for attr_name in six.iterkeys(self.swagger_types):
                value = kwargs.pop(attr_name, missing)
                if value is not missing:
                    setattr(self, attr_name, value)

            if kwargs:
                raise TypeError('Unrecognized keyword arguments: {}'.format(', '.join(six.iterkeys(kwargs))))

    return InitModelStateFromKwargsWrappedClass
