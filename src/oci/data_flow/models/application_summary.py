# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationSummary(object):
    """
    A data flow application object used in bulk listings.
    """

    #: A constant which can be used with the language property of a ApplicationSummary.
    #: This constant has a value of "SCALA"
    LANGUAGE_SCALA = "SCALA"

    #: A constant which can be used with the language property of a ApplicationSummary.
    #: This constant has a value of "JAVA"
    LANGUAGE_JAVA = "JAVA"

    #: A constant which can be used with the language property of a ApplicationSummary.
    #: This constant has a value of "PYTHON"
    LANGUAGE_PYTHON = "PYTHON"

    #: A constant which can be used with the language property of a ApplicationSummary.
    #: This constant has a value of "SQL"
    LANGUAGE_SQL = "SQL"

    #: A constant which can be used with the lifecycle_state property of a ApplicationSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApplicationSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ApplicationSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ApplicationSummary.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ApplicationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ApplicationSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApplicationSummary.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this ApplicationSummary.
        :type id: str

        :param language:
            The value to assign to the language property of this ApplicationSummary.
            Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type language: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApplicationSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param owner_principal_id:
            The value to assign to the owner_principal_id property of this ApplicationSummary.
        :type owner_principal_id: str

        :param owner_user_name:
            The value to assign to the owner_user_name property of this ApplicationSummary.
        :type owner_user_name: str

        :param time_created:
            The value to assign to the time_created property of this ApplicationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApplicationSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'language': 'str',
            'lifecycle_state': 'str',
            'owner_principal_id': 'str',
            'owner_user_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'language': 'language',
            'lifecycle_state': 'lifecycleState',
            'owner_principal_id': 'ownerPrincipalId',
            'owner_user_name': 'ownerUserName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._language = None
        self._lifecycle_state = None
        self._owner_principal_id = None
        self._owner_user_name = None
        self._time_created = None
        self._time_updated = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ApplicationSummary.
        The OCID of a compartment.


        :return: The compartment_id of this ApplicationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ApplicationSummary.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this ApplicationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this ApplicationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ApplicationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApplicationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ApplicationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ApplicationSummary.
        A user-friendly name. This name is not necessarily unique.


        :return: The display_name of this ApplicationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplicationSummary.
        A user-friendly name. This name is not necessarily unique.


        :param display_name: The display_name of this ApplicationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this ApplicationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ApplicationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApplicationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ApplicationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApplicationSummary.
        The application ID.


        :return: The id of this ApplicationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApplicationSummary.
        The application ID.


        :param id: The id of this ApplicationSummary.
        :type: str
        """
        self._id = id

    @property
    def language(self):
        """
        **[Required]** Gets the language of this ApplicationSummary.
        The Spark language.

        Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The language of this ApplicationSummary.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this ApplicationSummary.
        The Spark language.


        :param language: The language of this ApplicationSummary.
        :type: str
        """
        allowed_values = ["SCALA", "JAVA", "PYTHON", "SQL"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            language = 'UNKNOWN_ENUM_VALUE'
        self._language = language

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ApplicationSummary.
        The current state of this application.

        Allowed values for this property are: "ACTIVE", "DELETED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ApplicationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApplicationSummary.
        The current state of this application.


        :param lifecycle_state: The lifecycle_state of this ApplicationSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def owner_principal_id(self):
        """
        **[Required]** Gets the owner_principal_id of this ApplicationSummary.
        The OCID of the user who created the resource.


        :return: The owner_principal_id of this ApplicationSummary.
        :rtype: str
        """
        return self._owner_principal_id

    @owner_principal_id.setter
    def owner_principal_id(self, owner_principal_id):
        """
        Sets the owner_principal_id of this ApplicationSummary.
        The OCID of the user who created the resource.


        :param owner_principal_id: The owner_principal_id of this ApplicationSummary.
        :type: str
        """
        self._owner_principal_id = owner_principal_id

    @property
    def owner_user_name(self):
        """
        Gets the owner_user_name of this ApplicationSummary.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :return: The owner_user_name of this ApplicationSummary.
        :rtype: str
        """
        return self._owner_user_name

    @owner_user_name.setter
    def owner_user_name(self, owner_user_name):
        """
        Sets the owner_user_name of this ApplicationSummary.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :param owner_user_name: The owner_user_name of this ApplicationSummary.
        :type: str
        """
        self._owner_user_name = owner_user_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ApplicationSummary.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ApplicationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApplicationSummary.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ApplicationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ApplicationSummary.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ApplicationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ApplicationSummary.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ApplicationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
