# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetDetails(object):
    """
    Parameters needed to create a new data asset.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDataAssetDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDataAssetDetails.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this CreateDataAssetDetails.
        :type project_id: str

        :param description:
            The value to assign to the description property of this CreateDataAssetDetails.
        :type description: str

        :param data_source_details:
            The value to assign to the data_source_details property of this CreateDataAssetDetails.
        :type data_source_details: oci.ai_anomaly_detection.models.DataSourceDetails

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this CreateDataAssetDetails.
        :type private_endpoint_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDataAssetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDataAssetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'description': 'str',
            'data_source_details': 'DataSourceDetails',
            'private_endpoint_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'description': 'description',
            'data_source_details': 'dataSourceDetails',
            'private_endpoint_id': 'privateEndpointId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._project_id = None
        self._description = None
        self._data_source_details = None
        self._private_endpoint_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDataAssetDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :return: The display_name of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDataAssetDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDataAssetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDataAssetDetails.
        The OCID for the data asset's compartment.


        :return: The compartment_id of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDataAssetDetails.
        The OCID for the data asset's compartment.


        :param compartment_id: The compartment_id of this CreateDataAssetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateDataAssetDetails.
        The `OCID`__ of the project to associate with the data asset.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateDataAssetDetails.
        The `OCID`__ of the project to associate with the data asset.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateDataAssetDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """
        Gets the description of this CreateDataAssetDetails.
        A short description of the Ai data asset


        :return: The description of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDataAssetDetails.
        A short description of the Ai data asset


        :param description: The description of this CreateDataAssetDetails.
        :type: str
        """
        self._description = description

    @property
    def data_source_details(self):
        """
        **[Required]** Gets the data_source_details of this CreateDataAssetDetails.

        :return: The data_source_details of this CreateDataAssetDetails.
        :rtype: oci.ai_anomaly_detection.models.DataSourceDetails
        """
        return self._data_source_details

    @data_source_details.setter
    def data_source_details(self, data_source_details):
        """
        Sets the data_source_details of this CreateDataAssetDetails.

        :param data_source_details: The data_source_details of this CreateDataAssetDetails.
        :type: oci.ai_anomaly_detection.models.DataSourceDetails
        """
        self._data_source_details = data_source_details

    @property
    def private_endpoint_id(self):
        """
        Gets the private_endpoint_id of this CreateDataAssetDetails.
        OCID of Private Endpoint.


        :return: The private_endpoint_id of this CreateDataAssetDetails.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this CreateDataAssetDetails.
        OCID of Private Endpoint.


        :param private_endpoint_id: The private_endpoint_id of this CreateDataAssetDetails.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDataAssetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDataAssetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDataAssetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDataAssetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDataAssetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDataAssetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDataAssetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDataAssetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
