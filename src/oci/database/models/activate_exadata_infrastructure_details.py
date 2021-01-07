# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivateExadataInfrastructureDetails(object):
    """
    The activation details for the Exadata Cloud@Customer infrastructure. Applies to Exadata Cloud@Customer instances only.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ActivateExadataInfrastructureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param activation_file:
            The value to assign to the activation_file property of this ActivateExadataInfrastructureDetails.
        :type activation_file: str

        """
        self.swagger_types = {
            'activation_file': 'str'
        }

        self.attribute_map = {
            'activation_file': 'activationFile'
        }

        self._activation_file = None

    @property
    def activation_file(self):
        """
        **[Required]** Gets the activation_file of this ActivateExadataInfrastructureDetails.
        The activation zip file.


        :return: The activation_file of this ActivateExadataInfrastructureDetails.
        :rtype: str
        """
        return self._activation_file

    @activation_file.setter
    def activation_file(self, activation_file):
        """
        Sets the activation_file of this ActivateExadataInfrastructureDetails.
        The activation zip file.


        :param activation_file: The activation_file of this ActivateExadataInfrastructureDetails.
        :type: str
        """
        self._activation_file = activation_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
