# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmwareVCenterProperties(object):
    """
    VMware vCenter related properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmwareVCenterProperties object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcenter_key:
            The value to assign to the vcenter_key property of this VmwareVCenterProperties.
        :type vcenter_key: str

        :param vcenter_version:
            The value to assign to the vcenter_version property of this VmwareVCenterProperties.
        :type vcenter_version: str

        :param data_center:
            The value to assign to the data_center property of this VmwareVCenterProperties.
        :type data_center: str

        """
        self.swagger_types = {
            'vcenter_key': 'str',
            'vcenter_version': 'str',
            'data_center': 'str'
        }

        self.attribute_map = {
            'vcenter_key': 'vcenterKey',
            'vcenter_version': 'vcenterVersion',
            'data_center': 'dataCenter'
        }

        self._vcenter_key = None
        self._vcenter_version = None
        self._data_center = None

    @property
    def vcenter_key(self):
        """
        Gets the vcenter_key of this VmwareVCenterProperties.
        vCenter unique key.


        :return: The vcenter_key of this VmwareVCenterProperties.
        :rtype: str
        """
        return self._vcenter_key

    @vcenter_key.setter
    def vcenter_key(self, vcenter_key):
        """
        Sets the vcenter_key of this VmwareVCenterProperties.
        vCenter unique key.


        :param vcenter_key: The vcenter_key of this VmwareVCenterProperties.
        :type: str
        """
        self._vcenter_key = vcenter_key

    @property
    def vcenter_version(self):
        """
        Gets the vcenter_version of this VmwareVCenterProperties.
        Dot-separated version string.


        :return: The vcenter_version of this VmwareVCenterProperties.
        :rtype: str
        """
        return self._vcenter_version

    @vcenter_version.setter
    def vcenter_version(self, vcenter_version):
        """
        Sets the vcenter_version of this VmwareVCenterProperties.
        Dot-separated version string.


        :param vcenter_version: The vcenter_version of this VmwareVCenterProperties.
        :type: str
        """
        self._vcenter_version = vcenter_version

    @property
    def data_center(self):
        """
        Gets the data_center of this VmwareVCenterProperties.
        Data center name.


        :return: The data_center of this VmwareVCenterProperties.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """
        Sets the data_center of this VmwareVCenterProperties.
        Data center name.


        :param data_center: The data_center of this VmwareVCenterProperties.
        :type: str
        """
        self._data_center = data_center

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
