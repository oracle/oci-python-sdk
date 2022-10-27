# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeploymentUpgrade(object):
    """
    A container for your OCI GoldenGate Upgrade information.
    """

    #: A constant which can be used with the deployment_upgrade_type property of a DeploymentUpgrade.
    #: This constant has a value of "MANUAL"
    DEPLOYMENT_UPGRADE_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the deployment_upgrade_type property of a DeploymentUpgrade.
    #: This constant has a value of "AUTOMATIC"
    DEPLOYMENT_UPGRADE_TYPE_AUTOMATIC = "AUTOMATIC"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a DeploymentUpgrade.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "RECOVERING"
    LIFECYCLE_SUB_STATE_RECOVERING = "RECOVERING"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "STARTING"
    LIFECYCLE_SUB_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_SUB_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "MOVING"
    LIFECYCLE_SUB_STATE_MOVING = "MOVING"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "UPGRADING"
    LIFECYCLE_SUB_STATE_UPGRADING = "UPGRADING"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "RESTORING"
    LIFECYCLE_SUB_STATE_RESTORING = "RESTORING"

    #: A constant which can be used with the lifecycle_sub_state property of a DeploymentUpgrade.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_SUB_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new DeploymentUpgrade object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeploymentUpgrade.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DeploymentUpgrade.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DeploymentUpgrade.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeploymentUpgrade.
        :type compartment_id: str

        :param deployment_id:
            The value to assign to the deployment_id property of this DeploymentUpgrade.
        :type deployment_id: str

        :param deployment_upgrade_type:
            The value to assign to the deployment_upgrade_type property of this DeploymentUpgrade.
            Allowed values for this property are: "MANUAL", "AUTOMATIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_upgrade_type: str

        :param time_started:
            The value to assign to the time_started property of this DeploymentUpgrade.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this DeploymentUpgrade.
        :type time_finished: datetime

        :param ogg_version:
            The value to assign to the ogg_version property of this DeploymentUpgrade.
        :type ogg_version: str

        :param time_created:
            The value to assign to the time_created property of this DeploymentUpgrade.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeploymentUpgrade.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeploymentUpgrade.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_sub_state:
            The value to assign to the lifecycle_sub_state property of this DeploymentUpgrade.
            Allowed values for this property are: "RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_sub_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeploymentUpgrade.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeploymentUpgrade.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeploymentUpgrade.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeploymentUpgrade.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'deployment_id': 'str',
            'deployment_upgrade_type': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'ogg_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_sub_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'deployment_id': 'deploymentId',
            'deployment_upgrade_type': 'deploymentUpgradeType',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'ogg_version': 'oggVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_sub_state': 'lifecycleSubState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._deployment_id = None
        self._deployment_upgrade_type = None
        self._time_started = None
        self._time_finished = None
        self._ogg_version = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_sub_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeploymentUpgrade.
        The `OCID`__ of the deployment upgrade being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DeploymentUpgrade.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeploymentUpgrade.
        The `OCID`__ of the deployment upgrade being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DeploymentUpgrade.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this DeploymentUpgrade.
        An object's Display Name.


        :return: The display_name of this DeploymentUpgrade.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeploymentUpgrade.
        An object's Display Name.


        :param display_name: The display_name of this DeploymentUpgrade.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DeploymentUpgrade.
        Metadata about this specific object.


        :return: The description of this DeploymentUpgrade.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeploymentUpgrade.
        Metadata about this specific object.


        :param description: The description of this DeploymentUpgrade.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeploymentUpgrade.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DeploymentUpgrade.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeploymentUpgrade.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DeploymentUpgrade.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this DeploymentUpgrade.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this DeploymentUpgrade.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this DeploymentUpgrade.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this DeploymentUpgrade.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def deployment_upgrade_type(self):
        """
        **[Required]** Gets the deployment_upgrade_type of this DeploymentUpgrade.
        The type of the deployment upgrade: MANUAL or AUTOMATIC

        Allowed values for this property are: "MANUAL", "AUTOMATIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_upgrade_type of this DeploymentUpgrade.
        :rtype: str
        """
        return self._deployment_upgrade_type

    @deployment_upgrade_type.setter
    def deployment_upgrade_type(self, deployment_upgrade_type):
        """
        Sets the deployment_upgrade_type of this DeploymentUpgrade.
        The type of the deployment upgrade: MANUAL or AUTOMATIC


        :param deployment_upgrade_type: The deployment_upgrade_type of this DeploymentUpgrade.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTOMATIC"]
        if not value_allowed_none_or_none_sentinel(deployment_upgrade_type, allowed_values):
            deployment_upgrade_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_upgrade_type = deployment_upgrade_type

    @property
    def time_started(self):
        """
        Gets the time_started of this DeploymentUpgrade.
        The date and time the request was started. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this DeploymentUpgrade.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DeploymentUpgrade.
        The date and time the request was started. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this DeploymentUpgrade.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this DeploymentUpgrade.
        The date and time the request was finished. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this DeploymentUpgrade.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this DeploymentUpgrade.
        The date and time the request was finished. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this DeploymentUpgrade.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def ogg_version(self):
        """
        Gets the ogg_version of this DeploymentUpgrade.
        Version of OGG


        :return: The ogg_version of this DeploymentUpgrade.
        :rtype: str
        """
        return self._ogg_version

    @ogg_version.setter
    def ogg_version(self, ogg_version):
        """
        Sets the ogg_version of this DeploymentUpgrade.
        Version of OGG


        :param ogg_version: The ogg_version of this DeploymentUpgrade.
        :type: str
        """
        self._ogg_version = ogg_version

    @property
    def time_created(self):
        """
        Gets the time_created of this DeploymentUpgrade.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DeploymentUpgrade.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeploymentUpgrade.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DeploymentUpgrade.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeploymentUpgrade.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DeploymentUpgrade.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeploymentUpgrade.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DeploymentUpgrade.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DeploymentUpgrade.
        Possible lifecycle states.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DeploymentUpgrade.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeploymentUpgrade.
        Possible lifecycle states.


        :param lifecycle_state: The lifecycle_state of this DeploymentUpgrade.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", "IN_PROGRESS", "CANCELING", "CANCELED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_sub_state(self):
        """
        Gets the lifecycle_sub_state of this DeploymentUpgrade.
        Possible GGS lifecycle sub-states.

        Allowed values for this property are: "RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_sub_state of this DeploymentUpgrade.
        :rtype: str
        """
        return self._lifecycle_sub_state

    @lifecycle_sub_state.setter
    def lifecycle_sub_state(self, lifecycle_sub_state):
        """
        Sets the lifecycle_sub_state of this DeploymentUpgrade.
        Possible GGS lifecycle sub-states.


        :param lifecycle_sub_state: The lifecycle_sub_state of this DeploymentUpgrade.
        :type: str
        """
        allowed_values = ["RECOVERING", "STARTING", "STOPPING", "MOVING", "UPGRADING", "RESTORING", "BACKUP_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_sub_state, allowed_values):
            lifecycle_sub_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_sub_state = lifecycle_sub_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeploymentUpgrade.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this DeploymentUpgrade.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeploymentUpgrade.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this DeploymentUpgrade.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeploymentUpgrade.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DeploymentUpgrade.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeploymentUpgrade.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DeploymentUpgrade.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeploymentUpgrade.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DeploymentUpgrade.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeploymentUpgrade.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DeploymentUpgrade.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeploymentUpgrade.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeploymentUpgrade.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeploymentUpgrade.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeploymentUpgrade.
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
