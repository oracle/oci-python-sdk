# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContactList(object):
    """
    List of contacts
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContactList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param contact_list:
            The value to assign to the contact_list property of this ContactList.
        :type contact_list: list[Contact]

        """
        self.swagger_types = {
            'contact_list': 'list[Contact]'
        }

        self.attribute_map = {
            'contact_list': 'contactList'
        }

        self._contact_list = None

    @property
    def contact_list(self):
        """
        **[Required]** Gets the contact_list of this ContactList.
        List of contacts


        :return: The contact_list of this ContactList.
        :rtype: list[Contact]
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """
        Sets the contact_list of this ContactList.
        List of contacts


        :param contact_list: The contact_list of this ContactList.
        :type: list[Contact]
        """
        self._contact_list = contact_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
