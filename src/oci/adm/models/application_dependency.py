# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationDependency(object):
    """
    An Application Dependency resource creates a Vulnerability Audit.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationDependency object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param gav:
            The value to assign to the gav property of this ApplicationDependency.
        :type gav: str

        :param node_id:
            The value to assign to the node_id property of this ApplicationDependency.
        :type node_id: str

        :param application_dependency_node_ids:
            The value to assign to the application_dependency_node_ids property of this ApplicationDependency.
        :type application_dependency_node_ids: list[str]

        """
        self.swagger_types = {
            'gav': 'str',
            'node_id': 'str',
            'application_dependency_node_ids': 'list[str]'
        }

        self.attribute_map = {
            'gav': 'gav',
            'node_id': 'nodeId',
            'application_dependency_node_ids': 'applicationDependencyNodeIds'
        }

        self._gav = None
        self._node_id = None
        self._application_dependency_node_ids = None

    @property
    def gav(self):
        """
        **[Required]** Gets the gav of this ApplicationDependency.
        Unique Group Artifact Version (GAV) identifier (Group:Artifact:Version), e.g. org.graalvm.nativeimage:svm:21.1.0.


        :return: The gav of this ApplicationDependency.
        :rtype: str
        """
        return self._gav

    @gav.setter
    def gav(self, gav):
        """
        Sets the gav of this ApplicationDependency.
        Unique Group Artifact Version (GAV) identifier (Group:Artifact:Version), e.g. org.graalvm.nativeimage:svm:21.1.0.


        :param gav: The gav of this ApplicationDependency.
        :type: str
        """
        self._gav = gav

    @property
    def node_id(self):
        """
        **[Required]** Gets the node_id of this ApplicationDependency.
        Unique identifier of an Application Dependency node, e.g. nodeId1.


        :return: The node_id of this ApplicationDependency.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this ApplicationDependency.
        Unique identifier of an Application Dependency node, e.g. nodeId1.


        :param node_id: The node_id of this ApplicationDependency.
        :type: str
        """
        self._node_id = node_id

    @property
    def application_dependency_node_ids(self):
        """
        **[Required]** Gets the application_dependency_node_ids of this ApplicationDependency.
        List of (Application Dependencies) node identifiers on which this node depends.


        :return: The application_dependency_node_ids of this ApplicationDependency.
        :rtype: list[str]
        """
        return self._application_dependency_node_ids

    @application_dependency_node_ids.setter
    def application_dependency_node_ids(self, application_dependency_node_ids):
        """
        Sets the application_dependency_node_ids of this ApplicationDependency.
        List of (Application Dependencies) node identifiers on which this node depends.


        :param application_dependency_node_ids: The application_dependency_node_ids of this ApplicationDependency.
        :type: list[str]
        """
        self._application_dependency_node_ids = application_dependency_node_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
