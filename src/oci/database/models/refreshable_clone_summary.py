# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RefreshableCloneSummary(object):
    """
    An Autonomous Database refreshable clone
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RefreshableCloneSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RefreshableCloneSummary.
        :type id: str

        :param region:
            The value to assign to the region property of this RefreshableCloneSummary.
        :type region: str

        """
        self.swagger_types = {
            'id': 'str',
            'region': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'region': 'region'
        }

        self._id = None
        self._region = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RefreshableCloneSummary.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this RefreshableCloneSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RefreshableCloneSummary.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this RefreshableCloneSummary.
        :type: str
        """
        self._id = id

    @property
    def region(self):
        """
        **[Required]** Gets the region of this RefreshableCloneSummary.
        The name of the region where the refreshable clone exists.


        :return: The region of this RefreshableCloneSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this RefreshableCloneSummary.
        The name of the region where the refreshable clone exists.


        :param region: The region of this RefreshableCloneSummary.
        :type: str
        """
        self._region = region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
