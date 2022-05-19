# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateModuleStreamDetails(object):
    """
    Information detailing the state of a module stream
    """

    #: A constant which can be used with the status property of a UpdateModuleStreamDetails.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a UpdateModuleStreamDetails.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a UpdateModuleStreamDetails.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateModuleStreamDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stream_name:
            The value to assign to the stream_name property of this UpdateModuleStreamDetails.
        :type stream_name: str

        :param status:
            The value to assign to the status property of this UpdateModuleStreamDetails.
            Allowed values for this property are: "ENABLED", "DISABLED", "ACTIVE"
        :type status: str

        :param time_modified:
            The value to assign to the time_modified property of this UpdateModuleStreamDetails.
        :type time_modified: datetime

        :param software_source_name:
            The value to assign to the software_source_name property of this UpdateModuleStreamDetails.
        :type software_source_name: str

        :param software_source_url:
            The value to assign to the software_source_url property of this UpdateModuleStreamDetails.
        :type software_source_url: str

        :param is_default:
            The value to assign to the is_default property of this UpdateModuleStreamDetails.
        :type is_default: bool

        :param profiles:
            The value to assign to the profiles property of this UpdateModuleStreamDetails.
        :type profiles: list[oci.os_management.models.UpdateModuleStreamProfileDetails]

        """
        self.swagger_types = {
            'stream_name': 'str',
            'status': 'str',
            'time_modified': 'datetime',
            'software_source_name': 'str',
            'software_source_url': 'str',
            'is_default': 'bool',
            'profiles': 'list[UpdateModuleStreamProfileDetails]'
        }

        self.attribute_map = {
            'stream_name': 'streamName',
            'status': 'status',
            'time_modified': 'timeModified',
            'software_source_name': 'softwareSourceName',
            'software_source_url': 'softwareSourceUrl',
            'is_default': 'isDefault',
            'profiles': 'profiles'
        }

        self._stream_name = None
        self._status = None
        self._time_modified = None
        self._software_source_name = None
        self._software_source_url = None
        self._is_default = None
        self._profiles = None

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this UpdateModuleStreamDetails.
        The name of the stream of the parent module


        :return: The stream_name of this UpdateModuleStreamDetails.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this UpdateModuleStreamDetails.
        The name of the stream of the parent module


        :param stream_name: The stream_name of this UpdateModuleStreamDetails.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateModuleStreamDetails.
        The status of the stream

        A stream with the \"ENABLED\" status can be used as a source for installing
        profiles.  Streams with this status are also \"ACTIVE\".

        A stream with the \"DISABLED\" status cannot be the source for installing
        profiles.  To install profiles and packages from this stream, it must be
        enabled.

        A stream with the \"ACTIVE\" status can be used as a source for installing
        profiles.  The packages that comprise the stream are also used when a
        matching package is installed directly.  In general, a stream can have
        this status if it is the default stream for the module and no stream has
        been explicitly enabled.

        Allowed values for this property are: "ENABLED", "DISABLED", "ACTIVE"


        :return: The status of this UpdateModuleStreamDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateModuleStreamDetails.
        The status of the stream

        A stream with the \"ENABLED\" status can be used as a source for installing
        profiles.  Streams with this status are also \"ACTIVE\".

        A stream with the \"DISABLED\" status cannot be the source for installing
        profiles.  To install profiles and packages from this stream, it must be
        enabled.

        A stream with the \"ACTIVE\" status can be used as a source for installing
        profiles.  The packages that comprise the stream are also used when a
        matching package is installed directly.  In general, a stream can have
        this status if it is the default stream for the module and no stream has
        been explicitly enabled.


        :param status: The status of this UpdateModuleStreamDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "ACTIVE"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def time_modified(self):
        """
        **[Required]** Gets the time_modified of this UpdateModuleStreamDetails.
        The date and time of the last status change for this object, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_modified of this UpdateModuleStreamDetails.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this UpdateModuleStreamDetails.
        The date and time of the last status change for this object, as
        described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_modified: The time_modified of this UpdateModuleStreamDetails.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def software_source_name(self):
        """
        Gets the software_source_name of this UpdateModuleStreamDetails.
        The name of the software source that publishes this stream.


        :return: The software_source_name of this UpdateModuleStreamDetails.
        :rtype: str
        """
        return self._software_source_name

    @software_source_name.setter
    def software_source_name(self, software_source_name):
        """
        Sets the software_source_name of this UpdateModuleStreamDetails.
        The name of the software source that publishes this stream.


        :param software_source_name: The software_source_name of this UpdateModuleStreamDetails.
        :type: str
        """
        self._software_source_name = software_source_name

    @property
    def software_source_url(self):
        """
        Gets the software_source_url of this UpdateModuleStreamDetails.
        The URL of the software source that publishes this stream.


        :return: The software_source_url of this UpdateModuleStreamDetails.
        :rtype: str
        """
        return self._software_source_url

    @software_source_url.setter
    def software_source_url(self, software_source_url):
        """
        Sets the software_source_url of this UpdateModuleStreamDetails.
        The URL of the software source that publishes this stream.


        :param software_source_url: The software_source_url of this UpdateModuleStreamDetails.
        :type: str
        """
        self._software_source_url = software_source_url

    @property
    def is_default(self):
        """
        Gets the is_default of this UpdateModuleStreamDetails.
        Indicates if the module stream is the default


        :return: The is_default of this UpdateModuleStreamDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this UpdateModuleStreamDetails.
        Indicates if the module stream is the default


        :param is_default: The is_default of this UpdateModuleStreamDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def profiles(self):
        """
        Gets the profiles of this UpdateModuleStreamDetails.
        The profiles of the stream


        :return: The profiles of this UpdateModuleStreamDetails.
        :rtype: list[oci.os_management.models.UpdateModuleStreamProfileDetails]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this UpdateModuleStreamDetails.
        The profiles of the stream


        :param profiles: The profiles of this UpdateModuleStreamDetails.
        :type: list[oci.os_management.models.UpdateModuleStreamProfileDetails]
        """
        self._profiles = profiles

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
