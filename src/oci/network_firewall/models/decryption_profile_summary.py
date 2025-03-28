# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DecryptionProfileSummary(object):
    """
    Decryption Profile used on the firewall policy rules.
    """

    #: A constant which can be used with the type property of a DecryptionProfileSummary.
    #: This constant has a value of "SSL_INBOUND_INSPECTION"
    TYPE_SSL_INBOUND_INSPECTION = "SSL_INBOUND_INSPECTION"

    #: A constant which can be used with the type property of a DecryptionProfileSummary.
    #: This constant has a value of "SSL_FORWARD_PROXY"
    TYPE_SSL_FORWARD_PROXY = "SSL_FORWARD_PROXY"

    def __init__(self, **kwargs):
        """
        Initializes a new DecryptionProfileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DecryptionProfileSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this DecryptionProfileSummary.
            Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param parent_resource_id:
            The value to assign to the parent_resource_id property of this DecryptionProfileSummary.
        :type parent_resource_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'parent_resource_id': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'parent_resource_id': 'parentResourceId'
        }
        self._name = None
        self._type = None
        self._parent_resource_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DecryptionProfileSummary.
        Name of the secret.


        :return: The name of this DecryptionProfileSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DecryptionProfileSummary.
        Name of the secret.


        :param name: The name of this DecryptionProfileSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DecryptionProfileSummary.
        Type of the secrets mapped based on the policy.

          * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic.
          * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

        Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DecryptionProfileSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DecryptionProfileSummary.
        Type of the secrets mapped based on the policy.

          * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic.
          * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.


        :param type: The type of this DecryptionProfileSummary.
        :type: str
        """
        allowed_values = ["SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def parent_resource_id(self):
        """
        **[Required]** Gets the parent_resource_id of this DecryptionProfileSummary.
        OCID of the Network Firewall Policy this decryption profile belongs to.


        :return: The parent_resource_id of this DecryptionProfileSummary.
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """
        Sets the parent_resource_id of this DecryptionProfileSummary.
        OCID of the Network Firewall Policy this decryption profile belongs to.


        :param parent_resource_id: The parent_resource_id of this DecryptionProfileSummary.
        :type: str
        """
        self._parent_resource_id = parent_resource_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
