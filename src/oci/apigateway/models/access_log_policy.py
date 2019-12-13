# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessLogPolicy(object):
    """
    Configures the pushing of access logs to OCI Public Logging.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessLogPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this AccessLogPolicy.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled'
        }

        self._is_enabled = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AccessLogPolicy.
        Enables pushing of access logs to OCI Public Logging.


        :return: The is_enabled of this AccessLogPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AccessLogPolicy.
        Enables pushing of access logs to OCI Public Logging.


        :param is_enabled: The is_enabled of this AccessLogPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
