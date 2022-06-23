# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePathAnalyzerTestDetails(object):
    """
    Details used to create a `PathAnalyzerTest` resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePathAnalyzerTestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreatePathAnalyzerTestDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreatePathAnalyzerTestDetails.
        :type compartment_id: str

        :param protocol:
            The value to assign to the protocol property of this CreatePathAnalyzerTestDetails.
        :type protocol: int

        :param source_endpoint:
            The value to assign to the source_endpoint property of this CreatePathAnalyzerTestDetails.
        :type source_endpoint: oci.vn_monitoring.models.Endpoint

        :param destination_endpoint:
            The value to assign to the destination_endpoint property of this CreatePathAnalyzerTestDetails.
        :type destination_endpoint: oci.vn_monitoring.models.Endpoint

        :param protocol_parameters:
            The value to assign to the protocol_parameters property of this CreatePathAnalyzerTestDetails.
        :type protocol_parameters: oci.vn_monitoring.models.ProtocolParameters

        :param query_options:
            The value to assign to the query_options property of this CreatePathAnalyzerTestDetails.
        :type query_options: oci.vn_monitoring.models.QueryOptions

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreatePathAnalyzerTestDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreatePathAnalyzerTestDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'protocol': 'int',
            'source_endpoint': 'Endpoint',
            'destination_endpoint': 'Endpoint',
            'protocol_parameters': 'ProtocolParameters',
            'query_options': 'QueryOptions',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'protocol': 'protocol',
            'source_endpoint': 'sourceEndpoint',
            'destination_endpoint': 'destinationEndpoint',
            'protocol_parameters': 'protocolParameters',
            'query_options': 'queryOptions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._protocol = None
        self._source_endpoint = None
        self._destination_endpoint = None
        self._protocol_parameters = None
        self._query_options = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreatePathAnalyzerTestDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreatePathAnalyzerTestDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePathAnalyzerTestDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreatePathAnalyzerTestDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreatePathAnalyzerTestDetails.
        The `OCID`__ for the `PathAnalyzerTest` resource's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreatePathAnalyzerTestDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreatePathAnalyzerTestDetails.
        The `OCID`__ for the `PathAnalyzerTest` resource's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreatePathAnalyzerTestDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreatePathAnalyzerTestDetails.
        The IP protocol to use in the `PathAnalyzerTest` resource.


        :return: The protocol of this CreatePathAnalyzerTestDetails.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreatePathAnalyzerTestDetails.
        The IP protocol to use in the `PathAnalyzerTest` resource.


        :param protocol: The protocol of this CreatePathAnalyzerTestDetails.
        :type: int
        """
        self._protocol = protocol

    @property
    def source_endpoint(self):
        """
        **[Required]** Gets the source_endpoint of this CreatePathAnalyzerTestDetails.

        :return: The source_endpoint of this CreatePathAnalyzerTestDetails.
        :rtype: oci.vn_monitoring.models.Endpoint
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """
        Sets the source_endpoint of this CreatePathAnalyzerTestDetails.

        :param source_endpoint: The source_endpoint of this CreatePathAnalyzerTestDetails.
        :type: oci.vn_monitoring.models.Endpoint
        """
        self._source_endpoint = source_endpoint

    @property
    def destination_endpoint(self):
        """
        **[Required]** Gets the destination_endpoint of this CreatePathAnalyzerTestDetails.

        :return: The destination_endpoint of this CreatePathAnalyzerTestDetails.
        :rtype: oci.vn_monitoring.models.Endpoint
        """
        return self._destination_endpoint

    @destination_endpoint.setter
    def destination_endpoint(self, destination_endpoint):
        """
        Sets the destination_endpoint of this CreatePathAnalyzerTestDetails.

        :param destination_endpoint: The destination_endpoint of this CreatePathAnalyzerTestDetails.
        :type: oci.vn_monitoring.models.Endpoint
        """
        self._destination_endpoint = destination_endpoint

    @property
    def protocol_parameters(self):
        """
        Gets the protocol_parameters of this CreatePathAnalyzerTestDetails.

        :return: The protocol_parameters of this CreatePathAnalyzerTestDetails.
        :rtype: oci.vn_monitoring.models.ProtocolParameters
        """
        return self._protocol_parameters

    @protocol_parameters.setter
    def protocol_parameters(self, protocol_parameters):
        """
        Sets the protocol_parameters of this CreatePathAnalyzerTestDetails.

        :param protocol_parameters: The protocol_parameters of this CreatePathAnalyzerTestDetails.
        :type: oci.vn_monitoring.models.ProtocolParameters
        """
        self._protocol_parameters = protocol_parameters

    @property
    def query_options(self):
        """
        Gets the query_options of this CreatePathAnalyzerTestDetails.

        :return: The query_options of this CreatePathAnalyzerTestDetails.
        :rtype: oci.vn_monitoring.models.QueryOptions
        """
        return self._query_options

    @query_options.setter
    def query_options(self, query_options):
        """
        Sets the query_options of this CreatePathAnalyzerTestDetails.

        :param query_options: The query_options of this CreatePathAnalyzerTestDetails.
        :type: oci.vn_monitoring.models.QueryOptions
        """
        self._query_options = query_options

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreatePathAnalyzerTestDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreatePathAnalyzerTestDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreatePathAnalyzerTestDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreatePathAnalyzerTestDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreatePathAnalyzerTestDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreatePathAnalyzerTestDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreatePathAnalyzerTestDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreatePathAnalyzerTestDetails.
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
