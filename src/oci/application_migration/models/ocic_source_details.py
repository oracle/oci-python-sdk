# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .source_details import SourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OcicSourceDetails(SourceDetails):
    """
    Specifies configuration specific to the source environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OcicSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.OcicSourceDetails.type` attribute
        of this class is ``OCIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OcicSourceDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE"
        :type type: str

        :param region:
            The value to assign to the region property of this OcicSourceDetails.
        :type region: str

        :param compute_account:
            The value to assign to the compute_account property of this OcicSourceDetails.
        :type compute_account: str

        """
        self.swagger_types = {
            'type': 'str',
            'region': 'str',
            'compute_account': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'region': 'region',
            'compute_account': 'computeAccount'
        }

        self._type = None
        self._region = None
        self._compute_account = None
        self._type = 'OCIC'

    @property
    def region(self):
        """
        **[Required]** Gets the region of this OcicSourceDetails.
        The Oracle Cloud Infrastructure - Classic region name (e.g. us2-z11 or uscom-central-1)


        :return: The region of this OcicSourceDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this OcicSourceDetails.
        The Oracle Cloud Infrastructure - Classic region name (e.g. us2-z11 or uscom-central-1)


        :param region: The region of this OcicSourceDetails.
        :type: str
        """
        self._region = region

    @property
    def compute_account(self):
        """
        **[Required]** Gets the compute_account of this OcicSourceDetails.
        The compute account id


        :return: The compute_account of this OcicSourceDetails.
        :rtype: str
        """
        return self._compute_account

    @compute_account.setter
    def compute_account(self, compute_account):
        """
        Sets the compute_account of this OcicSourceDetails.
        The compute account id


        :param compute_account: The compute_account of this OcicSourceDetails.
        :type: str
        """
        self._compute_account = compute_account

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
