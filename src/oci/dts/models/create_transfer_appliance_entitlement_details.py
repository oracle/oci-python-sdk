# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTransferApplianceEntitlementDetails(object):
    """
    CreateTransferApplianceEntitlementDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTransferApplianceEntitlementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTransferApplianceEntitlementDetails.
        :type compartment_id: str

        :param requestor_name:
            The value to assign to the requestor_name property of this CreateTransferApplianceEntitlementDetails.
        :type requestor_name: str

        :param requestor_email:
            The value to assign to the requestor_email property of this CreateTransferApplianceEntitlementDetails.
        :type requestor_email: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'requestor_name': 'str',
            'requestor_email': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'requestor_name': 'requestorName',
            'requestor_email': 'requestorEmail'
        }

        self._compartment_id = None
        self._requestor_name = None
        self._requestor_email = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateTransferApplianceEntitlementDetails.

        :return: The compartment_id of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTransferApplianceEntitlementDetails.

        :param compartment_id: The compartment_id of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def requestor_name(self):
        """
        Gets the requestor_name of this CreateTransferApplianceEntitlementDetails.

        :return: The requestor_name of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._requestor_name

    @requestor_name.setter
    def requestor_name(self, requestor_name):
        """
        Sets the requestor_name of this CreateTransferApplianceEntitlementDetails.

        :param requestor_name: The requestor_name of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._requestor_name = requestor_name

    @property
    def requestor_email(self):
        """
        Gets the requestor_email of this CreateTransferApplianceEntitlementDetails.

        :return: The requestor_email of this CreateTransferApplianceEntitlementDetails.
        :rtype: str
        """
        return self._requestor_email

    @requestor_email.setter
    def requestor_email(self, requestor_email):
        """
        Sets the requestor_email of this CreateTransferApplianceEntitlementDetails.

        :param requestor_email: The requestor_email of this CreateTransferApplianceEntitlementDetails.
        :type: str
        """
        self._requestor_email = requestor_email

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
