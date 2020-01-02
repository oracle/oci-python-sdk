# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Link(object):
    """
    The model for links.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Link object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param href:
            The value to assign to the href property of this Link.
        :type href: str

        """
        self.swagger_types = {
            'href': 'str'
        }

        self.attribute_map = {
            'href': 'href'
        }

        self._href = None

    @property
    def href(self):
        """
        Gets the href of this Link.
        The anchor tag.


        :return: The href of this Link.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this Link.
        The anchor tag.


        :param href: The href of this Link.
        :type: str
        """
        self._href = href

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
