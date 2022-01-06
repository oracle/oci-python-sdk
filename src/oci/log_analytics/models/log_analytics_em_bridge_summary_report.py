# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsEmBridgeSummaryReport(object):
    """
    Log-Analytics EM Bridge counts summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsEmBridgeSummaryReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsEmBridgeSummaryReport.
        :type compartment_id: str

        :param active_em_bridge_count:
            The value to assign to the active_em_bridge_count property of this LogAnalyticsEmBridgeSummaryReport.
        :type active_em_bridge_count: int

        :param creating_em_bridge_count:
            The value to assign to the creating_em_bridge_count property of this LogAnalyticsEmBridgeSummaryReport.
        :type creating_em_bridge_count: int

        :param needs_attention_em_bridge_count:
            The value to assign to the needs_attention_em_bridge_count property of this LogAnalyticsEmBridgeSummaryReport.
        :type needs_attention_em_bridge_count: int

        :param deleted_em_bridge_count:
            The value to assign to the deleted_em_bridge_count property of this LogAnalyticsEmBridgeSummaryReport.
        :type deleted_em_bridge_count: int

        :param total_em_bridge_count:
            The value to assign to the total_em_bridge_count property of this LogAnalyticsEmBridgeSummaryReport.
        :type total_em_bridge_count: int

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'active_em_bridge_count': 'int',
            'creating_em_bridge_count': 'int',
            'needs_attention_em_bridge_count': 'int',
            'deleted_em_bridge_count': 'int',
            'total_em_bridge_count': 'int'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'active_em_bridge_count': 'activeEmBridgeCount',
            'creating_em_bridge_count': 'creatingEmBridgeCount',
            'needs_attention_em_bridge_count': 'needsAttentionEmBridgeCount',
            'deleted_em_bridge_count': 'deletedEmBridgeCount',
            'total_em_bridge_count': 'totalEmBridgeCount'
        }

        self._compartment_id = None
        self._active_em_bridge_count = None
        self._creating_em_bridge_count = None
        self._needs_attention_em_bridge_count = None
        self._deleted_em_bridge_count = None
        self._total_em_bridge_count = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogAnalyticsEmBridgeSummaryReport.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogAnalyticsEmBridgeSummaryReport.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsEmBridgeSummaryReport.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogAnalyticsEmBridgeSummaryReport.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def active_em_bridge_count(self):
        """
        **[Required]** Gets the active_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Total number of ACTIVE enterprise manager bridges.


        :return: The active_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :rtype: int
        """
        return self._active_em_bridge_count

    @active_em_bridge_count.setter
    def active_em_bridge_count(self, active_em_bridge_count):
        """
        Sets the active_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Total number of ACTIVE enterprise manager bridges.


        :param active_em_bridge_count: The active_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :type: int
        """
        self._active_em_bridge_count = active_em_bridge_count

    @property
    def creating_em_bridge_count(self):
        """
        **[Required]** Gets the creating_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Number of enterprise manager bridges in CREATING state.


        :return: The creating_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :rtype: int
        """
        return self._creating_em_bridge_count

    @creating_em_bridge_count.setter
    def creating_em_bridge_count(self, creating_em_bridge_count):
        """
        Sets the creating_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Number of enterprise manager bridges in CREATING state.


        :param creating_em_bridge_count: The creating_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :type: int
        """
        self._creating_em_bridge_count = creating_em_bridge_count

    @property
    def needs_attention_em_bridge_count(self):
        """
        **[Required]** Gets the needs_attention_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Number of enterprise manager bridges in NEEDS_ATTENTION state.


        :return: The needs_attention_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :rtype: int
        """
        return self._needs_attention_em_bridge_count

    @needs_attention_em_bridge_count.setter
    def needs_attention_em_bridge_count(self, needs_attention_em_bridge_count):
        """
        Sets the needs_attention_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Number of enterprise manager bridges in NEEDS_ATTENTION state.


        :param needs_attention_em_bridge_count: The needs_attention_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :type: int
        """
        self._needs_attention_em_bridge_count = needs_attention_em_bridge_count

    @property
    def deleted_em_bridge_count(self):
        """
        **[Required]** Gets the deleted_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Number of enterprise manager bridges in DELETED state.


        :return: The deleted_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :rtype: int
        """
        return self._deleted_em_bridge_count

    @deleted_em_bridge_count.setter
    def deleted_em_bridge_count(self, deleted_em_bridge_count):
        """
        Sets the deleted_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Number of enterprise manager bridges in DELETED state.


        :param deleted_em_bridge_count: The deleted_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :type: int
        """
        self._deleted_em_bridge_count = deleted_em_bridge_count

    @property
    def total_em_bridge_count(self):
        """
        **[Required]** Gets the total_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Total number of enterprise manager bridges.


        :return: The total_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :rtype: int
        """
        return self._total_em_bridge_count

    @total_em_bridge_count.setter
    def total_em_bridge_count(self, total_em_bridge_count):
        """
        Sets the total_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        Total number of enterprise manager bridges.


        :param total_em_bridge_count: The total_em_bridge_count of this LogAnalyticsEmBridgeSummaryReport.
        :type: int
        """
        self._total_em_bridge_count = total_em_bridge_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
