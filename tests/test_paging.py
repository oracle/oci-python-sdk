from tests.service_test_base import ServiceTestBase

class TestPaging(ServiceTestBase):

    def test_manual_paging(self):

        request_number = 0
        previous_first_ocid = None
        next_page = None

        while True:
            if request_number == 0:
                response = self.context.identity_api.list_users(self.context.config.tenancy, limit=2)
            else:
                response = self.context.identity_api.list_users(self.context.config.tenancy, limit=2, page=next_page)

            if not response.has_next_page:
                break

            next_page = response.next_page
            request_number += 1

            # Somethings probably wrong if we go past 30 requests.
            assert(request_number < 30)

            self.assertEqual(200, response.status)

            self.assertNotEqual(previous_first_ocid, response.data[0].id)
            previous_first_ocid = response.data[0].id

        # Make sure we've at least looked at a couple pages.
        assert(request_number > 1)

if __name__ == '__main__':
    unittest.main()