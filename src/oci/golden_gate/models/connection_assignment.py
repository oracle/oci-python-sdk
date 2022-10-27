# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionAssignment(object):
    """
    Represents the metadata description of a connection assignment.
    Before you can use a connection as a GoldenGate source or target, you must assign it to a deployment.
    """

    #: A constant which can be used with the lifecycle_state property of a ConnectionAssignment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionAssignment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConnectionAssignment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ConnectionAssignment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionAssignment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionAssignment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConnectionAssignment.
        :type id: str

        :param connection_id:
            The value to assign to the connection_id property of this ConnectionAssignment.
        :type connection_id: str

        :param deployment_id:
            The value to assign to the deployment_id property of this ConnectionAssignment.
        :type deployment_id: str

        :param alias_name:
            The value to assign to the alias_name property of this ConnectionAssignment.
        :type alias_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConnectionAssignment.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConnectionAssignment.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ConnectionAssignment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ConnectionAssignment.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'connection_id': 'str',
            'deployment_id': 'str',
            'alias_name': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'connection_id': 'connectionId',
            'deployment_id': 'deploymentId',
            'alias_name': 'aliasName',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._connection_id = None
        self._deployment_id = None
        self._alias_name = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConnectionAssignment.
        The `OCID`__ of the connection assignment being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ConnectionAssignment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionAssignment.
        The `OCID`__ of the connection assignment being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ConnectionAssignment.
        :type: str
        """
        self._id = id

    @property
    def connection_id(self):
        """
        **[Required]** Gets the connection_id of this ConnectionAssignment.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The connection_id of this ConnectionAssignment.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this ConnectionAssignment.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param connection_id: The connection_id of this ConnectionAssignment.
        :type: str
        """
        self._connection_id = connection_id

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this ConnectionAssignment.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this ConnectionAssignment.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this ConnectionAssignment.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this ConnectionAssignment.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def alias_name(self):
        """
        Gets the alias_name of this ConnectionAssignment.
        Credential store alias.


        :return: The alias_name of this ConnectionAssignment.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """
        Sets the alias_name of this ConnectionAssignment.
        Credential store alias.


        :param alias_name: The alias_name of this ConnectionAssignment.
        :type: str
        """
        self._alias_name = alias_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConnectionAssignment.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ConnectionAssignment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConnectionAssignment.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ConnectionAssignment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConnectionAssignment.
        Possible lifecycle states for connection assignments.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConnectionAssignment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConnectionAssignment.
        Possible lifecycle states for connection assignments.


        :param lifecycle_state: The lifecycle_state of this ConnectionAssignment.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConnectionAssignment.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ConnectionAssignment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConnectionAssignment.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ConnectionAssignment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ConnectionAssignment.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ConnectionAssignment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ConnectionAssignment.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ConnectionAssignment.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
