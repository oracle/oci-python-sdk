# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dataset_details import DatasetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageDataset(DatasetDetails):
    """
    Different type of location types supported for object storage
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageDataset object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.ObjectStorageDataset.dataset_type` attribute
        of this class is ``OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dataset_type:
            The value to assign to the dataset_type property of this ObjectStorageDataset.
            Allowed values for this property are: "OBJECT_STORAGE", "DATA_SCIENCE_LABELING"
        :type dataset_type: str

        :param location_details:
            The value to assign to the location_details property of this ObjectStorageDataset.
        :type location_details: oci.ai_language.models.LocationDetails

        """
        self.swagger_types = {
            'dataset_type': 'str',
            'location_details': 'LocationDetails'
        }

        self.attribute_map = {
            'dataset_type': 'datasetType',
            'location_details': 'locationDetails'
        }

        self._dataset_type = None
        self._location_details = None
        self._dataset_type = 'OBJECT_STORAGE'

    @property
    def location_details(self):
        """
        **[Required]** Gets the location_details of this ObjectStorageDataset.

        :return: The location_details of this ObjectStorageDataset.
        :rtype: oci.ai_language.models.LocationDetails
        """
        return self._location_details

    @location_details.setter
    def location_details(self, location_details):
        """
        Sets the location_details of this ObjectStorageDataset.

        :param location_details: The location_details of this ObjectStorageDataset.
        :type: oci.ai_language.models.LocationDetails
        """
        self._location_details = location_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
