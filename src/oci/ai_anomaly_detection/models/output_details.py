# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OutputDetails(object):
    """
    Detect anomaly job output details.
    """

    #: A constant which can be used with the output_type property of a OutputDetails.
    #: This constant has a value of "OBJECT_STORAGE"
    OUTPUT_TYPE_OBJECT_STORAGE = "OBJECT_STORAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new OutputDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_anomaly_detection.models.ObjectStoreOutputDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this OutputDetails.
            Allowed values for this property are: "OBJECT_STORAGE"
        :type output_type: str

        """
        self.swagger_types = {
            'output_type': 'str'
        }

        self.attribute_map = {
            'output_type': 'outputType'
        }

        self._output_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['outputType']

        if type == 'OBJECT_STORAGE':
            return 'ObjectStoreOutputDetails'
        else:
            return 'OutputDetails'

    @property
    def output_type(self):
        """
        **[Required]** Gets the output_type of this OutputDetails.
        The type of output location.
        Allowed values are:
        - `OBJECT_STORAGE`: Object store output location.

        Allowed values for this property are: "OBJECT_STORAGE"


        :return: The output_type of this OutputDetails.
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """
        Sets the output_type of this OutputDetails.
        The type of output location.
        Allowed values are:
        - `OBJECT_STORAGE`: Object store output location.


        :param output_type: The output_type of this OutputDetails.
        :type: str
        """
        allowed_values = ["OBJECT_STORAGE"]
        if not value_allowed_none_or_none_sentinel(output_type, allowed_values):
            raise ValueError(
                "Invalid value for `output_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._output_type = output_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
