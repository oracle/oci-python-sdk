# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMacsecKey(object):
    """
    An object defining the OCID of the Secret held in Vault that represent the MACsec key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMacsecKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connectivity_association_name_secret_id:
            The value to assign to the connectivity_association_name_secret_id property of this UpdateMacsecKey.
        :type connectivity_association_name_secret_id: str

        :param connectivity_association_name_secret_version:
            The value to assign to the connectivity_association_name_secret_version property of this UpdateMacsecKey.
        :type connectivity_association_name_secret_version: int

        :param connectivity_association_key_secret_id:
            The value to assign to the connectivity_association_key_secret_id property of this UpdateMacsecKey.
        :type connectivity_association_key_secret_id: str

        :param connectivity_association_key_secret_version:
            The value to assign to the connectivity_association_key_secret_version property of this UpdateMacsecKey.
        :type connectivity_association_key_secret_version: int

        """
        self.swagger_types = {
            'connectivity_association_name_secret_id': 'str',
            'connectivity_association_name_secret_version': 'int',
            'connectivity_association_key_secret_id': 'str',
            'connectivity_association_key_secret_version': 'int'
        }

        self.attribute_map = {
            'connectivity_association_name_secret_id': 'connectivityAssociationNameSecretId',
            'connectivity_association_name_secret_version': 'connectivityAssociationNameSecretVersion',
            'connectivity_association_key_secret_id': 'connectivityAssociationKeySecretId',
            'connectivity_association_key_secret_version': 'connectivityAssociationKeySecretVersion'
        }

        self._connectivity_association_name_secret_id = None
        self._connectivity_association_name_secret_version = None
        self._connectivity_association_key_secret_id = None
        self._connectivity_association_key_secret_version = None

    @property
    def connectivity_association_name_secret_id(self):
        """
        **[Required]** Gets the connectivity_association_name_secret_id of this UpdateMacsecKey.
        Secret `OCID`__ containing the Connectivity Association Key Name (CKN) of this MACsec key.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connectivity_association_name_secret_id of this UpdateMacsecKey.
        :rtype: str
        """
        return self._connectivity_association_name_secret_id

    @connectivity_association_name_secret_id.setter
    def connectivity_association_name_secret_id(self, connectivity_association_name_secret_id):
        """
        Sets the connectivity_association_name_secret_id of this UpdateMacsecKey.
        Secret `OCID`__ containing the Connectivity Association Key Name (CKN) of this MACsec key.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connectivity_association_name_secret_id: The connectivity_association_name_secret_id of this UpdateMacsecKey.
        :type: str
        """
        self._connectivity_association_name_secret_id = connectivity_association_name_secret_id

    @property
    def connectivity_association_name_secret_version(self):
        """
        **[Required]** Gets the connectivity_association_name_secret_version of this UpdateMacsecKey.
        The secret version of the connectivity association name secret in Vault.


        :return: The connectivity_association_name_secret_version of this UpdateMacsecKey.
        :rtype: int
        """
        return self._connectivity_association_name_secret_version

    @connectivity_association_name_secret_version.setter
    def connectivity_association_name_secret_version(self, connectivity_association_name_secret_version):
        """
        Sets the connectivity_association_name_secret_version of this UpdateMacsecKey.
        The secret version of the connectivity association name secret in Vault.


        :param connectivity_association_name_secret_version: The connectivity_association_name_secret_version of this UpdateMacsecKey.
        :type: int
        """
        self._connectivity_association_name_secret_version = connectivity_association_name_secret_version

    @property
    def connectivity_association_key_secret_id(self):
        """
        **[Required]** Gets the connectivity_association_key_secret_id of this UpdateMacsecKey.
        Secret `OCID`__ containing the Connectivity Association Key (CAK) of this MACsec key.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The connectivity_association_key_secret_id of this UpdateMacsecKey.
        :rtype: str
        """
        return self._connectivity_association_key_secret_id

    @connectivity_association_key_secret_id.setter
    def connectivity_association_key_secret_id(self, connectivity_association_key_secret_id):
        """
        Sets the connectivity_association_key_secret_id of this UpdateMacsecKey.
        Secret `OCID`__ containing the Connectivity Association Key (CAK) of this MACsec key.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param connectivity_association_key_secret_id: The connectivity_association_key_secret_id of this UpdateMacsecKey.
        :type: str
        """
        self._connectivity_association_key_secret_id = connectivity_association_key_secret_id

    @property
    def connectivity_association_key_secret_version(self):
        """
        **[Required]** Gets the connectivity_association_key_secret_version of this UpdateMacsecKey.
        The secret version of the connectivityAssociationKey secret in Vault.


        :return: The connectivity_association_key_secret_version of this UpdateMacsecKey.
        :rtype: int
        """
        return self._connectivity_association_key_secret_version

    @connectivity_association_key_secret_version.setter
    def connectivity_association_key_secret_version(self, connectivity_association_key_secret_version):
        """
        Sets the connectivity_association_key_secret_version of this UpdateMacsecKey.
        The secret version of the connectivityAssociationKey secret in Vault.


        :param connectivity_association_key_secret_version: The connectivity_association_key_secret_version of this UpdateMacsecKey.
        :type: int
        """
        self._connectivity_association_key_secret_version = connectivity_association_key_secret_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
