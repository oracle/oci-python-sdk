# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateBucketDetails(object):

    def __init__(self):

        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'metadata': 'dict(str, str)',
            'public_access_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'metadata': 'metadata',
            'public_access_type': 'publicAccessType'
        }

        self._name = None
        self._compartment_id = None
        self._metadata = None
        self._public_access_type = None

    @property
    def name(self):
        """
        Gets the name of this CreateBucketDetails.
        The name of the bucket. Valid characters are uppercase or lowercase letters,
        numbers, and dashes. Bucket names must be unique within the namespace.


        :return: The name of this CreateBucketDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateBucketDetails.
        The name of the bucket. Valid characters are uppercase or lowercase letters,
        numbers, and dashes. Bucket names must be unique within the namespace.


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
        Arbitrary string, up to 4KB, of keys and values for user-defined metadata.


        :return: The metadata of this CreateBucketDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateBucketDetails.
        Arbitrary string, up to 4KB, of keys and values for user-defined metadata.


        :param metadata: The metadata of this CreateBucketDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def public_access_type(self):
        """
        Gets the public_access_type of this CreateBucketDetails.
        The type of public access available on this bucket. Allows authenticated caller to access the bucket or
        contents of this bucket. By default a bucket is set to NoPublicAccess. It is treated as NoPublicAccess
        when this value is not specified. When the type is NoPublicAccess the bucket does not allow any public access.
        When the type is ObjectRead the bucket allows public access to the GetObject, HeadObject, ListObjects.

        Allowed values for this property are: "NoPublicAccess", "ObjectRead"


        :return: The public_access_type of this CreateBucketDetails.
        :rtype: str
        """
        return self._public_access_type

    @public_access_type.setter
    def public_access_type(self, public_access_type):
        """
        Sets the public_access_type of this CreateBucketDetails.
        The type of public access available on this bucket. Allows authenticated caller to access the bucket or
        contents of this bucket. By default a bucket is set to NoPublicAccess. It is treated as NoPublicAccess
        when this value is not specified. When the type is NoPublicAccess the bucket does not allow any public access.
        When the type is ObjectRead the bucket allows public access to the GetObject, HeadObject, ListObjects.


        :param public_access_type: The public_access_type of this CreateBucketDetails.
        :type: str
        """
        allowed_values = ["NoPublicAccess", "ObjectRead"]
        if public_access_type not in allowed_values:
            raise ValueError(
                "Invalid value for `public_access_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._public_access_type = public_access_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
