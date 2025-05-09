# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201210


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestRoverBundleDetails(object):
    """
    Information required by Object Storage to process a request to copy an object to another bucket.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestRoverBundleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination_compartment_id:
            The value to assign to the destination_compartment_id property of this RequestRoverBundleDetails.
        :type destination_compartment_id: str

        :param destination_bucket_name:
            The value to assign to the destination_bucket_name property of this RequestRoverBundleDetails.
        :type destination_bucket_name: str

        :param bundle_version:
            The value to assign to the bundle_version property of this RequestRoverBundleDetails.
        :type bundle_version: str

        """
        self.swagger_types = {
            'destination_compartment_id': 'str',
            'destination_bucket_name': 'str',
            'bundle_version': 'str'
        }
        self.attribute_map = {
            'destination_compartment_id': 'destinationCompartmentId',
            'destination_bucket_name': 'destinationBucketName',
            'bundle_version': 'bundleVersion'
        }
        self._destination_compartment_id = None
        self._destination_bucket_name = None
        self._bundle_version = None

    @property
    def destination_compartment_id(self):
        """
        **[Required]** Gets the destination_compartment_id of this RequestRoverBundleDetails.
        The compartment OCID of destination compartment that the bundle will be copied to.


        :return: The destination_compartment_id of this RequestRoverBundleDetails.
        :rtype: str
        """
        return self._destination_compartment_id

    @destination_compartment_id.setter
    def destination_compartment_id(self, destination_compartment_id):
        """
        Sets the destination_compartment_id of this RequestRoverBundleDetails.
        The compartment OCID of destination compartment that the bundle will be copied to.


        :param destination_compartment_id: The destination_compartment_id of this RequestRoverBundleDetails.
        :type: str
        """
        self._destination_compartment_id = destination_compartment_id

    @property
    def destination_bucket_name(self):
        """
        **[Required]** Gets the destination_bucket_name of this RequestRoverBundleDetails.
        The destination bucket name the bundle will be copied to.


        :return: The destination_bucket_name of this RequestRoverBundleDetails.
        :rtype: str
        """
        return self._destination_bucket_name

    @destination_bucket_name.setter
    def destination_bucket_name(self, destination_bucket_name):
        """
        Sets the destination_bucket_name of this RequestRoverBundleDetails.
        The destination bucket name the bundle will be copied to.


        :param destination_bucket_name: The destination_bucket_name of this RequestRoverBundleDetails.
        :type: str
        """
        self._destination_bucket_name = destination_bucket_name

    @property
    def bundle_version(self):
        """
        **[Required]** Gets the bundle_version of this RequestRoverBundleDetails.
        The bundle version that customer wants to upgrade to.


        :return: The bundle_version of this RequestRoverBundleDetails.
        :rtype: str
        """
        return self._bundle_version

    @bundle_version.setter
    def bundle_version(self, bundle_version):
        """
        Sets the bundle_version of this RequestRoverBundleDetails.
        The bundle version that customer wants to upgrade to.


        :param bundle_version: The bundle_version of this RequestRoverBundleDetails.
        :type: str
        """
        self._bundle_version = bundle_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
