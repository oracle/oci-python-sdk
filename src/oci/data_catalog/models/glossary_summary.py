# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GlossarySummary(object):
    """
    Summary of a glossary. A glossary of business terms, such as 'Customer', 'Account', 'Contact', 'Address',
    or 'Product', with definitions, used to provide common meaning across disparate data assets. Business glossaries
    may be hierarchical where some terms may contain child terms to allow them to be used as 'taxonomies'.
    By linking data assets, data entities, and attributes to glossaries and glossary terms, the glossary can act as a
    way of organizing data catalog objects in a hierarchy to make a large number of objects more navigable and easier to
    consume. Objects in the data catalog, such as data assets or data entities, may be linked to any level in the
    glossary, so that the glossary can be used to browse the available data according to the business model of the
    organization.
    """

    #: A constant which can be used with the workflow_status property of a GlossarySummary.
    #: This constant has a value of "NEW"
    WORKFLOW_STATUS_NEW = "NEW"

    #: A constant which can be used with the workflow_status property of a GlossarySummary.
    #: This constant has a value of "APPROVED"
    WORKFLOW_STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the workflow_status property of a GlossarySummary.
    #: This constant has a value of "UNDER_REVIEW"
    WORKFLOW_STATUS_UNDER_REVIEW = "UNDER_REVIEW"

    #: A constant which can be used with the workflow_status property of a GlossarySummary.
    #: This constant has a value of "ESCALATED"
    WORKFLOW_STATUS_ESCALATED = "ESCALATED"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a GlossarySummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new GlossarySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this GlossarySummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this GlossarySummary.
        :type display_name: str

        :param catalog_id:
            The value to assign to the catalog_id property of this GlossarySummary.
        :type catalog_id: str

        :param time_created:
            The value to assign to the time_created property of this GlossarySummary.
        :type time_created: datetime

        :param description:
            The value to assign to the description property of this GlossarySummary.
        :type description: str

        :param uri:
            The value to assign to the uri property of this GlossarySummary.
        :type uri: str

        :param workflow_status:
            The value to assign to the workflow_status property of this GlossarySummary.
            Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type workflow_status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GlossarySummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param import_job_definition_key:
            The value to assign to the import_job_definition_key property of this GlossarySummary.
        :type import_job_definition_key: str

        :param import_job_key:
            The value to assign to the import_job_key property of this GlossarySummary.
        :type import_job_key: str

        :param latest_import_job_execution_key:
            The value to assign to the latest_import_job_execution_key property of this GlossarySummary.
        :type latest_import_job_execution_key: str

        :param latest_import_job_execution_status:
            The value to assign to the latest_import_job_execution_status property of this GlossarySummary.
        :type latest_import_job_execution_status: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'catalog_id': 'str',
            'time_created': 'datetime',
            'description': 'str',
            'uri': 'str',
            'workflow_status': 'str',
            'lifecycle_state': 'str',
            'import_job_definition_key': 'str',
            'import_job_key': 'str',
            'latest_import_job_execution_key': 'str',
            'latest_import_job_execution_status': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'catalog_id': 'catalogId',
            'time_created': 'timeCreated',
            'description': 'description',
            'uri': 'uri',
            'workflow_status': 'workflowStatus',
            'lifecycle_state': 'lifecycleState',
            'import_job_definition_key': 'importJobDefinitionKey',
            'import_job_key': 'importJobKey',
            'latest_import_job_execution_key': 'latestImportJobExecutionKey',
            'latest_import_job_execution_status': 'latestImportJobExecutionStatus'
        }

        self._key = None
        self._display_name = None
        self._catalog_id = None
        self._time_created = None
        self._description = None
        self._uri = None
        self._workflow_status = None
        self._lifecycle_state = None
        self._import_job_definition_key = None
        self._import_job_key = None
        self._latest_import_job_execution_key = None
        self._latest_import_job_execution_status = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this GlossarySummary.
        Unique glossary key that is immutable.


        :return: The key of this GlossarySummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this GlossarySummary.
        Unique glossary key that is immutable.


        :param key: The key of this GlossarySummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this GlossarySummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this GlossarySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this GlossarySummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this GlossarySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this GlossarySummary.
        The data catalog's OCID.


        :return: The catalog_id of this GlossarySummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this GlossarySummary.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this GlossarySummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def time_created(self):
        """
        Gets the time_created of this GlossarySummary.
        The date and time the glossary was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this GlossarySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this GlossarySummary.
        The date and time the glossary was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this GlossarySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def description(self):
        """
        Gets the description of this GlossarySummary.
        Detailed description of the glossary.


        :return: The description of this GlossarySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GlossarySummary.
        Detailed description of the glossary.


        :param description: The description of this GlossarySummary.
        :type: str
        """
        self._description = description

    @property
    def uri(self):
        """
        Gets the uri of this GlossarySummary.
        URI to the glossary instance in the API.


        :return: The uri of this GlossarySummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this GlossarySummary.
        URI to the glossary instance in the API.


        :param uri: The uri of this GlossarySummary.
        :type: str
        """
        self._uri = uri

    @property
    def workflow_status(self):
        """
        Gets the workflow_status of this GlossarySummary.
        Status of the approval process workflow for this business glossary.

        Allowed values for this property are: "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The workflow_status of this GlossarySummary.
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """
        Sets the workflow_status of this GlossarySummary.
        Status of the approval process workflow for this business glossary.


        :param workflow_status: The workflow_status of this GlossarySummary.
        :type: str
        """
        allowed_values = ["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]
        if not value_allowed_none_or_none_sentinel(workflow_status, allowed_values):
            workflow_status = 'UNKNOWN_ENUM_VALUE'
        self._workflow_status = workflow_status

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this GlossarySummary.
        State of the Glossary.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this GlossarySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this GlossarySummary.
        State of the Glossary.


        :param lifecycle_state: The lifecycle_state of this GlossarySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def import_job_definition_key(self):
        """
        Gets the import_job_definition_key of this GlossarySummary.
        The unique key of the job definition resource that was used in the Glossary import.


        :return: The import_job_definition_key of this GlossarySummary.
        :rtype: str
        """
        return self._import_job_definition_key

    @import_job_definition_key.setter
    def import_job_definition_key(self, import_job_definition_key):
        """
        Sets the import_job_definition_key of this GlossarySummary.
        The unique key of the job definition resource that was used in the Glossary import.


        :param import_job_definition_key: The import_job_definition_key of this GlossarySummary.
        :type: str
        """
        self._import_job_definition_key = import_job_definition_key

    @property
    def import_job_key(self):
        """
        Gets the import_job_key of this GlossarySummary.
        The unique key of the job policy for Glossary import.


        :return: The import_job_key of this GlossarySummary.
        :rtype: str
        """
        return self._import_job_key

    @import_job_key.setter
    def import_job_key(self, import_job_key):
        """
        Sets the import_job_key of this GlossarySummary.
        The unique key of the job policy for Glossary import.


        :param import_job_key: The import_job_key of this GlossarySummary.
        :type: str
        """
        self._import_job_key = import_job_key

    @property
    def latest_import_job_execution_key(self):
        """
        Gets the latest_import_job_execution_key of this GlossarySummary.
        The unique key of the parent job execution for which the log resource was created.


        :return: The latest_import_job_execution_key of this GlossarySummary.
        :rtype: str
        """
        return self._latest_import_job_execution_key

    @latest_import_job_execution_key.setter
    def latest_import_job_execution_key(self, latest_import_job_execution_key):
        """
        Sets the latest_import_job_execution_key of this GlossarySummary.
        The unique key of the parent job execution for which the log resource was created.


        :param latest_import_job_execution_key: The latest_import_job_execution_key of this GlossarySummary.
        :type: str
        """
        self._latest_import_job_execution_key = latest_import_job_execution_key

    @property
    def latest_import_job_execution_status(self):
        """
        Gets the latest_import_job_execution_status of this GlossarySummary.
        Status of the latest glossary import job execution, such as running, paused, or completed.
        This may include additional information like time import started , import file size and % of completion


        :return: The latest_import_job_execution_status of this GlossarySummary.
        :rtype: str
        """
        return self._latest_import_job_execution_status

    @latest_import_job_execution_status.setter
    def latest_import_job_execution_status(self, latest_import_job_execution_status):
        """
        Sets the latest_import_job_execution_status of this GlossarySummary.
        Status of the latest glossary import job execution, such as running, paused, or completed.
        This may include additional information like time import started , import file size and % of completion


        :param latest_import_job_execution_status: The latest_import_job_execution_status of this GlossarySummary.
        :type: str
        """
        self._latest_import_job_execution_status = latest_import_job_execution_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
