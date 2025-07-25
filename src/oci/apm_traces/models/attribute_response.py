# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttributeResponse(object):
    """
    Response of an individual attribute item in the bulk activate or deactivate operation.
    """

    #: A constant which can be used with the attribute_type property of a AttributeResponse.
    #: This constant has a value of "NUMERIC"
    ATTRIBUTE_TYPE_NUMERIC = "NUMERIC"

    #: A constant which can be used with the attribute_type property of a AttributeResponse.
    #: This constant has a value of "STRING"
    ATTRIBUTE_TYPE_STRING = "STRING"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "NONE"
    UNIT_NONE = "NONE"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "EPOCH_TIME_MS"
    UNIT_EPOCH_TIME_MS = "EPOCH_TIME_MS"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "BYTES"
    UNIT_BYTES = "BYTES"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "COUNT"
    UNIT_COUNT = "COUNT"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "DURATION_MS"
    UNIT_DURATION_MS = "DURATION_MS"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "TRACE_STATUS"
    UNIT_TRACE_STATUS = "TRACE_STATUS"

    #: A constant which can be used with the unit property of a AttributeResponse.
    #: This constant has a value of "PERCENTAGE"
    UNIT_PERCENTAGE = "PERCENTAGE"

    #: A constant which can be used with the operation_type property of a AttributeResponse.
    #: This constant has a value of "ACTIVATE"
    OPERATION_TYPE_ACTIVATE = "ACTIVATE"

    #: A constant which can be used with the operation_type property of a AttributeResponse.
    #: This constant has a value of "DEACTIVATE"
    OPERATION_TYPE_DEACTIVATE = "DEACTIVATE"

    #: A constant which can be used with the attribute_name_space property of a AttributeResponse.
    #: This constant has a value of "TRACES"
    ATTRIBUTE_NAME_SPACE_TRACES = "TRACES"

    #: A constant which can be used with the attribute_name_space property of a AttributeResponse.
    #: This constant has a value of "SYNTHETIC"
    ATTRIBUTE_NAME_SPACE_SYNTHETIC = "SYNTHETIC"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_ALREADY_ACTIVE"
    ATTRIBUTE_STATUS_ATTRIBUTE_ALREADY_ACTIVE = "ATTRIBUTE_ALREADY_ACTIVE"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_ACTIVATED"
    ATTRIBUTE_STATUS_ATTRIBUTE_ACTIVATED = "ATTRIBUTE_ACTIVATED"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_DEACTIVATED"
    ATTRIBUTE_STATUS_ATTRIBUTE_DEACTIVATED = "ATTRIBUTE_DEACTIVATED"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "DEACTIVATION_NOT_ALLOWED"
    ATTRIBUTE_STATUS_DEACTIVATION_NOT_ALLOWED = "DEACTIVATION_NOT_ALLOWED"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_DOES_NOT_EXIST"
    ATTRIBUTE_STATUS_ATTRIBUTE_DOES_NOT_EXIST = "ATTRIBUTE_DOES_NOT_EXIST"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_ALREADY_DEACTIVATED"
    ATTRIBUTE_STATUS_ATTRIBUTE_ALREADY_DEACTIVATED = "ATTRIBUTE_ALREADY_DEACTIVATED"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "DUPLICATE_ATTRIBUTE"
    ATTRIBUTE_STATUS_DUPLICATE_ATTRIBUTE = "DUPLICATE_ATTRIBUTE"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "INVALID_ATTRIBUTE"
    ATTRIBUTE_STATUS_INVALID_ATTRIBUTE = "INVALID_ATTRIBUTE"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "INVALID_ATTRIBUTE_TYPE_CONFLICT"
    ATTRIBUTE_STATUS_INVALID_ATTRIBUTE_TYPE_CONFLICT = "INVALID_ATTRIBUTE_TYPE_CONFLICT"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_NOT_PROCESSED"
    ATTRIBUTE_STATUS_ATTRIBUTE_NOT_PROCESSED = "ATTRIBUTE_NOT_PROCESSED"

    #: A constant which can be used with the attribute_status property of a AttributeResponse.
    #: This constant has a value of "ATTRIBUTE_UPDATE_NOT_ALLOWED"
    ATTRIBUTE_STATUS_ATTRIBUTE_UPDATE_NOT_ALLOWED = "ATTRIBUTE_UPDATE_NOT_ALLOWED"

    def __init__(self, **kwargs):
        """
        Initializes a new AttributeResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this AttributeResponse.
        :type attribute_name: str

        :param attribute_type:
            The value to assign to the attribute_type property of this AttributeResponse.
            Allowed values for this property are: "NUMERIC", "STRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_type: str

        :param unit:
            The value to assign to the unit property of this AttributeResponse.
            Allowed values for this property are: "NONE", "EPOCH_TIME_MS", "BYTES", "COUNT", "DURATION_MS", "TRACE_STATUS", "PERCENTAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        :param notes:
            The value to assign to the notes property of this AttributeResponse.
        :type notes: str

        :param operation_type:
            The value to assign to the operation_type property of this AttributeResponse.
            Allowed values for this property are: "ACTIVATE", "DEACTIVATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param attribute_name_space:
            The value to assign to the attribute_name_space property of this AttributeResponse.
            Allowed values for this property are: "TRACES", "SYNTHETIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_name_space: str

        :param attribute_status:
            The value to assign to the attribute_status property of this AttributeResponse.
            Allowed values for this property are: "ATTRIBUTE_ALREADY_ACTIVE", "ATTRIBUTE_ACTIVATED", "ATTRIBUTE_DEACTIVATED", "DEACTIVATION_NOT_ALLOWED", "ATTRIBUTE_DOES_NOT_EXIST", "ATTRIBUTE_ALREADY_DEACTIVATED", "DUPLICATE_ATTRIBUTE", "INVALID_ATTRIBUTE", "INVALID_ATTRIBUTE_TYPE_CONFLICT", "ATTRIBUTE_NOT_PROCESSED", "ATTRIBUTE_UPDATE_NOT_ALLOWED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type attribute_status: str

        :param time_updated:
            The value to assign to the time_updated property of this AttributeResponse.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_type': 'str',
            'unit': 'str',
            'notes': 'str',
            'operation_type': 'str',
            'attribute_name_space': 'str',
            'attribute_status': 'str',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_type': 'attributeType',
            'unit': 'unit',
            'notes': 'notes',
            'operation_type': 'operationType',
            'attribute_name_space': 'attributeNameSpace',
            'attribute_status': 'attributeStatus',
            'time_updated': 'timeUpdated'
        }
        self._attribute_name = None
        self._attribute_type = None
        self._unit = None
        self._notes = None
        self._operation_type = None
        self._attribute_name_space = None
        self._attribute_status = None
        self._time_updated = None

    @property
    def attribute_name(self):
        """
        **[Required]** Gets the attribute_name of this AttributeResponse.
        Attribute that was activated or deactivated by this bulk operation.


        :return: The attribute_name of this AttributeResponse.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """
        Sets the attribute_name of this AttributeResponse.
        Attribute that was activated or deactivated by this bulk operation.


        :param attribute_name: The attribute_name of this AttributeResponse.
        :type: str
        """
        self._attribute_name = attribute_name

    @property
    def attribute_type(self):
        """
        **[Required]** Gets the attribute_type of this AttributeResponse.
        Type of the attribute.

        Allowed values for this property are: "NUMERIC", "STRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attribute_type of this AttributeResponse.
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """
        Sets the attribute_type of this AttributeResponse.
        Type of the attribute.


        :param attribute_type: The attribute_type of this AttributeResponse.
        :type: str
        """
        allowed_values = ["NUMERIC", "STRING"]
        if not value_allowed_none_or_none_sentinel(attribute_type, allowed_values):
            attribute_type = 'UNKNOWN_ENUM_VALUE'
        self._attribute_type = attribute_type

    @property
    def unit(self):
        """
        Gets the unit of this AttributeResponse.
        Unit of the attribute.   If unit is not specified, it defaults to NONE.

        Allowed values for this property are: "NONE", "EPOCH_TIME_MS", "BYTES", "COUNT", "DURATION_MS", "TRACE_STATUS", "PERCENTAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this AttributeResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this AttributeResponse.
        Unit of the attribute.   If unit is not specified, it defaults to NONE.


        :param unit: The unit of this AttributeResponse.
        :type: str
        """
        allowed_values = ["NONE", "EPOCH_TIME_MS", "BYTES", "COUNT", "DURATION_MS", "TRACE_STATUS", "PERCENTAGE"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    @property
    def notes(self):
        """
        Gets the notes of this AttributeResponse.
        Notes for the activated attribute.


        :return: The notes of this AttributeResponse.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this AttributeResponse.
        Notes for the activated attribute.


        :param notes: The notes of this AttributeResponse.
        :type: str
        """
        self._notes = notes

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this AttributeResponse.
        Type of operation - activate or deactivate.

        Allowed values for this property are: "ACTIVATE", "DEACTIVATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this AttributeResponse.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this AttributeResponse.
        Type of operation - activate or deactivate.


        :param operation_type: The operation_type of this AttributeResponse.
        :type: str
        """
        allowed_values = ["ACTIVATE", "DEACTIVATE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def attribute_name_space(self):
        """
        **[Required]** Gets the attribute_name_space of this AttributeResponse.
        Namespace of the attribute whose properties were updated.  The attributeNamespace will default to TRACES if it is
        not passed in.

        Allowed values for this property are: "TRACES", "SYNTHETIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attribute_name_space of this AttributeResponse.
        :rtype: str
        """
        return self._attribute_name_space

    @attribute_name_space.setter
    def attribute_name_space(self, attribute_name_space):
        """
        Sets the attribute_name_space of this AttributeResponse.
        Namespace of the attribute whose properties were updated.  The attributeNamespace will default to TRACES if it is
        not passed in.


        :param attribute_name_space: The attribute_name_space of this AttributeResponse.
        :type: str
        """
        allowed_values = ["TRACES", "SYNTHETIC"]
        if not value_allowed_none_or_none_sentinel(attribute_name_space, allowed_values):
            attribute_name_space = 'UNKNOWN_ENUM_VALUE'
        self._attribute_name_space = attribute_name_space

    @property
    def attribute_status(self):
        """
        **[Required]** Gets the attribute_status of this AttributeResponse.
        Status of the attribute after this operation.  The attribute can have one of the following statuses after the activate or deactivate operation.  The attribute
        can have either a success status or an error status.  The status of the attribute must be correlated with the operation status property in the bulk operation metadata
        object.  The bulk operation will be successful only when all attributes in the bulk request are processed successful and they get a success status back.
        The following are successful status values of individual attribute items in a bulk attribute activation operation.
        ATTRIBUTE_ACTIVATED - The attribute is activated and is available to be queried.  Note that ingest might still have not picked up the changes, and the
        associated caches would not have refreshed yet to pick up the changes.
        ATTRIBUTE_ALREADY_ACTIVE - The caller is trying to activate an attribute that is already active or in the process of getting activated.
        ATTRIBUTE_DEACTIVATED - The attribute is deactivated and will not appear in searches.  Ingest might not have picked up the new changes and the associated caches
        might not have refreshed yet.
        ATTRIBUTE_ALREADY_DEACTIVATED - The caller is trying to deactivate an attribute that has already been deactivated or in the process of deactivation.
        DUPLICATE_ATTRIBUTE - The attribute is a duplicate of an attribute that was present in this bulk request.  Note that we deduplicate the attribute collection, process only unique attributes,
        and call out duplicates.  A duplicate attribute in a bulk request will not prevent the processing of further attributes in the bulk operation.
        The following values are error statuses and the bulk processing is stopped when the first error is encountered.  None of the attributes in the bulk request would have been activated or
        deactivated by this bulk operation.
        DEACTIVATION_NOT_ALLOWED - The caller has asked for the deactivation of an out of box tag which is not permitted.
        ATTRIBUTE_DOES_NOT_EXIST - The caller tries to deactivate an attribute that doesn't exist in the APM Domain.
        INVALID_ATTRIBUTE - The attribute is invalid.
        INVALID_ATTRIBUTE_TYPE_CONFLICT - The attribute is invalid.  There were two attributes with same name but different type in the bulk request.
        ATTRIBUTE_NOT_PROCESSED - The attribute was not processed, as there was another attribute in this bulk request collection that resulted in a processing error.
        ATTRIBUTE_UPDATE_NOT_ALLOWED - The unit of the attribute cannot be updated as it is an in-built system attribute.

        Allowed values for this property are: "ATTRIBUTE_ALREADY_ACTIVE", "ATTRIBUTE_ACTIVATED", "ATTRIBUTE_DEACTIVATED", "DEACTIVATION_NOT_ALLOWED", "ATTRIBUTE_DOES_NOT_EXIST", "ATTRIBUTE_ALREADY_DEACTIVATED", "DUPLICATE_ATTRIBUTE", "INVALID_ATTRIBUTE", "INVALID_ATTRIBUTE_TYPE_CONFLICT", "ATTRIBUTE_NOT_PROCESSED", "ATTRIBUTE_UPDATE_NOT_ALLOWED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The attribute_status of this AttributeResponse.
        :rtype: str
        """
        return self._attribute_status

    @attribute_status.setter
    def attribute_status(self, attribute_status):
        """
        Sets the attribute_status of this AttributeResponse.
        Status of the attribute after this operation.  The attribute can have one of the following statuses after the activate or deactivate operation.  The attribute
        can have either a success status or an error status.  The status of the attribute must be correlated with the operation status property in the bulk operation metadata
        object.  The bulk operation will be successful only when all attributes in the bulk request are processed successful and they get a success status back.
        The following are successful status values of individual attribute items in a bulk attribute activation operation.
        ATTRIBUTE_ACTIVATED - The attribute is activated and is available to be queried.  Note that ingest might still have not picked up the changes, and the
        associated caches would not have refreshed yet to pick up the changes.
        ATTRIBUTE_ALREADY_ACTIVE - The caller is trying to activate an attribute that is already active or in the process of getting activated.
        ATTRIBUTE_DEACTIVATED - The attribute is deactivated and will not appear in searches.  Ingest might not have picked up the new changes and the associated caches
        might not have refreshed yet.
        ATTRIBUTE_ALREADY_DEACTIVATED - The caller is trying to deactivate an attribute that has already been deactivated or in the process of deactivation.
        DUPLICATE_ATTRIBUTE - The attribute is a duplicate of an attribute that was present in this bulk request.  Note that we deduplicate the attribute collection, process only unique attributes,
        and call out duplicates.  A duplicate attribute in a bulk request will not prevent the processing of further attributes in the bulk operation.
        The following values are error statuses and the bulk processing is stopped when the first error is encountered.  None of the attributes in the bulk request would have been activated or
        deactivated by this bulk operation.
        DEACTIVATION_NOT_ALLOWED - The caller has asked for the deactivation of an out of box tag which is not permitted.
        ATTRIBUTE_DOES_NOT_EXIST - The caller tries to deactivate an attribute that doesn't exist in the APM Domain.
        INVALID_ATTRIBUTE - The attribute is invalid.
        INVALID_ATTRIBUTE_TYPE_CONFLICT - The attribute is invalid.  There were two attributes with same name but different type in the bulk request.
        ATTRIBUTE_NOT_PROCESSED - The attribute was not processed, as there was another attribute in this bulk request collection that resulted in a processing error.
        ATTRIBUTE_UPDATE_NOT_ALLOWED - The unit of the attribute cannot be updated as it is an in-built system attribute.


        :param attribute_status: The attribute_status of this AttributeResponse.
        :type: str
        """
        allowed_values = ["ATTRIBUTE_ALREADY_ACTIVE", "ATTRIBUTE_ACTIVATED", "ATTRIBUTE_DEACTIVATED", "DEACTIVATION_NOT_ALLOWED", "ATTRIBUTE_DOES_NOT_EXIST", "ATTRIBUTE_ALREADY_DEACTIVATED", "DUPLICATE_ATTRIBUTE", "INVALID_ATTRIBUTE", "INVALID_ATTRIBUTE_TYPE_CONFLICT", "ATTRIBUTE_NOT_PROCESSED", "ATTRIBUTE_UPDATE_NOT_ALLOWED"]
        if not value_allowed_none_or_none_sentinel(attribute_status, allowed_values):
            attribute_status = 'UNKNOWN_ENUM_VALUE'
        self._attribute_status = attribute_status

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AttributeResponse.
        Time when the attribute was activated or deactivated.  Note that ingest might not have picked up the changes even if this time has elapsed.


        :return: The time_updated of this AttributeResponse.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AttributeResponse.
        Time when the attribute was activated or deactivated.  Note that ingest might not have picked up the changes even if this time has elapsed.


        :param time_updated: The time_updated of this AttributeResponse.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
