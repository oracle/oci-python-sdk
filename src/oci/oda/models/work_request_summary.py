# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    A description of the work request's status.
    """

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_ODA_INSTANCE"
    REQUEST_ACTION_CREATE_ODA_INSTANCE = "CREATE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "UPGRADE_ODA_INSTANCE"
    REQUEST_ACTION_UPGRADE_ODA_INSTANCE = "UPGRADE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_ODA_INSTANCE"
    REQUEST_ACTION_DELETE_ODA_INSTANCE = "DELETE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "PURGE_ODA_INSTANCE"
    REQUEST_ACTION_PURGE_ODA_INSTANCE = "PURGE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "RECOVER_ODA_INSTANCE"
    REQUEST_ACTION_RECOVER_ODA_INSTANCE = "RECOVER_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "STOP_ODA_INSTANCE"
    REQUEST_ACTION_STOP_ODA_INSTANCE = "STOP_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "START_ODA_INSTANCE"
    REQUEST_ACTION_START_ODA_INSTANCE = "START_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_ODA_INSTANCE_COMPARTMENT"
    REQUEST_ACTION_CHANGE_ODA_INSTANCE_COMPARTMENT = "CHANGE_ODA_INSTANCE_COMPARTMENT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CHANGE_CUST_ENC_KEY"
    REQUEST_ACTION_CHANGE_CUST_ENC_KEY = "CHANGE_CUST_ENC_KEY"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "DEACT_CUST_ENC_KEY"
    REQUEST_ACTION_DEACT_CUST_ENC_KEY = "DEACT_CUST_ENC_KEY"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_ASSOCIATION"
    REQUEST_ACTION_CREATE_ASSOCIATION = "CREATE_ASSOCIATION"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_ASSOCIATION"
    REQUEST_ACTION_DELETE_ASSOCIATION = "DELETE_ASSOCIATION"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ENTITLEMENTS_FOR_CACCT"
    REQUEST_ACTION_UPDATE_ENTITLEMENTS_FOR_CACCT = "UPDATE_ENTITLEMENTS_FOR_CACCT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "LOOKUP_ODA_INSTANCES_FOR_CACCT"
    REQUEST_ACTION_LOOKUP_ODA_INSTANCES_FOR_CACCT = "LOOKUP_ODA_INSTANCES_FOR_CACCT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_ODA_INSTANCE_ATTACHMENT"
    REQUEST_ACTION_CREATE_ODA_INSTANCE_ATTACHMENT = "CREATE_ODA_INSTANCE_ATTACHMENT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_ODA_INSTANCE_ATTACHMENT"
    REQUEST_ACTION_UPDATE_ODA_INSTANCE_ATTACHMENT = "UPDATE_ODA_INSTANCE_ATTACHMENT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_ODA_INSTANCE_ATTACHMENT"
    REQUEST_ACTION_DELETE_ODA_INSTANCE_ATTACHMENT = "DELETE_ODA_INSTANCE_ATTACHMENT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_IMPORTED_PACKAGE"
    REQUEST_ACTION_CREATE_IMPORTED_PACKAGE = "CREATE_IMPORTED_PACKAGE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "UPDATE_IMPORTED_PACKAGE"
    REQUEST_ACTION_UPDATE_IMPORTED_PACKAGE = "UPDATE_IMPORTED_PACKAGE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_IMPORTED_PACKAGE"
    REQUEST_ACTION_DELETE_IMPORTED_PACKAGE = "DELETE_IMPORTED_PACKAGE"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "IMPORT_BOT"
    REQUEST_ACTION_IMPORT_BOT = "IMPORT_BOT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_SKILL"
    REQUEST_ACTION_CREATE_SKILL = "CREATE_SKILL"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CLONE_SKILL"
    REQUEST_ACTION_CLONE_SKILL = "CLONE_SKILL"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "EXTEND_SKILL"
    REQUEST_ACTION_EXTEND_SKILL = "EXTEND_SKILL"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "VERSION_SKILL"
    REQUEST_ACTION_VERSION_SKILL = "VERSION_SKILL"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "EXPORT_SKILL"
    REQUEST_ACTION_EXPORT_SKILL = "EXPORT_SKILL"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CREATE_DIGITAL_ASSISTANT"
    REQUEST_ACTION_CREATE_DIGITAL_ASSISTANT = "CREATE_DIGITAL_ASSISTANT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "CLONE_DIGITAL_ASSISTANT"
    REQUEST_ACTION_CLONE_DIGITAL_ASSISTANT = "CLONE_DIGITAL_ASSISTANT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "EXTEND_DIGITAL_ASSISTANT"
    REQUEST_ACTION_EXTEND_DIGITAL_ASSISTANT = "EXTEND_DIGITAL_ASSISTANT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "VERSION_DIGITAL_ASSISTANT"
    REQUEST_ACTION_VERSION_DIGITAL_ASSISTANT = "VERSION_DIGITAL_ASSISTANT"

    #: A constant which can be used with the request_action property of a WorkRequestSummary.
    #: This constant has a value of "EXPORT_DIGITAL_ASSISTANT"
    REQUEST_ACTION_EXPORT_DIGITAL_ASSISTANT = "EXPORT_DIGITAL_ASSISTANT"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param oda_instance_id:
            The value to assign to the oda_instance_id property of this WorkRequestSummary.
        :type oda_instance_id: str

        :param request_action:
            The value to assign to the request_action property of this WorkRequestSummary.
            Allowed values for this property are: "CREATE_ODA_INSTANCE", "UPGRADE_ODA_INSTANCE", "DELETE_ODA_INSTANCE", "PURGE_ODA_INSTANCE", "RECOVER_ODA_INSTANCE", "STOP_ODA_INSTANCE", "START_ODA_INSTANCE", "CHANGE_ODA_INSTANCE_COMPARTMENT", "CHANGE_CUST_ENC_KEY", "DEACT_CUST_ENC_KEY", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", "LOOKUP_ODA_INSTANCES_FOR_CACCT", "CREATE_ODA_INSTANCE_ATTACHMENT", "UPDATE_ODA_INSTANCE_ATTACHMENT", "DELETE_ODA_INSTANCE_ATTACHMENT", "CREATE_IMPORTED_PACKAGE", "UPDATE_IMPORTED_PACKAGE", "DELETE_IMPORTED_PACKAGE", "IMPORT_BOT", "CREATE_SKILL", "CLONE_SKILL", "EXTEND_SKILL", "VERSION_SKILL", "EXPORT_SKILL", "CREATE_DIGITAL_ASSISTANT", "CLONE_DIGITAL_ASSISTANT", "EXTEND_DIGITAL_ASSISTANT", "VERSION_DIGITAL_ASSISTANT", "EXPORT_DIGITAL_ASSISTANT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_action: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[oci.oda.models.WorkRequestResource]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'oda_instance_id': 'str',
            'request_action': 'str',
            'status': 'str',
            'resources': 'list[WorkRequestResource]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'oda_instance_id': 'odaInstanceId',
            'request_action': 'requestAction',
            'status': 'status',
            'resources': 'resources'
        }

        self._id = None
        self._compartment_id = None
        self._oda_instance_id = None
        self._request_action = None
        self._status = None
        self._resources = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The identifier of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The identifier of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequestSummary.
        The identifier of the compartment that contains the work request.


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The identifier of the compartment that contains the work request.


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def oda_instance_id(self):
        """
        **[Required]** Gets the oda_instance_id of this WorkRequestSummary.
        The identifier of the Digital Assistant instance to which this work request pertains.


        :return: The oda_instance_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._oda_instance_id

    @oda_instance_id.setter
    def oda_instance_id(self, oda_instance_id):
        """
        Sets the oda_instance_id of this WorkRequestSummary.
        The identifier of the Digital Assistant instance to which this work request pertains.


        :param oda_instance_id: The oda_instance_id of this WorkRequestSummary.
        :type: str
        """
        self._oda_instance_id = oda_instance_id

    @property
    def request_action(self):
        """
        **[Required]** Gets the request_action of this WorkRequestSummary.
        The type of the operation that's associated with the work request.

        Allowed values for this property are: "CREATE_ODA_INSTANCE", "UPGRADE_ODA_INSTANCE", "DELETE_ODA_INSTANCE", "PURGE_ODA_INSTANCE", "RECOVER_ODA_INSTANCE", "STOP_ODA_INSTANCE", "START_ODA_INSTANCE", "CHANGE_ODA_INSTANCE_COMPARTMENT", "CHANGE_CUST_ENC_KEY", "DEACT_CUST_ENC_KEY", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", "LOOKUP_ODA_INSTANCES_FOR_CACCT", "CREATE_ODA_INSTANCE_ATTACHMENT", "UPDATE_ODA_INSTANCE_ATTACHMENT", "DELETE_ODA_INSTANCE_ATTACHMENT", "CREATE_IMPORTED_PACKAGE", "UPDATE_IMPORTED_PACKAGE", "DELETE_IMPORTED_PACKAGE", "IMPORT_BOT", "CREATE_SKILL", "CLONE_SKILL", "EXTEND_SKILL", "VERSION_SKILL", "EXPORT_SKILL", "CREATE_DIGITAL_ASSISTANT", "CLONE_DIGITAL_ASSISTANT", "EXTEND_DIGITAL_ASSISTANT", "VERSION_DIGITAL_ASSISTANT", "EXPORT_DIGITAL_ASSISTANT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_action of this WorkRequestSummary.
        :rtype: str
        """
        return self._request_action

    @request_action.setter
    def request_action(self, request_action):
        """
        Sets the request_action of this WorkRequestSummary.
        The type of the operation that's associated with the work request.


        :param request_action: The request_action of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["CREATE_ODA_INSTANCE", "UPGRADE_ODA_INSTANCE", "DELETE_ODA_INSTANCE", "PURGE_ODA_INSTANCE", "RECOVER_ODA_INSTANCE", "STOP_ODA_INSTANCE", "START_ODA_INSTANCE", "CHANGE_ODA_INSTANCE_COMPARTMENT", "CHANGE_CUST_ENC_KEY", "DEACT_CUST_ENC_KEY", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", "LOOKUP_ODA_INSTANCES_FOR_CACCT", "CREATE_ODA_INSTANCE_ATTACHMENT", "UPDATE_ODA_INSTANCE_ATTACHMENT", "DELETE_ODA_INSTANCE_ATTACHMENT", "CREATE_IMPORTED_PACKAGE", "UPDATE_IMPORTED_PACKAGE", "DELETE_IMPORTED_PACKAGE", "IMPORT_BOT", "CREATE_SKILL", "CLONE_SKILL", "EXTEND_SKILL", "VERSION_SKILL", "EXPORT_SKILL", "CREATE_DIGITAL_ASSISTANT", "CLONE_DIGITAL_ASSISTANT", "EXTEND_DIGITAL_ASSISTANT", "VERSION_DIGITAL_ASSISTANT", "EXPORT_DIGITAL_ASSISTANT"]
        if not value_allowed_none_or_none_sentinel(request_action, allowed_values):
            request_action = 'UNKNOWN_ENUM_VALUE'
        self._request_action = request_action

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        The status of current work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        The status of current work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequestSummary.
        The resources that this work request affects.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[oci.oda.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources that this work request affects.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[oci.oda.models.WorkRequestResource]
        """
        self._resources = resources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
