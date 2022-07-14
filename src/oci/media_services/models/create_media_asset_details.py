# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMediaAssetDetails(object):
    """
    The information about new MediaAsset.
    """

    #: A constant which can be used with the type property of a CreateMediaAssetDetails.
    #: This constant has a value of "AUDIO"
    TYPE_AUDIO = "AUDIO"

    #: A constant which can be used with the type property of a CreateMediaAssetDetails.
    #: This constant has a value of "VIDEO"
    TYPE_VIDEO = "VIDEO"

    #: A constant which can be used with the type property of a CreateMediaAssetDetails.
    #: This constant has a value of "PLAYLIST"
    TYPE_PLAYLIST = "PLAYLIST"

    #: A constant which can be used with the type property of a CreateMediaAssetDetails.
    #: This constant has a value of "IMAGE"
    TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the type property of a CreateMediaAssetDetails.
    #: This constant has a value of "CAPTION_FILE"
    TYPE_CAPTION_FILE = "CAPTION_FILE"

    #: A constant which can be used with the type property of a CreateMediaAssetDetails.
    #: This constant has a value of "UNKNOWN"
    TYPE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMediaAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_media_workflow_id:
            The value to assign to the source_media_workflow_id property of this CreateMediaAssetDetails.
        :type source_media_workflow_id: str

        :param media_workflow_job_id:
            The value to assign to the media_workflow_job_id property of this CreateMediaAssetDetails.
        :type media_workflow_job_id: str

        :param source_media_workflow_version:
            The value to assign to the source_media_workflow_version property of this CreateMediaAssetDetails.
        :type source_media_workflow_version: int

        :param display_name:
            The value to assign to the display_name property of this CreateMediaAssetDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMediaAssetDetails.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CreateMediaAssetDetails.
            Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"
        :type type: str

        :param parent_media_asset_id:
            The value to assign to the parent_media_asset_id property of this CreateMediaAssetDetails.
        :type parent_media_asset_id: str

        :param master_media_asset_id:
            The value to assign to the master_media_asset_id property of this CreateMediaAssetDetails.
        :type master_media_asset_id: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CreateMediaAssetDetails.
        :type bucket_name: str

        :param namespace_name:
            The value to assign to the namespace_name property of this CreateMediaAssetDetails.
        :type namespace_name: str

        :param object_name:
            The value to assign to the object_name property of this CreateMediaAssetDetails.
        :type object_name: str

        :param object_etag:
            The value to assign to the object_etag property of this CreateMediaAssetDetails.
        :type object_etag: str

        :param metadata:
            The value to assign to the metadata property of this CreateMediaAssetDetails.
        :type metadata: list[oci.media_services.models.Metadata]

        :param segment_range_start_index:
            The value to assign to the segment_range_start_index property of this CreateMediaAssetDetails.
        :type segment_range_start_index: int

        :param segment_range_end_index:
            The value to assign to the segment_range_end_index property of this CreateMediaAssetDetails.
        :type segment_range_end_index: int

        :param media_asset_tags:
            The value to assign to the media_asset_tags property of this CreateMediaAssetDetails.
        :type media_asset_tags: list[oci.media_services.models.MediaAssetTag]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMediaAssetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMediaAssetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'source_media_workflow_id': 'str',
            'media_workflow_job_id': 'str',
            'source_media_workflow_version': 'int',
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'parent_media_asset_id': 'str',
            'master_media_asset_id': 'str',
            'bucket_name': 'str',
            'namespace_name': 'str',
            'object_name': 'str',
            'object_etag': 'str',
            'metadata': 'list[Metadata]',
            'segment_range_start_index': 'int',
            'segment_range_end_index': 'int',
            'media_asset_tags': 'list[MediaAssetTag]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'source_media_workflow_id': 'sourceMediaWorkflowId',
            'media_workflow_job_id': 'mediaWorkflowJobId',
            'source_media_workflow_version': 'sourceMediaWorkflowVersion',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'parent_media_asset_id': 'parentMediaAssetId',
            'master_media_asset_id': 'masterMediaAssetId',
            'bucket_name': 'bucketName',
            'namespace_name': 'namespaceName',
            'object_name': 'objectName',
            'object_etag': 'objectEtag',
            'metadata': 'metadata',
            'segment_range_start_index': 'segmentRangeStartIndex',
            'segment_range_end_index': 'segmentRangeEndIndex',
            'media_asset_tags': 'mediaAssetTags',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._source_media_workflow_id = None
        self._media_workflow_job_id = None
        self._source_media_workflow_version = None
        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._parent_media_asset_id = None
        self._master_media_asset_id = None
        self._bucket_name = None
        self._namespace_name = None
        self._object_name = None
        self._object_etag = None
        self._metadata = None
        self._segment_range_start_index = None
        self._segment_range_end_index = None
        self._media_asset_tags = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def source_media_workflow_id(self):
        """
        Gets the source_media_workflow_id of this CreateMediaAssetDetails.
        The ID of the MediaWorkflow used to produce this asset.


        :return: The source_media_workflow_id of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._source_media_workflow_id

    @source_media_workflow_id.setter
    def source_media_workflow_id(self, source_media_workflow_id):
        """
        Sets the source_media_workflow_id of this CreateMediaAssetDetails.
        The ID of the MediaWorkflow used to produce this asset.


        :param source_media_workflow_id: The source_media_workflow_id of this CreateMediaAssetDetails.
        :type: str
        """
        self._source_media_workflow_id = source_media_workflow_id

    @property
    def media_workflow_job_id(self):
        """
        Gets the media_workflow_job_id of this CreateMediaAssetDetails.
        The ID of the MediaWorkflowJob used to produce this asset.


        :return: The media_workflow_job_id of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._media_workflow_job_id

    @media_workflow_job_id.setter
    def media_workflow_job_id(self, media_workflow_job_id):
        """
        Sets the media_workflow_job_id of this CreateMediaAssetDetails.
        The ID of the MediaWorkflowJob used to produce this asset.


        :param media_workflow_job_id: The media_workflow_job_id of this CreateMediaAssetDetails.
        :type: str
        """
        self._media_workflow_job_id = media_workflow_job_id

    @property
    def source_media_workflow_version(self):
        """
        Gets the source_media_workflow_version of this CreateMediaAssetDetails.
        The version of the MediaWorkflow used to produce this asset.


        :return: The source_media_workflow_version of this CreateMediaAssetDetails.
        :rtype: int
        """
        return self._source_media_workflow_version

    @source_media_workflow_version.setter
    def source_media_workflow_version(self, source_media_workflow_version):
        """
        Sets the source_media_workflow_version of this CreateMediaAssetDetails.
        The version of the MediaWorkflow used to produce this asset.


        :param source_media_workflow_version: The source_media_workflow_version of this CreateMediaAssetDetails.
        :type: int
        """
        self._source_media_workflow_version = source_media_workflow_version

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateMediaAssetDetails.
        Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateMediaAssetDetails.
        Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreateMediaAssetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateMediaAssetDetails.
        Compartment Identifier.


        :return: The compartment_id of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateMediaAssetDetails.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CreateMediaAssetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateMediaAssetDetails.
        The type of the media asset.

        Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"


        :return: The type of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateMediaAssetDetails.
        The type of the media asset.


        :param type: The type of this CreateMediaAssetDetails.
        :type: str
        """
        allowed_values = ["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def parent_media_asset_id(self):
        """
        Gets the parent_media_asset_id of this CreateMediaAssetDetails.
        The ID of the parent asset from which this asset is derived.


        :return: The parent_media_asset_id of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._parent_media_asset_id

    @parent_media_asset_id.setter
    def parent_media_asset_id(self, parent_media_asset_id):
        """
        Sets the parent_media_asset_id of this CreateMediaAssetDetails.
        The ID of the parent asset from which this asset is derived.


        :param parent_media_asset_id: The parent_media_asset_id of this CreateMediaAssetDetails.
        :type: str
        """
        self._parent_media_asset_id = parent_media_asset_id

    @property
    def master_media_asset_id(self):
        """
        Gets the master_media_asset_id of this CreateMediaAssetDetails.
        The ID of the senior most asset from which this asset is derived.


        :return: The master_media_asset_id of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._master_media_asset_id

    @master_media_asset_id.setter
    def master_media_asset_id(self, master_media_asset_id):
        """
        Sets the master_media_asset_id of this CreateMediaAssetDetails.
        The ID of the senior most asset from which this asset is derived.


        :param master_media_asset_id: The master_media_asset_id of this CreateMediaAssetDetails.
        :type: str
        """
        self._master_media_asset_id = master_media_asset_id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this CreateMediaAssetDetails.
        The name of the object storage bucket where this asset is located.


        :return: The bucket_name of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CreateMediaAssetDetails.
        The name of the object storage bucket where this asset is located.


        :param bucket_name: The bucket_name of this CreateMediaAssetDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this CreateMediaAssetDetails.
        The object storage namespace where this asset is located.


        :return: The namespace_name of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CreateMediaAssetDetails.
        The object storage namespace where this asset is located.


        :param namespace_name: The namespace_name of this CreateMediaAssetDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def object_name(self):
        """
        Gets the object_name of this CreateMediaAssetDetails.
        The object storage object name that identifies this asset.


        :return: The object_name of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this CreateMediaAssetDetails.
        The object storage object name that identifies this asset.


        :param object_name: The object_name of this CreateMediaAssetDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_etag(self):
        """
        Gets the object_etag of this CreateMediaAssetDetails.
        eTag of the underlying object storage object.


        :return: The object_etag of this CreateMediaAssetDetails.
        :rtype: str
        """
        return self._object_etag

    @object_etag.setter
    def object_etag(self, object_etag):
        """
        Sets the object_etag of this CreateMediaAssetDetails.
        eTag of the underlying object storage object.


        :param object_etag: The object_etag of this CreateMediaAssetDetails.
        :type: str
        """
        self._object_etag = object_etag

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateMediaAssetDetails.
        List of Metadata.


        :return: The metadata of this CreateMediaAssetDetails.
        :rtype: list[oci.media_services.models.Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateMediaAssetDetails.
        List of Metadata.


        :param metadata: The metadata of this CreateMediaAssetDetails.
        :type: list[oci.media_services.models.Metadata]
        """
        self._metadata = metadata

    @property
    def segment_range_start_index(self):
        """
        Gets the segment_range_start_index of this CreateMediaAssetDetails.
        The start index for video segment files.


        :return: The segment_range_start_index of this CreateMediaAssetDetails.
        :rtype: int
        """
        return self._segment_range_start_index

    @segment_range_start_index.setter
    def segment_range_start_index(self, segment_range_start_index):
        """
        Sets the segment_range_start_index of this CreateMediaAssetDetails.
        The start index for video segment files.


        :param segment_range_start_index: The segment_range_start_index of this CreateMediaAssetDetails.
        :type: int
        """
        self._segment_range_start_index = segment_range_start_index

    @property
    def segment_range_end_index(self):
        """
        Gets the segment_range_end_index of this CreateMediaAssetDetails.
        The end index for video segment files.


        :return: The segment_range_end_index of this CreateMediaAssetDetails.
        :rtype: int
        """
        return self._segment_range_end_index

    @segment_range_end_index.setter
    def segment_range_end_index(self, segment_range_end_index):
        """
        Sets the segment_range_end_index of this CreateMediaAssetDetails.
        The end index for video segment files.


        :param segment_range_end_index: The segment_range_end_index of this CreateMediaAssetDetails.
        :type: int
        """
        self._segment_range_end_index = segment_range_end_index

    @property
    def media_asset_tags(self):
        """
        Gets the media_asset_tags of this CreateMediaAssetDetails.
        list of tags for the MediaAsset.


        :return: The media_asset_tags of this CreateMediaAssetDetails.
        :rtype: list[oci.media_services.models.MediaAssetTag]
        """
        return self._media_asset_tags

    @media_asset_tags.setter
    def media_asset_tags(self, media_asset_tags):
        """
        Sets the media_asset_tags of this CreateMediaAssetDetails.
        list of tags for the MediaAsset.


        :param media_asset_tags: The media_asset_tags of this CreateMediaAssetDetails.
        :type: list[oci.media_services.models.MediaAssetTag]
        """
        self._media_asset_tags = media_asset_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateMediaAssetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateMediaAssetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateMediaAssetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateMediaAssetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateMediaAssetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateMediaAssetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateMediaAssetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateMediaAssetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
