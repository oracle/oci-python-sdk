# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CategoryLogDetails(object):
    """
    The log details for each category.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CategoryLogDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access:
            The value to assign to the access property of this CategoryLogDetails.
        :type access: oci.data_science.models.LogDetails

        :param predict:
            The value to assign to the predict property of this CategoryLogDetails.
        :type predict: oci.data_science.models.LogDetails

        """
        self.swagger_types = {
            'access': 'LogDetails',
            'predict': 'LogDetails'
        }

        self.attribute_map = {
            'access': 'access',
            'predict': 'predict'
        }

        self._access = None
        self._predict = None

    @property
    def access(self):
        """
        Gets the access of this CategoryLogDetails.

        :return: The access of this CategoryLogDetails.
        :rtype: oci.data_science.models.LogDetails
        """
        return self._access

    @access.setter
    def access(self, access):
        """
        Sets the access of this CategoryLogDetails.

        :param access: The access of this CategoryLogDetails.
        :type: oci.data_science.models.LogDetails
        """
        self._access = access

    @property
    def predict(self):
        """
        Gets the predict of this CategoryLogDetails.

        :return: The predict of this CategoryLogDetails.
        :rtype: oci.data_science.models.LogDetails
        """
        return self._predict

    @predict.setter
    def predict(self, predict):
        """
        Sets the predict of this CategoryLogDetails.

        :param predict: The predict of this CategoryLogDetails.
        :type: oci.data_science.models.LogDetails
        """
        self._predict = predict

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
