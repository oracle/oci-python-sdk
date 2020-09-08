# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsConfigWorkRequestPayload(object):
    """
    LogAnalyticsConfigWorkRequestPayload
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsConfigWorkRequestPayload object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_name:
            The value to assign to the source_name property of this LogAnalyticsConfigWorkRequestPayload.
        :type source_name: str

        :param entity_id:
            The value to assign to the entity_id property of this LogAnalyticsConfigWorkRequestPayload.
        :type entity_id: str

        :param lookup_reference:
            The value to assign to the lookup_reference property of this LogAnalyticsConfigWorkRequestPayload.
        :type lookup_reference: int

        """
        self.swagger_types = {
            'source_name': 'str',
            'entity_id': 'str',
            'lookup_reference': 'int'
        }

        self.attribute_map = {
            'source_name': 'sourceName',
            'entity_id': 'entityId',
            'lookup_reference': 'lookupReference'
        }

        self._source_name = None
        self._entity_id = None
        self._lookup_reference = None

    @property
    def source_name(self):
        """
        Gets the source_name of this LogAnalyticsConfigWorkRequestPayload.
        sourceName


        :return: The source_name of this LogAnalyticsConfigWorkRequestPayload.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this LogAnalyticsConfigWorkRequestPayload.
        sourceName


        :param source_name: The source_name of this LogAnalyticsConfigWorkRequestPayload.
        :type: str
        """
        self._source_name = source_name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this LogAnalyticsConfigWorkRequestPayload.
        entityId


        :return: The entity_id of this LogAnalyticsConfigWorkRequestPayload.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this LogAnalyticsConfigWorkRequestPayload.
        entityId


        :param entity_id: The entity_id of this LogAnalyticsConfigWorkRequestPayload.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def lookup_reference(self):
        """
        Gets the lookup_reference of this LogAnalyticsConfigWorkRequestPayload.
        lookupReference


        :return: The lookup_reference of this LogAnalyticsConfigWorkRequestPayload.
        :rtype: int
        """
        return self._lookup_reference

    @lookup_reference.setter
    def lookup_reference(self, lookup_reference):
        """
        Sets the lookup_reference of this LogAnalyticsConfigWorkRequestPayload.
        lookupReference


        :param lookup_reference: The lookup_reference of this LogAnalyticsConfigWorkRequestPayload.
        :type: int
        """
        self._lookup_reference = lookup_reference

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
