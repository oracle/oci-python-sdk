import unittest
import oraclebmc


class TestResponse(unittest.TestCase):
    def test_response(self):
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

        self.assertEqual(status, response.status)
        self.assertEqual('h1val', response.headers['h1'])
        self.assertEqual('next!', response.next_page)
        self.assertEqual('myid', response.request_id)
        self.assertEqual(True, response.has_next_page)

    def test_response_none_headers(self):
        status = "mystatus"
        headers = None
        data = 'testdata'

        response = oraclebmc.Response(status, headers, data, None)

        self.assertEqual(status, response.status)
        self.assertEqual(None, response.next_page)
        self.assertEqual(None, response.request_id)
        self.assertEqual(False, response.has_next_page)

    def test_response_empty_headers(self):
        status = "mystatus"
        headers = {}
        data = 'testdata'

        response = oraclebmc.Response(status, headers, data, None)

        self.assertEqual(status, response.status)
        self.assertEqual(None, response.next_page)
        self.assertEqual(None, response.request_id)
        self.assertEqual(False, response.has_next_page)
