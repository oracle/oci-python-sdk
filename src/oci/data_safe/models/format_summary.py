# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FormatSummary(object):
    """
    Summary of a masking format.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FormatSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FormatSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this FormatSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this FormatSummary.
        :type description: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description'
        }

        self._id = None
        self._name = None
        self._description = None

    @property
    def id(self):
        """
        Gets the id of this FormatSummary.
        The OCID of the masking format.


        :return: The id of this FormatSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FormatSummary.
        The OCID of the masking format.


        :param id: The id of this FormatSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this FormatSummary.
        The name of the masking format.


        :return: The name of this FormatSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FormatSummary.
        The name of the masking format.


        :param name: The name of this FormatSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FormatSummary.
        The description of the masking format.


        :return: The description of this FormatSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FormatSummary.
        The description of the masking format.


        :param description: The description of this FormatSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
