# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodePoolPodNetworkOptionDetails(object):
    """
    The CNI type and relevant network details for the pods of a given node pool
    """

    #: A constant which can be used with the cni_type property of a NodePoolPodNetworkOptionDetails.
    #: This constant has a value of "OCI_VCN_IP_NATIVE"
    CNI_TYPE_OCI_VCN_IP_NATIVE = "OCI_VCN_IP_NATIVE"

    #: A constant which can be used with the cni_type property of a NodePoolPodNetworkOptionDetails.
    #: This constant has a value of "FLANNEL_OVERLAY"
    CNI_TYPE_FLANNEL_OVERLAY = "FLANNEL_OVERLAY"

    def __init__(self, **kwargs):
        """
        Initializes a new NodePoolPodNetworkOptionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.container_engine.models.OciVcnIpNativeNodePoolPodNetworkOptionDetails`
        * :class:`~oci.container_engine.models.FlannelOverlayNodePoolPodNetworkOptionDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cni_type:
            The value to assign to the cni_type property of this NodePoolPodNetworkOptionDetails.
            Allowed values for this property are: "OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cni_type: str

        """
        self.swagger_types = {
            'cni_type': 'str'
        }

        self.attribute_map = {
            'cni_type': 'cniType'
        }

        self._cni_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['cniType']

        if type == 'OCI_VCN_IP_NATIVE':
            return 'OciVcnIpNativeNodePoolPodNetworkOptionDetails'

        if type == 'FLANNEL_OVERLAY':
            return 'FlannelOverlayNodePoolPodNetworkOptionDetails'
        else:
            return 'NodePoolPodNetworkOptionDetails'

    @property
    def cni_type(self):
        """
        **[Required]** Gets the cni_type of this NodePoolPodNetworkOptionDetails.
        The CNI plugin used by this node pool

        Allowed values for this property are: "OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cni_type of this NodePoolPodNetworkOptionDetails.
        :rtype: str
        """
        return self._cni_type

    @cni_type.setter
    def cni_type(self, cni_type):
        """
        Sets the cni_type of this NodePoolPodNetworkOptionDetails.
        The CNI plugin used by this node pool


        :param cni_type: The cni_type of this NodePoolPodNetworkOptionDetails.
        :type: str
        """
        allowed_values = ["OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY"]
        if not value_allowed_none_or_none_sentinel(cni_type, allowed_values):
            cni_type = 'UNKNOWN_ENUM_VALUE'
        self._cni_type = cni_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
