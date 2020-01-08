# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportKeyVersionDetails(object):
    """
    ImportKeyVersionDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportKeyVersionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this ImportKeyVersionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ImportKeyVersionDetails.
        :type freeform_tags: dict(str, str)

        :param wrapped_import_key:
            The value to assign to the wrapped_import_key property of this ImportKeyVersionDetails.
        :type wrapped_import_key: WrappedImportKey

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'wrapped_import_key': 'WrappedImportKey'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'wrapped_import_key': 'wrappedImportKey'
        }

        self._defined_tags = None
        self._freeform_tags = None
        self._wrapped_import_key = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ImportKeyVersionDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :return: The defined_tags of this ImportKeyVersionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ImportKeyVersionDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"foo-value\"}}`


        :param defined_tags: The defined_tags of this ImportKeyVersionDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ImportKeyVersionDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ImportKeyVersionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ImportKeyVersionDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ImportKeyVersionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def wrapped_import_key(self):
        """
        **[Required]** Gets the wrapped_import_key of this ImportKeyVersionDetails.

        :return: The wrapped_import_key of this ImportKeyVersionDetails.
        :rtype: WrappedImportKey
        """
        return self._wrapped_import_key

    @wrapped_import_key.setter
    def wrapped_import_key(self, wrapped_import_key):
        """
        Sets the wrapped_import_key of this ImportKeyVersionDetails.

        :param wrapped_import_key: The wrapped_import_key of this ImportKeyVersionDetails.
        :type: WrappedImportKey
        """
        self._wrapped_import_key = wrapped_import_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
