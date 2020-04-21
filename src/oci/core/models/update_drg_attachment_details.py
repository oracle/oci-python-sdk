# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgAttachmentDetails(object):
    """
    UpdateDrgAttachmentDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDrgAttachmentDetails.
        :type display_name: str

        :param route_table_id:
            The value to assign to the route_table_id property of this UpdateDrgAttachmentDetails.
        :type route_table_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'route_table_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'route_table_id': 'routeTableId'
        }

        self._display_name = None
        self._route_table_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateDrgAttachmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDrgAttachmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this UpdateDrgAttachmentDetails.
        The OCID of the route table the DRG attachment will use.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this UpdateDrgAttachmentDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this UpdateDrgAttachmentDetails.
        The OCID of the route table the DRG attachment will use.

        For information about why you would associate a route table with a DRG attachment, see:

          * `Transit Routing: Access to Multiple VCNs in Same Region`__
          * `Transit Routing: Private Access to Oracle Services`__

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm
        __ https://docs.cloud.oracle.com/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this UpdateDrgAttachmentDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
