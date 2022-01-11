.. _sdk-allow_control_chars_response:

Allow control characters in response
~~~~~~~~
The SDK helps deserialize any response object that is coming in from an API call. The deserialization uses the json library 
to call json.loads(). By defaualt, the deserialization will not allow the response object to contain control characters in a string.
If the user chooses to allow control characters in a response, the SDK provides 3 option of settings to allow this feature:
* Request setting: Specify in the request to allow control characters
* Client setting: Set a specific service client's base client to allow control character
* Global setting: Set BaseClient to allow control characters on all response.

The request setting will take the highest precedence, follow by the client setting, and finally global setting. 

Example
-------

.. code-block:: python

    # Allowing control characters at the request level.
    response = identity_client.list_region_subscriptions.list_region_subscriptions(compartment_id, allow_control_chars=True)

    # Allow control characters at the client level.
    identity_client.base_client.allow_control_chars = True

    # Allow control characters at the global level.
    BaseClient.ALLOW_CONTROL_CHARACTERS = True
