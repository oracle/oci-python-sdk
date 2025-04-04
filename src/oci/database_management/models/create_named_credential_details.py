# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNamedCredentialDetails(object):
    """
    The details required to create a named credential.
    """

    #: A constant which can be used with the scope property of a CreateNamedCredentialDetails.
    #: This constant has a value of "RESOURCE"
    SCOPE_RESOURCE = "RESOURCE"

    #: A constant which can be used with the scope property of a CreateNamedCredentialDetails.
    #: This constant has a value of "GLOBAL"
    SCOPE_GLOBAL = "GLOBAL"

    #: A constant which can be used with the type property of a CreateNamedCredentialDetails.
    #: This constant has a value of "ORACLE_DB"
    TYPE_ORACLE_DB = "ORACLE_DB"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNamedCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateNamedCredentialDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateNamedCredentialDetails.
        :type description: str

        :param scope:
            The value to assign to the scope property of this CreateNamedCredentialDetails.
            Allowed values for this property are: "RESOURCE", "GLOBAL"
        :type scope: str

        :param type:
            The value to assign to the type property of this CreateNamedCredentialDetails.
            Allowed values for this property are: "ORACLE_DB"
        :type type: str

        :param content:
            The value to assign to the content property of this CreateNamedCredentialDetails.
        :type content: oci.database_management.models.NamedCredentialContent

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNamedCredentialDetails.
        :type compartment_id: str

        :param associated_resource:
            The value to assign to the associated_resource property of this CreateNamedCredentialDetails.
        :type associated_resource: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNamedCredentialDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNamedCredentialDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'scope': 'str',
            'type': 'str',
            'content': 'NamedCredentialContent',
            'compartment_id': 'str',
            'associated_resource': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'scope': 'scope',
            'type': 'type',
            'content': 'content',
            'compartment_id': 'compartmentId',
            'associated_resource': 'associatedResource',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._name = None
        self._description = None
        self._scope = None
        self._type = None
        self._content = None
        self._compartment_id = None
        self._associated_resource = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateNamedCredentialDetails.
        The name of the named credential. Valid characters are uppercase or
        lowercase letters, numbers, and \"_\". The name of the named credential
        cannot be modified. It must be unique in the compartment and must begin with
        an alphabetic character.


        :return: The name of this CreateNamedCredentialDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateNamedCredentialDetails.
        The name of the named credential. Valid characters are uppercase or
        lowercase letters, numbers, and \"_\". The name of the named credential
        cannot be modified. It must be unique in the compartment and must begin with
        an alphabetic character.


        :param name: The name of this CreateNamedCredentialDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateNamedCredentialDetails.
        The information specified by the user about the named credential.


        :return: The description of this CreateNamedCredentialDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateNamedCredentialDetails.
        The information specified by the user about the named credential.


        :param description: The description of this CreateNamedCredentialDetails.
        :type: str
        """
        self._description = description

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this CreateNamedCredentialDetails.
        The scope of the named credential.

        Allowed values for this property are: "RESOURCE", "GLOBAL"


        :return: The scope of this CreateNamedCredentialDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CreateNamedCredentialDetails.
        The scope of the named credential.


        :param scope: The scope of this CreateNamedCredentialDetails.
        :type: str
        """
        allowed_values = ["RESOURCE", "GLOBAL"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            raise ValueError(
                f"Invalid value for `scope`, must be None or one of {allowed_values}"
            )
        self._scope = scope

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateNamedCredentialDetails.
        The type of resource associated with the named credential.

        Allowed values for this property are: "ORACLE_DB"


        :return: The type of this CreateNamedCredentialDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateNamedCredentialDetails.
        The type of resource associated with the named credential.


        :param type: The type of this CreateNamedCredentialDetails.
        :type: str
        """
        allowed_values = ["ORACLE_DB"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def content(self):
        """
        **[Required]** Gets the content of this CreateNamedCredentialDetails.

        :return: The content of this CreateNamedCredentialDetails.
        :rtype: oci.database_management.models.NamedCredentialContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CreateNamedCredentialDetails.

        :param content: The content of this CreateNamedCredentialDetails.
        :type: oci.database_management.models.NamedCredentialContent
        """
        self._content = content

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateNamedCredentialDetails.
        The `OCID`__ of the compartment
        in which the named credential resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateNamedCredentialDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateNamedCredentialDetails.
        The `OCID`__ of the compartment
        in which the named credential resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateNamedCredentialDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def associated_resource(self):
        """
        Gets the associated_resource of this CreateNamedCredentialDetails.
        The `OCID`__ of the resource that
        is associated to the named credential.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The associated_resource of this CreateNamedCredentialDetails.
        :rtype: str
        """
        return self._associated_resource

    @associated_resource.setter
    def associated_resource(self, associated_resource):
        """
        Sets the associated_resource of this CreateNamedCredentialDetails.
        The `OCID`__ of the resource that
        is associated to the named credential.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param associated_resource: The associated_resource of this CreateNamedCredentialDetails.
        :type: str
        """
        self._associated_resource = associated_resource

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateNamedCredentialDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateNamedCredentialDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateNamedCredentialDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateNamedCredentialDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateNamedCredentialDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateNamedCredentialDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateNamedCredentialDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateNamedCredentialDetails.
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
