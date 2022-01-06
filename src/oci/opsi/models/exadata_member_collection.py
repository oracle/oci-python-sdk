# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataMemberCollection(object):
    """
    Partial definition of the exadata insight resource.
    """

    #: A constant which can be used with the exadata_type property of a ExadataMemberCollection.
    #: This constant has a value of "DBMACHINE"
    EXADATA_TYPE_DBMACHINE = "DBMACHINE"

    #: A constant which can be used with the exadata_type property of a ExadataMemberCollection.
    #: This constant has a value of "EXACS"
    EXADATA_TYPE_EXACS = "EXACS"

    #: A constant which can be used with the exadata_type property of a ExadataMemberCollection.
    #: This constant has a value of "EXACC"
    EXADATA_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the exadata_rack_type property of a ExadataMemberCollection.
    #: This constant has a value of "FULL"
    EXADATA_RACK_TYPE_FULL = "FULL"

    #: A constant which can be used with the exadata_rack_type property of a ExadataMemberCollection.
    #: This constant has a value of "HALF"
    EXADATA_RACK_TYPE_HALF = "HALF"

    #: A constant which can be used with the exadata_rack_type property of a ExadataMemberCollection.
    #: This constant has a value of "QUARTER"
    EXADATA_RACK_TYPE_QUARTER = "QUARTER"

    #: A constant which can be used with the exadata_rack_type property of a ExadataMemberCollection.
    #: This constant has a value of "EIGHTH"
    EXADATA_RACK_TYPE_EIGHTH = "EIGHTH"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataMemberCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this ExadataMemberCollection.
        :type exadata_insight_id: str

        :param exadata_name:
            The value to assign to the exadata_name property of this ExadataMemberCollection.
        :type exadata_name: str

        :param exadata_display_name:
            The value to assign to the exadata_display_name property of this ExadataMemberCollection.
        :type exadata_display_name: str

        :param exadata_type:
            The value to assign to the exadata_type property of this ExadataMemberCollection.
            Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_type: str

        :param exadata_rack_type:
            The value to assign to the exadata_rack_type property of this ExadataMemberCollection.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type exadata_rack_type: str

        :param items:
            The value to assign to the items property of this ExadataMemberCollection.
        :type items: list[oci.opsi.models.ExadataMemberSummary]

        """
        self.swagger_types = {
            'exadata_insight_id': 'str',
            'exadata_name': 'str',
            'exadata_display_name': 'str',
            'exadata_type': 'str',
            'exadata_rack_type': 'str',
            'items': 'list[ExadataMemberSummary]'
        }

        self.attribute_map = {
            'exadata_insight_id': 'exadataInsightId',
            'exadata_name': 'exadataName',
            'exadata_display_name': 'exadataDisplayName',
            'exadata_type': 'exadataType',
            'exadata_rack_type': 'exadataRackType',
            'items': 'items'
        }

        self._exadata_insight_id = None
        self._exadata_name = None
        self._exadata_display_name = None
        self._exadata_type = None
        self._exadata_rack_type = None
        self._items = None

    @property
    def exadata_insight_id(self):
        """
        **[Required]** Gets the exadata_insight_id of this ExadataMemberCollection.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this ExadataMemberCollection.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this ExadataMemberCollection.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this ExadataMemberCollection.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    @property
    def exadata_name(self):
        """
        **[Required]** Gets the exadata_name of this ExadataMemberCollection.
        The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.


        :return: The exadata_name of this ExadataMemberCollection.
        :rtype: str
        """
        return self._exadata_name

    @exadata_name.setter
    def exadata_name(self, exadata_name):
        """
        Sets the exadata_name of this ExadataMemberCollection.
        The Exadata system name. If the Exadata systems managed by Enterprise Manager, the name is unique amongst the Exadata systems managed by the same Enterprise Manager.


        :param exadata_name: The exadata_name of this ExadataMemberCollection.
        :type: str
        """
        self._exadata_name = exadata_name

    @property
    def exadata_display_name(self):
        """
        **[Required]** Gets the exadata_display_name of this ExadataMemberCollection.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :return: The exadata_display_name of this ExadataMemberCollection.
        :rtype: str
        """
        return self._exadata_display_name

    @exadata_display_name.setter
    def exadata_display_name(self, exadata_display_name):
        """
        Sets the exadata_display_name of this ExadataMemberCollection.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :param exadata_display_name: The exadata_display_name of this ExadataMemberCollection.
        :type: str
        """
        self._exadata_display_name = exadata_display_name

    @property
    def exadata_type(self):
        """
        **[Required]** Gets the exadata_type of this ExadataMemberCollection.
        Operations Insights internal representation of the the Exadata system type.

        Allowed values for this property are: "DBMACHINE", "EXACS", "EXACC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_type of this ExadataMemberCollection.
        :rtype: str
        """
        return self._exadata_type

    @exadata_type.setter
    def exadata_type(self, exadata_type):
        """
        Sets the exadata_type of this ExadataMemberCollection.
        Operations Insights internal representation of the the Exadata system type.


        :param exadata_type: The exadata_type of this ExadataMemberCollection.
        :type: str
        """
        allowed_values = ["DBMACHINE", "EXACS", "EXACC"]
        if not value_allowed_none_or_none_sentinel(exadata_type, allowed_values):
            exadata_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_type = exadata_type

    @property
    def exadata_rack_type(self):
        """
        **[Required]** Gets the exadata_rack_type of this ExadataMemberCollection.
        Exadata rack type.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The exadata_rack_type of this ExadataMemberCollection.
        :rtype: str
        """
        return self._exadata_rack_type

    @exadata_rack_type.setter
    def exadata_rack_type(self, exadata_rack_type):
        """
        Sets the exadata_rack_type of this ExadataMemberCollection.
        Exadata rack type.


        :param exadata_rack_type: The exadata_rack_type of this ExadataMemberCollection.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH"]
        if not value_allowed_none_or_none_sentinel(exadata_rack_type, allowed_values):
            exadata_rack_type = 'UNKNOWN_ENUM_VALUE'
        self._exadata_rack_type = exadata_rack_type

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ExadataMemberCollection.
        Collection of Exadata members


        :return: The items of this ExadataMemberCollection.
        :rtype: list[oci.opsi.models.ExadataMemberSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ExadataMemberCollection.
        Collection of Exadata members


        :param items: The items of this ExadataMemberCollection.
        :type: list[oci.opsi.models.ExadataMemberSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
