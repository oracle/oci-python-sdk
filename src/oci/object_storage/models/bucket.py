# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Bucket(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Bucket object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this Bucket.
        :type namespace: str

        :param name:
            The value to assign to the name property of this Bucket.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Bucket.
        :type compartment_id: str

        :param metadata:
            The value to assign to the metadata property of this Bucket.
        :type metadata: dict(str, str)

        :param created_by:
            The value to assign to the created_by property of this Bucket.
        :type created_by: str

        :param time_created:
            The value to assign to the time_created property of this Bucket.
        :type time_created: datetime

        :param etag:
            The value to assign to the etag property of this Bucket.
        :type etag: str

        :param public_access_type:
            The value to assign to the public_access_type property of this Bucket.
            Allowed values for this property are: "NoPublicAccess", "ObjectRead", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type public_access_type: str

        :param storage_tier:
            The value to assign to the storage_tier property of this Bucket.
            Allowed values for this property are: "Standard", "Archive", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type storage_tier: str

        """
        self.swagger_types = {
            'namespace': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'metadata': 'dict(str, str)',
            'created_by': 'str',
            'time_created': 'datetime',
            'etag': 'str',
            'public_access_type': 'str',
            'storage_tier': 'str'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'metadata': 'metadata',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'etag': 'etag',
            'public_access_type': 'publicAccessType',
            'storage_tier': 'storageTier'
        }

        self._namespace = None
        self._name = None
        self._compartment_id = None
        self._metadata = None
        self._created_by = None
        self._time_created = None
        self._etag = None
        self._public_access_type = None
        self._storage_tier = None

    @property
    def namespace(self):
        """
        Gets the namespace of this Bucket.
        The namespace in which the bucket lives.


        :return: The namespace of this Bucket.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this Bucket.
        The namespace in which the bucket lives.


        :param namespace: The namespace of this Bucket.
        :type: str
        """
        self._namespace = namespace

    @property
    def name(self):
        """
        Gets the name of this Bucket.
        The name of the bucket. Avoid entering confidential information.
        Example: my-new-bucket1


        :return: The name of this Bucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Bucket.
        The name of the bucket. Avoid entering confidential information.
        Example: my-new-bucket1


        :param name: The name of this Bucket.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Bucket.
        The compartment ID in which the bucket is authorized.


        :return: The compartment_id of this Bucket.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Bucket.
        The compartment ID in which the bucket is authorized.


        :param compartment_id: The compartment_id of this Bucket.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metadata(self):
        """
        Gets the metadata of this Bucket.
        Arbitrary string keys and values for user-defined metadata.


        :return: The metadata of this Bucket.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Bucket.
        Arbitrary string keys and values for user-defined metadata.


        :param metadata: The metadata of this Bucket.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def created_by(self):
        """
        Gets the created_by of this Bucket.
        The OCID of the user who created the bucket.


        :return: The created_by of this Bucket.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Bucket.
        The OCID of the user who created the bucket.


        :param created_by: The created_by of this Bucket.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        Gets the time_created of this Bucket.
        The date and time the bucket was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :return: The time_created of this Bucket.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Bucket.
        The date and time the bucket was created, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :param time_created: The time_created of this Bucket.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def etag(self):
        """
        Gets the etag of this Bucket.
        The entity tag for the bucket.


        :return: The etag of this Bucket.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this Bucket.
        The entity tag for the bucket.


        :param etag: The etag of this Bucket.
        :type: str
        """
        self._etag = etag

    @property
    def public_access_type(self):
        """
        Gets the public_access_type of this Bucket.
        The type of public access enabled on this bucket.
        A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
        bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
        `GetObject`, `HeadObject`, and `ListObjects` operations.

        Allowed values for this property are: "NoPublicAccess", "ObjectRead", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The public_access_type of this Bucket.
        :rtype: str
        """
        return self._public_access_type

    @public_access_type.setter
    def public_access_type(self, public_access_type):
        """
        Sets the public_access_type of this Bucket.
        The type of public access enabled on this bucket.
        A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the
        bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the
        `GetObject`, `HeadObject`, and `ListObjects` operations.


        :param public_access_type: The public_access_type of this Bucket.
        :type: str
        """
        allowed_values = ["NoPublicAccess", "ObjectRead"]
        if public_access_type not in allowed_values:
            public_access_type = 'UNKNOWN_ENUM_VALUE'
        self._public_access_type = public_access_type

    @property
    def storage_tier(self):
        """
        Gets the storage_tier of this Bucket.
        The type of storage tier of this bucket.
        A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier.
        When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier'
        property is immutable once the bucket is created.

        Allowed values for this property are: "Standard", "Archive", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The storage_tier of this Bucket.
        :rtype: str
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """
        Sets the storage_tier of this Bucket.
        The type of storage tier of this bucket.
        A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier.
        When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier'
        property is immutable once the bucket is created.


        :param storage_tier: The storage_tier of this Bucket.
        :type: str
        """
        allowed_values = ["Standard", "Archive"]
        if storage_tier not in allowed_values:
            storage_tier = 'UNKNOWN_ENUM_VALUE'
        self._storage_tier = storage_tier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
