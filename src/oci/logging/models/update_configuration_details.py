# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigurationDetails(object):
    """
    The updatable configuration properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this UpdateConfigurationDetails.
        :type source: SourceUpdateDetails

        :param archiving:
            The value to assign to the archiving property of this UpdateConfigurationDetails.
        :type archiving: Archiving

        """
        self.swagger_types = {
            'source': 'SourceUpdateDetails',
            'archiving': 'Archiving'
        }

        self.attribute_map = {
            'source': 'source',
            'archiving': 'archiving'
        }

        self._source = None
        self._archiving = None

    @property
    def source(self):
        """
        **[Required]** Gets the source of this UpdateConfigurationDetails.

        :return: The source of this UpdateConfigurationDetails.
        :rtype: SourceUpdateDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this UpdateConfigurationDetails.

        :param source: The source of this UpdateConfigurationDetails.
        :type: SourceUpdateDetails
        """
        self._source = source

    @property
    def archiving(self):
        """
        Gets the archiving of this UpdateConfigurationDetails.

        :return: The archiving of this UpdateConfigurationDetails.
        :rtype: Archiving
        """
        return self._archiving

    @archiving.setter
    def archiving(self, archiving):
        """
        Sets the archiving of this UpdateConfigurationDetails.

        :param archiving: The archiving of this UpdateConfigurationDetails.
        :type: Archiving
        """
        self._archiving = archiving

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
