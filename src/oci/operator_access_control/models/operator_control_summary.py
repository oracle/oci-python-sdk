# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatorControlSummary(object):
    """
    Summary of the OperatorControl.
    """

    #: A constant which can be used with the resource_type property of a OperatorControlSummary.
    #: This constant has a value of "EXACC"
    RESOURCE_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the resource_type property of a OperatorControlSummary.
    #: This constant has a value of "EXADATAINFRASTRUCTURE"
    RESOURCE_TYPE_EXADATAINFRASTRUCTURE = "EXADATAINFRASTRUCTURE"

    #: A constant which can be used with the resource_type property of a OperatorControlSummary.
    #: This constant has a value of "AUTONOMOUSVMCLUSTER"
    RESOURCE_TYPE_AUTONOMOUSVMCLUSTER = "AUTONOMOUSVMCLUSTER"

    #: A constant which can be used with the resource_type property of a OperatorControlSummary.
    #: This constant has a value of "CLOUDAUTONOMOUSVMCLUSTER"
    RESOURCE_TYPE_CLOUDAUTONOMOUSVMCLUSTER = "CLOUDAUTONOMOUSVMCLUSTER"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlSummary.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlSummary.
    #: This constant has a value of "ASSIGNED"
    LIFECYCLE_STATE_ASSIGNED = "ASSIGNED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlSummary.
    #: This constant has a value of "UNASSIGNED"
    LIFECYCLE_STATE_UNASSIGNED = "UNASSIGNED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new OperatorControlSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperatorControlSummary.
        :type id: str

        :param operator_control_name:
            The value to assign to the operator_control_name property of this OperatorControlSummary.
        :type operator_control_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OperatorControlSummary.
        :type compartment_id: str

        :param is_fully_pre_approved:
            The value to assign to the is_fully_pre_approved property of this OperatorControlSummary.
        :type is_fully_pre_approved: bool

        :param resource_type:
            The value to assign to the resource_type property of this OperatorControlSummary.
            Allowed values for this property are: "EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param time_of_creation:
            The value to assign to the time_of_creation property of this OperatorControlSummary.
        :type time_of_creation: datetime

        :param time_of_modification:
            The value to assign to the time_of_modification property of this OperatorControlSummary.
        :type time_of_modification: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this OperatorControlSummary.
        :type time_of_deletion: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OperatorControlSummary.
            Allowed values for this property are: "CREATED", "ASSIGNED", "UNASSIGNED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OperatorControlSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OperatorControlSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'operator_control_name': 'str',
            'compartment_id': 'str',
            'is_fully_pre_approved': 'bool',
            'resource_type': 'str',
            'time_of_creation': 'datetime',
            'time_of_modification': 'datetime',
            'time_of_deletion': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'operator_control_name': 'operatorControlName',
            'compartment_id': 'compartmentId',
            'is_fully_pre_approved': 'isFullyPreApproved',
            'resource_type': 'resourceType',
            'time_of_creation': 'timeOfCreation',
            'time_of_modification': 'timeOfModification',
            'time_of_deletion': 'timeOfDeletion',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._operator_control_name = None
        self._compartment_id = None
        self._is_fully_pre_approved = None
        self._resource_type = None
        self._time_of_creation = None
        self._time_of_modification = None
        self._time_of_deletion = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperatorControlSummary.
        The OCID of the operator control.


        :return: The id of this OperatorControlSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperatorControlSummary.
        The OCID of the operator control.


        :param id: The id of this OperatorControlSummary.
        :type: str
        """
        self._id = id

    @property
    def operator_control_name(self):
        """
        **[Required]** Gets the operator_control_name of this OperatorControlSummary.
        Name of the operator control.


        :return: The operator_control_name of this OperatorControlSummary.
        :rtype: str
        """
        return self._operator_control_name

    @operator_control_name.setter
    def operator_control_name(self, operator_control_name):
        """
        Sets the operator_control_name of this OperatorControlSummary.
        Name of the operator control.


        :param operator_control_name: The operator_control_name of this OperatorControlSummary.
        :type: str
        """
        self._operator_control_name = operator_control_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this OperatorControlSummary.
        The OCID of the compartment that contains the operator control.


        :return: The compartment_id of this OperatorControlSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OperatorControlSummary.
        The OCID of the compartment that contains the operator control.


        :param compartment_id: The compartment_id of this OperatorControlSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_fully_pre_approved(self):
        """
        Gets the is_fully_pre_approved of this OperatorControlSummary.
        Whether all operator actions are pre-approved. If yes, an access request associated with a resource governed by the operator control will be automatically approved by the system.


        :return: The is_fully_pre_approved of this OperatorControlSummary.
        :rtype: bool
        """
        return self._is_fully_pre_approved

    @is_fully_pre_approved.setter
    def is_fully_pre_approved(self, is_fully_pre_approved):
        """
        Sets the is_fully_pre_approved of this OperatorControlSummary.
        Whether all operator actions are pre-approved. If yes, an access request associated with a resource governed by the operator control will be automatically approved by the system.


        :param is_fully_pre_approved: The is_fully_pre_approved of this OperatorControlSummary.
        :type: bool
        """
        self._is_fully_pre_approved = is_fully_pre_approved

    @property
    def resource_type(self):
        """
        Gets the resource_type of this OperatorControlSummary.
        resourceType for which the OperatorControl is applicable

        Allowed values for this property are: "EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this OperatorControlSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this OperatorControlSummary.
        resourceType for which the OperatorControl is applicable


        :param resource_type: The resource_type of this OperatorControlSummary.
        :type: str
        """
        allowed_values = ["EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def time_of_creation(self):
        """
        Gets the time_of_creation of this OperatorControlSummary.
        Time when the operator control was created, expressed in `RFC 3339]`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_creation of this OperatorControlSummary.
        :rtype: datetime
        """
        return self._time_of_creation

    @time_of_creation.setter
    def time_of_creation(self, time_of_creation):
        """
        Sets the time_of_creation of this OperatorControlSummary.
        Time when the operator control was created, expressed in `RFC 3339]`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_creation: The time_of_creation of this OperatorControlSummary.
        :type: datetime
        """
        self._time_of_creation = time_of_creation

    @property
    def time_of_modification(self):
        """
        Gets the time_of_modification of this OperatorControlSummary.
        Time when the operator control was last modified, expressed in `RFC 3339]`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_modification of this OperatorControlSummary.
        :rtype: datetime
        """
        return self._time_of_modification

    @time_of_modification.setter
    def time_of_modification(self, time_of_modification):
        """
        Sets the time_of_modification of this OperatorControlSummary.
        Time when the operator control was last modified, expressed in `RFC 3339]`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_modification: The time_of_modification of this OperatorControlSummary.
        :type: datetime
        """
        self._time_of_modification = time_of_modification

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this OperatorControlSummary.
        Time when the operator control was deleted, expressed in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this OperatorControlSummary.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this OperatorControlSummary.
        Time when the operator control was deleted, expressed in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this OperatorControlSummary.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OperatorControlSummary.
        The current lifecycle state of the operator control.

        Allowed values for this property are: "CREATED", "ASSIGNED", "UNASSIGNED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OperatorControlSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OperatorControlSummary.
        The current lifecycle state of the operator control.


        :param lifecycle_state: The lifecycle_state of this OperatorControlSummary.
        :type: str
        """
        allowed_values = ["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OperatorControlSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this OperatorControlSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OperatorControlSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this OperatorControlSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OperatorControlSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this OperatorControlSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OperatorControlSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this OperatorControlSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
