# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WarningReferenceDetails(object):
    """
    A list of LogAnalyticsWarning references.  Used as input to APIs which operate on a
    list.  For example, the suppress warning API accepts a list of warning references
    and will suppress all warnings in the input list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WarningReferenceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param warning_references:
            The value to assign to the warning_references property of this WarningReferenceDetails.
        :type warning_references: list[str]

        """
        self.swagger_types = {
            'warning_references': 'list[str]'
        }

        self.attribute_map = {
            'warning_references': 'warningReferences'
        }

        self._warning_references = None

    @property
    def warning_references(self):
        """
        Gets the warning_references of this WarningReferenceDetails.
        A list of LogAnalyticsWarning references.  Used as input to APIs which operate on a
        list.  For example, the suppress warning API accepts a list of warning references
        and will suppress all warnings in the input list.


        :return: The warning_references of this WarningReferenceDetails.
        :rtype: list[str]
        """
        return self._warning_references

    @warning_references.setter
    def warning_references(self, warning_references):
        """
        Sets the warning_references of this WarningReferenceDetails.
        A list of LogAnalyticsWarning references.  Used as input to APIs which operate on a
        list.  For example, the suppress warning API accepts a list of warning references
        and will suppress all warnings in the input list.


        :param warning_references: The warning_references of this WarningReferenceDetails.
        :type: list[str]
        """
        self._warning_references = warning_references

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
