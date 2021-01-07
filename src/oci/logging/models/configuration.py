# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    Log object configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Configuration.
        :type compartment_id: str

        :param source:
            The value to assign to the source property of this Configuration.
        :type source: oci.logging.models.Source

        :param archiving:
            The value to assign to the archiving property of this Configuration.
        :type archiving: oci.logging.models.Archiving

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'source': 'Source',
            'archiving': 'Archiving'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'source': 'source',
            'archiving': 'archiving'
        }

        self._compartment_id = None
        self._source = None
        self._archiving = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Configuration.
        The OCID of the compartment that the resource belongs to.


        :return: The compartment_id of this Configuration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Configuration.
        The OCID of the compartment that the resource belongs to.


        :param compartment_id: The compartment_id of this Configuration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source(self):
        """
        **[Required]** Gets the source of this Configuration.

        :return: The source of this Configuration.
        :rtype: oci.logging.models.Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Configuration.

        :param source: The source of this Configuration.
        :type: oci.logging.models.Source
        """
        self._source = source

    @property
    def archiving(self):
        """
        Gets the archiving of this Configuration.

        :return: The archiving of this Configuration.
        :rtype: oci.logging.models.Archiving
        """
        return self._archiving

    @archiving.setter
    def archiving(self, archiving):
        """
        Sets the archiving of this Configuration.

        :param archiving: The archiving of this Configuration.
        :type: oci.logging.models.Archiving
        """
        self._archiving = archiving

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
