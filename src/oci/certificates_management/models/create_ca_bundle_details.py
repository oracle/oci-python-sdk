# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCaBundleDetails(object):
    """
    The details of the CA bundle that you want to create.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCaBundleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateCaBundleDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateCaBundleDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCaBundleDetails.
        :type compartment_id: str

        :param ca_bundle_pem:
            The value to assign to the ca_bundle_pem property of this CreateCaBundleDetails.
        :type ca_bundle_pem: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCaBundleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCaBundleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'ca_bundle_pem': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'ca_bundle_pem': 'caBundlePem',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._name = None
        self._description = None
        self._compartment_id = None
        self._ca_bundle_pem = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateCaBundleDetails.
        A user-friendly name for the CA bundle. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :return: The name of this CreateCaBundleDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateCaBundleDetails.
        A user-friendly name for the CA bundle. Names are unique within a compartment. Avoid entering confidential information. Valid characters include uppercase or lowercase letters, numbers, hyphens, underscores, and periods.


        :param name: The name of this CreateCaBundleDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateCaBundleDetails.
        A brief description of the CA bundle.


        :return: The description of this CreateCaBundleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCaBundleDetails.
        A brief description of the CA bundle.


        :param description: The description of this CreateCaBundleDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateCaBundleDetails.
        The OCID of the compartment for the CA bundle.


        :return: The compartment_id of this CreateCaBundleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCaBundleDetails.
        The OCID of the compartment for the CA bundle.


        :param compartment_id: The compartment_id of this CreateCaBundleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ca_bundle_pem(self):
        """
        **[Required]** Gets the ca_bundle_pem of this CreateCaBundleDetails.
        Certificates (in PEM format) to include in the CA bundle.


        :return: The ca_bundle_pem of this CreateCaBundleDetails.
        :rtype: str
        """
        return self._ca_bundle_pem

    @ca_bundle_pem.setter
    def ca_bundle_pem(self, ca_bundle_pem):
        """
        Sets the ca_bundle_pem of this CreateCaBundleDetails.
        Certificates (in PEM format) to include in the CA bundle.


        :param ca_bundle_pem: The ca_bundle_pem of this CreateCaBundleDetails.
        :type: str
        """
        self._ca_bundle_pem = ca_bundle_pem

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateCaBundleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateCaBundleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateCaBundleDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateCaBundleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateCaBundleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateCaBundleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateCaBundleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateCaBundleDetails.
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
