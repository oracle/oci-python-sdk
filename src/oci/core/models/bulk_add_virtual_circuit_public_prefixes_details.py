# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkAddVirtualCircuitPublicPrefixesDetails(object):
    """
    BulkAddVirtualCircuitPublicPrefixesDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkAddVirtualCircuitPublicPrefixesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param public_prefixes:
            The value to assign to the public_prefixes property of this BulkAddVirtualCircuitPublicPrefixesDetails.
        :type public_prefixes: list[CreateVirtualCircuitPublicPrefixDetails]

        """
        self.swagger_types = {
            'public_prefixes': 'list[CreateVirtualCircuitPublicPrefixDetails]'
        }

        self.attribute_map = {
            'public_prefixes': 'publicPrefixes'
        }

        self._public_prefixes = None

    @property
    def public_prefixes(self):
        """
        **[Required]** Gets the public_prefixes of this BulkAddVirtualCircuitPublicPrefixesDetails.
        The public IP prefixes (CIDRs) to add to the public virtual circuit.


        :return: The public_prefixes of this BulkAddVirtualCircuitPublicPrefixesDetails.
        :rtype: list[CreateVirtualCircuitPublicPrefixDetails]
        """
        return self._public_prefixes

    @public_prefixes.setter
    def public_prefixes(self, public_prefixes):
        """
        Sets the public_prefixes of this BulkAddVirtualCircuitPublicPrefixesDetails.
        The public IP prefixes (CIDRs) to add to the public virtual circuit.


        :param public_prefixes: The public_prefixes of this BulkAddVirtualCircuitPublicPrefixesDetails.
        :type: list[CreateVirtualCircuitPublicPrefixDetails]
        """
        self._public_prefixes = public_prefixes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
