import oraclebmc
import pytest


@pytest.fixture
def expected_content():
    return "a/b/c/object3"


@pytest.fixture
def response(object_storage, expected_content):
    _response = object_storage.get_object(
        namespace_name="internalbriangustafson",
        bucket_name="ReadOnlyTestBucket2",
        object_name=expected_content
    )
    assert _response.status == 200
    return _response


def test_content(response, expected_content):
    assert expected_content == response.data.content.decode('UTF-8')


def test_iter_content(response, expected_content):
    response_text = ''
    chunk_count = 0
    chunk_size = 2
    for chunk in response.data.iter_content(chunk_size=chunk_size):
        response_text += chunk.decode('UTF-8')
        chunk_count += 1

    assert chunk_count >= (len(expected_content) / chunk_size)
    assert response_text == expected_content


def test_raw(response, expected_content):
    response_text = response.data.raw.read(100).decode('UTF-8')
    assert response_text == expected_content


def test_content_multiple_access(response, expected_content):
    assert expected_content == response.data.content.decode('UTF-8')
    assert expected_content == response.data.content.decode('UTF-8')
    assert expected_content == response.data.content.decode('UTF-8')


def test_stream_after_content(response, expected_content):
    assert expected_content == response.data.content.decode('UTF-8')

    response_text = ''
    chunk_count = 0
    chunk_size = 2
    for chunk in response.data.iter_content(chunk_size=chunk_size):
        response_text += chunk.decode('UTF-8')
        chunk_count += 1

    assert chunk_count >= (len(expected_content) / chunk_size)
    assert response_text == expected_content


def test_content_after_stream(response, expected_content):
    response_text = ''
    for chunk in response.data.iter_content():
        response_text += chunk.decode('UTF-8')
    assert response_text == expected_content

    with pytest.raises(oraclebmc.exceptions.StreamAlreadyConsumed):
        # content was already consumed by iter_content above
        getattr(response.data, "content")


def test_stream_twice(response, expected_content):
    response_text = ''
    for chunk in response.data.iter_content():
        response_text += chunk.decode('UTF-8')
    assert response_text == expected_content

    with pytest.raises(oraclebmc.exceptions.StreamAlreadyConsumed):
        for chunk in response.data.iter_content():
            response_text += chunk.decode('UTF-8')
