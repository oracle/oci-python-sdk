from tests.service_test_base import ServiceTestBase
import os
import sys
import oraclebmc
import tests.util

class TestDebug(ServiceTestBase):

    def test_api_call_success(self):
        log_file = tests.util.get_resource_path('test_debug.log')
        if os.path.isfile(log_file):
            os.remove(log_file)

        previous_stdout = sys.stdout
        sys.stdout = open(log_file, 'a')

        self.config.log_requests = True
        self.config.additional_user_agent = 'example_extra_user_agent_text'
        api = oraclebmc.apis.VirtualNetworkApi(self.config)

        try:
            response = api.list_vcns(self.config.tenancy)
            self.assertEqual(200, response.status)
        finally:
            sys.stdout.close()
            sys.stdout = previous_stdout

        log = open(log_file, 'r').read()
        assert (len(log) > 0)
        assert ('user-agent: Oracle-PythonSDK/' in log)
        assert ('opc-client-info: Oracle-PythonSDK/' in log)
        assert ('opc-request-id: ' in log)
        assert ('200 OK' in log)
        assert ('example_extra_user_agent_text' in log)

if __name__ == '__main__':
    unittest.main()