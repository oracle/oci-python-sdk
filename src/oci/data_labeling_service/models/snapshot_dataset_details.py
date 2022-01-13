# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SnapshotDatasetDetails(object):
    """
    Allows outputting the latest records paired with annotations and write them to object storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SnapshotDatasetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param are_annotations_included:
            The value to assign to the are_annotations_included property of this SnapshotDatasetDetails.
        :type are_annotations_included: bool

        :param are_unannotated_records_included:
            The value to assign to the are_unannotated_records_included property of this SnapshotDatasetDetails.
        :type are_unannotated_records_included: bool

        :param export_details:
            The value to assign to the export_details property of this SnapshotDatasetDetails.
        :type export_details: oci.data_labeling_service.models.ObjectStorageSnapshotExportDetails

        :param export_format:
            The value to assign to the export_format property of this SnapshotDatasetDetails.
        :type export_format: oci.data_labeling_service.models.ExportFormat

        """
        self.swagger_types = {
            'are_annotations_included': 'bool',
            'are_unannotated_records_included': 'bool',
            'export_details': 'ObjectStorageSnapshotExportDetails',
            'export_format': 'ExportFormat'
        }

        self.attribute_map = {
            'are_annotations_included': 'areAnnotationsIncluded',
            'are_unannotated_records_included': 'areUnannotatedRecordsIncluded',
            'export_details': 'exportDetails',
            'export_format': 'exportFormat'
        }

        self._are_annotations_included = None
        self._are_unannotated_records_included = None
        self._export_details = None
        self._export_format = None

    @property
    def are_annotations_included(self):
        """
        **[Required]** Gets the are_annotations_included of this SnapshotDatasetDetails.
        Whether annotations are to be included in the export dataset digest.


        :return: The are_annotations_included of this SnapshotDatasetDetails.
        :rtype: bool
        """
        return self._are_annotations_included

    @are_annotations_included.setter
    def are_annotations_included(self, are_annotations_included):
        """
        Sets the are_annotations_included of this SnapshotDatasetDetails.
        Whether annotations are to be included in the export dataset digest.


        :param are_annotations_included: The are_annotations_included of this SnapshotDatasetDetails.
        :type: bool
        """
        self._are_annotations_included = are_annotations_included

    @property
    def are_unannotated_records_included(self):
        """
        **[Required]** Gets the are_unannotated_records_included of this SnapshotDatasetDetails.
        Whether to include records that have yet to be annotated in the export dataset digest.


        :return: The are_unannotated_records_included of this SnapshotDatasetDetails.
        :rtype: bool
        """
        return self._are_unannotated_records_included

    @are_unannotated_records_included.setter
    def are_unannotated_records_included(self, are_unannotated_records_included):
        """
        Sets the are_unannotated_records_included of this SnapshotDatasetDetails.
        Whether to include records that have yet to be annotated in the export dataset digest.


        :param are_unannotated_records_included: The are_unannotated_records_included of this SnapshotDatasetDetails.
        :type: bool
        """
        self._are_unannotated_records_included = are_unannotated_records_included

    @property
    def export_details(self):
        """
        **[Required]** Gets the export_details of this SnapshotDatasetDetails.

        :return: The export_details of this SnapshotDatasetDetails.
        :rtype: oci.data_labeling_service.models.ObjectStorageSnapshotExportDetails
        """
        return self._export_details

    @export_details.setter
    def export_details(self, export_details):
        """
        Sets the export_details of this SnapshotDatasetDetails.

        :param export_details: The export_details of this SnapshotDatasetDetails.
        :type: oci.data_labeling_service.models.ObjectStorageSnapshotExportDetails
        """
        self._export_details = export_details

    @property
    def export_format(self):
        """
        Gets the export_format of this SnapshotDatasetDetails.

        :return: The export_format of this SnapshotDatasetDetails.
        :rtype: oci.data_labeling_service.models.ExportFormat
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        """
        Sets the export_format of this SnapshotDatasetDetails.

        :param export_format: The export_format of this SnapshotDatasetDetails.
        :type: oci.data_labeling_service.models.ExportFormat
        """
        self._export_format = export_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
