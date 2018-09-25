# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBucketDetails(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the public_access_type property of a CreateBucketDetails.
    #: This constant has a value of "NoPublicAccess"
    PUBLIC_ACCESS_TYPE_NO_PUBLIC_ACCESS = "NoPublicAccess"

    #: A constant which can be used with the public_access_type property of a CreateBucketDetails.
    #: This constant has a value of "ObjectRead"
    PUBLIC_ACCESS_TYPE_OBJECT_READ = "ObjectRead"

    #: A constant which can be used with the public_access_type property of a CreateBucketDetails.
    #: This constant has a value of "ObjectReadWithoutList"
    PUBLIC_ACCESS_TYPE_OBJECT_READ_WITHOUT_LIST = "ObjectReadWithoutList"

    #: A constant which can be used with the storage_tier property of a CreateBucketDetails.
    #: This constant has a value of "Standard"
    STORAGE_TIER_STANDARD = "Standard"

    #: A constant which can be used with the storage_tier property of a CreateBucketDetails.
    #: This constant has a value of "Archive"
    STORAGE_TIER_ARCHIVE = "Archive"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBucketDetails object with values from keyword arguments.
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
            Allowed values for this property are: "NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"
        :type public_access_type: str

        :param storage_tier:
            The value to assign to the storage_tier property of this CreateBucketDetails.
            Allowed values for this property are: "Standard", "Archive"
        :type storage_tier: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBucketDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBucketDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateBucketDetails.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'metadata': 'dict(str, str)',
            'public_access_type': 'str',
            'storage_tier': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'metadata': 'metadata',
            'public_access_type': 'publicAccessType',
            'storage_tier': 'storageTier',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'kms_key_id': 'kmsKeyId'
        }

        self._name = None
        self._compartment_id = None
        self._metadata = None
        self._public_access_type = None
        self._storage_tier = None
        self._freeform_tags = None
        self._defined_tags = None
        self._kms_key_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateBucketDetails.
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
        **[Required]** Gets the compartment_id of this CreateBucketDetails.
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
        `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket,
        public access is allowed for the `GetObject` and `HeadObject` operations.

        Allowed values for this property are: "NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"


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
        `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket,
        public access is allowed for the `GetObject` and `HeadObject` operations.


        :param public_access_type: The public_access_type of this CreateBucketDetails.
        :type: str
        """
        allowed_values = ["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]
        if not value_allowed_none_or_none_sentinel(public_access_type, allowed_values):
            raise ValueError(
                "Invalid value for `public_access_type`, must be None or one of {0}"
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
        if not value_allowed_none_or_none_sentinel(storage_tier, allowed_values):
            raise ValueError(
                "Invalid value for `storage_tier`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._storage_tier = storage_tier

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBucketDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateBucketDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBucketDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateBucketDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBucketDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateBucketDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBucketDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateBucketDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateBucketDetails.
        The OCID of a KMS key id used to call KMS to generate data key, decrypt the encrypted data key


        :return: The kms_key_id of this CreateBucketDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateBucketDetails.
        The OCID of a KMS key id used to call KMS to generate data key, decrypt the encrypted data key


        :param kms_key_id: The kms_key_id of this CreateBucketDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
