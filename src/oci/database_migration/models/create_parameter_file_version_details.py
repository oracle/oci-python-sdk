# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateParameterFileVersionDetails(object):
    """
    Details about a specific ParameterFileVersion
    """

    #: A constant which can be used with the kind property of a CreateParameterFileVersionDetails.
    #: This constant has a value of "EXTRACT"
    KIND_EXTRACT = "EXTRACT"

    #: A constant which can be used with the kind property of a CreateParameterFileVersionDetails.
    #: This constant has a value of "REPLICAT"
    KIND_REPLICAT = "REPLICAT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateParameterFileVersionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateParameterFileVersionDetails.
        :type description: str

        :param kind:
            The value to assign to the kind property of this CreateParameterFileVersionDetails.
            Allowed values for this property are: "EXTRACT", "REPLICAT"
        :type kind: str

        :param content:
            The value to assign to the content property of this CreateParameterFileVersionDetails.
        :type content: str

        :param name:
            The value to assign to the name property of this CreateParameterFileVersionDetails.
        :type name: str

        """
        self.swagger_types = {
            'description': 'str',
            'kind': 'str',
            'content': 'str',
            'name': 'str'
        }
        self.attribute_map = {
            'description': 'description',
            'kind': 'kind',
            'content': 'content',
            'name': 'name'
        }
        self._description = None
        self._kind = None
        self._content = None
        self._name = None

    @property
    def description(self):
        """
        Gets the description of this CreateParameterFileVersionDetails.
        Describes the current parameter file version


        :return: The description of this CreateParameterFileVersionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateParameterFileVersionDetails.
        Describes the current parameter file version


        :param description: The description of this CreateParameterFileVersionDetails.
        :type: str
        """
        self._description = description

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this CreateParameterFileVersionDetails.
        Indicator of Parameter File 'kind' (for an EXTRACT or a REPLICAT)

        Allowed values for this property are: "EXTRACT", "REPLICAT"


        :return: The kind of this CreateParameterFileVersionDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this CreateParameterFileVersionDetails.
        Indicator of Parameter File 'kind' (for an EXTRACT or a REPLICAT)


        :param kind: The kind of this CreateParameterFileVersionDetails.
        :type: str
        """
        allowed_values = ["EXTRACT", "REPLICAT"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            raise ValueError(
                f"Invalid value for `kind`, must be None or one of {allowed_values}"
            )
        self._kind = kind

    @property
    def content(self):
        """
        **[Required]** Gets the content of this CreateParameterFileVersionDetails.
        The content in base64 encoded character string containing the value of the parameter file


        :return: The content of this CreateParameterFileVersionDetails.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CreateParameterFileVersionDetails.
        The content in base64 encoded character string containing the value of the parameter file


        :param content: The content of this CreateParameterFileVersionDetails.
        :type: str
        """
        self._content = content

    @property
    def name(self):
        """
        Gets the name of this CreateParameterFileVersionDetails.
        Customizable name for the paramenter file version.


        :return: The name of this CreateParameterFileVersionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateParameterFileVersionDetails.
        Customizable name for the paramenter file version.


        :param name: The name of this CreateParameterFileVersionDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
