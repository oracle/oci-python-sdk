# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccmDemandSignalSummary(object):
    """
    A summary model for the occm demand signal.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OccmDemandSignalSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OccmDemandSignalSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OccmDemandSignalSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this OccmDemandSignalSummary.
        :type display_name: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OccmDemandSignalSummary.
        :type lifecycle_details: str

        :param description:
            The value to assign to the description property of this OccmDemandSignalSummary.
        :type description: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OccmDemandSignalSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OccmDemandSignalSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OccmDemandSignalSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OccmDemandSignalSummary.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this OccmDemandSignalSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OccmDemandSignalSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_details': 'str',
            'description': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_details': 'lifecycleDetails',
            'description': 'description',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_details = None
        self._description = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OccmDemandSignalSummary.
        The OCID of the demand signal.


        :return: The id of this OccmDemandSignalSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OccmDemandSignalSummary.
        The OCID of the demand signal.


        :param id: The id of this OccmDemandSignalSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OccmDemandSignalSummary.
        The OCID of the tenancy from which the request to create the demand signal was made.


        :return: The compartment_id of this OccmDemandSignalSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OccmDemandSignalSummary.
        The OCID of the tenancy from which the request to create the demand signal was made.


        :param compartment_id: The compartment_id of this OccmDemandSignalSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OccmDemandSignalSummary.
        The display name of the demand signal.


        :return: The display_name of this OccmDemandSignalSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OccmDemandSignalSummary.
        The display name of the demand signal.


        :param display_name: The display_name of this OccmDemandSignalSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this OccmDemandSignalSummary.
        The different states associated with a demand signal.

        CREATED -> A demand signal is by default created in this state.
        SUBMITTED -> Once you have reviewed the details of the demand signal, you can transition it to SUBMITTED state so that OCI can start working on it.
        DELETED -> You can delete a demand signal as long as it is in either CREATED or SUBMITTED state.
        IN_PROGRESS -> Once OCI starts working on a given demand signal. They transition it to IN_PROGRESS.
        REJECTED -> OCI can transition the demand signal to this state if all the demand signal items of that demand signal are declined.
        COMPLETED -> OCI will transition the demand signal to COMPLETED state once the quantities which OCI committed to deliver to you has been delivered.


        :return: The lifecycle_details of this OccmDemandSignalSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OccmDemandSignalSummary.
        The different states associated with a demand signal.

        CREATED -> A demand signal is by default created in this state.
        SUBMITTED -> Once you have reviewed the details of the demand signal, you can transition it to SUBMITTED state so that OCI can start working on it.
        DELETED -> You can delete a demand signal as long as it is in either CREATED or SUBMITTED state.
        IN_PROGRESS -> Once OCI starts working on a given demand signal. They transition it to IN_PROGRESS.
        REJECTED -> OCI can transition the demand signal to this state if all the demand signal items of that demand signal are declined.
        COMPLETED -> OCI will transition the demand signal to COMPLETED state once the quantities which OCI committed to deliver to you has been delivered.


        :param lifecycle_details: The lifecycle_details of this OccmDemandSignalSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def description(self):
        """
        Gets the description of this OccmDemandSignalSummary.
        A short description about the demand signal.


        :return: The description of this OccmDemandSignalSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OccmDemandSignalSummary.
        A short description about the demand signal.


        :param description: The description of this OccmDemandSignalSummary.
        :type: str
        """
        self._description = description

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OccmDemandSignalSummary.
        The current lifecycle state of the demand signal.


        :return: The lifecycle_state of this OccmDemandSignalSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OccmDemandSignalSummary.
        The current lifecycle state of the demand signal.


        :param lifecycle_state: The lifecycle_state of this OccmDemandSignalSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OccmDemandSignalSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OccmDemandSignalSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OccmDemandSignalSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OccmDemandSignalSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OccmDemandSignalSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OccmDemandSignalSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OccmDemandSignalSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OccmDemandSignalSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OccmDemandSignalSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OccmDemandSignalSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OccmDemandSignalSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OccmDemandSignalSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OccmDemandSignalSummary.
        The time when the demand signal was created.


        :return: The time_created of this OccmDemandSignalSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OccmDemandSignalSummary.
        The time when the demand signal was created.


        :param time_created: The time_created of this OccmDemandSignalSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this OccmDemandSignalSummary.
        The time when the demand signal was last updated.


        :return: The time_updated of this OccmDemandSignalSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OccmDemandSignalSummary.
        The time when the demand signal was last updated.


        :param time_updated: The time_updated of this OccmDemandSignalSummary.
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
