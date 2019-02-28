# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingPolicy(object):
    """
    A Policy defines the rules and actions of an AutoScalingConfiguration. The only supported type is 'threshold'
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.autoscaling.models.ThresholdPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity:
            The value to assign to the capacity property of this AutoScalingPolicy.
        :type capacity: Capacity

        :param id:
            The value to assign to the id property of this AutoScalingPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AutoScalingPolicy.
        :type display_name: str

        :param policy_type:
            The value to assign to the policy_type property of this AutoScalingPolicy.
        :type policy_type: str

        :param time_created:
            The value to assign to the time_created property of this AutoScalingPolicy.
        :type time_created: datetime

        """
        self.swagger_types = {
            'capacity': 'Capacity',
            'id': 'str',
            'display_name': 'str',
            'policy_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'id': 'id',
            'display_name': 'displayName',
            'policy_type': 'policyType',
            'time_created': 'timeCreated'
        }

        self._capacity = None
        self._id = None
        self._display_name = None
        self._policy_type = None
        self._time_created = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['policyType']

        if type == 'threshold':
            return 'ThresholdPolicy'
        else:
            return 'AutoScalingPolicy'

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this AutoScalingPolicy.
        The capacity requirements of the Policy


        :return: The capacity of this AutoScalingPolicy.
        :rtype: Capacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this AutoScalingPolicy.
        The capacity requirements of the Policy


        :param capacity: The capacity of this AutoScalingPolicy.
        :type: Capacity
        """
        self._capacity = capacity

    @property
    def id(self):
        """
        Gets the id of this AutoScalingPolicy.
        The ID of the policy that is assigned after creation


        :return: The id of this AutoScalingPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutoScalingPolicy.
        The ID of the policy that is assigned after creation


        :param id: The id of this AutoScalingPolicy.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this AutoScalingPolicy.
        A user-friendly name for the Policy. Does not have to be unique, and it's changeable. Avoid entering
        confidential information.


        :return: The display_name of this AutoScalingPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutoScalingPolicy.
        A user-friendly name for the Policy. Does not have to be unique, and it's changeable. Avoid entering
        confidential information.


        :param display_name: The display_name of this AutoScalingPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def policy_type(self):
        """
        **[Required]** Gets the policy_type of this AutoScalingPolicy.
        Indicates type of Policy


        :return: The policy_type of this AutoScalingPolicy.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """
        Sets the policy_type of this AutoScalingPolicy.
        Indicates type of Policy


        :param policy_type: The policy_type of this AutoScalingPolicy.
        :type: str
        """
        self._policy_type = policy_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AutoScalingPolicy.
        The date and time the AutoScalingConfiguration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this AutoScalingPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutoScalingPolicy.
        The date and time the AutoScalingConfiguration was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this AutoScalingPolicy.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
