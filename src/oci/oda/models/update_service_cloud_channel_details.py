# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_channel_details import UpdateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateServiceCloudChannelDetails(UpdateChannelDetails):
    """
    Properties to update a Service Cloud agent channel.
    """

    #: A constant which can be used with the client_type property of a UpdateServiceCloudChannelDetails.
    #: This constant has a value of "WSDL"
    CLIENT_TYPE_WSDL = "WSDL"

    #: A constant which can be used with the client_type property of a UpdateServiceCloudChannelDetails.
    #: This constant has a value of "REST"
    CLIENT_TYPE_REST = "REST"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateServiceCloudChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.UpdateServiceCloudChannelDetails.type` attribute
        of this class is ``SERVICECLOUD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateServiceCloudChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this UpdateServiceCloudChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this UpdateServiceCloudChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateServiceCloudChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateServiceCloudChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param domain_name:
            The value to assign to the domain_name property of this UpdateServiceCloudChannelDetails.
        :type domain_name: str

        :param host_name_prefix:
            The value to assign to the host_name_prefix property of this UpdateServiceCloudChannelDetails.
        :type host_name_prefix: str

        :param user_name:
            The value to assign to the user_name property of this UpdateServiceCloudChannelDetails.
        :type user_name: str

        :param password:
            The value to assign to the password property of this UpdateServiceCloudChannelDetails.
        :type password: str

        :param client_type:
            The value to assign to the client_type property of this UpdateServiceCloudChannelDetails.
            Allowed values for this property are: "WSDL", "REST"
        :type client_type: str

        """
        self.swagger_types = {
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'domain_name': 'str',
            'host_name_prefix': 'str',
            'user_name': 'str',
            'password': 'str',
            'client_type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'domain_name': 'domainName',
            'host_name_prefix': 'hostNamePrefix',
            'user_name': 'userName',
            'password': 'password',
            'client_type': 'clientType'
        }

        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._domain_name = None
        self._host_name_prefix = None
        self._user_name = None
        self._password = None
        self._client_type = None
        self._type = 'SERVICECLOUD'

    @property
    def domain_name(self):
        """
        Gets the domain_name of this UpdateServiceCloudChannelDetails.
        The domain name.

        If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
        Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
        is sitename and the domain name is exampledomain.com.

        If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
        then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.


        :return: The domain_name of this UpdateServiceCloudChannelDetails.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this UpdateServiceCloudChannelDetails.
        The domain name.

        If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
        Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
        is sitename and the domain name is exampledomain.com.

        If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
        then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.


        :param domain_name: The domain_name of this UpdateServiceCloudChannelDetails.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def host_name_prefix(self):
        """
        Gets the host_name_prefix of this UpdateServiceCloudChannelDetails.
        The host prefix.

        If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
        Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
        is sitename and the domain name is exampledomain.com.

        If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
        then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.


        :return: The host_name_prefix of this UpdateServiceCloudChannelDetails.
        :rtype: str
        """
        return self._host_name_prefix

    @host_name_prefix.setter
    def host_name_prefix(self, host_name_prefix):
        """
        Sets the host_name_prefix of this UpdateServiceCloudChannelDetails.
        The host prefix.

        If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
        Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
        is sitename and the domain name is exampledomain.com.

        If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
        then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.


        :param host_name_prefix: The host_name_prefix of this UpdateServiceCloudChannelDetails.
        :type: str
        """
        self._host_name_prefix = host_name_prefix

    @property
    def user_name(self):
        """
        Gets the user_name of this UpdateServiceCloudChannelDetails.
        The user name for an Oracle B2C Service staff member who has the necessary profile permissions.


        :return: The user_name of this UpdateServiceCloudChannelDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UpdateServiceCloudChannelDetails.
        The user name for an Oracle B2C Service staff member who has the necessary profile permissions.


        :param user_name: The user_name of this UpdateServiceCloudChannelDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """
        Gets the password of this UpdateServiceCloudChannelDetails.
        The password for the Oracle B2C Service staff member who has the necessary profile permissions.


        :return: The password of this UpdateServiceCloudChannelDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateServiceCloudChannelDetails.
        The password for the Oracle B2C Service staff member who has the necessary profile permissions.


        :param password: The password of this UpdateServiceCloudChannelDetails.
        :type: str
        """
        self._password = password

    @property
    def client_type(self):
        """
        Gets the client_type of this UpdateServiceCloudChannelDetails.
        The type of Service Cloud client.

        Allowed values for this property are: "WSDL", "REST"


        :return: The client_type of this UpdateServiceCloudChannelDetails.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """
        Sets the client_type of this UpdateServiceCloudChannelDetails.
        The type of Service Cloud client.


        :param client_type: The client_type of this UpdateServiceCloudChannelDetails.
        :type: str
        """
        allowed_values = ["WSDL", "REST"]
        if not value_allowed_none_or_none_sentinel(client_type, allowed_values):
            raise ValueError(
                "Invalid value for `client_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._client_type = client_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
