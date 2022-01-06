# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiffSection(object):
    """
    Details about a section of changes within a difference chunk.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiffSection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DiffSection.
        :type type: str

        :param lines:
            The value to assign to the lines property of this DiffSection.
        :type lines: list[oci.devops.models.DiffLineDetails]

        """
        self.swagger_types = {
            'type': 'str',
            'lines': 'list[DiffLineDetails]'
        }

        self.attribute_map = {
            'type': 'type',
            'lines': 'lines'
        }

        self._type = None
        self._lines = None

    @property
    def type(self):
        """
        Gets the type of this DiffSection.
        Type of change.


        :return: The type of this DiffSection.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DiffSection.
        Type of change.


        :param type: The type of this DiffSection.
        :type: str
        """
        self._type = type

    @property
    def lines(self):
        """
        Gets the lines of this DiffSection.
        The lines within changed section.


        :return: The lines of this DiffSection.
        :rtype: list[oci.devops.models.DiffLineDetails]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this DiffSection.
        The lines within changed section.


        :param lines: The lines of this DiffSection.
        :type: list[oci.devops.models.DiffLineDetails]
        """
        self._lines = lines

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
