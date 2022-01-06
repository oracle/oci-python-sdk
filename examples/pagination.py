# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates different methods of pagination in the SDK via the oci.pagination module. This module supports:
#
#   - Eagerly loading all possible results from a list call
#   - Eagerly loading all results from a list call up to a given limit
#   - Generators that can be used to lazily iterate over results from a list call. These generators can yield either values/models
#     or the raw responses of the call
#   - Pagination using raw responses instead of the oci.pagination module

import oci


config = oci.config.from_file()
compartment_id = config["tenancy"]
identity = oci.identity.IdentityClient(config)

# This demonstrates the eager loading of all possible results. This will return an oci.response.Response whose data attribute contains
# a list of all results. The other attributes of the Response object come from the last response received from the service.
print('--------------------------------------------')
print('Eager load all results')
print('--------------------------------------------')
response = oci.pagination.list_call_get_all_results(identity.list_users, compartment_id)
for user in response.data:
    print('User: {}'.format(user.name))

# This demonstrates the eager loading of all results up to a given limit. Note that we have to specify a record limit (20) and
# a page size (5)
#
# This will return an oci.response.Response whose data attribute contains a list of all results. The other attributes of the
# Response object come from the last response received from the service.
print('--------------------------------------------')
print('Eager load up to limit')
print('--------------------------------------------')
response = oci.pagination.list_call_get_up_to_limit(identity.list_users, 20, 5, compartment_id)
total_results = 0
for user in response.data:
    total_results += 1
    print('User: {}'.format(user.name))
print('Total results: {}'.format(total_results))

# This demonstrates lazily loading, via a generator, all results. Here we use a generator which yields values/models via specifying
# the yield_mode as 'record'
print('--------------------------------------------')
print('Lazy load all results - yield values')
print('--------------------------------------------')
for user in oci.pagination.list_call_get_all_results_generator(identity.list_users, 'record', config["tenancy"]):
    print('User: {}'.format(user.name))

# The below demonstrates lazily loading, via a generator, results up to a certain limit

print('--------------------------------------------')
print('Lazy load all results - yield raw responses')
print('--------------------------------------------')
response_num = 0
for response in oci.pagination.list_call_get_all_results_generator(identity.list_users, 'response', config["tenancy"]):
    response_num += 1
    for user in response.data:
        print('Response: {}, User: {}'.format(response_num, user.name))

print('--------------------------------------------')
print('Lazy load up to limit - yield values')
print('--------------------------------------------')
total_results = 0
for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 20, 10, 'record', config["tenancy"]):
    total_results += 1
    print('User: {}'.format(user.name))
print('Total results: {}'.format(total_results))

print('--------------------------------------------')
print('Lazy load up to limit - yield raw responses')
print('--------------------------------------------')
response_num = 0
total_results = 0
for response in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 20, 10, 'response', config["tenancy"]):
    response_num += 1
    for user in response.data:
        total_results += 1
        print('Response: {}, User: {}'.format(response_num, user.name))
print('Total results: {}'.format(total_results))

print('--------------------------------------------')
print('Pagination using raw responses')
print('--------------------------------------------')
response = identity.list_users(compartment_id)
users = response.data
while response.has_next_page:
    response = identity.list_users(compartment_id, page=response.next_page)
    users.extend(response.data)
for u in users:
    print('User: {}'.format(u.name))
