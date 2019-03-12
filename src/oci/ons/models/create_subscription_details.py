# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSubscriptionDetails(object):
    """
    The configuration details for creating the subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param topic_id:
            The value to assign to the topic_id property of this CreateSubscriptionDetails.
        :type topic_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSubscriptionDetails.
        :type compartment_id: str

        :param protocol:
            The value to assign to the protocol property of this CreateSubscriptionDetails.
        :type protocol: str

        :param endpoint:
            The value to assign to the endpoint property of this CreateSubscriptionDetails.
        :type endpoint: str

        :param metadata:
            The value to assign to the metadata property of this CreateSubscriptionDetails.
        :type metadata: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSubscriptionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSubscriptionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'topic_id': 'str',
            'compartment_id': 'str',
            'protocol': 'str',
            'endpoint': 'str',
            'metadata': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'topic_id': 'topicId',
            'compartment_id': 'compartmentId',
            'protocol': 'protocol',
            'endpoint': 'endpoint',
            'metadata': 'metadata',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._topic_id = None
        self._compartment_id = None
        self._protocol = None
        self._endpoint = None
        self._metadata = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def topic_id(self):
        """
        **[Required]** Gets the topic_id of this CreateSubscriptionDetails.
        The `OCID`__ of the topic for the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The topic_id of this CreateSubscriptionDetails.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """
        Sets the topic_id of this CreateSubscriptionDetails.
        The `OCID`__ of the topic for the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param topic_id: The topic_id of this CreateSubscriptionDetails.
        :type: str
        """
        self._topic_id = topic_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSubscriptionDetails.
        The `OCID`__ of the compartment for the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateSubscriptionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSubscriptionDetails.
        The `OCID`__ of the compartment for the subscription.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateSubscriptionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateSubscriptionDetails.
        The protocol to use for delivering messages. Valid values: EMAIL, HTTPS.


        :return: The protocol of this CreateSubscriptionDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateSubscriptionDetails.
        The protocol to use for delivering messages. Valid values: EMAIL, HTTPS.


        :param protocol: The protocol of this CreateSubscriptionDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def endpoint(self):
        """
        **[Required]** Gets the endpoint of this CreateSubscriptionDetails.
        The endpoint of the subscription. Valid values depend on the protocol.
        For EMAIL, only an email address is valid. For HTTPS, only a PagerDuty URL is valid. A URL cannot exceed 512 characters.
        Avoid entering confidential information.


        :return: The endpoint of this CreateSubscriptionDetails.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this CreateSubscriptionDetails.
        The endpoint of the subscription. Valid values depend on the protocol.
        For EMAIL, only an email address is valid. For HTTPS, only a PagerDuty URL is valid. A URL cannot exceed 512 characters.
        Avoid entering confidential information.


        :param endpoint: The endpoint of this CreateSubscriptionDetails.
        :type: str
        """
        self._endpoint = endpoint

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateSubscriptionDetails.
        Metadata for the subscription. Avoid entering confidential information.


        :return: The metadata of this CreateSubscriptionDetails.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateSubscriptionDetails.
        Metadata for the subscription. Avoid entering confidential information.


        :param metadata: The metadata of this CreateSubscriptionDetails.
        :type: str
        """
        self._metadata = metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSubscriptionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSubscriptionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSubscriptionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSubscriptionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSubscriptionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSubscriptionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSubscriptionDetails.
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
