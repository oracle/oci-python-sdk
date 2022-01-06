# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExternalPluggableDatabaseDetails(object):
    """
    Details for creating an external pluggable database resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExternalPluggableDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_id:
            The value to assign to the source_id property of this CreateExternalPluggableDatabaseDetails.
        :type source_id: str

        :param external_container_database_id:
            The value to assign to the external_container_database_id property of this CreateExternalPluggableDatabaseDetails.
        :type external_container_database_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateExternalPluggableDatabaseDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateExternalPluggableDatabaseDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateExternalPluggableDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateExternalPluggableDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'source_id': 'str',
            'external_container_database_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'source_id': 'sourceId',
            'external_container_database_id': 'externalContainerDatabaseId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._source_id = None
        self._external_container_database_id = None
        self._compartment_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def source_id(self):
        """
        Gets the source_id of this CreateExternalPluggableDatabaseDetails.
        The `OCID`__ of the the non-container database that was converted
        to a pluggable database to create this resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_id of this CreateExternalPluggableDatabaseDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this CreateExternalPluggableDatabaseDetails.
        The `OCID`__ of the the non-container database that was converted
        to a pluggable database to create this resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this CreateExternalPluggableDatabaseDetails.
        :type: str
        """
        self._source_id = source_id

    @property
    def external_container_database_id(self):
        """
        **[Required]** Gets the external_container_database_id of this CreateExternalPluggableDatabaseDetails.
        The `OCID`__ of the
        :func:`create_external_container_database_details` that contains
        the specified :func:`create_external_pluggable_database_details` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The external_container_database_id of this CreateExternalPluggableDatabaseDetails.
        :rtype: str
        """
        return self._external_container_database_id

    @external_container_database_id.setter
    def external_container_database_id(self, external_container_database_id):
        """
        Sets the external_container_database_id of this CreateExternalPluggableDatabaseDetails.
        The `OCID`__ of the
        :func:`create_external_container_database_details` that contains
        the specified :func:`create_external_pluggable_database_details` resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param external_container_database_id: The external_container_database_id of this CreateExternalPluggableDatabaseDetails.
        :type: str
        """
        self._external_container_database_id = external_container_database_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateExternalPluggableDatabaseDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateExternalPluggableDatabaseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateExternalPluggableDatabaseDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateExternalPluggableDatabaseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateExternalPluggableDatabaseDetails.
        The user-friendly name for the external database. The name does not have to be unique.


        :return: The display_name of this CreateExternalPluggableDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateExternalPluggableDatabaseDetails.
        The user-friendly name for the external database. The name does not have to be unique.


        :param display_name: The display_name of this CreateExternalPluggableDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateExternalPluggableDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateExternalPluggableDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateExternalPluggableDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateExternalPluggableDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateExternalPluggableDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateExternalPluggableDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateExternalPluggableDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateExternalPluggableDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
