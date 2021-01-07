# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingConfigurationSummary(object):
    """
    The information about auto scale configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingConfigurationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutoScalingConfigurationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AutoScalingConfigurationSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutoScalingConfigurationSummary.
        :type lifecycle_state: str

        :param node_type:
            The value to assign to the node_type property of this AutoScalingConfigurationSummary.
        :type node_type: str

        :param time_created:
            The value to assign to the time_created property of this AutoScalingConfigurationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AutoScalingConfigurationSummary.
        :type time_updated: datetime

        :param policy:
            The value to assign to the policy property of this AutoScalingConfigurationSummary.
        :type policy: oci.bds.models.AutoScalePolicy

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'node_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'policy': 'AutoScalePolicy'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'node_type': 'nodeType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'policy': 'policy'
        }

        self._id = None
        self._display_name = None
        self._lifecycle_state = None
        self._node_type = None
        self._time_created = None
        self._time_updated = None
        self._policy = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutoScalingConfigurationSummary.
        The OCID of the autoscaling configuration.


        :return: The id of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutoScalingConfigurationSummary.
        The OCID of the autoscaling configuration.


        :param id: The id of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutoScalingConfigurationSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutoScalingConfigurationSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutoScalingConfigurationSummary.
        The state of the autoscaling configuration


        :return: The lifecycle_state of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutoScalingConfigurationSummary.
        The state of the autoscaling configuration


        :param lifecycle_state: The lifecycle_state of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this AutoScalingConfigurationSummary.
        A node type that is managed by an autoscaling configuration. The only supported type is WORKER.


        :return: The node_type of this AutoScalingConfigurationSummary.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this AutoScalingConfigurationSummary.
        A node type that is managed by an autoscaling configuration. The only supported type is WORKER.


        :param node_type: The node_type of this AutoScalingConfigurationSummary.
        :type: str
        """
        self._node_type = node_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AutoScalingConfigurationSummary.
        The time the BDS instance was created. An RFC3339 formatted datetime string


        :return: The time_created of this AutoScalingConfigurationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutoScalingConfigurationSummary.
        The time the BDS instance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this AutoScalingConfigurationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AutoScalingConfigurationSummary.
        The time the autoscale configuration was updated.
        An RFC3339 formatted datetime string


        :return: The time_updated of this AutoScalingConfigurationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AutoScalingConfigurationSummary.
        The time the autoscale configuration was updated.
        An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this AutoScalingConfigurationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this AutoScalingConfigurationSummary.

        :return: The policy of this AutoScalingConfigurationSummary.
        :rtype: oci.bds.models.AutoScalePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this AutoScalingConfigurationSummary.

        :param policy: The policy of this AutoScalingConfigurationSummary.
        :type: oci.bds.models.AutoScalePolicy
        """
        self._policy = policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
