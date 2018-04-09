# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CaptureConsoleHistoryDetails(object):
    """
    CaptureConsoleHistoryDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CaptureConsoleHistoryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this CaptureConsoleHistoryDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CaptureConsoleHistoryDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CaptureConsoleHistoryDetails.
        :type freeform_tags: dict(str, str)

        :param instance_id:
            The value to assign to the instance_id property of this CaptureConsoleHistoryDetails.
        :type instance_id: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'instance_id': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'instance_id': 'instanceId'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._instance_id = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CaptureConsoleHistoryDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CaptureConsoleHistoryDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CaptureConsoleHistoryDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CaptureConsoleHistoryDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CaptureConsoleHistoryDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CaptureConsoleHistoryDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CaptureConsoleHistoryDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CaptureConsoleHistoryDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CaptureConsoleHistoryDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CaptureConsoleHistoryDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CaptureConsoleHistoryDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CaptureConsoleHistoryDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this CaptureConsoleHistoryDetails.
        The OCID of the instance to get the console history from.


        :return: The instance_id of this CaptureConsoleHistoryDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CaptureConsoleHistoryDetails.
        The OCID of the instance to get the console history from.


        :param instance_id: The instance_id of this CaptureConsoleHistoryDetails.
        :type: str
        """
        self._instance_id = instance_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
