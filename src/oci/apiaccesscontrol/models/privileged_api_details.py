# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivilegedApiDetails(object):
    """
    It represents the api details of the service
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivilegedApiDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this PrivilegedApiDetails.
        :type entity_type: str

        :param api_name:
            The value to assign to the api_name property of this PrivilegedApiDetails.
        :type api_name: str

        :param attribute_names:
            The value to assign to the attribute_names property of this PrivilegedApiDetails.
        :type attribute_names: list[str]

        """
        self.swagger_types = {
            'entity_type': 'str',
            'api_name': 'str',
            'attribute_names': 'list[str]'
        }
        self.attribute_map = {
            'entity_type': 'entityType',
            'api_name': 'apiName',
            'attribute_names': 'attributeNames'
        }
        self._entity_type = None
        self._api_name = None
        self._attribute_names = None

    @property
    def entity_type(self):
        """
        Gets the entity_type of this PrivilegedApiDetails.
        type of the entity which needs to be protected.


        :return: The entity_type of this PrivilegedApiDetails.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this PrivilegedApiDetails.
        type of the entity which needs to be protected.


        :param entity_type: The entity_type of this PrivilegedApiDetails.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def api_name(self):
        """
        **[Required]** Gets the api_name of this PrivilegedApiDetails.
        name of the api which needs to be protected.


        :return: The api_name of this PrivilegedApiDetails.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """
        Sets the api_name of this PrivilegedApiDetails.
        name of the api which needs to be protected.


        :param api_name: The api_name of this PrivilegedApiDetails.
        :type: str
        """
        self._api_name = api_name

    @property
    def attribute_names(self):
        """
        Gets the attribute_names of this PrivilegedApiDetails.
        list of attributes belonging to the above api which needs to be protected.


        :return: The attribute_names of this PrivilegedApiDetails.
        :rtype: list[str]
        """
        return self._attribute_names

    @attribute_names.setter
    def attribute_names(self, attribute_names):
        """
        Sets the attribute_names of this PrivilegedApiDetails.
        list of attributes belonging to the above api which needs to be protected.


        :param attribute_names: The attribute_names of this PrivilegedApiDetails.
        :type: list[str]
        """
        self._attribute_names = attribute_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
