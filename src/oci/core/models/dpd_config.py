# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DpdConfig(object):
    """
    These configuration details are used for dead peer detection (DPD). DPD periodically checks the stability of the connection to the customer premises (CPE), and may be used to detect that the link to the CPE has gone down.
    """

    #: A constant which can be used with the dpd_mode property of a DpdConfig.
    #: This constant has a value of "INITIATE_AND_RESPOND"
    DPD_MODE_INITIATE_AND_RESPOND = "INITIATE_AND_RESPOND"

    #: A constant which can be used with the dpd_mode property of a DpdConfig.
    #: This constant has a value of "RESPOND_ONLY"
    DPD_MODE_RESPOND_ONLY = "RESPOND_ONLY"

    def __init__(self, **kwargs):
        """
        Initializes a new DpdConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dpd_mode:
            The value to assign to the dpd_mode property of this DpdConfig.
            Allowed values for this property are: "INITIATE_AND_RESPOND", "RESPOND_ONLY"
        :type dpd_mode: str

        :param dpd_timeout_in_sec:
            The value to assign to the dpd_timeout_in_sec property of this DpdConfig.
        :type dpd_timeout_in_sec: int

        """
        self.swagger_types = {
            'dpd_mode': 'str',
            'dpd_timeout_in_sec': 'int'
        }

        self.attribute_map = {
            'dpd_mode': 'dpdMode',
            'dpd_timeout_in_sec': 'dpdTimeoutInSec'
        }

        self._dpd_mode = None
        self._dpd_timeout_in_sec = None

    @property
    def dpd_mode(self):
        """
        Gets the dpd_mode of this DpdConfig.
        This option defines whether DPD can be initiated from the Oracle side of the connection.

        Allowed values for this property are: "INITIATE_AND_RESPOND", "RESPOND_ONLY"


        :return: The dpd_mode of this DpdConfig.
        :rtype: str
        """
        return self._dpd_mode

    @dpd_mode.setter
    def dpd_mode(self, dpd_mode):
        """
        Sets the dpd_mode of this DpdConfig.
        This option defines whether DPD can be initiated from the Oracle side of the connection.


        :param dpd_mode: The dpd_mode of this DpdConfig.
        :type: str
        """
        allowed_values = ["INITIATE_AND_RESPOND", "RESPOND_ONLY"]
        if not value_allowed_none_or_none_sentinel(dpd_mode, allowed_values):
            raise ValueError(
                "Invalid value for `dpd_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._dpd_mode = dpd_mode

    @property
    def dpd_timeout_in_sec(self):
        """
        Gets the dpd_timeout_in_sec of this DpdConfig.
        DPD timeout in seconds. This sets the longest interval between CPE device health messages before the IPSec connection indicates it has lost contact with the CPE. The default is 20 seconds.


        :return: The dpd_timeout_in_sec of this DpdConfig.
        :rtype: int
        """
        return self._dpd_timeout_in_sec

    @dpd_timeout_in_sec.setter
    def dpd_timeout_in_sec(self, dpd_timeout_in_sec):
        """
        Sets the dpd_timeout_in_sec of this DpdConfig.
        DPD timeout in seconds. This sets the longest interval between CPE device health messages before the IPSec connection indicates it has lost contact with the CPE. The default is 20 seconds.


        :param dpd_timeout_in_sec: The dpd_timeout_in_sec of this DpdConfig.
        :type: int
        """
        self._dpd_timeout_in_sec = dpd_timeout_in_sec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
