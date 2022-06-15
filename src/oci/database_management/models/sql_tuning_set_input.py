# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningSetInput(object):
    """
    The SQL tuning set for a SQL tuning task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningSetInput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SqlTuningSetInput.
        :type name: str

        :param owner:
            The value to assign to the owner property of this SqlTuningSetInput.
        :type owner: str

        """
        self.swagger_types = {
            'name': 'str',
            'owner': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'owner': 'owner'
        }

        self._name = None
        self._owner = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlTuningSetInput.
        The name of the SQL tuning set.


        :return: The name of this SqlTuningSetInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlTuningSetInput.
        The name of the SQL tuning set.


        :param name: The name of this SqlTuningSetInput.
        :type: str
        """
        self._name = name

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this SqlTuningSetInput.
        The owner of the SQL tuning set.


        :return: The owner of this SqlTuningSetInput.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SqlTuningSetInput.
        The owner of the SQL tuning set.


        :param owner: The owner of this SqlTuningSetInput.
        :type: str
        """
        self._owner = owner

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
