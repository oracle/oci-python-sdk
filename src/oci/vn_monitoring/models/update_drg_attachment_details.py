# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgAttachmentDetails(object):
    """
    UpdateDrgAttachmentDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDrgAttachmentDetails.
        :type display_name: str

        :param drg_route_table_id:
            The value to assign to the drg_route_table_id property of this UpdateDrgAttachmentDetails.
        :type drg_route_table_id: str

        :param network_details:
            The value to assign to the network_details property of this UpdateDrgAttachmentDetails.
        :type network_details: oci.vn_monitoring.models.DrgAttachmentNetworkUpdateDetails

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDrgAttachmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDrgAttachmentDetails.
        :type freeform_tags: dict(str, str)

        :param export_drg_route_distribution_id:
            The value to assign to the export_drg_route_distribution_id property of this UpdateDrgAttachmentDetails.
        :type export_drg_route_distribution_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'drg_route_table_id': 'str',
            'network_details': 'DrgAttachmentNetworkUpdateDetails',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'export_drg_route_distribution_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'drg_route_table_id': 'drgRouteTableId',
            'network_details': 'networkDetails',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'export_drg_route_distribution_id': 'exportDrgRouteDistributionId'
        }

        self._display_name = None
        self._drg_route_table_id = None
        self._network_details = None
        self._defined_tags = None
        self._freeform_tags = None
        self._export_drg_route_distribution_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateDrgAttachmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDrgAttachmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_route_table_id(self):
        """
        Gets the drg_route_table_id of this UpdateDrgAttachmentDetails.
        The `OCID`__ of the DRG route table that is assigned to this attachment.

        The DRG route table manages traffic inside the DRG.

        You can't remove a DRG route table from a DRG attachment, but you can reassign which
        DRG route table it uses.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_route_table_id of this UpdateDrgAttachmentDetails.
        :rtype: str
        """
        return self._drg_route_table_id

    @drg_route_table_id.setter
    def drg_route_table_id(self, drg_route_table_id):
        """
        Sets the drg_route_table_id of this UpdateDrgAttachmentDetails.
        The `OCID`__ of the DRG route table that is assigned to this attachment.

        The DRG route table manages traffic inside the DRG.

        You can't remove a DRG route table from a DRG attachment, but you can reassign which
        DRG route table it uses.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_route_table_id: The drg_route_table_id of this UpdateDrgAttachmentDetails.
        :type: str
        """
        self._drg_route_table_id = drg_route_table_id

    @property
    def network_details(self):
        """
        Gets the network_details of this UpdateDrgAttachmentDetails.

        :return: The network_details of this UpdateDrgAttachmentDetails.
        :rtype: oci.vn_monitoring.models.DrgAttachmentNetworkUpdateDetails
        """
        return self._network_details

    @network_details.setter
    def network_details(self, network_details):
        """
        Sets the network_details of this UpdateDrgAttachmentDetails.

        :param network_details: The network_details of this UpdateDrgAttachmentDetails.
        :type: oci.vn_monitoring.models.DrgAttachmentNetworkUpdateDetails
        """
        self._network_details = network_details

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDrgAttachmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDrgAttachmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDrgAttachmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDrgAttachmentDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDrgAttachmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDrgAttachmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDrgAttachmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDrgAttachmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def export_drg_route_distribution_id(self):
        """
        Gets the export_drg_route_distribution_id of this UpdateDrgAttachmentDetails.
        The `OCID`__ of the export route distribution used to specify how routes in the assigned DRG route table
        are advertised out through the attachment.
        If this value is null, no routes are advertised through this attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The export_drg_route_distribution_id of this UpdateDrgAttachmentDetails.
        :rtype: str
        """
        return self._export_drg_route_distribution_id

    @export_drg_route_distribution_id.setter
    def export_drg_route_distribution_id(self, export_drg_route_distribution_id):
        """
        Sets the export_drg_route_distribution_id of this UpdateDrgAttachmentDetails.
        The `OCID`__ of the export route distribution used to specify how routes in the assigned DRG route table
        are advertised out through the attachment.
        If this value is null, no routes are advertised through this attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param export_drg_route_distribution_id: The export_drg_route_distribution_id of this UpdateDrgAttachmentDetails.
        :type: str
        """
        self._export_drg_route_distribution_id = export_drg_route_distribution_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
