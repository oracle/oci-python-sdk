# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAwsS3Details(object):
    """
    AWS S3 bucket details used for source Connection resources with RDS_ORACLE type.
    Only supported for source Connection resources with RDS_ORACLE type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAwsS3Details object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateAwsS3Details.
        :type name: str

        :param region:
            The value to assign to the region property of this UpdateAwsS3Details.
        :type region: str

        :param access_key_id:
            The value to assign to the access_key_id property of this UpdateAwsS3Details.
        :type access_key_id: str

        :param secret_access_key:
            The value to assign to the secret_access_key property of this UpdateAwsS3Details.
        :type secret_access_key: str

        """
        self.swagger_types = {
            'name': 'str',
            'region': 'str',
            'access_key_id': 'str',
            'secret_access_key': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'region': 'region',
            'access_key_id': 'accessKeyId',
            'secret_access_key': 'secretAccessKey'
        }

        self._name = None
        self._region = None
        self._access_key_id = None
        self._secret_access_key = None

    @property
    def name(self):
        """
        Gets the name of this UpdateAwsS3Details.
        S3 bucket name.


        :return: The name of this UpdateAwsS3Details.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateAwsS3Details.
        S3 bucket name.


        :param name: The name of this UpdateAwsS3Details.
        :type: str
        """
        self._name = name

    @property
    def region(self):
        """
        Gets the region of this UpdateAwsS3Details.
        AWS region code where the S3 bucket is located.
        Region code should match the documented available regions:
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions


        :return: The region of this UpdateAwsS3Details.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UpdateAwsS3Details.
        AWS region code where the S3 bucket is located.
        Region code should match the documented available regions:
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions


        :param region: The region of this UpdateAwsS3Details.
        :type: str
        """
        self._region = region

    @property
    def access_key_id(self):
        """
        Gets the access_key_id of this UpdateAwsS3Details.
        AWS access key credentials identifier
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :return: The access_key_id of this UpdateAwsS3Details.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """
        Sets the access_key_id of this UpdateAwsS3Details.
        AWS access key credentials identifier
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :param access_key_id: The access_key_id of this UpdateAwsS3Details.
        :type: str
        """
        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """
        Gets the secret_access_key of this UpdateAwsS3Details.
        AWS secret access key credentials
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :return: The secret_access_key of this UpdateAwsS3Details.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """
        Sets the secret_access_key of this UpdateAwsS3Details.
        AWS secret access key credentials
        Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys


        :param secret_access_key: The secret_access_key of this UpdateAwsS3Details.
        :type: str
        """
        self._secret_access_key = secret_access_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
