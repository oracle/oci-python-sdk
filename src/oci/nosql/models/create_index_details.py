# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIndexDetails(object):
    """
    Specifications for the new index.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIndexDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateIndexDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIndexDetails.
        :type compartment_id: str

        :param keys:
            The value to assign to the keys property of this CreateIndexDetails.
        :type keys: list[oci.nosql.models.IndexKey]

        :param is_if_not_exists:
            The value to assign to the is_if_not_exists property of this CreateIndexDetails.
        :type is_if_not_exists: bool

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'keys': 'list[IndexKey]',
            'is_if_not_exists': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'keys': 'keys',
            'is_if_not_exists': 'isIfNotExists'
        }

        self._name = None
        self._compartment_id = None
        self._keys = None
        self._is_if_not_exists = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateIndexDetails.
        Index name.


        :return: The name of this CreateIndexDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateIndexDetails.
        Index name.


        :param name: The name of this CreateIndexDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateIndexDetails.
        The OCID of the table's compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and compartmentId is supplied, the latter
        must match the identified table's compartmentId.


        :return: The compartment_id of this CreateIndexDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIndexDetails.
        The OCID of the table's compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and compartmentId is supplied, the latter
        must match the identified table's compartmentId.


        :param compartment_id: The compartment_id of this CreateIndexDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def keys(self):
        """
        **[Required]** Gets the keys of this CreateIndexDetails.
        A set of keys for a secondary index.


        :return: The keys of this CreateIndexDetails.
        :rtype: list[oci.nosql.models.IndexKey]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """
        Sets the keys of this CreateIndexDetails.
        A set of keys for a secondary index.


        :param keys: The keys of this CreateIndexDetails.
        :type: list[oci.nosql.models.IndexKey]
        """
        self._keys = keys

    @property
    def is_if_not_exists(self):
        """
        Gets the is_if_not_exists of this CreateIndexDetails.
        If true, the operation completes successfully even when the
        index exists.  Otherwise, an attempt to create an index
        that already exists will return an error.


        :return: The is_if_not_exists of this CreateIndexDetails.
        :rtype: bool
        """
        return self._is_if_not_exists

    @is_if_not_exists.setter
    def is_if_not_exists(self, is_if_not_exists):
        """
        Sets the is_if_not_exists of this CreateIndexDetails.
        If true, the operation completes successfully even when the
        index exists.  Otherwise, an attempt to create an index
        that already exists will return an error.


        :param is_if_not_exists: The is_if_not_exists of this CreateIndexDetails.
        :type: bool
        """
        self._is_if_not_exists = is_if_not_exists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
