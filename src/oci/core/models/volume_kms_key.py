# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeKmsKey(object):
    """
    Kms key id associated with this volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeKmsKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this VolumeKmsKey.
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
        Gets the kms_key_id of this VolumeKmsKey.
        Kms key id associated with this volume. If volume is not using KMS, then kmsKeyId will be null string.


        :return: The kms_key_id of this VolumeKmsKey.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this VolumeKmsKey.
        Kms key id associated with this volume. If volume is not using KMS, then kmsKeyId will be null string.


        :param kms_key_id: The kms_key_id of this VolumeKmsKey.
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
