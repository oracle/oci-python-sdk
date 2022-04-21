# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIngressGatewayDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIngressGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateIngressGatewayDetails.
        :type description: str

        :param hosts:
            The value to assign to the hosts property of this UpdateIngressGatewayDetails.
        :type hosts: list[oci.service_mesh.models.IngressGatewayHost]

        :param access_logging:
            The value to assign to the access_logging property of this UpdateIngressGatewayDetails.
        :type access_logging: oci.service_mesh.models.AccessLoggingConfiguration

        :param mtls:
            The value to assign to the mtls property of this UpdateIngressGatewayDetails.
        :type mtls: oci.service_mesh.models.CreateIngressGatewayMutualTransportLayerSecurityDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateIngressGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateIngressGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'hosts': 'list[IngressGatewayHost]',
            'access_logging': 'AccessLoggingConfiguration',
            'mtls': 'CreateIngressGatewayMutualTransportLayerSecurityDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'hosts': 'hosts',
            'access_logging': 'accessLogging',
            'mtls': 'mtls',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._hosts = None
        self._access_logging = None
        self._mtls = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateIngressGatewayDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this UpdateIngressGatewayDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateIngressGatewayDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this UpdateIngressGatewayDetails.
        :type: str
        """
        self._description = description

    @property
    def hosts(self):
        """
        Gets the hosts of this UpdateIngressGatewayDetails.
        An array of hostnames and their listener configuration that this gateway will bind to.


        :return: The hosts of this UpdateIngressGatewayDetails.
        :rtype: list[oci.service_mesh.models.IngressGatewayHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this UpdateIngressGatewayDetails.
        An array of hostnames and their listener configuration that this gateway will bind to.


        :param hosts: The hosts of this UpdateIngressGatewayDetails.
        :type: list[oci.service_mesh.models.IngressGatewayHost]
        """
        self._hosts = hosts

    @property
    def access_logging(self):
        """
        Gets the access_logging of this UpdateIngressGatewayDetails.

        :return: The access_logging of this UpdateIngressGatewayDetails.
        :rtype: oci.service_mesh.models.AccessLoggingConfiguration
        """
        return self._access_logging

    @access_logging.setter
    def access_logging(self, access_logging):
        """
        Sets the access_logging of this UpdateIngressGatewayDetails.

        :param access_logging: The access_logging of this UpdateIngressGatewayDetails.
        :type: oci.service_mesh.models.AccessLoggingConfiguration
        """
        self._access_logging = access_logging

    @property
    def mtls(self):
        """
        Gets the mtls of this UpdateIngressGatewayDetails.

        :return: The mtls of this UpdateIngressGatewayDetails.
        :rtype: oci.service_mesh.models.CreateIngressGatewayMutualTransportLayerSecurityDetails
        """
        return self._mtls

    @mtls.setter
    def mtls(self, mtls):
        """
        Sets the mtls of this UpdateIngressGatewayDetails.

        :param mtls: The mtls of this UpdateIngressGatewayDetails.
        :type: oci.service_mesh.models.CreateIngressGatewayMutualTransportLayerSecurityDetails
        """
        self._mtls = mtls

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateIngressGatewayDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateIngressGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateIngressGatewayDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateIngressGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateIngressGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateIngressGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateIngressGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateIngressGatewayDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
