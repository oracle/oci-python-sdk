# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSnapshotDetails(object):
    """
    Details for creating the snapshot.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSnapshotDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_system_id:
            The value to assign to the file_system_id property of this CreateSnapshotDetails.
        :type file_system_id: str

        :param name:
            The value to assign to the name property of this CreateSnapshotDetails.
        :type name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSnapshotDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSnapshotDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'file_system_id': 'str',
            'name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'file_system_id': 'fileSystemId',
            'name': 'name',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._file_system_id = None
        self._name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this CreateSnapshotDetails.
        The OCID of the file system to take a snapshot of.


        :return: The file_system_id of this CreateSnapshotDetails.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this CreateSnapshotDetails.
        The OCID of the file system to take a snapshot of.


        :param file_system_id: The file_system_id of this CreateSnapshotDetails.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateSnapshotDetails.
        Name of the snapshot. This value is immutable. It must also be unique with respect
        to all other non-DELETED snapshots on the associated file
        system.

        Avoid entering confidential information.

        Example: `Sunday`


        :return: The name of this CreateSnapshotDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateSnapshotDetails.
        Name of the snapshot. This value is immutable. It must also be unique with respect
        to all other non-DELETED snapshots on the associated file
        system.

        Avoid entering confidential information.

        Example: `Sunday`


        :param name: The name of this CreateSnapshotDetails.
        :type: str
        """
        self._name = name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSnapshotDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSnapshotDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSnapshotDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSnapshotDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSnapshotDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSnapshotDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSnapshotDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSnapshotDetails.
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
