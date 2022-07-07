# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .cluster_pod_network_option_details import ClusterPodNetworkOptionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FlannelOverlayClusterPodNetworkOptionDetails(ClusterPodNetworkOptionDetails):
    """
    Network options specific to using the flannel (FLANNEL_OVERLAY) CNI
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FlannelOverlayClusterPodNetworkOptionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_engine.models.FlannelOverlayClusterPodNetworkOptionDetails.cni_type` attribute
        of this class is ``FLANNEL_OVERLAY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cni_type:
            The value to assign to the cni_type property of this FlannelOverlayClusterPodNetworkOptionDetails.
            Allowed values for this property are: "OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY"
        :type cni_type: str

        """
        self.swagger_types = {
            'cni_type': 'str'
        }

        self.attribute_map = {
            'cni_type': 'cniType'
        }

        self._cni_type = None
        self._cni_type = 'FLANNEL_OVERLAY'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
