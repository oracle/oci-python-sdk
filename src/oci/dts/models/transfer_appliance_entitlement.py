# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferApplianceEntitlement(object):
    """
    TransferApplianceEntitlement model.
    """

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "REQUESTED"
    STATUS_REQUESTED = "REQUESTED"

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "PENDING_SIGNING"
    STATUS_PENDING_SIGNING = "PENDING_SIGNING"

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "PENDING_APPROVAL"
    STATUS_PENDING_APPROVAL = "PENDING_APPROVAL"

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "TERMS_EXPIRED"
    STATUS_TERMS_EXPIRED = "TERMS_EXPIRED"

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "APPROVED"
    STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "REJECTED"
    STATUS_REJECTED = "REJECTED"

    #: A constant which can be used with the status property of a TransferApplianceEntitlement.
    #: This constant has a value of "CANCELLED"
    STATUS_CANCELLED = "CANCELLED"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferApplianceEntitlement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this TransferApplianceEntitlement.
        :type tenant_id: str

        :param requestor_name:
            The value to assign to the requestor_name property of this TransferApplianceEntitlement.
        :type requestor_name: str

        :param requestor_email:
            The value to assign to the requestor_email property of this TransferApplianceEntitlement.
        :type requestor_email: str

        :param status:
            The value to assign to the status property of this TransferApplianceEntitlement.
            Allowed values for this property are: "REQUESTED", "PENDING_SIGNING", "PENDING_APPROVAL", "TERMS_EXPIRED", "APPROVED", "REJECTED", "CANCELLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferApplianceEntitlement.
        :type creation_time: datetime

        :param update_time:
            The value to assign to the update_time property of this TransferApplianceEntitlement.
        :type update_time: datetime

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'requestor_name': 'str',
            'requestor_email': 'str',
            'status': 'str',
            'creation_time': 'datetime',
            'update_time': 'datetime'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'requestor_name': 'requestorName',
            'requestor_email': 'requestorEmail',
            'status': 'status',
            'creation_time': 'creationTime',
            'update_time': 'updateTime'
        }

        self._tenant_id = None
        self._requestor_name = None
        self._requestor_email = None
        self._status = None
        self._creation_time = None
        self._update_time = None

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this TransferApplianceEntitlement.

        :return: The tenant_id of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this TransferApplianceEntitlement.

        :param tenant_id: The tenant_id of this TransferApplianceEntitlement.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def requestor_name(self):
        """
        Gets the requestor_name of this TransferApplianceEntitlement.

        :return: The requestor_name of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._requestor_name

    @requestor_name.setter
    def requestor_name(self, requestor_name):
        """
        Sets the requestor_name of this TransferApplianceEntitlement.

        :param requestor_name: The requestor_name of this TransferApplianceEntitlement.
        :type: str
        """
        self._requestor_name = requestor_name

    @property
    def requestor_email(self):
        """
        Gets the requestor_email of this TransferApplianceEntitlement.

        :return: The requestor_email of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._requestor_email

    @requestor_email.setter
    def requestor_email(self, requestor_email):
        """
        Sets the requestor_email of this TransferApplianceEntitlement.

        :param requestor_email: The requestor_email of this TransferApplianceEntitlement.
        :type: str
        """
        self._requestor_email = requestor_email

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TransferApplianceEntitlement.
        Allowed values for this property are: "REQUESTED", "PENDING_SIGNING", "PENDING_APPROVAL", "TERMS_EXPIRED", "APPROVED", "REJECTED", "CANCELLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TransferApplianceEntitlement.

        :param status: The status of this TransferApplianceEntitlement.
        :type: str
        """
        allowed_values = ["REQUESTED", "PENDING_SIGNING", "PENDING_APPROVAL", "TERMS_EXPIRED", "APPROVED", "REJECTED", "CANCELLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferApplianceEntitlement.

        :return: The creation_time of this TransferApplianceEntitlement.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferApplianceEntitlement.

        :param creation_time: The creation_time of this TransferApplianceEntitlement.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def update_time(self):
        """
        Gets the update_time of this TransferApplianceEntitlement.

        :return: The update_time of this TransferApplianceEntitlement.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this TransferApplianceEntitlement.

        :param update_time: The update_time of this TransferApplianceEntitlement.
        :type: datetime
        """
        self._update_time = update_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
