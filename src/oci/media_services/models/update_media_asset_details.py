# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMediaAssetDetails(object):
    """
    The information to be updated.
    """

    #: A constant which can be used with the type property of a UpdateMediaAssetDetails.
    #: This constant has a value of "AUDIO"
    TYPE_AUDIO = "AUDIO"

    #: A constant which can be used with the type property of a UpdateMediaAssetDetails.
    #: This constant has a value of "VIDEO"
    TYPE_VIDEO = "VIDEO"

    #: A constant which can be used with the type property of a UpdateMediaAssetDetails.
    #: This constant has a value of "PLAYLIST"
    TYPE_PLAYLIST = "PLAYLIST"

    #: A constant which can be used with the type property of a UpdateMediaAssetDetails.
    #: This constant has a value of "IMAGE"
    TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the type property of a UpdateMediaAssetDetails.
    #: This constant has a value of "CAPTION_FILE"
    TYPE_CAPTION_FILE = "CAPTION_FILE"

    #: A constant which can be used with the type property of a UpdateMediaAssetDetails.
    #: This constant has a value of "UNKNOWN"
    TYPE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMediaAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMediaAssetDetails.
        :type display_name: str

        :param type:
            The value to assign to the type property of this UpdateMediaAssetDetails.
            Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"
        :type type: str

        :param parent_media_asset_id:
            The value to assign to the parent_media_asset_id property of this UpdateMediaAssetDetails.
        :type parent_media_asset_id: str

        :param master_media_asset_id:
            The value to assign to the master_media_asset_id property of this UpdateMediaAssetDetails.
        :type master_media_asset_id: str

        :param metadata:
            The value to assign to the metadata property of this UpdateMediaAssetDetails.
        :type metadata: list[oci.media_services.models.Metadata]

        :param media_asset_tags:
            The value to assign to the media_asset_tags property of this UpdateMediaAssetDetails.
        :type media_asset_tags: list[oci.media_services.models.MediaAssetTag]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMediaAssetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMediaAssetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'type': 'str',
            'parent_media_asset_id': 'str',
            'master_media_asset_id': 'str',
            'metadata': 'list[Metadata]',
            'media_asset_tags': 'list[MediaAssetTag]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'type': 'type',
            'parent_media_asset_id': 'parentMediaAssetId',
            'master_media_asset_id': 'masterMediaAssetId',
            'metadata': 'metadata',
            'media_asset_tags': 'mediaAssetTags',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._type = None
        self._parent_media_asset_id = None
        self._master_media_asset_id = None
        self._metadata = None
        self._media_asset_tags = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMediaAssetDetails.
        Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this UpdateMediaAssetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMediaAssetDetails.
        Display name for the Media Asset. Does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateMediaAssetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this UpdateMediaAssetDetails.
        The type of the media asset.

        Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"


        :return: The type of this UpdateMediaAssetDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateMediaAssetDetails.
        The type of the media asset.


        :param type: The type of this UpdateMediaAssetDetails.
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
        Gets the parent_media_asset_id of this UpdateMediaAssetDetails.
        The ID of the parent asset from which this asset is derived.


        :return: The parent_media_asset_id of this UpdateMediaAssetDetails.
        :rtype: str
        """
        return self._parent_media_asset_id

    @parent_media_asset_id.setter
    def parent_media_asset_id(self, parent_media_asset_id):
        """
        Sets the parent_media_asset_id of this UpdateMediaAssetDetails.
        The ID of the parent asset from which this asset is derived.


        :param parent_media_asset_id: The parent_media_asset_id of this UpdateMediaAssetDetails.
        :type: str
        """
        self._parent_media_asset_id = parent_media_asset_id

    @property
    def master_media_asset_id(self):
        """
        Gets the master_media_asset_id of this UpdateMediaAssetDetails.
        The ID of the senior most asset from which this asset is derived.


        :return: The master_media_asset_id of this UpdateMediaAssetDetails.
        :rtype: str
        """
        return self._master_media_asset_id

    @master_media_asset_id.setter
    def master_media_asset_id(self, master_media_asset_id):
        """
        Sets the master_media_asset_id of this UpdateMediaAssetDetails.
        The ID of the senior most asset from which this asset is derived.


        :param master_media_asset_id: The master_media_asset_id of this UpdateMediaAssetDetails.
        :type: str
        """
        self._master_media_asset_id = master_media_asset_id

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateMediaAssetDetails.
        List of Metadata.


        :return: The metadata of this UpdateMediaAssetDetails.
        :rtype: list[oci.media_services.models.Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateMediaAssetDetails.
        List of Metadata.


        :param metadata: The metadata of this UpdateMediaAssetDetails.
        :type: list[oci.media_services.models.Metadata]
        """
        self._metadata = metadata

    @property
    def media_asset_tags(self):
        """
        Gets the media_asset_tags of this UpdateMediaAssetDetails.
        List of tags for the MediaAsset.


        :return: The media_asset_tags of this UpdateMediaAssetDetails.
        :rtype: list[oci.media_services.models.MediaAssetTag]
        """
        return self._media_asset_tags

    @media_asset_tags.setter
    def media_asset_tags(self, media_asset_tags):
        """
        Sets the media_asset_tags of this UpdateMediaAssetDetails.
        List of tags for the MediaAsset.


        :param media_asset_tags: The media_asset_tags of this UpdateMediaAssetDetails.
        :type: list[oci.media_services.models.MediaAssetTag]
        """
        self._media_asset_tags = media_asset_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMediaAssetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateMediaAssetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMediaAssetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateMediaAssetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMediaAssetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMediaAssetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMediaAssetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMediaAssetDetails.
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
