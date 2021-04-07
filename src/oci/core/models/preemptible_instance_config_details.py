# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PreemptibleInstanceConfigDetails(object):
    """
    Configuration options for preemptible instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PreemptibleInstanceConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param preemption_action:
            The value to assign to the preemption_action property of this PreemptibleInstanceConfigDetails.
        :type preemption_action: oci.core.models.PreemptionAction

        """
        self.swagger_types = {
            'preemption_action': 'PreemptionAction'
        }

        self.attribute_map = {
            'preemption_action': 'preemptionAction'
        }

        self._preemption_action = None

    @property
    def preemption_action(self):
        """
        **[Required]** Gets the preemption_action of this PreemptibleInstanceConfigDetails.

        :return: The preemption_action of this PreemptibleInstanceConfigDetails.
        :rtype: oci.core.models.PreemptionAction
        """
        return self._preemption_action

    @preemption_action.setter
    def preemption_action(self, preemption_action):
        """
        Sets the preemption_action of this PreemptibleInstanceConfigDetails.

        :param preemption_action: The preemption_action of this PreemptibleInstanceConfigDetails.
        :type: oci.core.models.PreemptionAction
        """
        self._preemption_action = preemption_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
