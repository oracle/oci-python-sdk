# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateObjectStorageTierDetails(object):
    """
    To change the storage tier of an object, we specify the object name and the desired
    storage tier in the body. Objects can be moved between Standard and InfrequentAccess
    tiers and from Standard or InfrequentAccess tier to Archive tier. If a version id is
    specified, only the specified version of the object is moved to a different storage
    tier, else the current version is used.
    """

    #: A constant which can be used with the storage_tier property of a UpdateObjectStorageTierDetails.
    #: This constant has a value of "Standard"
    STORAGE_TIER_STANDARD = "Standard"

    #: A constant which can be used with the storage_tier property of a UpdateObjectStorageTierDetails.
    #: This constant has a value of "InfrequentAccess"
    STORAGE_TIER_INFREQUENT_ACCESS = "InfrequentAccess"

    #: A constant which can be used with the storage_tier property of a UpdateObjectStorageTierDetails.
    #: This constant has a value of "Archive"
    STORAGE_TIER_ARCHIVE = "Archive"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateObjectStorageTierDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_name:
            The value to assign to the object_name property of this UpdateObjectStorageTierDetails.
        :type object_name: str

        :param storage_tier:
            The value to assign to the storage_tier property of this UpdateObjectStorageTierDetails.
            Allowed values for this property are: "Standard", "InfrequentAccess", "Archive"
        :type storage_tier: str

        :param version_id:
            The value to assign to the version_id property of this UpdateObjectStorageTierDetails.
        :type version_id: str

        """
        self.swagger_types = {
            'object_name': 'str',
            'storage_tier': 'str',
            'version_id': 'str'
        }

        self.attribute_map = {
            'object_name': 'objectName',
            'storage_tier': 'storageTier',
            'version_id': 'versionId'
        }

        self._object_name = None
        self._storage_tier = None
        self._version_id = None

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this UpdateObjectStorageTierDetails.
        An object for which the storage tier needs to be changed.


        :return: The object_name of this UpdateObjectStorageTierDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this UpdateObjectStorageTierDetails.
        An object for which the storage tier needs to be changed.


        :param object_name: The object_name of this UpdateObjectStorageTierDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def storage_tier(self):
        """
        **[Required]** Gets the storage_tier of this UpdateObjectStorageTierDetails.
        The storage tier that the object should be moved to.

        Allowed values for this property are: "Standard", "InfrequentAccess", "Archive"


        :return: The storage_tier of this UpdateObjectStorageTierDetails.
        :rtype: str
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """
        Sets the storage_tier of this UpdateObjectStorageTierDetails.
        The storage tier that the object should be moved to.


        :param storage_tier: The storage_tier of this UpdateObjectStorageTierDetails.
        :type: str
        """
        allowed_values = ["Standard", "InfrequentAccess", "Archive"]
        if not value_allowed_none_or_none_sentinel(storage_tier, allowed_values):
            raise ValueError(
                "Invalid value for `storage_tier`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._storage_tier = storage_tier

    @property
    def version_id(self):
        """
        Gets the version_id of this UpdateObjectStorageTierDetails.
        The versionId of the object. Current object version is used by default.


        :return: The version_id of this UpdateObjectStorageTierDetails.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """
        Sets the version_id of this UpdateObjectStorageTierDetails.
        The versionId of the object. Current object version is used by default.


        :param version_id: The version_id of this UpdateObjectStorageTierDetails.
        :type: str
        """
        self._version_id = version_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
