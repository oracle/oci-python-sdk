# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMacsecKey(object):
    """
    Defines the secret `OCID`__s held in Vault that represent the MACsec key.

    __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMacsecKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connectivity_association_name_secret_id:
            The value to assign to the connectivity_association_name_secret_id property of this CreateMacsecKey.
        :type connectivity_association_name_secret_id: str

        :param connectivity_association_key_secret_id:
            The value to assign to the connectivity_association_key_secret_id property of this CreateMacsecKey.
        :type connectivity_association_key_secret_id: str

        """
        self.swagger_types = {
            'connectivity_association_name_secret_id': 'str',
            'connectivity_association_key_secret_id': 'str'
        }

        self.attribute_map = {
            'connectivity_association_name_secret_id': 'connectivityAssociationNameSecretId',
            'connectivity_association_key_secret_id': 'connectivityAssociationKeySecretId'
        }

        self._connectivity_association_name_secret_id = None
        self._connectivity_association_key_secret_id = None

    @property
    def connectivity_association_name_secret_id(self):
        """
        **[Required]** Gets the connectivity_association_name_secret_id of this CreateMacsecKey.
        Secret `OCID`__ containing the Connectivity association Key Name (CKN) of this MACsec key.

        NOTE: Only the latest secret version will be used.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connectivity_association_name_secret_id of this CreateMacsecKey.
        :rtype: str
        """
        return self._connectivity_association_name_secret_id

    @connectivity_association_name_secret_id.setter
    def connectivity_association_name_secret_id(self, connectivity_association_name_secret_id):
        """
        Sets the connectivity_association_name_secret_id of this CreateMacsecKey.
        Secret `OCID`__ containing the Connectivity association Key Name (CKN) of this MACsec key.

        NOTE: Only the latest secret version will be used.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connectivity_association_name_secret_id: The connectivity_association_name_secret_id of this CreateMacsecKey.
        :type: str
        """
        self._connectivity_association_name_secret_id = connectivity_association_name_secret_id

    @property
    def connectivity_association_key_secret_id(self):
        """
        **[Required]** Gets the connectivity_association_key_secret_id of this CreateMacsecKey.
        Secret `OCID`__ containing the Connectivity Association Key (CAK) of this MACsec key.

        NOTE: Only the latest secret version will be used.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connectivity_association_key_secret_id of this CreateMacsecKey.
        :rtype: str
        """
        return self._connectivity_association_key_secret_id

    @connectivity_association_key_secret_id.setter
    def connectivity_association_key_secret_id(self, connectivity_association_key_secret_id):
        """
        Sets the connectivity_association_key_secret_id of this CreateMacsecKey.
        Secret `OCID`__ containing the Connectivity Association Key (CAK) of this MACsec key.

        NOTE: Only the latest secret version will be used.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connectivity_association_key_secret_id: The connectivity_association_key_secret_id of this CreateMacsecKey.
        :type: str
        """
        self._connectivity_association_key_secret_id = connectivity_association_key_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
