# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContextualData(object):
    """
    ContextualData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContextualData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param client_id:
            The value to assign to the client_id property of this ContextualData.
        :type client_id: str

        :param schema_name:
            The value to assign to the schema_name property of this ContextualData.
        :type schema_name: str

        :param schema_version:
            The value to assign to the schema_version property of this ContextualData.
        :type schema_version: str

        :param payload:
            The value to assign to the payload property of this ContextualData.
        :type payload: str

        """
        self.swagger_types = {
            'client_id': 'str',
            'schema_name': 'str',
            'schema_version': 'str',
            'payload': 'str'
        }

        self.attribute_map = {
            'client_id': 'clientId',
            'schema_name': 'schemaName',
            'schema_version': 'schemaVersion',
            'payload': 'payload'
        }

        self._client_id = None
        self._schema_name = None
        self._schema_version = None
        self._payload = None

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this ContextualData.
        The unique client identifier


        :return: The client_id of this ContextualData.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this ContextualData.
        The unique client identifier


        :param client_id: The client_id of this ContextualData.
        :type: str
        """
        self._client_id = client_id

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this ContextualData.
        The schema name


        :return: The schema_name of this ContextualData.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this ContextualData.
        The schema name


        :param schema_name: The schema_name of this ContextualData.
        :type: str
        """
        self._schema_name = schema_name

    @property
    def schema_version(self):
        """
        **[Required]** Gets the schema_version of this ContextualData.
        The schema version


        :return: The schema_version of this ContextualData.
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """
        Sets the schema_version of this ContextualData.
        The schema version


        :param schema_version: The schema_version of this ContextualData.
        :type: str
        """
        self._schema_version = schema_version

    @property
    def payload(self):
        """
        **[Required]** Gets the payload of this ContextualData.
        The context data payload


        :return: The payload of this ContextualData.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this ContextualData.
        The context data payload


        :param payload: The payload of this ContextualData.
        :type: str
        """
        self._payload = payload

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
