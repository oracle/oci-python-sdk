# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOdaInstanceAttachmentDetails(object):
    """
    ODA attachment details to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOdaInstanceAttachmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachment_metadata:
            The value to assign to the attachment_metadata property of this UpdateOdaInstanceAttachmentDetails.
        :type attachment_metadata: str

        :param restricted_operations:
            The value to assign to the restricted_operations property of this UpdateOdaInstanceAttachmentDetails.
        :type restricted_operations: list[str]

        :param owner:
            The value to assign to the owner property of this UpdateOdaInstanceAttachmentDetails.
        :type owner: oci.oda.models.OdaInstanceAttachmentOwner

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOdaInstanceAttachmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOdaInstanceAttachmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'attachment_metadata': 'str',
            'restricted_operations': 'list[str]',
            'owner': 'OdaInstanceAttachmentOwner',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'attachment_metadata': 'attachmentMetadata',
            'restricted_operations': 'restrictedOperations',
            'owner': 'owner',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._attachment_metadata = None
        self._restricted_operations = None
        self._owner = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def attachment_metadata(self):
        """
        **[Required]** Gets the attachment_metadata of this UpdateOdaInstanceAttachmentDetails.
        Attachment specific metadata. Defined by the target service.


        :return: The attachment_metadata of this UpdateOdaInstanceAttachmentDetails.
        :rtype: str
        """
        return self._attachment_metadata

    @attachment_metadata.setter
    def attachment_metadata(self, attachment_metadata):
        """
        Sets the attachment_metadata of this UpdateOdaInstanceAttachmentDetails.
        Attachment specific metadata. Defined by the target service.


        :param attachment_metadata: The attachment_metadata of this UpdateOdaInstanceAttachmentDetails.
        :type: str
        """
        self._attachment_metadata = attachment_metadata

    @property
    def restricted_operations(self):
        """
        **[Required]** Gets the restricted_operations of this UpdateOdaInstanceAttachmentDetails.
        List of operations that are restricted while this instance is attached.


        :return: The restricted_operations of this UpdateOdaInstanceAttachmentDetails.
        :rtype: list[str]
        """
        return self._restricted_operations

    @restricted_operations.setter
    def restricted_operations(self, restricted_operations):
        """
        Sets the restricted_operations of this UpdateOdaInstanceAttachmentDetails.
        List of operations that are restricted while this instance is attached.


        :param restricted_operations: The restricted_operations of this UpdateOdaInstanceAttachmentDetails.
        :type: list[str]
        """
        self._restricted_operations = restricted_operations

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this UpdateOdaInstanceAttachmentDetails.

        :return: The owner of this UpdateOdaInstanceAttachmentDetails.
        :rtype: oci.oda.models.OdaInstanceAttachmentOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this UpdateOdaInstanceAttachmentDetails.

        :param owner: The owner of this UpdateOdaInstanceAttachmentDetails.
        :type: oci.oda.models.OdaInstanceAttachmentOwner
        """
        self._owner = owner

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOdaInstanceAttachmentDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOdaInstanceAttachmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOdaInstanceAttachmentDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOdaInstanceAttachmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOdaInstanceAttachmentDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOdaInstanceAttachmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOdaInstanceAttachmentDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOdaInstanceAttachmentDetails.
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
