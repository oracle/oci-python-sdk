# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFullPushDownTaskDetails(object):
    """
    The full pushdown task parameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFullPushDownTaskDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateFullPushDownTaskDetails.
        :type model_type: str

        :param source:
            The value to assign to the source property of this CreateFullPushDownTaskDetails.
        :type source: oci.data_connectivity.models.Source

        :param target:
            The value to assign to the target property of this CreateFullPushDownTaskDetails.
        :type target: oci.data_connectivity.models.Target

        """
        self.swagger_types = {
            'model_type': 'str',
            'source': 'Source',
            'target': 'Target'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'source': 'source',
            'target': 'target'
        }

        self._model_type = None
        self._source = None
        self._target = None

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this CreateFullPushDownTaskDetails.
        The type of of FullPushDownTask.


        :return: The model_type of this CreateFullPushDownTaskDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateFullPushDownTaskDetails.
        The type of of FullPushDownTask.


        :param model_type: The model_type of this CreateFullPushDownTaskDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def source(self):
        """
        Gets the source of this CreateFullPushDownTaskDetails.

        :return: The source of this CreateFullPushDownTaskDetails.
        :rtype: oci.data_connectivity.models.Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateFullPushDownTaskDetails.

        :param source: The source of this CreateFullPushDownTaskDetails.
        :type: oci.data_connectivity.models.Source
        """
        self._source = source

    @property
    def target(self):
        """
        Gets the target of this CreateFullPushDownTaskDetails.

        :return: The target of this CreateFullPushDownTaskDetails.
        :rtype: oci.data_connectivity.models.Target
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CreateFullPushDownTaskDetails.

        :param target: The target of this CreateFullPushDownTaskDetails.
        :type: oci.data_connectivity.models.Target
        """
        self._target = target

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
