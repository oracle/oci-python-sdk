# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DnssecKeyVersionDsData(object):
    """
    Data for a parent zone DS record corresponding to this key-signing key (KSK).
    """

    #: A constant which can be used with the digest_type property of a DnssecKeyVersionDsData.
    #: This constant has a value of "SHA_256"
    DIGEST_TYPE_SHA_256 = "SHA_256"

    def __init__(self, **kwargs):
        """
        Initializes a new DnssecKeyVersionDsData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rdata:
            The value to assign to the rdata property of this DnssecKeyVersionDsData.
        :type rdata: str

        :param digest_type:
            The value to assign to the digest_type property of this DnssecKeyVersionDsData.
            Allowed values for this property are: "SHA_256", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type digest_type: str

        """
        self.swagger_types = {
            'rdata': 'str',
            'digest_type': 'str'
        }
        self.attribute_map = {
            'rdata': 'rdata',
            'digest_type': 'digestType'
        }
        self._rdata = None
        self._digest_type = None

    @property
    def rdata(self):
        """
        Gets the rdata of this DnssecKeyVersionDsData.
        Presentation-format DS record data that must be added to the parent zone. For more information about RDATA,
        see `Supported DNS Resource Record Types`__

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm


        :return: The rdata of this DnssecKeyVersionDsData.
        :rtype: str
        """
        return self._rdata

    @rdata.setter
    def rdata(self, rdata):
        """
        Sets the rdata of this DnssecKeyVersionDsData.
        Presentation-format DS record data that must be added to the parent zone. For more information about RDATA,
        see `Supported DNS Resource Record Types`__

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Reference/supporteddnsresource.htm


        :param rdata: The rdata of this DnssecKeyVersionDsData.
        :type: str
        """
        self._rdata = rdata

    @property
    def digest_type(self):
        """
        Gets the digest_type of this DnssecKeyVersionDsData.
        The type of the digest associated with the rdata.

        Allowed values for this property are: "SHA_256", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The digest_type of this DnssecKeyVersionDsData.
        :rtype: str
        """
        return self._digest_type

    @digest_type.setter
    def digest_type(self, digest_type):
        """
        Sets the digest_type of this DnssecKeyVersionDsData.
        The type of the digest associated with the rdata.


        :param digest_type: The digest_type of this DnssecKeyVersionDsData.
        :type: str
        """
        allowed_values = ["SHA_256"]
        if not value_allowed_none_or_none_sentinel(digest_type, allowed_values):
            digest_type = 'UNKNOWN_ENUM_VALUE'
        self._digest_type = digest_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
