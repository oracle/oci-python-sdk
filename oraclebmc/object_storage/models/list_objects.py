# coding: utf-8
# Copyright (c) 2017 Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class ListObjects(object):

    def __init__(self):

        self.swagger_types = {
            'objects': 'list[ObjectSummary]',
            'prefixes': 'list[str]',
            'next_start_with': 'str'
        }

        self.attribute_map = {
            'objects': 'objects',
            'prefixes': 'prefixes',
            'next_start_with': 'nextStartWith'
        }

        self._objects = None
        self._prefixes = None
        self._next_start_with = None

    @property
    def objects(self):
        """
        Gets the objects of this ListObjects.

        :return: The objects of this ListObjects.
        :rtype: list[ObjectSummary]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this ListObjects.

        :param objects: The objects of this ListObjects.
        :type: list[ObjectSummary]
        """
        self._objects = objects

    @property
    def prefixes(self):
        """
        Gets the prefixes of this ListObjects.

        :return: The prefixes of this ListObjects.
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """
        Sets the prefixes of this ListObjects.

        :param prefixes: The prefixes of this ListObjects.
        :type: list[str]
        """
        self._prefixes = prefixes

    @property
    def next_start_with(self):
        """
        Gets the next_start_with of this ListObjects.
        The name of the object to be used in startWith parameter to obtain next page of
        a truncated list objects response.


        :return: The next_start_with of this ListObjects.
        :rtype: str
        """
        return self._next_start_with

    @next_start_with.setter
    def next_start_with(self, next_start_with):
        """
        Sets the next_start_with of this ListObjects.
        The name of the object to be used in startWith parameter to obtain next page of
        a truncated list objects response.


        :param next_start_with: The next_start_with of this ListObjects.
        :type: str
        """
        self._next_start_with = next_start_with

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
