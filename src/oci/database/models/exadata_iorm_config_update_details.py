# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataIormConfigUpdateDetails(object):
    """
    IORM Setting details for this Exadata System to be updated
    """

    #: A constant which can be used with the objective property of a ExadataIormConfigUpdateDetails.
    #: This constant has a value of "LOW_LATENCY"
    OBJECTIVE_LOW_LATENCY = "LOW_LATENCY"

    #: A constant which can be used with the objective property of a ExadataIormConfigUpdateDetails.
    #: This constant has a value of "HIGH_THROUGHPUT"
    OBJECTIVE_HIGH_THROUGHPUT = "HIGH_THROUGHPUT"

    #: A constant which can be used with the objective property of a ExadataIormConfigUpdateDetails.
    #: This constant has a value of "BALANCED"
    OBJECTIVE_BALANCED = "BALANCED"

    #: A constant which can be used with the objective property of a ExadataIormConfigUpdateDetails.
    #: This constant has a value of "AUTO"
    OBJECTIVE_AUTO = "AUTO"

    #: A constant which can be used with the objective property of a ExadataIormConfigUpdateDetails.
    #: This constant has a value of "BASIC"
    OBJECTIVE_BASIC = "BASIC"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataIormConfigUpdateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param objective:
            The value to assign to the objective property of this ExadataIormConfigUpdateDetails.
            Allowed values for this property are: "LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC"
        :type objective: str

        :param db_plans:
            The value to assign to the db_plans property of this ExadataIormConfigUpdateDetails.
        :type db_plans: list[DbIormConfigUpdateDetail]

        """
        self.swagger_types = {
            'objective': 'str',
            'db_plans': 'list[DbIormConfigUpdateDetail]'
        }

        self.attribute_map = {
            'objective': 'objective',
            'db_plans': 'dbPlans'
        }

        self._objective = None
        self._db_plans = None

    @property
    def objective(self):
        """
        Gets the objective of this ExadataIormConfigUpdateDetails.
        Value for the IORM objective
        Default is \"Auto\"

        Allowed values for this property are: "LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC"


        :return: The objective of this ExadataIormConfigUpdateDetails.
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """
        Sets the objective of this ExadataIormConfigUpdateDetails.
        Value for the IORM objective
        Default is \"Auto\"


        :param objective: The objective of this ExadataIormConfigUpdateDetails.
        :type: str
        """
        allowed_values = ["LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC"]
        if not value_allowed_none_or_none_sentinel(objective, allowed_values):
            raise ValueError(
                "Invalid value for `objective`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._objective = objective

    @property
    def db_plans(self):
        """
        Gets the db_plans of this ExadataIormConfigUpdateDetails.
        Array of IORM Setting for all the database in
        this Exadata DB System


        :return: The db_plans of this ExadataIormConfigUpdateDetails.
        :rtype: list[DbIormConfigUpdateDetail]
        """
        return self._db_plans

    @db_plans.setter
    def db_plans(self, db_plans):
        """
        Sets the db_plans of this ExadataIormConfigUpdateDetails.
        Array of IORM Setting for all the database in
        this Exadata DB System


        :param db_plans: The db_plans of this ExadataIormConfigUpdateDetails.
        :type: list[DbIormConfigUpdateDetail]
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
