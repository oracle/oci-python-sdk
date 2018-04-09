# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceConsoleConnectionDetails(object):
    """
    The details for creating a instance console connection.
    The instance console connection is created in the same compartment as the instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceConsoleConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateInstanceConsoleConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateInstanceConsoleConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param instance_id:
            The value to assign to the instance_id property of this CreateInstanceConsoleConnectionDetails.
        :type instance_id: str

        :param public_key:
            The value to assign to the public_key property of this CreateInstanceConsoleConnectionDetails.
        :type public_key: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'instance_id': 'str',
            'public_key': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'instance_id': 'instanceId',
            'public_key': 'publicKey'
        }

        self._defined_tags = None
        self._freeform_tags = None
        self._instance_id = None
        self._public_key = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateInstanceConsoleConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateInstanceConsoleConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateInstanceConsoleConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateInstanceConsoleConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateInstanceConsoleConnectionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateInstanceConsoleConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateInstanceConsoleConnectionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateInstanceConsoleConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this CreateInstanceConsoleConnectionDetails.
        The OCID of the instance to create the console connection to.


        :return: The instance_id of this CreateInstanceConsoleConnectionDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this CreateInstanceConsoleConnectionDetails.
        The OCID of the instance to create the console connection to.


        :param instance_id: The instance_id of this CreateInstanceConsoleConnectionDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this CreateInstanceConsoleConnectionDetails.
        The SSH public key used to authenticate the console connection.


        :return: The public_key of this CreateInstanceConsoleConnectionDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this CreateInstanceConsoleConnectionDetails.
        The SSH public key used to authenticate the console connection.


        :param public_key: The public_key of this CreateInstanceConsoleConnectionDetails.
        :type: str
        """
        self._public_key = public_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
