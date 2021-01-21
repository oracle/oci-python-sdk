# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ByoipRange(object):
    """
    Oracle offers the ability to Bring Your Own IP (BYOIP), importing public IP addresses that you currently own to Oracle Cloud Infrastructure. A `ByoipRange` resource is a record of the imported address block (a BYOIP CIDR block) and also some associated metadata.
    The process used to `Bring Your Own IP`__ is explained in the documentation.

    __ https://docs.cloud.oracle.com/Content/Network/Concepts/BYOIP.htm
    """

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "CREATING"
    LIFECYCLE_DETAILS_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "VALIDATING"
    LIFECYCLE_DETAILS_VALIDATING = "VALIDATING"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "PROVISIONED"
    LIFECYCLE_DETAILS_PROVISIONED = "PROVISIONED"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_DETAILS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "FAILED"
    LIFECYCLE_DETAILS_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "DELETING"
    LIFECYCLE_DETAILS_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "DELETED"
    LIFECYCLE_DETAILS_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "ADVERTISING"
    LIFECYCLE_DETAILS_ADVERTISING = "ADVERTISING"

    #: A constant which can be used with the lifecycle_details property of a ByoipRange.
    #: This constant has a value of "WITHDRAWING"
    LIFECYCLE_DETAILS_WITHDRAWING = "WITHDRAWING"

    #: A constant which can be used with the lifecycle_state property of a ByoipRange.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ByoipRange.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ByoipRange.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ByoipRange.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ByoipRange.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ByoipRange object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this ByoipRange.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ByoipRange.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this ByoipRange.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ByoipRange.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ByoipRange.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this ByoipRange.
        :type id: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ByoipRange.
            Allowed values for this property are: "CREATING", "VALIDATING", "PROVISIONED", "ACTIVE", "FAILED", "DELETING", "DELETED", "ADVERTISING", "WITHDRAWING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ByoipRange.
            Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ByoipRange.
        :type time_created: datetime

        :param time_validated:
            The value to assign to the time_validated property of this ByoipRange.
        :type time_validated: datetime

        :param time_advertised:
            The value to assign to the time_advertised property of this ByoipRange.
        :type time_advertised: datetime

        :param time_withdrawn:
            The value to assign to the time_withdrawn property of this ByoipRange.
        :type time_withdrawn: datetime

        :param validation_token:
            The value to assign to the validation_token property of this ByoipRange.
        :type validation_token: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_validated': 'datetime',
            'time_advertised': 'datetime',
            'time_withdrawn': 'datetime',
            'validation_token': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_validated': 'timeValidated',
            'time_advertised': 'timeAdvertised',
            'time_withdrawn': 'timeWithdrawn',
            'validation_token': 'validationToken'
        }

        self._cidr_block = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_validated = None
        self._time_advertised = None
        self._time_withdrawn = None
        self._validation_token = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this ByoipRange.
        The public IPv4 CIDR block being imported from on-premises to the Oracle cloud.


        :return: The cidr_block of this ByoipRange.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this ByoipRange.
        The public IPv4 CIDR block being imported from on-premises to the Oracle cloud.


        :param cidr_block: The cidr_block of this ByoipRange.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ByoipRange.
        The `OCID`__ of the compartment containing the BYOIP CIDR block.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ByoipRange.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ByoipRange.
        The `OCID`__ of the compartment containing the BYOIP CIDR block.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ByoipRange.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ByoipRange.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ByoipRange.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ByoipRange.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ByoipRange.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this ByoipRange.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this ByoipRange.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ByoipRange.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this ByoipRange.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ByoipRange.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ByoipRange.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ByoipRange.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ByoipRange.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ByoipRange.
        The `OCID`__ of the `ByoipRange` resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ByoipRange.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ByoipRange.
        The `OCID`__ of the `ByoipRange` resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ByoipRange.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ByoipRange.
        The `ByoipRange` resource's current status.

        Allowed values for this property are: "CREATING", "VALIDATING", "PROVISIONED", "ACTIVE", "FAILED", "DELETING", "DELETED", "ADVERTISING", "WITHDRAWING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this ByoipRange.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ByoipRange.
        The `ByoipRange` resource's current status.


        :param lifecycle_details: The lifecycle_details of this ByoipRange.
        :type: str
        """
        allowed_values = ["CREATING", "VALIDATING", "PROVISIONED", "ACTIVE", "FAILED", "DELETING", "DELETED", "ADVERTISING", "WITHDRAWING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ByoipRange.
        The `ByoipRange` resource's current state.

        Allowed values for this property are: "INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ByoipRange.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ByoipRange.
        The `ByoipRange` resource's current state.


        :param lifecycle_state: The lifecycle_state of this ByoipRange.
        :type: str
        """
        allowed_values = ["INACTIVE", "UPDATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ByoipRange.
        The date and time the `ByoipRange` resource was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ByoipRange.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ByoipRange.
        The date and time the `ByoipRange` resource was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ByoipRange.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_validated(self):
        """
        Gets the time_validated of this ByoipRange.
        The date and time the `ByoipRange` resource was validated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_validated of this ByoipRange.
        :rtype: datetime
        """
        return self._time_validated

    @time_validated.setter
    def time_validated(self, time_validated):
        """
        Sets the time_validated of this ByoipRange.
        The date and time the `ByoipRange` resource was validated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_validated: The time_validated of this ByoipRange.
        :type: datetime
        """
        self._time_validated = time_validated

    @property
    def time_advertised(self):
        """
        Gets the time_advertised of this ByoipRange.
        The date and time the `ByoipRange` resource was advertised to the internet by BGP, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_advertised of this ByoipRange.
        :rtype: datetime
        """
        return self._time_advertised

    @time_advertised.setter
    def time_advertised(self, time_advertised):
        """
        Sets the time_advertised of this ByoipRange.
        The date and time the `ByoipRange` resource was advertised to the internet by BGP, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_advertised: The time_advertised of this ByoipRange.
        :type: datetime
        """
        self._time_advertised = time_advertised

    @property
    def time_withdrawn(self):
        """
        Gets the time_withdrawn of this ByoipRange.
        The date and time the `ByoipRange` resource was withdrawn from advertisement by BGP to the internet, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_withdrawn of this ByoipRange.
        :rtype: datetime
        """
        return self._time_withdrawn

    @time_withdrawn.setter
    def time_withdrawn(self, time_withdrawn):
        """
        Sets the time_withdrawn of this ByoipRange.
        The date and time the `ByoipRange` resource was withdrawn from advertisement by BGP to the internet, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_withdrawn: The time_withdrawn of this ByoipRange.
        :type: datetime
        """
        self._time_withdrawn = time_withdrawn

    @property
    def validation_token(self):
        """
        **[Required]** Gets the validation_token of this ByoipRange.
        The validation token is an internally-generated ASCII string used in the validation process. See `Importing a CIDR block`__ for details.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/BYOIP.htm#import_cidr


        :return: The validation_token of this ByoipRange.
        :rtype: str
        """
        return self._validation_token

    @validation_token.setter
    def validation_token(self, validation_token):
        """
        Sets the validation_token of this ByoipRange.
        The validation token is an internally-generated ASCII string used in the validation process. See `Importing a CIDR block`__ for details.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/BYOIP.htm#import_cidr


        :param validation_token: The validation_token of this ByoipRange.
        :type: str
        """
        self._validation_token = validation_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
