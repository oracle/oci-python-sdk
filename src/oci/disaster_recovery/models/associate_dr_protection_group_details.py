# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociateDrProtectionGroupDetails(object):
    """
    The details for associating this DR Protection Group with a peer (remote) DR Protection Group.
    """

    #: A constant which can be used with the role property of a AssociateDrProtectionGroupDetails.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a AssociateDrProtectionGroupDetails.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a AssociateDrProtectionGroupDetails.
    #: This constant has a value of "UNCONFIGURED"
    ROLE_UNCONFIGURED = "UNCONFIGURED"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociateDrProtectionGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param peer_id:
            The value to assign to the peer_id property of this AssociateDrProtectionGroupDetails.
        :type peer_id: str

        :param peer_region:
            The value to assign to the peer_region property of this AssociateDrProtectionGroupDetails.
        :type peer_region: str

        :param role:
            The value to assign to the role property of this AssociateDrProtectionGroupDetails.
            Allowed values for this property are: "PRIMARY", "STANDBY", "UNCONFIGURED"
        :type role: str

        """
        self.swagger_types = {
            'peer_id': 'str',
            'peer_region': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'peer_id': 'peerId',
            'peer_region': 'peerRegion',
            'role': 'role'
        }

        self._peer_id = None
        self._peer_region = None
        self._role = None

    @property
    def peer_id(self):
        """
        Gets the peer_id of this AssociateDrProtectionGroupDetails.
        The OCID of the peer (remote) DR Protection Group.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :return: The peer_id of this AssociateDrProtectionGroupDetails.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """
        Sets the peer_id of this AssociateDrProtectionGroupDetails.
        The OCID of the peer (remote) DR Protection Group.

        Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`


        :param peer_id: The peer_id of this AssociateDrProtectionGroupDetails.
        :type: str
        """
        self._peer_id = peer_id

    @property
    def peer_region(self):
        """
        Gets the peer_region of this AssociateDrProtectionGroupDetails.
        The region of the peer (remote) DR Protection Group.

        Example: `us-ashburn-1`


        :return: The peer_region of this AssociateDrProtectionGroupDetails.
        :rtype: str
        """
        return self._peer_region

    @peer_region.setter
    def peer_region(self, peer_region):
        """
        Sets the peer_region of this AssociateDrProtectionGroupDetails.
        The region of the peer (remote) DR Protection Group.

        Example: `us-ashburn-1`


        :param peer_region: The peer_region of this AssociateDrProtectionGroupDetails.
        :type: str
        """
        self._peer_region = peer_region

    @property
    def role(self):
        """
        **[Required]** Gets the role of this AssociateDrProtectionGroupDetails.
        The role of this DR Protection Group.

        Allowed values for this property are: "PRIMARY", "STANDBY", "UNCONFIGURED"


        :return: The role of this AssociateDrProtectionGroupDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this AssociateDrProtectionGroupDetails.
        The role of this DR Protection Group.


        :param role: The role of this AssociateDrProtectionGroupDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "UNCONFIGURED"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                "Invalid value for `role`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
