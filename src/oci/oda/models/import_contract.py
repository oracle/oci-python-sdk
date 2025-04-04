# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportContract(object):
    """
    The contract guiding the import experience for the consumer and behavior of the resource providers for all resource types in a package.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportContract object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param import_contract:
            The value to assign to the import_contract property of this ImportContract.
        :type import_contract: list[oci.oda.models.ResourceTypeImportContract]

        """
        self.swagger_types = {
            'import_contract': 'list[ResourceTypeImportContract]'
        }
        self.attribute_map = {
            'import_contract': 'importContract'
        }
        self._import_contract = None

    @property
    def import_contract(self):
        """
        Gets the import_contract of this ImportContract.
        A list of resource type specific import contracts, one for each resource type listed in the package definition.


        :return: The import_contract of this ImportContract.
        :rtype: list[oci.oda.models.ResourceTypeImportContract]
        """
        return self._import_contract

    @import_contract.setter
    def import_contract(self, import_contract):
        """
        Sets the import_contract of this ImportContract.
        A list of resource type specific import contracts, one for each resource type listed in the package definition.


        :param import_contract: The import_contract of this ImportContract.
        :type: list[oci.oda.models.ResourceTypeImportContract]
        """
        self._import_contract = import_contract

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
