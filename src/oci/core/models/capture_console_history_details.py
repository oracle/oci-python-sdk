# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CaptureConsoleHistoryDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'instance_id': 'instanceId'
        }

        self._display_name = None
        self._instance_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CaptureConsoleHistoryDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CaptureConsoleHistoryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CaptureConsoleHistoryDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CaptureConsoleHistoryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        Gets the instance_id of this CaptureConsoleHistoryDetails.
        The OCID of the instance to get the console history from.


        :return: The instance_id of this CaptureConsoleHistoryDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CaptureConsoleHistoryDetails.
        The OCID of the instance to get the console history from.


        :param instance_id: The instance_id of this CaptureConsoleHistoryDetails.
        :type: str
        """
        self._instance_id = instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
