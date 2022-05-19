# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaInstanceOwner(object):
    """
    Details about an ODA instance owner
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OdaInstanceOwner object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param owner_service_name:
            The value to assign to the owner_service_name property of this OdaInstanceOwner.
        :type owner_service_name: str

        :param owner_service_tenancy:
            The value to assign to the owner_service_tenancy property of this OdaInstanceOwner.
        :type owner_service_tenancy: str

        """
        self.swagger_types = {
            'owner_service_name': 'str',
            'owner_service_tenancy': 'str'
        }

        self.attribute_map = {
            'owner_service_name': 'ownerServiceName',
            'owner_service_tenancy': 'ownerServiceTenancy'
        }

        self._owner_service_name = None
        self._owner_service_tenancy = None

    @property
    def owner_service_name(self):
        """
        **[Required]** Gets the owner_service_name of this OdaInstanceOwner.
        Name of the owner service principal


        :return: The owner_service_name of this OdaInstanceOwner.
        :rtype: str
        """
        return self._owner_service_name

    @owner_service_name.setter
    def owner_service_name(self, owner_service_name):
        """
        Sets the owner_service_name of this OdaInstanceOwner.
        Name of the owner service principal


        :param owner_service_name: The owner_service_name of this OdaInstanceOwner.
        :type: str
        """
        self._owner_service_name = owner_service_name

    @property
    def owner_service_tenancy(self):
        """
        **[Required]** Gets the owner_service_tenancy of this OdaInstanceOwner.
        Tenancy OCID of the owner service principal


        :return: The owner_service_tenancy of this OdaInstanceOwner.
        :rtype: str
        """
        return self._owner_service_tenancy

    @owner_service_tenancy.setter
    def owner_service_tenancy(self, owner_service_tenancy):
        """
        Sets the owner_service_tenancy of this OdaInstanceOwner.
        Tenancy OCID of the owner service principal


        :param owner_service_tenancy: The owner_service_tenancy of this OdaInstanceOwner.
        :type: str
        """
        self._owner_service_tenancy = owner_service_tenancy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
