# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementDashboardTileDetails(object):
    """
    Properties of the dashboard tile representing a saved search.
    Tiles are laid out in a twelve column grid system with (0,0) at upper left corner.
    """

    #: A constant which can be used with the state property of a ManagementDashboardTileDetails.
    #: This constant has a value of "DELETED"
    STATE_DELETED = "DELETED"

    #: A constant which can be used with the state property of a ManagementDashboardTileDetails.
    #: This constant has a value of "UNAUTHORIZED"
    STATE_UNAUTHORIZED = "UNAUTHORIZED"

    #: A constant which can be used with the state property of a ManagementDashboardTileDetails.
    #: This constant has a value of "DEFAULT"
    STATE_DEFAULT = "DEFAULT"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementDashboardTileDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ManagementDashboardTileDetails.
        :type display_name: str

        :param saved_search_id:
            The value to assign to the saved_search_id property of this ManagementDashboardTileDetails.
        :type saved_search_id: str

        :param row:
            The value to assign to the row property of this ManagementDashboardTileDetails.
        :type row: int

        :param column:
            The value to assign to the column property of this ManagementDashboardTileDetails.
        :type column: int

        :param height:
            The value to assign to the height property of this ManagementDashboardTileDetails.
        :type height: int

        :param width:
            The value to assign to the width property of this ManagementDashboardTileDetails.
        :type width: int

        :param nls:
            The value to assign to the nls property of this ManagementDashboardTileDetails.
        :type nls: object

        :param ui_config:
            The value to assign to the ui_config property of this ManagementDashboardTileDetails.
        :type ui_config: object

        :param data_config:
            The value to assign to the data_config property of this ManagementDashboardTileDetails.
        :type data_config: list[object]

        :param state:
            The value to assign to the state property of this ManagementDashboardTileDetails.
            Allowed values for this property are: "DELETED", "UNAUTHORIZED", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param drilldown_config:
            The value to assign to the drilldown_config property of this ManagementDashboardTileDetails.
        :type drilldown_config: object

        :param parameters_map:
            The value to assign to the parameters_map property of this ManagementDashboardTileDetails.
        :type parameters_map: object

        """
        self.swagger_types = {
            'display_name': 'str',
            'saved_search_id': 'str',
            'row': 'int',
            'column': 'int',
            'height': 'int',
            'width': 'int',
            'nls': 'object',
            'ui_config': 'object',
            'data_config': 'list[object]',
            'state': 'str',
            'drilldown_config': 'object',
            'parameters_map': 'object'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'saved_search_id': 'savedSearchId',
            'row': 'row',
            'column': 'column',
            'height': 'height',
            'width': 'width',
            'nls': 'nls',
            'ui_config': 'uiConfig',
            'data_config': 'dataConfig',
            'state': 'state',
            'drilldown_config': 'drilldownConfig',
            'parameters_map': 'parametersMap'
        }

        self._display_name = None
        self._saved_search_id = None
        self._row = None
        self._column = None
        self._height = None
        self._width = None
        self._nls = None
        self._ui_config = None
        self._data_config = None
        self._state = None
        self._drilldown_config = None
        self._parameters_map = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ManagementDashboardTileDetails.
        Display name of the saved search.


        :return: The display_name of this ManagementDashboardTileDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementDashboardTileDetails.
        Display name of the saved search.


        :param display_name: The display_name of this ManagementDashboardTileDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def saved_search_id(self):
        """
        **[Required]** Gets the saved_search_id of this ManagementDashboardTileDetails.
        ID of the saved search.


        :return: The saved_search_id of this ManagementDashboardTileDetails.
        :rtype: str
        """
        return self._saved_search_id

    @saved_search_id.setter
    def saved_search_id(self, saved_search_id):
        """
        Sets the saved_search_id of this ManagementDashboardTileDetails.
        ID of the saved search.


        :param saved_search_id: The saved_search_id of this ManagementDashboardTileDetails.
        :type: str
        """
        self._saved_search_id = saved_search_id

    @property
    def row(self):
        """
        **[Required]** Gets the row of this ManagementDashboardTileDetails.
        Tile's row number.


        :return: The row of this ManagementDashboardTileDetails.
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row):
        """
        Sets the row of this ManagementDashboardTileDetails.
        Tile's row number.


        :param row: The row of this ManagementDashboardTileDetails.
        :type: int
        """
        self._row = row

    @property
    def column(self):
        """
        **[Required]** Gets the column of this ManagementDashboardTileDetails.
        Tile's column number.


        :return: The column of this ManagementDashboardTileDetails.
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this ManagementDashboardTileDetails.
        Tile's column number.


        :param column: The column of this ManagementDashboardTileDetails.
        :type: int
        """
        self._column = column

    @property
    def height(self):
        """
        **[Required]** Gets the height of this ManagementDashboardTileDetails.
        The number of rows the tile occupies.


        :return: The height of this ManagementDashboardTileDetails.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ManagementDashboardTileDetails.
        The number of rows the tile occupies.


        :param height: The height of this ManagementDashboardTileDetails.
        :type: int
        """
        self._height = height

    @property
    def width(self):
        """
        **[Required]** Gets the width of this ManagementDashboardTileDetails.
        The number of columns the tile occupies.


        :return: The width of this ManagementDashboardTileDetails.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ManagementDashboardTileDetails.
        The number of columns the tile occupies.


        :param width: The width of this ManagementDashboardTileDetails.
        :type: int
        """
        self._width = width

    @property
    def nls(self):
        """
        **[Required]** Gets the nls of this ManagementDashboardTileDetails.
        JSON that contains internationalization options.


        :return: The nls of this ManagementDashboardTileDetails.
        :rtype: object
        """
        return self._nls

    @nls.setter
    def nls(self, nls):
        """
        Sets the nls of this ManagementDashboardTileDetails.
        JSON that contains internationalization options.


        :param nls: The nls of this ManagementDashboardTileDetails.
        :type: object
        """
        self._nls = nls

    @property
    def ui_config(self):
        """
        **[Required]** Gets the ui_config of this ManagementDashboardTileDetails.
        JSON that contains user interface options.


        :return: The ui_config of this ManagementDashboardTileDetails.
        :rtype: object
        """
        return self._ui_config

    @ui_config.setter
    def ui_config(self, ui_config):
        """
        Sets the ui_config of this ManagementDashboardTileDetails.
        JSON that contains user interface options.


        :param ui_config: The ui_config of this ManagementDashboardTileDetails.
        :type: object
        """
        self._ui_config = ui_config

    @property
    def data_config(self):
        """
        **[Required]** Gets the data_config of this ManagementDashboardTileDetails.
        Array of JSON that contain data source options.


        :return: The data_config of this ManagementDashboardTileDetails.
        :rtype: list[object]
        """
        return self._data_config

    @data_config.setter
    def data_config(self, data_config):
        """
        Sets the data_config of this ManagementDashboardTileDetails.
        Array of JSON that contain data source options.


        :param data_config: The data_config of this ManagementDashboardTileDetails.
        :type: list[object]
        """
        self._data_config = data_config

    @property
    def state(self):
        """
        **[Required]** Gets the state of this ManagementDashboardTileDetails.
        Current state of the saved search.

        Allowed values for this property are: "DELETED", "UNAUTHORIZED", "DEFAULT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this ManagementDashboardTileDetails.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ManagementDashboardTileDetails.
        Current state of the saved search.


        :param state: The state of this ManagementDashboardTileDetails.
        :type: str
        """
        allowed_values = ["DELETED", "UNAUTHORIZED", "DEFAULT"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def drilldown_config(self):
        """
        **[Required]** Gets the drilldown_config of this ManagementDashboardTileDetails.
        Drill-down configuration to define the destination of a drill-down action.


        :return: The drilldown_config of this ManagementDashboardTileDetails.
        :rtype: object
        """
        return self._drilldown_config

    @drilldown_config.setter
    def drilldown_config(self, drilldown_config):
        """
        Sets the drilldown_config of this ManagementDashboardTileDetails.
        Drill-down configuration to define the destination of a drill-down action.


        :param drilldown_config: The drilldown_config of this ManagementDashboardTileDetails.
        :type: object
        """
        self._drilldown_config = drilldown_config

    @property
    def parameters_map(self):
        """
        Gets the parameters_map of this ManagementDashboardTileDetails.
        Specifies the saved search parameters values


        :return: The parameters_map of this ManagementDashboardTileDetails.
        :rtype: object
        """
        return self._parameters_map

    @parameters_map.setter
    def parameters_map(self, parameters_map):
        """
        Sets the parameters_map of this ManagementDashboardTileDetails.
        Specifies the saved search parameters values


        :param parameters_map: The parameters_map of this ManagementDashboardTileDetails.
        :type: object
        """
        self._parameters_map = parameters_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
