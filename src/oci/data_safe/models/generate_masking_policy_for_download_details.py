# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateMaskingPolicyForDownloadDetails(object):
    """
    Details to generate a downloadable masking policy.
    """

    #: A constant which can be used with the policy_format property of a GenerateMaskingPolicyForDownloadDetails.
    #: This constant has a value of "XML"
    POLICY_FORMAT_XML = "XML"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateMaskingPolicyForDownloadDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_format:
            The value to assign to the policy_format property of this GenerateMaskingPolicyForDownloadDetails.
            Allowed values for this property are: "XML"
        :type policy_format: str

        """
        self.swagger_types = {
            'policy_format': 'str'
        }

        self.attribute_map = {
            'policy_format': 'policyFormat'
        }

        self._policy_format = None

    @property
    def policy_format(self):
        """
        Gets the policy_format of this GenerateMaskingPolicyForDownloadDetails.
        The format of the masking policy file.

        Allowed values for this property are: "XML"


        :return: The policy_format of this GenerateMaskingPolicyForDownloadDetails.
        :rtype: str
        """
        return self._policy_format

    @policy_format.setter
    def policy_format(self, policy_format):
        """
        Sets the policy_format of this GenerateMaskingPolicyForDownloadDetails.
        The format of the masking policy file.


        :param policy_format: The policy_format of this GenerateMaskingPolicyForDownloadDetails.
        :type: str
        """
        allowed_values = ["XML"]
        if not value_allowed_none_or_none_sentinel(policy_format, allowed_values):
            raise ValueError(
                "Invalid value for `policy_format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._policy_format = policy_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
