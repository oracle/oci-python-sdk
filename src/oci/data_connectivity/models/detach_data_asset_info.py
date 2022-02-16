# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetachDataAssetInfo(object):
    """
    The detach DataAsset response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetachDataAssetInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference_info:
            The value to assign to the reference_info property of this DetachDataAssetInfo.
        :type reference_info: dict(str, ValidationResult)

        """
        self.swagger_types = {
            'reference_info': 'dict(str, ValidationResult)'
        }

        self.attribute_map = {
            'reference_info': 'referenceInfo'
        }

        self._reference_info = None

    @property
    def reference_info(self):
        """
        **[Required]** Gets the reference_info of this DetachDataAssetInfo.
        Map of DataAsset name as key and results as value


        :return: The reference_info of this DetachDataAssetInfo.
        :rtype: dict(str, ValidationResult)
        """
        return self._reference_info

    @reference_info.setter
    def reference_info(self, reference_info):
        """
        Sets the reference_info of this DetachDataAssetInfo.
        Map of DataAsset name as key and results as value


        :param reference_info: The reference_info of this DetachDataAssetInfo.
        :type: dict(str, ValidationResult)
        """
        self._reference_info = reference_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
