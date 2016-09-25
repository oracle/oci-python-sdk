def test_manual_paging(identity, config):
    request_number = 0
    previous_first_ocid = None
    next_page = None

    while True:
        if request_number == 0:
            response = identity.list_users(config.tenancy, limit=2)
        else:
            response = identity.list_users(config.tenancy, limit=2, page=next_page)

        if not response.has_next_page:
            break

        next_page = response.next_page
        request_number += 1

        # Somethings probably wrong if we go past 30 requests.
        assert(request_number < 30)
        assert response.status == 200
        assert previous_first_ocid != response.data[0].id

        previous_first_ocid = response.data[0].id

    # Make sure we've at least looked at a couple pages.
    assert request_number > 1
