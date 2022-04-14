# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceAliasCredential(object):
    """
    Monitored Resource Alias Credential Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceAliasCredential object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this MonitoredResourceAliasCredential.
        :type source: str

        :param name:
            The value to assign to the name property of this MonitoredResourceAliasCredential.
        :type name: str

        :param credential:
            The value to assign to the credential property of this MonitoredResourceAliasCredential.
        :type credential: oci.stack_monitoring.models.MonitoredResourceAliasSourceCredential

        """
        self.swagger_types = {
            'source': 'str',
            'name': 'str',
            'credential': 'MonitoredResourceAliasSourceCredential'
        }

        self.attribute_map = {
            'source': 'source',
            'name': 'name',
            'credential': 'credential'
        }

        self._source = None
        self._name = None
        self._credential = None

    @property
    def source(self):
        """
        **[Required]** Gets the source of this MonitoredResourceAliasCredential.
        The source type and source name combination,delimited with (.) separator. Ex. {source type}.{source name} and source type max char limit is 63.


        :return: The source of this MonitoredResourceAliasCredential.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this MonitoredResourceAliasCredential.
        The source type and source name combination,delimited with (.) separator. Ex. {source type}.{source name} and source type max char limit is 63.


        :param source: The source of this MonitoredResourceAliasCredential.
        :type: str
        """
        self._source = source

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MonitoredResourceAliasCredential.
        The name of the alias, within the context of the source.


        :return: The name of this MonitoredResourceAliasCredential.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitoredResourceAliasCredential.
        The name of the alias, within the context of the source.


        :param name: The name of this MonitoredResourceAliasCredential.
        :type: str
        """
        self._name = name

    @property
    def credential(self):
        """
        **[Required]** Gets the credential of this MonitoredResourceAliasCredential.

        :return: The credential of this MonitoredResourceAliasCredential.
        :rtype: oci.stack_monitoring.models.MonitoredResourceAliasSourceCredential
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """
        Sets the credential of this MonitoredResourceAliasCredential.

        :param credential: The credential of this MonitoredResourceAliasCredential.
        :type: oci.stack_monitoring.models.MonitoredResourceAliasSourceCredential
        """
        self._credential = credential

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
