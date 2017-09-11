# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .export_image_details import ExportImageDetails
from ...util import formatted_flat_dict


class ExportImageViaObjectStorageUriDetails(ExportImageDetails):

    def __init__(self):

        self.swagger_types = {
            'destination_type': 'str',
            'destination_uri': 'str'
        }

        self.attribute_map = {
            'destination_type': 'destinationType',
            'destination_uri': 'destinationUri'
        }

        self._destination_type = None
        self._destination_uri = None
        self._destination_type = 'objectStorageUri'

    @property
    def destination_uri(self):
        """
        Gets the destination_uri of this ExportImageViaObjectStorageUriDetails.
        The Object Storage Service URL to export the image to. See `Object Storage URLs`__
        and `pre-authenticated requests`__ for constructing URLs for image import/export.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth


        :return: The destination_uri of this ExportImageViaObjectStorageUriDetails.
        :rtype: str
        """
        return self._destination_uri

    @destination_uri.setter
    def destination_uri(self, destination_uri):
        """
        Sets the destination_uri of this ExportImageViaObjectStorageUriDetails.
        The Object Storage Service URL to export the image to. See `Object Storage URLs`__
        and `pre-authenticated requests`__ for constructing URLs for image import/export.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/imageimportexport.htm#URLs
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingaccess.htm#pre-auth


        :param destination_uri: The destination_uri of this ExportImageViaObjectStorageUriDetails.
        :type: str
        """
        self._destination_uri = destination_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
