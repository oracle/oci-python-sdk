# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningTaskSqlExecutionPlanStep(object):
    """
    A step in the SQL execution plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningTaskSqlExecutionPlanStep object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_hash_value:
            The value to assign to the plan_hash_value property of this SqlTuningTaskSqlExecutionPlanStep.
        :type plan_hash_value: int

        :param step_id:
            The value to assign to the step_id property of this SqlTuningTaskSqlExecutionPlanStep.
        :type step_id: int

        :param parent_step_id:
            The value to assign to the parent_step_id property of this SqlTuningTaskSqlExecutionPlanStep.
        :type parent_step_id: int

        :param position:
            The value to assign to the position property of this SqlTuningTaskSqlExecutionPlanStep.
        :type position: int

        :param operation:
            The value to assign to the operation property of this SqlTuningTaskSqlExecutionPlanStep.
        :type operation: str

        :param options:
            The value to assign to the options property of this SqlTuningTaskSqlExecutionPlanStep.
        :type options: str

        :param optimizer_mode:
            The value to assign to the optimizer_mode property of this SqlTuningTaskSqlExecutionPlanStep.
        :type optimizer_mode: str

        :param cost:
            The value to assign to the cost property of this SqlTuningTaskSqlExecutionPlanStep.
        :type cost: float

        :param cardinality:
            The value to assign to the cardinality property of this SqlTuningTaskSqlExecutionPlanStep.
        :type cardinality: int

        :param bytes:
            The value to assign to the bytes property of this SqlTuningTaskSqlExecutionPlanStep.
        :type bytes: int

        :param cpu_cost:
            The value to assign to the cpu_cost property of this SqlTuningTaskSqlExecutionPlanStep.
        :type cpu_cost: float

        :param io_cost:
            The value to assign to the io_cost property of this SqlTuningTaskSqlExecutionPlanStep.
        :type io_cost: float

        :param temp_space:
            The value to assign to the temp_space property of this SqlTuningTaskSqlExecutionPlanStep.
        :type temp_space: int

        :param time:
            The value to assign to the time property of this SqlTuningTaskSqlExecutionPlanStep.
        :type time: int

        :param object_node:
            The value to assign to the object_node property of this SqlTuningTaskSqlExecutionPlanStep.
        :type object_node: str

        :param object_owner:
            The value to assign to the object_owner property of this SqlTuningTaskSqlExecutionPlanStep.
        :type object_owner: str

        :param object_name:
            The value to assign to the object_name property of this SqlTuningTaskSqlExecutionPlanStep.
        :type object_name: str

        :param object_position:
            The value to assign to the object_position property of this SqlTuningTaskSqlExecutionPlanStep.
        :type object_position: int

        :param object_type:
            The value to assign to the object_type property of this SqlTuningTaskSqlExecutionPlanStep.
        :type object_type: str

        :param partition_start:
            The value to assign to the partition_start property of this SqlTuningTaskSqlExecutionPlanStep.
        :type partition_start: str

        :param partition_stop:
            The value to assign to the partition_stop property of this SqlTuningTaskSqlExecutionPlanStep.
        :type partition_stop: str

        :param partition_id:
            The value to assign to the partition_id property of this SqlTuningTaskSqlExecutionPlanStep.
        :type partition_id: int

        :param remarks:
            The value to assign to the remarks property of this SqlTuningTaskSqlExecutionPlanStep.
        :type remarks: str

        :param number_of_search_column:
            The value to assign to the number_of_search_column property of this SqlTuningTaskSqlExecutionPlanStep.
        :type number_of_search_column: int

        :param other:
            The value to assign to the other property of this SqlTuningTaskSqlExecutionPlanStep.
        :type other: str

        :param other_tag:
            The value to assign to the other_tag property of this SqlTuningTaskSqlExecutionPlanStep.
        :type other_tag: str

        :param attribute:
            The value to assign to the attribute property of this SqlTuningTaskSqlExecutionPlanStep.
        :type attribute: str

        :param access_predicates:
            The value to assign to the access_predicates property of this SqlTuningTaskSqlExecutionPlanStep.
        :type access_predicates: str

        :param filter_predicates:
            The value to assign to the filter_predicates property of this SqlTuningTaskSqlExecutionPlanStep.
        :type filter_predicates: str

        """
        self.swagger_types = {
            'plan_hash_value': 'int',
            'step_id': 'int',
            'parent_step_id': 'int',
            'position': 'int',
            'operation': 'str',
            'options': 'str',
            'optimizer_mode': 'str',
            'cost': 'float',
            'cardinality': 'int',
            'bytes': 'int',
            'cpu_cost': 'float',
            'io_cost': 'float',
            'temp_space': 'int',
            'time': 'int',
            'object_node': 'str',
            'object_owner': 'str',
            'object_name': 'str',
            'object_position': 'int',
            'object_type': 'str',
            'partition_start': 'str',
            'partition_stop': 'str',
            'partition_id': 'int',
            'remarks': 'str',
            'number_of_search_column': 'int',
            'other': 'str',
            'other_tag': 'str',
            'attribute': 'str',
            'access_predicates': 'str',
            'filter_predicates': 'str'
        }

        self.attribute_map = {
            'plan_hash_value': 'planHashValue',
            'step_id': 'stepId',
            'parent_step_id': 'parentStepId',
            'position': 'position',
            'operation': 'operation',
            'options': 'options',
            'optimizer_mode': 'optimizerMode',
            'cost': 'cost',
            'cardinality': 'cardinality',
            'bytes': 'bytes',
            'cpu_cost': 'cpuCost',
            'io_cost': 'ioCost',
            'temp_space': 'tempSpace',
            'time': 'time',
            'object_node': 'objectNode',
            'object_owner': 'objectOwner',
            'object_name': 'objectName',
            'object_position': 'objectPosition',
            'object_type': 'objectType',
            'partition_start': 'partitionStart',
            'partition_stop': 'partitionStop',
            'partition_id': 'partitionId',
            'remarks': 'remarks',
            'number_of_search_column': 'numberOfSearchColumn',
            'other': 'other',
            'other_tag': 'otherTag',
            'attribute': 'attribute',
            'access_predicates': 'accessPredicates',
            'filter_predicates': 'filterPredicates'
        }

        self._plan_hash_value = None
        self._step_id = None
        self._parent_step_id = None
        self._position = None
        self._operation = None
        self._options = None
        self._optimizer_mode = None
        self._cost = None
        self._cardinality = None
        self._bytes = None
        self._cpu_cost = None
        self._io_cost = None
        self._temp_space = None
        self._time = None
        self._object_node = None
        self._object_owner = None
        self._object_name = None
        self._object_position = None
        self._object_type = None
        self._partition_start = None
        self._partition_stop = None
        self._partition_id = None
        self._remarks = None
        self._number_of_search_column = None
        self._other = None
        self._other_tag = None
        self._attribute = None
        self._access_predicates = None
        self._filter_predicates = None

    @property
    def plan_hash_value(self):
        """
        Gets the plan_hash_value of this SqlTuningTaskSqlExecutionPlanStep.
        The numerical representation of the SQL execution plan.


        :return: The plan_hash_value of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._plan_hash_value

    @plan_hash_value.setter
    def plan_hash_value(self, plan_hash_value):
        """
        Sets the plan_hash_value of this SqlTuningTaskSqlExecutionPlanStep.
        The numerical representation of the SQL execution plan.


        :param plan_hash_value: The plan_hash_value of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._plan_hash_value = plan_hash_value

    @property
    def step_id(self):
        """
        Gets the step_id of this SqlTuningTaskSqlExecutionPlanStep.
        The identification number of a step in the SQL execution plan. This is unique within the SQL execution plan.
        This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The step_id of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """
        Sets the step_id of this SqlTuningTaskSqlExecutionPlanStep.
        The identification number of a step in the SQL execution plan. This is unique within the SQL execution plan.
        This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param step_id: The step_id of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._step_id = step_id

    @property
    def parent_step_id(self):
        """
        Gets the parent_step_id of this SqlTuningTaskSqlExecutionPlanStep.
        The ID of the next step that operates on the results of this step.
        This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The parent_step_id of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._parent_step_id

    @parent_step_id.setter
    def parent_step_id(self, parent_step_id):
        """
        Sets the parent_step_id of this SqlTuningTaskSqlExecutionPlanStep.
        The ID of the next step that operates on the results of this step.
        This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param parent_step_id: The parent_step_id of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._parent_step_id = parent_step_id

    @property
    def position(self):
        """
        Gets the position of this SqlTuningTaskSqlExecutionPlanStep.
        The order of processing for steps with the same parent ID.


        :return: The position of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this SqlTuningTaskSqlExecutionPlanStep.
        The order of processing for steps with the same parent ID.


        :param position: The position of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._position = position

    @property
    def operation(self):
        """
        Gets the operation of this SqlTuningTaskSqlExecutionPlanStep.
        The name of the operation performed at this step.


        :return: The operation of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this SqlTuningTaskSqlExecutionPlanStep.
        The name of the operation performed at this step.


        :param operation: The operation of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._operation = operation

    @property
    def options(self):
        """
        Gets the options of this SqlTuningTaskSqlExecutionPlanStep.
        The options used for the operation performed at this step.


        :return: The options of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this SqlTuningTaskSqlExecutionPlanStep.
        The options used for the operation performed at this step.


        :param options: The options of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._options = options

    @property
    def optimizer_mode(self):
        """
        Gets the optimizer_mode of this SqlTuningTaskSqlExecutionPlanStep.
        The current mode of the optimizer, such as all_rows, first_rows_n (where n = 1, 10, 100, 1000, and so on).


        :return: The optimizer_mode of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._optimizer_mode

    @optimizer_mode.setter
    def optimizer_mode(self, optimizer_mode):
        """
        Sets the optimizer_mode of this SqlTuningTaskSqlExecutionPlanStep.
        The current mode of the optimizer, such as all_rows, first_rows_n (where n = 1, 10, 100, 1000, and so on).


        :param optimizer_mode: The optimizer_mode of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._optimizer_mode = optimizer_mode

    @property
    def cost(self):
        """
        Gets the cost of this SqlTuningTaskSqlExecutionPlanStep.
        The cost of the current operation estimated by the cost-based optimizer (CBO).


        :return: The cost of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this SqlTuningTaskSqlExecutionPlanStep.
        The cost of the current operation estimated by the cost-based optimizer (CBO).


        :param cost: The cost of this SqlTuningTaskSqlExecutionPlanStep.
        :type: float
        """
        self._cost = cost

    @property
    def cardinality(self):
        """
        Gets the cardinality of this SqlTuningTaskSqlExecutionPlanStep.
        The number of rows returned by the current operation (estimated by the CBO).


        :return: The cardinality of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """
        Sets the cardinality of this SqlTuningTaskSqlExecutionPlanStep.
        The number of rows returned by the current operation (estimated by the CBO).


        :param cardinality: The cardinality of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._cardinality = cardinality

    @property
    def bytes(self):
        """
        Gets the bytes of this SqlTuningTaskSqlExecutionPlanStep.
        The number of bytes returned by the current operation.


        :return: The bytes of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """
        Sets the bytes of this SqlTuningTaskSqlExecutionPlanStep.
        The number of bytes returned by the current operation.


        :param bytes: The bytes of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._bytes = bytes

    @property
    def cpu_cost(self):
        """
        Gets the cpu_cost of this SqlTuningTaskSqlExecutionPlanStep.
        The CPU cost of the current operation.


        :return: The cpu_cost of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: float
        """
        return self._cpu_cost

    @cpu_cost.setter
    def cpu_cost(self, cpu_cost):
        """
        Sets the cpu_cost of this SqlTuningTaskSqlExecutionPlanStep.
        The CPU cost of the current operation.


        :param cpu_cost: The cpu_cost of this SqlTuningTaskSqlExecutionPlanStep.
        :type: float
        """
        self._cpu_cost = cpu_cost

    @property
    def io_cost(self):
        """
        Gets the io_cost of this SqlTuningTaskSqlExecutionPlanStep.
        The I/O cost of the current operation.


        :return: The io_cost of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: float
        """
        return self._io_cost

    @io_cost.setter
    def io_cost(self, io_cost):
        """
        Sets the io_cost of this SqlTuningTaskSqlExecutionPlanStep.
        The I/O cost of the current operation.


        :param io_cost: The io_cost of this SqlTuningTaskSqlExecutionPlanStep.
        :type: float
        """
        self._io_cost = io_cost

    @property
    def temp_space(self):
        """
        Gets the temp_space of this SqlTuningTaskSqlExecutionPlanStep.
        The temporary space usage (in bytes) of the operation (sort or hash-join) as estimated by the CBO.


        :return: The temp_space of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._temp_space

    @temp_space.setter
    def temp_space(self, temp_space):
        """
        Sets the temp_space of this SqlTuningTaskSqlExecutionPlanStep.
        The temporary space usage (in bytes) of the operation (sort or hash-join) as estimated by the CBO.


        :param temp_space: The temp_space of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._temp_space = temp_space

    @property
    def time(self):
        """
        Gets the time of this SqlTuningTaskSqlExecutionPlanStep.
        The elapsed time (in seconds) of the operation as estimated by the CBO.


        :return: The time of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this SqlTuningTaskSqlExecutionPlanStep.
        The elapsed time (in seconds) of the operation as estimated by the CBO.


        :param time: The time of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._time = time

    @property
    def object_node(self):
        """
        Gets the object_node of this SqlTuningTaskSqlExecutionPlanStep.
        The name of the database link used to reference the object.


        :return: The object_node of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._object_node

    @object_node.setter
    def object_node(self, object_node):
        """
        Sets the object_node of this SqlTuningTaskSqlExecutionPlanStep.
        The name of the database link used to reference the object.


        :param object_node: The object_node of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._object_node = object_node

    @property
    def object_owner(self):
        """
        Gets the object_owner of this SqlTuningTaskSqlExecutionPlanStep.
        The owner of the object.


        :return: The object_owner of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._object_owner

    @object_owner.setter
    def object_owner(self, object_owner):
        """
        Sets the object_owner of this SqlTuningTaskSqlExecutionPlanStep.
        The owner of the object.


        :param object_owner: The object_owner of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._object_owner = object_owner

    @property
    def object_name(self):
        """
        Gets the object_name of this SqlTuningTaskSqlExecutionPlanStep.
        The name of the object.


        :return: The object_name of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this SqlTuningTaskSqlExecutionPlanStep.
        The name of the object.


        :param object_name: The object_name of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._object_name = object_name

    @property
    def object_position(self):
        """
        Gets the object_position of this SqlTuningTaskSqlExecutionPlanStep.
        The numbered position of the object name in the original SQL statement.


        :return: The object_position of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._object_position

    @object_position.setter
    def object_position(self, object_position):
        """
        Sets the object_position of this SqlTuningTaskSqlExecutionPlanStep.
        The numbered position of the object name in the original SQL statement.


        :param object_position: The object_position of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._object_position = object_position

    @property
    def object_type(self):
        """
        Gets the object_type of this SqlTuningTaskSqlExecutionPlanStep.
        The descriptive modifier that further describes the type of object.


        :return: The object_type of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SqlTuningTaskSqlExecutionPlanStep.
        The descriptive modifier that further describes the type of object.


        :param object_type: The object_type of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._object_type = object_type

    @property
    def partition_start(self):
        """
        Gets the partition_start of this SqlTuningTaskSqlExecutionPlanStep.
        A step may get data from a range of partitions of a partitioned object, such as table or index,
        based on predicates and sorting order. The partionStart is the starting partition of the range.
        The partitionStop is the ending partition of the range.


        :return: The partition_start of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._partition_start

    @partition_start.setter
    def partition_start(self, partition_start):
        """
        Sets the partition_start of this SqlTuningTaskSqlExecutionPlanStep.
        A step may get data from a range of partitions of a partitioned object, such as table or index,
        based on predicates and sorting order. The partionStart is the starting partition of the range.
        The partitionStop is the ending partition of the range.


        :param partition_start: The partition_start of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._partition_start = partition_start

    @property
    def partition_stop(self):
        """
        Gets the partition_stop of this SqlTuningTaskSqlExecutionPlanStep.
        A step may get data from a range of partitions of a partitioned object, such as table or index,
        based on predicates and sorting order. The partionStart is the starting partition of the range.
        The partitionStop is the ending partition of the range.


        :return: The partition_stop of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._partition_stop

    @partition_stop.setter
    def partition_stop(self, partition_stop):
        """
        Sets the partition_stop of this SqlTuningTaskSqlExecutionPlanStep.
        A step may get data from a range of partitions of a partitioned object, such as table or index,
        based on predicates and sorting order. The partionStart is the starting partition of the range.
        The partitionStop is the ending partition of the range.


        :param partition_stop: The partition_stop of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._partition_stop = partition_stop

    @property
    def partition_id(self):
        """
        Gets the partition_id of this SqlTuningTaskSqlExecutionPlanStep.
        The ID of the step in the execution plan that has computed the pair of values of partitionStart and partitionStop.


        :return: The partition_id of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """
        Sets the partition_id of this SqlTuningTaskSqlExecutionPlanStep.
        The ID of the step in the execution plan that has computed the pair of values of partitionStart and partitionStop.


        :param partition_id: The partition_id of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._partition_id = partition_id

    @property
    def remarks(self):
        """
        Gets the remarks of this SqlTuningTaskSqlExecutionPlanStep.
        The place for comments that can be added to the steps of the execution plan.


        :return: The remarks of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """
        Sets the remarks of this SqlTuningTaskSqlExecutionPlanStep.
        The place for comments that can be added to the steps of the execution plan.


        :param remarks: The remarks of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._remarks = remarks

    @property
    def number_of_search_column(self):
        """
        Gets the number_of_search_column of this SqlTuningTaskSqlExecutionPlanStep.
        Number of index columns with start and stop keys (that is, the number of columns with matching predicates).


        :return: The number_of_search_column of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: int
        """
        return self._number_of_search_column

    @number_of_search_column.setter
    def number_of_search_column(self, number_of_search_column):
        """
        Sets the number_of_search_column of this SqlTuningTaskSqlExecutionPlanStep.
        Number of index columns with start and stop keys (that is, the number of columns with matching predicates).


        :param number_of_search_column: The number_of_search_column of this SqlTuningTaskSqlExecutionPlanStep.
        :type: int
        """
        self._number_of_search_column = number_of_search_column

    @property
    def other(self):
        """
        Gets the other of this SqlTuningTaskSqlExecutionPlanStep.
        Information about parallel execution servers and parallel queries


        :return: The other of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """
        Sets the other of this SqlTuningTaskSqlExecutionPlanStep.
        Information about parallel execution servers and parallel queries


        :param other: The other of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._other = other

    @property
    def other_tag(self):
        """
        Gets the other_tag of this SqlTuningTaskSqlExecutionPlanStep.
        Describes the function of the SQL text in the OTHER column.


        :return: The other_tag of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._other_tag

    @other_tag.setter
    def other_tag(self, other_tag):
        """
        Sets the other_tag of this SqlTuningTaskSqlExecutionPlanStep.
        Describes the function of the SQL text in the OTHER column.


        :param other_tag: The other_tag of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._other_tag = other_tag

    @property
    def attribute(self):
        """
        Gets the attribute of this SqlTuningTaskSqlExecutionPlanStep.
        The text string identifying the type of execution plan.


        :return: The attribute of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """
        Sets the attribute of this SqlTuningTaskSqlExecutionPlanStep.
        The text string identifying the type of execution plan.


        :param attribute: The attribute of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._attribute = attribute

    @property
    def access_predicates(self):
        """
        Gets the access_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        The predicates used to locate rows in an access structure. For example,
        start or stop predicates for an index range scan.


        :return: The access_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._access_predicates

    @access_predicates.setter
    def access_predicates(self, access_predicates):
        """
        Sets the access_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        The predicates used to locate rows in an access structure. For example,
        start or stop predicates for an index range scan.


        :param access_predicates: The access_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._access_predicates = access_predicates

    @property
    def filter_predicates(self):
        """
        Gets the filter_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        The predicates used to filter rows before producing them.


        :return: The filter_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        :rtype: str
        """
        return self._filter_predicates

    @filter_predicates.setter
    def filter_predicates(self, filter_predicates):
        """
        Sets the filter_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        The predicates used to filter rows before producing them.


        :param filter_predicates: The filter_predicates of this SqlTuningTaskSqlExecutionPlanStep.
        :type: str
        """
        self._filter_predicates = filter_predicates

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
