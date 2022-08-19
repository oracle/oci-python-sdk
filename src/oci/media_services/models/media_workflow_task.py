# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaWorkflowTask(object):
    """
    Defines the type of processing to be run at a given point in the workflow, parameters to configure the
    processing, and any processing that must be completed before this processing begins.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MediaWorkflowTask object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this MediaWorkflowTask.
        :type type: str

        :param version:
            The value to assign to the version property of this MediaWorkflowTask.
        :type version: int

        :param key:
            The value to assign to the key property of this MediaWorkflowTask.
        :type key: str

        :param prerequisites:
            The value to assign to the prerequisites property of this MediaWorkflowTask.
        :type prerequisites: list[str]

        :param enable_parameter_reference:
            The value to assign to the enable_parameter_reference property of this MediaWorkflowTask.
        :type enable_parameter_reference: str

        :param enable_when_referenced_parameter_equals:
            The value to assign to the enable_when_referenced_parameter_equals property of this MediaWorkflowTask.
        :type enable_when_referenced_parameter_equals: dict(str, object)

        :param parameters:
            The value to assign to the parameters property of this MediaWorkflowTask.
        :type parameters: dict(str, object)

        """
        self.swagger_types = {
            'type': 'str',
            'version': 'int',
            'key': 'str',
            'prerequisites': 'list[str]',
            'enable_parameter_reference': 'str',
            'enable_when_referenced_parameter_equals': 'dict(str, object)',
            'parameters': 'dict(str, object)'
        }

        self.attribute_map = {
            'type': 'type',
            'version': 'version',
            'key': 'key',
            'prerequisites': 'prerequisites',
            'enable_parameter_reference': 'enableParameterReference',
            'enable_when_referenced_parameter_equals': 'enableWhenReferencedParameterEquals',
            'parameters': 'parameters'
        }

        self._type = None
        self._version = None
        self._key = None
        self._prerequisites = None
        self._enable_parameter_reference = None
        self._enable_when_referenced_parameter_equals = None
        self._parameters = None

    @property
    def type(self):
        """
        Gets the type of this MediaWorkflowTask.
        The type of process to run at this task. Refers to the name of a MediaWorkflowTaskDeclaration.


        :return: The type of this MediaWorkflowTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MediaWorkflowTask.
        The type of process to run at this task. Refers to the name of a MediaWorkflowTaskDeclaration.


        :param type: The type of this MediaWorkflowTask.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this MediaWorkflowTask.
        The version of the MediaWorkflowTaskDeclaration.


        :return: The version of this MediaWorkflowTask.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this MediaWorkflowTask.
        The version of the MediaWorkflowTaskDeclaration.


        :param version: The version of this MediaWorkflowTask.
        :type: int
        """
        self._version = version

    @property
    def key(self):
        """
        **[Required]** Gets the key of this MediaWorkflowTask.
        A unique identifier for this task within its workflow. Keys are used to reference a task within workflows
        and MediaWorkflowJobs. Tasks are referenced as prerequisites and to track output and state.


        :return: The key of this MediaWorkflowTask.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this MediaWorkflowTask.
        A unique identifier for this task within its workflow. Keys are used to reference a task within workflows
        and MediaWorkflowJobs. Tasks are referenced as prerequisites and to track output and state.


        :param key: The key of this MediaWorkflowTask.
        :type: str
        """
        self._key = key

    @property
    def prerequisites(self):
        """
        Gets the prerequisites of this MediaWorkflowTask.
        Keys to the other tasks in this workflow that must be completed before execution of this task can begin.


        :return: The prerequisites of this MediaWorkflowTask.
        :rtype: list[str]
        """
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, prerequisites):
        """
        Sets the prerequisites of this MediaWorkflowTask.
        Keys to the other tasks in this workflow that must be completed before execution of this task can begin.


        :param prerequisites: The prerequisites of this MediaWorkflowTask.
        :type: list[str]
        """
        self._prerequisites = prerequisites

    @property
    def enable_parameter_reference(self):
        """
        Gets the enable_parameter_reference of this MediaWorkflowTask.
        Allows this task to be conditionally enabled.  If no value or a blank value is given, the task is
        unconditionally enbled.  Otherwise the given string specifies a parameter of the job created for this task's
        workflow using the JSON pointer syntax. The JSON pointer is validated when a job is created from the workflow of this task.


        :return: The enable_parameter_reference of this MediaWorkflowTask.
        :rtype: str
        """
        return self._enable_parameter_reference

    @enable_parameter_reference.setter
    def enable_parameter_reference(self, enable_parameter_reference):
        """
        Sets the enable_parameter_reference of this MediaWorkflowTask.
        Allows this task to be conditionally enabled.  If no value or a blank value is given, the task is
        unconditionally enbled.  Otherwise the given string specifies a parameter of the job created for this task's
        workflow using the JSON pointer syntax. The JSON pointer is validated when a job is created from the workflow of this task.


        :param enable_parameter_reference: The enable_parameter_reference of this MediaWorkflowTask.
        :type: str
        """
        self._enable_parameter_reference = enable_parameter_reference

    @property
    def enable_when_referenced_parameter_equals(self):
        """
        Gets the enable_when_referenced_parameter_equals of this MediaWorkflowTask.
        Used in conjunction with enableParameterReference to conditionally enable a task.  When a job is created
        from the workflow of this task, the task will only be enabled if the value of the parameter specified by
        enableParameterReference is equal to the value of this property. This property must be prenset if and only if
        a enableParameterReference is given. The value is a JSON node.


        :return: The enable_when_referenced_parameter_equals of this MediaWorkflowTask.
        :rtype: dict(str, object)
        """
        return self._enable_when_referenced_parameter_equals

    @enable_when_referenced_parameter_equals.setter
    def enable_when_referenced_parameter_equals(self, enable_when_referenced_parameter_equals):
        """
        Sets the enable_when_referenced_parameter_equals of this MediaWorkflowTask.
        Used in conjunction with enableParameterReference to conditionally enable a task.  When a job is created
        from the workflow of this task, the task will only be enabled if the value of the parameter specified by
        enableParameterReference is equal to the value of this property. This property must be prenset if and only if
        a enableParameterReference is given. The value is a JSON node.


        :param enable_when_referenced_parameter_equals: The enable_when_referenced_parameter_equals of this MediaWorkflowTask.
        :type: dict(str, object)
        """
        self._enable_when_referenced_parameter_equals = enable_when_referenced_parameter_equals

    @property
    def parameters(self):
        """
        Gets the parameters of this MediaWorkflowTask.
        Data specifiying how this task is to be run. The data is a JSON object that must conform to the JSON Schema
        specified by the parameters of the MediaWorkflowTaskDeclaration this task references. The parameters may
        contain values or references to other parameters.


        :return: The parameters of this MediaWorkflowTask.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this MediaWorkflowTask.
        Data specifiying how this task is to be run. The data is a JSON object that must conform to the JSON Schema
        specified by the parameters of the MediaWorkflowTaskDeclaration this task references. The parameters may
        contain values or references to other parameters.


        :param parameters: The parameters of this MediaWorkflowTask.
        :type: dict(str, object)
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
