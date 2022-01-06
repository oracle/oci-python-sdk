# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Query(object):
    """
    The query to filter and aggregate.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Query object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Query.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Query.
        :type compartment_id: str

        :param query_definition:
            The value to assign to the query_definition property of this Query.
        :type query_definition: oci.usage_api.models.QueryDefinition

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'query_definition': 'QueryDefinition'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'query_definition': 'queryDefinition'
        }

        self._id = None
        self._compartment_id = None
        self._query_definition = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Query.
        The query OCID.


        :return: The id of this Query.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Query.
        The query OCID.


        :param id: The id of this Query.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Query.
        The compartment OCID.


        :return: The compartment_id of this Query.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Query.
        The compartment OCID.


        :param compartment_id: The compartment_id of this Query.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def query_definition(self):
        """
        **[Required]** Gets the query_definition of this Query.

        :return: The query_definition of this Query.
        :rtype: oci.usage_api.models.QueryDefinition
        """
        return self._query_definition

    @query_definition.setter
    def query_definition(self, query_definition):
        """
        Sets the query_definition of this Query.

        :param query_definition: The query_definition of this Query.
        :type: oci.usage_api.models.QueryDefinition
        """
        self._query_definition = query_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
