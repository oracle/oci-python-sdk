# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationTraceConfig(object):
    """
    Define the tracing configuration for an application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationTraceConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this ApplicationTraceConfig.
        :type is_enabled: bool

        :param domain_id:
            The value to assign to the domain_id property of this ApplicationTraceConfig.
        :type domain_id: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'domain_id': 'str'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'domain_id': 'domainId'
        }

        self._is_enabled = None
        self._domain_id = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this ApplicationTraceConfig.
        Define if tracing is enabled for the resource.


        :return: The is_enabled of this ApplicationTraceConfig.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ApplicationTraceConfig.
        Define if tracing is enabled for the resource.


        :param is_enabled: The is_enabled of this ApplicationTraceConfig.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def domain_id(self):
        """
        Gets the domain_id of this ApplicationTraceConfig.
        The OCID of the collector (e.g. an APM Domain) trace events will be sent to.


        :return: The domain_id of this ApplicationTraceConfig.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this ApplicationTraceConfig.
        The OCID of the collector (e.g. an APM Domain) trace events will be sent to.


        :param domain_id: The domain_id of this ApplicationTraceConfig.
        :type: str
        """
        self._domain_id = domain_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
