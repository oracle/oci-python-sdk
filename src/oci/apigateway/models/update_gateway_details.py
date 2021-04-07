# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGatewayDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateGatewayDetails.
        :type display_name: str

        :param certificate_id:
            The value to assign to the certificate_id property of this UpdateGatewayDetails.
        :type certificate_id: str

        :param response_cache_details:
            The value to assign to the response_cache_details property of this UpdateGatewayDetails.
        :type response_cache_details: oci.apigateway.models.ResponseCacheDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'certificate_id': 'str',
            'response_cache_details': 'ResponseCacheDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'certificate_id': 'certificateId',
            'response_cache_details': 'responseCacheDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._certificate_id = None
        self._response_cache_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this UpdateGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this UpdateGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this UpdateGatewayDetails.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The certificate_id of this UpdateGatewayDetails.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this UpdateGatewayDetails.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param certificate_id: The certificate_id of this UpdateGatewayDetails.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def response_cache_details(self):
        """
        Gets the response_cache_details of this UpdateGatewayDetails.

        :return: The response_cache_details of this UpdateGatewayDetails.
        :rtype: oci.apigateway.models.ResponseCacheDetails
        """
        return self._response_cache_details

    @response_cache_details.setter
    def response_cache_details(self, response_cache_details):
        """
        Sets the response_cache_details of this UpdateGatewayDetails.

        :param response_cache_details: The response_cache_details of this UpdateGatewayDetails.
        :type: oci.apigateway.models.ResponseCacheDetails
        """
        self._response_cache_details = response_cache_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateGatewayDetails.
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
