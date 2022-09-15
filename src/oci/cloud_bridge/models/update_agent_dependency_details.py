# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAgentDependencyDetails(object):
    """
    The information about new AgentDependency.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAgentDependencyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAgentDependencyDetails.
        :type display_name: str

        :param dependency_name:
            The value to assign to the dependency_name property of this UpdateAgentDependencyDetails.
        :type dependency_name: str

        :param dependency_version:
            The value to assign to the dependency_version property of this UpdateAgentDependencyDetails.
        :type dependency_version: str

        :param description:
            The value to assign to the description property of this UpdateAgentDependencyDetails.
        :type description: str

        :param namespace:
            The value to assign to the namespace property of this UpdateAgentDependencyDetails.
        :type namespace: str

        :param bucket:
            The value to assign to the bucket property of this UpdateAgentDependencyDetails.
        :type bucket: str

        :param object_name:
            The value to assign to the object_name property of this UpdateAgentDependencyDetails.
        :type object_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAgentDependencyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAgentDependencyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this UpdateAgentDependencyDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'dependency_name': 'str',
            'dependency_version': 'str',
            'description': 'str',
            'namespace': 'str',
            'bucket': 'str',
            'object_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'dependency_name': 'dependencyName',
            'dependency_version': 'dependencyVersion',
            'description': 'description',
            'namespace': 'namespace',
            'bucket': 'bucket',
            'object_name': 'objectName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._dependency_name = None
        self._dependency_version = None
        self._description = None
        self._namespace = None
        self._bucket = None
        self._object_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAgentDependencyDetails.
        Display name of the Agent dependency.


        :return: The display_name of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAgentDependencyDetails.
        Display name of the Agent dependency.


        :param display_name: The display_name of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def dependency_name(self):
        """
        Gets the dependency_name of this UpdateAgentDependencyDetails.
        Name of the dependency type. This should match the whitelisted enum of dependency names.


        :return: The dependency_name of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._dependency_name

    @dependency_name.setter
    def dependency_name(self, dependency_name):
        """
        Sets the dependency_name of this UpdateAgentDependencyDetails.
        Name of the dependency type. This should match the whitelisted enum of dependency names.


        :param dependency_name: The dependency_name of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._dependency_name = dependency_name

    @property
    def dependency_version(self):
        """
        Gets the dependency_version of this UpdateAgentDependencyDetails.
        Version of the Agent dependency.


        :return: The dependency_version of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._dependency_version

    @dependency_version.setter
    def dependency_version(self, dependency_version):
        """
        Sets the dependency_version of this UpdateAgentDependencyDetails.
        Version of the Agent dependency.


        :param dependency_version: The dependency_version of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._dependency_version = dependency_version

    @property
    def description(self):
        """
        Gets the description of this UpdateAgentDependencyDetails.
        Description about the Agent dependency.


        :return: The description of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAgentDependencyDetails.
        Description about the Agent dependency.


        :param description: The description of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._description = description

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdateAgentDependencyDetails.
        Object storage namespace associated with the customer's tenancy.


        :return: The namespace of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdateAgentDependencyDetails.
        Object storage namespace associated with the customer's tenancy.


        :param namespace: The namespace of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket(self):
        """
        Gets the bucket of this UpdateAgentDependencyDetails.
        Object storage bucket where the dependency is uploaded.


        :return: The bucket of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this UpdateAgentDependencyDetails.
        Object storage bucket where the dependency is uploaded.


        :param bucket: The bucket of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._bucket = bucket

    @property
    def object_name(self):
        """
        Gets the object_name of this UpdateAgentDependencyDetails.
        Name of the dependency object uploaded by the customer.


        :return: The object_name of this UpdateAgentDependencyDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this UpdateAgentDependencyDetails.
        Name of the dependency object uploaded by the customer.


        :param object_name: The object_name of this UpdateAgentDependencyDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAgentDependencyDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAgentDependencyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAgentDependencyDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAgentDependencyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAgentDependencyDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAgentDependencyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAgentDependencyDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAgentDependencyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this UpdateAgentDependencyDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this UpdateAgentDependencyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this UpdateAgentDependencyDetails.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this UpdateAgentDependencyDetails.
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
