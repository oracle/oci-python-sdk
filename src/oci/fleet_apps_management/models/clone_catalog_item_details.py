# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloneCatalogItemDetails(object):
    """
    The configuration details for the clone operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloneCatalogItemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CloneCatalogItemDetails.
        :type compartment_id: str

        :param version_description:
            The value to assign to the version_description property of this CloneCatalogItemDetails.
        :type version_description: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'version_description': 'str'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'version_description': 'versionDescription'
        }
        self._compartment_id = None
        self._version_description = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CloneCatalogItemDetails.
        The `OCID`__ of the compartment to clone the CatalogItem to

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CloneCatalogItemDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloneCatalogItemDetails.
        The `OCID`__ of the compartment to clone the CatalogItem to

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CloneCatalogItemDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def version_description(self):
        """
        Gets the version_description of this CloneCatalogItemDetails.
        Version description about the catalog item.


        :return: The version_description of this CloneCatalogItemDetails.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        """
        Sets the version_description of this CloneCatalogItemDetails.
        Version description about the catalog item.


        :param version_description: The version_description of this CloneCatalogItemDetails.
        :type: str
        """
        self._version_description = version_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
