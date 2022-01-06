# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationSummary(object):
    """
    Summary of an application.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApplicationSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ApplicationSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ApplicationSummary.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApplicationSummary.
        :type lifecycle_state: str

        :param subnet_ids:
            The value to assign to the subnet_ids property of this ApplicationSummary.
        :type subnet_ids: list[str]

        :param network_security_group_ids:
            The value to assign to the network_security_group_ids property of this ApplicationSummary.
        :type network_security_group_ids: list[str]

        :param trace_config:
            The value to assign to the trace_config property of this ApplicationSummary.
        :type trace_config: oci.functions.models.ApplicationTraceConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApplicationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApplicationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this ApplicationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApplicationSummary.
        :type time_updated: datetime

        :param image_policy_config:
            The value to assign to the image_policy_config property of this ApplicationSummary.
        :type image_policy_config: oci.functions.models.ImagePolicyConfig

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'subnet_ids': 'list[str]',
            'network_security_group_ids': 'list[str]',
            'trace_config': 'ApplicationTraceConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'image_policy_config': 'ImagePolicyConfig'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'subnet_ids': 'subnetIds',
            'network_security_group_ids': 'networkSecurityGroupIds',
            'trace_config': 'traceConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'image_policy_config': 'imagePolicyConfig'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._subnet_ids = None
        self._network_security_group_ids = None
        self._trace_config = None
        self._freeform_tags = None
        self._defined_tags = None
        self._time_created = None
        self._time_updated = None
        self._image_policy_config = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApplicationSummary.
        The `OCID`__ of the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ApplicationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApplicationSummary.
        The `OCID`__ of the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ApplicationSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ApplicationSummary.
        The OCID of the compartment that contains the application.


        :return: The compartment_id of this ApplicationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ApplicationSummary.
        The OCID of the compartment that contains the application.


        :param compartment_id: The compartment_id of this ApplicationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ApplicationSummary.
        The display name of the application. The display name is unique within the compartment containing the application.


        :return: The display_name of this ApplicationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplicationSummary.
        The display name of the application. The display name is unique within the compartment containing the application.


        :param display_name: The display_name of this ApplicationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApplicationSummary.
        The current state of the application.


        :return: The lifecycle_state of this ApplicationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApplicationSummary.
        The current state of the application.


        :param lifecycle_state: The lifecycle_state of this ApplicationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def subnet_ids(self):
        """
        Gets the subnet_ids of this ApplicationSummary.
        The `OCID`__s of the subnets in which to run functions in the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_ids of this ApplicationSummary.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this ApplicationSummary.
        The `OCID`__s of the subnets in which to run functions in the application.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_ids: The subnet_ids of this ApplicationSummary.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def network_security_group_ids(self):
        """
        Gets the network_security_group_ids of this ApplicationSummary.
        The `OCID`__s of the Network Security Groups to add the application to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The network_security_group_ids of this ApplicationSummary.
        :rtype: list[str]
        """
        return self._network_security_group_ids

    @network_security_group_ids.setter
    def network_security_group_ids(self, network_security_group_ids):
        """
        Sets the network_security_group_ids of this ApplicationSummary.
        The `OCID`__s of the Network Security Groups to add the application to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param network_security_group_ids: The network_security_group_ids of this ApplicationSummary.
        :type: list[str]
        """
        self._network_security_group_ids = network_security_group_ids

    @property
    def trace_config(self):
        """
        Gets the trace_config of this ApplicationSummary.

        :return: The trace_config of this ApplicationSummary.
        :rtype: oci.functions.models.ApplicationTraceConfig
        """
        return self._trace_config

    @trace_config.setter
    def trace_config(self, trace_config):
        """
        Sets the trace_config of this ApplicationSummary.

        :param trace_config: The trace_config of this ApplicationSummary.
        :type: oci.functions.models.ApplicationTraceConfig
        """
        self._trace_config = trace_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ApplicationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ApplicationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApplicationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ApplicationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ApplicationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ApplicationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApplicationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ApplicationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def time_created(self):
        """
        Gets the time_created of this ApplicationSummary.
        The time the application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ApplicationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApplicationSummary.
        The time the application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ApplicationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ApplicationSummary.
        The time the application was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ApplicationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ApplicationSummary.
        The time the application was updated, expressed in `RFC 3339`__
        timestamp format.
        Example: `2018-09-12T22:47:12.613Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ApplicationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def image_policy_config(self):
        """
        Gets the image_policy_config of this ApplicationSummary.

        :return: The image_policy_config of this ApplicationSummary.
        :rtype: oci.functions.models.ImagePolicyConfig
        """
        return self._image_policy_config

    @image_policy_config.setter
    def image_policy_config(self, image_policy_config):
        """
        Sets the image_policy_config of this ApplicationSummary.

        :param image_policy_config: The image_policy_config of this ApplicationSummary.
        :type: oci.functions.models.ImagePolicyConfig
        """
        self._image_policy_config = image_policy_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
