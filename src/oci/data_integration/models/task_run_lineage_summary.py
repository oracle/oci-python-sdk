# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskRunLineageSummary(object):
    """
    The information about TaskRunLineage.
    """

    #: A constant which can be used with the task_execution_status property of a TaskRunLineageSummary.
    #: This constant has a value of "SUCCESS"
    TASK_EXECUTION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the task_execution_status property of a TaskRunLineageSummary.
    #: This constant has a value of "ERROR"
    TASK_EXECUTION_STATUS_ERROR = "ERROR"

    #: A constant which can be used with the task_execution_status property of a TaskRunLineageSummary.
    #: This constant has a value of "TERMINATED"
    TASK_EXECUTION_STATUS_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new TaskRunLineageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TaskRunLineageSummary.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this TaskRunLineageSummary.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this TaskRunLineageSummary.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskRunLineageSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskRunLineageSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskRunLineageSummary.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskRunLineageSummary.
        :type object_version: int

        :param task_name:
            The value to assign to the task_name property of this TaskRunLineageSummary.
        :type task_name: str

        :param task_type:
            The value to assign to the task_type property of this TaskRunLineageSummary.
        :type task_type: str

        :param task_key:
            The value to assign to the task_key property of this TaskRunLineageSummary.
        :type task_key: str

        :param is_lineage_gen_completed:
            The value to assign to the is_lineage_gen_completed property of this TaskRunLineageSummary.
        :type is_lineage_gen_completed: bool

        :param task_execution_status:
            The value to assign to the task_execution_status property of this TaskRunLineageSummary.
            Allowed values for this property are: "SUCCESS", "ERROR", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_execution_status: str

        :param flow:
            The value to assign to the flow property of this TaskRunLineageSummary.
        :type flow: oci.data_integration.models.DataFlow

        :param metadata:
            The value to assign to the metadata property of this TaskRunLineageSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'task_name': 'str',
            'task_type': 'str',
            'task_key': 'str',
            'is_lineage_gen_completed': 'bool',
            'task_execution_status': 'str',
            'flow': 'DataFlow',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'task_name': 'taskName',
            'task_type': 'taskType',
            'task_key': 'taskKey',
            'is_lineage_gen_completed': 'isLineageGenCompleted',
            'task_execution_status': 'taskExecutionStatus',
            'flow': 'flow',
            'metadata': 'metadata'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._task_name = None
        self._task_type = None
        self._task_key = None
        self._is_lineage_gen_completed = None
        self._task_execution_status = None
        self._flow = None
        self._metadata = None

    @property
    def key(self):
        """
        Gets the key of this TaskRunLineageSummary.
        The object key.


        :return: The key of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TaskRunLineageSummary.
        The object key.


        :param key: The key of this TaskRunLineageSummary.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this TaskRunLineageSummary.
        The object type.


        :return: The model_type of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this TaskRunLineageSummary.
        The object type.


        :param model_type: The model_type of this TaskRunLineageSummary.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this TaskRunLineageSummary.
        The object's model version.


        :return: The model_version of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this TaskRunLineageSummary.
        The object's model version.


        :param model_version: The model_version of this TaskRunLineageSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this TaskRunLineageSummary.

        :return: The parent_ref of this TaskRunLineageSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this TaskRunLineageSummary.

        :param parent_ref: The parent_ref of this TaskRunLineageSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this TaskRunLineageSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaskRunLineageSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this TaskRunLineageSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TaskRunLineageSummary.
        Detailed description for the object.


        :return: The description of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TaskRunLineageSummary.
        Detailed description for the object.


        :param description: The description of this TaskRunLineageSummary.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this TaskRunLineageSummary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this TaskRunLineageSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this TaskRunLineageSummary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this TaskRunLineageSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def task_name(self):
        """
        Gets the task_name of this TaskRunLineageSummary.
        Task name


        :return: The task_name of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this TaskRunLineageSummary.
        Task name


        :param task_name: The task_name of this TaskRunLineageSummary.
        :type: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """
        Gets the task_type of this TaskRunLineageSummary.
        Task name


        :return: The task_type of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """
        Sets the task_type of this TaskRunLineageSummary.
        Task name


        :param task_type: The task_type of this TaskRunLineageSummary.
        :type: str
        """
        self._task_type = task_type

    @property
    def task_key(self):
        """
        Gets the task_key of this TaskRunLineageSummary.
        The object key.


        :return: The task_key of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._task_key

    @task_key.setter
    def task_key(self, task_key):
        """
        Sets the task_key of this TaskRunLineageSummary.
        The object key.


        :param task_key: The task_key of this TaskRunLineageSummary.
        :type: str
        """
        self._task_key = task_key

    @property
    def is_lineage_gen_completed(self):
        """
        Gets the is_lineage_gen_completed of this TaskRunLineageSummary.
        This value is used to track if lineage generation for a task is completed or not.


        :return: The is_lineage_gen_completed of this TaskRunLineageSummary.
        :rtype: bool
        """
        return self._is_lineage_gen_completed

    @is_lineage_gen_completed.setter
    def is_lineage_gen_completed(self, is_lineage_gen_completed):
        """
        Sets the is_lineage_gen_completed of this TaskRunLineageSummary.
        This value is used to track if lineage generation for a task is completed or not.


        :param is_lineage_gen_completed: The is_lineage_gen_completed of this TaskRunLineageSummary.
        :type: bool
        """
        self._is_lineage_gen_completed = is_lineage_gen_completed

    @property
    def task_execution_status(self):
        """
        Gets the task_execution_status of this TaskRunLineageSummary.
        The status of the task run.

        Allowed values for this property are: "SUCCESS", "ERROR", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_execution_status of this TaskRunLineageSummary.
        :rtype: str
        """
        return self._task_execution_status

    @task_execution_status.setter
    def task_execution_status(self, task_execution_status):
        """
        Sets the task_execution_status of this TaskRunLineageSummary.
        The status of the task run.


        :param task_execution_status: The task_execution_status of this TaskRunLineageSummary.
        :type: str
        """
        allowed_values = ["SUCCESS", "ERROR", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(task_execution_status, allowed_values):
            task_execution_status = 'UNKNOWN_ENUM_VALUE'
        self._task_execution_status = task_execution_status

    @property
    def flow(self):
        """
        Gets the flow of this TaskRunLineageSummary.

        :return: The flow of this TaskRunLineageSummary.
        :rtype: oci.data_integration.models.DataFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """
        Sets the flow of this TaskRunLineageSummary.

        :param flow: The flow of this TaskRunLineageSummary.
        :type: oci.data_integration.models.DataFlow
        """
        self._flow = flow

    @property
    def metadata(self):
        """
        Gets the metadata of this TaskRunLineageSummary.

        :return: The metadata of this TaskRunLineageSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TaskRunLineageSummary.

        :param metadata: The metadata of this TaskRunLineageSummary.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
