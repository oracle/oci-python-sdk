# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportSourceDetails(SourceDetails):
    """
    / Basic details about the source, import manifest and object storage bucket as well as object name of the archive that should be used during import
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.ImportSourceDetails.type` attribute
        of this class is ``IMPORT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ImportSourceDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE", "OCC", "OCIC_IDCS", "IMPORT"
        :type type: str

        :param manifest:
            The value to assign to the manifest property of this ImportSourceDetails.
        :type manifest: oci.application_migration.models.ImportManifest

        :param namespace:
            The value to assign to the namespace property of this ImportSourceDetails.
        :type namespace: str

        :param bucket:
            The value to assign to the bucket property of this ImportSourceDetails.
        :type bucket: str

        :param object_name:
            The value to assign to the object_name property of this ImportSourceDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'manifest': 'ImportManifest',
            'namespace': 'str',
            'bucket': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'manifest': 'manifest',
            'namespace': 'namespace',
            'bucket': 'bucket',
            'object_name': 'objectName'
        }

        self._type = None
        self._manifest = None
        self._namespace = None
        self._bucket = None
        self._object_name = None
        self._type = 'IMPORT'

    @property
    def manifest(self):
        """
        **[Required]** Gets the manifest of this ImportSourceDetails.

        :return: The manifest of this ImportSourceDetails.
        :rtype: oci.application_migration.models.ImportManifest
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this ImportSourceDetails.

        :param manifest: The manifest of this ImportSourceDetails.
        :type: oci.application_migration.models.ImportManifest
        """
        self._manifest = manifest

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this ImportSourceDetails.
        the object storage namespace where the bucket and uploaded object resides


        :return: The namespace of this ImportSourceDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this ImportSourceDetails.
        the object storage namespace where the bucket and uploaded object resides


        :param namespace: The namespace of this ImportSourceDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        **[Required]** Gets the bucket of this ImportSourceDetails.
        the bucket wherein the export archive exists in object storage


        :return: The bucket of this ImportSourceDetails.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this ImportSourceDetails.
        the bucket wherein the export archive exists in object storage


        :param bucket: The bucket of this ImportSourceDetails.
        :type: str
        """
        self._bucket = bucket

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this ImportSourceDetails.
        the name of the archive as it exists in object storage


        :return: The object_name of this ImportSourceDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ImportSourceDetails.
        the name of the archive as it exists in object storage


        :param object_name: The object_name of this ImportSourceDetails.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
