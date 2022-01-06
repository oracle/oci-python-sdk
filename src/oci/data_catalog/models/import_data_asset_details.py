# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImportDataAssetDetails(object):
    """
    Specifies the file contents to be imported.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImportDataAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param import_file_contents:
            The value to assign to the import_file_contents property of this ImportDataAssetDetails.
        :type import_file_contents: str

        """
        self.swagger_types = {
            'import_file_contents': 'str'
        }

        self.attribute_map = {
            'import_file_contents': 'importFileContents'
        }

        self._import_file_contents = None

    @property
    def import_file_contents(self):
        """
        **[Required]** Gets the import_file_contents of this ImportDataAssetDetails.
        The file contents to be imported. File size not to exceed 10 MB.


        :return: The import_file_contents of this ImportDataAssetDetails.
        :rtype: str
        """
        return self._import_file_contents

    @import_file_contents.setter
    def import_file_contents(self, import_file_contents):
        """
        Sets the import_file_contents of this ImportDataAssetDetails.
        The file contents to be imported. File size not to exceed 10 MB.


        :param import_file_contents: The import_file_contents of this ImportDataAssetDetails.
        :type: str
        """
        self._import_file_contents = import_file_contents

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
