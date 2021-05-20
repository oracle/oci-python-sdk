# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class ArtifactsClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.artifacts.ArtifactsClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new ArtifactsClientCompositeOperations object

        :param ArtifactsClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def create_container_repository_and_wait_for_state(self, create_container_repository_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.create_container_repository` and waits for the :py:class:`~oci.artifacts.models.ContainerRepository` acted upon
        to enter the given state(s).

        :param oci.artifacts.models.CreateContainerRepositoryDetails create_container_repository_details: (required)
            Create container repository details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.ContainerRepository.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.create_container_repository`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_container_repository(create_container_repository_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_container_repository(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_repository_and_wait_for_state(self, create_repository_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.create_repository` and waits for the :py:class:`~oci.artifacts.models.Repository` acted upon
        to enter the given state(s).

        :param oci.artifacts.models.CreateRepositoryDetails create_repository_details: (required)
            Creates a new repository for storing artifacts.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.Repository.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.create_repository`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_repository(create_repository_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_repository(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_container_image_and_wait_for_state(self, image_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.delete_container_image` and waits for the :py:class:`~oci.artifacts.models.ContainerImage` acted upon
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the container image.

            Example: `ocid1.containerimage.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.ContainerImage.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.delete_container_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_container_image(image_id)
        operation_result = None
        try:
            operation_result = self.client.delete_container_image(image_id, **operation_kwargs)
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
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_container_repository_and_wait_for_state(self, repository_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.delete_container_repository` and waits for the :py:class:`~oci.artifacts.models.ContainerRepository` acted upon
        to enter the given state(s).

        :param str repository_id: (required)
            The `OCID`__ of the container repository.

            Example: `ocid1.containerrepo.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.ContainerRepository.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.delete_container_repository`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_container_repository(repository_id)
        operation_result = None
        try:
            operation_result = self.client.delete_container_repository(repository_id, **operation_kwargs)
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
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_generic_artifact_and_wait_for_state(self, artifact_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.delete_generic_artifact` and waits for the :py:class:`~oci.artifacts.models.GenericArtifact` acted upon
        to enter the given state(s).

        :param str artifact_id: (required)
            The `OCID`__ of the artifact.

            Example: `ocid1.genericartifact.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.GenericArtifact.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.delete_generic_artifact`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_generic_artifact(artifact_id)
        operation_result = None
        try:
            operation_result = self.client.delete_generic_artifact(artifact_id, **operation_kwargs)
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
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_repository_and_wait_for_state(self, repository_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.delete_repository` and waits for the :py:class:`~oci.artifacts.models.Repository` acted upon
        to enter the given state(s).

        :param str repository_id: (required)
            The `OCID`__ of the repository.

            Example: `ocid1.artifactrepository.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.Repository.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.delete_repository`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_repository(repository_id)
        operation_result = None
        try:
            operation_result = self.client.delete_repository(repository_id, **operation_kwargs)
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
                initial_get_result,
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                succeed_on_not_found=True,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def remove_container_version_and_wait_for_state(self, image_id, remove_container_version_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.remove_container_version` and waits for the :py:class:`~oci.artifacts.models.ContainerImage` acted upon
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the container image.

            Example: `ocid1.containerimage.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.artifacts.models.RemoveContainerVersionDetails remove_container_version_details: (required)
            Remove version details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.ContainerImage.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.remove_container_version`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.remove_container_version(image_id, remove_container_version_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_container_image(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def restore_container_image_and_wait_for_state(self, image_id, restore_container_image_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.restore_container_image` and waits for the :py:class:`~oci.artifacts.models.ContainerImage` acted upon
        to enter the given state(s).

        :param str image_id: (required)
            The `OCID`__ of the container image.

            Example: `ocid1.containerimage.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.artifacts.models.RestoreContainerImageDetails restore_container_image_details: (required)
            Restore container image details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.ContainerImage.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.restore_container_image`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.restore_container_image(image_id, restore_container_image_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_container_image(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_container_repository_and_wait_for_state(self, repository_id, update_container_repository_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.update_container_repository` and waits for the :py:class:`~oci.artifacts.models.ContainerRepository` acted upon
        to enter the given state(s).

        :param str repository_id: (required)
            The `OCID`__ of the container repository.

            Example: `ocid1.containerrepo.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.artifacts.models.UpdateContainerRepositoryDetails update_container_repository_details: (required)
            Update container repository details.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.ContainerRepository.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.update_container_repository`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_container_repository(repository_id, update_container_repository_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_container_repository(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_generic_artifact_and_wait_for_state(self, artifact_id, update_generic_artifact_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.update_generic_artifact` and waits for the :py:class:`~oci.artifacts.models.GenericArtifact` acted upon
        to enter the given state(s).

        :param str artifact_id: (required)
            The `OCID`__ of the artifact.

            Example: `ocid1.genericartifact.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.artifacts.models.UpdateGenericArtifactDetails update_generic_artifact_details: (required)
            Updates the artifact with the specified `OCID`__. You can only update the tags of an artifact.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.GenericArtifact.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.update_generic_artifact`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_generic_artifact(artifact_id, update_generic_artifact_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_generic_artifact(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_repository_and_wait_for_state(self, repository_id, update_repository_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.artifacts.ArtifactsClient.update_repository` and waits for the :py:class:`~oci.artifacts.models.Repository` acted upon
        to enter the given state(s).

        :param str repository_id: (required)
            The `OCID`__ of the repository.

            Example: `ocid1.artifactrepository.oc1..exampleuniqueID`

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.artifacts.models.UpdateRepositoryDetails update_repository_details: (required)
            Updates the properties of a repository.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.artifacts.models.Repository.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.artifacts.ArtifactsClient.update_repository`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_repository(repository_id, update_repository_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_repository(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
