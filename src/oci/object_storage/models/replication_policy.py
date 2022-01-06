# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicationPolicy(object):
    """
    The details of a replication policy.
    """

    #: A constant which can be used with the status property of a ReplicationPolicy.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a ReplicationPolicy.
    #: This constant has a value of "CLIENT_ERROR"
    STATUS_CLIENT_ERROR = "CLIENT_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicationPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ReplicationPolicy.
        :type id: str

        :param name:
            The value to assign to the name property of this ReplicationPolicy.
        :type name: str

        :param destination_region_name:
            The value to assign to the destination_region_name property of this ReplicationPolicy.
        :type destination_region_name: str

        :param destination_bucket_name:
            The value to assign to the destination_bucket_name property of this ReplicationPolicy.
        :type destination_bucket_name: str

        :param time_created:
            The value to assign to the time_created property of this ReplicationPolicy.
        :type time_created: datetime

        :param time_last_sync:
            The value to assign to the time_last_sync property of this ReplicationPolicy.
        :type time_last_sync: datetime

        :param status:
            The value to assign to the status property of this ReplicationPolicy.
            Allowed values for this property are: "ACTIVE", "CLIENT_ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_message:
            The value to assign to the status_message property of this ReplicationPolicy.
        :type status_message: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'destination_region_name': 'str',
            'destination_bucket_name': 'str',
            'time_created': 'datetime',
            'time_last_sync': 'datetime',
            'status': 'str',
            'status_message': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'destination_region_name': 'destinationRegionName',
            'destination_bucket_name': 'destinationBucketName',
            'time_created': 'timeCreated',
            'time_last_sync': 'timeLastSync',
            'status': 'status',
            'status_message': 'statusMessage'
        }

        self._id = None
        self._name = None
        self._destination_region_name = None
        self._destination_bucket_name = None
        self._time_created = None
        self._time_last_sync = None
        self._status = None
        self._status_message = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ReplicationPolicy.
        The id of the replication policy.


        :return: The id of this ReplicationPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReplicationPolicy.
        The id of the replication policy.


        :param id: The id of this ReplicationPolicy.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ReplicationPolicy.
        The name of the policy.


        :return: The name of this ReplicationPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReplicationPolicy.
        The name of the policy.


        :param name: The name of this ReplicationPolicy.
        :type: str
        """
        self._name = name

    @property
    def destination_region_name(self):
        """
        **[Required]** Gets the destination_region_name of this ReplicationPolicy.
        The destination region to replicate to, for example \"us-ashburn-1\".


        :return: The destination_region_name of this ReplicationPolicy.
        :rtype: str
        """
        return self._destination_region_name

    @destination_region_name.setter
    def destination_region_name(self, destination_region_name):
        """
        Sets the destination_region_name of this ReplicationPolicy.
        The destination region to replicate to, for example \"us-ashburn-1\".


        :param destination_region_name: The destination_region_name of this ReplicationPolicy.
        :type: str
        """
        self._destination_region_name = destination_region_name

    @property
    def destination_bucket_name(self):
        """
        **[Required]** Gets the destination_bucket_name of this ReplicationPolicy.
        The bucket to replicate to in the destination region. Replication policy creation does not automatically
        create a destination bucket. Create the destination bucket before creating the policy.


        :return: The destination_bucket_name of this ReplicationPolicy.
        :rtype: str
        """
        return self._destination_bucket_name

    @destination_bucket_name.setter
    def destination_bucket_name(self, destination_bucket_name):
        """
        Sets the destination_bucket_name of this ReplicationPolicy.
        The bucket to replicate to in the destination region. Replication policy creation does not automatically
        create a destination bucket. Create the destination bucket before creating the policy.


        :param destination_bucket_name: The destination_bucket_name of this ReplicationPolicy.
        :type: str
        """
        self._destination_bucket_name = destination_bucket_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ReplicationPolicy.
        The date when the replication policy was created as per `RFC 3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ReplicationPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ReplicationPolicy.
        The date when the replication policy was created as per `RFC 3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ReplicationPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_sync(self):
        """
        **[Required]** Gets the time_last_sync of this ReplicationPolicy.
        Changes made to the source bucket before this time has been replicated.


        :return: The time_last_sync of this ReplicationPolicy.
        :rtype: datetime
        """
        return self._time_last_sync

    @time_last_sync.setter
    def time_last_sync(self, time_last_sync):
        """
        Sets the time_last_sync of this ReplicationPolicy.
        Changes made to the source bucket before this time has been replicated.


        :param time_last_sync: The time_last_sync of this ReplicationPolicy.
        :type: datetime
        """
        self._time_last_sync = time_last_sync

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ReplicationPolicy.
        The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue
        described in the status message, the status will become ACTIVE.

        Allowed values for this property are: "ACTIVE", "CLIENT_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ReplicationPolicy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ReplicationPolicy.
        The replication status of the policy. If the status is CLIENT_ERROR, once the user fixes the issue
        described in the status message, the status will become ACTIVE.


        :param status: The status of this ReplicationPolicy.
        :type: str
        """
        allowed_values = ["ACTIVE", "CLIENT_ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_message(self):
        """
        **[Required]** Gets the status_message of this ReplicationPolicy.
        A human-readable description of the status.


        :return: The status_message of this ReplicationPolicy.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ReplicationPolicy.
        A human-readable description of the status.


        :param status_message: The status_message of this ReplicationPolicy.
        :type: str
        """
        self._status_message = status_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
