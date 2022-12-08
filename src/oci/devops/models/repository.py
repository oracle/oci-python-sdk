# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Repository(object):
    """
    Repositories containing the source code to build and deploy.
    """

    #: A constant which can be used with the repository_type property of a Repository.
    #: This constant has a value of "MIRRORED"
    REPOSITORY_TYPE_MIRRORED = "MIRRORED"

    #: A constant which can be used with the repository_type property of a Repository.
    #: This constant has a value of "HOSTED"
    REPOSITORY_TYPE_HOSTED = "HOSTED"

    #: A constant which can be used with the lifecycle_state property of a Repository.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Repository.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Repository.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Repository.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the trigger_build_events property of a Repository.
    #: This constant has a value of "PUSH"
    TRIGGER_BUILD_EVENTS_PUSH = "PUSH"

    #: A constant which can be used with the trigger_build_events property of a Repository.
    #: This constant has a value of "COMMIT_UPDATES"
    TRIGGER_BUILD_EVENTS_COMMIT_UPDATES = "COMMIT_UPDATES"

    def __init__(self, **kwargs):
        """
        Initializes a new Repository object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Repository.
        :type id: str

        :param name:
            The value to assign to the name property of this Repository.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Repository.
        :type compartment_id: str

        :param namespace:
            The value to assign to the namespace property of this Repository.
        :type namespace: str

        :param project_id:
            The value to assign to the project_id property of this Repository.
        :type project_id: str

        :param project_name:
            The value to assign to the project_name property of this Repository.
        :type project_name: str

        :param ssh_url:
            The value to assign to the ssh_url property of this Repository.
        :type ssh_url: str

        :param http_url:
            The value to assign to the http_url property of this Repository.
        :type http_url: str

        :param description:
            The value to assign to the description property of this Repository.
        :type description: str

        :param default_branch:
            The value to assign to the default_branch property of this Repository.
        :type default_branch: str

        :param repository_type:
            The value to assign to the repository_type property of this Repository.
            Allowed values for this property are: "MIRRORED", "HOSTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type repository_type: str

        :param mirror_repository_config:
            The value to assign to the mirror_repository_config property of this Repository.
        :type mirror_repository_config: oci.devops.models.MirrorRepositoryConfig

        :param time_created:
            The value to assign to the time_created property of this Repository.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Repository.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Repository.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this Repository.
        :type lifecyle_details: str

        :param branch_count:
            The value to assign to the branch_count property of this Repository.
        :type branch_count: int

        :param commit_count:
            The value to assign to the commit_count property of this Repository.
        :type commit_count: int

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this Repository.
        :type size_in_bytes: int

        :param trigger_build_events:
            The value to assign to the trigger_build_events property of this Repository.
            Allowed values for items in this list are: "PUSH", "COMMIT_UPDATES", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trigger_build_events: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Repository.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Repository.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Repository.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'namespace': 'str',
            'project_id': 'str',
            'project_name': 'str',
            'ssh_url': 'str',
            'http_url': 'str',
            'description': 'str',
            'default_branch': 'str',
            'repository_type': 'str',
            'mirror_repository_config': 'MirrorRepositoryConfig',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'branch_count': 'int',
            'commit_count': 'int',
            'size_in_bytes': 'int',
            'trigger_build_events': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'namespace': 'namespace',
            'project_id': 'projectId',
            'project_name': 'projectName',
            'ssh_url': 'sshUrl',
            'http_url': 'httpUrl',
            'description': 'description',
            'default_branch': 'defaultBranch',
            'repository_type': 'repositoryType',
            'mirror_repository_config': 'mirrorRepositoryConfig',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'branch_count': 'branchCount',
            'commit_count': 'commitCount',
            'size_in_bytes': 'sizeInBytes',
            'trigger_build_events': 'triggerBuildEvents',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._namespace = None
        self._project_id = None
        self._project_name = None
        self._ssh_url = None
        self._http_url = None
        self._description = None
        self._default_branch = None
        self._repository_type = None
        self._mirror_repository_config = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._branch_count = None
        self._commit_count = None
        self._size_in_bytes = None
        self._trigger_build_events = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Repository.
        The OCID of the repository. This value is unique and immutable.


        :return: The id of this Repository.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Repository.
        The OCID of the repository. This value is unique and immutable.


        :param id: The id of this Repository.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Repository.
        Unique name of a repository. This value is mutable.


        :return: The name of this Repository.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Repository.
        Unique name of a repository. This value is mutable.


        :param name: The name of this Repository.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Repository.
        The OCID of the repository's compartment.


        :return: The compartment_id of this Repository.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Repository.
        The OCID of the repository's compartment.


        :param compartment_id: The compartment_id of this Repository.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def namespace(self):
        """
        Gets the namespace of this Repository.
        Tenancy unique namespace.


        :return: The namespace of this Repository.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this Repository.
        Tenancy unique namespace.


        :param namespace: The namespace of this Repository.
        :type: str
        """
        self._namespace = namespace

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Repository.
        The OCID of the DevOps project containing the repository.


        :return: The project_id of this Repository.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Repository.
        The OCID of the DevOps project containing the repository.


        :param project_id: The project_id of this Repository.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """
        Gets the project_name of this Repository.
        Unique project name in a namespace.


        :return: The project_name of this Repository.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """
        Sets the project_name of this Repository.
        Unique project name in a namespace.


        :param project_name: The project_name of this Repository.
        :type: str
        """
        self._project_name = project_name

    @property
    def ssh_url(self):
        """
        Gets the ssh_url of this Repository.
        SSH URL that you use to git clone, pull and push.


        :return: The ssh_url of this Repository.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """
        Sets the ssh_url of this Repository.
        SSH URL that you use to git clone, pull and push.


        :param ssh_url: The ssh_url of this Repository.
        :type: str
        """
        self._ssh_url = ssh_url

    @property
    def http_url(self):
        """
        Gets the http_url of this Repository.
        HTTP URL that you use to git clone, pull and push.


        :return: The http_url of this Repository.
        :rtype: str
        """
        return self._http_url

    @http_url.setter
    def http_url(self, http_url):
        """
        Sets the http_url of this Repository.
        HTTP URL that you use to git clone, pull and push.


        :param http_url: The http_url of this Repository.
        :type: str
        """
        self._http_url = http_url

    @property
    def description(self):
        """
        Gets the description of this Repository.
        Details of the repository. Avoid entering confidential information.


        :return: The description of this Repository.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Repository.
        Details of the repository. Avoid entering confidential information.


        :param description: The description of this Repository.
        :type: str
        """
        self._description = description

    @property
    def default_branch(self):
        """
        Gets the default_branch of this Repository.
        The default branch of the repository.


        :return: The default_branch of this Repository.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """
        Sets the default_branch of this Repository.
        The default branch of the repository.


        :param default_branch: The default_branch of this Repository.
        :type: str
        """
        self._default_branch = default_branch

    @property
    def repository_type(self):
        """
        Gets the repository_type of this Repository.
        Type of repository:
        MIRRORED - Repository created by mirroring an existing repository.
        HOSTED - Repository created and hosted using OCI DevOps code repository.

        Allowed values for this property are: "MIRRORED", "HOSTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The repository_type of this Repository.
        :rtype: str
        """
        return self._repository_type

    @repository_type.setter
    def repository_type(self, repository_type):
        """
        Sets the repository_type of this Repository.
        Type of repository:
        MIRRORED - Repository created by mirroring an existing repository.
        HOSTED - Repository created and hosted using OCI DevOps code repository.


        :param repository_type: The repository_type of this Repository.
        :type: str
        """
        allowed_values = ["MIRRORED", "HOSTED"]
        if not value_allowed_none_or_none_sentinel(repository_type, allowed_values):
            repository_type = 'UNKNOWN_ENUM_VALUE'
        self._repository_type = repository_type

    @property
    def mirror_repository_config(self):
        """
        Gets the mirror_repository_config of this Repository.

        :return: The mirror_repository_config of this Repository.
        :rtype: oci.devops.models.MirrorRepositoryConfig
        """
        return self._mirror_repository_config

    @mirror_repository_config.setter
    def mirror_repository_config(self, mirror_repository_config):
        """
        Sets the mirror_repository_config of this Repository.

        :param mirror_repository_config: The mirror_repository_config of this Repository.
        :type: oci.devops.models.MirrorRepositoryConfig
        """
        self._mirror_repository_config = mirror_repository_config

    @property
    def time_created(self):
        """
        Gets the time_created of this Repository.
        The time the repository was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this Repository.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Repository.
        The time the repository was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this Repository.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Repository.
        The time the repository was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this Repository.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Repository.
        The time the repository was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this Repository.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Repository.
        The current state of the repository.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Repository.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Repository.
        The current state of the repository.


        :param lifecycle_state: The lifecycle_state of this Repository.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this Repository.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecyle_details of this Repository.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this Repository.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecyle_details: The lifecyle_details of this Repository.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def branch_count(self):
        """
        Gets the branch_count of this Repository.
        The count of the branches present in the repository.


        :return: The branch_count of this Repository.
        :rtype: int
        """
        return self._branch_count

    @branch_count.setter
    def branch_count(self, branch_count):
        """
        Sets the branch_count of this Repository.
        The count of the branches present in the repository.


        :param branch_count: The branch_count of this Repository.
        :type: int
        """
        self._branch_count = branch_count

    @property
    def commit_count(self):
        """
        Gets the commit_count of this Repository.
        The count of the commits present in the repository.


        :return: The commit_count of this Repository.
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        """
        Sets the commit_count of this Repository.
        The count of the commits present in the repository.


        :param commit_count: The commit_count of this Repository.
        :type: int
        """
        self._commit_count = commit_count

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this Repository.
        The size of the repository in bytes.


        :return: The size_in_bytes of this Repository.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this Repository.
        The size of the repository in bytes.


        :param size_in_bytes: The size_in_bytes of this Repository.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def trigger_build_events(self):
        """
        Gets the trigger_build_events of this Repository.
        Trigger build events supported for this repository:
        PUSH - Build is triggered when a push event occurs.
        COMMIT_UPDATES - Build is triggered when new commits are mirrored into a repository.

        Allowed values for items in this list are: "PUSH", "COMMIT_UPDATES", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The trigger_build_events of this Repository.
        :rtype: list[str]
        """
        return self._trigger_build_events

    @trigger_build_events.setter
    def trigger_build_events(self, trigger_build_events):
        """
        Sets the trigger_build_events of this Repository.
        Trigger build events supported for this repository:
        PUSH - Build is triggered when a push event occurs.
        COMMIT_UPDATES - Build is triggered when new commits are mirrored into a repository.


        :param trigger_build_events: The trigger_build_events of this Repository.
        :type: list[str]
        """
        allowed_values = ["PUSH", "COMMIT_UPDATES"]
        if trigger_build_events:
            trigger_build_events[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in trigger_build_events]
        self._trigger_build_events = trigger_build_events

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Repository.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Repository.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Repository.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Repository.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Repository.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Repository.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Repository.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Repository.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Repository.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Repository.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Repository.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Repository.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
