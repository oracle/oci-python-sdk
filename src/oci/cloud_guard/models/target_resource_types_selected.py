# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_selected import TargetSelected
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetResourceTypesSelected(TargetSelected):
    """
    Target selection on basis of TargetResourceTypes.
    """

    #: A constant which can be used with the values property of a TargetResourceTypesSelected.
    #: This constant has a value of "COMPARTMENT"
    VALUES_COMPARTMENT = "COMPARTMENT"

    #: A constant which can be used with the values property of a TargetResourceTypesSelected.
    #: This constant has a value of "ERPCLOUD"
    VALUES_ERPCLOUD = "ERPCLOUD"

    #: A constant which can be used with the values property of a TargetResourceTypesSelected.
    #: This constant has a value of "HCMCLOUD"
    VALUES_HCMCLOUD = "HCMCLOUD"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetResourceTypesSelected object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.TargetResourceTypesSelected.kind` attribute
        of this class is ``TARGETTYPES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this TargetResourceTypesSelected.
            Allowed values for this property are: "ALL", "TARGETTYPES", "TARGETIDS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param values:
            The value to assign to the values property of this TargetResourceTypesSelected.
            Allowed values for items in this list are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type values: list[str]

        """
        self.swagger_types = {
            'kind': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'values': 'values'
        }

        self._kind = None
        self._values = None
        self._kind = 'TARGETTYPES'

    @property
    def values(self):
        """
        Gets the values of this TargetResourceTypesSelected.
        Types of Targets

        Allowed values for items in this list are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The values of this TargetResourceTypesSelected.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this TargetResourceTypesSelected.
        Types of Targets


        :param values: The values of this TargetResourceTypesSelected.
        :type: list[str]
        """
        allowed_values = ["COMPARTMENT", "ERPCLOUD", "HCMCLOUD"]
        if values:
            values[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in values]
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
