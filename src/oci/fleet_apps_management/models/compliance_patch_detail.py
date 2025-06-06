# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompliancePatchDetail(object):
    """
    Details of the Patch.
    """

    #: A constant which can be used with the severity property of a CompliancePatchDetail.
    #: This constant has a value of "CRITICAL"
    SEVERITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the severity property of a CompliancePatchDetail.
    #: This constant has a value of "HIGH"
    SEVERITY_HIGH = "HIGH"

    #: A constant which can be used with the severity property of a CompliancePatchDetail.
    #: This constant has a value of "MEDIUM"
    SEVERITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the severity property of a CompliancePatchDetail.
    #: This constant has a value of "LOW"
    SEVERITY_LOW = "LOW"

    def __init__(self, **kwargs):
        """
        Initializes a new CompliancePatchDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patch_id:
            The value to assign to the patch_id property of this CompliancePatchDetail.
        :type patch_id: str

        :param patch_name:
            The value to assign to the patch_name property of this CompliancePatchDetail.
        :type patch_name: str

        :param patch_description:
            The value to assign to the patch_description property of this CompliancePatchDetail.
        :type patch_description: str

        :param time_released:
            The value to assign to the time_released property of this CompliancePatchDetail.
        :type time_released: datetime

        :param patch_type:
            The value to assign to the patch_type property of this CompliancePatchDetail.
        :type patch_type: str

        :param severity:
            The value to assign to the severity property of this CompliancePatchDetail.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param product:
            The value to assign to the product property of this CompliancePatchDetail.
        :type product: oci.fleet_apps_management.models.ComplianceDetailProduct

        """
        self.swagger_types = {
            'patch_id': 'str',
            'patch_name': 'str',
            'patch_description': 'str',
            'time_released': 'datetime',
            'patch_type': 'str',
            'severity': 'str',
            'product': 'ComplianceDetailProduct'
        }
        self.attribute_map = {
            'patch_id': 'patchId',
            'patch_name': 'patchName',
            'patch_description': 'patchDescription',
            'time_released': 'timeReleased',
            'patch_type': 'patchType',
            'severity': 'severity',
            'product': 'product'
        }
        self._patch_id = None
        self._patch_name = None
        self._patch_description = None
        self._time_released = None
        self._patch_type = None
        self._severity = None
        self._product = None

    @property
    def patch_id(self):
        """
        Gets the patch_id of this CompliancePatchDetail.
        patch OCID.


        :return: The patch_id of this CompliancePatchDetail.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this CompliancePatchDetail.
        patch OCID.


        :param patch_id: The patch_id of this CompliancePatchDetail.
        :type: str
        """
        self._patch_id = patch_id

    @property
    def patch_name(self):
        """
        **[Required]** Gets the patch_name of this CompliancePatchDetail.
        patch Name.


        :return: The patch_name of this CompliancePatchDetail.
        :rtype: str
        """
        return self._patch_name

    @patch_name.setter
    def patch_name(self, patch_name):
        """
        Sets the patch_name of this CompliancePatchDetail.
        patch Name.


        :param patch_name: The patch_name of this CompliancePatchDetail.
        :type: str
        """
        self._patch_name = patch_name

    @property
    def patch_description(self):
        """
        Gets the patch_description of this CompliancePatchDetail.
        Patch Description.


        :return: The patch_description of this CompliancePatchDetail.
        :rtype: str
        """
        return self._patch_description

    @patch_description.setter
    def patch_description(self, patch_description):
        """
        Sets the patch_description of this CompliancePatchDetail.
        Patch Description.


        :param patch_description: The patch_description of this CompliancePatchDetail.
        :type: str
        """
        self._patch_description = patch_description

    @property
    def time_released(self):
        """
        Gets the time_released of this CompliancePatchDetail.
        Date on which patch was released


        :return: The time_released of this CompliancePatchDetail.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this CompliancePatchDetail.
        Date on which patch was released


        :param time_released: The time_released of this CompliancePatchDetail.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def patch_type(self):
        """
        **[Required]** Gets the patch_type of this CompliancePatchDetail.
        Type of patch.


        :return: The patch_type of this CompliancePatchDetail.
        :rtype: str
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """
        Sets the patch_type of this CompliancePatchDetail.
        Type of patch.


        :param patch_type: The patch_type of this CompliancePatchDetail.
        :type: str
        """
        self._patch_type = patch_type

    @property
    def severity(self):
        """
        Gets the severity of this CompliancePatchDetail.
        Patch Severity.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this CompliancePatchDetail.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this CompliancePatchDetail.
        Patch Severity.


        :param severity: The severity of this CompliancePatchDetail.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def product(self):
        """
        Gets the product of this CompliancePatchDetail.

        :return: The product of this CompliancePatchDetail.
        :rtype: oci.fleet_apps_management.models.ComplianceDetailProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this CompliancePatchDetail.

        :param product: The product of this CompliancePatchDetail.
        :type: oci.fleet_apps_management.models.ComplianceDetailProduct
        """
        self._product = product

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
