# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MountTarget(object):
    """
    Provides access to a collection of file systems through one or more VNICs on a
    specified subnet. The set of file systems is controlled through the
    referenced export set.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a MountTarget.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MountTarget.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MountTarget.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MountTarget.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MountTarget.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MountTarget object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this MountTarget.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MountTarget.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MountTarget.
        :type display_name: str

        :param export_set_id:
            The value to assign to the export_set_id property of this MountTarget.
        :type export_set_id: str

        :param id:
            The value to assign to the id property of this MountTarget.
        :type id: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MountTarget.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MountTarget.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param private_ip_ids:
            The value to assign to the private_ip_ids property of this MountTarget.
        :type private_ip_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this MountTarget.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this MountTarget.
        :type nsg_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this MountTarget.
        :type time_created: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MountTarget.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MountTarget.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'export_set_id': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'private_ip_ids': 'list[str]',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'time_created': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'export_set_id': 'exportSetId',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'private_ip_ids': 'privateIpIds',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'time_created': 'timeCreated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._export_set_id = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._private_ip_ids = None
        self._subnet_id = None
        self._nsg_ids = None
        self._time_created = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this MountTarget.
        The availability domain the mount target is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this MountTarget.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this MountTarget.
        The availability domain the mount target is in. May be unset
        as a blank or NULL value.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this MountTarget.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MountTarget.
        The `OCID`__ of the compartment that contains the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MountTarget.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MountTarget.
        The `OCID`__ of the compartment that contains the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MountTarget.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MountTarget.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :return: The display_name of this MountTarget.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MountTarget.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :param display_name: The display_name of this MountTarget.
        :type: str
        """
        self._display_name = display_name

    @property
    def export_set_id(self):
        """
        Gets the export_set_id of this MountTarget.
        The `OCID`__ of the associated export set. Controls what file
        systems will be exported through Network File System (NFS) protocol on this
        mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The export_set_id of this MountTarget.
        :rtype: str
        """
        return self._export_set_id

    @export_set_id.setter
    def export_set_id(self, export_set_id):
        """
        Sets the export_set_id of this MountTarget.
        The `OCID`__ of the associated export set. Controls what file
        systems will be exported through Network File System (NFS) protocol on this
        mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param export_set_id: The export_set_id of this MountTarget.
        :type: str
        """
        self._export_set_id = export_set_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MountTarget.
        The `OCID`__ of the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MountTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MountTarget.
        The `OCID`__ of the mount target.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MountTarget.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this MountTarget.
        Additional information about the current 'lifecycleState'.


        :return: The lifecycle_details of this MountTarget.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MountTarget.
        Additional information about the current 'lifecycleState'.


        :param lifecycle_details: The lifecycle_details of this MountTarget.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MountTarget.
        The current state of the mount target.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MountTarget.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MountTarget.
        The current state of the mount target.


        :param lifecycle_state: The lifecycle_state of this MountTarget.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def private_ip_ids(self):
        """
        **[Required]** Gets the private_ip_ids of this MountTarget.
        The OCIDs of the private IP addresses associated with this mount target.


        :return: The private_ip_ids of this MountTarget.
        :rtype: list[str]
        """
        return self._private_ip_ids

    @private_ip_ids.setter
    def private_ip_ids(self, private_ip_ids):
        """
        Sets the private_ip_ids of this MountTarget.
        The OCIDs of the private IP addresses associated with this mount target.


        :param private_ip_ids: The private_ip_ids of this MountTarget.
        :type: list[str]
        """
        self._private_ip_ids = private_ip_ids

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this MountTarget.
        The `OCID`__ of the subnet the mount target is in.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this MountTarget.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this MountTarget.
        The `OCID`__ of the subnet the mount target is in.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this MountTarget.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this MountTarget.
        A list of Network Security Group `OCIDs`__ associated with this mount target.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the mount target from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this MountTarget.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this MountTarget.
        A list of Network Security Group `OCIDs`__ associated with this mount target.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the mount target from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this MountTarget.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MountTarget.
        The date and time the mount target was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this MountTarget.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MountTarget.
        The date and time the mount target was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this MountTarget.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MountTarget.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this MountTarget.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MountTarget.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this MountTarget.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MountTarget.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this MountTarget.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MountTarget.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this MountTarget.
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
