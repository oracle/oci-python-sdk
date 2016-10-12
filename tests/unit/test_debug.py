import oraclebmc


def test_client_call_success(capfd, config):
    config["log_requests"] = True
    config["additional_user_agent"] = 'example_extra_user_agent_text'
    virtual_network = oraclebmc.clients.VirtualNetworkClient(config)
    response = virtual_network.list_vcns(config["tenancy"])
    assert response.status == 200

    resout, _ = capfd.readouterr()

    assert 'user-agent: Oracle-PythonSDK/' in resout
    assert 'opc-client-info: Oracle-PythonSDK/' in resout
    assert 'opc-request-id: ' in resout
    assert '200 OK' in resout
    assert 'example_extra_user_agent_text' in resout
