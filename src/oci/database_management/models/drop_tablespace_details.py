# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DropTablespaceDetails(object):
    """
    The details required to drop a tablespace.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DropTablespaceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param credential_details:
            The value to assign to the credential_details property of this DropTablespaceDetails.
        :type credential_details: oci.database_management.models.TablespaceAdminCredentialDetails

        :param is_including_contents:
            The value to assign to the is_including_contents property of this DropTablespaceDetails.
        :type is_including_contents: bool

        :param is_dropping_data_files:
            The value to assign to the is_dropping_data_files property of this DropTablespaceDetails.
        :type is_dropping_data_files: bool

        :param is_cascade_constraints:
            The value to assign to the is_cascade_constraints property of this DropTablespaceDetails.
        :type is_cascade_constraints: bool

        """
        self.swagger_types = {
            'credential_details': 'TablespaceAdminCredentialDetails',
            'is_including_contents': 'bool',
            'is_dropping_data_files': 'bool',
            'is_cascade_constraints': 'bool'
        }

        self.attribute_map = {
            'credential_details': 'credentialDetails',
            'is_including_contents': 'isIncludingContents',
            'is_dropping_data_files': 'isDroppingDataFiles',
            'is_cascade_constraints': 'isCascadeConstraints'
        }

        self._credential_details = None
        self._is_including_contents = None
        self._is_dropping_data_files = None
        self._is_cascade_constraints = None

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this DropTablespaceDetails.

        :return: The credential_details of this DropTablespaceDetails.
        :rtype: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this DropTablespaceDetails.

        :param credential_details: The credential_details of this DropTablespaceDetails.
        :type: oci.database_management.models.TablespaceAdminCredentialDetails
        """
        self._credential_details = credential_details

    @property
    def is_including_contents(self):
        """
        Gets the is_including_contents of this DropTablespaceDetails.
        Specifies whether all the contents of the tablespace being dropped should be dropped.


        :return: The is_including_contents of this DropTablespaceDetails.
        :rtype: bool
        """
        return self._is_including_contents

    @is_including_contents.setter
    def is_including_contents(self, is_including_contents):
        """
        Sets the is_including_contents of this DropTablespaceDetails.
        Specifies whether all the contents of the tablespace being dropped should be dropped.


        :param is_including_contents: The is_including_contents of this DropTablespaceDetails.
        :type: bool
        """
        self._is_including_contents = is_including_contents

    @property
    def is_dropping_data_files(self):
        """
        Gets the is_dropping_data_files of this DropTablespaceDetails.
        Specifies whether all the associated data files of the tablespace being dropped should be dropped.


        :return: The is_dropping_data_files of this DropTablespaceDetails.
        :rtype: bool
        """
        return self._is_dropping_data_files

    @is_dropping_data_files.setter
    def is_dropping_data_files(self, is_dropping_data_files):
        """
        Sets the is_dropping_data_files of this DropTablespaceDetails.
        Specifies whether all the associated data files of the tablespace being dropped should be dropped.


        :param is_dropping_data_files: The is_dropping_data_files of this DropTablespaceDetails.
        :type: bool
        """
        self._is_dropping_data_files = is_dropping_data_files

    @property
    def is_cascade_constraints(self):
        """
        Gets the is_cascade_constraints of this DropTablespaceDetails.
        Specifies whether all the constraints on the tablespace being dropped should be dropped.


        :return: The is_cascade_constraints of this DropTablespaceDetails.
        :rtype: bool
        """
        return self._is_cascade_constraints

    @is_cascade_constraints.setter
    def is_cascade_constraints(self, is_cascade_constraints):
        """
        Sets the is_cascade_constraints of this DropTablespaceDetails.
        Specifies whether all the constraints on the tablespace being dropped should be dropped.


        :param is_cascade_constraints: The is_cascade_constraints of this DropTablespaceDetails.
        :type: bool
        """
        self._is_cascade_constraints = is_cascade_constraints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
