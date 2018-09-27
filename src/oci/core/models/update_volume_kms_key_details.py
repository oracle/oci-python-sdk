# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVolumeKmsKeyDetails(object):
    """
    UpdateVolumeKmsKeyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVolumeKmsKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this UpdateVolumeKmsKeyDetails.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId'
        }

        self._kms_key_id = None

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this UpdateVolumeKmsKeyDetails.
        The new kms key which will be used to protect the specific volume.
        This key has to be a valid kms key ocid, and user must have key delegation policy to allow them to access this key.
        Even if this new kms key is the same as the previous kms key id, block storage service will use it to regenerate a new volume encryption key.
        Example: `{\"kmsKeyId\": \"ocid1.key.region1.sea.afnl2n7daag4s.abzwkljs6uevhlgcznhmh7oiatyrxngrywc3tje3uk3g77hzmewqiieuk75f\"}`


        :return: The kms_key_id of this UpdateVolumeKmsKeyDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this UpdateVolumeKmsKeyDetails.
        The new kms key which will be used to protect the specific volume.
        This key has to be a valid kms key ocid, and user must have key delegation policy to allow them to access this key.
        Even if this new kms key is the same as the previous kms key id, block storage service will use it to regenerate a new volume encryption key.
        Example: `{\"kmsKeyId\": \"ocid1.key.region1.sea.afnl2n7daag4s.abzwkljs6uevhlgcznhmh7oiatyrxngrywc3tje3uk3g77hzmewqiieuk75f\"}`


        :param kms_key_id: The kms_key_id of this UpdateVolumeKmsKeyDetails.
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
