# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectNameFilter(object):
    """
    A filter that compares object names to a set of object name prefixes to determine if a rule applies to a
    given object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectNameFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param inclusion_prefixes:
            The value to assign to the inclusion_prefixes property of this ObjectNameFilter.
        :type inclusion_prefixes: list[str]

        """
        self.swagger_types = {
            'inclusion_prefixes': 'list[str]'
        }

        self.attribute_map = {
            'inclusion_prefixes': 'inclusionPrefixes'
        }

        self._inclusion_prefixes = None

    @property
    def inclusion_prefixes(self):
        """
        Gets the inclusion_prefixes of this ObjectNameFilter.
        An array of object name prefixes that the rule will apply to. An empty array means to include all objects.


        :return: The inclusion_prefixes of this ObjectNameFilter.
        :rtype: list[str]
        """
        return self._inclusion_prefixes

    @inclusion_prefixes.setter
    def inclusion_prefixes(self, inclusion_prefixes):
        """
        Sets the inclusion_prefixes of this ObjectNameFilter.
        An array of object name prefixes that the rule will apply to. An empty array means to include all objects.


        :param inclusion_prefixes: The inclusion_prefixes of this ObjectNameFilter.
        :type: list[str]
        """
        self._inclusion_prefixes = inclusion_prefixes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
