# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExternalDatabaseConnectorDetails(object):
    """
    Details for updating an external database connector.
    """

    #: A constant which can be used with the connector_type property of a UpdateExternalDatabaseConnectorDetails.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExternalDatabaseConnectorDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.UpdateExternalMacsConnectorDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateExternalDatabaseConnectorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateExternalDatabaseConnectorDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateExternalDatabaseConnectorDetails.
        :type display_name: str

        :param connector_type:
            The value to assign to the connector_type property of this UpdateExternalDatabaseConnectorDetails.
            Allowed values for this property are: "MACS"
        :type connector_type: str

        """
        self.swagger_types = {
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'connector_type': 'str'
        }

        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'connector_type': 'connectorType'
        }

        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._connector_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'MACS':
            return 'UpdateExternalMacsConnectorDetails'
        else:
            return 'UpdateExternalDatabaseConnectorDetails'

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateExternalDatabaseConnectorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateExternalDatabaseConnectorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateExternalDatabaseConnectorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateExternalDatabaseConnectorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateExternalDatabaseConnectorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateExternalDatabaseConnectorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateExternalDatabaseConnectorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateExternalDatabaseConnectorDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateExternalDatabaseConnectorDetails.
        The user-friendly name for the
        :func:`create_external_database_connector_details`.
        The name does not have to be unique.


        :return: The display_name of this UpdateExternalDatabaseConnectorDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateExternalDatabaseConnectorDetails.
        The user-friendly name for the
        :func:`create_external_database_connector_details`.
        The name does not have to be unique.


        :param display_name: The display_name of this UpdateExternalDatabaseConnectorDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def connector_type(self):
        """
        Gets the connector_type of this UpdateExternalDatabaseConnectorDetails.
        The type of connector used by the external database resource.

        Allowed values for this property are: "MACS"


        :return: The connector_type of this UpdateExternalDatabaseConnectorDetails.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this UpdateExternalDatabaseConnectorDetails.
        The type of connector used by the external database resource.


        :param connector_type: The connector_type of this UpdateExternalDatabaseConnectorDetails.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            raise ValueError(
                "Invalid value for `connector_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._connector_type = connector_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
