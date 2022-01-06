# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublisherSummary(object):
    """
    Summary details about the publisher of the listing.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublisherSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PublisherSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this PublisherSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this PublisherSummary.
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
        Gets the id of this PublisherSummary.
        The unique identifier for the publisher.


        :return: The id of this PublisherSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PublisherSummary.
        The unique identifier for the publisher.


        :param id: The id of this PublisherSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PublisherSummary.
        The name of the publisher.


        :return: The name of this PublisherSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PublisherSummary.
        The name of the publisher.


        :param name: The name of this PublisherSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PublisherSummary.
        A description of the publisher.


        :return: The description of this PublisherSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PublisherSummary.
        A description of the publisher.


        :param description: The description of this PublisherSummary.
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
