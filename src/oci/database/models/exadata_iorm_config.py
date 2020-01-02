# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataIormConfig(object):
    """
    Response details which has IORM Settings for this Exadata System
    """

    #: A constant which can be used with the lifecycle_state property of a ExadataIormConfig.
    #: This constant has a value of "BOOTSTRAPPING"
    LIFECYCLE_STATE_BOOTSTRAPPING = "BOOTSTRAPPING"

    #: A constant which can be used with the lifecycle_state property of a ExadataIormConfig.
    #: This constant has a value of "ENABLED"
    LIFECYCLE_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the lifecycle_state property of a ExadataIormConfig.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a ExadataIormConfig.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExadataIormConfig.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the objective property of a ExadataIormConfig.
    #: This constant has a value of "LOW_LATENCY"
    OBJECTIVE_LOW_LATENCY = "LOW_LATENCY"

    #: A constant which can be used with the objective property of a ExadataIormConfig.
    #: This constant has a value of "HIGH_THROUGHPUT"
    OBJECTIVE_HIGH_THROUGHPUT = "HIGH_THROUGHPUT"

    #: A constant which can be used with the objective property of a ExadataIormConfig.
    #: This constant has a value of "BALANCED"
    OBJECTIVE_BALANCED = "BALANCED"

    #: A constant which can be used with the objective property of a ExadataIormConfig.
    #: This constant has a value of "AUTO"
    OBJECTIVE_AUTO = "AUTO"

    #: A constant which can be used with the objective property of a ExadataIormConfig.
    #: This constant has a value of "BASIC"
    OBJECTIVE_BASIC = "BASIC"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataIormConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExadataIormConfig.
            Allowed values for this property are: "BOOTSTRAPPING", "ENABLED", "DISABLED", "UPDATING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExadataIormConfig.
        :type lifecycle_details: str

        :param objective:
            The value to assign to the objective property of this ExadataIormConfig.
            Allowed values for this property are: "LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type objective: str

        :param db_plans:
            The value to assign to the db_plans property of this ExadataIormConfig.
        :type db_plans: list[DbIormConfig]

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'objective': 'str',
            'db_plans': 'list[DbIormConfig]'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'objective': 'objective',
            'db_plans': 'dbPlans'
        }

        self._lifecycle_state = None
        self._lifecycle_details = None
        self._objective = None
        self._db_plans = None

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ExadataIormConfig.
        The current config state of IORM settings for this Exadata System.

        Allowed values for this property are: "BOOTSTRAPPING", "ENABLED", "DISABLED", "UPDATING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExadataIormConfig.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExadataIormConfig.
        The current config state of IORM settings for this Exadata System.


        :param lifecycle_state: The lifecycle_state of this ExadataIormConfig.
        :type: str
        """
        allowed_values = ["BOOTSTRAPPING", "ENABLED", "DISABLED", "UPDATING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExadataIormConfig.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this ExadataIormConfig.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExadataIormConfig.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this ExadataIormConfig.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def objective(self):
        """
        Gets the objective of this ExadataIormConfig.
        Value for the IORM objective
        Default is \"Auto\"

        Allowed values for this property are: "LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The objective of this ExadataIormConfig.
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """
        Sets the objective of this ExadataIormConfig.
        Value for the IORM objective
        Default is \"Auto\"


        :param objective: The objective of this ExadataIormConfig.
        :type: str
        """
        allowed_values = ["LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC"]
        if not value_allowed_none_or_none_sentinel(objective, allowed_values):
            objective = 'UNKNOWN_ENUM_VALUE'
        self._objective = objective

    @property
    def db_plans(self):
        """
        Gets the db_plans of this ExadataIormConfig.
        Array of IORM Setting for all the database in
        this Exadata DB System


        :return: The db_plans of this ExadataIormConfig.
        :rtype: list[DbIormConfig]
        """
        return self._db_plans

    @db_plans.setter
    def db_plans(self, db_plans):
        """
        Sets the db_plans of this ExadataIormConfig.
        Array of IORM Setting for all the database in
        this Exadata DB System


        :param db_plans: The db_plans of this ExadataIormConfig.
        :type: list[DbIormConfig]
        """
        self._db_plans = db_plans

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
