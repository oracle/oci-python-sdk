# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateClusterDetails(object):
    """
    The properties that define a request to create a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateClusterDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateClusterDetails.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateClusterDetails.
        :type vcn_id: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this CreateClusterDetails.
        :type kubernetes_version: str

        :param options:
            The value to assign to the options property of this CreateClusterDetails.
        :type options: ClusterCreateOptions

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'kubernetes_version': 'str',
            'options': 'ClusterCreateOptions'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'kubernetes_version': 'kubernetesVersion',
            'options': 'options'
        }

        self._name = None
        self._compartment_id = None
        self._vcn_id = None
        self._kubernetes_version = None
        self._options = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateClusterDetails.
        The name of the cluster. Avoid entering confidential information.


        :return: The name of this CreateClusterDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateClusterDetails.
        The name of the cluster. Avoid entering confidential information.


        :param name: The name of this CreateClusterDetails.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateClusterDetails.
        The OCID of the compartment in which to create the cluster.


        :return: The compartment_id of this CreateClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateClusterDetails.
        The OCID of the compartment in which to create the cluster.


        :param compartment_id: The compartment_id of this CreateClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateClusterDetails.
        The OCID of the virtual cloud network (VCN) in which to create the cluster.


        :return: The vcn_id of this CreateClusterDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateClusterDetails.
        The OCID of the virtual cloud network (VCN) in which to create the cluster.


        :param vcn_id: The vcn_id of this CreateClusterDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def kubernetes_version(self):
        """
        **[Required]** Gets the kubernetes_version of this CreateClusterDetails.
        The version of Kubernetes to install into the cluster masters.


        :return: The kubernetes_version of this CreateClusterDetails.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        """
        Sets the kubernetes_version of this CreateClusterDetails.
        The version of Kubernetes to install into the cluster masters.


        :param kubernetes_version: The kubernetes_version of this CreateClusterDetails.
        :type: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def options(self):
        """
        Gets the options of this CreateClusterDetails.
        Optional attributes for the cluster.


        :return: The options of this CreateClusterDetails.
        :rtype: ClusterCreateOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this CreateClusterDetails.
        Optional attributes for the cluster.


        :param options: The options of this CreateClusterDetails.
        :type: ClusterCreateOptions
        """
        self._options = options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
