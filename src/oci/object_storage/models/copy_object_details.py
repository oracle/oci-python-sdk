# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CopyObjectDetails(object):
    """
    The parameters required by Object Storage to process a request to copy an object to another bucket.

    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CopyObjectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_object_name:
            The value to assign to the source_object_name property of this CopyObjectDetails.
        :type source_object_name: str

        :param source_object_if_match_e_tag:
            The value to assign to the source_object_if_match_e_tag property of this CopyObjectDetails.
        :type source_object_if_match_e_tag: str

        :param source_version_id:
            The value to assign to the source_version_id property of this CopyObjectDetails.
        :type source_version_id: str

        :param destination_region:
            The value to assign to the destination_region property of this CopyObjectDetails.
        :type destination_region: str

        :param destination_namespace:
            The value to assign to the destination_namespace property of this CopyObjectDetails.
        :type destination_namespace: str

        :param destination_bucket:
            The value to assign to the destination_bucket property of this CopyObjectDetails.
        :type destination_bucket: str

        :param destination_object_name:
            The value to assign to the destination_object_name property of this CopyObjectDetails.
        :type destination_object_name: str

        :param destination_object_if_match_e_tag:
            The value to assign to the destination_object_if_match_e_tag property of this CopyObjectDetails.
        :type destination_object_if_match_e_tag: str

        :param destination_object_if_none_match_e_tag:
            The value to assign to the destination_object_if_none_match_e_tag property of this CopyObjectDetails.
        :type destination_object_if_none_match_e_tag: str

        :param destination_object_metadata:
            The value to assign to the destination_object_metadata property of this CopyObjectDetails.
        :type destination_object_metadata: dict(str, str)

        """
        self.swagger_types = {
            'source_object_name': 'str',
            'source_object_if_match_e_tag': 'str',
            'source_version_id': 'str',
            'destination_region': 'str',
            'destination_namespace': 'str',
            'destination_bucket': 'str',
            'destination_object_name': 'str',
            'destination_object_if_match_e_tag': 'str',
            'destination_object_if_none_match_e_tag': 'str',
            'destination_object_metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'source_object_name': 'sourceObjectName',
            'source_object_if_match_e_tag': 'sourceObjectIfMatchETag',
            'source_version_id': 'sourceVersionId',
            'destination_region': 'destinationRegion',
            'destination_namespace': 'destinationNamespace',
            'destination_bucket': 'destinationBucket',
            'destination_object_name': 'destinationObjectName',
            'destination_object_if_match_e_tag': 'destinationObjectIfMatchETag',
            'destination_object_if_none_match_e_tag': 'destinationObjectIfNoneMatchETag',
            'destination_object_metadata': 'destinationObjectMetadata'
        }

        self._source_object_name = None
        self._source_object_if_match_e_tag = None
        self._source_version_id = None
        self._destination_region = None
        self._destination_namespace = None
        self._destination_bucket = None
        self._destination_object_name = None
        self._destination_object_if_match_e_tag = None
        self._destination_object_if_none_match_e_tag = None
        self._destination_object_metadata = None

    @property
    def source_object_name(self):
        """
        **[Required]** Gets the source_object_name of this CopyObjectDetails.
        The name of the object to be copied.


        :return: The source_object_name of this CopyObjectDetails.
        :rtype: str
        """
        return self._source_object_name

    @source_object_name.setter
    def source_object_name(self, source_object_name):
        """
        Sets the source_object_name of this CopyObjectDetails.
        The name of the object to be copied.


        :param source_object_name: The source_object_name of this CopyObjectDetails.
        :type: str
        """
        self._source_object_name = source_object_name

    @property
    def source_object_if_match_e_tag(self):
        """
        Gets the source_object_if_match_e_tag of this CopyObjectDetails.
        The entity tag (ETag) to match against that of the source object. Used to confirm that the source object
        with a given name is the version of that object storing a specified ETag.


        :return: The source_object_if_match_e_tag of this CopyObjectDetails.
        :rtype: str
        """
        return self._source_object_if_match_e_tag

    @source_object_if_match_e_tag.setter
    def source_object_if_match_e_tag(self, source_object_if_match_e_tag):
        """
        Sets the source_object_if_match_e_tag of this CopyObjectDetails.
        The entity tag (ETag) to match against that of the source object. Used to confirm that the source object
        with a given name is the version of that object storing a specified ETag.


        :param source_object_if_match_e_tag: The source_object_if_match_e_tag of this CopyObjectDetails.
        :type: str
        """
        self._source_object_if_match_e_tag = source_object_if_match_e_tag

    @property
    def source_version_id(self):
        """
        Gets the source_version_id of this CopyObjectDetails.
        VersionId of the object to copy. If not provided then current version is copied by default.


        :return: The source_version_id of this CopyObjectDetails.
        :rtype: str
        """
        return self._source_version_id

    @source_version_id.setter
    def source_version_id(self, source_version_id):
        """
        Sets the source_version_id of this CopyObjectDetails.
        VersionId of the object to copy. If not provided then current version is copied by default.


        :param source_version_id: The source_version_id of this CopyObjectDetails.
        :type: str
        """
        self._source_version_id = source_version_id

    @property
    def destination_region(self):
        """
        **[Required]** Gets the destination_region of this CopyObjectDetails.
        The destination region the object will be copied to, for example \"us-ashburn-1\".


        :return: The destination_region of this CopyObjectDetails.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """
        Sets the destination_region of this CopyObjectDetails.
        The destination region the object will be copied to, for example \"us-ashburn-1\".


        :param destination_region: The destination_region of this CopyObjectDetails.
        :type: str
        """
        self._destination_region = destination_region

    @property
    def destination_namespace(self):
        """
        **[Required]** Gets the destination_namespace of this CopyObjectDetails.
        The destination Object Storage namespace the object will be copied to.


        :return: The destination_namespace of this CopyObjectDetails.
        :rtype: str
        """
        return self._destination_namespace

    @destination_namespace.setter
    def destination_namespace(self, destination_namespace):
        """
        Sets the destination_namespace of this CopyObjectDetails.
        The destination Object Storage namespace the object will be copied to.


        :param destination_namespace: The destination_namespace of this CopyObjectDetails.
        :type: str
        """
        self._destination_namespace = destination_namespace

    @property
    def destination_bucket(self):
        """
        **[Required]** Gets the destination_bucket of this CopyObjectDetails.
        The destination bucket the object will be copied to.


        :return: The destination_bucket of this CopyObjectDetails.
        :rtype: str
        """
        return self._destination_bucket

    @destination_bucket.setter
    def destination_bucket(self, destination_bucket):
        """
        Sets the destination_bucket of this CopyObjectDetails.
        The destination bucket the object will be copied to.


        :param destination_bucket: The destination_bucket of this CopyObjectDetails.
        :type: str
        """
        self._destination_bucket = destination_bucket

    @property
    def destination_object_name(self):
        """
        **[Required]** Gets the destination_object_name of this CopyObjectDetails.
        The name of the destination object resulting from the copy operation.


        :return: The destination_object_name of this CopyObjectDetails.
        :rtype: str
        """
        return self._destination_object_name

    @destination_object_name.setter
    def destination_object_name(self, destination_object_name):
        """
        Sets the destination_object_name of this CopyObjectDetails.
        The name of the destination object resulting from the copy operation.


        :param destination_object_name: The destination_object_name of this CopyObjectDetails.
        :type: str
        """
        self._destination_object_name = destination_object_name

    @property
    def destination_object_if_match_e_tag(self):
        """
        Gets the destination_object_if_match_e_tag of this CopyObjectDetails.
        The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten).
        Used to confirm that the destination object stored under a given name is the version of that object
        storing a specified entity tag.


        :return: The destination_object_if_match_e_tag of this CopyObjectDetails.
        :rtype: str
        """
        return self._destination_object_if_match_e_tag

    @destination_object_if_match_e_tag.setter
    def destination_object_if_match_e_tag(self, destination_object_if_match_e_tag):
        """
        Sets the destination_object_if_match_e_tag of this CopyObjectDetails.
        The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten).
        Used to confirm that the destination object stored under a given name is the version of that object
        storing a specified entity tag.


        :param destination_object_if_match_e_tag: The destination_object_if_match_e_tag of this CopyObjectDetails.
        :type: str
        """
        self._destination_object_if_match_e_tag = destination_object_if_match_e_tag

    @property
    def destination_object_if_none_match_e_tag(self):
        """
        Gets the destination_object_if_none_match_e_tag of this CopyObjectDetails.
        The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail
        if the object already exists in the destination bucket.


        :return: The destination_object_if_none_match_e_tag of this CopyObjectDetails.
        :rtype: str
        """
        return self._destination_object_if_none_match_e_tag

    @destination_object_if_none_match_e_tag.setter
    def destination_object_if_none_match_e_tag(self, destination_object_if_none_match_e_tag):
        """
        Sets the destination_object_if_none_match_e_tag of this CopyObjectDetails.
        The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail
        if the object already exists in the destination bucket.


        :param destination_object_if_none_match_e_tag: The destination_object_if_none_match_e_tag of this CopyObjectDetails.
        :type: str
        """
        self._destination_object_if_none_match_e_tag = destination_object_if_none_match_e_tag

    @property
    def destination_object_metadata(self):
        """
        Gets the destination_object_metadata of this CopyObjectDetails.
        Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in
        \"opc-meta-*\" format. Avoid entering confidential information. Metadata key-value pairs entered
        in this field are assigned to the destination object. If you enter no metadata values, the destination
        object will inherit any existing metadata values associated with the source object.


        :return: The destination_object_metadata of this CopyObjectDetails.
        :rtype: dict(str, str)
        """
        return self._destination_object_metadata

    @destination_object_metadata.setter
    def destination_object_metadata(self, destination_object_metadata):
        """
        Sets the destination_object_metadata of this CopyObjectDetails.
        Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in
        \"opc-meta-*\" format. Avoid entering confidential information. Metadata key-value pairs entered
        in this field are assigned to the destination object. If you enter no metadata values, the destination
        object will inherit any existing metadata values associated with the source object.


        :param destination_object_metadata: The destination_object_metadata of this CopyObjectDetails.
        :type: dict(str, str)
        """
        self._destination_object_metadata = destination_object_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
