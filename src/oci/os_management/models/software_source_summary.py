# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftwareSourceSummary(object):
    """
    A software source contains a collection of packages
    """

    #: A constant which can be used with the status property of a SoftwareSourceSummary.
    #: This constant has a value of "NORMAL"
    STATUS_NORMAL = "NORMAL"

    #: A constant which can be used with the status property of a SoftwareSourceSummary.
    #: This constant has a value of "UNREACHABLE"
    STATUS_UNREACHABLE = "UNREACHABLE"

    #: A constant which can be used with the status property of a SoftwareSourceSummary.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a SoftwareSourceSummary.
    #: This constant has a value of "WARNING"
    STATUS_WARNING = "WARNING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSourceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSourceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSourceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSourceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSourceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SoftwareSourceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SoftwareSourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SoftwareSourceSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this SoftwareSourceSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SoftwareSourceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SoftwareSourceSummary.
        :type display_name: str

        :param repo_type:
            The value to assign to the repo_type property of this SoftwareSourceSummary.
        :type repo_type: str

        :param status:
            The value to assign to the status property of this SoftwareSourceSummary.
            Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param packages:
            The value to assign to the packages property of this SoftwareSourceSummary.
        :type packages: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SoftwareSourceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param parent_id:
            The value to assign to the parent_id property of this SoftwareSourceSummary.
        :type parent_id: str

        :param parent_name:
            The value to assign to the parent_name property of this SoftwareSourceSummary.
        :type parent_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SoftwareSourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SoftwareSourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'repo_type': 'str',
            'status': 'str',
            'packages': 'int',
            'lifecycle_state': 'str',
            'parent_id': 'str',
            'parent_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'repo_type': 'repoType',
            'status': 'status',
            'packages': 'packages',
            'lifecycle_state': 'lifecycleState',
            'parent_id': 'parentId',
            'parent_name': 'parentName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._description = None
        self._compartment_id = None
        self._display_name = None
        self._repo_type = None
        self._status = None
        self._packages = None
        self._lifecycle_state = None
        self._parent_id = None
        self._parent_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SoftwareSourceSummary.
        OCID for the Software Source


        :return: The id of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SoftwareSourceSummary.
        OCID for the Software Source


        :param id: The id of this SoftwareSourceSummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this SoftwareSourceSummary.
        Information specified by the user about the software source


        :return: The description of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SoftwareSourceSummary.
        Information specified by the user about the software source


        :param description: The description of this SoftwareSourceSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SoftwareSourceSummary.
        OCID for the Compartment


        :return: The compartment_id of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SoftwareSourceSummary.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this SoftwareSourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SoftwareSourceSummary.
        User friendly name for the software source


        :return: The display_name of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SoftwareSourceSummary.
        User friendly name for the software source


        :param display_name: The display_name of this SoftwareSourceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def repo_type(self):
        """
        **[Required]** Gets the repo_type of this SoftwareSourceSummary.
        Type of the Software Source


        :return: The repo_type of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """
        Sets the repo_type of this SoftwareSourceSummary.
        Type of the Software Source


        :param repo_type: The repo_type of this SoftwareSourceSummary.
        :type: str
        """
        self._repo_type = repo_type

    @property
    def status(self):
        """
        Gets the status of this SoftwareSourceSummary.
        status of the software source.

        Allowed values for this property are: "NORMAL", "UNREACHABLE", "ERROR", "WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SoftwareSourceSummary.
        status of the software source.


        :param status: The status of this SoftwareSourceSummary.
        :type: str
        """
        allowed_values = ["NORMAL", "UNREACHABLE", "ERROR", "WARNING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def packages(self):
        """
        Gets the packages of this SoftwareSourceSummary.
        Number of packages


        :return: The packages of this SoftwareSourceSummary.
        :rtype: int
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this SoftwareSourceSummary.
        Number of packages


        :param packages: The packages of this SoftwareSourceSummary.
        :type: int
        """
        self._packages = packages

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SoftwareSourceSummary.
        The current state of the software source.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SoftwareSourceSummary.
        The current state of the software source.


        :param lifecycle_state: The lifecycle_state of this SoftwareSourceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def parent_id(self):
        """
        Gets the parent_id of this SoftwareSourceSummary.
        OCID for the parent software source, if there is one


        :return: The parent_id of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this SoftwareSourceSummary.
        OCID for the parent software source, if there is one


        :param parent_id: The parent_id of this SoftwareSourceSummary.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def parent_name(self):
        """
        Gets the parent_name of this SoftwareSourceSummary.
        Display name the parent software source, if there is one


        :return: The parent_name of this SoftwareSourceSummary.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """
        Sets the parent_name of this SoftwareSourceSummary.
        Display name the parent software source, if there is one


        :param parent_name: The parent_name of this SoftwareSourceSummary.
        :type: str
        """
        self._parent_name = parent_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SoftwareSourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this SoftwareSourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SoftwareSourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this SoftwareSourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SoftwareSourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this SoftwareSourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SoftwareSourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this SoftwareSourceSummary.
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
