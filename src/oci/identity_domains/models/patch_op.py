# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchOp(object):
    """
    See `Section 3.5.2`__. HTTP PATCH is an OPTIONAL server function that enables clients to update one or more attributes of a SCIM resource using a sequence of operations to \"add\", \"remove\", or \"replace\" values. Clients may discover service provider support for PATCH by querying the service provider configuration. The general form of the SCIM patch request is based on JavaScript Object Notation (JSON) Patch [RFC6902]. One difference between SCIM patch and JSON patch is that SCIM servers do not support array indexing and do not support [RFC6902] operation types relating to array element manipulation such as \"move\". A patch request, regardless of the number of operations, SHALL be treated as atomic. If a single operation encounters an error condition, the original SCIM resource MUST be restored, and a failure status SHALL be returned.

    __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.5.2
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchOp object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schemas:
            The value to assign to the schemas property of this PatchOp.
        :type schemas: list[str]

        :param operations:
            The value to assign to the operations property of this PatchOp.
        :type operations: list[oci.identity_domains.models.Operations]

        """
        self.swagger_types = {
            'schemas': 'list[str]',
            'operations': 'list[Operations]'
        }

        self.attribute_map = {
            'schemas': 'schemas',
            'operations': 'Operations'
        }

        self._schemas = None
        self._operations = None

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this PatchOp.
        The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior. REQUIRED.


        :return: The schemas of this PatchOp.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this PatchOp.
        The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior. REQUIRED.


        :param schemas: The schemas of this PatchOp.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def operations(self):
        """
        **[Required]** Gets the operations of this PatchOp.
        The body of an HTTP PATCH request MUST contain the attribute \"Operations\", whose value is an array of one or more patch operations.


        :return: The operations of this PatchOp.
        :rtype: list[oci.identity_domains.models.Operations]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this PatchOp.
        The body of an HTTP PATCH request MUST contain the attribute \"Operations\", whose value is an array of one or more patch operations.


        :param operations: The operations of this PatchOp.
        :type: list[oci.identity_domains.models.Operations]
        """
        self._operations = operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
