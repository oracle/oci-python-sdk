# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class CreateBucketDetails(object):

    def __init__(self):

        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'metadata': 'metadata'
        }

        self._name = None
        self._compartment_id = None
        self._metadata = None

    @property
    def name(self):
        """
        Gets the name of this CreateBucketDetails.
        The name of the bucket. Valid characters are letters (upper or lower case),
        numbers and dashes. Bucket names must be unique within the namespace.

        :return: The name of this CreateBucketDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateBucketDetails.
        The name of the bucket. Valid characters are letters (upper or lower case),
        numbers and dashes. Bucket names must be unique within the namespace.

        :param name: The name of this CreateBucketDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateBucketDetails.
        The ID of the compartment in which to create the bucket.

        :return: The compartment_id of this CreateBucketDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBucketDetails.
        The ID of the compartment in which to create the bucket.

        :param compartment_id: The compartment_id of this CreateBucketDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateBucketDetails.
        Arbitrary string keys and values for user-defined metadata.

        :return: The metadata of this CreateBucketDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateBucketDetails.
        Arbitrary string keys and values for user-defined metadata.

        :param metadata: The metadata of this CreateBucketDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
