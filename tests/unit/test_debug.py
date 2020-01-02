# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import oci


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
