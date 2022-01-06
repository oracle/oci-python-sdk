# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReencryptObjectDetails(object):
    """
    The details used to re-encrypt the data encryption keys associated with an object.
    You can only specify either a kmsKeyId or an sseCustomerKey in the request payload, not both.
    If the request payload is empty, the object is encrypted using the encryption key assigned to the
    bucket. The bucket encryption mechanism can either be a master encryption key managed by Oracle or the Vault service.

    - The sseCustomerKey field specifies the customer-provided encryption key (SSE-C) that will be used to re-encrypt the data encryption keys of the
    object and its chunks.

    - The sourceSSECustomerKey field specifies information about the customer-provided encryption key that is currently
    associated with the object source. Specify a value for the sourceSSECustomerKey only if the object
    is encrypted with a customer-provided encryption key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReencryptObjectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this ReencryptObjectDetails.
        :type kms_key_id: str

        :param sse_customer_key:
            The value to assign to the sse_customer_key property of this ReencryptObjectDetails.
        :type sse_customer_key: oci.object_storage.models.SSECustomerKeyDetails

        :param source_sse_customer_key:
            The value to assign to the source_sse_customer_key property of this ReencryptObjectDetails.
        :type source_sse_customer_key: oci.object_storage.models.SSECustomerKeyDetails

        """
        self.swagger_types = {
            'kms_key_id': 'str',
            'sse_customer_key': 'SSECustomerKeyDetails',
            'source_sse_customer_key': 'SSECustomerKeyDetails'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId',
            'sse_customer_key': 'sseCustomerKey',
            'source_sse_customer_key': 'sourceSseCustomerKey'
        }

        self._kms_key_id = None
        self._sse_customer_key = None
        self._source_sse_customer_key = None

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this ReencryptObjectDetails.
        The `OCID`__ of the master encryption key used to call the Vault
        service to re-encrypt the data encryption keys associated with the object and its chunks. If the kmsKeyId value is
        empty, whether null or an empty string, the API will perform re-encryption by using the kmsKeyId associated with the
        bucket or the master encryption key managed by Oracle, depending on the bucket encryption mechanism.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this ReencryptObjectDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this ReencryptObjectDetails.
        The `OCID`__ of the master encryption key used to call the Vault
        service to re-encrypt the data encryption keys associated with the object and its chunks. If the kmsKeyId value is
        empty, whether null or an empty string, the API will perform re-encryption by using the kmsKeyId associated with the
        bucket or the master encryption key managed by Oracle, depending on the bucket encryption mechanism.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this ReencryptObjectDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def sse_customer_key(self):
        """
        Gets the sse_customer_key of this ReencryptObjectDetails.

        :return: The sse_customer_key of this ReencryptObjectDetails.
        :rtype: oci.object_storage.models.SSECustomerKeyDetails
        """
        return self._sse_customer_key

    @sse_customer_key.setter
    def sse_customer_key(self, sse_customer_key):
        """
        Sets the sse_customer_key of this ReencryptObjectDetails.

        :param sse_customer_key: The sse_customer_key of this ReencryptObjectDetails.
        :type: oci.object_storage.models.SSECustomerKeyDetails
        """
        self._sse_customer_key = sse_customer_key

    @property
    def source_sse_customer_key(self):
        """
        Gets the source_sse_customer_key of this ReencryptObjectDetails.

        :return: The source_sse_customer_key of this ReencryptObjectDetails.
        :rtype: oci.object_storage.models.SSECustomerKeyDetails
        """
        return self._source_sse_customer_key

    @source_sse_customer_key.setter
    def source_sse_customer_key(self, source_sse_customer_key):
        """
        Sets the source_sse_customer_key of this ReencryptObjectDetails.

        :param source_sse_customer_key: The source_sse_customer_key of this ReencryptObjectDetails.
        :type: oci.object_storage.models.SSECustomerKeyDetails
        """
        self._source_sse_customer_key = source_sse_customer_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
