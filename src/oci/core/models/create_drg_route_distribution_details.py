# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrgRouteDistributionDetails(object):
    """
    Details used to create a route distribution.
    """

    #: A constant which can be used with the distribution_type property of a CreateDrgRouteDistributionDetails.
    #: This constant has a value of "IMPORT"
    DISTRIBUTION_TYPE_IMPORT = "IMPORT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrgRouteDistributionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDrgRouteDistributionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateDrgRouteDistributionDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDrgRouteDistributionDetails.
        :type freeform_tags: dict(str, str)

        :param drg_id:
            The value to assign to the drg_id property of this CreateDrgRouteDistributionDetails.
        :type drg_id: str

        :param distribution_type:
            The value to assign to the distribution_type property of this CreateDrgRouteDistributionDetails.
            Allowed values for this property are: "IMPORT"
        :type distribution_type: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'drg_id': 'str',
            'distribution_type': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'drg_id': 'drgId',
            'distribution_type': 'distributionType'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._drg_id = None
        self._distribution_type = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDrgRouteDistributionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDrgRouteDistributionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDrgRouteDistributionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDrgRouteDistributionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDrgRouteDistributionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateDrgRouteDistributionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrgRouteDistributionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateDrgRouteDistributionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDrgRouteDistributionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDrgRouteDistributionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDrgRouteDistributionDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDrgRouteDistributionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this CreateDrgRouteDistributionDetails.
        The `OCID`__ of the DRG the DRG route table belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The drg_id of this CreateDrgRouteDistributionDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateDrgRouteDistributionDetails.
        The `OCID`__ of the DRG the DRG route table belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param drg_id: The drg_id of this CreateDrgRouteDistributionDetails.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def distribution_type(self):
        """
        **[Required]** Gets the distribution_type of this CreateDrgRouteDistributionDetails.
        Whether this distribution defines how routes get imported into route tables or exported through DRG Attachments

        Allowed values for this property are: "IMPORT"


        :return: The distribution_type of this CreateDrgRouteDistributionDetails.
        :rtype: str
        """
        return self._distribution_type

    @distribution_type.setter
    def distribution_type(self, distribution_type):
        """
        Sets the distribution_type of this CreateDrgRouteDistributionDetails.
        Whether this distribution defines how routes get imported into route tables or exported through DRG Attachments


        :param distribution_type: The distribution_type of this CreateDrgRouteDistributionDetails.
        :type: str
        """
        allowed_values = ["IMPORT"]
        if not value_allowed_none_or_none_sentinel(distribution_type, allowed_values):
            raise ValueError(
                "Invalid value for `distribution_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._distribution_type = distribution_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
