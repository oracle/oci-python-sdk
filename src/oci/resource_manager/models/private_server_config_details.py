# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateServerConfigDetails(object):
    """
    Details about a private endpoint associated with the configuration source provider.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateServerConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this PrivateServerConfigDetails.
        :type private_endpoint_id: str

        :param certificate_id:
            The value to assign to the certificate_id property of this PrivateServerConfigDetails.
        :type certificate_id: str

        """
        self.swagger_types = {
            'private_endpoint_id': 'str',
            'certificate_id': 'str'
        }

        self.attribute_map = {
            'private_endpoint_id': 'privateEndpointId',
            'certificate_id': 'certificateId'
        }

        self._private_endpoint_id = None
        self._certificate_id = None

    @property
    def private_endpoint_id(self):
        """
        **[Required]** Gets the private_endpoint_id of this PrivateServerConfigDetails.
        The `OCID`__ of a private endpoint associated with the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The private_endpoint_id of this PrivateServerConfigDetails.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this PrivateServerConfigDetails.
        The `OCID`__ of a private endpoint associated with the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param private_endpoint_id: The private_endpoint_id of this PrivateServerConfigDetails.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    @property
    def certificate_id(self):
        """
        **[Required]** Gets the certificate_id of this PrivateServerConfigDetails.
        The `OCID`__ of a certificate associated with the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The certificate_id of this PrivateServerConfigDetails.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this PrivateServerConfigDetails.
        The `OCID`__ of a certificate associated with the configuration source provider.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param certificate_id: The certificate_id of this PrivateServerConfigDetails.
        :type: str
        """
        self._certificate_id = certificate_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
