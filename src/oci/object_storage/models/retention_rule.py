# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RetentionRule(object):
    """
    The details of a retention rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RetentionRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RetentionRule.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this RetentionRule.
        :type display_name: str

        :param duration:
            The value to assign to the duration property of this RetentionRule.
        :type duration: oci.object_storage.models.Duration

        :param etag:
            The value to assign to the etag property of this RetentionRule.
        :type etag: str

        :param time_rule_locked:
            The value to assign to the time_rule_locked property of this RetentionRule.
        :type time_rule_locked: datetime

        :param time_created:
            The value to assign to the time_created property of this RetentionRule.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this RetentionRule.
        :type time_modified: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'duration': 'Duration',
            'etag': 'str',
            'time_rule_locked': 'datetime',
            'time_created': 'datetime',
            'time_modified': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'duration': 'duration',
            'etag': 'etag',
            'time_rule_locked': 'timeRuleLocked',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified'
        }

        self._id = None
        self._display_name = None
        self._duration = None
        self._etag = None
        self._time_rule_locked = None
        self._time_created = None
        self._time_modified = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RetentionRule.
        Unique identifier for the retention rule.


        :return: The id of this RetentionRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RetentionRule.
        Unique identifier for the retention rule.


        :param id: The id of this RetentionRule.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this RetentionRule.
        User specified name for the retention rule.


        :return: The display_name of this RetentionRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RetentionRule.
        User specified name for the retention rule.


        :param display_name: The display_name of this RetentionRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def duration(self):
        """
        Gets the duration of this RetentionRule.

        :return: The duration of this RetentionRule.
        :rtype: oci.object_storage.models.Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this RetentionRule.

        :param duration: The duration of this RetentionRule.
        :type: oci.object_storage.models.Duration
        """
        self._duration = duration

    @property
    def etag(self):
        """
        **[Required]** Gets the etag of this RetentionRule.
        The entity tag (ETag) for the retention rule.


        :return: The etag of this RetentionRule.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this RetentionRule.
        The entity tag (ETag) for the retention rule.


        :param etag: The etag of this RetentionRule.
        :type: str
        """
        self._etag = etag

    @property
    def time_rule_locked(self):
        """
        Gets the time_rule_locked of this RetentionRule.
        The date and time as per `RFC 3339`__ after which this rule becomes locked.
        and can only be deleted by deleting the bucket.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_rule_locked of this RetentionRule.
        :rtype: datetime
        """
        return self._time_rule_locked

    @time_rule_locked.setter
    def time_rule_locked(self, time_rule_locked):
        """
        Sets the time_rule_locked of this RetentionRule.
        The date and time as per `RFC 3339`__ after which this rule becomes locked.
        and can only be deleted by deleting the bucket.

        __ https://tools.ietf.org/html/rfc3339


        :param time_rule_locked: The time_rule_locked of this RetentionRule.
        :type: datetime
        """
        self._time_rule_locked = time_rule_locked

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RetentionRule.
        The date and time that the retention rule was created as per `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this RetentionRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RetentionRule.
        The date and time that the retention rule was created as per `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this RetentionRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        **[Required]** Gets the time_modified of this RetentionRule.
        The date and time that the retention rule was modified as per `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_modified of this RetentionRule.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this RetentionRule.
        The date and time that the retention rule was modified as per `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_modified: The time_modified of this RetentionRule.
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
