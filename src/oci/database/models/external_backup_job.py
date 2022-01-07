# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalBackupJob(object):
    """
    Provides all the details that apply to an external backup job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalBackupJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_id:
            The value to assign to the backup_id property of this ExternalBackupJob.
        :type backup_id: str

        :param provisioning:
            The value to assign to the provisioning property of this ExternalBackupJob.
        :type provisioning: bool

        :param swift_path:
            The value to assign to the swift_path property of this ExternalBackupJob.
        :type swift_path: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ExternalBackupJob.
        :type bucket_name: str

        :param tag:
            The value to assign to the tag property of this ExternalBackupJob.
        :type tag: str

        :param user_name:
            The value to assign to the user_name property of this ExternalBackupJob.
        :type user_name: str

        :param swift_password:
            The value to assign to the swift_password property of this ExternalBackupJob.
        :type swift_password: str

        """
        self.swagger_types = {
            'backup_id': 'str',
            'provisioning': 'bool',
            'swift_path': 'str',
            'bucket_name': 'str',
            'tag': 'str',
            'user_name': 'str',
            'swift_password': 'str'
        }

        self.attribute_map = {
            'backup_id': 'backupId',
            'provisioning': 'provisioning',
            'swift_path': 'swiftPath',
            'bucket_name': 'bucketName',
            'tag': 'tag',
            'user_name': 'userName',
            'swift_password': 'swiftPassword'
        }

        self._backup_id = None
        self._provisioning = None
        self._swift_path = None
        self._bucket_name = None
        self._tag = None
        self._user_name = None
        self._swift_password = None

    @property
    def backup_id(self):
        """
        **[Required]** Gets the backup_id of this ExternalBackupJob.
        The `OCID`__ of the associated backup resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The backup_id of this ExternalBackupJob.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """
        Sets the backup_id of this ExternalBackupJob.
        The `OCID`__ of the associated backup resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param backup_id: The backup_id of this ExternalBackupJob.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def provisioning(self):
        """
        **[Required]** Gets the provisioning of this ExternalBackupJob.
        An indicator for the provisioning state of the resource. If `TRUE`, the resource is still being provisioned.


        :return: The provisioning of this ExternalBackupJob.
        :rtype: bool
        """
        return self._provisioning

    @provisioning.setter
    def provisioning(self, provisioning):
        """
        Sets the provisioning of this ExternalBackupJob.
        An indicator for the provisioning state of the resource. If `TRUE`, the resource is still being provisioned.


        :param provisioning: The provisioning of this ExternalBackupJob.
        :type: bool
        """
        self._provisioning = provisioning

    @property
    def swift_path(self):
        """
        **[Required]** Gets the swift_path of this ExternalBackupJob.
        The Swift path to use as a destination for the standalone backup.


        :return: The swift_path of this ExternalBackupJob.
        :rtype: str
        """
        return self._swift_path

    @swift_path.setter
    def swift_path(self, swift_path):
        """
        Sets the swift_path of this ExternalBackupJob.
        The Swift path to use as a destination for the standalone backup.


        :param swift_path: The swift_path of this ExternalBackupJob.
        :type: str
        """
        self._swift_path = swift_path

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ExternalBackupJob.
        The name of the Swift compartment bucket where the backup should be stored.


        :return: The bucket_name of this ExternalBackupJob.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ExternalBackupJob.
        The name of the Swift compartment bucket where the backup should be stored.


        :param bucket_name: The bucket_name of this ExternalBackupJob.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def tag(self):
        """
        **[Required]** Gets the tag of this ExternalBackupJob.
        The tag for RMAN to apply to the backup.


        :return: The tag of this ExternalBackupJob.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this ExternalBackupJob.
        The tag for RMAN to apply to the backup.


        :param tag: The tag of this ExternalBackupJob.
        :type: str
        """
        self._tag = tag

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this ExternalBackupJob.
        The Swift user name to use for transferring the standalone backup to the designated Swift compartment bucket.


        :return: The user_name of this ExternalBackupJob.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this ExternalBackupJob.
        The Swift user name to use for transferring the standalone backup to the designated Swift compartment bucket.


        :param user_name: The user_name of this ExternalBackupJob.
        :type: str
        """
        self._user_name = user_name

    @property
    def swift_password(self):
        """
        Gets the swift_password of this ExternalBackupJob.
        The auth token to use for access to the Swift compartment bucket that will store the standalone backup.
        For information about auth tokens, see `Working with Auth Tokens`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Tasks/managingcredentials.htm#two


        :return: The swift_password of this ExternalBackupJob.
        :rtype: str
        """
        return self._swift_password

    @swift_password.setter
    def swift_password(self, swift_password):
        """
        Sets the swift_password of this ExternalBackupJob.
        The auth token to use for access to the Swift compartment bucket that will store the standalone backup.
        For information about auth tokens, see `Working with Auth Tokens`__.

        __ https://docs.cloud.oracle.com/Content/Identity/Tasks/managingcredentials.htm#two


        :param swift_password: The swift_password of this ExternalBackupJob.
        :type: str
        """
        self._swift_password = swift_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
