# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateNamespaceMetadataDetails(object):

    def __init__(self):

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
