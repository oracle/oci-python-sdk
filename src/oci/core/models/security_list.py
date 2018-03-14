# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityList(object):

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityList object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityList.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityList.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this SecurityList.
        :type display_name: str

        :param egress_security_rules:
            The value to assign to the egress_security_rules property of this SecurityList.
        :type egress_security_rules: list[EgressSecurityRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityList.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this SecurityList.
        :type id: str

        :param ingress_security_rules:
            The value to assign to the ingress_security_rules property of this SecurityList.
        :type ingress_security_rules: list[IngressSecurityRule]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityList.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this SecurityList.
        :type time_created: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this SecurityList.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'egress_security_rules': 'list[EgressSecurityRule]',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'ingress_security_rules': 'list[IngressSecurityRule]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'egress_security_rules': 'egressSecurityRules',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'ingress_security_rules': 'ingressSecurityRules',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._egress_security_rules = None
        self._freeform_tags = None
        self._id = None
        self._ingress_security_rules = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SecurityList.
        The OCID of the compartment containing the security list.


        :return: The compartment_id of this SecurityList.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityList.
        The OCID of the compartment containing the security list.


        :param compartment_id: The compartment_id of this SecurityList.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityList.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SecurityList.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityList.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SecurityList.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SecurityList.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this SecurityList.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SecurityList.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this SecurityList.
        :type: str
        """
        self._display_name = display_name

    @property
    def egress_security_rules(self):
        """
        **[Required]** Gets the egress_security_rules of this SecurityList.
        Rules for allowing egress IP packets.


        :return: The egress_security_rules of this SecurityList.
        :rtype: list[EgressSecurityRule]
        """
        return self._egress_security_rules

    @egress_security_rules.setter
    def egress_security_rules(self, egress_security_rules):
        """
        Sets the egress_security_rules of this SecurityList.
        Rules for allowing egress IP packets.


        :param egress_security_rules: The egress_security_rules of this SecurityList.
        :type: list[EgressSecurityRule]
        """
        self._egress_security_rules = egress_security_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityList.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SecurityList.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityList.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SecurityList.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SecurityList.
        The security list's Oracle Cloud ID (OCID).


        :return: The id of this SecurityList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityList.
        The security list's Oracle Cloud ID (OCID).


        :param id: The id of this SecurityList.
        :type: str
        """
        self._id = id

    @property
    def ingress_security_rules(self):
        """
        **[Required]** Gets the ingress_security_rules of this SecurityList.
        Rules for allowing ingress IP packets.


        :return: The ingress_security_rules of this SecurityList.
        :rtype: list[IngressSecurityRule]
        """
        return self._ingress_security_rules

    @ingress_security_rules.setter
    def ingress_security_rules(self, ingress_security_rules):
        """
        Sets the ingress_security_rules of this SecurityList.
        Rules for allowing ingress IP packets.


        :param ingress_security_rules: The ingress_security_rules of this SecurityList.
        :type: list[IngressSecurityRule]
        """
        self._ingress_security_rules = ingress_security_rules

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SecurityList.
        The security list's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SecurityList.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityList.
        The security list's current state.


        :param lifecycle_state: The lifecycle_state of this SecurityList.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SecurityList.
        The date and time the security list was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SecurityList.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityList.
        The date and time the security list was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SecurityList.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this SecurityList.
        The OCID of the VCN the security list belongs to.


        :return: The vcn_id of this SecurityList.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this SecurityList.
        The OCID of the VCN the security list belongs to.


        :param vcn_id: The vcn_id of this SecurityList.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
