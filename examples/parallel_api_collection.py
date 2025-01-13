# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Goal of Script!!!
# By avoiding API calls without dependencies to be processed in serial in our code, we get a significant performance increase on API collections.
# This code sends the API call to the thread pool so we do not have to wait for the previous API call to finish before going to the next API call.

import oci
import concurrent.futures
import time

config = oci.config.from_file()
identity_client = oci.identity.IdentityClient(config)
# Time How Long the the API Calls Take.
timer = time.time()

# Run the "List Users" call to get all of the configured users. This will get the dependencies for the "List API Keys" call.
list_users_response = identity_client.list_users(config['tenancy'])

# Save the active API keys to this list.
active_api_keys = []

# Function that executes the "list_api_keys" call.
# If the user has an active API key, the function will add it to the active_api_keys list.


def api_function(user_ocid):
    list_api_keys_response = identity_client.list_api_keys(user_ocid)
    if list_api_keys_response.data:
        active_api_keys.extend(list_api_keys_response.data)


# Create a Thread Pool to submit tasks. The Max Workers is how many threads can be executed at one time.
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)

# Iterate through each user and get the API keys.
# Submit the call to the thread pool with the user.id argument to the list_api_keys API call.
for user in list_users_response.data:
    thread_pool.submit(api_function, user.id)

# Wait for all of the tasks in the thread pool to complete before finishing the script.
thread_pool.shutdown(wait=True)

# Show How Many Keys Were Found
print(len(active_api_keys))

# See How Long the Call Took. Enjoy your speed enhancement on your OCI API calls :)
print(f"Script took {(time.time()- timer)}s")
