# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sdk(object):
    """
    Information about the SDK.
    """

    #: A constant which can be used with the lifecycle_state property of a Sdk.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Sdk.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Sdk.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Sdk.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Sdk.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Sdk object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Sdk.
        :type id: str

        :param api_id:
            The value to assign to the api_id property of this Sdk.
        :type api_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Sdk.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Sdk.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Sdk.
        :type time_updated: datetime

        :param display_name:
            The value to assign to the display_name property of this Sdk.
        :type display_name: str

        :param target_language:
            The value to assign to the target_language property of this Sdk.
        :type target_language: str

        :param artifact_url:
            The value to assign to the artifact_url property of this Sdk.
        :type artifact_url: str

        :param time_artifact_url_expires_at:
            The value to assign to the time_artifact_url_expires_at property of this Sdk.
        :type time_artifact_url_expires_at: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Sdk.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Sdk.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Sdk.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Sdk.
        :type defined_tags: dict(str, dict(str, object))

        :param parameters:
            The value to assign to the parameters property of this Sdk.
        :type parameters: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'api_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'display_name': 'str',
            'target_language': 'str',
            'artifact_url': 'str',
            'time_artifact_url_expires_at': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'parameters': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'api_id': 'apiId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'display_name': 'displayName',
            'target_language': 'targetLanguage',
            'artifact_url': 'artifactUrl',
            'time_artifact_url_expires_at': 'timeArtifactUrlExpiresAt',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'parameters': 'parameters'
        }

        self._id = None
        self._api_id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._display_name = None
        self._target_language = None
        self._artifact_url = None
        self._time_artifact_url_expires_at = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._parameters = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Sdk.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Sdk.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sdk.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Sdk.
        :type: str
        """
        self._id = id

    @property
    def api_id(self):
        """
        **[Required]** Gets the api_id of this Sdk.
        The `OCID`__ of API resource

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The api_id of this Sdk.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """
        Sets the api_id of this Sdk.
        The `OCID`__ of API resource

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param api_id: The api_id of this Sdk.
        :type: str
        """
        self._api_id = api_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Sdk.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Sdk.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Sdk.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Sdk.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Sdk.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this Sdk.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Sdk.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this Sdk.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Sdk.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this Sdk.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Sdk.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this Sdk.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Sdk.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this Sdk.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Sdk.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this Sdk.
        :type: str
        """
        self._display_name = display_name

    @property
    def target_language(self):
        """
        **[Required]** Gets the target_language of this Sdk.
        The string representing the target programming language for generating the SDK.


        :return: The target_language of this Sdk.
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """
        Sets the target_language of this Sdk.
        The string representing the target programming language for generating the SDK.


        :param target_language: The target_language of this Sdk.
        :type: str
        """
        self._target_language = target_language

    @property
    def artifact_url(self):
        """
        Gets the artifact_url of this Sdk.
        File location for generated SDK.


        :return: The artifact_url of this Sdk.
        :rtype: str
        """
        return self._artifact_url

    @artifact_url.setter
    def artifact_url(self, artifact_url):
        """
        Sets the artifact_url of this Sdk.
        File location for generated SDK.


        :param artifact_url: The artifact_url of this Sdk.
        :type: str
        """
        self._artifact_url = artifact_url

    @property
    def time_artifact_url_expires_at(self):
        """
        Gets the time_artifact_url_expires_at of this Sdk.
        Expiry of artifact url.


        :return: The time_artifact_url_expires_at of this Sdk.
        :rtype: datetime
        """
        return self._time_artifact_url_expires_at

    @time_artifact_url_expires_at.setter
    def time_artifact_url_expires_at(self, time_artifact_url_expires_at):
        """
        Sets the time_artifact_url_expires_at of this Sdk.
        Expiry of artifact url.


        :param time_artifact_url_expires_at: The time_artifact_url_expires_at of this Sdk.
        :type: datetime
        """
        self._time_artifact_url_expires_at = time_artifact_url_expires_at

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Sdk.
        The current state of the SDK.
        - The SDK will be in CREATING state if the SDK creation is in progress.
        - The SDK will be in ACTIVE state if create is successful.
        - The SDK will be in FAILED state if the create, or delete fails.
        - The SDK will be in DELETING state if the deletion in in progress.
        - The SDK will be in DELETED state if the delete is successful.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Sdk.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Sdk.
        The current state of the SDK.
        - The SDK will be in CREATING state if the SDK creation is in progress.
        - The SDK will be in ACTIVE state if create is successful.
        - The SDK will be in FAILED state if the create, or delete fails.
        - The SDK will be in DELETING state if the deletion in in progress.
        - The SDK will be in DELETED state if the delete is successful.


        :param lifecycle_state: The lifecycle_state of this Sdk.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Sdk.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :return: The lifecycle_details of this Sdk.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Sdk.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a
        resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this Sdk.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Sdk.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Sdk.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Sdk.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Sdk.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Sdk.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Sdk.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Sdk.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Sdk.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def parameters(self):
        """
        Gets the parameters of this Sdk.
        Additional optional configurations passed.
        The applicable config keys are listed under \"parameters\" when \"/sdkLanguageTypes\" is called.

        Example: `{\"configName\": \"configValue\"}`


        :return: The parameters of this Sdk.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Sdk.
        Additional optional configurations passed.
        The applicable config keys are listed under \"parameters\" when \"/sdkLanguageTypes\" is called.

        Example: `{\"configName\": \"configValue\"}`


        :param parameters: The parameters of this Sdk.
        :type: dict(str, str)
        """
        self._parameters = parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
