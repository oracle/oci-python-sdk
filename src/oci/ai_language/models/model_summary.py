# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelSummary(object):
    """
    Summary of the language Model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModelSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ModelSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ModelSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ModelSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this ModelSummary.
        :type description: str

        :param model_details:
            The value to assign to the model_details property of this ModelSummary.
        :type model_details: oci.ai_language.models.ModelDetails

        :param time_created:
            The value to assign to the time_created property of this ModelSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ModelSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ModelSummary.
        :type lifecycle_details: str

        :param project_id:
            The value to assign to the project_id property of this ModelSummary.
        :type project_id: str

        :param version:
            The value to assign to the version property of this ModelSummary.
        :type version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ModelSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ModelSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ModelSummary.
        :type system_tags: dict(str, object)

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'model_details': 'ModelDetails',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'project_id': 'str',
            'version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'model_details': 'modelDetails',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'project_id': 'projectId',
            'version': 'version',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._model_details = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._project_id = None
        self._version = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ModelSummary.
        Unique identifier model OCID of a model that is immutable on creation


        :return: The id of this ModelSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModelSummary.
        Unique identifier model OCID of a model that is immutable on creation


        :param id: The id of this ModelSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ModelSummary.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :return: The display_name of this ModelSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ModelSummary.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this ModelSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ModelSummary.
        The `OCID`__  for the model's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ModelSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ModelSummary.
        The `OCID`__  for the model's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ModelSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this ModelSummary.
        A short description of the Model.


        :return: The description of this ModelSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModelSummary.
        A short description of the Model.


        :param description: The description of this ModelSummary.
        :type: str
        """
        self._description = description

    @property
    def model_details(self):
        """
        **[Required]** Gets the model_details of this ModelSummary.

        :return: The model_details of this ModelSummary.
        :rtype: oci.ai_language.models.ModelDetails
        """
        return self._model_details

    @model_details.setter
    def model_details(self, model_details):
        """
        Sets the model_details of this ModelSummary.

        :param model_details: The model_details of this ModelSummary.
        :type: oci.ai_language.models.ModelDetails
        """
        self._model_details = model_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ModelSummary.
        The time the the Model was created. An RFC3339 formatted datetime string.


        :return: The time_created of this ModelSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ModelSummary.
        The time the the Model was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ModelSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ModelSummary.
        The state of the model.


        :return: The lifecycle_state of this ModelSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ModelSummary.
        The state of the model.


        :param lifecycle_state: The lifecycle_state of this ModelSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ModelSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.


        :return: The lifecycle_details of this ModelSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ModelSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.


        :param lifecycle_details: The lifecycle_details of this ModelSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this ModelSummary.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this ModelSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this ModelSummary.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this ModelSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def version(self):
        """
        Gets the version of this ModelSummary.
        Identifying the model by model id is difficult. This param provides ease of use for end customer.
        <<service>>::<<service-name>>-<<model-type-version>>::<<custom model on which this training has to be done>>
        ex: ai-lang::NER_V1::CUSTOM-V0


        :return: The version of this ModelSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ModelSummary.
        Identifying the model by model id is difficult. This param provides ease of use for end customer.
        <<service>>::<<service-name>>-<<model-type-version>>::<<custom model on which this training has to be done>>
        ex: ai-lang::NER_V1::CUSTOM-V0


        :param version: The version of this ModelSummary.
        :type: str
        """
        self._version = version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ModelSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ModelSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ModelSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ModelSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ModelSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ModelSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ModelSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ModelSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ModelSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`


        :return: The system_tags of this ModelSummary.
        :rtype: dict(str, object)
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ModelSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{ \"orcl-cloud\": { \"free-tier-retained\": \"true\" } }`


        :param system_tags: The system_tags of this ModelSummary.
        :type: dict(str, object)
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
