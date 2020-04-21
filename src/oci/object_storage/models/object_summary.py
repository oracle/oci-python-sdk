# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectSummary(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ObjectSummary.
        :type name: str

        :param size:
            The value to assign to the size property of this ObjectSummary.
        :type size: int

        :param md5:
            The value to assign to the md5 property of this ObjectSummary.
        :type md5: str

        :param time_created:
            The value to assign to the time_created property of this ObjectSummary.
        :type time_created: datetime

        :param etag:
            The value to assign to the etag property of this ObjectSummary.
        :type etag: str

        :param time_modified:
            The value to assign to the time_modified property of this ObjectSummary.
        :type time_modified: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'size': 'int',
            'md5': 'str',
            'time_created': 'datetime',
            'etag': 'str',
            'time_modified': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'size': 'size',
            'md5': 'md5',
            'time_created': 'timeCreated',
            'etag': 'etag',
            'time_modified': 'timeModified'
        }

        self._name = None
        self._size = None
        self._md5 = None
        self._time_created = None
        self._etag = None
        self._time_modified = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ObjectSummary.
        The name of the object. Avoid entering confidential information.
        Example: test/object1.log


        :return: The name of this ObjectSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectSummary.
        The name of the object. Avoid entering confidential information.
        Example: test/object1.log


        :param name: The name of this ObjectSummary.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """
        Gets the size of this ObjectSummary.
        Size of the object in bytes.


        :return: The size of this ObjectSummary.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ObjectSummary.
        Size of the object in bytes.


        :param size: The size of this ObjectSummary.
        :type: int
        """
        self._size = size

    @property
    def md5(self):
        """
        Gets the md5 of this ObjectSummary.
        Base64-encoded MD5 hash of the object data.


        :return: The md5 of this ObjectSummary.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this ObjectSummary.
        Base64-encoded MD5 hash of the object data.


        :param md5: The md5 of this ObjectSummary.
        :type: str
        """
        self._md5 = md5

    @property
    def time_created(self):
        """
        Gets the time_created of this ObjectSummary.
        The date and time the object was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :return: The time_created of this ObjectSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ObjectSummary.
        The date and time the object was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :param time_created: The time_created of this ObjectSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def etag(self):
        """
        Gets the etag of this ObjectSummary.
        The current entity tag (ETag) for the object.


        :return: The etag of this ObjectSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this ObjectSummary.
        The current entity tag (ETag) for the object.


        :param etag: The etag of this ObjectSummary.
        :type: str
        """
        self._etag = etag

    @property
    def time_modified(self):
        """
        Gets the time_modified of this ObjectSummary.
        The date and time the object was modified, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :return: The time_modified of this ObjectSummary.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ObjectSummary.
        The date and time the object was modified, as described in `RFC 2616`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc2616


        :param time_modified: The time_modified of this ObjectSummary.
        :type: datetime
        """
        self._time_modified = time_modified

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
