# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsTotpSettings(object):
    """
    Settings related to Time-Based One-Time Passcodes (TOTP), such as hashing algo, totp time step, passcode length, and so on

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    #: A constant which can be used with the hashing_algorithm property of a AuthenticationFactorSettingsTotpSettings.
    #: This constant has a value of "SHA1"
    HASHING_ALGORITHM_SHA1 = "SHA1"

    #: A constant which can be used with the hashing_algorithm property of a AuthenticationFactorSettingsTotpSettings.
    #: This constant has a value of "SHA256"
    HASHING_ALGORITHM_SHA256 = "SHA256"

    #: A constant which can be used with the hashing_algorithm property of a AuthenticationFactorSettingsTotpSettings.
    #: This constant has a value of "SHA384"
    HASHING_ALGORITHM_SHA384 = "SHA384"

    #: A constant which can be used with the hashing_algorithm property of a AuthenticationFactorSettingsTotpSettings.
    #: This constant has a value of "SHA512"
    HASHING_ALGORITHM_SHA512 = "SHA512"

    #: A constant which can be used with the hashing_algorithm property of a AuthenticationFactorSettingsTotpSettings.
    #: This constant has a value of "MD5"
    HASHING_ALGORITHM_MD5 = "MD5"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsTotpSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hashing_algorithm:
            The value to assign to the hashing_algorithm property of this AuthenticationFactorSettingsTotpSettings.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", "MD5", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type hashing_algorithm: str

        :param passcode_length:
            The value to assign to the passcode_length property of this AuthenticationFactorSettingsTotpSettings.
        :type passcode_length: int

        :param key_refresh_interval_in_days:
            The value to assign to the key_refresh_interval_in_days property of this AuthenticationFactorSettingsTotpSettings.
        :type key_refresh_interval_in_days: int

        :param time_step_in_secs:
            The value to assign to the time_step_in_secs property of this AuthenticationFactorSettingsTotpSettings.
        :type time_step_in_secs: int

        :param time_step_tolerance:
            The value to assign to the time_step_tolerance property of this AuthenticationFactorSettingsTotpSettings.
        :type time_step_tolerance: int

        :param sms_otp_validity_duration_in_mins:
            The value to assign to the sms_otp_validity_duration_in_mins property of this AuthenticationFactorSettingsTotpSettings.
        :type sms_otp_validity_duration_in_mins: int

        :param jwt_validity_duration_in_secs:
            The value to assign to the jwt_validity_duration_in_secs property of this AuthenticationFactorSettingsTotpSettings.
        :type jwt_validity_duration_in_secs: int

        :param sms_passcode_length:
            The value to assign to the sms_passcode_length property of this AuthenticationFactorSettingsTotpSettings.
        :type sms_passcode_length: int

        :param email_otp_validity_duration_in_mins:
            The value to assign to the email_otp_validity_duration_in_mins property of this AuthenticationFactorSettingsTotpSettings.
        :type email_otp_validity_duration_in_mins: int

        :param email_passcode_length:
            The value to assign to the email_passcode_length property of this AuthenticationFactorSettingsTotpSettings.
        :type email_passcode_length: int

        """
        self.swagger_types = {
            'hashing_algorithm': 'str',
            'passcode_length': 'int',
            'key_refresh_interval_in_days': 'int',
            'time_step_in_secs': 'int',
            'time_step_tolerance': 'int',
            'sms_otp_validity_duration_in_mins': 'int',
            'jwt_validity_duration_in_secs': 'int',
            'sms_passcode_length': 'int',
            'email_otp_validity_duration_in_mins': 'int',
            'email_passcode_length': 'int'
        }
        self.attribute_map = {
            'hashing_algorithm': 'hashingAlgorithm',
            'passcode_length': 'passcodeLength',
            'key_refresh_interval_in_days': 'keyRefreshIntervalInDays',
            'time_step_in_secs': 'timeStepInSecs',
            'time_step_tolerance': 'timeStepTolerance',
            'sms_otp_validity_duration_in_mins': 'smsOtpValidityDurationInMins',
            'jwt_validity_duration_in_secs': 'jwtValidityDurationInSecs',
            'sms_passcode_length': 'smsPasscodeLength',
            'email_otp_validity_duration_in_mins': 'emailOtpValidityDurationInMins',
            'email_passcode_length': 'emailPasscodeLength'
        }
        self._hashing_algorithm = None
        self._passcode_length = None
        self._key_refresh_interval_in_days = None
        self._time_step_in_secs = None
        self._time_step_tolerance = None
        self._sms_otp_validity_duration_in_mins = None
        self._jwt_validity_duration_in_secs = None
        self._sms_passcode_length = None
        self._email_otp_validity_duration_in_mins = None
        self._email_passcode_length = None

    @property
    def hashing_algorithm(self):
        """
        **[Required]** Gets the hashing_algorithm of this AuthenticationFactorSettingsTotpSettings.
        The hashing algorithm to be used to calculate a One-Time Passcode. By default, the system uses SHA1.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512", "MD5", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The hashing_algorithm of this AuthenticationFactorSettingsTotpSettings.
        :rtype: str
        """
        return self._hashing_algorithm

    @hashing_algorithm.setter
    def hashing_algorithm(self, hashing_algorithm):
        """
        Sets the hashing_algorithm of this AuthenticationFactorSettingsTotpSettings.
        The hashing algorithm to be used to calculate a One-Time Passcode. By default, the system uses SHA1.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param hashing_algorithm: The hashing_algorithm of this AuthenticationFactorSettingsTotpSettings.
        :type: str
        """
        allowed_values = ["SHA1", "SHA256", "SHA384", "SHA512", "MD5"]
        if not value_allowed_none_or_none_sentinel(hashing_algorithm, allowed_values):
            hashing_algorithm = 'UNKNOWN_ENUM_VALUE'
        self._hashing_algorithm = hashing_algorithm

    @property
    def passcode_length(self):
        """
        **[Required]** Gets the passcode_length of this AuthenticationFactorSettingsTotpSettings.
        Exact length of the One-Time Passcode that the system should generate

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 4
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The passcode_length of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._passcode_length

    @passcode_length.setter
    def passcode_length(self, passcode_length):
        """
        Sets the passcode_length of this AuthenticationFactorSettingsTotpSettings.
        Exact length of the One-Time Passcode that the system should generate

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 4
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param passcode_length: The passcode_length of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._passcode_length = passcode_length

    @property
    def key_refresh_interval_in_days(self):
        """
        **[Required]** Gets the key_refresh_interval_in_days of this AuthenticationFactorSettingsTotpSettings.
        The duration of time (in days) after which the shared secret has to be refreshed

        **SCIM++ Properties:**
         - idcsMaxValue: 999
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The key_refresh_interval_in_days of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._key_refresh_interval_in_days

    @key_refresh_interval_in_days.setter
    def key_refresh_interval_in_days(self, key_refresh_interval_in_days):
        """
        Sets the key_refresh_interval_in_days of this AuthenticationFactorSettingsTotpSettings.
        The duration of time (in days) after which the shared secret has to be refreshed

        **SCIM++ Properties:**
         - idcsMaxValue: 999
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param key_refresh_interval_in_days: The key_refresh_interval_in_days of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._key_refresh_interval_in_days = key_refresh_interval_in_days

    @property
    def time_step_in_secs(self):
        """
        **[Required]** Gets the time_step_in_secs of this AuthenticationFactorSettingsTotpSettings.
        Time (in secs) to be used as the time step

        **SCIM++ Properties:**
         - idcsMaxValue: 300
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The time_step_in_secs of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._time_step_in_secs

    @time_step_in_secs.setter
    def time_step_in_secs(self, time_step_in_secs):
        """
        Sets the time_step_in_secs of this AuthenticationFactorSettingsTotpSettings.
        Time (in secs) to be used as the time step

        **SCIM++ Properties:**
         - idcsMaxValue: 300
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param time_step_in_secs: The time_step_in_secs of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._time_step_in_secs = time_step_in_secs

    @property
    def time_step_tolerance(self):
        """
        **[Required]** Gets the time_step_tolerance of this AuthenticationFactorSettingsTotpSettings.
        The tolerance/step-size that the system should use when validating a One-Time Passcode

        **SCIM++ Properties:**
         - idcsMaxValue: 3
         - idcsMinValue: 2
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The time_step_tolerance of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._time_step_tolerance

    @time_step_tolerance.setter
    def time_step_tolerance(self, time_step_tolerance):
        """
        Sets the time_step_tolerance of this AuthenticationFactorSettingsTotpSettings.
        The tolerance/step-size that the system should use when validating a One-Time Passcode

        **SCIM++ Properties:**
         - idcsMaxValue: 3
         - idcsMinValue: 2
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param time_step_tolerance: The time_step_tolerance of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._time_step_tolerance = time_step_tolerance

    @property
    def sms_otp_validity_duration_in_mins(self):
        """
        **[Required]** Gets the sms_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        The period of time (in minutes) for which a One-Time Passcode that the system sends by Short Message Service (SMS) or by voice remains valid

        **SCIM++ Properties:**
         - idcsMaxValue: 60
         - idcsMinValue: 2
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The sms_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._sms_otp_validity_duration_in_mins

    @sms_otp_validity_duration_in_mins.setter
    def sms_otp_validity_duration_in_mins(self, sms_otp_validity_duration_in_mins):
        """
        Sets the sms_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        The period of time (in minutes) for which a One-Time Passcode that the system sends by Short Message Service (SMS) or by voice remains valid

        **SCIM++ Properties:**
         - idcsMaxValue: 60
         - idcsMinValue: 2
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param sms_otp_validity_duration_in_mins: The sms_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._sms_otp_validity_duration_in_mins = sms_otp_validity_duration_in_mins

    @property
    def jwt_validity_duration_in_secs(self):
        """
        **[Required]** Gets the jwt_validity_duration_in_secs of this AuthenticationFactorSettingsTotpSettings.
        The period of time (in seconds) that a JSON Web Token (JWT) is valid

        **SCIM++ Properties:**
         - idcsMaxValue: 99999
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The jwt_validity_duration_in_secs of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._jwt_validity_duration_in_secs

    @jwt_validity_duration_in_secs.setter
    def jwt_validity_duration_in_secs(self, jwt_validity_duration_in_secs):
        """
        Sets the jwt_validity_duration_in_secs of this AuthenticationFactorSettingsTotpSettings.
        The period of time (in seconds) that a JSON Web Token (JWT) is valid

        **SCIM++ Properties:**
         - idcsMaxValue: 99999
         - idcsMinValue: 30
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param jwt_validity_duration_in_secs: The jwt_validity_duration_in_secs of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._jwt_validity_duration_in_secs = jwt_validity_duration_in_secs

    @property
    def sms_passcode_length(self):
        """
        **[Required]** Gets the sms_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        Exact length of the Short Message Service (SMS) One-Time Passcode

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 4
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The sms_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._sms_passcode_length

    @sms_passcode_length.setter
    def sms_passcode_length(self, sms_passcode_length):
        """
        Sets the sms_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        Exact length of the Short Message Service (SMS) One-Time Passcode

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 4
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param sms_passcode_length: The sms_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._sms_passcode_length = sms_passcode_length

    @property
    def email_otp_validity_duration_in_mins(self):
        """
        **[Required]** Gets the email_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        The period of time (in minutes) that a one-time passcode remains valid that the system sends by email.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - idcsMaxValue: 60
         - idcsMinValue: 2
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The email_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._email_otp_validity_duration_in_mins

    @email_otp_validity_duration_in_mins.setter
    def email_otp_validity_duration_in_mins(self, email_otp_validity_duration_in_mins):
        """
        Sets the email_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        The period of time (in minutes) that a one-time passcode remains valid that the system sends by email.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - idcsMaxValue: 60
         - idcsMinValue: 2
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param email_otp_validity_duration_in_mins: The email_otp_validity_duration_in_mins of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._email_otp_validity_duration_in_mins = email_otp_validity_duration_in_mins

    @property
    def email_passcode_length(self):
        """
        **[Required]** Gets the email_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        Exact length of the email one-time passcode.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 4
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The email_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        :rtype: int
        """
        return self._email_passcode_length

    @email_passcode_length.setter
    def email_passcode_length(self, email_passcode_length):
        """
        Sets the email_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        Exact length of the email one-time passcode.

        **Added In:** 18.1.2

        **SCIM++ Properties:**
         - idcsMaxValue: 10
         - idcsMinValue: 4
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param email_passcode_length: The email_passcode_length of this AuthenticationFactorSettingsTotpSettings.
        :type: int
        """
        self._email_passcode_length = email_passcode_length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
