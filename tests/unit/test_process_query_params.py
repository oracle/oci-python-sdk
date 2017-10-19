import oci
import pytest

@pytest.fixture
def base_client(config):
    return oci.BaseClient(
        service='compute',
        config=config,
        signer=None,
        type_mapping={}
    )

def test_process_query_params(base_client):
    raw_query_params = {
        'stuff': 'things',
        'numStuff': 55,
        'definedTags': {'tag1': ['val1', 'val2', 'val3'], "tag2": ['val1']},
        'definedTagsExists': {'tag3': True, 'tag4': True}
    }

    expected_query_params = {
        'stuff': 'things',
        'numStuff': '55',
        'definedTags.tag1': ['val1', 'val2', 'val3'],
        'definedTags.tag2': ['val1'],
        'definedTagsExists.tag3': True,
        'definedTagsExists.tag4': True,
    }

    assert expected_query_params == base_client.process_query_params(raw_query_params)
