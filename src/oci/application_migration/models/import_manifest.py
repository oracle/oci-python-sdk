# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportManifest(object):
    """
    Manifest describing details about an import source
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportManifest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this ImportManifest.
        :type version: str

        :param export_type:
            The value to assign to the export_type property of this ImportManifest.
        :type export_type: str

        :param export_details:
            The value to assign to the export_details property of this ImportManifest.
        :type export_details: object

        :param timestamp:
            The value to assign to the timestamp property of this ImportManifest.
        :type timestamp: datetime

        :param md5:
            The value to assign to the md5 property of this ImportManifest.
        :type md5: str

        :param signature:
            The value to assign to the signature property of this ImportManifest.
        :type signature: str

        """
        self.swagger_types = {
            'version': 'str',
            'export_type': 'str',
            'export_details': 'object',
            'timestamp': 'datetime',
            'md5': 'str',
            'signature': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'export_type': 'exportType',
            'export_details': 'exportDetails',
            'timestamp': 'timestamp',
            'md5': 'md5',
            'signature': 'signature'
        }

        self._version = None
        self._export_type = None
        self._export_details = None
        self._timestamp = None
        self._md5 = None
        self._signature = None

    @property
    def version(self):
        """
        Gets the version of this ImportManifest.
        the version of the export tool that was used to generate the manifest


        :return: The version of this ImportManifest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ImportManifest.
        the version of the export tool that was used to generate the manifest


        :param version: The version of this ImportManifest.
        :type: str
        """
        self._version = version

    @property
    def export_type(self):
        """
        Gets the export_type of this ImportManifest.
        the type of application that the export tool was executed against to generate this manifest


        :return: The export_type of this ImportManifest.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """
        Sets the export_type of this ImportManifest.
        the type of application that the export tool was executed against to generate this manifest


        :param export_type: The export_type of this ImportManifest.
        :type: str
        """
        self._export_type = export_type

    @property
    def export_details(self):
        """
        Gets the export_details of this ImportManifest.
        application specific details as parsed from various sources of the application that was exported


        :return: The export_details of this ImportManifest.
        :rtype: object
        """
        return self._export_details

    @export_details.setter
    def export_details(self, export_details):
        """
        Sets the export_details of this ImportManifest.
        application specific details as parsed from various sources of the application that was exported


        :param export_details: The export_details of this ImportManifest.
        :type: object
        """
        self._export_details = export_details

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ImportManifest.
        when this manifest was generated


        :return: The timestamp of this ImportManifest.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ImportManifest.
        when this manifest was generated


        :param timestamp: The timestamp of this ImportManifest.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def md5(self):
        """
        Gets the md5 of this ImportManifest.
        the MD5 hash of the export artifact archive that was produced by the export tool and should be used with this manifest


        :return: The md5 of this ImportManifest.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this ImportManifest.
        the MD5 hash of the export artifact archive that was produced by the export tool and should be used with this manifest


        :param md5: The md5 of this ImportManifest.
        :type: str
        """
        self._md5 = md5

    @property
    def signature(self):
        """
        Gets the signature of this ImportManifest.
        a sha1 hash of all the fields of this manifest (excluding the signature)


        :return: The signature of this ImportManifest.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this ImportManifest.
        a sha1 hash of all the fields of this manifest (excluding the signature)


        :param signature: The signature of this ImportManifest.
        :type: str
        """
        self._signature = signature

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
