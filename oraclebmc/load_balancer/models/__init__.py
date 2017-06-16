# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .backend import Backend
from .backend_details import BackendDetails
from .backend_set import BackendSet
from .backend_set_details import BackendSetDetails
from .certificate import Certificate
from .certificate_details import CertificateDetails
from .create_backend_details import CreateBackendDetails
from .create_backend_set_details import CreateBackendSetDetails
from .create_certificate_details import CreateCertificateDetails
from .create_listener_details import CreateListenerDetails
from .create_load_balancer_details import CreateLoadBalancerDetails
from .health_checker import HealthChecker
from .health_checker_details import HealthCheckerDetails
from .ip_address import IpAddress
from .listener import Listener
from .listener_details import ListenerDetails
from .load_balancer import LoadBalancer
from .load_balancer_policy import LoadBalancerPolicy
from .load_balancer_protocol import LoadBalancerProtocol
from .load_balancer_shape import LoadBalancerShape
from .ssl_configuration import SSLConfiguration
from .ssl_configuration_details import SSLConfigurationDetails
from .session_persistence_configuration_details import SessionPersistenceConfigurationDetails
from .update_backend_details import UpdateBackendDetails
from .update_backend_set_details import UpdateBackendSetDetails
from .update_health_checker_details import UpdateHealthCheckerDetails
from .update_listener_details import UpdateListenerDetails
from .update_load_balancer_details import UpdateLoadBalancerDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError

# Maps type names to classes for load_balancer services.
load_balancer_type_mapping = {
    "Backend": Backend,
    "BackendDetails": BackendDetails,
    "BackendSet": BackendSet,
    "BackendSetDetails": BackendSetDetails,
    "Certificate": Certificate,
    "CertificateDetails": CertificateDetails,
    "CreateBackendDetails": CreateBackendDetails,
    "CreateBackendSetDetails": CreateBackendSetDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateListenerDetails": CreateListenerDetails,
    "CreateLoadBalancerDetails": CreateLoadBalancerDetails,
    "HealthChecker": HealthChecker,
    "HealthCheckerDetails": HealthCheckerDetails,
    "IpAddress": IpAddress,
    "Listener": Listener,
    "ListenerDetails": ListenerDetails,
    "LoadBalancer": LoadBalancer,
    "LoadBalancerPolicy": LoadBalancerPolicy,
    "LoadBalancerProtocol": LoadBalancerProtocol,
    "LoadBalancerShape": LoadBalancerShape,
    "SSLConfiguration": SSLConfiguration,
    "SSLConfigurationDetails": SSLConfigurationDetails,
    "SessionPersistenceConfigurationDetails": SessionPersistenceConfigurationDetails,
    "UpdateBackendDetails": UpdateBackendDetails,
    "UpdateBackendSetDetails": UpdateBackendSetDetails,
    "UpdateHealthCheckerDetails": UpdateHealthCheckerDetails,
    "UpdateListenerDetails": UpdateListenerDetails,
    "UpdateLoadBalancerDetails": UpdateLoadBalancerDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError
}
