# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SightingType(object):
    """
    Specific behavior that can trigger a Sighting
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SightingType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SightingType.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this SightingType.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SightingType.
        :type description: str

        :param mitre_link:
            The value to assign to the mitre_link property of this SightingType.
        :type mitre_link: str

        :param tactic:
            The value to assign to the tactic property of this SightingType.
        :type tactic: str

        :param techniques:
            The value to assign to the techniques property of this SightingType.
        :type techniques: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'mitre_link': 'str',
            'tactic': 'str',
            'techniques': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'mitre_link': 'mitreLink',
            'tactic': 'tactic',
            'techniques': 'techniques'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._mitre_link = None
        self._tactic = None
        self._techniques = None

    @property
    def id(self):
        """
        Gets the id of this SightingType.
        The unique identifier of sighting type


        :return: The id of this SightingType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SightingType.
        The unique identifier of sighting type


        :param id: The id of this SightingType.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this SightingType.
        Name of the sighting type


        :return: The display_name of this SightingType.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SightingType.
        Name of the sighting type


        :param display_name: The display_name of this SightingType.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SightingType.
        Description of the sighting type


        :return: The description of this SightingType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SightingType.
        Description of the sighting type


        :param description: The description of this SightingType.
        :type: str
        """
        self._description = description

    @property
    def mitre_link(self):
        """
        Gets the mitre_link of this SightingType.
        Link of the sighting type


        :return: The mitre_link of this SightingType.
        :rtype: str
        """
        return self._mitre_link

    @mitre_link.setter
    def mitre_link(self, mitre_link):
        """
        Sets the mitre_link of this SightingType.
        Link of the sighting type


        :param mitre_link: The mitre_link of this SightingType.
        :type: str
        """
        self._mitre_link = mitre_link

    @property
    def tactic(self):
        """
        Gets the tactic of this SightingType.
        Mitre Att&ck tactic


        :return: The tactic of this SightingType.
        :rtype: str
        """
        return self._tactic

    @tactic.setter
    def tactic(self, tactic):
        """
        Sets the tactic of this SightingType.
        Mitre Att&ck tactic


        :param tactic: The tactic of this SightingType.
        :type: str
        """
        self._tactic = tactic

    @property
    def techniques(self):
        """
        Gets the techniques of this SightingType.
        List of Mitre Att&ck Techniques


        :return: The techniques of this SightingType.
        :rtype: list[str]
        """
        return self._techniques

    @techniques.setter
    def techniques(self, techniques):
        """
        Sets the techniques of this SightingType.
        List of Mitre Att&ck Techniques


        :param techniques: The techniques of this SightingType.
        :type: list[str]
        """
        self._techniques = techniques

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
