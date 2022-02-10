# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Label(object):
    """
    A label describing an image. Every label returned by the pre-deployed model will be in English.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Label object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Label.
        :type name: str

        :param confidence:
            The value to assign to the confidence property of this Label.
        :type confidence: float

        """
        self.swagger_types = {
            'name': 'str',
            'confidence': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'confidence': 'confidence'
        }

        self._name = None
        self._confidence = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Label.
        Classification catagory label name.


        :return: The name of this Label.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Label.
        Classification catagory label name.


        :param name: The name of this Label.
        :type: str
        """
        self._name = name

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this Label.
        Confidence score between 0 to 1.


        :return: The confidence of this Label.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Label.
        Confidence score between 0 to 1.


        :param confidence: The confidence of this Label.
        :type: float
        """
        self._confidence = confidence

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
