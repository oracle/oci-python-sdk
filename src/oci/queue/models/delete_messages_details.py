# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeleteMessagesDetails(object):
    """
    The details of a DeleteMessages request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeleteMessagesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entries:
            The value to assign to the entries property of this DeleteMessagesDetails.
        :type entries: list[oci.queue.models.DeleteMessagesDetailsEntry]

        """
        self.swagger_types = {
            'entries': 'list[DeleteMessagesDetailsEntry]'
        }

        self.attribute_map = {
            'entries': 'entries'
        }

        self._entries = None

    @property
    def entries(self):
        """
        **[Required]** Gets the entries of this DeleteMessagesDetails.
        The array of messages to delete from a queue.


        :return: The entries of this DeleteMessagesDetails.
        :rtype: list[oci.queue.models.DeleteMessagesDetailsEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this DeleteMessagesDetails.
        The array of messages to delete from a queue.


        :param entries: The entries of this DeleteMessagesDetails.
        :type: list[oci.queue.models.DeleteMessagesDetailsEntry]
        """
        self._entries = entries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
