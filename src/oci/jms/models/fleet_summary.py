# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetSummary(object):
    """
    The summary of the Fleet.
    A Fleet is the primary collection with which users interact when using Java Management Service.
    """

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a FleetSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new FleetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FleetSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FleetSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this FleetSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FleetSummary.
        :type compartment_id: str

        :param approximate_jre_count:
            The value to assign to the approximate_jre_count property of this FleetSummary.
        :type approximate_jre_count: int

        :param approximate_installation_count:
            The value to assign to the approximate_installation_count property of this FleetSummary.
        :type approximate_installation_count: int

        :param approximate_application_count:
            The value to assign to the approximate_application_count property of this FleetSummary.
        :type approximate_application_count: int

        :param approximate_managed_instance_count:
            The value to assign to the approximate_managed_instance_count property of this FleetSummary.
        :type approximate_managed_instance_count: int

        :param inventory_log:
            The value to assign to the inventory_log property of this FleetSummary.
        :type inventory_log: oci.jms.models.CustomLog

        :param operation_log:
            The value to assign to the operation_log property of this FleetSummary.
        :type operation_log: oci.jms.models.CustomLog

        :param time_created:
            The value to assign to the time_created property of this FleetSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FleetSummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param defined_tags:
            The value to assign to the defined_tags property of this FleetSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FleetSummary.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this FleetSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'approximate_jre_count': 'int',
            'approximate_installation_count': 'int',
            'approximate_application_count': 'int',
            'approximate_managed_instance_count': 'int',
            'inventory_log': 'CustomLog',
            'operation_log': 'CustomLog',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'approximate_jre_count': 'approximateJreCount',
            'approximate_installation_count': 'approximateInstallationCount',
            'approximate_application_count': 'approximateApplicationCount',
            'approximate_managed_instance_count': 'approximateManagedInstanceCount',
            'inventory_log': 'inventoryLog',
            'operation_log': 'operationLog',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._approximate_jre_count = None
        self._approximate_installation_count = None
        self._approximate_application_count = None
        self._approximate_managed_instance_count = None
        self._inventory_log = None
        self._operation_log = None
        self._time_created = None
        self._lifecycle_state = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FleetSummary.
        The `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this FleetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FleetSummary.
        The `OCID`__ of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this FleetSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FleetSummary.
        The name of the Fleet. The displayName must be unique for Fleets in the same compartment.


        :return: The display_name of this FleetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FleetSummary.
        The name of the Fleet. The displayName must be unique for Fleets in the same compartment.


        :param display_name: The display_name of this FleetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this FleetSummary.
        The Fleet's description.


        :return: The description of this FleetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FleetSummary.
        The Fleet's description.


        :param description: The description of this FleetSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FleetSummary.
        The `OCID`__ of the compartment of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this FleetSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FleetSummary.
        The `OCID`__ of the compartment of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this FleetSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def approximate_jre_count(self):
        """
        **[Required]** Gets the approximate_jre_count of this FleetSummary.
        The approximate count of all unique Java Runtimes in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :return: The approximate_jre_count of this FleetSummary.
        :rtype: int
        """
        return self._approximate_jre_count

    @approximate_jre_count.setter
    def approximate_jre_count(self, approximate_jre_count):
        """
        Sets the approximate_jre_count of this FleetSummary.
        The approximate count of all unique Java Runtimes in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :param approximate_jre_count: The approximate_jre_count of this FleetSummary.
        :type: int
        """
        self._approximate_jre_count = approximate_jre_count

    @property
    def approximate_installation_count(self):
        """
        **[Required]** Gets the approximate_installation_count of this FleetSummary.
        The approximate count of all unique Java Installations in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :return: The approximate_installation_count of this FleetSummary.
        :rtype: int
        """
        return self._approximate_installation_count

    @approximate_installation_count.setter
    def approximate_installation_count(self, approximate_installation_count):
        """
        Sets the approximate_installation_count of this FleetSummary.
        The approximate count of all unique Java Installations in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :param approximate_installation_count: The approximate_installation_count of this FleetSummary.
        :type: int
        """
        self._approximate_installation_count = approximate_installation_count

    @property
    def approximate_application_count(self):
        """
        **[Required]** Gets the approximate_application_count of this FleetSummary.
        The approximate count of all unique applications in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :return: The approximate_application_count of this FleetSummary.
        :rtype: int
        """
        return self._approximate_application_count

    @approximate_application_count.setter
    def approximate_application_count(self, approximate_application_count):
        """
        Sets the approximate_application_count of this FleetSummary.
        The approximate count of all unique applications in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :param approximate_application_count: The approximate_application_count of this FleetSummary.
        :type: int
        """
        self._approximate_application_count = approximate_application_count

    @property
    def approximate_managed_instance_count(self):
        """
        **[Required]** Gets the approximate_managed_instance_count of this FleetSummary.
        The approximate count of all unique managed instances in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :return: The approximate_managed_instance_count of this FleetSummary.
        :rtype: int
        """
        return self._approximate_managed_instance_count

    @approximate_managed_instance_count.setter
    def approximate_managed_instance_count(self, approximate_managed_instance_count):
        """
        Sets the approximate_managed_instance_count of this FleetSummary.
        The approximate count of all unique managed instances in the Fleet in the past seven days.
        This metric is provided on a best-effort manner, and is not taken into account when computing the resource ETag.


        :param approximate_managed_instance_count: The approximate_managed_instance_count of this FleetSummary.
        :type: int
        """
        self._approximate_managed_instance_count = approximate_managed_instance_count

    @property
    def inventory_log(self):
        """
        Gets the inventory_log of this FleetSummary.

        :return: The inventory_log of this FleetSummary.
        :rtype: oci.jms.models.CustomLog
        """
        return self._inventory_log

    @inventory_log.setter
    def inventory_log(self, inventory_log):
        """
        Sets the inventory_log of this FleetSummary.

        :param inventory_log: The inventory_log of this FleetSummary.
        :type: oci.jms.models.CustomLog
        """
        self._inventory_log = inventory_log

    @property
    def operation_log(self):
        """
        Gets the operation_log of this FleetSummary.

        :return: The operation_log of this FleetSummary.
        :rtype: oci.jms.models.CustomLog
        """
        return self._operation_log

    @operation_log.setter
    def operation_log(self, operation_log):
        """
        Sets the operation_log of this FleetSummary.

        :param operation_log: The operation_log of this FleetSummary.
        :type: oci.jms.models.CustomLog
        """
        self._operation_log = operation_log

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FleetSummary.
        The creation date and time of the Fleet (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this FleetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FleetSummary.
        The creation date and time of the Fleet (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this FleetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FleetSummary.
        The lifecycle state of the Fleet.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FleetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FleetSummary.
        The lifecycle state of the Fleet.


        :param lifecycle_state: The lifecycle_state of this FleetSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "NEEDS_ATTENTION", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FleetSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this FleetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FleetSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this FleetSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FleetSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this FleetSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FleetSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this FleetSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this FleetSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this FleetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this FleetSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this FleetSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
