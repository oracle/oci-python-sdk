# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Bucket(object):
    """
    A bucket is a container for storing objects in a compartment within a namespace. A bucket is associated with a single compartment.
    The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket. For more
    information, see `Managing Buckets`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Object/Tasks/managingbuckets.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
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

    #: A constant which can be used with the versioning property of a Bucket.
    #: This constant has a value of "Enabled"
    VERSIONING_ENABLED = "Enabled"

    #: A constant which can be used with the versioning property of a Bucket.
    #: This constant has a value of "Suspended"
    VERSIONING_SUSPENDED = "Suspended"

    #: A constant which can be used with the versioning property of a Bucket.
    #: This constant has a value of "Disabled"
    VERSIONING_DISABLED = "Disabled"

    #: A constant which can be used with the auto_tiering property of a Bucket.
    #: This constant has a value of "Disabled"
    AUTO_TIERING_DISABLED = "Disabled"

    #: A constant which can be used with the auto_tiering property of a Bucket.
    #: This constant has a value of "InfrequentAccess"
    AUTO_TIERING_INFREQUENT_ACCESS = "InfrequentAccess"

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

        :param object_events_enabled:
            The value to assign to the object_events_enabled property of this Bucket.
        :type object_events_enabled: bool

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

        :param approximate_count:
            The value to assign to the approximate_count property of this Bucket.
        :type approximate_count: int

        :param approximate_size:
            The value to assign to the approximate_size property of this Bucket.
        :type approximate_size: int

        :param replication_enabled:
            The value to assign to the replication_enabled property of this Bucket.
        :type replication_enabled: bool

        :param is_read_only:
            The value to assign to the is_read_only property of this Bucket.
        :type is_read_only: bool

        :param id:
            The value to assign to the id property of this Bucket.
        :type id: str

        :param versioning:
            The value to assign to the versioning property of this Bucket.
            Allowed values for this property are: "Enabled", "Suspended", "Disabled", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type versioning: str

        :param auto_tiering:
            The value to assign to the auto_tiering property of this Bucket.
            Allowed values for this property are: "Disabled", "InfrequentAccess", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type auto_tiering: str

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
            'object_events_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'kms_key_id': 'str',
            'object_lifecycle_policy_etag': 'str',
            'approximate_count': 'int',
            'approximate_size': 'int',
            'replication_enabled': 'bool',
            'is_read_only': 'bool',
            'id': 'str',
            'versioning': 'str',
            'auto_tiering': 'str'
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
            'object_events_enabled': 'objectEventsEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'kms_key_id': 'kmsKeyId',
            'object_lifecycle_policy_etag': 'objectLifecyclePolicyEtag',
            'approximate_count': 'approximateCount',
            'approximate_size': 'approximateSize',
            'replication_enabled': 'replicationEnabled',
            'is_read_only': 'isReadOnly',
            'id': 'id',
            'versioning': 'versioning',
            'auto_tiering': 'autoTiering'
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
        self._object_events_enabled = None
        self._freeform_tags = None
        self._defined_tags = None
        self._kms_key_id = None
        self._object_lifecycle_policy_etag = None
        self._approximate_count = None
        self._approximate_size = None
        self._replication_enabled = None
        self._is_read_only = None
        self._id = None
        self._versioning = None
        self._auto_tiering = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this Bucket.
        The Object Storage namespace in which the bucket resides.


        :return: The namespace of this Bucket.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this Bucket.
        The Object Storage namespace in which the bucket resides.


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
        The `OCID`__ of the user who created the bucket.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The created_by of this Bucket.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Bucket.
        The `OCID`__ of the user who created the bucket.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this Bucket.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Bucket.
        The date and time the bucket was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :return: The time_created of this Bucket.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Bucket.
        The date and time the bucket was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :param time_created: The time_created of this Bucket.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this Bucket.
        The entity tag (ETag) for the bucket.


        :return: The etag of this Bucket.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this Bucket.
        The entity tag (ETag) for the bucket.


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
        The storage tier type assigned to the bucket. A bucket is set to `Standard` tier by default, which means
        objects uploaded or copied to the bucket will be in the standard storage tier. When the `Archive` tier type
        is set explicitly for a bucket, objects uploaded or copied to the bucket will be stored in archive storage.
        The `storageTier` property is immutable after bucket is created.

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
        The storage tier type assigned to the bucket. A bucket is set to `Standard` tier by default, which means
        objects uploaded or copied to the bucket will be in the standard storage tier. When the `Archive` tier type
        is set explicitly for a bucket, objects uploaded or copied to the bucket will be stored in archive storage.
        The `storageTier` property is immutable after bucket is created.


        :param storage_tier: The storage_tier of this Bucket.
        :type: str
        """
        allowed_values = ["Standard", "Archive"]
        if not value_allowed_none_or_none_sentinel(storage_tier, allowed_values):
            storage_tier = 'UNKNOWN_ENUM_VALUE'
        self._storage_tier = storage_tier

    @property
    def object_events_enabled(self):
        """
        Gets the object_events_enabled of this Bucket.
        Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is
        set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information
        about events, see `Overview of Events`__.

        __ https://docs.cloud.oracle.com/Content/Events/Concepts/eventsoverview.htm


        :return: The object_events_enabled of this Bucket.
        :rtype: bool
        """
        return self._object_events_enabled

    @object_events_enabled.setter
    def object_events_enabled(self, object_events_enabled):
        """
        Sets the object_events_enabled of this Bucket.
        Whether or not events are emitted for object state changes in this bucket. By default, `objectEventsEnabled` is
        set to `false`. Set `objectEventsEnabled` to `true` to emit events for object state changes. For more information
        about events, see `Overview of Events`__.

        __ https://docs.cloud.oracle.com/Content/Events/Concepts/eventsoverview.htm


        :param object_events_enabled: The object_events_enabled of this Bucket.
        :type: bool
        """
        self._object_events_enabled = object_events_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Bucket.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


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

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


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

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


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

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Bucket.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this Bucket.
        The `OCID`__ of a master encryption key used to call the Key Management
        service to generate a data encryption key or to encrypt or decrypt a data encryption key.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this Bucket.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this Bucket.
        The `OCID`__ of a master encryption key used to call the Key Management
        service to generate a data encryption key or to encrypt or decrypt a data encryption key.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this Bucket.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def object_lifecycle_policy_etag(self):
        """
        Gets the object_lifecycle_policy_etag of this Bucket.
        The entity tag (ETag) for the live object lifecycle policy on the bucket.


        :return: The object_lifecycle_policy_etag of this Bucket.
        :rtype: str
        """
        return self._object_lifecycle_policy_etag

    @object_lifecycle_policy_etag.setter
    def object_lifecycle_policy_etag(self, object_lifecycle_policy_etag):
        """
        Sets the object_lifecycle_policy_etag of this Bucket.
        The entity tag (ETag) for the live object lifecycle policy on the bucket.


        :param object_lifecycle_policy_etag: The object_lifecycle_policy_etag of this Bucket.
        :type: str
        """
        self._object_lifecycle_policy_etag = object_lifecycle_policy_etag

    @property
    def approximate_count(self):
        """
        Gets the approximate_count of this Bucket.
        The approximate number of objects in the bucket. Count statistics are reported periodically. You will see a
        lag between what is displayed and the actual object count.


        :return: The approximate_count of this Bucket.
        :rtype: int
        """
        return self._approximate_count

    @approximate_count.setter
    def approximate_count(self, approximate_count):
        """
        Sets the approximate_count of this Bucket.
        The approximate number of objects in the bucket. Count statistics are reported periodically. You will see a
        lag between what is displayed and the actual object count.


        :param approximate_count: The approximate_count of this Bucket.
        :type: int
        """
        self._approximate_count = approximate_count

    @property
    def approximate_size(self):
        """
        Gets the approximate_size of this Bucket.
        The approximate total size in bytes of all objects in the bucket. Size statistics are reported periodically. You will
        see a lag between what is displayed and the actual size of the bucket.


        :return: The approximate_size of this Bucket.
        :rtype: int
        """
        return self._approximate_size

    @approximate_size.setter
    def approximate_size(self, approximate_size):
        """
        Sets the approximate_size of this Bucket.
        The approximate total size in bytes of all objects in the bucket. Size statistics are reported periodically. You will
        see a lag between what is displayed and the actual size of the bucket.


        :param approximate_size: The approximate_size of this Bucket.
        :type: int
        """
        self._approximate_size = approximate_size

    @property
    def replication_enabled(self):
        """
        Gets the replication_enabled of this Bucket.
        Whether or not this bucket is a replication source. By default, `replicationEnabled` is set to `false`. This will
        be set to 'true' when you create a replication policy for the bucket.


        :return: The replication_enabled of this Bucket.
        :rtype: bool
        """
        return self._replication_enabled

    @replication_enabled.setter
    def replication_enabled(self, replication_enabled):
        """
        Sets the replication_enabled of this Bucket.
        Whether or not this bucket is a replication source. By default, `replicationEnabled` is set to `false`. This will
        be set to 'true' when you create a replication policy for the bucket.


        :param replication_enabled: The replication_enabled of this Bucket.
        :type: bool
        """
        self._replication_enabled = replication_enabled

    @property
    def is_read_only(self):
        """
        Gets the is_read_only of this Bucket.
        Whether or not this bucket is read only. By default, `isReadOnly` is set to `false`. This will
        be set to 'true' when this bucket is configured as a destination in a replication policy.


        :return: The is_read_only of this Bucket.
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """
        Sets the is_read_only of this Bucket.
        Whether or not this bucket is read only. By default, `isReadOnly` is set to `false`. This will
        be set to 'true' when this bucket is configured as a destination in a replication policy.


        :param is_read_only: The is_read_only of this Bucket.
        :type: bool
        """
        self._is_read_only = is_read_only

    @property
    def id(self):
        """
        Gets the id of this Bucket.
        The `OCID`__ of the bucket.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Bucket.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Bucket.
        The `OCID`__ of the bucket.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Bucket.
        :type: str
        """
        self._id = id

    @property
    def versioning(self):
        """
        Gets the versioning of this Bucket.
        The versioning status on the bucket. A bucket is created with versioning `Disabled` by default.
        For versioning `Enabled`, objects are protected from overwrites and deletes, by maintaining their version history. When versioning is `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted.

        Allowed values for this property are: "Enabled", "Suspended", "Disabled", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The versioning of this Bucket.
        :rtype: str
        """
        return self._versioning

    @versioning.setter
    def versioning(self, versioning):
        """
        Sets the versioning of this Bucket.
        The versioning status on the bucket. A bucket is created with versioning `Disabled` by default.
        For versioning `Enabled`, objects are protected from overwrites and deletes, by maintaining their version history. When versioning is `Suspended`, the previous versions will still remain but new versions will no longer be created when overwitten or deleted.


        :param versioning: The versioning of this Bucket.
        :type: str
        """
        allowed_values = ["Enabled", "Suspended", "Disabled"]
        if not value_allowed_none_or_none_sentinel(versioning, allowed_values):
            versioning = 'UNKNOWN_ENUM_VALUE'
        self._versioning = versioning

    @property
    def auto_tiering(self):
        """
        Gets the auto_tiering of this Bucket.
        The auto tiering status on the bucket. A bucket is created with auto tiering `Disabled` by default.
        For auto tiering `InfrequentAccess`, objects are transitioned automatically between the 'Standard'
        and 'InfrequentAccess' tiers based on the access pattern of the objects.

        Allowed values for this property are: "Disabled", "InfrequentAccess", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The auto_tiering of this Bucket.
        :rtype: str
        """
        return self._auto_tiering

    @auto_tiering.setter
    def auto_tiering(self, auto_tiering):
        """
        Sets the auto_tiering of this Bucket.
        The auto tiering status on the bucket. A bucket is created with auto tiering `Disabled` by default.
        For auto tiering `InfrequentAccess`, objects are transitioned automatically between the 'Standard'
        and 'InfrequentAccess' tiers based on the access pattern of the objects.


        :param auto_tiering: The auto_tiering of this Bucket.
        :type: str
        """
        allowed_values = ["Disabled", "InfrequentAccess"]
        if not value_allowed_none_or_none_sentinel(auto_tiering, allowed_values):
            auto_tiering = 'UNKNOWN_ENUM_VALUE'
        self._auto_tiering = auto_tiering

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
