# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityZoneTargetDetails(TargetDetails):
    """
    Details about Security Zone Target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityZoneTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.SecurityZoneTargetDetails.target_resource_type` attribute
        of this class is ``SECURITY_ZONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_resource_type:
            The value to assign to the target_resource_type property of this SecurityZoneTargetDetails.
            Allowed values for this property are: "COMPARTMENT", "ERPCLOUD", "HCMCLOUD", "SECURITY_ZONE"
        :type target_resource_type: str

        :param security_zone_id:
            The value to assign to the security_zone_id property of this SecurityZoneTargetDetails.
        :type security_zone_id: str

        :param security_zone_display_name:
            The value to assign to the security_zone_display_name property of this SecurityZoneTargetDetails.
        :type security_zone_display_name: str

        :param target_security_zone_recipes:
            The value to assign to the target_security_zone_recipes property of this SecurityZoneTargetDetails.
        :type target_security_zone_recipes: list[oci.cloud_guard.models.SecurityRecipe]

        """
        self.swagger_types = {
            'target_resource_type': 'str',
            'security_zone_id': 'str',
            'security_zone_display_name': 'str',
            'target_security_zone_recipes': 'list[SecurityRecipe]'
        }

        self.attribute_map = {
            'target_resource_type': 'targetResourceType',
            'security_zone_id': 'securityZoneId',
            'security_zone_display_name': 'securityZoneDisplayName',
            'target_security_zone_recipes': 'targetSecurityZoneRecipes'
        }

        self._target_resource_type = None
        self._security_zone_id = None
        self._security_zone_display_name = None
        self._target_security_zone_recipes = None
        self._target_resource_type = 'SECURITY_ZONE'

    @property
    def security_zone_id(self):
        """
        Gets the security_zone_id of this SecurityZoneTargetDetails.
        The OCID of the security zone to associate this compartment with.


        :return: The security_zone_id of this SecurityZoneTargetDetails.
        :rtype: str
        """
        return self._security_zone_id

    @security_zone_id.setter
    def security_zone_id(self, security_zone_id):
        """
        Sets the security_zone_id of this SecurityZoneTargetDetails.
        The OCID of the security zone to associate this compartment with.


        :param security_zone_id: The security_zone_id of this SecurityZoneTargetDetails.
        :type: str
        """
        self._security_zone_id = security_zone_id

    @property
    def security_zone_display_name(self):
        """
        Gets the security_zone_display_name of this SecurityZoneTargetDetails.
        The name of the security zone to associate this compartment with.


        :return: The security_zone_display_name of this SecurityZoneTargetDetails.
        :rtype: str
        """
        return self._security_zone_display_name

    @security_zone_display_name.setter
    def security_zone_display_name(self, security_zone_display_name):
        """
        Sets the security_zone_display_name of this SecurityZoneTargetDetails.
        The name of the security zone to associate this compartment with.


        :param security_zone_display_name: The security_zone_display_name of this SecurityZoneTargetDetails.
        :type: str
        """
        self._security_zone_display_name = security_zone_display_name

    @property
    def target_security_zone_recipes(self):
        """
        Gets the target_security_zone_recipes of this SecurityZoneTargetDetails.
        The list of security zone recipes to associate this compartment with.


        :return: The target_security_zone_recipes of this SecurityZoneTargetDetails.
        :rtype: list[oci.cloud_guard.models.SecurityRecipe]
        """
        return self._target_security_zone_recipes

    @target_security_zone_recipes.setter
    def target_security_zone_recipes(self, target_security_zone_recipes):
        """
        Sets the target_security_zone_recipes of this SecurityZoneTargetDetails.
        The list of security zone recipes to associate this compartment with.


        :param target_security_zone_recipes: The target_security_zone_recipes of this SecurityZoneTargetDetails.
        :type: list[oci.cloud_guard.models.SecurityRecipe]
        """
        self._target_security_zone_recipes = target_security_zone_recipes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
