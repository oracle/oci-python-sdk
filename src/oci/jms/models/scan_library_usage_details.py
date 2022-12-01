# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScanLibraryUsageDetails(object):
    """
    The list of managed instances to scan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScanLibraryUsageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this ScanLibraryUsageDetails.
        :type managed_instance_ids: list[str]

        """
        self.swagger_types = {
            'managed_instance_ids': 'list[str]'
        }

        self.attribute_map = {
            'managed_instance_ids': 'managedInstanceIds'
        }

        self._managed_instance_ids = None

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this ScanLibraryUsageDetails.
        The list of `OCIDs`__ of managed instances to scan.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_ids of this ScanLibraryUsageDetails.
        :rtype: list[str]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this ScanLibraryUsageDetails.
        The list of `OCIDs`__ of managed instances to scan.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_instance_ids: The managed_instance_ids of this ScanLibraryUsageDetails.
        :type: list[str]
        """
        self._managed_instance_ids = managed_instance_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
