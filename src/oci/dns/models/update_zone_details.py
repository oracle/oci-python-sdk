# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateZoneDetails(object):
    """
    The body for updating a zone.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the dnssec_state property of a UpdateZoneDetails.
    #: This constant has a value of "ENABLED"
    DNSSEC_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the dnssec_state property of a UpdateZoneDetails.
    #: This constant has a value of "DISABLED"
    DNSSEC_STATE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateZoneDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateZoneDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateZoneDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param dnssec_state:
            The value to assign to the dnssec_state property of this UpdateZoneDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type dnssec_state: str

        :param external_masters:
            The value to assign to the external_masters property of this UpdateZoneDetails.
        :type external_masters: list[oci.dns.models.ExternalMaster]

        :param external_downstreams:
            The value to assign to the external_downstreams property of this UpdateZoneDetails.
        :type external_downstreams: list[oci.dns.models.ExternalDownstream]

        """
        self.swagger_types = {
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'dnssec_state': 'str',
            'external_masters': 'list[ExternalMaster]',
            'external_downstreams': 'list[ExternalDownstream]'
        }
        self.attribute_map = {
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'dnssec_state': 'dnssecState',
            'external_masters': 'externalMasters',
            'external_downstreams': 'externalDownstreams'
        }
        self._freeform_tags = None
        self._defined_tags = None
        self._dnssec_state = None
        self._external_masters = None
        self._external_downstreams = None

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateZoneDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateZoneDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateZoneDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateZoneDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateZoneDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateZoneDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateZoneDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateZoneDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def dnssec_state(self):
        """
        Gets the dnssec_state of this UpdateZoneDetails.
        The state of DNSSEC on the zone.

        For DNSSEC to function, every parent zone in the DNS tree up to the top-level domain (or an independent
        trust anchor) must also have DNSSEC correctly set up.
        After enabling DNSSEC, you must add a DS record to the zone's parent zone containing the
        `KskDnssecKeyVersion` data. You can find the DS data in the `dsData` attribute of the `KskDnssecKeyVersion`.
        Then, use the `PromoteZoneDnssecKeyVersion` operation to promote the `KskDnssecKeyVersion`.

        New `KskDnssecKeyVersion`s are generated annually, a week before the existing `KskDnssecKeyVersion`'s expiration.
        To rollover a `KskDnssecKeyVersion`, you must replace the parent zone's DS record containing the old
        `KskDnssecKeyVersion` data with the data from the new `KskDnssecKeyVersion`.

        To remove the old DS record without causing service disruption, wait until the old DS record's TTL has
        expired, and the new DS record has propagated. After the DS replacement has been completed, then the
        `PromoteZoneDnssecKeyVersion` operation must be called.

        Metrics are emitted in the `oci_dns` namespace daily for each `KskDnssecKeyVersion` indicating how many
        days are left until expiration.
        We recommend that you set up alarms and notifications for KskDnssecKeyVersion expiration so that the
        necessary parent zone updates can be made and the `PromoteZoneDnssecKeyVersion` operation can be called.

        Enabling DNSSEC results in additional records in DNS responses which increases their size and can
        cause higher response latency.

        For more information, see `DNSSEC`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnssec.htm

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The dnssec_state of this UpdateZoneDetails.
        :rtype: str
        """
        return self._dnssec_state

    @dnssec_state.setter
    def dnssec_state(self, dnssec_state):
        """
        Sets the dnssec_state of this UpdateZoneDetails.
        The state of DNSSEC on the zone.

        For DNSSEC to function, every parent zone in the DNS tree up to the top-level domain (or an independent
        trust anchor) must also have DNSSEC correctly set up.
        After enabling DNSSEC, you must add a DS record to the zone's parent zone containing the
        `KskDnssecKeyVersion` data. You can find the DS data in the `dsData` attribute of the `KskDnssecKeyVersion`.
        Then, use the `PromoteZoneDnssecKeyVersion` operation to promote the `KskDnssecKeyVersion`.

        New `KskDnssecKeyVersion`s are generated annually, a week before the existing `KskDnssecKeyVersion`'s expiration.
        To rollover a `KskDnssecKeyVersion`, you must replace the parent zone's DS record containing the old
        `KskDnssecKeyVersion` data with the data from the new `KskDnssecKeyVersion`.

        To remove the old DS record without causing service disruption, wait until the old DS record's TTL has
        expired, and the new DS record has propagated. After the DS replacement has been completed, then the
        `PromoteZoneDnssecKeyVersion` operation must be called.

        Metrics are emitted in the `oci_dns` namespace daily for each `KskDnssecKeyVersion` indicating how many
        days are left until expiration.
        We recommend that you set up alarms and notifications for KskDnssecKeyVersion expiration so that the
        necessary parent zone updates can be made and the `PromoteZoneDnssecKeyVersion` operation can be called.

        Enabling DNSSEC results in additional records in DNS responses which increases their size and can
        cause higher response latency.

        For more information, see `DNSSEC`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnssec.htm


        :param dnssec_state: The dnssec_state of this UpdateZoneDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(dnssec_state, allowed_values):
            raise ValueError(
                f"Invalid value for `dnssec_state`, must be None or one of {allowed_values}"
            )
        self._dnssec_state = dnssec_state

    @property
    def external_masters(self):
        """
        Gets the external_masters of this UpdateZoneDetails.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :return: The external_masters of this UpdateZoneDetails.
        :rtype: list[oci.dns.models.ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this UpdateZoneDetails.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :param external_masters: The external_masters of this UpdateZoneDetails.
        :type: list[oci.dns.models.ExternalMaster]
        """
        self._external_masters = external_masters

    @property
    def external_downstreams(self):
        """
        Gets the external_downstreams of this UpdateZoneDetails.
        External secondary servers for the zone.
        This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.


        :return: The external_downstreams of this UpdateZoneDetails.
        :rtype: list[oci.dns.models.ExternalDownstream]
        """
        return self._external_downstreams

    @external_downstreams.setter
    def external_downstreams(self, external_downstreams):
        """
        Sets the external_downstreams of this UpdateZoneDetails.
        External secondary servers for the zone.
        This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.


        :param external_downstreams: The external_downstreams of this UpdateZoneDetails.
        :type: list[oci.dns.models.ExternalDownstream]
        """
        self._external_downstreams = external_downstreams

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
