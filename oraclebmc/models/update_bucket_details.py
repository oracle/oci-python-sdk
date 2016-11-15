# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class UpdateBucketDetails(object):

    def __init__(self):

        self.swagger_types = {
            'namespace': 'str',
            'name': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'name': 'name',
            'metadata': 'metadata'
        }

        self._namespace = None
        self._name = None
        self._metadata = None

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdateBucketDetails.
        The namespace in which the bucket lives.

        :return: The namespace of this UpdateBucketDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdateBucketDetails.
        The namespace in which the bucket lives.

        :param namespace: The namespace of this UpdateBucketDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def name(self):
        """
        Gets the name of this UpdateBucketDetails.
        The name of the bucket.

        :return: The name of this UpdateBucketDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateBucketDetails.
        The name of the bucket.

        :param name: The name of this UpdateBucketDetails.
        :type: str
        """
        self._name = name

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateBucketDetails.
        Arbitrary string keys and values for the user-defined metadata.

        :return: The metadata of this UpdateBucketDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateBucketDetails.
        Arbitrary string keys and values for the user-defined metadata.

        :param metadata: The metadata of this UpdateBucketDetails.
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
