# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Function(object):
    """
    A function resource defines the code (Docker image) and configuration for a specific function. Functions are defined in applications. Avoid entering confidential information.
    """

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Function.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Function object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Function.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Function.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Function.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param application_id:
            The value to assign to the application_id property of this Function.
        :type application_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Function.
        :type compartment_id: str

        :param image:
            The value to assign to the image property of this Function.
        :type image: str

        :param image_digest:
            The value to assign to the image_digest property of this Function.
        :type image_digest: str

        :param memory_in_mbs:
            The value to assign to the memory_in_mbs property of this Function.
        :type memory_in_mbs: int

        :param config:
            The value to assign to the config property of this Function.
        :type config: dict(str, str)

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this Function.
        :type timeout_in_seconds: int

        :param trace_config:
            The value to assign to the trace_config property of this Function.
        :type trace_config: oci.functions.models.FunctionTraceConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Function.
        :type freeform_tags: dict(str, str)

        :param invoke_endpoint:
            The value to assign to the invoke_endpoint property of this Function.
        :type invoke_endpoint: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Function.
        :type defined_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this Function.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Function.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'application_id': 'str',
            'compartment_id': 'str',
            'image': 'str',
            'image_digest': 'str',
            'memory_in_mbs': 'int',
            'config': 'dict(str, str)',
            'timeout_in_seconds': 'int',
            'trace_config': 'FunctionTraceConfig',
            'freeform_tags': 'dict(str, str)',
            'invoke_endpoint': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'application_id': 'applicationId',
            'compartment_id': 'compartmentId',
            'image': 'image',
            'image_digest': 'imageDigest',
            'memory_in_mbs': 'memoryInMBs',
            'config': 'config',
            'timeout_in_seconds': 'timeoutInSeconds',
            'trace_config': 'traceConfig',
            'freeform_tags': 'freeformTags',
            'invoke_endpoint': 'invokeEndpoint',
            'defined_tags': 'definedTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._display_name = None
        self._lifecycle_state = None
        self._application_id = None
        self._compartment_id = None
        self._image = None
        self._image_digest = None
        self._memory_in_mbs = None
        self._config = None
        self._timeout_in_seconds = None
        self._trace_config = None
        self._freeform_tags = None
        self._invoke_endpoint = None
        self._defined_tags = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Function.
        The `OCID`__ of the function.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Function.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Function.
        The `OCID`__ of the function.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Function.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Function.
        The display name of the function. The display name is unique within the application containing the function.


        :return: The display_name of this Function.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Function.
        The display name of the function. The display name is unique within the application containing the function.


        :param display_name: The display_name of this Function.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Function.
        The current state of the function.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Function.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Function.
        The current state of the function.


        :param lifecycle_state: The lifecycle_state of this Function.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def application_id(self):
        """
        Gets the application_id of this Function.
        The OCID of the application the function belongs to.


        :return: The application_id of this Function.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this Function.
        The OCID of the application the function belongs to.


        :param application_id: The application_id of this Function.
        :type: str
        """
        self._application_id = application_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Function.
        The OCID of the compartment that contains the function.


        :return: The compartment_id of this Function.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Function.
        The OCID of the compartment that contains the function.


        :param compartment_id: The compartment_id of this Function.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def image(self):
        """
        Gets the image of this Function.
        The qualified name of the Docker image to use in the function, including the image tag.
        The image should be in the OCI Registry that is in the same region as the function itself.
        Example: `phx.ocir.io/ten/functions/function:0.0.1`


        :return: The image of this Function.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Function.
        The qualified name of the Docker image to use in the function, including the image tag.
        The image should be in the OCI Registry that is in the same region as the function itself.
        Example: `phx.ocir.io/ten/functions/function:0.0.1`


        :param image: The image of this Function.
        :type: str
        """
        self._image = image

    @property
    def image_digest(self):
        """
        Gets the image_digest of this Function.
        The image digest for the version of the image that will be pulled when invoking this function.
        If no value is specified, the digest currently associated with the image in the OCI Registry will be used.
        Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`


        :return: The image_digest of this Function.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """
        Sets the image_digest of this Function.
        The image digest for the version of the image that will be pulled when invoking this function.
        If no value is specified, the digest currently associated with the image in the OCI Registry will be used.
        Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`


        :param image_digest: The image_digest of this Function.
        :type: str
        """
        self._image_digest = image_digest

    @property
    def memory_in_mbs(self):
        """
        Gets the memory_in_mbs of this Function.
        Maximum usable memory for the function (MiB).


        :return: The memory_in_mbs of this Function.
        :rtype: int
        """
        return self._memory_in_mbs

    @memory_in_mbs.setter
    def memory_in_mbs(self, memory_in_mbs):
        """
        Sets the memory_in_mbs of this Function.
        Maximum usable memory for the function (MiB).


        :param memory_in_mbs: The memory_in_mbs of this Function.
        :type: int
        """
        self._memory_in_mbs = memory_in_mbs

    @property
    def config(self):
        """
        Gets the config of this Function.
        Function configuration. Overrides application configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :return: The config of this Function.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this Function.
        Function configuration. Overrides application configuration.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :param config: The config of this Function.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this Function.
        Timeout for executions of the function. Value in seconds.


        :return: The timeout_in_seconds of this Function.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this Function.
        Timeout for executions of the function. Value in seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this Function.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def trace_config(self):
        """
        Gets the trace_config of this Function.

        :return: The trace_config of this Function.
        :rtype: oci.functions.models.FunctionTraceConfig
        """
        return self._trace_config

    @trace_config.setter
    def trace_config(self, trace_config):
        """
        Sets the trace_config of this Function.

        :param trace_config: The trace_config of this Function.
        :type: oci.functions.models.FunctionTraceConfig
        """
        self._trace_config = trace_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Function.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Function.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Function.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Function.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def invoke_endpoint(self):
        """
        Gets the invoke_endpoint of this Function.
        The base https invoke URL to set on a client in order to invoke a function. This URL will never change over the lifetime of the function and can be cached.


        :return: The invoke_endpoint of this Function.
        :rtype: str
        """
        return self._invoke_endpoint

    @invoke_endpoint.setter
    def invoke_endpoint(self, invoke_endpoint):
        """
        Sets the invoke_endpoint of this Function.
        The base https invoke URL to set on a client in order to invoke a function. This URL will never change over the lifetime of the function and can be cached.


        :param invoke_endpoint: The invoke_endpoint of this Function.
        :type: str
        """
        self._invoke_endpoint = invoke_endpoint

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Function.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Function.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Function.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Function.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def time_created(self):
        """
        Gets the time_created of this Function.
        The time the function was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Function.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Function.
        The time the function was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Function.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Function.
        The time the function was updated, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Function.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Function.
        The time the function was updated, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Function.
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
