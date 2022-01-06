# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateRevocationListDetails(object):
    """
    The details of the certificate revocation list (CRL).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateRevocationListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_storage_config:
            The value to assign to the object_storage_config property of this CertificateRevocationListDetails.
        :type object_storage_config: oci.certificates_management.models.ObjectStorageBucketConfigDetails

        :param custom_formatted_urls:
            The value to assign to the custom_formatted_urls property of this CertificateRevocationListDetails.
        :type custom_formatted_urls: list[str]

        """
        self.swagger_types = {
            'object_storage_config': 'ObjectStorageBucketConfigDetails',
            'custom_formatted_urls': 'list[str]'
        }

        self.attribute_map = {
            'object_storage_config': 'objectStorageConfig',
            'custom_formatted_urls': 'customFormattedUrls'
        }

        self._object_storage_config = None
        self._custom_formatted_urls = None

    @property
    def object_storage_config(self):
        """
        **[Required]** Gets the object_storage_config of this CertificateRevocationListDetails.

        :return: The object_storage_config of this CertificateRevocationListDetails.
        :rtype: oci.certificates_management.models.ObjectStorageBucketConfigDetails
        """
        return self._object_storage_config

    @object_storage_config.setter
    def object_storage_config(self, object_storage_config):
        """
        Sets the object_storage_config of this CertificateRevocationListDetails.

        :param object_storage_config: The object_storage_config of this CertificateRevocationListDetails.
        :type: oci.certificates_management.models.ObjectStorageBucketConfigDetails
        """
        self._object_storage_config = object_storage_config

    @property
    def custom_formatted_urls(self):
        """
        Gets the custom_formatted_urls of this CertificateRevocationListDetails.
        Optional CRL access points, expressed using a format where the version number of the issuing CA is inserted wherever you include a pair of curly braces. This versioning scheme helps avoid collisions when new CA versions are created. For example, myCrlFileIssuedFromCAVersion{}.crl becomes myCrlFileIssuedFromCAVersion2.crl for CA version 2.


        :return: The custom_formatted_urls of this CertificateRevocationListDetails.
        :rtype: list[str]
        """
        return self._custom_formatted_urls

    @custom_formatted_urls.setter
    def custom_formatted_urls(self, custom_formatted_urls):
        """
        Sets the custom_formatted_urls of this CertificateRevocationListDetails.
        Optional CRL access points, expressed using a format where the version number of the issuing CA is inserted wherever you include a pair of curly braces. This versioning scheme helps avoid collisions when new CA versions are created. For example, myCrlFileIssuedFromCAVersion{}.crl becomes myCrlFileIssuedFromCAVersion2.crl for CA version 2.


        :param custom_formatted_urls: The custom_formatted_urls of this CertificateRevocationListDetails.
        :type: list[str]
        """
        self._custom_formatted_urls = custom_formatted_urls

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
