# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestoreObjectsDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new RestoreObjectsDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_name:
            The value to assign to the object_name property of this RestoreObjectsDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'object_name': 'str'
        }

        self.attribute_map = {
            'object_name': 'objectName'
        }

        self._object_name = None

    @property
    def object_name(self):
        """
        Gets the object_name of this RestoreObjectsDetails.
        A object which was in an archived state and need to be restored.


        :return: The object_name of this RestoreObjectsDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this RestoreObjectsDetails.
        A object which was in an archived state and need to be restored.


        :param object_name: The object_name of this RestoreObjectsDetails.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
