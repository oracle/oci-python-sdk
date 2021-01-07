# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbHomeDetails(object):
    """
    Describes the modification parameters for the Database Home.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbHomeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_version:
            The value to assign to the db_version property of this UpdateDbHomeDetails.
        :type db_version: oci.database.models.PatchDetails

        :param one_off_patches:
            The value to assign to the one_off_patches property of this UpdateDbHomeDetails.
        :type one_off_patches: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDbHomeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDbHomeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'db_version': 'PatchDetails',
            'one_off_patches': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'db_version': 'dbVersion',
            'one_off_patches': 'oneOffPatches',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._db_version = None
        self._one_off_patches = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def db_version(self):
        """
        Gets the db_version of this UpdateDbHomeDetails.

        :return: The db_version of this UpdateDbHomeDetails.
        :rtype: oci.database.models.PatchDetails
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this UpdateDbHomeDetails.

        :param db_version: The db_version of this UpdateDbHomeDetails.
        :type: oci.database.models.PatchDetails
        """
        self._db_version = db_version

    @property
    def one_off_patches(self):
        """
        Gets the one_off_patches of this UpdateDbHomeDetails.
        List of one-off patches for Database Homes.


        :return: The one_off_patches of this UpdateDbHomeDetails.
        :rtype: list[str]
        """
        return self._one_off_patches

    @one_off_patches.setter
    def one_off_patches(self, one_off_patches):
        """
        Sets the one_off_patches of this UpdateDbHomeDetails.
        List of one-off patches for Database Homes.


        :param one_off_patches: The one_off_patches of this UpdateDbHomeDetails.
        :type: list[str]
        """
        self._one_off_patches = one_off_patches

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDbHomeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateDbHomeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDbHomeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateDbHomeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDbHomeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateDbHomeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDbHomeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateDbHomeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
