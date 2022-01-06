# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWaitCriteriaDetails(object):
    """
    Specifies wait criteria for the Wait stage.
    """

    #: A constant which can be used with the wait_type property of a CreateWaitCriteriaDetails.
    #: This constant has a value of "ABSOLUTE_WAIT"
    WAIT_TYPE_ABSOLUTE_WAIT = "ABSOLUTE_WAIT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWaitCriteriaDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.CreateAbsoluteWaitCriteriaDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wait_type:
            The value to assign to the wait_type property of this CreateWaitCriteriaDetails.
            Allowed values for this property are: "ABSOLUTE_WAIT"
        :type wait_type: str

        """
        self.swagger_types = {
            'wait_type': 'str'
        }

        self.attribute_map = {
            'wait_type': 'waitType'
        }

        self._wait_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['waitType']

        if type == 'ABSOLUTE_WAIT':
            return 'CreateAbsoluteWaitCriteriaDetails'
        else:
            return 'CreateWaitCriteriaDetails'

    @property
    def wait_type(self):
        """
        **[Required]** Gets the wait_type of this CreateWaitCriteriaDetails.
        Wait criteria type.

        Allowed values for this property are: "ABSOLUTE_WAIT"


        :return: The wait_type of this CreateWaitCriteriaDetails.
        :rtype: str
        """
        return self._wait_type

    @wait_type.setter
    def wait_type(self, wait_type):
        """
        Sets the wait_type of this CreateWaitCriteriaDetails.
        Wait criteria type.


        :param wait_type: The wait_type of this CreateWaitCriteriaDetails.
        :type: str
        """
        allowed_values = ["ABSOLUTE_WAIT"]
        if not value_allowed_none_or_none_sentinel(wait_type, allowed_values):
            raise ValueError(
                "Invalid value for `wait_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._wait_type = wait_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
