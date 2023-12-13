# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableExternalExadataInfrastructureManagementDetails(object):
    """
    The details required to enable Database Management on the Exadata infrastructure.
    """

    #: A constant which can be used with the license_model property of a EnableExternalExadataInfrastructureManagementDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a EnableExternalExadataInfrastructureManagementDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new EnableExternalExadataInfrastructureManagementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param license_model:
            The value to assign to the license_model property of this EnableExternalExadataInfrastructureManagementDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        """
        self.swagger_types = {
            'license_model': 'str'
        }

        self.attribute_map = {
            'license_model': 'licenseModel'
        }

        self._license_model = None

    @property
    def license_model(self):
        """
        **[Required]** Gets the license_model of this EnableExternalExadataInfrastructureManagementDetails.
        The Oracle license model.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this EnableExternalExadataInfrastructureManagementDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this EnableExternalExadataInfrastructureManagementDetails.
        The Oracle license model.


        :param license_model: The license_model of this EnableExternalExadataInfrastructureManagementDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                f"Invalid value for `license_model`, must be None or one of {allowed_values}"
            )
        self._license_model = license_model

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
