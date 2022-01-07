# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachedView(object):
    """
    Properties of an attached view.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachedView object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param view_id:
            The value to assign to the view_id property of this AttachedView.
        :type view_id: str

        """
        self.swagger_types = {
            'view_id': 'str'
        }

        self.attribute_map = {
            'view_id': 'viewId'
        }

        self._view_id = None

    @property
    def view_id(self):
        """
        **[Required]** Gets the view_id of this AttachedView.
        The OCID of the view.


        :return: The view_id of this AttachedView.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """
        Sets the view_id of this AttachedView.
        The OCID of the view.


        :param view_id: The view_id of this AttachedView.
        :type: str
        """
        self._view_id = view_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
