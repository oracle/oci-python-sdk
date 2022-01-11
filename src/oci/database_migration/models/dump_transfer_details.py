# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DumpTransferDetails(object):
    """
    Optional additional properties for dump transfer.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DumpTransferDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this DumpTransferDetails.
        :type source: oci.database_migration.models.HostDumpTransferDetails

        :param target:
            The value to assign to the target property of this DumpTransferDetails.
        :type target: oci.database_migration.models.HostDumpTransferDetails

        """
        self.swagger_types = {
            'source': 'HostDumpTransferDetails',
            'target': 'HostDumpTransferDetails'
        }

        self.attribute_map = {
            'source': 'source',
            'target': 'target'
        }

        self._source = None
        self._target = None

    @property
    def source(self):
        """
        Gets the source of this DumpTransferDetails.

        :return: The source of this DumpTransferDetails.
        :rtype: oci.database_migration.models.HostDumpTransferDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DumpTransferDetails.

        :param source: The source of this DumpTransferDetails.
        :type: oci.database_migration.models.HostDumpTransferDetails
        """
        self._source = source

    @property
    def target(self):
        """
        Gets the target of this DumpTransferDetails.

        :return: The target of this DumpTransferDetails.
        :rtype: oci.database_migration.models.HostDumpTransferDetails
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this DumpTransferDetails.

        :param target: The target of this DumpTransferDetails.
        :type: oci.database_migration.models.HostDumpTransferDetails
        """
        self._target = target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
