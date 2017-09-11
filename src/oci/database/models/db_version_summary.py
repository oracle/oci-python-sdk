# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class DbVersionSummary(object):

    def __init__(self):

        self.swagger_types = {
            'supports_pdb': 'bool',
            'version': 'str'
        }

        self.attribute_map = {
            'supports_pdb': 'supportsPdb',
            'version': 'version'
        }

        self._supports_pdb = None
        self._version = None

    @property
    def supports_pdb(self):
        """
        Gets the supports_pdb of this DbVersionSummary.
        True if this version of the Oracle database software supports pluggable dbs.


        :return: The supports_pdb of this DbVersionSummary.
        :rtype: bool
        """
        return self._supports_pdb

    @supports_pdb.setter
    def supports_pdb(self, supports_pdb):
        """
        Sets the supports_pdb of this DbVersionSummary.
        True if this version of the Oracle database software supports pluggable dbs.


        :param supports_pdb: The supports_pdb of this DbVersionSummary.
        :type: bool
        """
        self._supports_pdb = supports_pdb

    @property
    def version(self):
        """
        Gets the version of this DbVersionSummary.
        A valid Oracle database version.


        :return: The version of this DbVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DbVersionSummary.
        A valid Oracle database version.


        :param version: The version of this DbVersionSummary.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
