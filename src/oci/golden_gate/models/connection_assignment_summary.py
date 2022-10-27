# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionAssignmentSummary(object):
    """
    Summary of the Connection Assignment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionAssignmentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConnectionAssignmentSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConnectionAssignmentSummary.
        :type compartment_id: str

        :param connection_id:
            The value to assign to the connection_id property of this ConnectionAssignmentSummary.
        :type connection_id: str

        :param deployment_id:
            The value to assign to the deployment_id property of this ConnectionAssignmentSummary.
        :type deployment_id: str

        :param alias_name:
            The value to assign to the alias_name property of this ConnectionAssignmentSummary.
        :type alias_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConnectionAssignmentSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ConnectionAssignmentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ConnectionAssignmentSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'connection_id': 'str',
            'deployment_id': 'str',
            'alias_name': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'connection_id': 'connectionId',
            'deployment_id': 'deploymentId',
            'alias_name': 'aliasName',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._connection_id = None
        self._deployment_id = None
        self._alias_name = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConnectionAssignmentSummary.
        The `OCID`__ of the connection assignment being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ConnectionAssignmentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionAssignmentSummary.
        The `OCID`__ of the connection assignment being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ConnectionAssignmentSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConnectionAssignmentSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ConnectionAssignmentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConnectionAssignmentSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ConnectionAssignmentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def connection_id(self):
        """
        **[Required]** Gets the connection_id of this ConnectionAssignmentSummary.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The connection_id of this ConnectionAssignmentSummary.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this ConnectionAssignmentSummary.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param connection_id: The connection_id of this ConnectionAssignmentSummary.
        :type: str
        """
        self._connection_id = connection_id

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this ConnectionAssignmentSummary.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this ConnectionAssignmentSummary.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this ConnectionAssignmentSummary.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this ConnectionAssignmentSummary.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def alias_name(self):
        """
        **[Required]** Gets the alias_name of this ConnectionAssignmentSummary.
        Credential store alias.


        :return: The alias_name of this ConnectionAssignmentSummary.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """
        Sets the alias_name of this ConnectionAssignmentSummary.
        Credential store alias.


        :param alias_name: The alias_name of this ConnectionAssignmentSummary.
        :type: str
        """
        self._alias_name = alias_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConnectionAssignmentSummary.
        Possible lifecycle states for connection assignments.


        :return: The lifecycle_state of this ConnectionAssignmentSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConnectionAssignmentSummary.
        Possible lifecycle states for connection assignments.


        :param lifecycle_state: The lifecycle_state of this ConnectionAssignmentSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConnectionAssignmentSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ConnectionAssignmentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConnectionAssignmentSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ConnectionAssignmentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ConnectionAssignmentSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ConnectionAssignmentSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ConnectionAssignmentSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ConnectionAssignmentSummary.
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
