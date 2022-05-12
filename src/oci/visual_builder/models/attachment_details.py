# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachmentDetails(object):
    """
    Description of an attachments for this instance
    """

    #: A constant which can be used with the target_role property of a AttachmentDetails.
    #: This constant has a value of "PARENT"
    TARGET_ROLE_PARENT = "PARENT"

    #: A constant which can be used with the target_role property of a AttachmentDetails.
    #: This constant has a value of "CHILD"
    TARGET_ROLE_CHILD = "CHILD"

    def __init__(self, **kwargs):
        """
        Initializes a new AttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_role:
            The value to assign to the target_role property of this AttachmentDetails.
            Allowed values for this property are: "PARENT", "CHILD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target_role: str

        :param is_implicit:
            The value to assign to the is_implicit property of this AttachmentDetails.
        :type is_implicit: bool

        :param target_id:
            The value to assign to the target_id property of this AttachmentDetails.
        :type target_id: str

        :param target_instance_url:
            The value to assign to the target_instance_url property of this AttachmentDetails.
        :type target_instance_url: str

        :param target_service_type:
            The value to assign to the target_service_type property of this AttachmentDetails.
        :type target_service_type: str

        """
        self.swagger_types = {
            'target_role': 'str',
            'is_implicit': 'bool',
            'target_id': 'str',
            'target_instance_url': 'str',
            'target_service_type': 'str'
        }

        self.attribute_map = {
            'target_role': 'targetRole',
            'is_implicit': 'isImplicit',
            'target_id': 'targetId',
            'target_instance_url': 'targetInstanceUrl',
            'target_service_type': 'targetServiceType'
        }

        self._target_role = None
        self._is_implicit = None
        self._target_id = None
        self._target_instance_url = None
        self._target_service_type = None

    @property
    def target_role(self):
        """
        **[Required]** Gets the target_role of this AttachmentDetails.
        The role of the target attachment.
           * `PARENT` - The target instance is the parent of this attachment.
           * `CHILD` - The target instance is the child of this attachment.

        Allowed values for this property are: "PARENT", "CHILD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target_role of this AttachmentDetails.
        :rtype: str
        """
        return self._target_role

    @target_role.setter
    def target_role(self, target_role):
        """
        Sets the target_role of this AttachmentDetails.
        The role of the target attachment.
           * `PARENT` - The target instance is the parent of this attachment.
           * `CHILD` - The target instance is the child of this attachment.


        :param target_role: The target_role of this AttachmentDetails.
        :type: str
        """
        allowed_values = ["PARENT", "CHILD"]
        if not value_allowed_none_or_none_sentinel(target_role, allowed_values):
            target_role = 'UNKNOWN_ENUM_VALUE'
        self._target_role = target_role

    @property
    def is_implicit(self):
        """
        **[Required]** Gets the is_implicit of this AttachmentDetails.
        * If role == `PARENT`, the attached instance was created by this service instance
        * If role == `CHILD`, this instance was created from attached instance on behalf of a user


        :return: The is_implicit of this AttachmentDetails.
        :rtype: bool
        """
        return self._is_implicit

    @is_implicit.setter
    def is_implicit(self, is_implicit):
        """
        Sets the is_implicit of this AttachmentDetails.
        * If role == `PARENT`, the attached instance was created by this service instance
        * If role == `CHILD`, this instance was created from attached instance on behalf of a user


        :param is_implicit: The is_implicit of this AttachmentDetails.
        :type: bool
        """
        self._is_implicit = is_implicit

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this AttachmentDetails.
        The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.


        :return: The target_id of this AttachmentDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AttachmentDetails.
        The OCID of the target instance (which could be any other OCI PaaS/SaaS resource), to which this instance is attached.


        :param target_id: The target_id of this AttachmentDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_instance_url(self):
        """
        **[Required]** Gets the target_instance_url of this AttachmentDetails.
        The dataplane instance URL of the attached instance


        :return: The target_instance_url of this AttachmentDetails.
        :rtype: str
        """
        return self._target_instance_url

    @target_instance_url.setter
    def target_instance_url(self, target_instance_url):
        """
        Sets the target_instance_url of this AttachmentDetails.
        The dataplane instance URL of the attached instance


        :param target_instance_url: The target_instance_url of this AttachmentDetails.
        :type: str
        """
        self._target_instance_url = target_instance_url

    @property
    def target_service_type(self):
        """
        **[Required]** Gets the target_service_type of this AttachmentDetails.
        The type of the target instance, such as \"FUSION\".


        :return: The target_service_type of this AttachmentDetails.
        :rtype: str
        """
        return self._target_service_type

    @target_service_type.setter
    def target_service_type(self, target_service_type):
        """
        Sets the target_service_type of this AttachmentDetails.
        The type of the target instance, such as \"FUSION\".


        :param target_service_type: The target_service_type of this AttachmentDetails.
        :type: str
        """
        self._target_service_type = target_service_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
