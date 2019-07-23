# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstanceConfigurationBase(object):
    """
    An instance configuration that can be used to launch
    """

    #: A constant which can be used with the source property of a CreateInstanceConfigurationBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a CreateInstanceConfigurationBase.
    #: This constant has a value of "INSTANCE"
    SOURCE_INSTANCE = "INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstanceConfigurationBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.CreateInstanceConfigurationDetails`
        * :class:`~oci.core.models.CreateInstanceConfigurationFromInstanceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateInstanceConfigurationBase.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateInstanceConfigurationBase.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateInstanceConfigurationBase.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateInstanceConfigurationBase.
        :type freeform_tags: dict(str, str)

        :param source:
            The value to assign to the source property of this CreateInstanceConfigurationBase.
            Allowed values for this property are: "NONE", "INSTANCE"
        :type source: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'source': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'source': 'source'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'NONE':
            return 'CreateInstanceConfigurationDetails'

        if type == 'INSTANCE':
            return 'CreateInstanceConfigurationFromInstanceDetails'
        else:
            return 'CreateInstanceConfigurationBase'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateInstanceConfigurationBase.
        The OCID of the compartment containing the instance configuration.


        :return: The compartment_id of this CreateInstanceConfigurationBase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateInstanceConfigurationBase.
        The OCID of the compartment containing the instance configuration.


        :param compartment_id: The compartment_id of this CreateInstanceConfigurationBase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateInstanceConfigurationBase.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateInstanceConfigurationBase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateInstanceConfigurationBase.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateInstanceConfigurationBase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateInstanceConfigurationBase.
        A user-friendly name for the instance configuration


        :return: The display_name of this CreateInstanceConfigurationBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateInstanceConfigurationBase.
        A user-friendly name for the instance configuration


        :param display_name: The display_name of this CreateInstanceConfigurationBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateInstanceConfigurationBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateInstanceConfigurationBase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateInstanceConfigurationBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateInstanceConfigurationBase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def source(self):
        """
        Gets the source of this CreateInstanceConfigurationBase.
        The source of the instance configuration:
        NONE for creating a new instance configuration from the API input. INSTANCE for creating a new instance
        configuration from an existing instance. The default is NONE.

        Allowed values for this property are: "NONE", "INSTANCE"


        :return: The source of this CreateInstanceConfigurationBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateInstanceConfigurationBase.
        The source of the instance configuration:
        NONE for creating a new instance configuration from the API input. INSTANCE for creating a new instance
        configuration from an existing instance. The default is NONE.


        :param source: The source of this CreateInstanceConfigurationBase.
        :type: str
        """
        allowed_values = ["NONE", "INSTANCE"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
