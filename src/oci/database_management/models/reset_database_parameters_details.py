# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResetDatabaseParametersDetails(object):
    """
    The details required to reset database parameter values.
    """

    #: A constant which can be used with the scope property of a ResetDatabaseParametersDetails.
    #: This constant has a value of "MEMORY"
    SCOPE_MEMORY = "MEMORY"

    #: A constant which can be used with the scope property of a ResetDatabaseParametersDetails.
    #: This constant has a value of "SPFILE"
    SCOPE_SPFILE = "SPFILE"

    #: A constant which can be used with the scope property of a ResetDatabaseParametersDetails.
    #: This constant has a value of "BOTH"
    SCOPE_BOTH = "BOTH"

    def __init__(self, **kwargs):
        """
        Initializes a new ResetDatabaseParametersDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credentials:
            The value to assign to the credentials property of this ResetDatabaseParametersDetails.
        :type credentials: oci.database_management.models.DatabaseCredentials

        :param scope:
            The value to assign to the scope property of this ResetDatabaseParametersDetails.
            Allowed values for this property are: "MEMORY", "SPFILE", "BOTH"
        :type scope: str

        :param parameters:
            The value to assign to the parameters property of this ResetDatabaseParametersDetails.
        :type parameters: list[str]

        """
        self.swagger_types = {
            'credentials': 'DatabaseCredentials',
            'scope': 'str',
            'parameters': 'list[str]'
        }

        self.attribute_map = {
            'credentials': 'credentials',
            'scope': 'scope',
            'parameters': 'parameters'
        }

        self._credentials = None
        self._scope = None
        self._parameters = None

    @property
    def credentials(self):
        """
        **[Required]** Gets the credentials of this ResetDatabaseParametersDetails.

        :return: The credentials of this ResetDatabaseParametersDetails.
        :rtype: oci.database_management.models.DatabaseCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ResetDatabaseParametersDetails.

        :param credentials: The credentials of this ResetDatabaseParametersDetails.
        :type: oci.database_management.models.DatabaseCredentials
        """
        self._credentials = credentials

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this ResetDatabaseParametersDetails.
        The clause used to specify when the parameter change takes effect.

        Use `MEMORY` to make the change in memory and ensure that it takes
        effect immediately. Use `SPFILE` to make the change in the server
        parameter file. The change takes effect when the database is next
        shut down and started up again. Use `BOTH` to make the change in
        memory and in the server parameter file. The change takes effect
        immediately and persists after the database is shut down and
        started up again.

        Allowed values for this property are: "MEMORY", "SPFILE", "BOTH"


        :return: The scope of this ResetDatabaseParametersDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this ResetDatabaseParametersDetails.
        The clause used to specify when the parameter change takes effect.

        Use `MEMORY` to make the change in memory and ensure that it takes
        effect immediately. Use `SPFILE` to make the change in the server
        parameter file. The change takes effect when the database is next
        shut down and started up again. Use `BOTH` to make the change in
        memory and in the server parameter file. The change takes effect
        immediately and persists after the database is shut down and
        started up again.


        :param scope: The scope of this ResetDatabaseParametersDetails.
        :type: str
        """
        allowed_values = ["MEMORY", "SPFILE", "BOTH"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            raise ValueError(
                "Invalid value for `scope`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._scope = scope

    @property
    def parameters(self):
        """
        **[Required]** Gets the parameters of this ResetDatabaseParametersDetails.
        A list of database parameter names.


        :return: The parameters of this ResetDatabaseParametersDetails.
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ResetDatabaseParametersDetails.
        A list of database parameter names.


        :param parameters: The parameters of this ResetDatabaseParametersDetails.
        :type: list[str]
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
