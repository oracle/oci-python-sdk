# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdcsInfoDetails(object):
    """
    Information for IDCS access
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdcsInfoDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idcs_app_location_url:
            The value to assign to the idcs_app_location_url property of this IdcsInfoDetails.
        :type idcs_app_location_url: str

        :param idcs_app_display_name:
            The value to assign to the idcs_app_display_name property of this IdcsInfoDetails.
        :type idcs_app_display_name: str

        :param idcs_app_id:
            The value to assign to the idcs_app_id property of this IdcsInfoDetails.
        :type idcs_app_id: str

        :param idcs_app_name:
            The value to assign to the idcs_app_name property of this IdcsInfoDetails.
        :type idcs_app_name: str

        :param instance_primary_audience_url:
            The value to assign to the instance_primary_audience_url property of this IdcsInfoDetails.
        :type instance_primary_audience_url: str

        """
        self.swagger_types = {
            'idcs_app_location_url': 'str',
            'idcs_app_display_name': 'str',
            'idcs_app_id': 'str',
            'idcs_app_name': 'str',
            'instance_primary_audience_url': 'str'
        }

        self.attribute_map = {
            'idcs_app_location_url': 'idcsAppLocationUrl',
            'idcs_app_display_name': 'idcsAppDisplayName',
            'idcs_app_id': 'idcsAppId',
            'idcs_app_name': 'idcsAppName',
            'instance_primary_audience_url': 'instancePrimaryAudienceUrl'
        }

        self._idcs_app_location_url = None
        self._idcs_app_display_name = None
        self._idcs_app_id = None
        self._idcs_app_name = None
        self._instance_primary_audience_url = None

    @property
    def idcs_app_location_url(self):
        """
        **[Required]** Gets the idcs_app_location_url of this IdcsInfoDetails.
        URL for the location of the IDCS Application (used by IDCS APIs)


        :return: The idcs_app_location_url of this IdcsInfoDetails.
        :rtype: str
        """
        return self._idcs_app_location_url

    @idcs_app_location_url.setter
    def idcs_app_location_url(self, idcs_app_location_url):
        """
        Sets the idcs_app_location_url of this IdcsInfoDetails.
        URL for the location of the IDCS Application (used by IDCS APIs)


        :param idcs_app_location_url: The idcs_app_location_url of this IdcsInfoDetails.
        :type: str
        """
        self._idcs_app_location_url = idcs_app_location_url

    @property
    def idcs_app_display_name(self):
        """
        **[Required]** Gets the idcs_app_display_name of this IdcsInfoDetails.
        The IDCS application display name associated with the instance


        :return: The idcs_app_display_name of this IdcsInfoDetails.
        :rtype: str
        """
        return self._idcs_app_display_name

    @idcs_app_display_name.setter
    def idcs_app_display_name(self, idcs_app_display_name):
        """
        Sets the idcs_app_display_name of this IdcsInfoDetails.
        The IDCS application display name associated with the instance


        :param idcs_app_display_name: The idcs_app_display_name of this IdcsInfoDetails.
        :type: str
        """
        self._idcs_app_display_name = idcs_app_display_name

    @property
    def idcs_app_id(self):
        """
        **[Required]** Gets the idcs_app_id of this IdcsInfoDetails.
        The IDCS application ID associated with the instance


        :return: The idcs_app_id of this IdcsInfoDetails.
        :rtype: str
        """
        return self._idcs_app_id

    @idcs_app_id.setter
    def idcs_app_id(self, idcs_app_id):
        """
        Sets the idcs_app_id of this IdcsInfoDetails.
        The IDCS application ID associated with the instance


        :param idcs_app_id: The idcs_app_id of this IdcsInfoDetails.
        :type: str
        """
        self._idcs_app_id = idcs_app_id

    @property
    def idcs_app_name(self):
        """
        **[Required]** Gets the idcs_app_name of this IdcsInfoDetails.
        The IDCS application name associated with the instance


        :return: The idcs_app_name of this IdcsInfoDetails.
        :rtype: str
        """
        return self._idcs_app_name

    @idcs_app_name.setter
    def idcs_app_name(self, idcs_app_name):
        """
        Sets the idcs_app_name of this IdcsInfoDetails.
        The IDCS application name associated with the instance


        :param idcs_app_name: The idcs_app_name of this IdcsInfoDetails.
        :type: str
        """
        self._idcs_app_name = idcs_app_name

    @property
    def instance_primary_audience_url(self):
        """
        **[Required]** Gets the instance_primary_audience_url of this IdcsInfoDetails.
        The URL used as the primary audience for visual builder flows in this instance
        type: string


        :return: The instance_primary_audience_url of this IdcsInfoDetails.
        :rtype: str
        """
        return self._instance_primary_audience_url

    @instance_primary_audience_url.setter
    def instance_primary_audience_url(self, instance_primary_audience_url):
        """
        Sets the instance_primary_audience_url of this IdcsInfoDetails.
        The URL used as the primary audience for visual builder flows in this instance
        type: string


        :param instance_primary_audience_url: The instance_primary_audience_url of this IdcsInfoDetails.
        :type: str
        """
        self._instance_primary_audience_url = instance_primary_audience_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
