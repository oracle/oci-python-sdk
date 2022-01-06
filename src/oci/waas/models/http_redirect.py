# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpRedirect(object):
    """
    The details of a HTTP Redirect configuration to allow redirecting HTTP traffic from a request domain to a new target.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a HttpRedirect.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a HttpRedirect.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HttpRedirect.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a HttpRedirect.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a HttpRedirect.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a HttpRedirect.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpRedirect object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HttpRedirect.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HttpRedirect.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this HttpRedirect.
        :type display_name: str

        :param domain:
            The value to assign to the domain property of this HttpRedirect.
        :type domain: str

        :param target:
            The value to assign to the target property of this HttpRedirect.
        :type target: oci.waas.models.HttpRedirectTarget

        :param response_code:
            The value to assign to the response_code property of this HttpRedirect.
        :type response_code: int

        :param time_created:
            The value to assign to the time_created property of this HttpRedirect.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HttpRedirect.
            Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this HttpRedirect.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this HttpRedirect.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'domain': 'str',
            'target': 'HttpRedirectTarget',
            'response_code': 'int',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'domain': 'domain',
            'target': 'target',
            'response_code': 'responseCode',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._domain = None
        self._target = None
        self._response_code = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this HttpRedirect.
        The `OCID`__ of the HTTP Redirect.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this HttpRedirect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HttpRedirect.
        The `OCID`__ of the HTTP Redirect.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this HttpRedirect.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this HttpRedirect.
        The `OCID`__ of the HTTP Redirect's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this HttpRedirect.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HttpRedirect.
        The `OCID`__ of the HTTP Redirect's compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this HttpRedirect.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this HttpRedirect.
        The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.


        :return: The display_name of this HttpRedirect.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this HttpRedirect.
        The user-friendly name of the HTTP Redirect. The name can be changed and does not need to be unique.


        :param display_name: The display_name of this HttpRedirect.
        :type: str
        """
        self._display_name = display_name

    @property
    def domain(self):
        """
        Gets the domain of this HttpRedirect.
        The domain from which traffic will be redirected.


        :return: The domain of this HttpRedirect.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this HttpRedirect.
        The domain from which traffic will be redirected.


        :param domain: The domain of this HttpRedirect.
        :type: str
        """
        self._domain = domain

    @property
    def target(self):
        """
        Gets the target of this HttpRedirect.
        The redirect target object including all the redirect data.


        :return: The target of this HttpRedirect.
        :rtype: oci.waas.models.HttpRedirectTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this HttpRedirect.
        The redirect target object including all the redirect data.


        :param target: The target of this HttpRedirect.
        :type: oci.waas.models.HttpRedirectTarget
        """
        self._target = target

    @property
    def response_code(self):
        """
        Gets the response_code of this HttpRedirect.
        The response code returned for the redirect to the client. For more information, see `RFC 7231`__.

        __ https://tools.ietf.org/html/rfc7231#section-6.4


        :return: The response_code of this HttpRedirect.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this HttpRedirect.
        The response code returned for the redirect to the client. For more information, see `RFC 7231`__.

        __ https://tools.ietf.org/html/rfc7231#section-6.4


        :param response_code: The response_code of this HttpRedirect.
        :type: int
        """
        self._response_code = response_code

    @property
    def time_created(self):
        """
        Gets the time_created of this HttpRedirect.
        The date and time the policy was created, expressed in RFC 3339 timestamp format.


        :return: The time_created of this HttpRedirect.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HttpRedirect.
        The date and time the policy was created, expressed in RFC 3339 timestamp format.


        :param time_created: The time_created of this HttpRedirect.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this HttpRedirect.
        The current lifecycle state of the HTTP Redirect.

        Allowed values for this property are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this HttpRedirect.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this HttpRedirect.
        The current lifecycle state of the HTTP Redirect.


        :param lifecycle_state: The lifecycle_state of this HttpRedirect.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this HttpRedirect.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this HttpRedirect.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this HttpRedirect.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this HttpRedirect.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this HttpRedirect.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this HttpRedirect.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this HttpRedirect.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this HttpRedirect.
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
