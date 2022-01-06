# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CancelDeploymentDetails(object):
    """
    The information regarding the deployment to be canceled.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CancelDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reason:
            The value to assign to the reason property of this CancelDeploymentDetails.
        :type reason: str

        """
        self.swagger_types = {
            'reason': 'str'
        }

        self.attribute_map = {
            'reason': 'reason'
        }

        self._reason = None

    @property
    def reason(self):
        """
        **[Required]** Gets the reason of this CancelDeploymentDetails.
        The reason for canceling the deployment.


        :return: The reason of this CancelDeploymentDetails.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this CancelDeploymentDetails.
        The reason for canceling the deployment.


        :param reason: The reason of this CancelDeploymentDetails.
        :type: str
        """
        self._reason = reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
