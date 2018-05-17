# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIPSecConnectionDetails(object):
    """
    CreateIPSecConnectionDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIPSecConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIPSecConnectionDetails.
        :type compartment_id: str

        :param cpe_id:
            The value to assign to the cpe_id property of this CreateIPSecConnectionDetails.
        :type cpe_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIPSecConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateIPSecConnectionDetails.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this CreateIPSecConnectionDetails.
        :type drg_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIPSecConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param static_routes:
            The value to assign to the static_routes property of this CreateIPSecConnectionDetails.
        :type static_routes: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cpe_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'drg_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'static_routes': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cpe_id': 'cpeId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'freeform_tags': 'freeformTags',
            'static_routes': 'staticRoutes'
        }

        self._compartment_id = None
        self._cpe_id = None
        self._defined_tags = None
        self._display_name = None
        self._drg_id = None
        self._freeform_tags = None
        self._static_routes = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateIPSecConnectionDetails.
        The OCID of the compartment to contain the IPSec connection.


        :return: The compartment_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIPSecConnectionDetails.
        The OCID of the compartment to contain the IPSec connection.


        :param compartment_id: The compartment_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpe_id(self):
        """
        **[Required]** Gets the cpe_id of this CreateIPSecConnectionDetails.
        The OCID of the CPE.


        :return: The cpe_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._cpe_id

    @cpe_id.setter
    def cpe_id(self, cpe_id):
        """
        Sets the cpe_id of this CreateIPSecConnectionDetails.
        The OCID of the CPE.


        :param cpe_id: The cpe_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._cpe_id = cpe_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateIPSecConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateIPSecConnectionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateIPSecConnectionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateIPSecConnectionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateIPSecConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateIPSecConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this CreateIPSecConnectionDetails.
        The OCID of the DRG.


        :return: The drg_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateIPSecConnectionDetails.
        The OCID of the DRG.


        :param drg_id: The drg_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateIPSecConnectionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateIPSecConnectionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateIPSecConnectionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateIPSecConnectionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def static_routes(self):
        """
        **[Required]** Gets the static_routes of this CreateIPSecConnectionDetails.
        Static routes to the CPE. At least one route must be included. The CIDR must not be a
        multicast address or class E address.

        Example: `10.0.1.0/24`


        :return: The static_routes of this CreateIPSecConnectionDetails.
        :rtype: list[str]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this CreateIPSecConnectionDetails.
        Static routes to the CPE. At least one route must be included. The CIDR must not be a
        multicast address or class E address.

        Example: `10.0.1.0/24`


        :param static_routes: The static_routes of this CreateIPSecConnectionDetails.
        :type: list[str]
        """
        self._static_routes = static_routes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
