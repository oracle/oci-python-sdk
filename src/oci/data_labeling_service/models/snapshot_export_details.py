# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SnapshotExportDetails(object):
    """
    Specifies where to output the export.
    """

    #: A constant which can be used with the export_type property of a SnapshotExportDetails.
    #: This constant has a value of "OBJECT_STORAGE"
    EXPORT_TYPE_OBJECT_STORAGE = "OBJECT_STORAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new SnapshotExportDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_labeling_service.models.ObjectStorageSnapshotExportDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_type:
            The value to assign to the export_type property of this SnapshotExportDetails.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type export_type: str

        """
        self.swagger_types = {
            'export_type': 'str'
        }

        self.attribute_map = {
            'export_type': 'exportType'
        }

        self._export_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['exportType']

        if type == 'OBJECT_STORAGE':
            return 'ObjectStorageSnapshotExportDetails'
        else:
            return 'SnapshotExportDetails'

    @property
    def export_type(self):
        """
        **[Required]** Gets the export_type of this SnapshotExportDetails.
        The target destination for the snapshot.  Using OBJECT_STORAGE means the snapshot will be written to Object Storage.

        Allowed values for this property are: "OBJECT_STORAGE"


        :return: The export_type of this SnapshotExportDetails.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """
        Sets the export_type of this SnapshotExportDetails.
        The target destination for the snapshot.  Using OBJECT_STORAGE means the snapshot will be written to Object Storage.


        :param export_type: The export_type of this SnapshotExportDetails.
        :type: str
        """
        allowed_values = ["OBJECT_STORAGE"]
        if not value_allowed_none_or_none_sentinel(export_type, allowed_values):
            raise ValueError(
                "Invalid value for `export_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._export_type = export_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
