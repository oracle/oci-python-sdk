# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RenameDatasetLabelsDetails(object):
    """
    Renames a subset of Labels in the Dataset's LabelSet.  The Labels in the source LabelSet will be replaced with the Labels in the target LabelSet.
    Labels are correlated by index, i.e. the first Label in the source LabelSet will be replaced by the first Label in the target LabelSet.
    If the size of the\u00A0source and target LabelSets are not equal, the request will be rejected.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RenameDatasetLabelsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_label_set:
            The value to assign to the source_label_set property of this RenameDatasetLabelsDetails.
        :type source_label_set: oci.data_labeling_service.models.LabelSet

        :param target_label_set:
            The value to assign to the target_label_set property of this RenameDatasetLabelsDetails.
        :type target_label_set: oci.data_labeling_service.models.LabelSet

        """
        self.swagger_types = {
            'source_label_set': 'LabelSet',
            'target_label_set': 'LabelSet'
        }

        self.attribute_map = {
            'source_label_set': 'sourceLabelSet',
            'target_label_set': 'targetLabelSet'
        }

        self._source_label_set = None
        self._target_label_set = None

    @property
    def source_label_set(self):
        """
        Gets the source_label_set of this RenameDatasetLabelsDetails.

        :return: The source_label_set of this RenameDatasetLabelsDetails.
        :rtype: oci.data_labeling_service.models.LabelSet
        """
        return self._source_label_set

    @source_label_set.setter
    def source_label_set(self, source_label_set):
        """
        Sets the source_label_set of this RenameDatasetLabelsDetails.

        :param source_label_set: The source_label_set of this RenameDatasetLabelsDetails.
        :type: oci.data_labeling_service.models.LabelSet
        """
        self._source_label_set = source_label_set

    @property
    def target_label_set(self):
        """
        Gets the target_label_set of this RenameDatasetLabelsDetails.

        :return: The target_label_set of this RenameDatasetLabelsDetails.
        :rtype: oci.data_labeling_service.models.LabelSet
        """
        return self._target_label_set

    @target_label_set.setter
    def target_label_set(self, target_label_set):
        """
        Sets the target_label_set of this RenameDatasetLabelsDetails.

        :param target_label_set: The target_label_set of this RenameDatasetLabelsDetails.
        :type: oci.data_labeling_service.models.LabelSet
        """
        self._target_label_set = target_label_set

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
