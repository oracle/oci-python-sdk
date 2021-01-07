# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CandidateResponderRule(object):
    """
    Candidate Responder Rule list in Detector rule
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CandidateResponderRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CandidateResponderRule.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this CandidateResponderRule.
        :type display_name: str

        :param is_preferred:
            The value to assign to the is_preferred property of this CandidateResponderRule.
        :type is_preferred: bool

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'is_preferred': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'is_preferred': 'isPreferred'
        }

        self._id = None
        self._display_name = None
        self._is_preferred = None

    @property
    def id(self):
        """
        Gets the id of this CandidateResponderRule.
        The unique identifier of the Responder rule


        :return: The id of this CandidateResponderRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CandidateResponderRule.
        The unique identifier of the Responder rule


        :param id: The id of this CandidateResponderRule.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this CandidateResponderRule.
        The display name of the Responder rule


        :return: The display_name of this CandidateResponderRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CandidateResponderRule.
        The display name of the Responder rule


        :param display_name: The display_name of this CandidateResponderRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_preferred(self):
        """
        Gets the is_preferred of this CandidateResponderRule.
        Preferred state


        :return: The is_preferred of this CandidateResponderRule.
        :rtype: bool
        """
        return self._is_preferred

    @is_preferred.setter
    def is_preferred(self, is_preferred):
        """
        Sets the is_preferred of this CandidateResponderRule.
        Preferred state


        :param is_preferred: The is_preferred of this CandidateResponderRule.
        :type: bool
        """
        self._is_preferred = is_preferred

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
