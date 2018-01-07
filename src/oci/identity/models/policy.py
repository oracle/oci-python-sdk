# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Policy(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Policy object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Policy.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Policy.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this Policy.
        :type name: str

        :param statements:
            The value to assign to the statements property of this Policy.
        :type statements: list[str]

        :param description:
            The value to assign to the description property of this Policy.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this Policy.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Policy.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this Policy.
        :type inactive_status: int

        :param version_date:
            The value to assign to the version_date property of this Policy.
        :type version_date: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Policy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Policy.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'statements': 'list[str]',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'version_date': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'statements': 'statements',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'version_date': 'versionDate',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._statements = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._version_date = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this Policy.
        The OCID of the policy.


        :return: The id of this Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Policy.
        The OCID of the policy.


        :param id: The id of this Policy.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Policy.
        The OCID of the compartment containing the policy (either the tenancy or another compartment).


        :return: The compartment_id of this Policy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Policy.
        The OCID of the compartment containing the policy (either the tenancy or another compartment).


        :param compartment_id: The compartment_id of this Policy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this Policy.
        The name you assign to the policy during creation. The name must be unique across all policies
        in the tenancy and cannot be changed.


        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Policy.
        The name you assign to the policy during creation. The name must be unique across all policies
        in the tenancy and cannot be changed.


        :param name: The name of this Policy.
        :type: str
        """
        self._name = name

    @property
    def statements(self):
        """
        Gets the statements of this Policy.
        An array of one or more policy statements written in the policy language.


        :return: The statements of this Policy.
        :rtype: list[str]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this Policy.
        An array of one or more policy statements written in the policy language.


        :param statements: The statements of this Policy.
        :type: list[str]
        """
        self._statements = statements

    @property
    def description(self):
        """
        Gets the description of this Policy.
        The description you assign to the policy. Does not have to be unique, and it's changeable.


        :return: The description of this Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Policy.
        The description you assign to the policy. Does not have to be unique, and it's changeable.


        :param description: The description of this Policy.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Policy.
        Date and time the policy was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Policy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Policy.
        Date and time the policy was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Policy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Policy.
        The policy's current state. After creating a policy, make sure its `lifecycleState` changes from CREATING to
        ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Policy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Policy.
        The policy's current state. After creating a policy, make sure its `lifecycleState` changes from CREATING to
        ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this Policy.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this Policy.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this Policy.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this Policy.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this Policy.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def version_date(self):
        """
        Gets the version_date of this Policy.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
        policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
        date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


        :return: The version_date of this Policy.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this Policy.
        The version of the policy. If null or set to an empty string, when a request comes in for authorization, the
        policy will be evaluated according to the current behavior of the services at that moment. If set to a particular
        date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.


        :param version_date: The version_date of this Policy.
        :type: datetime
        """
        self._version_date = version_date

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Policy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Policy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Policy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Policy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Policy.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this Policy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Policy.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this Policy.
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
