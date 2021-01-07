# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IncidentType(object):
    """
    Details about the incident type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IncidentType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IncidentType.
        :type id: str

        :param name:
            The value to assign to the name property of this IncidentType.
        :type name: str

        :param label:
            The value to assign to the label property of this IncidentType.
        :type label: str

        :param description:
            The value to assign to the description property of this IncidentType.
        :type description: str

        :param classifier_list:
            The value to assign to the classifier_list property of this IncidentType.
        :type classifier_list: list[oci.cims.models.Classifier]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'label': 'str',
            'description': 'str',
            'classifier_list': 'list[Classifier]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'label': 'label',
            'description': 'description',
            'classifier_list': 'classifierList'
        }

        self._id = None
        self._name = None
        self._label = None
        self._description = None
        self._classifier_list = None

    @property
    def id(self):
        """
        Gets the id of this IncidentType.
        Unique identifier for the incident type.


        :return: The id of this IncidentType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IncidentType.
        Unique identifier for the incident type.


        :param id: The id of this IncidentType.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this IncidentType.
        The name of the incident type.


        :return: The name of this IncidentType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IncidentType.
        The name of the incident type.


        :param name: The name of this IncidentType.
        :type: str
        """
        self._name = name

    @property
    def label(self):
        """
        Gets the label of this IncidentType.
        The label associated with the incident type.


        :return: The label of this IncidentType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this IncidentType.
        The label associated with the incident type.


        :param label: The label of this IncidentType.
        :type: str
        """
        self._label = label

    @property
    def description(self):
        """
        Gets the description of this IncidentType.
        The description of the incident type.


        :return: The description of this IncidentType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IncidentType.
        The description of the incident type.


        :param description: The description of this IncidentType.
        :type: str
        """
        self._description = description

    @property
    def classifier_list(self):
        """
        Gets the classifier_list of this IncidentType.
        The list of classifiers.


        :return: The classifier_list of this IncidentType.
        :rtype: list[oci.cims.models.Classifier]
        """
        return self._classifier_list

    @classifier_list.setter
    def classifier_list(self, classifier_list):
        """
        Sets the classifier_list of this IncidentType.
        The list of classifiers.


        :param classifier_list: The classifier_list of this IncidentType.
        :type: list[oci.cims.models.Classifier]
        """
        self._classifier_list = classifier_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
