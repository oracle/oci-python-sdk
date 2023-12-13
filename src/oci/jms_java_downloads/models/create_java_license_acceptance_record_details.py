# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJavaLicenseAcceptanceRecordDetails(object):
    """
    The attributes to create a new JavaLicenseAcceptanceRecord.
    """

    #: A constant which can be used with the license_type property of a CreateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "OTN"
    LICENSE_TYPE_OTN = "OTN"

    #: A constant which can be used with the license_type property of a CreateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "NFTC"
    LICENSE_TYPE_NFTC = "NFTC"

    #: A constant which can be used with the license_type property of a CreateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "RESTRICTED"
    LICENSE_TYPE_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the license_acceptance_status property of a CreateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "ACCEPTED"
    LICENSE_ACCEPTANCE_STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the license_acceptance_status property of a CreateJavaLicenseAcceptanceRecordDetails.
    #: This constant has a value of "REVOKED"
    LICENSE_ACCEPTANCE_STATUS_REVOKED = "REVOKED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJavaLicenseAcceptanceRecordDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateJavaLicenseAcceptanceRecordDetails.
        :type compartment_id: str

        :param license_type:
            The value to assign to the license_type property of this CreateJavaLicenseAcceptanceRecordDetails.
            Allowed values for this property are: "OTN", "NFTC", "RESTRICTED"
        :type license_type: str

        :param license_acceptance_status:
            The value to assign to the license_acceptance_status property of this CreateJavaLicenseAcceptanceRecordDetails.
            Allowed values for this property are: "ACCEPTED", "REVOKED"
        :type license_acceptance_status: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'license_type': 'str',
            'license_acceptance_status': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'license_type': 'licenseType',
            'license_acceptance_status': 'licenseAcceptanceStatus'
        }

        self._compartment_id = None
        self._license_type = None
        self._license_acceptance_status = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateJavaLicenseAcceptanceRecordDetails.
        The tenancy `OCID`__ of the user accepting the license.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateJavaLicenseAcceptanceRecordDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateJavaLicenseAcceptanceRecordDetails.
        The tenancy `OCID`__ of the user accepting the license.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateJavaLicenseAcceptanceRecordDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this CreateJavaLicenseAcceptanceRecordDetails.
        License type for the Java version.

        Allowed values for this property are: "OTN", "NFTC", "RESTRICTED"


        :return: The license_type of this CreateJavaLicenseAcceptanceRecordDetails.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this CreateJavaLicenseAcceptanceRecordDetails.
        License type for the Java version.


        :param license_type: The license_type of this CreateJavaLicenseAcceptanceRecordDetails.
        :type: str
        """
        allowed_values = ["OTN", "NFTC", "RESTRICTED"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            raise ValueError(
                f"Invalid value for `license_type`, must be None or one of {allowed_values}"
            )
        self._license_type = license_type

    @property
    def license_acceptance_status(self):
        """
        **[Required]** Gets the license_acceptance_status of this CreateJavaLicenseAcceptanceRecordDetails.
        Status of license acceptance.

        Allowed values for this property are: "ACCEPTED", "REVOKED"


        :return: The license_acceptance_status of this CreateJavaLicenseAcceptanceRecordDetails.
        :rtype: str
        """
        return self._license_acceptance_status

    @license_acceptance_status.setter
    def license_acceptance_status(self, license_acceptance_status):
        """
        Sets the license_acceptance_status of this CreateJavaLicenseAcceptanceRecordDetails.
        Status of license acceptance.


        :param license_acceptance_status: The license_acceptance_status of this CreateJavaLicenseAcceptanceRecordDetails.
        :type: str
        """
        allowed_values = ["ACCEPTED", "REVOKED"]
        if not value_allowed_none_or_none_sentinel(license_acceptance_status, allowed_values):
            raise ValueError(
                f"Invalid value for `license_acceptance_status`, must be None or one of {allowed_values}"
            )
        self._license_acceptance_status = license_acceptance_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
