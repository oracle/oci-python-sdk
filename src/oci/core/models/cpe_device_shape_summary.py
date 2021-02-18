# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CpeDeviceShapeSummary(object):
    """
    A summary of information about a particular CPE device type. Compare with
    :class:`CpeDeviceShapeDetail`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CpeDeviceShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CpeDeviceShapeSummary.
        :type id: str

        :param cpe_device_info:
            The value to assign to the cpe_device_info property of this CpeDeviceShapeSummary.
        :type cpe_device_info: oci.core.models.CpeDeviceInfo

        """
        self.swagger_types = {
            'id': 'str',
            'cpe_device_info': 'CpeDeviceInfo'
        }

        self.attribute_map = {
            'id': 'id',
            'cpe_device_info': 'cpeDeviceInfo'
        }

        self._id = None
        self._cpe_device_info = None

    @property
    def id(self):
        """
        Gets the id of this CpeDeviceShapeSummary.
        The `OCID`__ of the CPE device shape.
        This value uniquely identifies the type of CPE device.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this CpeDeviceShapeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CpeDeviceShapeSummary.
        The `OCID`__ of the CPE device shape.
        This value uniquely identifies the type of CPE device.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this CpeDeviceShapeSummary.
        :type: str
        """
        self._id = id

    @property
    def cpe_device_info(self):
        """
        Gets the cpe_device_info of this CpeDeviceShapeSummary.

        :return: The cpe_device_info of this CpeDeviceShapeSummary.
        :rtype: oci.core.models.CpeDeviceInfo
        """
        return self._cpe_device_info

    @cpe_device_info.setter
    def cpe_device_info(self, cpe_device_info):
        """
        Sets the cpe_device_info of this CpeDeviceShapeSummary.

        :param cpe_device_info: The cpe_device_info of this CpeDeviceShapeSummary.
        :type: oci.core.models.CpeDeviceInfo
        """
        self._cpe_device_info = cpe_device_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
