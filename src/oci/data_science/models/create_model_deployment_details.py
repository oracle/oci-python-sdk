# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateModelDeploymentDetails(object):
    """
    Parameters needed to create a new model deployment. Model deployments are used by data scientists to perform predictions from the model hosted on an HTTP server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateModelDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateModelDeploymentDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateModelDeploymentDetails.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this CreateModelDeploymentDetails.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateModelDeploymentDetails.
        :type compartment_id: str

        :param model_deployment_configuration_details:
            The value to assign to the model_deployment_configuration_details property of this CreateModelDeploymentDetails.
        :type model_deployment_configuration_details: oci.data_science.models.ModelDeploymentConfigurationDetails

        :param category_log_details:
            The value to assign to the category_log_details property of this CreateModelDeploymentDetails.
        :type category_log_details: oci.data_science.models.CategoryLogDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateModelDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateModelDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'model_deployment_configuration_details': 'ModelDeploymentConfigurationDetails',
            'category_log_details': 'CategoryLogDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'model_deployment_configuration_details': 'modelDeploymentConfigurationDetails',
            'category_log_details': 'categoryLogDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._project_id = None
        self._compartment_id = None
        self._model_deployment_configuration_details = None
        self._category_log_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateModelDeploymentDetails.
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
        Example: `My ModelDeployment`


        :return: The display_name of this CreateModelDeploymentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateModelDeploymentDetails.
        A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information.
        Example: `My ModelDeployment`


        :param display_name: The display_name of this CreateModelDeploymentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateModelDeploymentDetails.
        A short description of the model deployment.


        :return: The description of this CreateModelDeploymentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateModelDeploymentDetails.
        A short description of the model deployment.


        :param description: The description of this CreateModelDeploymentDetails.
        :type: str
        """
        self._description = description

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateModelDeploymentDetails.
        The `OCID`__ of the project to associate with the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateModelDeploymentDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateModelDeploymentDetails.
        The `OCID`__ of the project to associate with the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateModelDeploymentDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateModelDeploymentDetails.
        The `OCID`__ of the compartment where you want to create the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateModelDeploymentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateModelDeploymentDetails.
        The `OCID`__ of the compartment where you want to create the model deployment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateModelDeploymentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def model_deployment_configuration_details(self):
        """
        **[Required]** Gets the model_deployment_configuration_details of this CreateModelDeploymentDetails.

        :return: The model_deployment_configuration_details of this CreateModelDeploymentDetails.
        :rtype: oci.data_science.models.ModelDeploymentConfigurationDetails
        """
        return self._model_deployment_configuration_details

    @model_deployment_configuration_details.setter
    def model_deployment_configuration_details(self, model_deployment_configuration_details):
        """
        Sets the model_deployment_configuration_details of this CreateModelDeploymentDetails.

        :param model_deployment_configuration_details: The model_deployment_configuration_details of this CreateModelDeploymentDetails.
        :type: oci.data_science.models.ModelDeploymentConfigurationDetails
        """
        self._model_deployment_configuration_details = model_deployment_configuration_details

    @property
    def category_log_details(self):
        """
        Gets the category_log_details of this CreateModelDeploymentDetails.

        :return: The category_log_details of this CreateModelDeploymentDetails.
        :rtype: oci.data_science.models.CategoryLogDetails
        """
        return self._category_log_details

    @category_log_details.setter
    def category_log_details(self, category_log_details):
        """
        Sets the category_log_details of this CreateModelDeploymentDetails.

        :param category_log_details: The category_log_details of this CreateModelDeploymentDetails.
        :type: oci.data_science.models.CategoryLogDetails
        """
        self._category_log_details = category_log_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateModelDeploymentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateModelDeploymentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateModelDeploymentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateModelDeploymentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateModelDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateModelDeploymentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateModelDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateModelDeploymentDetails.
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
