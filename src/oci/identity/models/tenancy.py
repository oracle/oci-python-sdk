# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tenancy(object):
    """
    The root compartment that contains all of your organization's compartments and other
    Oracle Cloud Infrastructure cloud resources. When you sign up for Oracle Cloud Infrastructure,
    Oracle creates a tenancy for your company, which is a secure and isolated partition
    where you can create, organize, and administer your cloud resources.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Tenancy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Tenancy.
        :type id: str

        :param name:
            The value to assign to the name property of this Tenancy.
        :type name: str

        :param description:
            The value to assign to the description property of this Tenancy.
        :type description: str

        :param home_region_key:
            The value to assign to the home_region_key property of this Tenancy.
        :type home_region_key: str

        :param upi_idcs_compatibility_layer_endpoint:
            The value to assign to the upi_idcs_compatibility_layer_endpoint property of this Tenancy.
        :type upi_idcs_compatibility_layer_endpoint: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Tenancy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Tenancy.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'home_region_key': 'str',
            'upi_idcs_compatibility_layer_endpoint': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'home_region_key': 'homeRegionKey',
            'upi_idcs_compatibility_layer_endpoint': 'upiIdcsCompatibilityLayerEndpoint',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._name = None
        self._description = None
        self._home_region_key = None
        self._upi_idcs_compatibility_layer_endpoint = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this Tenancy.
        The OCID of the tenancy.


        :return: The id of this Tenancy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tenancy.
        The OCID of the tenancy.


        :param id: The id of this Tenancy.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Tenancy.
        The name of the tenancy.


        :return: The name of this Tenancy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tenancy.
        The name of the tenancy.


        :param name: The name of this Tenancy.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Tenancy.
        The description of the tenancy.


        :return: The description of this Tenancy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Tenancy.
        The description of the tenancy.


        :param description: The description of this Tenancy.
        :type: str
        """
        self._description = description

    @property
    def home_region_key(self):
        """
        Gets the home_region_key of this Tenancy.
        The region key for the tenancy's home region. For the full list of supported regions, see
        `Regions and Availability Domains`__.

        Example: `PHX`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The home_region_key of this Tenancy.
        :rtype: str
        """
        return self._home_region_key

    @home_region_key.setter
    def home_region_key(self, home_region_key):
        """
        Sets the home_region_key of this Tenancy.
        The region key for the tenancy's home region. For the full list of supported regions, see
        `Regions and Availability Domains`__.

        Example: `PHX`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :param home_region_key: The home_region_key of this Tenancy.
        :type: str
        """
        self._home_region_key = home_region_key

    @property
    def upi_idcs_compatibility_layer_endpoint(self):
        """
        Gets the upi_idcs_compatibility_layer_endpoint of this Tenancy.
        Url which refers to the UPI IDCS compatibility layer endpoint configured for this Tenant's home region.


        :return: The upi_idcs_compatibility_layer_endpoint of this Tenancy.
        :rtype: str
        """
        return self._upi_idcs_compatibility_layer_endpoint

    @upi_idcs_compatibility_layer_endpoint.setter
    def upi_idcs_compatibility_layer_endpoint(self, upi_idcs_compatibility_layer_endpoint):
        """
        Sets the upi_idcs_compatibility_layer_endpoint of this Tenancy.
        Url which refers to the UPI IDCS compatibility layer endpoint configured for this Tenant's home region.


        :param upi_idcs_compatibility_layer_endpoint: The upi_idcs_compatibility_layer_endpoint of this Tenancy.
        :type: str
        """
        self._upi_idcs_compatibility_layer_endpoint = upi_idcs_compatibility_layer_endpoint

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Tenancy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Tenancy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Tenancy.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Tenancy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Tenancy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Tenancy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Tenancy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Tenancy.
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
