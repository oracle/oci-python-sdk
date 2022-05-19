# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateChannelDetails(object):
    """
    Properties that are required to create a Channel.
    """

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "ANDROID"
    TYPE_ANDROID = "ANDROID"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "APPEVENT"
    TYPE_APPEVENT = "APPEVENT"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "APPLICATION"
    TYPE_APPLICATION = "APPLICATION"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "CORTANA"
    TYPE_CORTANA = "CORTANA"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "FACEBOOK"
    TYPE_FACEBOOK = "FACEBOOK"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "IOS"
    TYPE_IOS = "IOS"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "MSTEAMS"
    TYPE_MSTEAMS = "MSTEAMS"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "OSS"
    TYPE_OSS = "OSS"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "OSVC"
    TYPE_OSVC = "OSVC"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "SERVICECLOUD"
    TYPE_SERVICECLOUD = "SERVICECLOUD"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "SLACK"
    TYPE_SLACK = "SLACK"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "TEST"
    TYPE_TEST = "TEST"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "TWILIO"
    TYPE_TWILIO = "TWILIO"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "WEB"
    TYPE_WEB = "WEB"

    #: A constant which can be used with the type property of a CreateChannelDetails.
    #: This constant has a value of "WEBHOOK"
    TYPE_WEBHOOK = "WEBHOOK"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateChannelDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.oda.models.CreateMSTeamsChannelDetails`
        * :class:`~oci.oda.models.CreateWebChannelDetails`
        * :class:`~oci.oda.models.CreateFacebookChannelDetails`
        * :class:`~oci.oda.models.CreateApplicationChannelDetails`
        * :class:`~oci.oda.models.CreateServiceCloudChannelDetails`
        * :class:`~oci.oda.models.CreateSlackChannelDetails`
        * :class:`~oci.oda.models.CreateOsvcChannelDetails`
        * :class:`~oci.oda.models.CreateAppEventChannelDetails`
        * :class:`~oci.oda.models.CreateOSSChannelDetails`
        * :class:`~oci.oda.models.CreateCortanaChannelDetails`
        * :class:`~oci.oda.models.CreateAndroidChannelDetails`
        * :class:`~oci.oda.models.CreateTwilioChannelDetails`
        * :class:`~oci.oda.models.CreateWebhookChannelDetails`
        * :class:`~oci.oda.models.CreateIosChannelDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateChannelDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'MSTEAMS':
            return 'CreateMSTeamsChannelDetails'

        if type == 'WEB':
            return 'CreateWebChannelDetails'

        if type == 'FACEBOOK':
            return 'CreateFacebookChannelDetails'

        if type == 'APPLICATION':
            return 'CreateApplicationChannelDetails'

        if type == 'SERVICECLOUD':
            return 'CreateServiceCloudChannelDetails'

        if type == 'SLACK':
            return 'CreateSlackChannelDetails'

        if type == 'OSVC':
            return 'CreateOsvcChannelDetails'

        if type == 'APPEVENT':
            return 'CreateAppEventChannelDetails'

        if type == 'OSS':
            return 'CreateOSSChannelDetails'

        if type == 'CORTANA':
            return 'CreateCortanaChannelDetails'

        if type == 'ANDROID':
            return 'CreateAndroidChannelDetails'

        if type == 'TWILIO':
            return 'CreateTwilioChannelDetails'

        if type == 'WEBHOOK':
            return 'CreateWebhookChannelDetails'

        if type == 'IOS':
            return 'CreateIosChannelDetails'
        else:
            return 'CreateChannelDetails'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateChannelDetails.
        The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.


        :return: The name of this CreateChannelDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateChannelDetails.
        The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.


        :param name: The name of this CreateChannelDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateChannelDetails.
        A short description of the Channel.


        :return: The description of this CreateChannelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateChannelDetails.
        A short description of the Channel.


        :param description: The description of this CreateChannelDetails.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateChannelDetails.
        The Channel type.

        Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"


        :return: The type of this CreateChannelDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateChannelDetails.
        The Channel type.


        :param type: The type of this CreateChannelDetails.
        :type: str
        """
        allowed_values = ["ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def session_expiry_duration_in_milliseconds(self):
        """
        Gets the session_expiry_duration_in_milliseconds of this CreateChannelDetails.
        The number of milliseconds before a session expires.


        :return: The session_expiry_duration_in_milliseconds of this CreateChannelDetails.
        :rtype: int
        """
        return self._session_expiry_duration_in_milliseconds

    @session_expiry_duration_in_milliseconds.setter
    def session_expiry_duration_in_milliseconds(self, session_expiry_duration_in_milliseconds):
        """
        Sets the session_expiry_duration_in_milliseconds of this CreateChannelDetails.
        The number of milliseconds before a session expires.


        :param session_expiry_duration_in_milliseconds: The session_expiry_duration_in_milliseconds of this CreateChannelDetails.
        :type: int
        """
        self._session_expiry_duration_in_milliseconds = session_expiry_duration_in_milliseconds

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateChannelDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateChannelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateChannelDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateChannelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateChannelDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateChannelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateChannelDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateChannelDetails.
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
