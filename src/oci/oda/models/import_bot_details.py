# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportBotDetails(object):
    """
    Properties to import a Bot resource from Object Storage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportBotDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this ImportBotDetails.
        :type source: oci.oda.models.StorageLocation

        """
        self.swagger_types = {
            'source': 'StorageLocation'
        }

        self.attribute_map = {
            'source': 'source'
        }

        self._source = None

    @property
    def source(self):
        """
        **[Required]** Gets the source of this ImportBotDetails.

        :return: The source of this ImportBotDetails.
        :rtype: oci.oda.models.StorageLocation
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ImportBotDetails.

        :param source: The source of this ImportBotDetails.
        :type: oci.oda.models.StorageLocation
        """
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
