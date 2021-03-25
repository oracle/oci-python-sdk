# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtractLogFieldResults(object):
    """
    log field path values
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtractLogFieldResults object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param paths:
            The value to assign to the paths property of this ExtractLogFieldResults.
        :type paths: list[str]

        """
        self.swagger_types = {
            'paths': 'list[str]'
        }

        self.attribute_map = {
            'paths': 'paths'
        }

        self._paths = None

    @property
    def paths(self):
        """
        Gets the paths of this ExtractLogFieldResults.
        The log field path values.


        :return: The paths of this ExtractLogFieldResults.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this ExtractLogFieldResults.
        The log field path values.


        :param paths: The paths of this ExtractLogFieldResults.
        :type: list[str]
        """
        self._paths = paths

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
