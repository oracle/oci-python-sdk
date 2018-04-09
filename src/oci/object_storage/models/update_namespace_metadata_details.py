# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNamespaceMetadataDetails(object):
    """
    An UpdateNamespaceMetadataDetails is used for update NamespaceMetadata. To be able to upate the NamespaceMetadata, a user
    must have NAMESPACE_UPDATE permission.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNamespaceMetadataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_s3_compartment_id:
            The value to assign to the default_s3_compartment_id property of this UpdateNamespaceMetadataDetails.
        :type default_s3_compartment_id: str

        :param default_swift_compartment_id:
            The value to assign to the default_swift_compartment_id property of this UpdateNamespaceMetadataDetails.
        :type default_swift_compartment_id: str

        """
        self.swagger_types = {
            'default_s3_compartment_id': 'str',
            'default_swift_compartment_id': 'str'
        }

        self.attribute_map = {
            'default_s3_compartment_id': 'defaultS3CompartmentId',
            'default_swift_compartment_id': 'defaultSwiftCompartmentId'
        }

        self._default_s3_compartment_id = None
        self._default_swift_compartment_id = None

    @property
    def default_s3_compartment_id(self):
        """
        Gets the default_s3_compartment_id of this UpdateNamespaceMetadataDetails.
        The update compartment id for an S3 client if this field is set.


        :return: The default_s3_compartment_id of this UpdateNamespaceMetadataDetails.
        :rtype: str
        """
        return self._default_s3_compartment_id

    @default_s3_compartment_id.setter
    def default_s3_compartment_id(self, default_s3_compartment_id):
        """
        Sets the default_s3_compartment_id of this UpdateNamespaceMetadataDetails.
        The update compartment id for an S3 client if this field is set.


        :param default_s3_compartment_id: The default_s3_compartment_id of this UpdateNamespaceMetadataDetails.
        :type: str
        """
        self._default_s3_compartment_id = default_s3_compartment_id

    @property
    def default_swift_compartment_id(self):
        """
        Gets the default_swift_compartment_id of this UpdateNamespaceMetadataDetails.
        The update compartment id for a Swift client if this field is set.


        :return: The default_swift_compartment_id of this UpdateNamespaceMetadataDetails.
        :rtype: str
        """
        return self._default_swift_compartment_id

    @default_swift_compartment_id.setter
    def default_swift_compartment_id(self, default_swift_compartment_id):
        """
        Sets the default_swift_compartment_id of this UpdateNamespaceMetadataDetails.
        The update compartment id for a Swift client if this field is set.


        :param default_swift_compartment_id: The default_swift_compartment_id of this UpdateNamespaceMetadataDetails.
        :type: str
        """
        self._default_swift_compartment_id = default_swift_compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
