# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbHomeDetails(object):
    """
    Describes the modification parameters for the database home.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbHomeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_version:
            The value to assign to the db_version property of this UpdateDbHomeDetails.
        :type db_version: PatchDetails

        """
        self.swagger_types = {
            'db_version': 'PatchDetails'
        }

        self.attribute_map = {
            'db_version': 'dbVersion'
        }

        self._db_version = None

    @property
    def db_version(self):
        """
        Gets the db_version of this UpdateDbHomeDetails.

        :return: The db_version of this UpdateDbHomeDetails.
        :rtype: PatchDetails
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this UpdateDbHomeDetails.

        :param db_version: The db_version of this UpdateDbHomeDetails.
        :type: PatchDetails
        """
        self._db_version = db_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
