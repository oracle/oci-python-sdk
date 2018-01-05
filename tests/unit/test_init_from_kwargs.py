from datetime import datetime

import oci
import pytest
import six


ENUM_ATTR_TO_VALUE = {
    'CreateVirtualCircuitDetails': {'type': 'PRIVATE'},
    'UpdateVirtualCircuitDetails': {'provider_state': 'ACTIVE'},
    'PatchDetails': {'action': 'APPLY'},
    'LaunchDbSystemDetails': {'license_model': 'LICENSE_INCLUDED', 'disk_redundancy': 'NORMAL', 'database_edition': 'STANDARD_EDITION'},
    'CreateDatabaseDetails': {'db_workload': 'OLTP'},
    'CreateDataGuardAssociationDetails': {'protection_mode': 'MAXIMUM_AVAILABILITY', 'transport_type': 'SYNC'},
    'CreateDataGuardAssociationToExistingDbSystemDetails': {'protection_mode': 'MAXIMUM_AVAILABILITY', 'transport_type': 'SYNC'},
    'CreateSaml2IdentityProviderDetails': {'protocol': 'SAML2', 'product_type': 'ADFS'},
    'UpdateSaml2IdentityProviderDetails': {'protocol': 'SAML2', 'product_type': 'ADFS'},
    'CreateIdentityProviderDetails': {'protocol': 'SAML2', 'product_type': 'ADFS'},
    'UpdateIdentityProviderDetails': {'protocol': 'SAML2', 'product_type': 'ADFS'},
    'CreateBucketDetails': {'public_access_type': 'NoPublicAccess', 'storage_tier': 'Standard'},
    'UpdateBucketDetails': {'public_access_type': 'NoPublicAccess'},
    'CreatePreauthenticatedRequestDetails': {'access_type': 'ObjectRead'},
    'CreateDbHomeWithDbSystemIdBase': {'source': 'DB_BACKUP'},
    'CreateDbHomeWithDbSystemIdFromBackupDetails': {'source': 'DB_BACKUP'},
    'CreateDbHomeWithDbSystemIdDetails': {'source': 'NONE'},
    'CreateImageDetails': {'launch_mode': 'NATIVE'},
    'ImageSourceDetails': {'source_image_type': 'QCOW2'},
    'ImageSourceViaObjectStorageUriDetails': {'source_image_type': 'QCOW2'},
    'ImageSourceViaObjectStorageTupleDetails': {'source_image_type': 'QCOW2'}
}


def test_all_model_classes_can_be_init_from_kwargs():
    model_mappings = [
        oci.audit.models.audit_type_mapping,
        oci.core.models.core_type_mapping,
        oci.database.models.database_type_mapping,
        oci.identity.models.identity_type_mapping,
        oci.load_balancer.models.load_balancer_type_mapping,
        oci.object_storage.models.object_storage_type_mapping
    ]

    for mapping in model_mappings:
        for model_name, model_ref in six.iteritems(mapping):
            base_model = model_ref()
            kwargs = {}
            for attr_name, attr_type in six.iteritems(base_model.swagger_types):
                if attr_type == 'str':
                    if model_name in ENUM_ATTR_TO_VALUE and attr_name in ENUM_ATTR_TO_VALUE[model_name]:
                        kwargs[attr_name] = ENUM_ATTR_TO_VALUE[model_name][attr_name]
                    else:
                        kwargs[attr_name] = attr_type
                elif attr_type == 'int':
                    kwargs[attr_name] = 55
                elif attr_type == 'datetime':
                    kwargs[attr_name] = datetime.utcnow()
                elif attr_type.startswith('list['):
                    kwargs[attr_name] = []
                elif attr_type == 'dict(str, str)':
                    kwargs[attr_name] = {'a': 'b', 'c': 'd'}
                elif attr_type == 'dict(str, list[str])':
                    kwargs[attr_name] = {'f': ['cat', 'hat', 'mat']}
                elif attr_type == 'dict(str, object)':
                    kwargs[attr_name] = {'g': {'h': 'i'}}
                elif attr_type.startswith('dict('):
                    kwargs[attr_name] = {}
                else:
                    if attr_name in mapping:
                        kwargs[attr_name] = mapping[attr_name]()
                    else:
                        kwargs[attr_name] = attr_name

            model_with_kwargs = model_ref(**kwargs)
            for attr_name, attr_value in six.iteritems(kwargs):
                value_from_model = getattr(model_with_kwargs, attr_name)
                if value_from_model == 'UNKNOWN_ENUM_VALUE':
                    continue
                assert attr_value == value_from_model


def test_decorated_model_class_init_no_kwargs():
    model = MyTestModel()

    for attr_name in model.attribute_map.keys():
        assert getattr(model, attr_name) is None


def test_decorated_model_class_init_from_kwargs_full():
    test_datetime = datetime.utcnow()
    model = MyTestModel(
        namespace='test namespace',
        name='test name',
        compartment_id='test compartment_id',
        metadata={'a': 'b', 'c': 'd'},
        created_by='test user',
        time_created=test_datetime,
        etag='test etag',
        public_access_type='NoPublicAccess',
        storage_tier='Archive'
    )

    assert model.namespace == 'test namespace'
    assert model.name == 'test name'
    assert model.compartment_id == 'test compartment_id'
    assert model.metadata == {'a': 'b', 'c': 'd'}
    assert model.created_by == 'test user'
    assert model.time_created == test_datetime
    assert model.etag == 'test etag'
    assert model.public_access_type == 'NoPublicAccess'
    assert model.storage_tier == 'Archive'


def test_decorated_model_class_init_from_kwargs_partial():
    model = MyTestModel(namespace='test namespace', storage_tier='Standard')

    assert model.namespace == 'test namespace'
    assert model.name is None
    assert model.compartment_id is None
    assert model.metadata is None
    assert model.created_by is None
    assert model.time_created is None
    assert model.etag is None
    assert model.public_access_type is None
    assert model.storage_tier == 'Standard'


def test_decorated_model_class_honors_enum_logic():
    model = MyTestModel(storage_tier='superman')
    assert model.storage_tier == 'UNKNOWN_ENUM_VALUE'

    with pytest.raises(ValueError) as err:
        model = MyTestModel(public_access_type='bad value')
    assert 'Invalid value for `public_access_type`, must be one of' in str(err)


def test_decorated_model_class_rejects_unknown_values():
    with pytest.raises(TypeError) as err:
        MyTestModel(bad_key='bad val', another_bad_key=55, bad_dict={'a', 'b'})

    assert 'Unrecognized keyword arguments' in str(err)
    assert 'bad_key' in str(err)
    assert 'another_bad_key' in str(err)
    assert 'bad_dict' in str(err)


@oci.decorators.init_model_state_from_kwargs
class MyTestModel(object):
    def __init__(self):
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
            raise ValueError(
                "Invalid value for `public_access_type`, must be one of {0}"
                .format(allowed_values)
            )
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
