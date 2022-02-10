# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataVisibility(object):
    """
    The visibility level associated with data and an associated TLP (https://www.cisa.gov/tlp) level.
    """

    #: A constant which can be used with the tlp_name property of a DataVisibility.
    #: This constant has a value of "TLP_INTERNAL_AUDIT"
    TLP_NAME_TLP_INTERNAL_AUDIT = "TLP_INTERNAL_AUDIT"

    #: A constant which can be used with the tlp_name property of a DataVisibility.
    #: This constant has a value of "TLP_WHITE"
    TLP_NAME_TLP_WHITE = "TLP_WHITE"

    #: A constant which can be used with the tlp_name property of a DataVisibility.
    #: This constant has a value of "TLP_GREEN"
    TLP_NAME_TLP_GREEN = "TLP_GREEN"

    #: A constant which can be used with the tlp_name property of a DataVisibility.
    #: This constant has a value of "TLP_AMBER"
    TLP_NAME_TLP_AMBER = "TLP_AMBER"

    #: A constant which can be used with the tlp_name property of a DataVisibility.
    #: This constant has a value of "TLP_RED"
    TLP_NAME_TLP_RED = "TLP_RED"

    def __init__(self, **kwargs):
        """
        Initializes a new DataVisibility object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DataVisibility.
        :type name: str

        :param tlp_name:
            The value to assign to the tlp_name property of this DataVisibility.
            Allowed values for this property are: "TLP_INTERNAL_AUDIT", "TLP_WHITE", "TLP_GREEN", "TLP_AMBER", "TLP_RED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tlp_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'tlp_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'tlp_name': 'tlpName'
        }

        self._name = None
        self._tlp_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DataVisibility.
        The name of the visibility level.


        :return: The name of this DataVisibility.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataVisibility.
        The name of the visibility level.


        :param name: The name of this DataVisibility.
        :type: str
        """
        self._name = name

    @property
    def tlp_name(self):
        """
        **[Required]** Gets the tlp_name of this DataVisibility.
        The Traffic Light Protocol (TLP) name of the visibility level.

        Allowed values for this property are: "TLP_INTERNAL_AUDIT", "TLP_WHITE", "TLP_GREEN", "TLP_AMBER", "TLP_RED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tlp_name of this DataVisibility.
        :rtype: str
        """
        return self._tlp_name

    @tlp_name.setter
    def tlp_name(self, tlp_name):
        """
        Sets the tlp_name of this DataVisibility.
        The Traffic Light Protocol (TLP) name of the visibility level.


        :param tlp_name: The tlp_name of this DataVisibility.
        :type: str
        """
        allowed_values = ["TLP_INTERNAL_AUDIT", "TLP_WHITE", "TLP_GREEN", "TLP_AMBER", "TLP_RED"]
        if not value_allowed_none_or_none_sentinel(tlp_name, allowed_values):
            tlp_name = 'UNKNOWN_ENUM_VALUE'
        self._tlp_name = tlp_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
