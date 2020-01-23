# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferApplianceEntitlement(object):
    """
    TransferApplianceEntitlement model.
    """

    #: A constant which can be used with the lifecycle_state property of a TransferApplianceEntitlement.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TransferApplianceEntitlement.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TransferApplianceEntitlement.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TransferApplianceEntitlement.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferApplianceEntitlement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TransferApplianceEntitlement.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TransferApplianceEntitlement.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this TransferApplianceEntitlement.
        :type display_name: str

        :param requestor_name:
            The value to assign to the requestor_name property of this TransferApplianceEntitlement.
        :type requestor_name: str

        :param requestor_email:
            The value to assign to the requestor_email property of this TransferApplianceEntitlement.
        :type requestor_email: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TransferApplianceEntitlement.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this TransferApplianceEntitlement.
        :type lifecycle_state_details: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferApplianceEntitlement.
        :type creation_time: datetime

        :param update_time:
            The value to assign to the update_time property of this TransferApplianceEntitlement.
        :type update_time: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TransferApplianceEntitlement.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TransferApplianceEntitlement.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'requestor_name': 'str',
            'requestor_email': 'str',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'creation_time': 'datetime',
            'update_time': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'requestor_name': 'requestorName',
            'requestor_email': 'requestorEmail',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'creation_time': 'creationTime',
            'update_time': 'updateTime',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._requestor_name = None
        self._requestor_email = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._creation_time = None
        self._update_time = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this TransferApplianceEntitlement.

        :return: The id of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TransferApplianceEntitlement.

        :param id: The id of this TransferApplianceEntitlement.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TransferApplianceEntitlement.

        :return: The compartment_id of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TransferApplianceEntitlement.

        :param compartment_id: The compartment_id of this TransferApplianceEntitlement.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this TransferApplianceEntitlement.

        :return: The display_name of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TransferApplianceEntitlement.

        :param display_name: The display_name of this TransferApplianceEntitlement.
        :type: str
        """
        self._display_name = display_name

    @property
    def requestor_name(self):
        """
        Gets the requestor_name of this TransferApplianceEntitlement.

        :return: The requestor_name of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._requestor_name

    @requestor_name.setter
    def requestor_name(self, requestor_name):
        """
        Sets the requestor_name of this TransferApplianceEntitlement.

        :param requestor_name: The requestor_name of this TransferApplianceEntitlement.
        :type: str
        """
        self._requestor_name = requestor_name

    @property
    def requestor_email(self):
        """
        Gets the requestor_email of this TransferApplianceEntitlement.

        :return: The requestor_email of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._requestor_email

    @requestor_email.setter
    def requestor_email(self, requestor_email):
        """
        Sets the requestor_email of this TransferApplianceEntitlement.

        :param requestor_email: The requestor_email of this TransferApplianceEntitlement.
        :type: str
        """
        self._requestor_email = requestor_email

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TransferApplianceEntitlement.
        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TransferApplianceEntitlement.

        :param lifecycle_state: The lifecycle_state of this TransferApplianceEntitlement.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this TransferApplianceEntitlement.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this TransferApplianceEntitlement.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this TransferApplianceEntitlement.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this TransferApplianceEntitlement.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferApplianceEntitlement.

        :return: The creation_time of this TransferApplianceEntitlement.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferApplianceEntitlement.

        :param creation_time: The creation_time of this TransferApplianceEntitlement.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def update_time(self):
        """
        Gets the update_time of this TransferApplianceEntitlement.

        :return: The update_time of this TransferApplianceEntitlement.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this TransferApplianceEntitlement.

        :param update_time: The update_time of this TransferApplianceEntitlement.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TransferApplianceEntitlement.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this TransferApplianceEntitlement.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TransferApplianceEntitlement.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this TransferApplianceEntitlement.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TransferApplianceEntitlement.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this TransferApplianceEntitlement.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TransferApplianceEntitlement.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this TransferApplianceEntitlement.
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
