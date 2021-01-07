# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExternalPublicationValidationDetails(object):
    """
    The task type contains the audit summary information and the definition of the task that is published externally.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExternalPublicationValidationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateExternalPublicationValidationDetails.
        :type key: str

        """
        self.swagger_types = {
            'key': 'str'
        }

        self.attribute_map = {
            'key': 'key'
        }

        self._key = None

    @property
    def key(self):
        """
        Gets the key of this CreateExternalPublicationValidationDetails.
        Generated key that can be used in API calls to identify the task. On scenarios where reference to the task is needed, a value can be passed in the create operation.


        :return: The key of this CreateExternalPublicationValidationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateExternalPublicationValidationDetails.
        Generated key that can be used in API calls to identify the task. On scenarios where reference to the task is needed, a value can be passed in the create operation.


        :param key: The key of this CreateExternalPublicationValidationDetails.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
