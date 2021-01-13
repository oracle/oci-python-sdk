# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NotificationsTargetDetails(TargetDetails):
    """
    The topic used for the Notifications target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NotificationsTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.NotificationsTargetDetails.kind` attribute
        of this class is ``notifications`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this NotificationsTargetDetails.
            Allowed values for this property are: "functions", "loggingAnalytics", "monitoring", "notifications", "objectStorage", "streaming"
        :type kind: str

        :param topic_id:
            The value to assign to the topic_id property of this NotificationsTargetDetails.
        :type topic_id: str

        """
        self.swagger_types = {
            'kind': 'str',
            'topic_id': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'topic_id': 'topicId'
        }

        self._kind = None
        self._topic_id = None
        self._kind = 'notifications'

    @property
    def topic_id(self):
        """
        **[Required]** Gets the topic_id of this NotificationsTargetDetails.
        The `OCID`__ of the topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The topic_id of this NotificationsTargetDetails.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """
        Sets the topic_id of this NotificationsTargetDetails.
        The `OCID`__ of the topic.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param topic_id: The topic_id of this NotificationsTargetDetails.
        :type: str
        """
        self._topic_id = topic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
