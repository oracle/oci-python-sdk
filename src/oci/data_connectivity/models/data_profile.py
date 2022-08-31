# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataProfile(object):
    """
    The data profile response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataProfile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_name:
            The value to assign to the entity_name property of this DataProfile.
        :type entity_name: str

        :param entity_profile_result:
            The value to assign to the entity_profile_result property of this DataProfile.
        :type entity_profile_result: oci.data_connectivity.models.EntityProfileResult

        :param attribute_profile_results:
            The value to assign to the attribute_profile_results property of this DataProfile.
        :type attribute_profile_results: list[oci.data_connectivity.models.AttributeProfileResult]

        """
        self.swagger_types = {
            'entity_name': 'str',
            'entity_profile_result': 'EntityProfileResult',
            'attribute_profile_results': 'list[AttributeProfileResult]'
        }

        self.attribute_map = {
            'entity_name': 'entityName',
            'entity_profile_result': 'entityProfileResult',
            'attribute_profile_results': 'attributeProfileResults'
        }

        self._entity_name = None
        self._entity_profile_result = None
        self._attribute_profile_results = None

    @property
    def entity_name(self):
        """
        **[Required]** Gets the entity_name of this DataProfile.
        Entity name for which profiling is requested.


        :return: The entity_name of this DataProfile.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this DataProfile.
        Entity name for which profiling is requested.


        :param entity_name: The entity_name of this DataProfile.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def entity_profile_result(self):
        """
        Gets the entity_profile_result of this DataProfile.

        :return: The entity_profile_result of this DataProfile.
        :rtype: oci.data_connectivity.models.EntityProfileResult
        """
        return self._entity_profile_result

    @entity_profile_result.setter
    def entity_profile_result(self, entity_profile_result):
        """
        Sets the entity_profile_result of this DataProfile.

        :param entity_profile_result: The entity_profile_result of this DataProfile.
        :type: oci.data_connectivity.models.EntityProfileResult
        """
        self._entity_profile_result = entity_profile_result

    @property
    def attribute_profile_results(self):
        """
        Gets the attribute_profile_results of this DataProfile.
        Array of profiling results.


        :return: The attribute_profile_results of this DataProfile.
        :rtype: list[oci.data_connectivity.models.AttributeProfileResult]
        """
        return self._attribute_profile_results

    @attribute_profile_results.setter
    def attribute_profile_results(self, attribute_profile_results):
        """
        Sets the attribute_profile_results of this DataProfile.
        Array of profiling results.


        :param attribute_profile_results: The attribute_profile_results of this DataProfile.
        :type: list[oci.data_connectivity.models.AttributeProfileResult]
        """
        self._attribute_profile_results = attribute_profile_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
