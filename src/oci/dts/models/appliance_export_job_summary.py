# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplianceExportJobSummary(object):
    """
    ApplianceExportJobSummary model.
    """

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "INPROGRESS"
    LIFECYCLE_STATE_INPROGRESS = "INPROGRESS"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a ApplianceExportJobSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplianceExportJobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApplianceExportJobSummary.
        :type id: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ApplianceExportJobSummary.
        :type bucket_name: str

        :param display_name:
            The value to assign to the display_name property of this ApplianceExportJobSummary.
        :type display_name: str

        :param creation_time:
            The value to assign to the creation_time property of this ApplianceExportJobSummary.
        :type creation_time: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApplianceExportJobSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this ApplianceExportJobSummary.
        :type lifecycle_state_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApplianceExportJobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApplianceExportJobSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'bucket_name': 'str',
            'display_name': 'str',
            'creation_time': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_state_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'bucket_name': 'bucketName',
            'display_name': 'displayName',
            'creation_time': 'creationTime',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._bucket_name = None
        self._display_name = None
        self._creation_time = None
        self._lifecycle_state = None
        self._lifecycle_state_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this ApplianceExportJobSummary.

        :return: The id of this ApplianceExportJobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApplianceExportJobSummary.

        :param id: The id of this ApplianceExportJobSummary.
        :type: str
        """
        self._id = id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ApplianceExportJobSummary.

        :return: The bucket_name of this ApplianceExportJobSummary.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ApplianceExportJobSummary.

        :param bucket_name: The bucket_name of this ApplianceExportJobSummary.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def display_name(self):
        """
        Gets the display_name of this ApplianceExportJobSummary.

        :return: The display_name of this ApplianceExportJobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApplianceExportJobSummary.

        :param display_name: The display_name of this ApplianceExportJobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def creation_time(self):
        """
        Gets the creation_time of this ApplianceExportJobSummary.

        :return: The creation_time of this ApplianceExportJobSummary.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this ApplianceExportJobSummary.

        :param creation_time: The creation_time of this ApplianceExportJobSummary.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApplianceExportJobSummary.
        Allowed values for this property are: "CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ApplianceExportJobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApplianceExportJobSummary.

        :param lifecycle_state: The lifecycle_state of this ApplianceExportJobSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this ApplianceExportJobSummary.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this ApplianceExportJobSummary.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this ApplianceExportJobSummary.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this ApplianceExportJobSummary.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ApplianceExportJobSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ApplianceExportJobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApplianceExportJobSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ApplianceExportJobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ApplianceExportJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ApplianceExportJobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApplianceExportJobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ApplianceExportJobSummary.
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
