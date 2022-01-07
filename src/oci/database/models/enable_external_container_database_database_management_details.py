# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableExternalContainerDatabaseDatabaseManagementDetails(object):
    """
    Details to enable Database Management on an external container database.
    """

    #: A constant which can be used with the license_model property of a EnableExternalContainerDatabaseDatabaseManagementDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a EnableExternalContainerDatabaseDatabaseManagementDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new EnableExternalContainerDatabaseDatabaseManagementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param license_model:
            The value to assign to the license_model property of this EnableExternalContainerDatabaseDatabaseManagementDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param external_database_connector_id:
            The value to assign to the external_database_connector_id property of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        :type external_database_connector_id: str

        """
        self.swagger_types = {
            'license_model': 'str',
            'external_database_connector_id': 'str'
        }

        self.attribute_map = {
            'license_model': 'licenseModel',
            'external_database_connector_id': 'externalDatabaseConnectorId'
        }

        self._license_model = None
        self._external_database_connector_id = None

    @property
    def license_model(self):
        """
        **[Required]** Gets the license_model of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        The Oracle license model that applies to the external database.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        The Oracle license model that applies to the external database.


        :param license_model: The license_model of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    @property
    def external_database_connector_id(self):
        """
        **[Required]** Gets the external_database_connector_id of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_database_connector_id of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        :rtype: str
        """
        return self._external_database_connector_id

    @external_database_connector_id.setter
    def external_database_connector_id(self, external_database_connector_id):
        """
        Sets the external_database_connector_id of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        The `OCID`__ of the
        :func:`create_external_database_connector_details`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_database_connector_id: The external_database_connector_id of this EnableExternalContainerDatabaseDatabaseManagementDetails.
        :type: str
        """
        self._external_database_connector_id = external_database_connector_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
