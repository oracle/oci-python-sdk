# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableDatabaseInsightDetails(object):
    """
    The information about database to be analyzed.
    """

    #: A constant which can be used with the entity_source property of a EnableDatabaseInsightDetails.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_DATABASE"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_DATABASE = "EM_MANAGED_EXTERNAL_DATABASE"

    #: A constant which can be used with the entity_source property of a EnableDatabaseInsightDetails.
    #: This constant has a value of "PE_COMANAGED_DATABASE"
    ENTITY_SOURCE_PE_COMANAGED_DATABASE = "PE_COMANAGED_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new EnableDatabaseInsightDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.EnableEmManagedExternalDatabaseInsightDetails`
        * :class:`~oci.opsi.models.EnablePeComanagedDatabaseInsightDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnableDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"
        :type entity_source: str

        """
        self.swagger_types = {
            'entity_source': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource'
        }

        self._entity_source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'EM_MANAGED_EXTERNAL_DATABASE':
            return 'EnableEmManagedExternalDatabaseInsightDetails'

        if type == 'PE_COMANAGED_DATABASE':
            return 'EnablePeComanagedDatabaseInsightDetails'
        else:
            return 'EnableDatabaseInsightDetails'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this EnableDatabaseInsightDetails.
        Source of the database entity.

        Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"


        :return: The entity_source of this EnableDatabaseInsightDetails.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this EnableDatabaseInsightDetails.
        Source of the database entity.


        :param entity_source: The entity_source of this EnableDatabaseInsightDetails.
        :type: str
        """
        allowed_values = ["EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            raise ValueError(
                "Invalid value for `entity_source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._entity_source = entity_source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
