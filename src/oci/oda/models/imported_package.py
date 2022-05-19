# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportedPackage(object):
    """
    An imported/instantiated package within an instance.
    """

    #: A constant which can be used with the status property of a ImportedPackage.
    #: This constant has a value of "READY"
    STATUS_READY = "READY"

    #: A constant which can be used with the status property of a ImportedPackage.
    #: This constant has a value of "OPERATION_PENDING"
    STATUS_OPERATION_PENDING = "OPERATION_PENDING"

    #: A constant which can be used with the status property of a ImportedPackage.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ImportedPackage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param oda_instance_id:
            The value to assign to the oda_instance_id property of this ImportedPackage.
        :type oda_instance_id: str

        :param current_package_id:
            The value to assign to the current_package_id property of this ImportedPackage.
        :type current_package_id: str

        :param name:
            The value to assign to the name property of this ImportedPackage.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this ImportedPackage.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ImportedPackage.
        :type version: str

        :param status:
            The value to assign to the status property of this ImportedPackage.
            Allowed values for this property are: "READY", "OPERATION_PENDING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this ImportedPackage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ImportedPackage.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ImportedPackage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ImportedPackage.
        :type defined_tags: dict(str, dict(str, object))

        :param status_message:
            The value to assign to the status_message property of this ImportedPackage.
        :type status_message: str

        :param parameter_values:
            The value to assign to the parameter_values property of this ImportedPackage.
        :type parameter_values: dict(str, str)

        """
        self.swagger_types = {
            'oda_instance_id': 'str',
            'current_package_id': 'str',
            'name': 'str',
            'display_name': 'str',
            'version': 'str',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'status_message': 'str',
            'parameter_values': 'dict(str, str)'
        }

        self.attribute_map = {
            'oda_instance_id': 'odaInstanceId',
            'current_package_id': 'currentPackageId',
            'name': 'name',
            'display_name': 'displayName',
            'version': 'version',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'status_message': 'statusMessage',
            'parameter_values': 'parameterValues'
        }

        self._oda_instance_id = None
        self._current_package_id = None
        self._name = None
        self._display_name = None
        self._version = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._status_message = None
        self._parameter_values = None

    @property
    def oda_instance_id(self):
        """
        **[Required]** Gets the oda_instance_id of this ImportedPackage.
        ID of the host instance.


        :return: The oda_instance_id of this ImportedPackage.
        :rtype: str
        """
        return self._oda_instance_id

    @oda_instance_id.setter
    def oda_instance_id(self, oda_instance_id):
        """
        Sets the oda_instance_id of this ImportedPackage.
        ID of the host instance.


        :param oda_instance_id: The oda_instance_id of this ImportedPackage.
        :type: str
        """
        self._oda_instance_id = oda_instance_id

    @property
    def current_package_id(self):
        """
        **[Required]** Gets the current_package_id of this ImportedPackage.
        ID of the package.


        :return: The current_package_id of this ImportedPackage.
        :rtype: str
        """
        return self._current_package_id

    @current_package_id.setter
    def current_package_id(self, current_package_id):
        """
        Sets the current_package_id of this ImportedPackage.
        ID of the package.


        :param current_package_id: The current_package_id of this ImportedPackage.
        :type: str
        """
        self._current_package_id = current_package_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ImportedPackage.
        Stable name of the package (the same across versions).


        :return: The name of this ImportedPackage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ImportedPackage.
        Stable name of the package (the same across versions).


        :param name: The name of this ImportedPackage.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ImportedPackage.
        Display name of the package (can change across versions).


        :return: The display_name of this ImportedPackage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ImportedPackage.
        Display name of the package (can change across versions).


        :param display_name: The display_name of this ImportedPackage.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ImportedPackage.
        version of the package.


        :return: The version of this ImportedPackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ImportedPackage.
        version of the package.


        :param version: The version of this ImportedPackage.
        :type: str
        """
        self._version = version

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ImportedPackage.
        Status of the imported package.

        Allowed values for this property are: "READY", "OPERATION_PENDING", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ImportedPackage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ImportedPackage.
        Status of the imported package.


        :param status: The status of this ImportedPackage.
        :type: str
        """
        allowed_values = ["READY", "OPERATION_PENDING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ImportedPackage.
        When the imported package was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ImportedPackage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ImportedPackage.
        When the imported package was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ImportedPackage.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ImportedPackage.
        When the imported package was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this ImportedPackage.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ImportedPackage.
        When the imported package was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this ImportedPackage.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ImportedPackage.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ImportedPackage.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ImportedPackage.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ImportedPackage.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ImportedPackage.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ImportedPackage.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ImportedPackage.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ImportedPackage.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def status_message(self):
        """
        **[Required]** Gets the status_message of this ImportedPackage.
        Short message explaining the status of this imported package.


        :return: The status_message of this ImportedPackage.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ImportedPackage.
        Short message explaining the status of this imported package.


        :param status_message: The status_message of this ImportedPackage.
        :type: str
        """
        self._status_message = status_message

    @property
    def parameter_values(self):
        """
        **[Required]** Gets the parameter_values of this ImportedPackage.
        A list of parameter values used to import the package.


        :return: The parameter_values of this ImportedPackage.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        """
        Sets the parameter_values of this ImportedPackage.
        A list of parameter values used to import the package.


        :param parameter_values: The parameter_values of this ImportedPackage.
        :type: dict(str, str)
        """
        self._parameter_values = parameter_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
