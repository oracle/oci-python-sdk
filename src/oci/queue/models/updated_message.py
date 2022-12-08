# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatedMessage(object):
    """
    An updated message with the new visibility.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatedMessage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdatedMessage.
        :type id: int

        :param visible_after:
            The value to assign to the visible_after property of this UpdatedMessage.
        :type visible_after: datetime

        """
        self.swagger_types = {
            'id': 'int',
            'visible_after': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'visible_after': 'visibleAfter'
        }

        self._id = None
        self._visible_after = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this UpdatedMessage.
        The id of the message that's been updated.


        :return: The id of this UpdatedMessage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdatedMessage.
        The id of the message that's been updated.


        :param id: The id of this UpdatedMessage.
        :type: int
        """
        self._id = id

    @property
    def visible_after(self):
        """
        **[Required]** Gets the visible_after of this UpdatedMessage.
        The time after which the message will be visible to other consumers. An RFC3339 formatted datetime string


        :return: The visible_after of this UpdatedMessage.
        :rtype: datetime
        """
        return self._visible_after

    @visible_after.setter
    def visible_after(self, visible_after):
        """
        Sets the visible_after of this UpdatedMessage.
        The time after which the message will be visible to other consumers. An RFC3339 formatted datetime string


        :param visible_after: The visible_after of this UpdatedMessage.
        :type: datetime
        """
        self._visible_after = visible_after

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
