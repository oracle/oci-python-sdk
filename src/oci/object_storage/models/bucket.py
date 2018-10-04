# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Bucket(object):
    """
    A bucket is a container for storing objects in a compartment within a namespace. A bucket is associated with a single compartment.
    The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket. For more
    information, see `Managing Buckets`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Object/Tasks/managingbuckets.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the public_access_type property of a Bucket.
    #: This constant has a value of "NoPublicAccess"
    PUBLIC_ACCESS_TYPE_NO_PUBLIC_ACCESS = "NoPublicAccess"

    #: A constant which can be used with the public_access_type property of a Bucket.
    #: This constant has a value of "ObjectRead"
    PUBLIC_ACCESS_TYPE_OBJECT_READ = "ObjectRead"

    #: A constant which can be used with the public_access_type property of a Bucket.
    #: This constant has a value of "ObjectReadWithoutList"
    PUBLIC_ACCESS_TYPE_OBJECT_READ_WITHOUT_LIST = "ObjectReadWithoutList"

    #: A constant which can be used with the storage_tier property of a Bucket.
    #: This constant has a value of "Standard"
    STORAGE_TIER_STANDARD = "Standard"

    #: A constant which can be used with the storage_tier property of a Bucket.
    #: This constant has a value of "Archive"
    STORAGE_TIER_ARCHIVE = "Archive"

    def __init__(self, **kwargs):
        """
        Initializes a new Bucket object with values from keyword arguments.
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
            Allowed values for this property are: "NoPublicAccess", "ObjectRead", "ObjectReadWithoutList", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type public_access_type: str

        :param storage_tier:
            The value to assign to the storage_tier property of this Bucket.
            Allowed values for this property are: "Standard", "Archive", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type storage_tier: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Bucket.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Bucket.
        :type defined_tags: dict(str, dict(str, object))

        :param kms_key_id:
            The value to assign to the kms_key_id property of this Bucket.
        :type kms_key_id: str

        :param object_lifecycle_policy_etag:
            The value to assign to the object_lifecycle_policy_etag property of this Bucket.
        :type object_lifecycle_policy_etag: str

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
            'storage_tier': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'kms_key_id': 'str',
            'object_lifecycle_policy_etag': 'str'
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
            'storage_tier': 'storageTier',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'kms_key_id': 'kmsKeyId',
            'object_lifecycle_policy_etag': 'objectLifecyclePolicyEtag'
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
        self._freeform_tags = None
        self._defined_tags = None
        self._kms_key_id = None
        self._object_lifecycle_policy_etag = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this Bucket.
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
        **[Required]** Gets the name of this Bucket.
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
        **[Required]** Gets the compartment_id of this Bucket.
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
        **[Required]** Gets the metadata of this Bucket.
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
        **[Required]** Gets the created_by of this Bucket.
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
        **[Required]** Gets the time_created of this Bucket.
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
        **[Required]** Gets the etag of this Bucket.
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
        `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the
        bucket, public access is allowed for the `GetObject` and `HeadObject` operations.

        Allowed values for this property are: "NoPublicAccess", "ObjectRead", "ObjectReadWithoutList", 'UNKNOWN_ENUM_VALUE'.
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
        `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the
        bucket, public access is allowed for the `GetObject` and `HeadObject` operations.


        :param public_access_type: The public_access_type of this Bucket.
        :type: str
        """
        allowed_values = ["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]
        if not value_allowed_none_or_none_sentinel(public_access_type, allowed_values):
            public_access_type = 'UNKNOWN_ENUM_VALUE'
        self._public_access_type = public_access_type

    @property
    def storage_tier(self):
        """
        Gets the storage_tier of this Bucket.
        The type of storage tier of this bucket.
        A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier.
        When 'Archive' tier type is set explicitly, the bucket is put in the archive storage tier. The 'storageTier'
        property is immutable after bucket is created.

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
        When 'Archive' tier type is set explicitly, the bucket is put in the archive storage tier. The 'storageTier'
        property is immutable after bucket is created.


        :param storage_tier: The storage_tier of this Bucket.
        :type: str
        """
        allowed_values = ["Standard", "Archive"]
        if not value_allowed_none_or_none_sentinel(storage_tier, allowed_values):
            storage_tier = 'UNKNOWN_ENUM_VALUE'
        self._storage_tier = storage_tier

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Bucket.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Bucket.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Bucket.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Bucket.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Bucket.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Bucket.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Bucket.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Bucket.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this Bucket.
        The OCID of a KMS key id used to call KMS to generate data key, decrypt the encrypted data key


        :return: The kms_key_id of this Bucket.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this Bucket.
        The OCID of a KMS key id used to call KMS to generate data key, decrypt the encrypted data key


        :param kms_key_id: The kms_key_id of this Bucket.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def object_lifecycle_policy_etag(self):
        """
        Gets the object_lifecycle_policy_etag of this Bucket.
        The entity tag for the live object lifecycle policy on the bucket.


        :return: The object_lifecycle_policy_etag of this Bucket.
        :rtype: str
        """
        return self._object_lifecycle_policy_etag

    @object_lifecycle_policy_etag.setter
    def object_lifecycle_policy_etag(self, object_lifecycle_policy_etag):
        """
        Sets the object_lifecycle_policy_etag of this Bucket.
        The entity tag for the live object lifecycle policy on the bucket.


        :param object_lifecycle_policy_etag: The object_lifecycle_policy_etag of this Bucket.
        :type: str
        """
        self._object_lifecycle_policy_etag = object_lifecycle_policy_etag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
