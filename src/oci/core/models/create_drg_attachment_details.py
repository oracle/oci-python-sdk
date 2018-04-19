# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrgAttachmentDetails(object):
    """
    CreateDrgAttachmentDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrgAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDrgAttachmentDetails.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this CreateDrgAttachmentDetails.
        :type drg_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateDrgAttachmentDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'drg_id': 'str',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'vcn_id': 'vcnId'
        }

        self._display_name = None
        self._drg_id = None
        self._vcn_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrgAttachmentDetails.
        A user-friendly name. Does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this CreateDrgAttachmentDetails.
        The OCID of the DRG.


        :return: The drg_id of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateDrgAttachmentDetails.
        The OCID of the DRG.


        :param drg_id: The drg_id of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateDrgAttachmentDetails.
        The OCID of the VCN.


        :return: The vcn_id of this CreateDrgAttachmentDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateDrgAttachmentDetails.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this CreateDrgAttachmentDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
