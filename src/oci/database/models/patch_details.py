# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchDetails(object):
    """
    The details about what actions to perform and using what patch to the specified target.
    This is part of an update request that is applied to a version field on the target such
    as DB system, Database Home, etc.
    """

    #: A constant which can be used with the action property of a PatchDetails.
    #: This constant has a value of "APPLY"
    ACTION_APPLY = "APPLY"

    #: A constant which can be used with the action property of a PatchDetails.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param patch_id:
            The value to assign to the patch_id property of this PatchDetails.
        :type patch_id: str

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this PatchDetails.
        :type database_software_image_id: str

        :param action:
            The value to assign to the action property of this PatchDetails.
            Allowed values for this property are: "APPLY", "PRECHECK"
        :type action: str

        """
        self.swagger_types = {
            'patch_id': 'str',
            'database_software_image_id': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'patch_id': 'patchId',
            'database_software_image_id': 'databaseSoftwareImageId',
            'action': 'action'
        }

        self._patch_id = None
        self._database_software_image_id = None
        self._action = None

    @property
    def patch_id(self):
        """
        Gets the patch_id of this PatchDetails.
        The `OCID`__ of the patch.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The patch_id of this PatchDetails.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this PatchDetails.
        The `OCID`__ of the patch.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param patch_id: The patch_id of this PatchDetails.
        :type: str
        """
        self._patch_id = patch_id

    @property
    def database_software_image_id(self):
        """
        Gets the database_software_image_id of this PatchDetails.
        The `OCID`__ of the database software image.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_software_image_id of this PatchDetails.
        :rtype: str
        """
        return self._database_software_image_id

    @database_software_image_id.setter
    def database_software_image_id(self, database_software_image_id):
        """
        Sets the database_software_image_id of this PatchDetails.
        The `OCID`__ of the database software image.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_software_image_id: The database_software_image_id of this PatchDetails.
        :type: str
        """
        self._database_software_image_id = database_software_image_id

    @property
    def action(self):
        """
        Gets the action of this PatchDetails.
        The action to perform on the patch.

        Allowed values for this property are: "APPLY", "PRECHECK"


        :return: The action of this PatchDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PatchDetails.
        The action to perform on the patch.


        :param action: The action of this PatchDetails.
        :type: str
        """
        allowed_values = ["APPLY", "PRECHECK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
