# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateImageDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateImageDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateImageDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateImageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateImageDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateImageDetails.
        :type freeform_tags: dict(str, str)

        :param image_source_details:
            The value to assign to the image_source_details property of this CreateImageDetails.
        :type image_source_details: ImageSourceDetails

        :param instance_id:
            The value to assign to the instance_id property of this CreateImageDetails.
        :type instance_id: str

        :param launch_mode:
            The value to assign to the launch_mode property of this CreateImageDetails.
            Allowed values for this property are: "NATIVE", "EMULATED", "CUSTOM"
        :type launch_mode: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'image_source_details': 'ImageSourceDetails',
            'instance_id': 'str',
            'launch_mode': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'image_source_details': 'imageSourceDetails',
            'instance_id': 'instanceId',
            'launch_mode': 'launchMode'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._image_source_details = None
        self._instance_id = None
        self._launch_mode = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateImageDetails.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :return: The compartment_id of this CreateImageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateImageDetails.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :param compartment_id: The compartment_id of this CreateImageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateImageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateImageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateImageDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateImageDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My Oracle Linux image`


        :return: The display_name of this CreateImageDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateImageDetails.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My Oracle Linux image`


        :param display_name: The display_name of this CreateImageDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateImageDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateImageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateImageDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateImageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def image_source_details(self):
        """
        Gets the image_source_details of this CreateImageDetails.
        Details for creating an image through import


        :return: The image_source_details of this CreateImageDetails.
        :rtype: ImageSourceDetails
        """
        return self._image_source_details

    @image_source_details.setter
    def image_source_details(self, image_source_details):
        """
        Sets the image_source_details of this CreateImageDetails.
        Details for creating an image through import


        :param image_source_details: The image_source_details of this CreateImageDetails.
        :type: ImageSourceDetails
        """
        self._image_source_details = image_source_details

    @property
    def instance_id(self):
        """
        Gets the instance_id of this CreateImageDetails.
        The OCID of the instance you want to use as the basis for the image.


        :return: The instance_id of this CreateImageDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateImageDetails.
        The OCID of the instance you want to use as the basis for the image.


        :param instance_id: The instance_id of this CreateImageDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def launch_mode(self):
        """
        Gets the launch_mode of this CreateImageDetails.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

        Allowed values for this property are: "NATIVE", "EMULATED", "CUSTOM"


        :return: The launch_mode of this CreateImageDetails.
        :rtype: str
        """
        return self._launch_mode

    @launch_mode.setter
    def launch_mode(self, launch_mode):
        """
        Sets the launch_mode of this CreateImageDetails.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.


        :param launch_mode: The launch_mode of this CreateImageDetails.
        :type: str
        """
        allowed_values = ["NATIVE", "EMULATED", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(launch_mode, allowed_values):
            raise ValueError(
                "Invalid value for `launch_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._launch_mode = launch_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
