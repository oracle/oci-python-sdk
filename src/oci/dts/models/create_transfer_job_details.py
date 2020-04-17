# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTransferJobDetails(object):
    """
    CreateTransferJobDetails model.
    """

    #: A constant which can be used with the device_type property of a CreateTransferJobDetails.
    #: This constant has a value of "DISK"
    DEVICE_TYPE_DISK = "DISK"

    #: A constant which can be used with the device_type property of a CreateTransferJobDetails.
    #: This constant has a value of "APPLIANCE"
    DEVICE_TYPE_APPLIANCE = "APPLIANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTransferJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateTransferJobDetails.
        :type compartment_id: str

        :param upload_bucket_name:
            The value to assign to the upload_bucket_name property of this CreateTransferJobDetails.
        :type upload_bucket_name: str

        :param display_name:
            The value to assign to the display_name property of this CreateTransferJobDetails.
        :type display_name: str

        :param device_type:
            The value to assign to the device_type property of this CreateTransferJobDetails.
            Allowed values for this property are: "DISK", "APPLIANCE"
        :type device_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateTransferJobDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateTransferJobDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'upload_bucket_name': 'str',
            'display_name': 'str',
            'device_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'upload_bucket_name': 'uploadBucketName',
            'display_name': 'displayName',
            'device_type': 'deviceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._upload_bucket_name = None
        self._display_name = None
        self._device_type = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateTransferJobDetails.

        :return: The compartment_id of this CreateTransferJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateTransferJobDetails.

        :param compartment_id: The compartment_id of this CreateTransferJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def upload_bucket_name(self):
        """
        Gets the upload_bucket_name of this CreateTransferJobDetails.

        :return: The upload_bucket_name of this CreateTransferJobDetails.
        :rtype: str
        """
        return self._upload_bucket_name

    @upload_bucket_name.setter
    def upload_bucket_name(self, upload_bucket_name):
        """
        Sets the upload_bucket_name of this CreateTransferJobDetails.

        :param upload_bucket_name: The upload_bucket_name of this CreateTransferJobDetails.
        :type: str
        """
        self._upload_bucket_name = upload_bucket_name

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateTransferJobDetails.

        :return: The display_name of this CreateTransferJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateTransferJobDetails.

        :param display_name: The display_name of this CreateTransferJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def device_type(self):
        """
        Gets the device_type of this CreateTransferJobDetails.
        Allowed values for this property are: "DISK", "APPLIANCE"


        :return: The device_type of this CreateTransferJobDetails.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this CreateTransferJobDetails.

        :param device_type: The device_type of this CreateTransferJobDetails.
        :type: str
        """
        allowed_values = ["DISK", "APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(device_type, allowed_values):
            raise ValueError(
                "Invalid value for `device_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._device_type = device_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateTransferJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateTransferJobDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateTransferJobDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateTransferJobDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateTransferJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateTransferJobDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateTransferJobDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateTransferJobDetails.
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
