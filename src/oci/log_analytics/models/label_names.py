# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LabelNames(object):
    """
    LabelName
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LabelNames object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label_names:
            The value to assign to the label_names property of this LabelNames.
        :type label_names: list[str]

        """
        self.swagger_types = {
            'label_names': 'list[str]'
        }

        self.attribute_map = {
            'label_names': 'labelNames'
        }

        self._label_names = None

    @property
    def label_names(self):
        """
        Gets the label_names of this LabelNames.
        An array of label names.


        :return: The label_names of this LabelNames.
        :rtype: list[str]
        """
        return self._label_names

    @label_names.setter
    def label_names(self, label_names):
        """
        Sets the label_names of this LabelNames.
        An array of label names.


        :param label_names: The label_names of this LabelNames.
        :type: list[str]
        """
        self._label_names = label_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
