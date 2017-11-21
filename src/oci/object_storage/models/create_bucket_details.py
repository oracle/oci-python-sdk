# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBucketDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBucketDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateBucketDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBucketDetails.
        :type compartment_id: str

        :param metadata:
            The value to assign to the metadata property of this CreateBucketDetails.
        :type metadata: dict(str, str)

        :param public_access_type:
            The value to assign to the public_access_type property of this CreateBucketDetails.
            Allowed values for this property are: "NoPublicAccess", "ObjectRead"
        :type public_access_type: str

        :param storage_tier:
            The value to assign to the storage_tier property of this CreateBucketDetails.
            Allowed values for this property are: "Standard", "Archive"
        :type storage_tier: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'metadata': 'dict(str, str)',
            'public_access_type': 'str',
            'storage_tier': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'metadata': 'metadata',
            'public_access_type': 'publicAccessType',
            'storage_tier': 'storageTier'
        }

        self._name = None
        self._compartment_id = None
        self._metadata = None
        self._public_access_type = None
        self._storage_tier = None

    @property
    def name(self):
        """
        Gets the name of this CreateBucketDetails.
        The name of the bucket. Valid characters are uppercase or lowercase letters,
        numbers, and dashes. Bucket names must be unique within the namespace. Avoid entering confidential information.
        example: Example: my-new-bucket1


        :return: The name of this CreateBucketDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateBucketDetails.
        The name of the bucket. Valid characters are uppercase or lowercase letters,
        numbers, and dashes. Bucket names must be unique within the namespace. Avoid entering confidential information.
        example: Example: my-new-bucket1


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
        The type of public access enabled on this bucket.
        A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
        bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
        `GetObject`, `HeadObject`, and `ListObjects` operations.

        Allowed values for this property are: "NoPublicAccess", "ObjectRead"


        :return: The public_access_type of this CreateBucketDetails.
        :rtype: str
        """
        return self._public_access_type

    @public_access_type.setter
    def public_access_type(self, public_access_type):
        """
        Sets the public_access_type of this CreateBucketDetails.
        The type of public access enabled on this bucket.
        A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
        bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
        `GetObject`, `HeadObject`, and `ListObjects` operations.


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

    @property
    def storage_tier(self):
        """
        Gets the storage_tier of this CreateBucketDetails.
        The type of storage tier of this bucket.
        A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier.
        When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier'
        property is immutable after bucket is created.

        Allowed values for this property are: "Standard", "Archive"


        :return: The storage_tier of this CreateBucketDetails.
        :rtype: str
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """
        Sets the storage_tier of this CreateBucketDetails.
        The type of storage tier of this bucket.
        A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier.
        When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier'
        property is immutable after bucket is created.


        :param storage_tier: The storage_tier of this CreateBucketDetails.
        :type: str
        """
        allowed_values = ["Standard", "Archive"]
        if storage_tier not in allowed_values:
            raise ValueError(
                "Invalid value for `storage_tier`, must be one of {0}"
                .format(allowed_values)
            )
        self._storage_tier = storage_tier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
