# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudAutonomousVmClusterResourceDetails(object):
    """
    Unallocated resource details of the CAVM
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudAutonomousVmClusterResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CloudAutonomousVmClusterResourceDetails.
        :type id: str

        :param un_allocated_adb_storage_in_tbs:
            The value to assign to the un_allocated_adb_storage_in_tbs property of this CloudAutonomousVmClusterResourceDetails.
        :type un_allocated_adb_storage_in_tbs: float

        """
        self.swagger_types = {
            'id': 'str',
            'un_allocated_adb_storage_in_tbs': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'un_allocated_adb_storage_in_tbs': 'unAllocatedAdbStorageInTBs'
        }

        self._id = None
        self._un_allocated_adb_storage_in_tbs = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CloudAutonomousVmClusterResourceDetails.
        The `OCID`__ of the Cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this CloudAutonomousVmClusterResourceDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudAutonomousVmClusterResourceDetails.
        The `OCID`__ of the Cloud Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this CloudAutonomousVmClusterResourceDetails.
        :type: str
        """
        self._id = id

    @property
    def un_allocated_adb_storage_in_tbs(self):
        """
        **[Required]** Gets the un_allocated_adb_storage_in_tbs of this CloudAutonomousVmClusterResourceDetails.
        Total unallocated autonomous data storage in the CAVM in TBs.


        :return: The un_allocated_adb_storage_in_tbs of this CloudAutonomousVmClusterResourceDetails.
        :rtype: float
        """
        return self._un_allocated_adb_storage_in_tbs

    @un_allocated_adb_storage_in_tbs.setter
    def un_allocated_adb_storage_in_tbs(self, un_allocated_adb_storage_in_tbs):
        """
        Sets the un_allocated_adb_storage_in_tbs of this CloudAutonomousVmClusterResourceDetails.
        Total unallocated autonomous data storage in the CAVM in TBs.


        :param un_allocated_adb_storage_in_tbs: The un_allocated_adb_storage_in_tbs of this CloudAutonomousVmClusterResourceDetails.
        :type: float
        """
        self._un_allocated_adb_storage_in_tbs = un_allocated_adb_storage_in_tbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
