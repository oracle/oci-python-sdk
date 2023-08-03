# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppFormFillUrlMatch(object):
    """
    A list of application-formURLs that FormFill should match against any formUrl that the user-specifies when signing in to the target service.  Each item in the list also indicates how FormFill should interpret that formUrl.

    **SCIM++ Properties:**
    - idcsCompositeKey: [formUrl]
    - multiValued: true
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppFormFillUrlMatch object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param form_url_match_type:
            The value to assign to the form_url_match_type property of this AppFormFillUrlMatch.
        :type form_url_match_type: str

        :param form_url:
            The value to assign to the form_url property of this AppFormFillUrlMatch.
        :type form_url: str

        """
        self.swagger_types = {
            'form_url_match_type': 'str',
            'form_url': 'str'
        }

        self.attribute_map = {
            'form_url_match_type': 'formUrlMatchType',
            'form_url': 'formUrl'
        }

        self._form_url_match_type = None
        self._form_url = None

    @property
    def form_url_match_type(self):
        """
        Gets the form_url_match_type of this AppFormFillUrlMatch.
        Indicates how to interpret the value of 'formUrl' when matching against a user-specified formUrl.  The system currently supports only 'Exact', which indicates that the value of 'formUrl' should be treated as a literal value.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The form_url_match_type of this AppFormFillUrlMatch.
        :rtype: str
        """
        return self._form_url_match_type

    @form_url_match_type.setter
    def form_url_match_type(self, form_url_match_type):
        """
        Sets the form_url_match_type of this AppFormFillUrlMatch.
        Indicates how to interpret the value of 'formUrl' when matching against a user-specified formUrl.  The system currently supports only 'Exact', which indicates that the value of 'formUrl' should be treated as a literal value.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param form_url_match_type: The form_url_match_type of this AppFormFillUrlMatch.
        :type: str
        """
        self._form_url_match_type = form_url_match_type

    @property
    def form_url(self):
        """
        **[Required]** Gets the form_url of this AppFormFillUrlMatch.
        An application formUrl that FormFill will match against any formUrl that a User enters in trying to access the target-service which this App represents.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The form_url of this AppFormFillUrlMatch.
        :rtype: str
        """
        return self._form_url

    @form_url.setter
    def form_url(self, form_url):
        """
        Sets the form_url of this AppFormFillUrlMatch.
        An application formUrl that FormFill will match against any formUrl that a User enters in trying to access the target-service which this App represents.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param form_url: The form_url of this AppFormFillUrlMatch.
        :type: str
        """
        self._form_url = form_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
