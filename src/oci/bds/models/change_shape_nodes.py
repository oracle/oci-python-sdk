# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeShapeNodes(object):
    """
    ChangeShapeNodes model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeShapeNodes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param worker:
            The value to assign to the worker property of this ChangeShapeNodes.
        :type worker: str

        :param master:
            The value to assign to the master property of this ChangeShapeNodes.
        :type master: str

        :param utility:
            The value to assign to the utility property of this ChangeShapeNodes.
        :type utility: str

        :param cloudsql:
            The value to assign to the cloudsql property of this ChangeShapeNodes.
        :type cloudsql: str

        """
        self.swagger_types = {
            'worker': 'str',
            'master': 'str',
            'utility': 'str',
            'cloudsql': 'str'
        }

        self.attribute_map = {
            'worker': 'worker',
            'master': 'master',
            'utility': 'utility',
            'cloudsql': 'cloudsql'
        }

        self._worker = None
        self._master = None
        self._utility = None
        self._cloudsql = None

    @property
    def worker(self):
        """
        Gets the worker of this ChangeShapeNodes.
        worker nodes shape


        :return: The worker of this ChangeShapeNodes.
        :rtype: str
        """
        return self._worker

    @worker.setter
    def worker(self, worker):
        """
        Sets the worker of this ChangeShapeNodes.
        worker nodes shape


        :param worker: The worker of this ChangeShapeNodes.
        :type: str
        """
        self._worker = worker

    @property
    def master(self):
        """
        Gets the master of this ChangeShapeNodes.
        master nodes shape


        :return: The master of this ChangeShapeNodes.
        :rtype: str
        """
        return self._master

    @master.setter
    def master(self, master):
        """
        Sets the master of this ChangeShapeNodes.
        master nodes shape


        :param master: The master of this ChangeShapeNodes.
        :type: str
        """
        self._master = master

    @property
    def utility(self):
        """
        Gets the utility of this ChangeShapeNodes.
        utility nodes shape


        :return: The utility of this ChangeShapeNodes.
        :rtype: str
        """
        return self._utility

    @utility.setter
    def utility(self, utility):
        """
        Sets the utility of this ChangeShapeNodes.
        utility nodes shape


        :param utility: The utility of this ChangeShapeNodes.
        :type: str
        """
        self._utility = utility

    @property
    def cloudsql(self):
        """
        Gets the cloudsql of this ChangeShapeNodes.
        cloudsql node shape


        :return: The cloudsql of this ChangeShapeNodes.
        :rtype: str
        """
        return self._cloudsql

    @cloudsql.setter
    def cloudsql(self, cloudsql):
        """
        Sets the cloudsql of this ChangeShapeNodes.
        cloudsql node shape


        :param cloudsql: The cloudsql of this ChangeShapeNodes.
        :type: str
        """
        self._cloudsql = cloudsql

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
