# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgAttachment(object):
    """
    A DRG attachment serves as a link between a DRG and a network resource. A DRG can be attached to a VCN,
    IPSec tunnel, remote peering connection, or virtual circuit.

    For more information, see `Overview of the Networking Service`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "ATTACHED"
    LIFECYCLE_STATE_ATTACHED = "ATTACHED"

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a DrgAttachment.
    #: This constant has a value of "DETACHED"
    LIFECYCLE_STATE_DETACHED = "DETACHED"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DrgAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DrgAttachment.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this DrgAttachment.
        :type drg_id: str

        :param id:
            The value to assign to the id property of this DrgAttachment.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DrgAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DrgAttachment.
        :type time_created: datetime

        :param drg_route_table_id:
            The value to assign to the drg_route_table_id property of this DrgAttachment.
        :type drg_route_table_id: str

        :param network_details:
            The value to assign to the network_details property of this DrgAttachment.
        :type network_details: oci.vn_monitoring.models.DrgAttachmentNetworkDetails

        :param defined_tags:
            The value to assign to the defined_tags property of this DrgAttachment.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DrgAttachment.
        :type freeform_tags: dict(str, str)

        :param vcn_id:
            The value to assign to the vcn_id property of this DrgAttachment.
        :type vcn_id: str

        :param export_drg_route_distribution_id:
            The value to assign to the export_drg_route_distribution_id property of this DrgAttachment.
        :type export_drg_route_distribution_id: str

        :param is_cross_tenancy:
            The value to assign to the is_cross_tenancy property of this DrgAttachment.
        :type is_cross_tenancy: bool

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'drg_route_table_id': 'str',
            'network_details': 'DrgAttachmentNetworkDetails',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'vcn_id': 'str',
            'export_drg_route_distribution_id': 'str',
            'is_cross_tenancy': 'bool'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'drg_route_table_id': 'drgRouteTableId',
            'network_details': 'networkDetails',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'vcn_id': 'vcnId',
            'export_drg_route_distribution_id': 'exportDrgRouteDistributionId',
            'is_cross_tenancy': 'isCrossTenancy'
        }

        self._compartment_id = None
        self._display_name = None
        self._drg_id = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._drg_route_table_id = None
        self._network_details = None
        self._defined_tags = None
        self._freeform_tags = None
        self._vcn_id = None
        self._export_drg_route_distribution_id = None
        self._is_cross_tenancy = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DrgAttachment.
        The `OCID`__ of the compartment containing the DRG attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DrgAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrgAttachment.
        The `OCID`__ of the compartment containing the DRG attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DrgAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DrgAttachment.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DrgAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrgAttachment.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DrgAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this DrgAttachment.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_id of this DrgAttachment.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this DrgAttachment.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_id: The drg_id of this DrgAttachment.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgAttachment.
        The DRG attachment's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this DrgAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgAttachment.
        The DRG attachment's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this DrgAttachment.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DrgAttachment.
        The DRG attachment's current state.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED"


        :return: The lifecycle_state of this DrgAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrgAttachment.
        The DRG attachment's current state.


        :param lifecycle_state: The lifecycle_state of this DrgAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this DrgAttachment.
        The date and time the DRG attachment was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DrgAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrgAttachment.
        The date and time the DRG attachment was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DrgAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def drg_route_table_id(self):
        """
        Gets the drg_route_table_id of this DrgAttachment.
        The `OCID`__ of the DRG route table that is assigned to this attachment.

        The DRG route table manages traffic inside the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_route_table_id of this DrgAttachment.
        :rtype: str
        """
        return self._drg_route_table_id

    @drg_route_table_id.setter
    def drg_route_table_id(self, drg_route_table_id):
        """
        Sets the drg_route_table_id of this DrgAttachment.
        The `OCID`__ of the DRG route table that is assigned to this attachment.

        The DRG route table manages traffic inside the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_route_table_id: The drg_route_table_id of this DrgAttachment.
        :type: str
        """
        self._drg_route_table_id = drg_route_table_id

    @property
    def network_details(self):
        """
        Gets the network_details of this DrgAttachment.

        :return: The network_details of this DrgAttachment.
        :rtype: oci.vn_monitoring.models.DrgAttachmentNetworkDetails
        """
        return self._network_details

    @network_details.setter
    def network_details(self, network_details):
        """
        Sets the network_details of this DrgAttachment.

        :param network_details: The network_details of this DrgAttachment.
        :type: oci.vn_monitoring.models.DrgAttachmentNetworkDetails
        """
        self._network_details = network_details

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DrgAttachment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DrgAttachment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DrgAttachment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DrgAttachment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DrgAttachment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DrgAttachment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DrgAttachment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DrgAttachment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this DrgAttachment.
        The `OCID`__ of the VCN.
        This field is deprecated. Instead, use the `networkDetails` field to view the `OCID`__ of the attached resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this DrgAttachment.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DrgAttachment.
        The `OCID`__ of the VCN.
        This field is deprecated. Instead, use the `networkDetails` field to view the `OCID`__ of the attached resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this DrgAttachment.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def export_drg_route_distribution_id(self):
        """
        Gets the export_drg_route_distribution_id of this DrgAttachment.
        The `OCID`__ of the export route distribution used to specify how routes in the assigned DRG route table
        are advertised to the attachment.
        If this value is null, no routes are advertised through this attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The export_drg_route_distribution_id of this DrgAttachment.
        :rtype: str
        """
        return self._export_drg_route_distribution_id

    @export_drg_route_distribution_id.setter
    def export_drg_route_distribution_id(self, export_drg_route_distribution_id):
        """
        Sets the export_drg_route_distribution_id of this DrgAttachment.
        The `OCID`__ of the export route distribution used to specify how routes in the assigned DRG route table
        are advertised to the attachment.
        If this value is null, no routes are advertised through this attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param export_drg_route_distribution_id: The export_drg_route_distribution_id of this DrgAttachment.
        :type: str
        """
        self._export_drg_route_distribution_id = export_drg_route_distribution_id

    @property
    def is_cross_tenancy(self):
        """
        Gets the is_cross_tenancy of this DrgAttachment.
        Indicates whether the DRG attachment and attached network live in a different tenancy than the DRG.

        Example: `false`


        :return: The is_cross_tenancy of this DrgAttachment.
        :rtype: bool
        """
        return self._is_cross_tenancy

    @is_cross_tenancy.setter
    def is_cross_tenancy(self, is_cross_tenancy):
        """
        Sets the is_cross_tenancy of this DrgAttachment.
        Indicates whether the DRG attachment and attached network live in a different tenancy than the DRG.

        Example: `false`


        :param is_cross_tenancy: The is_cross_tenancy of this DrgAttachment.
        :type: bool
        """
        self._is_cross_tenancy = is_cross_tenancy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
