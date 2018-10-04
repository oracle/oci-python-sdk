# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamespaceMetadata(object):
    """
    A NamespaceMetadata is a map for storing namespace and defaultS3CompartmentId, defaultSwiftCompartmentId.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NamespaceMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param namespace:
            The value to assign to the namespace property of this NamespaceMetadata.
        :type namespace: str

        :param default_s3_compartment_id:
            The value to assign to the default_s3_compartment_id property of this NamespaceMetadata.
        :type default_s3_compartment_id: str

        :param default_swift_compartment_id:
            The value to assign to the default_swift_compartment_id property of this NamespaceMetadata.
        :type default_swift_compartment_id: str

        """
        self.swagger_types = {
            'namespace': 'str',
            'default_s3_compartment_id': 'str',
            'default_swift_compartment_id': 'str'
        }

        self.attribute_map = {
            'namespace': 'namespace',
            'default_s3_compartment_id': 'defaultS3CompartmentId',
            'default_swift_compartment_id': 'defaultSwiftCompartmentId'
        }

        self._namespace = None
        self._default_s3_compartment_id = None
        self._default_swift_compartment_id = None

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this NamespaceMetadata.
        The namespace to which the metadata belongs.


        :return: The namespace of this NamespaceMetadata.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this NamespaceMetadata.
        The namespace to which the metadata belongs.


        :param namespace: The namespace of this NamespaceMetadata.
        :type: str
        """
        self._namespace = namespace

    @property
    def default_s3_compartment_id(self):
        """
        **[Required]** Gets the default_s3_compartment_id of this NamespaceMetadata.
        The default compartment ID for an S3 client.


        :return: The default_s3_compartment_id of this NamespaceMetadata.
        :rtype: str
        """
        return self._default_s3_compartment_id

    @default_s3_compartment_id.setter
    def default_s3_compartment_id(self, default_s3_compartment_id):
        """
        Sets the default_s3_compartment_id of this NamespaceMetadata.
        The default compartment ID for an S3 client.


        :param default_s3_compartment_id: The default_s3_compartment_id of this NamespaceMetadata.
        :type: str
        """
        self._default_s3_compartment_id = default_s3_compartment_id

    @property
    def default_swift_compartment_id(self):
        """
        **[Required]** Gets the default_swift_compartment_id of this NamespaceMetadata.
        The default compartment ID for a Swift client.


        :return: The default_swift_compartment_id of this NamespaceMetadata.
        :rtype: str
        """
        return self._default_swift_compartment_id

    @default_swift_compartment_id.setter
    def default_swift_compartment_id(self, default_swift_compartment_id):
        """
        Sets the default_swift_compartment_id of this NamespaceMetadata.
        The default compartment ID for a Swift client.


        :param default_swift_compartment_id: The default_swift_compartment_id of this NamespaceMetadata.
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
