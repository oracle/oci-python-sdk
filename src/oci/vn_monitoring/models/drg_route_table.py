# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgRouteTable(object):
    """
    All routing inside the DRG is driven by the contents of DRG route tables.
    DRG route tables contain rules which route packets to a particular network destination,
    represented as a DRG attachment.
    The routing decision for a packet entering a DRG is determined by the rules in the DRG route table
    assigned to the attachment-of-entry.

    Each DRG attachment can inject routes in any DRG route table, provided there is a statement corresponding to the attachment in the route table's `importDrgRouteDistribution`.
    You can also insert static routes into the DRG route tables.

    The DRG route table is always in the same compartment as the DRG. There must always be a default
    DRG route table for each attachment type.
    """

    #: A constant which can be used with the lifecycle_state property of a DrgRouteTable.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DrgRouteTable.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DrgRouteTable.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DrgRouteTable.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgRouteTable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DrgRouteTable.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DrgRouteTable.
        :type compartment_id: str

        :param drg_id:
            The value to assign to the drg_id property of this DrgRouteTable.
        :type drg_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DrgRouteTable.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this DrgRouteTable.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DrgRouteTable.
        :type freeform_tags: dict(str, str)

        :param time_created:
            The value to assign to the time_created property of this DrgRouteTable.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DrgRouteTable.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        :type lifecycle_state: str

        :param import_drg_route_distribution_id:
            The value to assign to the import_drg_route_distribution_id property of this DrgRouteTable.
        :type import_drg_route_distribution_id: str

        :param is_ecmp_enabled:
            The value to assign to the is_ecmp_enabled property of this DrgRouteTable.
        :type is_ecmp_enabled: bool

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'drg_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'import_drg_route_distribution_id': 'str',
            'is_ecmp_enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'drg_id': 'drgId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'import_drg_route_distribution_id': 'importDrgRouteDistributionId',
            'is_ecmp_enabled': 'isEcmpEnabled'
        }

        self._id = None
        self._compartment_id = None
        self._drg_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._time_created = None
        self._lifecycle_state = None
        self._import_drg_route_distribution_id = None
        self._is_ecmp_enabled = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgRouteTable.
        The `OCID`__ of the
        DRG route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this DrgRouteTable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgRouteTable.
        The `OCID`__ of the
        DRG route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this DrgRouteTable.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DrgRouteTable.
        The `OCID`__ of the compartment the DRG is in. The DRG route table
        is always in the same compartment as the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DrgRouteTable.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrgRouteTable.
        The `OCID`__ of the compartment the DRG is in. The DRG route table
        is always in the same compartment as the DRG.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DrgRouteTable.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this DrgRouteTable.
        The `OCID`__ of the DRG the DRG that contains this route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_id of this DrgRouteTable.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this DrgRouteTable.
        The `OCID`__ of the DRG the DRG that contains this route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_id: The drg_id of this DrgRouteTable.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DrgRouteTable.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DrgRouteTable.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DrgRouteTable.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DrgRouteTable.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this DrgRouteTable.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DrgRouteTable.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrgRouteTable.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DrgRouteTable.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DrgRouteTable.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DrgRouteTable.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DrgRouteTable.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DrgRouteTable.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DrgRouteTable.
        The date and time the DRG route table was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DrgRouteTable.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrgRouteTable.
        The date and time the DRG route table was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DrgRouteTable.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DrgRouteTable.
        The DRG route table's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"


        :return: The lifecycle_state of this DrgRouteTable.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrgRouteTable.
        The DRG route table's current state.


        :param lifecycle_state: The lifecycle_state of this DrgRouteTable.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def import_drg_route_distribution_id(self):
        """
        Gets the import_drg_route_distribution_id of this DrgRouteTable.
        The `OCID`__ of the import route distribution used to specify how incoming route advertisements from
        referenced attachments are inserted into the DRG route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The import_drg_route_distribution_id of this DrgRouteTable.
        :rtype: str
        """
        return self._import_drg_route_distribution_id

    @import_drg_route_distribution_id.setter
    def import_drg_route_distribution_id(self, import_drg_route_distribution_id):
        """
        Sets the import_drg_route_distribution_id of this DrgRouteTable.
        The `OCID`__ of the import route distribution used to specify how incoming route advertisements from
        referenced attachments are inserted into the DRG route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param import_drg_route_distribution_id: The import_drg_route_distribution_id of this DrgRouteTable.
        :type: str
        """
        self._import_drg_route_distribution_id = import_drg_route_distribution_id

    @property
    def is_ecmp_enabled(self):
        """
        **[Required]** Gets the is_ecmp_enabled of this DrgRouteTable.
        If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
        your on-premises network, enable ECMP on the DRG route table to which these attachments
        import routes.


        :return: The is_ecmp_enabled of this DrgRouteTable.
        :rtype: bool
        """
        return self._is_ecmp_enabled

    @is_ecmp_enabled.setter
    def is_ecmp_enabled(self, is_ecmp_enabled):
        """
        Sets the is_ecmp_enabled of this DrgRouteTable.
        If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
        your on-premises network, enable ECMP on the DRG route table to which these attachments
        import routes.


        :param is_ecmp_enabled: The is_ecmp_enabled of this DrgRouteTable.
        :type: bool
        """
        self._is_ecmp_enabled = is_ecmp_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
