# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManageModuleStreamsOnManagedInstanceGroupDetails(object):
    """
    The set of changes to make to the state of the modules, streams, and profiles on a managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManageModuleStreamsOnManagedInstanceGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_dry_run:
            The value to assign to the is_dry_run property of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type is_dry_run: bool

        :param enable:
            The value to assign to the enable property of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type enable: list[oci.os_management_hub.models.ModuleStreamDetails]

        :param disable:
            The value to assign to the disable property of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type disable: list[oci.os_management_hub.models.ModuleStreamDetails]

        :param install:
            The value to assign to the install property of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type install: list[oci.os_management_hub.models.ModuleStreamProfileDetails]

        :param remove:
            The value to assign to the remove property of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type remove: list[oci.os_management_hub.models.ModuleStreamProfileDetails]

        :param work_request_details:
            The value to assign to the work_request_details property of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type work_request_details: oci.os_management_hub.models.WorkRequestDetails

        """
        self.swagger_types = {
            'is_dry_run': 'bool',
            'enable': 'list[ModuleStreamDetails]',
            'disable': 'list[ModuleStreamDetails]',
            'install': 'list[ModuleStreamProfileDetails]',
            'remove': 'list[ModuleStreamProfileDetails]',
            'work_request_details': 'WorkRequestDetails'
        }
        self.attribute_map = {
            'is_dry_run': 'isDryRun',
            'enable': 'enable',
            'disable': 'disable',
            'install': 'install',
            'remove': 'remove',
            'work_request_details': 'workRequestDetails'
        }
        self._is_dry_run = None
        self._enable = None
        self._disable = None
        self._install = None
        self._remove = None
        self._work_request_details = None

    @property
    def is_dry_run(self):
        """
        Gets the is_dry_run of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        Indicates if this operation is a dry run or if the operation
        should be committed.  If set to true, the result of the operation
        will be evaluated but not committed.  If set to false, the
        operation is committed to the managed instance(s).  The default is
        false.


        :return: The is_dry_run of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :rtype: bool
        """
        return self._is_dry_run

    @is_dry_run.setter
    def is_dry_run(self, is_dry_run):
        """
        Sets the is_dry_run of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        Indicates if this operation is a dry run or if the operation
        should be committed.  If set to true, the result of the operation
        will be evaluated but not committed.  If set to false, the
        operation is committed to the managed instance(s).  The default is
        false.


        :param is_dry_run: The is_dry_run of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type: bool
        """
        self._is_dry_run = is_dry_run

    @property
    def enable(self):
        """
        Gets the enable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module streams to enable.


        :return: The enable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module streams to enable.


        :param enable: The enable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        self._enable = enable

    @property
    def disable(self):
        """
        Gets the disable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module streams to disable.


        :return: The disable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        """
        Sets the disable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module streams to disable.


        :param disable: The disable of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamDetails]
        """
        self._disable = disable

    @property
    def install(self):
        """
        Gets the install of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module stream profiles to install.


        :return: The install of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        return self._install

    @install.setter
    def install(self, install):
        """
        Sets the install of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module stream profiles to install.


        :param install: The install of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        self._install = install

    @property
    def remove(self):
        """
        Gets the remove of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module stream profiles to remove.


        :return: The remove of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :rtype: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """
        Sets the remove of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        The set of module stream profiles to remove.


        :param remove: The remove of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type: list[oci.os_management_hub.models.ModuleStreamProfileDetails]
        """
        self._remove = remove

    @property
    def work_request_details(self):
        """
        Gets the work_request_details of this ManageModuleStreamsOnManagedInstanceGroupDetails.

        :return: The work_request_details of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :rtype: oci.os_management_hub.models.WorkRequestDetails
        """
        return self._work_request_details

    @work_request_details.setter
    def work_request_details(self, work_request_details):
        """
        Sets the work_request_details of this ManageModuleStreamsOnManagedInstanceGroupDetails.

        :param work_request_details: The work_request_details of this ManageModuleStreamsOnManagedInstanceGroupDetails.
        :type: oci.os_management_hub.models.WorkRequestDetails
        """
        self._work_request_details = work_request_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
