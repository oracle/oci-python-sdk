# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataflowApplication(object):
    """
    Minimum information required to recognize a Dataflow Application object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataflowApplication object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_id:
            The value to assign to the application_id property of this DataflowApplication.
        :type application_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DataflowApplication.
        :type compartment_id: str

        :param config_values:
            The value to assign to the config_values property of this DataflowApplication.
        :type config_values: oci.data_integration.models.ConfigValues

        """
        self.swagger_types = {
            'application_id': 'str',
            'compartment_id': 'str',
            'config_values': 'ConfigValues'
        }

        self.attribute_map = {
            'application_id': 'applicationId',
            'compartment_id': 'compartmentId',
            'config_values': 'configValues'
        }

        self._application_id = None
        self._compartment_id = None
        self._config_values = None

    @property
    def application_id(self):
        """
        Gets the application_id of this DataflowApplication.
        The application id for which Oracle Cloud Infrastructure data flow task is to be created.


        :return: The application_id of this DataflowApplication.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this DataflowApplication.
        The application id for which Oracle Cloud Infrastructure data flow task is to be created.


        :param application_id: The application_id of this DataflowApplication.
        :type: str
        """
        self._application_id = application_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DataflowApplication.
        The compartmentId id under which Oracle Cloud Infrastructure dataflow application lies.


        :return: The compartment_id of this DataflowApplication.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataflowApplication.
        The compartmentId id under which Oracle Cloud Infrastructure dataflow application lies.


        :param compartment_id: The compartment_id of this DataflowApplication.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def config_values(self):
        """
        Gets the config_values of this DataflowApplication.

        :return: The config_values of this DataflowApplication.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this DataflowApplication.

        :param config_values: The config_values of this DataflowApplication.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
