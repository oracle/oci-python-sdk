# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgRouteDistribution(object):
    """
    A route distribution establishes how routes get imported into DRG route tables and exported through the DRG attachments.

    A route distribution is a list of statements. Each statement consists of a set of matches, all of which must be `True` in order for
    the statement's action to take place. Each statement determines which routes are propagated.

    You can assign a route distribution as a route table's import distribution. The statements in an import
    route distribution specify how how incoming route advertisements through a referenced attachment or all attachments of a certain type are inserted into the route table.

    You can assign a route distribution as a DRG attachment's export distribution. Export route distribution statements specify how routes in a
    DRG attachment's assigned table are advertised out through the attachment. When a DRG attachment is created, a route distribution is created with a
    single ACCEPT statement with match criteria MATCH_ALL.
    Exporting routes through VCN attachments is unsupported, so no VCN attachments are assigned an export distribution.

    The two auto-generated DRG route tables (one as the default for VCN attachments, and the other for all other types of attachments)
    are each assigned an auto generated import route distribution. The default VCN table's import distribution has a single statement with match criteria MATCH_ALL to import routes from
    each DRG attachment type. The other table's import distribution has a statement to import routes from attachments with the VCN type.

    The route distribution is always in the same compartment as the DRG.
    """

    #: A constant which can be used with the lifecycle_state property of a DrgRouteDistribution.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DrgRouteDistribution.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DrgRouteDistribution.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DrgRouteDistribution.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the distribution_type property of a DrgRouteDistribution.
    #: This constant has a value of "IMPORT"
    DISTRIBUTION_TYPE_IMPORT = "IMPORT"

    #: A constant which can be used with the distribution_type property of a DrgRouteDistribution.
    #: This constant has a value of "EXPORT"
    DISTRIBUTION_TYPE_EXPORT = "EXPORT"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgRouteDistribution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param drg_id:
            The value to assign to the drg_id property of this DrgRouteDistribution.
        :type drg_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DrgRouteDistribution.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DrgRouteDistribution.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this DrgRouteDistribution.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DrgRouteDistribution.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this DrgRouteDistribution.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DrgRouteDistribution.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DrgRouteDistribution.
        :type time_created: datetime

        :param distribution_type:
            The value to assign to the distribution_type property of this DrgRouteDistribution.
            Allowed values for this property are: "IMPORT", "EXPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type distribution_type: str

        """
        self.swagger_types = {
            'drg_id': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'distribution_type': 'str'
        }

        self.attribute_map = {
            'drg_id': 'drgId',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'distribution_type': 'distributionType'
        }

        self._drg_id = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._distribution_type = None

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this DrgRouteDistribution.
        The `OCID`__ of the DRG that contains this route distribution.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_id of this DrgRouteDistribution.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this DrgRouteDistribution.
        The `OCID`__ of the DRG that contains this route distribution.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_id: The drg_id of this DrgRouteDistribution.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DrgRouteDistribution.
        The `OCID`__ of the compartment containing the route distribution.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DrgRouteDistribution.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrgRouteDistribution.
        The `OCID`__ of the compartment containing the route distribution.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DrgRouteDistribution.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DrgRouteDistribution.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DrgRouteDistribution.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DrgRouteDistribution.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DrgRouteDistribution.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this DrgRouteDistribution.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DrgRouteDistribution.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrgRouteDistribution.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DrgRouteDistribution.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DrgRouteDistribution.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DrgRouteDistribution.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DrgRouteDistribution.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DrgRouteDistribution.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgRouteDistribution.
        The route distribution's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this DrgRouteDistribution.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgRouteDistribution.
        The route distribution's Oracle ID (`OCID`__).

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this DrgRouteDistribution.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DrgRouteDistribution.
        The route distribution's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DrgRouteDistribution.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrgRouteDistribution.
        The route distribution's current state.


        :param lifecycle_state: The lifecycle_state of this DrgRouteDistribution.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DrgRouteDistribution.
        The date and time the route distribution was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DrgRouteDistribution.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrgRouteDistribution.
        The date and time the route distribution was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DrgRouteDistribution.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def distribution_type(self):
        """
        **[Required]** Gets the distribution_type of this DrgRouteDistribution.
        Whether this distribution defines how routes get imported into route tables or exported through DRG attachments.

        Allowed values for this property are: "IMPORT", "EXPORT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The distribution_type of this DrgRouteDistribution.
        :rtype: str
        """
        return self._distribution_type

    @distribution_type.setter
    def distribution_type(self, distribution_type):
        """
        Sets the distribution_type of this DrgRouteDistribution.
        Whether this distribution defines how routes get imported into route tables or exported through DRG attachments.


        :param distribution_type: The distribution_type of this DrgRouteDistribution.
        :type: str
        """
        allowed_values = ["IMPORT", "EXPORT"]
        if not value_allowed_none_or_none_sentinel(distribution_type, allowed_values):
            distribution_type = 'UNKNOWN_ENUM_VALUE'
        self._distribution_type = distribution_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
