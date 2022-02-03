# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectPrivilegeSummary(object):
    """
    A summary of object privileges.
    """

    #: A constant which can be used with the hierarchy property of a ObjectPrivilegeSummary.
    #: This constant has a value of "YES"
    HIERARCHY_YES = "YES"

    #: A constant which can be used with the hierarchy property of a ObjectPrivilegeSummary.
    #: This constant has a value of "NO"
    HIERARCHY_NO = "NO"

    #: A constant which can be used with the grant_option property of a ObjectPrivilegeSummary.
    #: This constant has a value of "YES"
    GRANT_OPTION_YES = "YES"

    #: A constant which can be used with the grant_option property of a ObjectPrivilegeSummary.
    #: This constant has a value of "NO"
    GRANT_OPTION_NO = "NO"

    #: A constant which can be used with the common property of a ObjectPrivilegeSummary.
    #: This constant has a value of "YES"
    COMMON_YES = "YES"

    #: A constant which can be used with the common property of a ObjectPrivilegeSummary.
    #: This constant has a value of "NO"
    COMMON_NO = "NO"

    #: A constant which can be used with the inherited property of a ObjectPrivilegeSummary.
    #: This constant has a value of "YES"
    INHERITED_YES = "YES"

    #: A constant which can be used with the inherited property of a ObjectPrivilegeSummary.
    #: This constant has a value of "NO"
    INHERITED_NO = "NO"

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectPrivilegeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ObjectPrivilegeSummary.
        :type name: str

        :param schema_type:
            The value to assign to the schema_type property of this ObjectPrivilegeSummary.
        :type schema_type: str

        :param owner:
            The value to assign to the owner property of this ObjectPrivilegeSummary.
        :type owner: str

        :param grantor:
            The value to assign to the grantor property of this ObjectPrivilegeSummary.
        :type grantor: str

        :param hierarchy:
            The value to assign to the hierarchy property of this ObjectPrivilegeSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type hierarchy: str

        :param object:
            The value to assign to the object property of this ObjectPrivilegeSummary.
        :type object: str

        :param grant_option:
            The value to assign to the grant_option property of this ObjectPrivilegeSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type grant_option: str

        :param common:
            The value to assign to the common property of this ObjectPrivilegeSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type common: str

        :param inherited:
            The value to assign to the inherited property of this ObjectPrivilegeSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type inherited: str

        """
        self.swagger_types = {
            'name': 'str',
            'schema_type': 'str',
            'owner': 'str',
            'grantor': 'str',
            'hierarchy': 'str',
            'object': 'str',
            'grant_option': 'str',
            'common': 'str',
            'inherited': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'schema_type': 'schemaType',
            'owner': 'owner',
            'grantor': 'grantor',
            'hierarchy': 'hierarchy',
            'object': 'object',
            'grant_option': 'grantOption',
            'common': 'common',
            'inherited': 'inherited'
        }

        self._name = None
        self._schema_type = None
        self._owner = None
        self._grantor = None
        self._hierarchy = None
        self._object = None
        self._grant_option = None
        self._common = None
        self._inherited = None

    @property
    def name(self):
        """
        Gets the name of this ObjectPrivilegeSummary.
        The name of the privilege on the object.


        :return: The name of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectPrivilegeSummary.
        The name of the privilege on the object.


        :param name: The name of this ObjectPrivilegeSummary.
        :type: str
        """
        self._name = name

    @property
    def schema_type(self):
        """
        Gets the schema_type of this ObjectPrivilegeSummary.
        The type of object.


        :return: The schema_type of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._schema_type

    @schema_type.setter
    def schema_type(self, schema_type):
        """
        Sets the schema_type of this ObjectPrivilegeSummary.
        The type of object.


        :param schema_type: The schema_type of this ObjectPrivilegeSummary.
        :type: str
        """
        self._schema_type = schema_type

    @property
    def owner(self):
        """
        Gets the owner of this ObjectPrivilegeSummary.
        The owner of the object.


        :return: The owner of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this ObjectPrivilegeSummary.
        The owner of the object.


        :param owner: The owner of this ObjectPrivilegeSummary.
        :type: str
        """
        self._owner = owner

    @property
    def grantor(self):
        """
        Gets the grantor of this ObjectPrivilegeSummary.
        The name of the user who granted the object privilege.


        :return: The grantor of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._grantor

    @grantor.setter
    def grantor(self, grantor):
        """
        Sets the grantor of this ObjectPrivilegeSummary.
        The name of the user who granted the object privilege.


        :param grantor: The grantor of this ObjectPrivilegeSummary.
        :type: str
        """
        self._grantor = grantor

    @property
    def hierarchy(self):
        """
        Gets the hierarchy of this ObjectPrivilegeSummary.
        Indicates whether the privilege is granted with the HIERARCHY OPTION (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The hierarchy of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy):
        """
        Sets the hierarchy of this ObjectPrivilegeSummary.
        Indicates whether the privilege is granted with the HIERARCHY OPTION (YES) or not (NO).


        :param hierarchy: The hierarchy of this ObjectPrivilegeSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(hierarchy, allowed_values):
            hierarchy = 'UNKNOWN_ENUM_VALUE'
        self._hierarchy = hierarchy

    @property
    def object(self):
        """
        Gets the object of this ObjectPrivilegeSummary.
        The name of the object. The object can be any object, including tables, packages, indexes, sequences, and so on.


        :return: The object of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ObjectPrivilegeSummary.
        The name of the object. The object can be any object, including tables, packages, indexes, sequences, and so on.


        :param object: The object of this ObjectPrivilegeSummary.
        :type: str
        """
        self._object = object

    @property
    def grant_option(self):
        """
        Gets the grant_option of this ObjectPrivilegeSummary.
        Indicates whether the privilege is granted with the GRANT OPTION (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The grant_option of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._grant_option

    @grant_option.setter
    def grant_option(self, grant_option):
        """
        Sets the grant_option of this ObjectPrivilegeSummary.
        Indicates whether the privilege is granted with the GRANT OPTION (YES) or not (NO).


        :param grant_option: The grant_option of this ObjectPrivilegeSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(grant_option, allowed_values):
            grant_option = 'UNKNOWN_ENUM_VALUE'
        self._grant_option = grant_option

    @property
    def common(self):
        """
        Gets the common of this ObjectPrivilegeSummary.
        Indicates how the object privilege was granted. Possible values:
        YES if the role is granted commonly (CONTAINER=ALL is used)
        NO if the role is granted locally (CONTAINER=ALL is not used)

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The common of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._common

    @common.setter
    def common(self, common):
        """
        Sets the common of this ObjectPrivilegeSummary.
        Indicates how the object privilege was granted. Possible values:
        YES if the role is granted commonly (CONTAINER=ALL is used)
        NO if the role is granted locally (CONTAINER=ALL is not used)


        :param common: The common of this ObjectPrivilegeSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(common, allowed_values):
            common = 'UNKNOWN_ENUM_VALUE'
        self._common = common

    @property
    def inherited(self):
        """
        Gets the inherited of this ObjectPrivilegeSummary.
        Indicates whether the granted privilege is inherited from another container (YES) or not (NO).

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The inherited of this ObjectPrivilegeSummary.
        :rtype: str
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """
        Sets the inherited of this ObjectPrivilegeSummary.
        Indicates whether the granted privilege is inherited from another container (YES) or not (NO).


        :param inherited: The inherited of this ObjectPrivilegeSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(inherited, allowed_values):
            inherited = 'UNKNOWN_ENUM_VALUE'
        self._inherited = inherited

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
