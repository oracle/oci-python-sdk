# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RenameObjectDetails(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RenameObjectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_name:
            The value to assign to the source_name property of this RenameObjectDetails.
        :type source_name: str

        :param new_name:
            The value to assign to the new_name property of this RenameObjectDetails.
        :type new_name: str

        :param src_obj_if_match_e_tag:
            The value to assign to the src_obj_if_match_e_tag property of this RenameObjectDetails.
        :type src_obj_if_match_e_tag: str

        :param new_obj_if_match_e_tag:
            The value to assign to the new_obj_if_match_e_tag property of this RenameObjectDetails.
        :type new_obj_if_match_e_tag: str

        :param new_obj_if_none_match_e_tag:
            The value to assign to the new_obj_if_none_match_e_tag property of this RenameObjectDetails.
        :type new_obj_if_none_match_e_tag: str

        """
        self.swagger_types = {
            'source_name': 'str',
            'new_name': 'str',
            'src_obj_if_match_e_tag': 'str',
            'new_obj_if_match_e_tag': 'str',
            'new_obj_if_none_match_e_tag': 'str'
        }

        self.attribute_map = {
            'source_name': 'sourceName',
            'new_name': 'newName',
            'src_obj_if_match_e_tag': 'srcObjIfMatchETag',
            'new_obj_if_match_e_tag': 'newObjIfMatchETag',
            'new_obj_if_none_match_e_tag': 'newObjIfNoneMatchETag'
        }

        self._source_name = None
        self._new_name = None
        self._src_obj_if_match_e_tag = None
        self._new_obj_if_match_e_tag = None
        self._new_obj_if_none_match_e_tag = None

    @property
    def source_name(self):
        """
        **[Required]** Gets the source_name of this RenameObjectDetails.
        The name of the source object to be renamed.


        :return: The source_name of this RenameObjectDetails.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this RenameObjectDetails.
        The name of the source object to be renamed.


        :param source_name: The source_name of this RenameObjectDetails.
        :type: str
        """
        self._source_name = source_name

    @property
    def new_name(self):
        """
        **[Required]** Gets the new_name of this RenameObjectDetails.
        The new name of the source object.


        :return: The new_name of this RenameObjectDetails.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """
        Sets the new_name of this RenameObjectDetails.
        The new name of the source object.


        :param new_name: The new_name of this RenameObjectDetails.
        :type: str
        """
        self._new_name = new_name

    @property
    def src_obj_if_match_e_tag(self):
        """
        Gets the src_obj_if_match_e_tag of this RenameObjectDetails.
        The if-match entity tag (ETag) of the source object.


        :return: The src_obj_if_match_e_tag of this RenameObjectDetails.
        :rtype: str
        """
        return self._src_obj_if_match_e_tag

    @src_obj_if_match_e_tag.setter
    def src_obj_if_match_e_tag(self, src_obj_if_match_e_tag):
        """
        Sets the src_obj_if_match_e_tag of this RenameObjectDetails.
        The if-match entity tag (ETag) of the source object.


        :param src_obj_if_match_e_tag: The src_obj_if_match_e_tag of this RenameObjectDetails.
        :type: str
        """
        self._src_obj_if_match_e_tag = src_obj_if_match_e_tag

    @property
    def new_obj_if_match_e_tag(self):
        """
        Gets the new_obj_if_match_e_tag of this RenameObjectDetails.
        The if-match entity tag (ETag) of the new object.


        :return: The new_obj_if_match_e_tag of this RenameObjectDetails.
        :rtype: str
        """
        return self._new_obj_if_match_e_tag

    @new_obj_if_match_e_tag.setter
    def new_obj_if_match_e_tag(self, new_obj_if_match_e_tag):
        """
        Sets the new_obj_if_match_e_tag of this RenameObjectDetails.
        The if-match entity tag (ETag) of the new object.


        :param new_obj_if_match_e_tag: The new_obj_if_match_e_tag of this RenameObjectDetails.
        :type: str
        """
        self._new_obj_if_match_e_tag = new_obj_if_match_e_tag

    @property
    def new_obj_if_none_match_e_tag(self):
        """
        Gets the new_obj_if_none_match_e_tag of this RenameObjectDetails.
        The if-none-match entity tag (ETag) of the new object.


        :return: The new_obj_if_none_match_e_tag of this RenameObjectDetails.
        :rtype: str
        """
        return self._new_obj_if_none_match_e_tag

    @new_obj_if_none_match_e_tag.setter
    def new_obj_if_none_match_e_tag(self, new_obj_if_none_match_e_tag):
        """
        Sets the new_obj_if_none_match_e_tag of this RenameObjectDetails.
        The if-none-match entity tag (ETag) of the new object.


        :param new_obj_if_none_match_e_tag: The new_obj_if_none_match_e_tag of this RenameObjectDetails.
        :type: str
        """
        self._new_obj_if_none_match_e_tag = new_obj_if_none_match_e_tag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
