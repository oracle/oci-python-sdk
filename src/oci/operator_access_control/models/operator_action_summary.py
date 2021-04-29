# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatorActionSummary(object):
    """
    Details of the operator action. Operator actions are pre-defined set of commands available to the operator on different layers of the infrastructure.
    """

    #: A constant which can be used with the lifecycle_state property of a OperatorActionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OperatorActionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new OperatorActionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperatorActionSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this OperatorActionSummary.
        :type name: str

        :param component:
            The value to assign to the component property of this OperatorActionSummary.
        :type component: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OperatorActionSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OperatorActionSummary.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param description:
            The value to assign to the description property of this OperatorActionSummary.
        :type description: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'component': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'component': 'component',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'description': 'description'
        }

        self._id = None
        self._name = None
        self._component = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._description = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperatorActionSummary.
        Unique identifier assigned by Oracle to an operator action.


        :return: The id of this OperatorActionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperatorActionSummary.
        Unique identifier assigned by Oracle to an operator action.


        :param id: The id of this OperatorActionSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OperatorActionSummary.
        Name of the operator action.


        :return: The name of this OperatorActionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OperatorActionSummary.
        Name of the operator action.


        :param name: The name of this OperatorActionSummary.
        :type: str
        """
        self._name = name

    @property
    def component(self):
        """
        Gets the component of this OperatorActionSummary.
        Name of the component for which the operator action is applicable.


        :return: The component of this OperatorActionSummary.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this OperatorActionSummary.
        Name of the component for which the operator action is applicable.


        :param component: The component of this OperatorActionSummary.
        :type: str
        """
        self._component = component

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this OperatorActionSummary.
        compartmentId for which the OperatorAction is applicable


        :return: The compartment_id of this OperatorActionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OperatorActionSummary.
        compartmentId for which the OperatorAction is applicable


        :param compartment_id: The compartment_id of this OperatorActionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OperatorActionSummary.
        The current lifecycle state of the operator action.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OperatorActionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OperatorActionSummary.
        The current lifecycle state of the operator action.


        :param lifecycle_state: The lifecycle_state of this OperatorActionSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def description(self):
        """
        Gets the description of this OperatorActionSummary.
        Description of the operator action in terms of associated risk profile, and characteristics of the operating system commands made
        available to the operator under this operator action.


        :return: The description of this OperatorActionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OperatorActionSummary.
        Description of the operator action in terms of associated risk profile, and characteristics of the operating system commands made
        available to the operator under this operator action.


        :param description: The description of this OperatorActionSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
