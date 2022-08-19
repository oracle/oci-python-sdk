# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmInstancesDetails(object):
    """
    Results of a emWarehouse search. Contains boh EmWarehouseSummary items and other information, such as metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EmInstancesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param em_id:
            The value to assign to the em_id property of this EmInstancesDetails.
        :type em_id: str

        :param targets_count:
            The value to assign to the targets_count property of this EmInstancesDetails.
        :type targets_count: int

        :param em_host:
            The value to assign to the em_host property of this EmInstancesDetails.
        :type em_host: str

        :param em_discoverer_url:
            The value to assign to the em_discoverer_url property of this EmInstancesDetails.
        :type em_discoverer_url: str

        """
        self.swagger_types = {
            'em_id': 'str',
            'targets_count': 'int',
            'em_host': 'str',
            'em_discoverer_url': 'str'
        }

        self.attribute_map = {
            'em_id': 'emId',
            'targets_count': 'targetsCount',
            'em_host': 'emHost',
            'em_discoverer_url': 'emDiscovererUrl'
        }

        self._em_id = None
        self._targets_count = None
        self._em_host = None
        self._em_discoverer_url = None

    @property
    def em_id(self):
        """
        **[Required]** Gets the em_id of this EmInstancesDetails.
        operations Insights Warehouse Identifier


        :return: The em_id of this EmInstancesDetails.
        :rtype: str
        """
        return self._em_id

    @em_id.setter
    def em_id(self, em_id):
        """
        Sets the em_id of this EmInstancesDetails.
        operations Insights Warehouse Identifier


        :param em_id: The em_id of this EmInstancesDetails.
        :type: str
        """
        self._em_id = em_id

    @property
    def targets_count(self):
        """
        Gets the targets_count of this EmInstancesDetails.
        EmInstance Target count


        :return: The targets_count of this EmInstancesDetails.
        :rtype: int
        """
        return self._targets_count

    @targets_count.setter
    def targets_count(self, targets_count):
        """
        Sets the targets_count of this EmInstancesDetails.
        EmInstance Target count


        :param targets_count: The targets_count of this EmInstancesDetails.
        :type: int
        """
        self._targets_count = targets_count

    @property
    def em_host(self):
        """
        Gets the em_host of this EmInstancesDetails.
        emHost name


        :return: The em_host of this EmInstancesDetails.
        :rtype: str
        """
        return self._em_host

    @em_host.setter
    def em_host(self, em_host):
        """
        Sets the em_host of this EmInstancesDetails.
        emHost name


        :param em_host: The em_host of this EmInstancesDetails.
        :type: str
        """
        self._em_host = em_host

    @property
    def em_discoverer_url(self):
        """
        Gets the em_discoverer_url of this EmInstancesDetails.
        emdDiscoverer url


        :return: The em_discoverer_url of this EmInstancesDetails.
        :rtype: str
        """
        return self._em_discoverer_url

    @em_discoverer_url.setter
    def em_discoverer_url(self, em_discoverer_url):
        """
        Sets the em_discoverer_url of this EmInstancesDetails.
        emdDiscoverer url


        :param em_discoverer_url: The em_discoverer_url of this EmInstancesDetails.
        :type: str
        """
        self._em_discoverer_url = em_discoverer_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
