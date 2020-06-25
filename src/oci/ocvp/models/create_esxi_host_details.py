# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEsxiHostDetails(object):
    """
    Details of the ESXi host to add to the SDDC.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEsxiHostDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sddc_id:
            The value to assign to the sddc_id property of this CreateEsxiHostDetails.
        :type sddc_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateEsxiHostDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEsxiHostDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEsxiHostDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'sddc_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'sddc_id': 'sddcId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._sddc_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def sddc_id(self):
        """
        **[Required]** Gets the sddc_id of this CreateEsxiHostDetails.
        The `OCID`__ of the SDDC to add the
        ESXi host to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sddc_id of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._sddc_id

    @sddc_id.setter
    def sddc_id(self, sddc_id):
        """
        Sets the sddc_id of this CreateEsxiHostDetails.
        The `OCID`__ of the SDDC to add the
        ESXi host to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sddc_id: The sddc_id of this CreateEsxiHostDetails.
        :type: str
        """
        self._sddc_id = sddc_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateEsxiHostDetails.
        A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        If this attribute is not specified, the SDDC's `instanceDisplayNamePrefix` attribute is used
        to name and incrementally number the ESXi host. For example, if you're creating the fourth
        ESXi host in the SDDC, and `instanceDisplayNamePrefix` is `MySDDC`, the host's display
        name is `MySDDC-4`.


        :return: The display_name of this CreateEsxiHostDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEsxiHostDetails.
        A descriptive name for the ESXi host. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        If this attribute is not specified, the SDDC's `instanceDisplayNamePrefix` attribute is used
        to name and incrementally number the ESXi host. For example, if you're creating the fourth
        ESXi host in the SDDC, and `instanceDisplayNamePrefix` is `MySDDC`, the host's display
        name is `MySDDC-4`.


        :param display_name: The display_name of this CreateEsxiHostDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEsxiHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateEsxiHostDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEsxiHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateEsxiHostDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEsxiHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateEsxiHostDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEsxiHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateEsxiHostDetails.
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
