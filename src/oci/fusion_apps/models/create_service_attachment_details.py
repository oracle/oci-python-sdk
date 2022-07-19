# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateServiceAttachmentDetails(object):
    """
    Information about the service attachment.
    """

    #: A constant which can be used with the action property of a CreateServiceAttachmentDetails.
    #: This constant has a value of "CREATE_NEW_INSTANCE"
    ACTION_CREATE_NEW_INSTANCE = "CREATE_NEW_INSTANCE"

    #: A constant which can be used with the action property of a CreateServiceAttachmentDetails.
    #: This constant has a value of "ATTACH_EXISTING_INSTANCE"
    ACTION_ATTACH_EXISTING_INSTANCE = "ATTACH_EXISTING_INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateServiceAttachmentDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fusion_apps.models.AttachExistingInstanceDetails`
        * :class:`~oci.fusion_apps.models.CreateNewInstanceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this CreateServiceAttachmentDetails.
            Allowed values for this property are: "CREATE_NEW_INSTANCE", "ATTACH_EXISTING_INSTANCE"
        :type action: str

        """
        self.swagger_types = {
            'action': 'str'
        }

        self.attribute_map = {
            'action': 'action'
        }

        self._action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['action']

        if type == 'ATTACH_EXISTING_INSTANCE':
            return 'AttachExistingInstanceDetails'

        if type == 'CREATE_NEW_INSTANCE':
            return 'CreateNewInstanceDetails'
        else:
            return 'CreateServiceAttachmentDetails'

    @property
    def action(self):
        """
        **[Required]** Gets the action of this CreateServiceAttachmentDetails.
        The operation type - the customer can ask FAaaS to create a new instance or use an existing instance

        Allowed values for this property are: "CREATE_NEW_INSTANCE", "ATTACH_EXISTING_INSTANCE"


        :return: The action of this CreateServiceAttachmentDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this CreateServiceAttachmentDetails.
        The operation type - the customer can ask FAaaS to create a new instance or use an existing instance


        :param action: The action of this CreateServiceAttachmentDetails.
        :type: str
        """
        allowed_values = ["CREATE_NEW_INSTANCE", "ATTACH_EXISTING_INSTANCE"]
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
