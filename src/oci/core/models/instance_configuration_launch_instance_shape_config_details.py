# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationLaunchInstanceShapeConfigDetails(object):
    """
    The shape configuration requested for the instance. If provided, the instance will be created
    with the resources specified. In the case where some properties are missing or
    the entire parameter is not provided, the instance will be created with the default
    configuration values for the provided `shape`.

    Each shape only supports certain configurable values. If the values provided are invalid for the
    provided `shape`, an error will be returned.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationLaunchInstanceShapeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :type ocpus: float

        """
        self.swagger_types = {
            'ocpus': 'float'
        }

        self.attribute_map = {
            'ocpus': 'ocpus'
        }

        self._ocpus = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :return: The ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :param ocpus: The ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :type: float
        """
        self._ocpus = ocpus

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
