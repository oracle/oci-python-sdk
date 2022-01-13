# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecordAggregationDimensions(object):
    """
    The dimensions to summarize record information for a given dataset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RecordAggregationDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_labeled:
            The value to assign to the is_labeled property of this RecordAggregationDimensions.
        :type is_labeled: bool

        :param annotation_label_contains:
            The value to assign to the annotation_label_contains property of this RecordAggregationDimensions.
        :type annotation_label_contains: str

        """
        self.swagger_types = {
            'is_labeled': 'bool',
            'annotation_label_contains': 'str'
        }

        self.attribute_map = {
            'is_labeled': 'isLabeled',
            'annotation_label_contains': 'annotationLabelContains'
        }

        self._is_labeled = None
        self._annotation_label_contains = None

    @property
    def is_labeled(self):
        """
        Gets the is_labeled of this RecordAggregationDimensions.
        Whether or not the record has been labeled and has associated annotations.


        :return: The is_labeled of this RecordAggregationDimensions.
        :rtype: bool
        """
        return self._is_labeled

    @is_labeled.setter
    def is_labeled(self, is_labeled):
        """
        Sets the is_labeled of this RecordAggregationDimensions.
        Whether or not the record has been labeled and has associated annotations.


        :param is_labeled: The is_labeled of this RecordAggregationDimensions.
        :type: bool
        """
        self._is_labeled = is_labeled

    @property
    def annotation_label_contains(self):
        """
        Gets the annotation_label_contains of this RecordAggregationDimensions.
        Whether or not the annotation contains a label.


        :return: The annotation_label_contains of this RecordAggregationDimensions.
        :rtype: str
        """
        return self._annotation_label_contains

    @annotation_label_contains.setter
    def annotation_label_contains(self, annotation_label_contains):
        """
        Sets the annotation_label_contains of this RecordAggregationDimensions.
        Whether or not the annotation contains a label.


        :param annotation_label_contains: The annotation_label_contains of this RecordAggregationDimensions.
        :type: str
        """
        self._annotation_label_contains = annotation_label_contains

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
