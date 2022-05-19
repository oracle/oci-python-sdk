# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkUploadTemplate(object):
    """
    The bulk upload template file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkUploadTemplate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param template:
            The value to assign to the template property of this BulkUploadTemplate.
        :type template: str

        """
        self.swagger_types = {
            'template': 'str'
        }

        self.attribute_map = {
            'template': 'template'
        }

        self._template = None

    @property
    def template(self):
        """
        **[Required]** Gets the template of this BulkUploadTemplate.
        The bulk upload template.


        :return: The template of this BulkUploadTemplate.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this BulkUploadTemplate.
        The bulk upload template.


        :param template: The template of this BulkUploadTemplate.
        :type: str
        """
        self._template = template

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
