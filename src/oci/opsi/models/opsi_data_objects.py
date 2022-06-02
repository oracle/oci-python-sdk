# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiDataObjects(object):
    """
    Logical grouping used for OPSI data object targeted operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiDataObjects object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opsi_data_objects:
            The value to assign to the opsi_data_objects property of this OpsiDataObjects.
        :type opsi_data_objects: object

        """
        self.swagger_types = {
            'opsi_data_objects': 'object'
        }

        self.attribute_map = {
            'opsi_data_objects': 'opsiDataObjects'
        }

        self._opsi_data_objects = None

    @property
    def opsi_data_objects(self):
        """
        Gets the opsi_data_objects of this OpsiDataObjects.
        OPSI Data Object.


        :return: The opsi_data_objects of this OpsiDataObjects.
        :rtype: object
        """
        return self._opsi_data_objects

    @opsi_data_objects.setter
    def opsi_data_objects(self, opsi_data_objects):
        """
        Sets the opsi_data_objects of this OpsiDataObjects.
        OPSI Data Object.


        :param opsi_data_objects: The opsi_data_objects of this OpsiDataObjects.
        :type: object
        """
        self._opsi_data_objects = opsi_data_objects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
