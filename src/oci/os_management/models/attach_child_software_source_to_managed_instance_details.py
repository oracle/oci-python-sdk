# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachChildSoftwareSourceToManagedInstanceDetails(object):
    """
    Information for attaching a software source to a managed instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachChildSoftwareSourceToManagedInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param software_source_id:
            The value to assign to the software_source_id property of this AttachChildSoftwareSourceToManagedInstanceDetails.
        :type software_source_id: str

        """
        self.swagger_types = {
            'software_source_id': 'str'
        }
        self.attribute_map = {
            'software_source_id': 'softwareSourceId'
        }
        self._software_source_id = None

    @property
    def software_source_id(self):
        """
        **[Required]** Gets the software_source_id of this AttachChildSoftwareSourceToManagedInstanceDetails.
        OCID for the Software Source


        :return: The software_source_id of this AttachChildSoftwareSourceToManagedInstanceDetails.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this AttachChildSoftwareSourceToManagedInstanceDetails.
        OCID for the Software Source


        :param software_source_id: The software_source_id of this AttachChildSoftwareSourceToManagedInstanceDetails.
        :type: str
        """
        self._software_source_id = software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
