# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFunctionDetails(object):
    """
    Updates attributes of a function.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFunctionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image:
            The value to assign to the image property of this UpdateFunctionDetails.
        :type image: str

        :param image_digest:
            The value to assign to the image_digest property of this UpdateFunctionDetails.
        :type image_digest: str

        :param memory_in_mbs:
            The value to assign to the memory_in_mbs property of this UpdateFunctionDetails.
        :type memory_in_mbs: int

        :param config:
            The value to assign to the config property of this UpdateFunctionDetails.
        :type config: dict(str, str)

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this UpdateFunctionDetails.
        :type timeout_in_seconds: int

        :param trace_config:
            The value to assign to the trace_config property of this UpdateFunctionDetails.
        :type trace_config: oci.functions.models.FunctionTraceConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateFunctionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateFunctionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'image': 'str',
            'image_digest': 'str',
            'memory_in_mbs': 'int',
            'config': 'dict(str, str)',
            'timeout_in_seconds': 'int',
            'trace_config': 'FunctionTraceConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'image': 'image',
            'image_digest': 'imageDigest',
            'memory_in_mbs': 'memoryInMBs',
            'config': 'config',
            'timeout_in_seconds': 'timeoutInSeconds',
            'trace_config': 'traceConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._image = None
        self._image_digest = None
        self._memory_in_mbs = None
        self._config = None
        self._timeout_in_seconds = None
        self._trace_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def image(self):
        """
        Gets the image of this UpdateFunctionDetails.
        The qualified name of the Docker image to use in the function, including the image tag.
        The image should be in the OCI Registry that is in the same region as the function itself.
        If an image is specified but no value for imageDigest is provided, the digest currently associated with the image tag in the OCI Registry will be used.
        Example: `phx.ocir.io/ten/functions/function:0.0.1`


        :return: The image of this UpdateFunctionDetails.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this UpdateFunctionDetails.
        The qualified name of the Docker image to use in the function, including the image tag.
        The image should be in the OCI Registry that is in the same region as the function itself.
        If an image is specified but no value for imageDigest is provided, the digest currently associated with the image tag in the OCI Registry will be used.
        Example: `phx.ocir.io/ten/functions/function:0.0.1`


        :param image: The image of this UpdateFunctionDetails.
        :type: str
        """
        self._image = image

    @property
    def image_digest(self):
        """
        Gets the image_digest of this UpdateFunctionDetails.
        The image digest for the version of the image that will be pulled when invoking this function.
        Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`


        :return: The image_digest of this UpdateFunctionDetails.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """
        Sets the image_digest of this UpdateFunctionDetails.
        The image digest for the version of the image that will be pulled when invoking this function.
        Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`


        :param image_digest: The image_digest of this UpdateFunctionDetails.
        :type: str
        """
        self._image_digest = image_digest

    @property
    def memory_in_mbs(self):
        """
        Gets the memory_in_mbs of this UpdateFunctionDetails.
        Maximum usable memory for the function (MiB).


        :return: The memory_in_mbs of this UpdateFunctionDetails.
        :rtype: int
        """
        return self._memory_in_mbs

    @memory_in_mbs.setter
    def memory_in_mbs(self, memory_in_mbs):
        """
        Sets the memory_in_mbs of this UpdateFunctionDetails.
        Maximum usable memory for the function (MiB).


        :param memory_in_mbs: The memory_in_mbs of this UpdateFunctionDetails.
        :type: int
        """
        self._memory_in_mbs = memory_in_mbs

    @property
    def config(self):
        """
        Gets the config of this UpdateFunctionDetails.
        Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :return: The config of this UpdateFunctionDetails.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this UpdateFunctionDetails.
        Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values.
        Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

        Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

        The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.


        :param config: The config of this UpdateFunctionDetails.
        :type: dict(str, str)
        """
        self._config = config

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this UpdateFunctionDetails.
        Timeout for executions of the function. Value in seconds.


        :return: The timeout_in_seconds of this UpdateFunctionDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this UpdateFunctionDetails.
        Timeout for executions of the function. Value in seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this UpdateFunctionDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def trace_config(self):
        """
        Gets the trace_config of this UpdateFunctionDetails.

        :return: The trace_config of this UpdateFunctionDetails.
        :rtype: oci.functions.models.FunctionTraceConfig
        """
        return self._trace_config

    @trace_config.setter
    def trace_config(self, trace_config):
        """
        Sets the trace_config of this UpdateFunctionDetails.

        :param trace_config: The trace_config of this UpdateFunctionDetails.
        :type: oci.functions.models.FunctionTraceConfig
        """
        self._trace_config = trace_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateFunctionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateFunctionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateFunctionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateFunctionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateFunctionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateFunctionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateFunctionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateFunctionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
