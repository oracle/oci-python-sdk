# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class VnicAttachment(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'vnic_id': 'vnicId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._subnet_id = None
        self._time_created = None
        self._vnic_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this VnicAttachment.
        The Availability Domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this VnicAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VnicAttachment.
        The Availability Domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this VnicAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VnicAttachment.
        The OCID of the compartment.


        :return: The compartment_id of this VnicAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VnicAttachment.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this VnicAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VnicAttachment.
        A user-friendly name. Does not have to be unique.


        :return: The display_name of this VnicAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VnicAttachment.
        A user-friendly name. Does not have to be unique.


        :param display_name: The display_name of this VnicAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this VnicAttachment.
        The OCID of the VNIC attachment.


        :return: The id of this VnicAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VnicAttachment.
        The OCID of the VNIC attachment.


        :param id: The id of this VnicAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this VnicAttachment.
        The OCID of the instance.


        :return: The instance_id of this VnicAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this VnicAttachment.
        The OCID of the instance.


        :param instance_id: The instance_id of this VnicAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VnicAttachment.
        The current state of the VNIC attachment.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VnicAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VnicAttachment.
        The current state of the VNIC attachment.


        :param lifecycle_state: The lifecycle_state of this VnicAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this VnicAttachment.
        The OCID of the subnet of the VNIC.


        :return: The subnet_id of this VnicAttachment.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this VnicAttachment.
        The OCID of the subnet of the VNIC.


        :param subnet_id: The subnet_id of this VnicAttachment.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this VnicAttachment.
        The date and time the VNIC attachment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this VnicAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VnicAttachment.
        The date and time the VNIC attachment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this VnicAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this VnicAttachment.
        The OCID of the VNIC.


        :return: The vnic_id of this VnicAttachment.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this VnicAttachment.
        The OCID of the VNIC.


        :param vnic_id: The vnic_id of this VnicAttachment.
        :type: str
        """
        self._vnic_id = vnic_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
