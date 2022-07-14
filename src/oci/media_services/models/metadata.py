# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Metadata(object):
    """
    Technical metadata for this asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Metadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metadata:
            The value to assign to the metadata property of this Metadata.
        :type metadata: str

        """
        self.swagger_types = {
            'metadata': 'str'
        }

        self.attribute_map = {
            'metadata': 'metadata'
        }

        self._metadata = None

    @property
    def metadata(self):
        """
        **[Required]** Gets the metadata of this Metadata.
        JSON string containing the technial metadata for the media asset.


        :return: The metadata of this Metadata.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Metadata.
        JSON string containing the technial metadata for the media asset.


        :param metadata: The metadata of this Metadata.
        :type: str
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
