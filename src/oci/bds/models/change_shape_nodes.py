# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeShapeNodes(object):
    """
    Individual worker nodes groups details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeShapeNodes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param worker:
            The value to assign to the worker property of this ChangeShapeNodes.
        :type worker: str

        :param worker_shape_config:
            The value to assign to the worker_shape_config property of this ChangeShapeNodes.
        :type worker_shape_config: oci.bds.models.ShapeConfigDetails

        :param compute_only_worker:
            The value to assign to the compute_only_worker property of this ChangeShapeNodes.
        :type compute_only_worker: str

        :param compute_only_worker_shape_config:
            The value to assign to the compute_only_worker_shape_config property of this ChangeShapeNodes.
        :type compute_only_worker_shape_config: oci.bds.models.ShapeConfigDetails

        :param master:
            The value to assign to the master property of this ChangeShapeNodes.
        :type master: str

        :param master_shape_config:
            The value to assign to the master_shape_config property of this ChangeShapeNodes.
        :type master_shape_config: oci.bds.models.ShapeConfigDetails

        :param utility:
            The value to assign to the utility property of this ChangeShapeNodes.
        :type utility: str

        :param utility_shape_config:
            The value to assign to the utility_shape_config property of this ChangeShapeNodes.
        :type utility_shape_config: oci.bds.models.ShapeConfigDetails

        :param cloudsql:
            The value to assign to the cloudsql property of this ChangeShapeNodes.
        :type cloudsql: str

        """
        self.swagger_types = {
            'worker': 'str',
            'worker_shape_config': 'ShapeConfigDetails',
            'compute_only_worker': 'str',
            'compute_only_worker_shape_config': 'ShapeConfigDetails',
            'master': 'str',
            'master_shape_config': 'ShapeConfigDetails',
            'utility': 'str',
            'utility_shape_config': 'ShapeConfigDetails',
            'cloudsql': 'str'
        }

        self.attribute_map = {
            'worker': 'worker',
            'worker_shape_config': 'workerShapeConfig',
            'compute_only_worker': 'computeOnlyWorker',
            'compute_only_worker_shape_config': 'computeOnlyWorkerShapeConfig',
            'master': 'master',
            'master_shape_config': 'masterShapeConfig',
            'utility': 'utility',
            'utility_shape_config': 'utilityShapeConfig',
            'cloudsql': 'cloudsql'
        }

        self._worker = None
        self._worker_shape_config = None
        self._compute_only_worker = None
        self._compute_only_worker_shape_config = None
        self._master = None
        self._master_shape_config = None
        self._utility = None
        self._utility_shape_config = None
        self._cloudsql = None

    @property
    def worker(self):
        """
        Gets the worker of this ChangeShapeNodes.
        Change shape of worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :return: The worker of this ChangeShapeNodes.
        :rtype: str
        """
        return self._worker

    @worker.setter
    def worker(self, worker):
        """
        Sets the worker of this ChangeShapeNodes.
        Change shape of worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :param worker: The worker of this ChangeShapeNodes.
        :type: str
        """
        self._worker = worker

    @property
    def worker_shape_config(self):
        """
        Gets the worker_shape_config of this ChangeShapeNodes.

        :return: The worker_shape_config of this ChangeShapeNodes.
        :rtype: oci.bds.models.ShapeConfigDetails
        """
        return self._worker_shape_config

    @worker_shape_config.setter
    def worker_shape_config(self, worker_shape_config):
        """
        Sets the worker_shape_config of this ChangeShapeNodes.

        :param worker_shape_config: The worker_shape_config of this ChangeShapeNodes.
        :type: oci.bds.models.ShapeConfigDetails
        """
        self._worker_shape_config = worker_shape_config

    @property
    def compute_only_worker(self):
        """
        Gets the compute_only_worker of this ChangeShapeNodes.
        Change shape of compute only worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :return: The compute_only_worker of this ChangeShapeNodes.
        :rtype: str
        """
        return self._compute_only_worker

    @compute_only_worker.setter
    def compute_only_worker(self, compute_only_worker):
        """
        Sets the compute_only_worker of this ChangeShapeNodes.
        Change shape of compute only worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :param compute_only_worker: The compute_only_worker of this ChangeShapeNodes.
        :type: str
        """
        self._compute_only_worker = compute_only_worker

    @property
    def compute_only_worker_shape_config(self):
        """
        Gets the compute_only_worker_shape_config of this ChangeShapeNodes.

        :return: The compute_only_worker_shape_config of this ChangeShapeNodes.
        :rtype: oci.bds.models.ShapeConfigDetails
        """
        return self._compute_only_worker_shape_config

    @compute_only_worker_shape_config.setter
    def compute_only_worker_shape_config(self, compute_only_worker_shape_config):
        """
        Sets the compute_only_worker_shape_config of this ChangeShapeNodes.

        :param compute_only_worker_shape_config: The compute_only_worker_shape_config of this ChangeShapeNodes.
        :type: oci.bds.models.ShapeConfigDetails
        """
        self._compute_only_worker_shape_config = compute_only_worker_shape_config

    @property
    def master(self):
        """
        Gets the master of this ChangeShapeNodes.
        Change shape of master nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :return: The master of this ChangeShapeNodes.
        :rtype: str
        """
        return self._master

    @master.setter
    def master(self, master):
        """
        Sets the master of this ChangeShapeNodes.
        Change shape of master nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :param master: The master of this ChangeShapeNodes.
        :type: str
        """
        self._master = master

    @property
    def master_shape_config(self):
        """
        Gets the master_shape_config of this ChangeShapeNodes.

        :return: The master_shape_config of this ChangeShapeNodes.
        :rtype: oci.bds.models.ShapeConfigDetails
        """
        return self._master_shape_config

    @master_shape_config.setter
    def master_shape_config(self, master_shape_config):
        """
        Sets the master_shape_config of this ChangeShapeNodes.

        :param master_shape_config: The master_shape_config of this ChangeShapeNodes.
        :type: oci.bds.models.ShapeConfigDetails
        """
        self._master_shape_config = master_shape_config

    @property
    def utility(self):
        """
        Gets the utility of this ChangeShapeNodes.
        Change shape of utility nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :return: The utility of this ChangeShapeNodes.
        :rtype: str
        """
        return self._utility

    @utility.setter
    def utility(self, utility):
        """
        Sets the utility of this ChangeShapeNodes.
        Change shape of utility nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.


        :param utility: The utility of this ChangeShapeNodes.
        :type: str
        """
        self._utility = utility

    @property
    def utility_shape_config(self):
        """
        Gets the utility_shape_config of this ChangeShapeNodes.

        :return: The utility_shape_config of this ChangeShapeNodes.
        :rtype: oci.bds.models.ShapeConfigDetails
        """
        return self._utility_shape_config

    @utility_shape_config.setter
    def utility_shape_config(self, utility_shape_config):
        """
        Sets the utility_shape_config of this ChangeShapeNodes.

        :param utility_shape_config: The utility_shape_config of this ChangeShapeNodes.
        :type: oci.bds.models.ShapeConfigDetails
        """
        self._utility_shape_config = utility_shape_config

    @property
    def cloudsql(self):
        """
        Gets the cloudsql of this ChangeShapeNodes.
        Change shape of the Cloud SQL node to the desired target shape. Only VM_STANDARD shapes are allowed here.


        :return: The cloudsql of this ChangeShapeNodes.
        :rtype: str
        """
        return self._cloudsql

    @cloudsql.setter
    def cloudsql(self, cloudsql):
        """
        Sets the cloudsql of this ChangeShapeNodes.
        Change shape of the Cloud SQL node to the desired target shape. Only VM_STANDARD shapes are allowed here.


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
