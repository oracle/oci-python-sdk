# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PutRepositoryRefDetails(object):
    """
    The information needed to create a reference. If the reference already exists, then it can be used to update the reference.
    """

    #: A constant which can be used with the ref_type property of a PutRepositoryRefDetails.
    #: This constant has a value of "BRANCH"
    REF_TYPE_BRANCH = "BRANCH"

    #: A constant which can be used with the ref_type property of a PutRepositoryRefDetails.
    #: This constant has a value of "TAG"
    REF_TYPE_TAG = "TAG"

    def __init__(self, **kwargs):
        """
        Initializes a new PutRepositoryRefDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.PutRepositoryTagDetails`
        * :class:`~oci.devops.models.PutRepositoryBranchDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ref_type:
            The value to assign to the ref_type property of this PutRepositoryRefDetails.
            Allowed values for this property are: "BRANCH", "TAG"
        :type ref_type: str

        """
        self.swagger_types = {
            'ref_type': 'str'
        }

        self.attribute_map = {
            'ref_type': 'refType'
        }

        self._ref_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['refType']

        if type == 'TAG':
            return 'PutRepositoryTagDetails'

        if type == 'BRANCH':
            return 'PutRepositoryBranchDetails'
        else:
            return 'PutRepositoryRefDetails'

    @property
    def ref_type(self):
        """
        **[Required]** Gets the ref_type of this PutRepositoryRefDetails.
        The type of reference (Branch or Tag).

        Allowed values for this property are: "BRANCH", "TAG"


        :return: The ref_type of this PutRepositoryRefDetails.
        :rtype: str
        """
        return self._ref_type

    @ref_type.setter
    def ref_type(self, ref_type):
        """
        Sets the ref_type of this PutRepositoryRefDetails.
        The type of reference (Branch or Tag).


        :param ref_type: The ref_type of this PutRepositoryRefDetails.
        :type: str
        """
        allowed_values = ["BRANCH", "TAG"]
        if not value_allowed_none_or_none_sentinel(ref_type, allowed_values):
            raise ValueError(
                "Invalid value for `ref_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ref_type = ref_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
