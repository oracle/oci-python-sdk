# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagedInstanceGroupDetails(object):
    """
    Detail information for creating a managed instance group
    """

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "LINUX"
    OS_FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "WINDOWS"
    OS_FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_family property of a CreateManagedInstanceGroupDetails.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateManagedInstanceGroupDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateManagedInstanceGroupDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagedInstanceGroupDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateManagedInstanceGroupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateManagedInstanceGroupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param os_family:
            The value to assign to the os_family property of this CreateManagedInstanceGroupDetails.
            Allowed values for this property are: "LINUX", "WINDOWS", "ALL"
        :type os_family: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'os_family': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'os_family': 'osFamily'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._os_family = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagedInstanceGroupDetails.
        Managed Instance Group identifier


        :return: The display_name of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagedInstanceGroupDetails.
        Managed Instance Group identifier


        :param display_name: The display_name of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateManagedInstanceGroupDetails.
        Information specified by the user about the managed instance group


        :return: The description of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagedInstanceGroupDetails.
        Information specified by the user about the managed instance group


        :param description: The description of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagedInstanceGroupDetails.
        OCID for the Compartment


        :return: The compartment_id of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagedInstanceGroupDetails.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateManagedInstanceGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateManagedInstanceGroupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateManagedInstanceGroupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateManagedInstanceGroupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateManagedInstanceGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateManagedInstanceGroupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateManagedInstanceGroupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateManagedInstanceGroupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def os_family(self):
        """
        Gets the os_family of this CreateManagedInstanceGroupDetails.
        The Operating System type of the managed instance(s) on which this scheduled job will operate.
        If not specified, this defaults to Linux.

        Allowed values for this property are: "LINUX", "WINDOWS", "ALL"


        :return: The os_family of this CreateManagedInstanceGroupDetails.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CreateManagedInstanceGroupDetails.
        The Operating System type of the managed instance(s) on which this scheduled job will operate.
        If not specified, this defaults to Linux.


        :param os_family: The os_family of this CreateManagedInstanceGroupDetails.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            raise ValueError(
                "Invalid value for `os_family`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._os_family = os_family

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
