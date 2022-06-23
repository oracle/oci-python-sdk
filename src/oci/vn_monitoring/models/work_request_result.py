# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestResult(object):
    """
    Ephemeral data resulting from an asynchronous operation.
    """

    #: A constant which can be used with the result_type property of a WorkRequestResult.
    #: This constant has a value of "PATH_ANALYSIS"
    RESULT_TYPE_PATH_ANALYSIS = "PATH_ANALYSIS"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestResult object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.PathAnalysisWorkRequestResult`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param result_type:
            The value to assign to the result_type property of this WorkRequestResult.
            Allowed values for this property are: "PATH_ANALYSIS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type result_type: str

        """
        self.swagger_types = {
            'result_type': 'str'
        }

        self.attribute_map = {
            'result_type': 'resultType'
        }

        self._result_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['resultType']

        if type == 'PATH_ANALYSIS':
            return 'PathAnalysisWorkRequestResult'
        else:
            return 'WorkRequestResult'

    @property
    def result_type(self):
        """
        **[Required]** Gets the result_type of this WorkRequestResult.
        Type of `WorkRequestResult`.

        Allowed values for this property are: "PATH_ANALYSIS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The result_type of this WorkRequestResult.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """
        Sets the result_type of this WorkRequestResult.
        Type of `WorkRequestResult`.


        :param result_type: The result_type of this WorkRequestResult.
        :type: str
        """
        allowed_values = ["PATH_ANALYSIS"]
        if not value_allowed_none_or_none_sentinel(result_type, allowed_values):
            result_type = 'UNKNOWN_ENUM_VALUE'
        self._result_type = result_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
