# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseToolsConnectionDetails(object):
    """
    The information about new DatabaseToolsConnection.
    """

    #: A constant which can be used with the type property of a CreateDatabaseToolsConnectionDetails.
    #: This constant has a value of "ORACLE_DATABASE"
    TYPE_ORACLE_DATABASE = "ORACLE_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseToolsConnectionDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_tools.models.CreateDatabaseToolsConnectionOracleDatabaseDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDatabaseToolsConnectionDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDatabaseToolsConnectionDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseToolsConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseToolsConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param type:
            The value to assign to the type property of this CreateDatabaseToolsConnectionDetails.
            Allowed values for this property are: "ORACLE_DATABASE"
        :type type: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'type': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'type': 'type'
        }

        self._display_name = None
        self._compartment_id = None
        self._defined_tags = None
        self._freeform_tags = None
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'ORACLE_DATABASE':
            return 'CreateDatabaseToolsConnectionOracleDatabaseDetails'
        else:
            return 'CreateDatabaseToolsConnectionDetails'

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDatabaseToolsConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateDatabaseToolsConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDatabaseToolsConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDatabaseToolsConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDatabaseToolsConnectionDetails.
        The `OCID`__ of the containing Compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDatabaseToolsConnectionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDatabaseToolsConnectionDetails.
        The `OCID`__ of the containing Compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDatabaseToolsConnectionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseToolsConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDatabaseToolsConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseToolsConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDatabaseToolsConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseToolsConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDatabaseToolsConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseToolsConnectionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDatabaseToolsConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateDatabaseToolsConnectionDetails.
        The DatabaseToolsConnection type.

        Allowed values for this property are: "ORACLE_DATABASE"


        :return: The type of this CreateDatabaseToolsConnectionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateDatabaseToolsConnectionDetails.
        The DatabaseToolsConnection type.


        :param type: The type of this CreateDatabaseToolsConnectionDetails.
        :type: str
        """
        allowed_values = ["ORACLE_DATABASE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
