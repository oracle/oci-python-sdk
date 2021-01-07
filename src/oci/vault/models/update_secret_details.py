# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSecretDetails(object):
    """
    Details for updating a secret.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSecretDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_version_number:
            The value to assign to the current_version_number property of this UpdateSecretDetails.
        :type current_version_number: int

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSecretDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this UpdateSecretDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSecretDetails.
        :type freeform_tags: dict(str, str)

        :param metadata:
            The value to assign to the metadata property of this UpdateSecretDetails.
        :type metadata: dict(str, object)

        :param secret_content:
            The value to assign to the secret_content property of this UpdateSecretDetails.
        :type secret_content: oci.vault.models.SecretContentDetails

        :param secret_rules:
            The value to assign to the secret_rules property of this UpdateSecretDetails.
        :type secret_rules: list[oci.vault.models.SecretRule]

        """
        self.swagger_types = {
            'current_version_number': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'metadata': 'dict(str, object)',
            'secret_content': 'SecretContentDetails',
            'secret_rules': 'list[SecretRule]'
        }

        self.attribute_map = {
            'current_version_number': 'currentVersionNumber',
            'defined_tags': 'definedTags',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'metadata': 'metadata',
            'secret_content': 'secretContent',
            'secret_rules': 'secretRules'
        }

        self._current_version_number = None
        self._defined_tags = None
        self._description = None
        self._freeform_tags = None
        self._metadata = None
        self._secret_content = None
        self._secret_rules = None

    @property
    def current_version_number(self):
        """
        Gets the current_version_number of this UpdateSecretDetails.
        Details to update the secret version of the specified secret. The secret contents,
        version number, and rules can't be specified at the same time.
        Updating the secret contents automatically creates a new secret version.


        :return: The current_version_number of this UpdateSecretDetails.
        :rtype: int
        """
        return self._current_version_number

    @current_version_number.setter
    def current_version_number(self, current_version_number):
        """
        Sets the current_version_number of this UpdateSecretDetails.
        Details to update the secret version of the specified secret. The secret contents,
        version number, and rules can't be specified at the same time.
        Updating the secret contents automatically creates a new secret version.


        :param current_version_number: The current_version_number of this UpdateSecretDetails.
        :type: int
        """
        self._current_version_number = current_version_number

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSecretDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSecretDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSecretDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSecretDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this UpdateSecretDetails.
        A brief description of the secret. Avoid entering confidential information.


        :return: The description of this UpdateSecretDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSecretDetails.
        A brief description of the secret. Avoid entering confidential information.


        :param description: The description of this UpdateSecretDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSecretDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSecretDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSecretDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSecretDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateSecretDetails.
        Additional metadata that you can use to provide context about how to use the secret or during rotation or
        other administrative tasks. For example, for a secret that you use to connect to a database, the additional
        metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.


        :return: The metadata of this UpdateSecretDetails.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateSecretDetails.
        Additional metadata that you can use to provide context about how to use the secret or during rotation or
        other administrative tasks. For example, for a secret that you use to connect to a database, the additional
        metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.


        :param metadata: The metadata of this UpdateSecretDetails.
        :type: dict(str, object)
        """
        self._metadata = metadata

    @property
    def secret_content(self):
        """
        Gets the secret_content of this UpdateSecretDetails.

        :return: The secret_content of this UpdateSecretDetails.
        :rtype: oci.vault.models.SecretContentDetails
        """
        return self._secret_content

    @secret_content.setter
    def secret_content(self, secret_content):
        """
        Sets the secret_content of this UpdateSecretDetails.

        :param secret_content: The secret_content of this UpdateSecretDetails.
        :type: oci.vault.models.SecretContentDetails
        """
        self._secret_content = secret_content

    @property
    def secret_rules(self):
        """
        Gets the secret_rules of this UpdateSecretDetails.
        A list of rules to control how the secret is used and managed.


        :return: The secret_rules of this UpdateSecretDetails.
        :rtype: list[oci.vault.models.SecretRule]
        """
        return self._secret_rules

    @secret_rules.setter
    def secret_rules(self, secret_rules):
        """
        Sets the secret_rules of this UpdateSecretDetails.
        A list of rules to control how the secret is used and managed.


        :param secret_rules: The secret_rules of this UpdateSecretDetails.
        :type: list[oci.vault.models.SecretRule]
        """
        self._secret_rules = secret_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
