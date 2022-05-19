# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateImportedPackageDetails(object):
    """
    Payload for creating an imported package
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateImportedPackageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_package_id:
            The value to assign to the current_package_id property of this CreateImportedPackageDetails.
        :type current_package_id: str

        :param parameter_values:
            The value to assign to the parameter_values property of this CreateImportedPackageDetails.
        :type parameter_values: dict(str, str)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateImportedPackageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateImportedPackageDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'current_package_id': 'str',
            'parameter_values': 'dict(str, str)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'current_package_id': 'currentPackageId',
            'parameter_values': 'parameterValues',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._current_package_id = None
        self._parameter_values = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def current_package_id(self):
        """
        **[Required]** Gets the current_package_id of this CreateImportedPackageDetails.
        ID of the package to import.


        :return: The current_package_id of this CreateImportedPackageDetails.
        :rtype: str
        """
        return self._current_package_id

    @current_package_id.setter
    def current_package_id(self, current_package_id):
        """
        Sets the current_package_id of this CreateImportedPackageDetails.
        ID of the package to import.


        :param current_package_id: The current_package_id of this CreateImportedPackageDetails.
        :type: str
        """
        self._current_package_id = current_package_id

    @property
    def parameter_values(self):
        """
        Gets the parameter_values of this CreateImportedPackageDetails.
        A list of parameter values to use when importing the given package. Must match those defined in the import contract.


        :return: The parameter_values of this CreateImportedPackageDetails.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        """
        Sets the parameter_values of this CreateImportedPackageDetails.
        A list of parameter values to use when importing the given package. Must match those defined in the import contract.


        :param parameter_values: The parameter_values of this CreateImportedPackageDetails.
        :type: dict(str, str)
        """
        self._parameter_values = parameter_values

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateImportedPackageDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateImportedPackageDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateImportedPackageDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateImportedPackageDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateImportedPackageDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateImportedPackageDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateImportedPackageDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateImportedPackageDetails.
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
