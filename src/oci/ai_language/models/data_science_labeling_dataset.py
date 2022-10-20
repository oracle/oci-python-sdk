# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dataset_details import DatasetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataScienceLabelingDataset(DatasetDetails):
    """
    Dataset that uses data science labelling service as underlying data source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataScienceLabelingDataset object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.DataScienceLabelingDataset.dataset_type` attribute
        of this class is ``DATA_SCIENCE_LABELING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dataset_type:
            The value to assign to the dataset_type property of this DataScienceLabelingDataset.
            Allowed values for this property are: "OBJECT_STORAGE", "DATA_SCIENCE_LABELING"
        :type dataset_type: str

        :param dataset_id:
            The value to assign to the dataset_id property of this DataScienceLabelingDataset.
        :type dataset_id: str

        """
        self.swagger_types = {
            'dataset_type': 'str',
            'dataset_id': 'str'
        }

        self.attribute_map = {
            'dataset_type': 'datasetType',
            'dataset_id': 'datasetId'
        }

        self._dataset_type = None
        self._dataset_id = None
        self._dataset_type = 'DATA_SCIENCE_LABELING'

    @property
    def dataset_id(self):
        """
        **[Required]** Gets the dataset_id of this DataScienceLabelingDataset.
        Data Science Labelling Service OCID


        :return: The dataset_id of this DataScienceLabelingDataset.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """
        Sets the dataset_id of this DataScienceLabelingDataset.
        Data Science Labelling Service OCID


        :param dataset_id: The dataset_id of this DataScienceLabelingDataset.
        :type: str
        """
        self._dataset_id = dataset_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
