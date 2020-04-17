# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetDetails(object):
    """
    Properties used in data asset create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDataAssetDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDataAssetDetails.
        :type description: str

        :param type_key:
            The value to assign to the type_key property of this CreateDataAssetDetails.
        :type type_key: str

        :param properties:
            The value to assign to the properties property of this CreateDataAssetDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'type_key': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'type_key': 'typeKey',
            'properties': 'properties'
        }

        self._display_name = None
        self._description = None
        self._type_key = None
        self._properties = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDataAssetDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDataAssetDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateDataAssetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDataAssetDetails.
        Detailed description of the data asset.


        :return: The description of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDataAssetDetails.
        Detailed description of the data asset.


        :param description: The description of this CreateDataAssetDetails.
        :type: str
        """
        self._description = description

    @property
    def type_key(self):
        """
        **[Required]** Gets the type_key of this CreateDataAssetDetails.
        The key of the data asset type. This can be obtained via the '/types' endpoint.


        :return: The type_key of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._type_key

    @type_key.setter
    def type_key(self, type_key):
        """
        Sets the type_key of this CreateDataAssetDetails.
        The key of the data asset type. This can be obtained via the '/types' endpoint.


        :param type_key: The type_key of this CreateDataAssetDetails.
        :type: str
        """
        self._type_key = type_key

    @property
    def properties(self):
        """
        Gets the properties of this CreateDataAssetDetails.
        A map of maps that contains the properties which are specific to the data asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category. To determine the set of optional and
        required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a
        collection of all data asset types. The appropriate data asset type, which includes definitions of all of
        it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this CreateDataAssetDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateDataAssetDetails.
        A map of maps that contains the properties which are specific to the data asset type. Each data asset type
        definition defines it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        data assets have required properties within the \"default\" category. To determine the set of optional and
        required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a
        collection of all data asset types. The appropriate data asset type, which includes definitions of all of
        it's properties, can be identified from this collection.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this CreateDataAssetDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
