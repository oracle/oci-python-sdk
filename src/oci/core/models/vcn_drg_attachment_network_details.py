# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .drg_attachment_network_details import DrgAttachmentNetworkDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VcnDrgAttachmentNetworkDetails(DrgAttachmentNetworkDetails):
    """
    Specifies details within the VCN.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VcnDrgAttachmentNetworkDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VcnDrgAttachmentNetworkDetails.type` attribute
        of this class is ``VCN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VcnDrgAttachmentNetworkDetails.
            Allowed values for this property are: "VCN", "IPSEC_TUNNEL", "VIRTUAL_CIRCUIT", "REMOTE_PEERING_CONNECTION"
        :type type: str

        :param id:
            The value to assign to the id property of this VcnDrgAttachmentNetworkDetails.
        :type id: str

        :param route_table_id:
            The value to assign to the route_table_id property of this VcnDrgAttachmentNetworkDetails.
        :type route_table_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'route_table_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'route_table_id': 'routeTableId'
        }

        self._type = None
        self._id = None
        self._route_table_id = None
        self._type = 'VCN'

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this VcnDrgAttachmentNetworkDetails.
        The `OCID`__ of the route table the DRG attachment is using.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this VcnDrgAttachmentNetworkDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this VcnDrgAttachmentNetworkDetails.
        The `OCID`__ of the route table the DRG attachment is using.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this VcnDrgAttachmentNetworkDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
