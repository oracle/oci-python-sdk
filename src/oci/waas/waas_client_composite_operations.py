# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class WaasClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.waas.WaasClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new WaasClientCompositeOperations object

        :param WaasClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def accept_recommendations_and_wait_for_state(self, waas_policy_id, protection_rule_keys, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.accept_recommendations` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] protection_rule_keys: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.accept_recommendations`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.accept_recommendations(waas_policy_id, protection_rule_keys, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_address_list_and_wait_for_state(self, create_address_list_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.create_address_list` and waits for the :py:class:`~oci.waas.models.AddressList` acted upon
        to enter the given state(s).

        :param oci.waas.models.CreateAddressListDetails create_address_list_details: (required)
            The details of the address list resource to create.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.AddressList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.create_address_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_address_list(create_address_list_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        address_list_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_address_list(address_list_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_certificate_and_wait_for_state(self, create_certificate_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.create_certificate` and waits for the :py:class:`~oci.waas.models.Certificate` acted upon
        to enter the given state(s).

        :param oci.waas.models.CreateCertificateDetails create_certificate_details: (required)
            The details of the SSL certificate resource to create.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.Certificate.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.create_certificate`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_certificate(create_certificate_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        certificate_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_certificate(certificate_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_custom_protection_rule_and_wait_for_state(self, create_custom_protection_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.create_custom_protection_rule` and waits for the :py:class:`~oci.waas.models.CustomProtectionRule` acted upon
        to enter the given state(s).

        :param oci.waas.models.CreateCustomProtectionRuleDetails create_custom_protection_rule_details: (required)
            The details of the custom protection rule.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.CustomProtectionRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.create_custom_protection_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_custom_protection_rule(create_custom_protection_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        custom_protection_rule_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_custom_protection_rule(custom_protection_rule_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_waas_policy_and_wait_for_state(self, create_waas_policy_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.create_waas_policy` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param oci.waas.models.CreateWaasPolicyDetails create_waas_policy_details: (required)
            The details of the WAAS policy.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.create_waas_policy`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_waas_policy(create_waas_policy_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_address_list_and_wait_for_state(self, address_list_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.delete_address_list` and waits for the :py:class:`~oci.waas.models.AddressList` acted upon
        to enter the given state(s).

        :param str address_list_id: (required)
            The `OCID`__ of the address list. This number is generated when the address list is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.AddressList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.delete_address_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_address_list(address_list_id)
        operation_result = None
        try:
            operation_result = self.client.delete_address_list(address_list_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_certificate_and_wait_for_state(self, certificate_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.delete_certificate` and waits for the :py:class:`~oci.waas.models.Certificate` acted upon
        to enter the given state(s).

        :param str certificate_id: (required)
            The `OCID`__ of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.Certificate.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.delete_certificate`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_certificate(certificate_id)
        operation_result = None
        try:
            operation_result = self.client.delete_certificate(certificate_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_custom_protection_rule_and_wait_for_state(self, custom_protection_rule_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.delete_custom_protection_rule` and waits for the :py:class:`~oci.waas.models.CustomProtectionRule` acted upon
        to enter the given state(s).

        :param str custom_protection_rule_id: (required)
            The `OCID`__ of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.CustomProtectionRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.delete_custom_protection_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_custom_protection_rule(custom_protection_rule_id)
        operation_result = None
        try:
            operation_result = self.client.delete_custom_protection_rule(custom_protection_rule_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_waas_policy_and_wait_for_state(self, waas_policy_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.delete_waas_policy` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.delete_waas_policy`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = None
        try:
            operation_result = self.client.delete_waas_policy(waas_policy_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def purge_cache_and_wait_for_state(self, waas_policy_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.purge_cache` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.purge_cache`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.purge_cache(waas_policy_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_access_rules_and_wait_for_state(self, waas_policy_id, access_rules, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_access_rules` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[AccessRule] access_rules: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_access_rules`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_access_rules(waas_policy_id, access_rules, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_address_list_and_wait_for_state(self, address_list_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_address_list` and waits for the :py:class:`~oci.waas.models.AddressList` acted upon
        to enter the given state(s).

        :param str address_list_id: (required)
            The `OCID`__ of the address list. This number is generated when the address list is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.AddressList.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_address_list`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_address_list(address_list_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        address_list_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_address_list(address_list_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_caching_rules_and_wait_for_state(self, waas_policy_id, caching_rules_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_caching_rules` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[CachingRule] caching_rules_details: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_caching_rules`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_caching_rules(waas_policy_id, caching_rules_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_captchas_and_wait_for_state(self, waas_policy_id, captchas, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_captchas` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[Captcha] captchas: (required)
            A list of CAPTCHA details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_captchas`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_captchas(waas_policy_id, captchas, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_certificate_and_wait_for_state(self, certificate_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_certificate` and waits for the :py:class:`~oci.waas.models.Certificate` acted upon
        to enter the given state(s).

        :param str certificate_id: (required)
            The `OCID`__ of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.Certificate.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_certificate`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_certificate(certificate_id, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        certificate_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_certificate(certificate_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_custom_protection_rule_and_wait_for_state(self, custom_protection_rule_id, update_custom_protection_rule_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_custom_protection_rule` and waits for the :py:class:`~oci.waas.models.CustomProtectionRule` acted upon
        to enter the given state(s).

        :param str custom_protection_rule_id: (required)
            The `OCID`__ of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.UpdateCustomProtectionRuleDetails update_custom_protection_rule_details: (required)
            The details of the custom protection rule to update.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.CustomProtectionRule.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_custom_protection_rule`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_custom_protection_rule(custom_protection_rule_id, update_custom_protection_rule_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        custom_protection_rule_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_custom_protection_rule(custom_protection_rule_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_device_fingerprint_challenge_and_wait_for_state(self, waas_policy_id, update_device_fingerprint_challenge_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_device_fingerprint_challenge` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.DeviceFingerprintChallenge update_device_fingerprint_challenge_details: (required)
            The device fingerprint challenge settings to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_device_fingerprint_challenge`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_device_fingerprint_challenge(waas_policy_id, update_device_fingerprint_challenge_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_good_bots_and_wait_for_state(self, waas_policy_id, good_bots, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_good_bots` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[GoodBot] good_bots: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_good_bots`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_good_bots(waas_policy_id, good_bots, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_human_interaction_challenge_and_wait_for_state(self, waas_policy_id, update_human_interaction_challenge_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_human_interaction_challenge` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.HumanInteractionChallenge update_human_interaction_challenge_details: (required)
            The human interaction challenge settings.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_human_interaction_challenge`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_human_interaction_challenge(waas_policy_id, update_human_interaction_challenge_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_js_challenge_and_wait_for_state(self, waas_policy_id, update_js_challenge_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_js_challenge` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.JsChallenge update_js_challenge_details: (required)
            The JavaScript challenge settings to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_js_challenge`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_js_challenge(waas_policy_id, update_js_challenge_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_policy_config_and_wait_for_state(self, waas_policy_id, update_policy_config_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_policy_config` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.PolicyConfig update_policy_config_details: (required)
            The new configuration to apply to a WAAS policy.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_policy_config`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_policy_config(waas_policy_id, update_policy_config_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_protection_rules_and_wait_for_state(self, waas_policy_id, protection_rules, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_protection_rules` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[ProtectionRuleAction] protection_rules: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_protection_rules`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_protection_rules(waas_policy_id, protection_rules, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_protection_settings_and_wait_for_state(self, waas_policy_id, update_protection_settings_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_protection_settings` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.ProtectionSettings update_protection_settings_details: (required)
            The details of the protection settings to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_protection_settings`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_protection_settings(waas_policy_id, update_protection_settings_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_threat_feeds_and_wait_for_state(self, waas_policy_id, threat_feeds, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_threat_feeds` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[ThreatFeedAction] threat_feeds: (required)
            A list of threat feeds for which to update the actions.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_threat_feeds`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_threat_feeds(waas_policy_id, threat_feeds, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_waas_policy_and_wait_for_state(self, waas_policy_id, update_waas_policy_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_waas_policy` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.UpdateWaasPolicyDetails update_waas_policy_details: (required)
            The details of the WAAS policy to update.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_waas_policy`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_waas_policy(waas_policy_id, update_waas_policy_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_waas_policy_custom_protection_rules_and_wait_for_state(self, waas_policy_id, update_custom_protection_rules_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_waas_policy_custom_protection_rules` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[CustomProtectionRuleSetting] update_custom_protection_rules_details: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_waas_policy_custom_protection_rules`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_waas_policy_custom_protection_rules(waas_policy_id, update_custom_protection_rules_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_waf_address_rate_limiting_and_wait_for_state(self, waas_policy_id, update_waf_address_rate_limiting_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_waf_address_rate_limiting` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.AddressRateLimiting update_waf_address_rate_limiting_details: (required)
            The address rate limiting settings.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_waf_address_rate_limiting`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_waf_address_rate_limiting(waas_policy_id, update_waf_address_rate_limiting_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_waf_config_and_wait_for_state(self, waas_policy_id, update_waf_config_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_waf_config` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.WafConfig update_waf_config_details: (required)
            The new Web Application Firewall configuration to apply to a WAAS policy.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_waf_config`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_waf_config(waas_policy_id, update_waf_config_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_whitelists_and_wait_for_state(self, waas_policy_id, whitelists, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.waas.WaasClient.update_whitelists` and waits for the :py:class:`~oci.waas.models.WorkRequest`
        to enter the given state(s).

        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[Whitelist] whitelists: (required)

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.waas.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.waas.WaasClient.update_whitelists`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_whitelists(waas_policy_id, whitelists, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
