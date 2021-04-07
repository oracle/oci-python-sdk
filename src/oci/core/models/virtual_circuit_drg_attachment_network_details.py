# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .drg_attachment_network_details import DrgAttachmentNetworkDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCircuitDrgAttachmentNetworkDetails(DrgAttachmentNetworkDetails):
    """
    Specifies the virtual circuit attached to the DRG.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCircuitDrgAttachmentNetworkDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VirtualCircuitDrgAttachmentNetworkDetails.type` attribute
        of this class is ``VIRTUAL_CIRCUIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VirtualCircuitDrgAttachmentNetworkDetails.
            Allowed values for this property are: "VCN", "IPSEC_TUNNEL", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION"
        :type type: str

        :param id:
            The value to assign to the id property of this VirtualCircuitDrgAttachmentNetworkDetails.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None
        self._type = 'VIRTUAL_CIRCUIT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
