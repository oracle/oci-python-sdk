# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import logging


def test_client_call_success(capfd, config):
    config["log_requests"] = True
    config["additional_user_agent"] = 'example_extra_user_agent_text'
    identity = oci.identity.IdentityClient(config)
    response = identity.list_policies(config["tenancy"])
    assert response.status == 200

    resout, _ = capfd.readouterr()

    assert 'user-agent: Oracle-PythonSDK/' in resout
    assert 'opc-client-info: Oracle-PythonSDK/' in resout
    assert 'opc-request-id: ' in resout
    assert '200 OK' in resout
    assert 'example_extra_user_agent_text' in resout


def test_client_disable_log(capfd, config):
    config["log_requests"] = True
    logging.basicConfig()
    config["additional_user_agent"] = 'example_extra_user_agent_text'
    identity = oci.identity.IdentityClient(config)
    logger = logging.getLogger('oci.base_client.{}'.format(id(identity.base_client)))
    logger.disabled = True
    oci.base_client.is_http_log_enabled(False)
    response = identity.list_policies(config["tenancy"])

    assert response.status == 200
    resout, _ = capfd.readouterr()
    assert 'user-agent: Oracle-PythonSDK/' not in resout
    assert 'opc-client-info: Oracle-PythonSDK/' not in resout
    assert 'opc-request-id: ' not in resout
    assert '200 OK' not in resout
    assert 'example_extra_user_agent_text' not in resout
