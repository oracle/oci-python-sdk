# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DowngradeHcxDetails(object):
    """
    The HCX on-premise license keys to be reserved when downgrading from HCX Enterprise to HCX Advanced.
    Downgrading from HCX Enterprise to HCX Advanced reduces the number of provided license keys from 10 to 3.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DowngradeHcxDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reserving_hcx_on_premise_license_keys:
            The value to assign to the reserving_hcx_on_premise_license_keys property of this DowngradeHcxDetails.
        :type reserving_hcx_on_premise_license_keys: list[str]

        """
        self.swagger_types = {
            'reserving_hcx_on_premise_license_keys': 'list[str]'
        }

        self.attribute_map = {
            'reserving_hcx_on_premise_license_keys': 'reservingHcxOnPremiseLicenseKeys'
        }

        self._reserving_hcx_on_premise_license_keys = None

    @property
    def reserving_hcx_on_premise_license_keys(self):
        """
        **[Required]** Gets the reserving_hcx_on_premise_license_keys of this DowngradeHcxDetails.
        The HCX on-premise license keys to be reserved when downgrading from HCX Enterprise to HCX Advanced.


        :return: The reserving_hcx_on_premise_license_keys of this DowngradeHcxDetails.
        :rtype: list[str]
        """
        return self._reserving_hcx_on_premise_license_keys

    @reserving_hcx_on_premise_license_keys.setter
    def reserving_hcx_on_premise_license_keys(self, reserving_hcx_on_premise_license_keys):
        """
        Sets the reserving_hcx_on_premise_license_keys of this DowngradeHcxDetails.
        The HCX on-premise license keys to be reserved when downgrading from HCX Enterprise to HCX Advanced.


        :param reserving_hcx_on_premise_license_keys: The reserving_hcx_on_premise_license_keys of this DowngradeHcxDetails.
        :type: list[str]
        """
        self._reserving_hcx_on_premise_license_keys = reserving_hcx_on_premise_license_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
