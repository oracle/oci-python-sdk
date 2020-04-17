# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStreamPoolDetails(object):
    """
    Object used to create a stream pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStreamPoolDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateStreamPoolDetails.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this CreateStreamPoolDetails.
        :type name: str

        :param kafka_settings:
            The value to assign to the kafka_settings property of this CreateStreamPoolDetails.
        :type kafka_settings: KafkaSettings

        :param custom_encryption_key_details:
            The value to assign to the custom_encryption_key_details property of this CreateStreamPoolDetails.
        :type custom_encryption_key_details: CustomEncryptionKeyDetails

        :param private_endpoint_details:
            The value to assign to the private_endpoint_details property of this CreateStreamPoolDetails.
        :type private_endpoint_details: PrivateEndpointDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateStreamPoolDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateStreamPoolDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'kafka_settings': 'KafkaSettings',
            'custom_encryption_key_details': 'CustomEncryptionKeyDetails',
            'private_endpoint_details': 'PrivateEndpointDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'kafka_settings': 'kafkaSettings',
            'custom_encryption_key_details': 'customEncryptionKeyDetails',
            'private_endpoint_details': 'privateEndpointDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._name = None
        self._kafka_settings = None
        self._custom_encryption_key_details = None
        self._private_endpoint_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateStreamPoolDetails.
        The OCID of the compartment that contains the stream.


        :return: The compartment_id of this CreateStreamPoolDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateStreamPoolDetails.
        The OCID of the compartment that contains the stream.


        :param compartment_id: The compartment_id of this CreateStreamPoolDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateStreamPoolDetails.
        The name of the stream pool. Avoid entering confidential information.

        Example: `MyStreamPool`


        :return: The name of this CreateStreamPoolDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateStreamPoolDetails.
        The name of the stream pool. Avoid entering confidential information.

        Example: `MyStreamPool`


        :param name: The name of this CreateStreamPoolDetails.
        :type: str
        """
        self._name = name

    @property
    def kafka_settings(self):
        """
        Gets the kafka_settings of this CreateStreamPoolDetails.

        :return: The kafka_settings of this CreateStreamPoolDetails.
        :rtype: KafkaSettings
        """
        return self._kafka_settings

    @kafka_settings.setter
    def kafka_settings(self, kafka_settings):
        """
        Sets the kafka_settings of this CreateStreamPoolDetails.

        :param kafka_settings: The kafka_settings of this CreateStreamPoolDetails.
        :type: KafkaSettings
        """
        self._kafka_settings = kafka_settings

    @property
    def custom_encryption_key_details(self):
        """
        Gets the custom_encryption_key_details of this CreateStreamPoolDetails.

        :return: The custom_encryption_key_details of this CreateStreamPoolDetails.
        :rtype: CustomEncryptionKeyDetails
        """
        return self._custom_encryption_key_details

    @custom_encryption_key_details.setter
    def custom_encryption_key_details(self, custom_encryption_key_details):
        """
        Sets the custom_encryption_key_details of this CreateStreamPoolDetails.

        :param custom_encryption_key_details: The custom_encryption_key_details of this CreateStreamPoolDetails.
        :type: CustomEncryptionKeyDetails
        """
        self._custom_encryption_key_details = custom_encryption_key_details

    @property
    def private_endpoint_details(self):
        """
        Gets the private_endpoint_details of this CreateStreamPoolDetails.

        :return: The private_endpoint_details of this CreateStreamPoolDetails.
        :rtype: PrivateEndpointDetails
        """
        return self._private_endpoint_details

    @private_endpoint_details.setter
    def private_endpoint_details(self, private_endpoint_details):
        """
        Sets the private_endpoint_details of this CreateStreamPoolDetails.

        :param private_endpoint_details: The private_endpoint_details of this CreateStreamPoolDetails.
        :type: PrivateEndpointDetails
        """
        self._private_endpoint_details = private_endpoint_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateStreamPoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateStreamPoolDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateStreamPoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateStreamPoolDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateStreamPoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateStreamPoolDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateStreamPoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateStreamPoolDetails.
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
