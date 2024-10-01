# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240815


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkDeleteSecurityAttributesDetails(object):
    """
    Properties for deleting security attributes in bulk.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkDeleteSecurityAttributesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param security_attribute_ids:
            The value to assign to the security_attribute_ids property of this BulkDeleteSecurityAttributesDetails.
        :type security_attribute_ids: list[str]

        """
        self.swagger_types = {
            'security_attribute_ids': 'list[str]'
        }

        self.attribute_map = {
            'security_attribute_ids': 'securityAttributeIds'
        }

        self._security_attribute_ids = None

    @property
    def security_attribute_ids(self):
        """
        **[Required]** Gets the security_attribute_ids of this BulkDeleteSecurityAttributesDetails.
        The OCIDs of the security attributes to delete.


        :return: The security_attribute_ids of this BulkDeleteSecurityAttributesDetails.
        :rtype: list[str]
        """
        return self._security_attribute_ids

    @security_attribute_ids.setter
    def security_attribute_ids(self, security_attribute_ids):
        """
        Sets the security_attribute_ids of this BulkDeleteSecurityAttributesDetails.
        The OCIDs of the security attributes to delete.


        :param security_attribute_ids: The security_attribute_ids of this BulkDeleteSecurityAttributesDetails.
        :type: list[str]
        """
        self._security_attribute_ids = security_attribute_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
