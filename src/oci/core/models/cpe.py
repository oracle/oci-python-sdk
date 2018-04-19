# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Cpe(object):
    """
    An object you create when setting up an IPSec VPN between your on-premises network
    and VCN. The `Cpe` is a virtual representation of your Customer-Premises Equipment,
    which is the actual router on-premises at your site at your end of the IPSec VPN connection.
    For more information,
    see `Overview of the Networking Service`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/overview.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Cpe object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Cpe.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this Cpe.
        :type display_name: str

        :param id:
            The value to assign to the id property of this Cpe.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this Cpe.
        :type ip_address: str

        :param time_created:
            The value to assign to the time_created property of this Cpe.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'ip_address': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'ip_address': 'ipAddress',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._ip_address = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Cpe.
        The OCID of the compartment containing the CPE.


        :return: The compartment_id of this Cpe.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Cpe.
        The OCID of the compartment containing the CPE.


        :param compartment_id: The compartment_id of this Cpe.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Cpe.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this Cpe.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Cpe.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this Cpe.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Cpe.
        The CPE's Oracle ID (OCID).


        :return: The id of this Cpe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cpe.
        The CPE's Oracle ID (OCID).


        :param id: The id of this Cpe.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this Cpe.
        The public IP address of the on-premises router.


        :return: The ip_address of this Cpe.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Cpe.
        The public IP address of the on-premises router.


        :param ip_address: The ip_address of this Cpe.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def time_created(self):
        """
        Gets the time_created of this Cpe.
        The date and time the CPE was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Cpe.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Cpe.
        The date and time the CPE was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Cpe.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
