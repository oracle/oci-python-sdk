# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableHostInsightDetails(object):
    """
    The information about the host to be analyzed.
    """

    #: A constant which can be used with the entity_source property of a EnableHostInsightDetails.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_HOST = "MACS_MANAGED_EXTERNAL_HOST"

    #: A constant which can be used with the entity_source property of a EnableHostInsightDetails.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_HOST = "EM_MANAGED_EXTERNAL_HOST"

    def __init__(self, **kwargs):
        """
        Initializes a new EnableHostInsightDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.EnableMacsManagedExternalHostInsightDetails`
        * :class:`~oci.opsi.models.EnableEmManagedExternalHostInsightDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this EnableHostInsightDetails.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"
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

        if type == 'MACS_MANAGED_EXTERNAL_HOST':
            return 'EnableMacsManagedExternalHostInsightDetails'

        if type == 'EM_MANAGED_EXTERNAL_HOST':
            return 'EnableEmManagedExternalHostInsightDetails'
        else:
            return 'EnableHostInsightDetails'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this EnableHostInsightDetails.
        Source of the host entity.

        Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"


        :return: The entity_source of this EnableHostInsightDetails.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this EnableHostInsightDetails.
        Source of the host entity.


        :param entity_source: The entity_source of this EnableHostInsightDetails.
        :type: str
        """
        allowed_values = ["MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"]
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
