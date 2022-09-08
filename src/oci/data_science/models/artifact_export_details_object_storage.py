# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .artifact_export_details import ArtifactExportDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ArtifactExportDetailsObjectStorage(ArtifactExportDetails):
    """
    Model artifact source details for exporting artifact to service bucket
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ArtifactExportDetailsObjectStorage object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ArtifactExportDetailsObjectStorage.artifact_source_type` attribute
        of this class is ``ORACLE_OBJECT_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param artifact_source_type:
            The value to assign to the artifact_source_type property of this ArtifactExportDetailsObjectStorage.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE"
        :type artifact_source_type: str

        :param namespace:
            The value to assign to the namespace property of this ArtifactExportDetailsObjectStorage.
        :type namespace: str

        :param source_bucket:
            The value to assign to the source_bucket property of this ArtifactExportDetailsObjectStorage.
        :type source_bucket: str

        :param source_object_name:
            The value to assign to the source_object_name property of this ArtifactExportDetailsObjectStorage.
        :type source_object_name: str

        :param source_region:
            The value to assign to the source_region property of this ArtifactExportDetailsObjectStorage.
        :type source_region: str

        """
        self.swagger_types = {
            'artifact_source_type': 'str',
            'namespace': 'str',
            'source_bucket': 'str',
            'source_object_name': 'str',
            'source_region': 'str'
        }

        self.attribute_map = {
            'artifact_source_type': 'artifactSourceType',
            'namespace': 'namespace',
            'source_bucket': 'sourceBucket',
            'source_object_name': 'sourceObjectName',
            'source_region': 'sourceRegion'
        }

        self._artifact_source_type = None
        self._namespace = None
        self._source_bucket = None
        self._source_object_name = None
        self._source_region = None
        self._artifact_source_type = 'ORACLE_OBJECT_STORAGE'

    @property
    def namespace(self):
        """
        Gets the namespace of this ArtifactExportDetailsObjectStorage.
        The Object Storage namespace used for the request.


        :return: The namespace of this ArtifactExportDetailsObjectStorage.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ArtifactExportDetailsObjectStorage.
        The Object Storage namespace used for the request.


        :param namespace: The namespace of this ArtifactExportDetailsObjectStorage.
        :type: str
        """
        self._namespace = namespace

    @property
    def source_bucket(self):
        """
        Gets the source_bucket of this ArtifactExportDetailsObjectStorage.
        The name of the bucket. Avoid entering confidential information.


        :return: The source_bucket of this ArtifactExportDetailsObjectStorage.
        :rtype: str
        """
        return self._source_bucket

    @source_bucket.setter
    def source_bucket(self, source_bucket):
        """
        Sets the source_bucket of this ArtifactExportDetailsObjectStorage.
        The name of the bucket. Avoid entering confidential information.


        :param source_bucket: The source_bucket of this ArtifactExportDetailsObjectStorage.
        :type: str
        """
        self._source_bucket = source_bucket

    @property
    def source_object_name(self):
        """
        Gets the source_object_name of this ArtifactExportDetailsObjectStorage.
        The name of the object resulting from the copy operation.


        :return: The source_object_name of this ArtifactExportDetailsObjectStorage.
        :rtype: str
        """
        return self._source_object_name

    @source_object_name.setter
    def source_object_name(self, source_object_name):
        """
        Sets the source_object_name of this ArtifactExportDetailsObjectStorage.
        The name of the object resulting from the copy operation.


        :param source_object_name: The source_object_name of this ArtifactExportDetailsObjectStorage.
        :type: str
        """
        self._source_object_name = source_object_name

    @property
    def source_region(self):
        """
        Gets the source_region of this ArtifactExportDetailsObjectStorage.
        Region in which OSS bucket is present


        :return: The source_region of this ArtifactExportDetailsObjectStorage.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        """
        Sets the source_region of this ArtifactExportDetailsObjectStorage.
        Region in which OSS bucket is present


        :param source_region: The source_region of this ArtifactExportDetailsObjectStorage.
        :type: str
        """
        self._source_region = source_region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
