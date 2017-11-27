# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new PatchDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this PatchDetails.
            Allowed values for this property are: "APPLY", "PRECHECK"
        :type action: str

        :param patch_id:
            The value to assign to the patch_id property of this PatchDetails.
        :type patch_id: str

        """
        self.swagger_types = {
            'action': 'str',
            'patch_id': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'patch_id': 'patchId'
        }

        self._action = None
        self._patch_id = None

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
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action`, must be one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def patch_id(self):
        """
        Gets the patch_id of this PatchDetails.
        The OCID of the patch.


        :return: The patch_id of this PatchDetails.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this PatchDetails.
        The OCID of the patch.


        :param patch_id: The patch_id of this PatchDetails.
        :type: str
        """
        self._patch_id = patch_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
