# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateDbHomeDetails(object):

    def __init__(self):

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
