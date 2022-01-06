# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportStandardTagsDetails(object):
    """
    ImportStandardTagsDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportStandardTagsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ImportStandardTagsDetails.
        :type compartment_id: str

        :param standard_tag_namespace_name:
            The value to assign to the standard_tag_namespace_name property of this ImportStandardTagsDetails.
        :type standard_tag_namespace_name: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'standard_tag_namespace_name': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'standard_tag_namespace_name': 'standardTagNamespaceName'
        }

        self._compartment_id = None
        self._standard_tag_namespace_name = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ImportStandardTagsDetails.
        The OCID of the compartment where the bulk create request is submitted and where the tag namespaces will be created.


        :return: The compartment_id of this ImportStandardTagsDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ImportStandardTagsDetails.
        The OCID of the compartment where the bulk create request is submitted and where the tag namespaces will be created.


        :param compartment_id: The compartment_id of this ImportStandardTagsDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def standard_tag_namespace_name(self):
        """
        **[Required]** Gets the standard_tag_namespace_name of this ImportStandardTagsDetails.
        The name of standard tag namespace that will be imported in bulk


        :return: The standard_tag_namespace_name of this ImportStandardTagsDetails.
        :rtype: str
        """
        return self._standard_tag_namespace_name

    @standard_tag_namespace_name.setter
    def standard_tag_namespace_name(self, standard_tag_namespace_name):
        """
        Sets the standard_tag_namespace_name of this ImportStandardTagsDetails.
        The name of standard tag namespace that will be imported in bulk


        :param standard_tag_namespace_name: The standard_tag_namespace_name of this ImportStandardTagsDetails.
        :type: str
        """
        self._standard_tag_namespace_name = standard_tag_namespace_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
