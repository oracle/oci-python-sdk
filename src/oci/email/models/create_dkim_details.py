# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDkimDetails(object):
    """
    Properties to create a new DKIM.
    The new object will be created in the same compartment as the EmailDomain.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDkimDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateDkimDetails.
        :type name: str

        :param email_domain_id:
            The value to assign to the email_domain_id property of this CreateDkimDetails.
        :type email_domain_id: str

        :param description:
            The value to assign to the description property of this CreateDkimDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDkimDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDkimDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'email_domain_id': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'email_domain_id': 'emailDomainId',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._email_domain_id = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        Gets the name of this CreateDkimDetails.
        The DKIM selector. This selector is required to be globally unique for this email domain.
        If you do not provide the selector, we will generate one for you.
        If you do provide the selector, we suggest adding a short region indicator
        to differentiate from your signing of emails in other regions you may be subscribed to.
        Selectors limited to ASCII characters may use alphanumeric, dash (\"-\"), and dot (\".\") characters.
        Non-ASCII selector names should adopt IDNA2008 normalization (RFC 5891-5892).

        Avoid entering confidential information.

        Example: `mydomain-phx-20210228`


        :return: The name of this CreateDkimDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDkimDetails.
        The DKIM selector. This selector is required to be globally unique for this email domain.
        If you do not provide the selector, we will generate one for you.
        If you do provide the selector, we suggest adding a short region indicator
        to differentiate from your signing of emails in other regions you may be subscribed to.
        Selectors limited to ASCII characters may use alphanumeric, dash (\"-\"), and dot (\".\") characters.
        Non-ASCII selector names should adopt IDNA2008 normalization (RFC 5891-5892).

        Avoid entering confidential information.

        Example: `mydomain-phx-20210228`


        :param name: The name of this CreateDkimDetails.
        :type: str
        """
        self._name = name

    @property
    def email_domain_id(self):
        """
        **[Required]** Gets the email_domain_id of this CreateDkimDetails.
        The `OCID`__ of the EmailDomain for this DKIM.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The email_domain_id of this CreateDkimDetails.
        :rtype: str
        """
        return self._email_domain_id

    @email_domain_id.setter
    def email_domain_id(self, email_domain_id):
        """
        Sets the email_domain_id of this CreateDkimDetails.
        The `OCID`__ of the EmailDomain for this DKIM.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param email_domain_id: The email_domain_id of this CreateDkimDetails.
        :type: str
        """
        self._email_domain_id = email_domain_id

    @property
    def description(self):
        """
        Gets the description of this CreateDkimDetails.
        A string that describes the details about the DKIM. It does not have to be unique,
        and you can change it. Avoid entering confidential information.


        :return: The description of this CreateDkimDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDkimDetails.
        A string that describes the details about the DKIM. It does not have to be unique,
        and you can change it. Avoid entering confidential information.


        :param description: The description of this CreateDkimDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDkimDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDkimDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDkimDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDkimDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDkimDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDkimDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDkimDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDkimDetails.
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
