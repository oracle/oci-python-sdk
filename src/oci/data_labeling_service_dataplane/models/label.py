# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Label(object):
    """
    A label is a string value.  The API validates that it's one of the dataset's pre-defined labels.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Label object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this Label.
        :type label: str

        """
        self.swagger_types = {
            'label': 'str'
        }

        self.attribute_map = {
            'label': 'label'
        }

        self._label = None

    @property
    def label(self):
        """
        **[Required]** Gets the label of this Label.
        The label provided by the annotator.


        :return: The label of this Label.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Label.
        The label provided by the annotator.


        :param label: The label of this Label.
        :type: str
        """
        self._label = label

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
