# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity_reference import EntityReference
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndicatorReference(EntityReference):
    """
    A reference to a threat indicator resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IndicatorReference object with values from keyword arguments. The default value of the :py:attr:`~oci.threat_intelligence.models.IndicatorReference.type` attribute
        of this class is ``INDICATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this IndicatorReference.
            Allowed values for this property are: "INDICATOR"
        :type type: str

        :param indicator_id:
            The value to assign to the indicator_id property of this IndicatorReference.
        :type indicator_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'indicator_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'indicator_id': 'indicatorId'
        }

        self._type = None
        self._indicator_id = None
        self._type = 'INDICATOR'

    @property
    def indicator_id(self):
        """
        **[Required]** Gets the indicator_id of this IndicatorReference.
        The unique OCID of the referenced threat indicator.


        :return: The indicator_id of this IndicatorReference.
        :rtype: str
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """
        Sets the indicator_id of this IndicatorReference.
        The unique OCID of the referenced threat indicator.


        :param indicator_id: The indicator_id of this IndicatorReference.
        :type: str
        """
        self._indicator_id = indicator_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
