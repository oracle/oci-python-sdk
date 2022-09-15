# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgentDependencySummary(object):
    """
    Description of the AgentDependency, which is a sub-resource of the external environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AgentDependencySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AgentDependencySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AgentDependencySummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AgentDependencySummary.
        :type compartment_id: str

        :param dependency_name:
            The value to assign to the dependency_name property of this AgentDependencySummary.
        :type dependency_name: str

        :param dependency_version:
            The value to assign to the dependency_version property of this AgentDependencySummary.
        :type dependency_version: str

        :param description:
            The value to assign to the description property of this AgentDependencySummary.
        :type description: str

        :param namespace:
            The value to assign to the namespace property of this AgentDependencySummary.
        :type namespace: str

        :param bucket:
            The value to assign to the bucket property of this AgentDependencySummary.
        :type bucket: str

        :param object_name:
            The value to assign to the object_name property of this AgentDependencySummary.
        :type object_name: str

        :param time_created:
            The value to assign to the time_created property of this AgentDependencySummary.
        :type time_created: datetime

        :param e_tag:
            The value to assign to the e_tag property of this AgentDependencySummary.
        :type e_tag: str

        :param checksum:
            The value to assign to the checksum property of this AgentDependencySummary.
        :type checksum: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AgentDependencySummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AgentDependencySummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AgentDependencySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AgentDependencySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AgentDependencySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'dependency_name': 'str',
            'dependency_version': 'str',
            'description': 'str',
            'namespace': 'str',
            'bucket': 'str',
            'object_name': 'str',
            'time_created': 'datetime',
            'e_tag': 'str',
            'checksum': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'dependency_name': 'dependencyName',
            'dependency_version': 'dependencyVersion',
            'description': 'description',
            'namespace': 'namespace',
            'bucket': 'bucket',
            'object_name': 'objectName',
            'time_created': 'timeCreated',
            'e_tag': 'eTag',
            'checksum': 'checksum',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._dependency_name = None
        self._dependency_version = None
        self._description = None
        self._namespace = None
        self._bucket = None
        self._object_name = None
        self._time_created = None
        self._e_tag = None
        self._checksum = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AgentDependencySummary.
        Unique identifier that is immutable on creation.


        :return: The id of this AgentDependencySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AgentDependencySummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this AgentDependencySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AgentDependencySummary.
        Display name of the Agent dependency.


        :return: The display_name of this AgentDependencySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AgentDependencySummary.
        Display name of the Agent dependency.


        :param display_name: The display_name of this AgentDependencySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AgentDependencySummary.
        Compartment identifier.


        :return: The compartment_id of this AgentDependencySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AgentDependencySummary.
        Compartment identifier.


        :param compartment_id: The compartment_id of this AgentDependencySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dependency_name(self):
        """
        **[Required]** Gets the dependency_name of this AgentDependencySummary.
        Name of the dependency type. This should match the whitelisted enum of dependency names.


        :return: The dependency_name of this AgentDependencySummary.
        :rtype: str
        """
        return self._dependency_name

    @dependency_name.setter
    def dependency_name(self, dependency_name):
        """
        Sets the dependency_name of this AgentDependencySummary.
        Name of the dependency type. This should match the whitelisted enum of dependency names.


        :param dependency_name: The dependency_name of this AgentDependencySummary.
        :type: str
        """
        self._dependency_name = dependency_name

    @property
    def dependency_version(self):
        """
        Gets the dependency_version of this AgentDependencySummary.
        Version of the Agent dependency.


        :return: The dependency_version of this AgentDependencySummary.
        :rtype: str
        """
        return self._dependency_version

    @dependency_version.setter
    def dependency_version(self, dependency_version):
        """
        Sets the dependency_version of this AgentDependencySummary.
        Version of the Agent dependency.


        :param dependency_version: The dependency_version of this AgentDependencySummary.
        :type: str
        """
        self._dependency_version = dependency_version

    @property
    def description(self):
        """
        Gets the description of this AgentDependencySummary.
        Description about the Agent dependency.


        :return: The description of this AgentDependencySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AgentDependencySummary.
        Description about the Agent dependency.


        :param description: The description of this AgentDependencySummary.
        :type: str
        """
        self._description = description

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this AgentDependencySummary.
        Object storage namespace associated with the customer's tenancy.


        :return: The namespace of this AgentDependencySummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this AgentDependencySummary.
        Object storage namespace associated with the customer's tenancy.


        :param namespace: The namespace of this AgentDependencySummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        **[Required]** Gets the bucket of this AgentDependencySummary.
        Object storage bucket where the Agent dependency is uploaded.


        :return: The bucket of this AgentDependencySummary.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this AgentDependencySummary.
        Object storage bucket where the Agent dependency is uploaded.


        :param bucket: The bucket of this AgentDependencySummary.
        :type: str
        """
        self._bucket = bucket

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this AgentDependencySummary.
        Name of the dependency object uploaded by the customer.


        :return: The object_name of this AgentDependencySummary.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this AgentDependencySummary.
        Name of the dependency object uploaded by the customer.


        :param object_name: The object_name of this AgentDependencySummary.
        :type: str
        """
        self._object_name = object_name

    @property
    def time_created(self):
        """
        Gets the time_created of this AgentDependencySummary.
        The time when the AgentDependency was created. An RFC3339 formatted datetime string.


        :return: The time_created of this AgentDependencySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AgentDependencySummary.
        The time when the AgentDependency was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this AgentDependencySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def e_tag(self):
        """
        Gets the e_tag of this AgentDependencySummary.
        The eTag associated with the dependency object returned by Object Storage.


        :return: The e_tag of this AgentDependencySummary.
        :rtype: str
        """
        return self._e_tag

    @e_tag.setter
    def e_tag(self, e_tag):
        """
        Sets the e_tag of this AgentDependencySummary.
        The eTag associated with the dependency object returned by Object Storage.


        :param e_tag: The e_tag of this AgentDependencySummary.
        :type: str
        """
        self._e_tag = e_tag

    @property
    def checksum(self):
        """
        Gets the checksum of this AgentDependencySummary.
        The checksum associated with the dependency object returned by Object Storage.


        :return: The checksum of this AgentDependencySummary.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this AgentDependencySummary.
        The checksum associated with the dependency object returned by Object Storage.


        :param checksum: The checksum of this AgentDependencySummary.
        :type: str
        """
        self._checksum = checksum

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AgentDependencySummary.
        The current state of the external environment.


        :return: The lifecycle_state of this AgentDependencySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AgentDependencySummary.
        The current state of the external environment.


        :param lifecycle_state: The lifecycle_state of this AgentDependencySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AgentDependencySummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this AgentDependencySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AgentDependencySummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this AgentDependencySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AgentDependencySummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AgentDependencySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AgentDependencySummary.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AgentDependencySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AgentDependencySummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AgentDependencySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AgentDependencySummary.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AgentDependencySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AgentDependencySummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this AgentDependencySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AgentDependencySummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this AgentDependencySummary.
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
