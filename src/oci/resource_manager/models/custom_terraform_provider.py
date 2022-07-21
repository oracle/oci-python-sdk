# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomTerraformProvider(object):
    """
    Location information about custom Terraform providers for a stack.
    For more information, see `Custom Providers`__.
    Note: Older stacks that use Terraform version 12.x or 13.x must be explicitly updated to use Terraform Registry (`isThirdPartyProviderExperienceEnabled=true`).
    See :func:`update_stack`. For more information, see
    `To use Terraform Registry with an older stack`__.

    __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#features__custom-providers
    __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/managingstacksandjobs.htm#use-tf-reg
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomTerraformProvider object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this CustomTerraformProvider.
        :type region: str

        :param namespace:
            The value to assign to the namespace property of this CustomTerraformProvider.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CustomTerraformProvider.
        :type bucket_name: str

        """
        self.swagger_types = {
            'region': 'str',
            'namespace': 'str',
            'bucket_name': 'str'
        }

        self.attribute_map = {
            'region': 'region',
            'namespace': 'namespace',
            'bucket_name': 'bucketName'
        }

        self._region = None
        self._namespace = None
        self._bucket_name = None

    @property
    def region(self):
        """
        **[Required]** Gets the region of this CustomTerraformProvider.
        The name of the region that contains the bucket you want.
        For information about regions, see `Regions and Availability Domains`__.
        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm


        :return: The region of this CustomTerraformProvider.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CustomTerraformProvider.
        The name of the region that contains the bucket you want.
        For information about regions, see `Regions and Availability Domains`__.
        Example: `us-phoenix-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm


        :param region: The region of this CustomTerraformProvider.
        :type: str
        """
        self._region = region

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this CustomTerraformProvider.
        The Object Storage namespace that contains the bucket you want.
        For information about Object Storage namespaces, see `Understanding Object Storage Namespaces`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm


        :return: The namespace of this CustomTerraformProvider.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this CustomTerraformProvider.
        The Object Storage namespace that contains the bucket you want.
        For information about Object Storage namespaces, see `Understanding Object Storage Namespaces`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm


        :param namespace: The namespace of this CustomTerraformProvider.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CustomTerraformProvider.
        The name of the bucket that contains the binary files for the custom Terraform providers.
        For information about buckets, see `Managing Buckets`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm


        :return: The bucket_name of this CustomTerraformProvider.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CustomTerraformProvider.
        The name of the bucket that contains the binary files for the custom Terraform providers.
        For information about buckets, see `Managing Buckets`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingbuckets.htm


        :param bucket_name: The bucket_name of this CustomTerraformProvider.
        :type: str
        """
        self._bucket_name = bucket_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
