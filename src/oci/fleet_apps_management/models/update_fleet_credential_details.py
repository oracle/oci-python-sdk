# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFleetCredentialDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFleetCredentialDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateFleetCredentialDetails.
        :type display_name: str

        :param entity_specifics:
            The value to assign to the entity_specifics property of this UpdateFleetCredentialDetails.
        :type entity_specifics: oci.fleet_apps_management.models.CredentialEntitySpecificDetails

        :param user:
            The value to assign to the user property of this UpdateFleetCredentialDetails.
        :type user: oci.fleet_apps_management.models.CredentialDetails

        :param password:
            The value to assign to the password property of this UpdateFleetCredentialDetails.
        :type password: oci.fleet_apps_management.models.CredentialDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'entity_specifics': 'CredentialEntitySpecificDetails',
            'user': 'CredentialDetails',
            'password': 'CredentialDetails'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'entity_specifics': 'entitySpecifics',
            'user': 'user',
            'password': 'password'
        }
        self._display_name = None
        self._entity_specifics = None
        self._user = None
        self._password = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateFleetCredentialDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this UpdateFleetCredentialDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateFleetCredentialDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this UpdateFleetCredentialDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def entity_specifics(self):
        """
        Gets the entity_specifics of this UpdateFleetCredentialDetails.

        :return: The entity_specifics of this UpdateFleetCredentialDetails.
        :rtype: oci.fleet_apps_management.models.CredentialEntitySpecificDetails
        """
        return self._entity_specifics

    @entity_specifics.setter
    def entity_specifics(self, entity_specifics):
        """
        Sets the entity_specifics of this UpdateFleetCredentialDetails.

        :param entity_specifics: The entity_specifics of this UpdateFleetCredentialDetails.
        :type: oci.fleet_apps_management.models.CredentialEntitySpecificDetails
        """
        self._entity_specifics = entity_specifics

    @property
    def user(self):
        """
        Gets the user of this UpdateFleetCredentialDetails.

        :return: The user of this UpdateFleetCredentialDetails.
        :rtype: oci.fleet_apps_management.models.CredentialDetails
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UpdateFleetCredentialDetails.

        :param user: The user of this UpdateFleetCredentialDetails.
        :type: oci.fleet_apps_management.models.CredentialDetails
        """
        self._user = user

    @property
    def password(self):
        """
        Gets the password of this UpdateFleetCredentialDetails.

        :return: The password of this UpdateFleetCredentialDetails.
        :rtype: oci.fleet_apps_management.models.CredentialDetails
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateFleetCredentialDetails.

        :param password: The password of this UpdateFleetCredentialDetails.
        :type: oci.fleet_apps_management.models.CredentialDetails
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
