# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDomainDetails(object):
    """
    Create a domain details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDomainDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDomainDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDomainDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDomainDetails.
        :type description: str

        :param home_region:
            The value to assign to the home_region property of this CreateDomainDetails.
        :type home_region: str

        :param license_type:
            The value to assign to the license_type property of this CreateDomainDetails.
        :type license_type: str

        :param is_hidden_on_login:
            The value to assign to the is_hidden_on_login property of this CreateDomainDetails.
        :type is_hidden_on_login: bool

        :param admin_first_name:
            The value to assign to the admin_first_name property of this CreateDomainDetails.
        :type admin_first_name: str

        :param admin_last_name:
            The value to assign to the admin_last_name property of this CreateDomainDetails.
        :type admin_last_name: str

        :param admin_user_name:
            The value to assign to the admin_user_name property of this CreateDomainDetails.
        :type admin_user_name: str

        :param admin_email:
            The value to assign to the admin_email property of this CreateDomainDetails.
        :type admin_email: str

        :param is_notification_bypassed:
            The value to assign to the is_notification_bypassed property of this CreateDomainDetails.
        :type is_notification_bypassed: bool

        :param is_primary_email_required:
            The value to assign to the is_primary_email_required property of this CreateDomainDetails.
        :type is_primary_email_required: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDomainDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDomainDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'home_region': 'str',
            'license_type': 'str',
            'is_hidden_on_login': 'bool',
            'admin_first_name': 'str',
            'admin_last_name': 'str',
            'admin_user_name': 'str',
            'admin_email': 'str',
            'is_notification_bypassed': 'bool',
            'is_primary_email_required': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'home_region': 'homeRegion',
            'license_type': 'licenseType',
            'is_hidden_on_login': 'isHiddenOnLogin',
            'admin_first_name': 'adminFirstName',
            'admin_last_name': 'adminLastName',
            'admin_user_name': 'adminUserName',
            'admin_email': 'adminEmail',
            'is_notification_bypassed': 'isNotificationBypassed',
            'is_primary_email_required': 'isPrimaryEmailRequired',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._home_region = None
        self._license_type = None
        self._is_hidden_on_login = None
        self._admin_first_name = None
        self._admin_last_name = None
        self._admin_user_name = None
        self._admin_email = None
        self._is_notification_bypassed = None
        self._is_primary_email_required = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDomainDetails.
        The OCID of the Compartment where domain is created


        :return: The compartment_id of this CreateDomainDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDomainDetails.
        The OCID of the Compartment where domain is created


        :param compartment_id: The compartment_id of this CreateDomainDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDomainDetails.
        The mutable display name of the domain.


        :return: The display_name of this CreateDomainDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDomainDetails.
        The mutable display name of the domain.


        :param display_name: The display_name of this CreateDomainDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this CreateDomainDetails.
        Domain entity description


        :return: The description of this CreateDomainDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDomainDetails.
        Domain entity description


        :param description: The description of this CreateDomainDetails.
        :type: str
        """
        self._description = description

    @property
    def home_region(self):
        """
        **[Required]** Gets the home_region of this CreateDomainDetails.
        The region's name identifier. See `Regions and Availability Domains`__
        for the full list of supported region names.

        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The home_region of this CreateDomainDetails.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        """
        Sets the home_region of this CreateDomainDetails.
        The region's name identifier. See `Regions and Availability Domains`__
        for the full list of supported region names.

        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :param home_region: The home_region of this CreateDomainDetails.
        :type: str
        """
        self._home_region = home_region

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this CreateDomainDetails.
        The License type of Domain


        :return: The license_type of this CreateDomainDetails.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this CreateDomainDetails.
        The License type of Domain


        :param license_type: The license_type of this CreateDomainDetails.
        :type: str
        """
        self._license_type = license_type

    @property
    def is_hidden_on_login(self):
        """
        Gets the is_hidden_on_login of this CreateDomainDetails.
        Indicates whether domain is hidden on login screen or not.


        :return: The is_hidden_on_login of this CreateDomainDetails.
        :rtype: bool
        """
        return self._is_hidden_on_login

    @is_hidden_on_login.setter
    def is_hidden_on_login(self, is_hidden_on_login):
        """
        Sets the is_hidden_on_login of this CreateDomainDetails.
        Indicates whether domain is hidden on login screen or not.


        :param is_hidden_on_login: The is_hidden_on_login of this CreateDomainDetails.
        :type: bool
        """
        self._is_hidden_on_login = is_hidden_on_login

    @property
    def admin_first_name(self):
        """
        Gets the admin_first_name of this CreateDomainDetails.
        The admin first name


        :return: The admin_first_name of this CreateDomainDetails.
        :rtype: str
        """
        return self._admin_first_name

    @admin_first_name.setter
    def admin_first_name(self, admin_first_name):
        """
        Sets the admin_first_name of this CreateDomainDetails.
        The admin first name


        :param admin_first_name: The admin_first_name of this CreateDomainDetails.
        :type: str
        """
        self._admin_first_name = admin_first_name

    @property
    def admin_last_name(self):
        """
        Gets the admin_last_name of this CreateDomainDetails.
        The admin last name


        :return: The admin_last_name of this CreateDomainDetails.
        :rtype: str
        """
        return self._admin_last_name

    @admin_last_name.setter
    def admin_last_name(self, admin_last_name):
        """
        Sets the admin_last_name of this CreateDomainDetails.
        The admin last name


        :param admin_last_name: The admin_last_name of this CreateDomainDetails.
        :type: str
        """
        self._admin_last_name = admin_last_name

    @property
    def admin_user_name(self):
        """
        Gets the admin_user_name of this CreateDomainDetails.
        The admin user name


        :return: The admin_user_name of this CreateDomainDetails.
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        """
        Sets the admin_user_name of this CreateDomainDetails.
        The admin user name


        :param admin_user_name: The admin_user_name of this CreateDomainDetails.
        :type: str
        """
        self._admin_user_name = admin_user_name

    @property
    def admin_email(self):
        """
        Gets the admin_email of this CreateDomainDetails.
        The admin email address


        :return: The admin_email of this CreateDomainDetails.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this CreateDomainDetails.
        The admin email address


        :param admin_email: The admin_email of this CreateDomainDetails.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def is_notification_bypassed(self):
        """
        Gets the is_notification_bypassed of this CreateDomainDetails.
        Indicates if admin user created in IDCS stripe would like to receive notification like welcome email
        or not.
        Required field only if admin information is provided, otherwise optional.


        :return: The is_notification_bypassed of this CreateDomainDetails.
        :rtype: bool
        """
        return self._is_notification_bypassed

    @is_notification_bypassed.setter
    def is_notification_bypassed(self, is_notification_bypassed):
        """
        Sets the is_notification_bypassed of this CreateDomainDetails.
        Indicates if admin user created in IDCS stripe would like to receive notification like welcome email
        or not.
        Required field only if admin information is provided, otherwise optional.


        :param is_notification_bypassed: The is_notification_bypassed of this CreateDomainDetails.
        :type: bool
        """
        self._is_notification_bypassed = is_notification_bypassed

    @property
    def is_primary_email_required(self):
        """
        Gets the is_primary_email_required of this CreateDomainDetails.
        Optional field to indicate whether users in the domain are required to have a primary email address or not
        Defaults to true


        :return: The is_primary_email_required of this CreateDomainDetails.
        :rtype: bool
        """
        return self._is_primary_email_required

    @is_primary_email_required.setter
    def is_primary_email_required(self, is_primary_email_required):
        """
        Sets the is_primary_email_required of this CreateDomainDetails.
        Optional field to indicate whether users in the domain are required to have a primary email address or not
        Defaults to true


        :param is_primary_email_required: The is_primary_email_required of this CreateDomainDetails.
        :type: bool
        """
        self._is_primary_email_required = is_primary_email_required

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDomainDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDomainDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDomainDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDomainDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDomainDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDomainDetails.
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
