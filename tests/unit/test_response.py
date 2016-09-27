import oraclebmc


def test_response():
    status = "mystatus"
    headers = {'h1': 'h1val', 'opc-next-page': 'next!', 'opc-request-id': 'myid'}
    data = 'testdata'
    request = oraclebmc.Request(
        'method',
        'url',
        'query_params',
        'header_params',
        'body',
        'response_type'
    )

    response = oraclebmc.Response(status, headers, data, request)

    assert status == response.status
    assert 'h1val' == response.headers['h1']
    assert 'next!' == response.next_page
    assert 'myid' == response.request_id
    assert response.has_next_page is True


def test_response_none_headers():
    status = "mystatus"
    headers = None
    data = 'testdata'

    response = oraclebmc.Response(status, headers, data, None)

    assert status == response.status
    assert response.next_page is None
    assert response.request_id is None
    assert response.has_next_page is False


def test_response_empty_headers():
    status = "mystatus"
    headers = {}
    data = 'testdata'

    response = oraclebmc.Response(status, headers, data, None)

    assert status == response.status
    assert response.next_page is None
    assert response.request_id is None
    assert response.has_next_page is False
