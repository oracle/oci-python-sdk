# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .export_image_details import ExportImageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportImageViaObjectStorageUriDetails(ExportImageDetails):
    """
    ExportImageViaObjectStorageUriDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportImageViaObjectStorageUriDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.ExportImageViaObjectStorageUriDetails.destination_type` attribute
        of this class is ``objectStorageUri`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_type:
            The value to assign to the destination_type property of this ExportImageViaObjectStorageUriDetails.
        :type destination_type: str

        :param destination_uri:
            The value to assign to the destination_uri property of this ExportImageViaObjectStorageUriDetails.
        :type destination_uri: str

        """
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
        **[Required]** Gets the destination_uri of this ExportImageViaObjectStorageUriDetails.
        The Object Storage URL to export the image to. See `Object Storage URLs`__
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
        The Object Storage URL to export the image to. See `Object Storage URLs`__
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
