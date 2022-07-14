# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaAsset(object):
    """
    Represents the metadata associated with an asset that has been either produced by or registered with Media Services.
    """

    #: A constant which can be used with the lifecycle_state property of a MediaAsset.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MediaAsset.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MediaAsset.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MediaAsset.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MediaAsset.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MediaAsset.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the type property of a MediaAsset.
    #: This constant has a value of "AUDIO"
    TYPE_AUDIO = "AUDIO"

    #: A constant which can be used with the type property of a MediaAsset.
    #: This constant has a value of "VIDEO"
    TYPE_VIDEO = "VIDEO"

    #: A constant which can be used with the type property of a MediaAsset.
    #: This constant has a value of "PLAYLIST"
    TYPE_PLAYLIST = "PLAYLIST"

    #: A constant which can be used with the type property of a MediaAsset.
    #: This constant has a value of "IMAGE"
    TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the type property of a MediaAsset.
    #: This constant has a value of "CAPTION_FILE"
    TYPE_CAPTION_FILE = "CAPTION_FILE"

    #: A constant which can be used with the type property of a MediaAsset.
    #: This constant has a value of "UNKNOWN"
    TYPE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new MediaAsset object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MediaAsset.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MediaAsset.
        :type compartment_id: str

        :param source_media_workflow_id:
            The value to assign to the source_media_workflow_id property of this MediaAsset.
        :type source_media_workflow_id: str

        :param media_workflow_job_id:
            The value to assign to the media_workflow_job_id property of this MediaAsset.
        :type media_workflow_job_id: str

        :param source_media_workflow_version:
            The value to assign to the source_media_workflow_version property of this MediaAsset.
        :type source_media_workflow_version: int

        :param display_name:
            The value to assign to the display_name property of this MediaAsset.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this MediaAsset.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MediaAsset.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param type:
            The value to assign to the type property of this MediaAsset.
            Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param parent_media_asset_id:
            The value to assign to the parent_media_asset_id property of this MediaAsset.
        :type parent_media_asset_id: str

        :param master_media_asset_id:
            The value to assign to the master_media_asset_id property of this MediaAsset.
        :type master_media_asset_id: str

        :param bucket_name:
            The value to assign to the bucket_name property of this MediaAsset.
        :type bucket_name: str

        :param namespace_name:
            The value to assign to the namespace_name property of this MediaAsset.
        :type namespace_name: str

        :param object_name:
            The value to assign to the object_name property of this MediaAsset.
        :type object_name: str

        :param object_etag:
            The value to assign to the object_etag property of this MediaAsset.
        :type object_etag: str

        :param time_updated:
            The value to assign to the time_updated property of this MediaAsset.
        :type time_updated: datetime

        :param segment_range_start_index:
            The value to assign to the segment_range_start_index property of this MediaAsset.
        :type segment_range_start_index: int

        :param segment_range_end_index:
            The value to assign to the segment_range_end_index property of this MediaAsset.
        :type segment_range_end_index: int

        :param metadata:
            The value to assign to the metadata property of this MediaAsset.
        :type metadata: list[oci.media_services.models.Metadata]

        :param media_asset_tags:
            The value to assign to the media_asset_tags property of this MediaAsset.
        :type media_asset_tags: list[oci.media_services.models.MediaAssetTag]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MediaAsset.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MediaAsset.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MediaAsset.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'source_media_workflow_id': 'str',
            'media_workflow_job_id': 'str',
            'source_media_workflow_version': 'int',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'type': 'str',
            'parent_media_asset_id': 'str',
            'master_media_asset_id': 'str',
            'bucket_name': 'str',
            'namespace_name': 'str',
            'object_name': 'str',
            'object_etag': 'str',
            'time_updated': 'datetime',
            'segment_range_start_index': 'int',
            'segment_range_end_index': 'int',
            'metadata': 'list[Metadata]',
            'media_asset_tags': 'list[MediaAssetTag]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'source_media_workflow_id': 'sourceMediaWorkflowId',
            'media_workflow_job_id': 'mediaWorkflowJobId',
            'source_media_workflow_version': 'sourceMediaWorkflowVersion',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'type': 'type',
            'parent_media_asset_id': 'parentMediaAssetId',
            'master_media_asset_id': 'masterMediaAssetId',
            'bucket_name': 'bucketName',
            'namespace_name': 'namespaceName',
            'object_name': 'objectName',
            'object_etag': 'objectEtag',
            'time_updated': 'timeUpdated',
            'segment_range_start_index': 'segmentRangeStartIndex',
            'segment_range_end_index': 'segmentRangeEndIndex',
            'metadata': 'metadata',
            'media_asset_tags': 'mediaAssetTags',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._source_media_workflow_id = None
        self._media_workflow_job_id = None
        self._source_media_workflow_version = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._type = None
        self._parent_media_asset_id = None
        self._master_media_asset_id = None
        self._bucket_name = None
        self._namespace_name = None
        self._object_name = None
        self._object_etag = None
        self._time_updated = None
        self._segment_range_start_index = None
        self._segment_range_end_index = None
        self._metadata = None
        self._media_asset_tags = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MediaAsset.
        Unique identifier that is immutable on creation.


        :return: The id of this MediaAsset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MediaAsset.
        Unique identifier that is immutable on creation.


        :param id: The id of this MediaAsset.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MediaAsset.
        The ID of the compartment containing the MediaAsset.


        :return: The compartment_id of this MediaAsset.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MediaAsset.
        The ID of the compartment containing the MediaAsset.


        :param compartment_id: The compartment_id of this MediaAsset.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_media_workflow_id(self):
        """
        Gets the source_media_workflow_id of this MediaAsset.
        The ID of the MediaWorkflow used to produce this asset.


        :return: The source_media_workflow_id of this MediaAsset.
        :rtype: str
        """
        return self._source_media_workflow_id

    @source_media_workflow_id.setter
    def source_media_workflow_id(self, source_media_workflow_id):
        """
        Sets the source_media_workflow_id of this MediaAsset.
        The ID of the MediaWorkflow used to produce this asset.


        :param source_media_workflow_id: The source_media_workflow_id of this MediaAsset.
        :type: str
        """
        self._source_media_workflow_id = source_media_workflow_id

    @property
    def media_workflow_job_id(self):
        """
        Gets the media_workflow_job_id of this MediaAsset.
        The ID of the MediaWorkflowJob used to produce this asset.


        :return: The media_workflow_job_id of this MediaAsset.
        :rtype: str
        """
        return self._media_workflow_job_id

    @media_workflow_job_id.setter
    def media_workflow_job_id(self, media_workflow_job_id):
        """
        Sets the media_workflow_job_id of this MediaAsset.
        The ID of the MediaWorkflowJob used to produce this asset.


        :param media_workflow_job_id: The media_workflow_job_id of this MediaAsset.
        :type: str
        """
        self._media_workflow_job_id = media_workflow_job_id

    @property
    def source_media_workflow_version(self):
        """
        Gets the source_media_workflow_version of this MediaAsset.
        The version of the MediaWorkflow used to produce this asset.


        :return: The source_media_workflow_version of this MediaAsset.
        :rtype: int
        """
        return self._source_media_workflow_version

    @source_media_workflow_version.setter
    def source_media_workflow_version(self, source_media_workflow_version):
        """
        Sets the source_media_workflow_version of this MediaAsset.
        The version of the MediaWorkflow used to produce this asset.


        :param source_media_workflow_version: The source_media_workflow_version of this MediaAsset.
        :type: int
        """
        self._source_media_workflow_version = source_media_workflow_version

    @property
    def display_name(self):
        """
        Gets the display_name of this MediaAsset.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this MediaAsset.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MediaAsset.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this MediaAsset.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this MediaAsset.
        The time when the MediaAsset was created. An RFC3339 formatted datetime string.


        :return: The time_created of this MediaAsset.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MediaAsset.
        The time when the MediaAsset was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MediaAsset.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MediaAsset.
        The current state of the MediaAsset.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MediaAsset.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MediaAsset.
        The current state of the MediaAsset.


        :param lifecycle_state: The lifecycle_state of this MediaAsset.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MediaAsset.
        The type of the media asset.

        Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MediaAsset.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MediaAsset.
        The type of the media asset.


        :param type: The type of this MediaAsset.
        :type: str
        """
        allowed_values = ["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def parent_media_asset_id(self):
        """
        Gets the parent_media_asset_id of this MediaAsset.
        The ID of the parent asset from which this asset is derived.


        :return: The parent_media_asset_id of this MediaAsset.
        :rtype: str
        """
        return self._parent_media_asset_id

    @parent_media_asset_id.setter
    def parent_media_asset_id(self, parent_media_asset_id):
        """
        Sets the parent_media_asset_id of this MediaAsset.
        The ID of the parent asset from which this asset is derived.


        :param parent_media_asset_id: The parent_media_asset_id of this MediaAsset.
        :type: str
        """
        self._parent_media_asset_id = parent_media_asset_id

    @property
    def master_media_asset_id(self):
        """
        Gets the master_media_asset_id of this MediaAsset.
        The ID of the senior most asset from which this asset is derived.


        :return: The master_media_asset_id of this MediaAsset.
        :rtype: str
        """
        return self._master_media_asset_id

    @master_media_asset_id.setter
    def master_media_asset_id(self, master_media_asset_id):
        """
        Sets the master_media_asset_id of this MediaAsset.
        The ID of the senior most asset from which this asset is derived.


        :param master_media_asset_id: The master_media_asset_id of this MediaAsset.
        :type: str
        """
        self._master_media_asset_id = master_media_asset_id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this MediaAsset.
        The name of the object storage bucket where this represented asset is located.


        :return: The bucket_name of this MediaAsset.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this MediaAsset.
        The name of the object storage bucket where this represented asset is located.


        :param bucket_name: The bucket_name of this MediaAsset.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this MediaAsset.
        The object storage namespace where this asset is located.


        :return: The namespace_name of this MediaAsset.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this MediaAsset.
        The object storage namespace where this asset is located.


        :param namespace_name: The namespace_name of this MediaAsset.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def object_name(self):
        """
        Gets the object_name of this MediaAsset.
        The object storage object name that identifies this asset.


        :return: The object_name of this MediaAsset.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this MediaAsset.
        The object storage object name that identifies this asset.


        :param object_name: The object_name of this MediaAsset.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_etag(self):
        """
        Gets the object_etag of this MediaAsset.
        eTag of the underlying object storage object.


        :return: The object_etag of this MediaAsset.
        :rtype: str
        """
        return self._object_etag

    @object_etag.setter
    def object_etag(self, object_etag):
        """
        Sets the object_etag of this MediaAsset.
        eTag of the underlying object storage object.


        :param object_etag: The object_etag of this MediaAsset.
        :type: str
        """
        self._object_etag = object_etag

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MediaAsset.
        The time when the MediaAsset was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this MediaAsset.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MediaAsset.
        The time when the MediaAsset was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MediaAsset.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def segment_range_start_index(self):
        """
        Gets the segment_range_start_index of this MediaAsset.
        The start index for video segment files.


        :return: The segment_range_start_index of this MediaAsset.
        :rtype: int
        """
        return self._segment_range_start_index

    @segment_range_start_index.setter
    def segment_range_start_index(self, segment_range_start_index):
        """
        Sets the segment_range_start_index of this MediaAsset.
        The start index for video segment files.


        :param segment_range_start_index: The segment_range_start_index of this MediaAsset.
        :type: int
        """
        self._segment_range_start_index = segment_range_start_index

    @property
    def segment_range_end_index(self):
        """
        Gets the segment_range_end_index of this MediaAsset.
        The end index of video segment files.


        :return: The segment_range_end_index of this MediaAsset.
        :rtype: int
        """
        return self._segment_range_end_index

    @segment_range_end_index.setter
    def segment_range_end_index(self, segment_range_end_index):
        """
        Sets the segment_range_end_index of this MediaAsset.
        The end index of video segment files.


        :param segment_range_end_index: The segment_range_end_index of this MediaAsset.
        :type: int
        """
        self._segment_range_end_index = segment_range_end_index

    @property
    def metadata(self):
        """
        Gets the metadata of this MediaAsset.
        List of Metadata.


        :return: The metadata of this MediaAsset.
        :rtype: list[oci.media_services.models.Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MediaAsset.
        List of Metadata.


        :param metadata: The metadata of this MediaAsset.
        :type: list[oci.media_services.models.Metadata]
        """
        self._metadata = metadata

    @property
    def media_asset_tags(self):
        """
        Gets the media_asset_tags of this MediaAsset.
        List of tags for the MediaAsset.


        :return: The media_asset_tags of this MediaAsset.
        :rtype: list[oci.media_services.models.MediaAssetTag]
        """
        return self._media_asset_tags

    @media_asset_tags.setter
    def media_asset_tags(self, media_asset_tags):
        """
        Sets the media_asset_tags of this MediaAsset.
        List of tags for the MediaAsset.


        :param media_asset_tags: The media_asset_tags of this MediaAsset.
        :type: list[oci.media_services.models.MediaAssetTag]
        """
        self._media_asset_tags = media_asset_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MediaAsset.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MediaAsset.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MediaAsset.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MediaAsset.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MediaAsset.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MediaAsset.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MediaAsset.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MediaAsset.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MediaAsset.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MediaAsset.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MediaAsset.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MediaAsset.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
