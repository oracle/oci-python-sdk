# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverWorkload(object):
    """
    Information about a RoverWorkload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverWorkload object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RoverWorkload.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RoverWorkload.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this RoverWorkload.
        :type id: str

        :param size:
            The value to assign to the size property of this RoverWorkload.
        :type size: str

        :param object_count:
            The value to assign to the object_count property of this RoverWorkload.
        :type object_count: str

        :param prefix:
            The value to assign to the prefix property of this RoverWorkload.
        :type prefix: str

        :param range_start:
            The value to assign to the range_start property of this RoverWorkload.
        :type range_start: str

        :param range_end:
            The value to assign to the range_end property of this RoverWorkload.
        :type range_end: str

        :param workload_type:
            The value to assign to the workload_type property of this RoverWorkload.
        :type workload_type: str

        :param work_request_id:
            The value to assign to the work_request_id property of this RoverWorkload.
        :type work_request_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'size': 'str',
            'object_count': 'str',
            'prefix': 'str',
            'range_start': 'str',
            'range_end': 'str',
            'workload_type': 'str',
            'work_request_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'size': 'size',
            'object_count': 'objectCount',
            'prefix': 'prefix',
            'range_start': 'rangeStart',
            'range_end': 'rangeEnd',
            'workload_type': 'workloadType',
            'work_request_id': 'workRequestId'
        }

        self._name = None
        self._compartment_id = None
        self._id = None
        self._size = None
        self._object_count = None
        self._prefix = None
        self._range_start = None
        self._range_end = None
        self._workload_type = None
        self._work_request_id = None

    @property
    def name(self):
        """
        Gets the name of this RoverWorkload.
        Name of the Rover Workload


        :return: The name of this RoverWorkload.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RoverWorkload.
        Name of the Rover Workload


        :param name: The name of this RoverWorkload.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RoverWorkload.
        The OCID of the compartment containing the workload.


        :return: The compartment_id of this RoverWorkload.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RoverWorkload.
        The OCID of the compartment containing the workload.


        :param compartment_id: The compartment_id of this RoverWorkload.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RoverWorkload.
        The Unique Oracle ID (OCID) that is immutable on creation.


        :return: The id of this RoverWorkload.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RoverWorkload.
        The Unique Oracle ID (OCID) that is immutable on creation.


        :param id: The id of this RoverWorkload.
        :type: str
        """
        self._id = id

    @property
    def size(self):
        """
        Gets the size of this RoverWorkload.
        Size of the workload.


        :return: The size of this RoverWorkload.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this RoverWorkload.
        Size of the workload.


        :param size: The size of this RoverWorkload.
        :type: str
        """
        self._size = size

    @property
    def object_count(self):
        """
        Gets the object_count of this RoverWorkload.
        Number of objects in a workload.


        :return: The object_count of this RoverWorkload.
        :rtype: str
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """
        Sets the object_count of this RoverWorkload.
        Number of objects in a workload.


        :param object_count: The object_count of this RoverWorkload.
        :type: str
        """
        self._object_count = object_count

    @property
    def prefix(self):
        """
        Gets the prefix of this RoverWorkload.
        Prefix to filter objects in case it is a bucket.


        :return: The prefix of this RoverWorkload.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this RoverWorkload.
        Prefix to filter objects in case it is a bucket.


        :param prefix: The prefix of this RoverWorkload.
        :type: str
        """
        self._prefix = prefix

    @property
    def range_start(self):
        """
        Gets the range_start of this RoverWorkload.
        Start of the range in a bucket.


        :return: The range_start of this RoverWorkload.
        :rtype: str
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """
        Sets the range_start of this RoverWorkload.
        Start of the range in a bucket.


        :param range_start: The range_start of this RoverWorkload.
        :type: str
        """
        self._range_start = range_start

    @property
    def range_end(self):
        """
        Gets the range_end of this RoverWorkload.
        End of the range in a bucket.


        :return: The range_end of this RoverWorkload.
        :rtype: str
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """
        Sets the range_end of this RoverWorkload.
        End of the range in a bucket.


        :param range_end: The range_end of this RoverWorkload.
        :type: str
        """
        self._range_end = range_end

    @property
    def workload_type(self):
        """
        **[Required]** Gets the workload_type of this RoverWorkload.
        The type of workload


        :return: The workload_type of this RoverWorkload.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """
        Sets the workload_type of this RoverWorkload.
        The type of workload


        :param workload_type: The workload_type of this RoverWorkload.
        :type: str
        """
        self._workload_type = workload_type

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this RoverWorkload.
        The compute work request id to track progress of custom image exports.


        :return: The work_request_id of this RoverWorkload.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this RoverWorkload.
        The compute work request id to track progress of custom image exports.


        :param work_request_id: The work_request_id of this RoverWorkload.
        :type: str
        """
        self._work_request_id = work_request_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
