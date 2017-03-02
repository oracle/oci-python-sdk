Raw Requests
~~~~~~~~~~~~

The Python SDK exposes a custom :class:`requests.auth.AuthBase` which you can use to sign non-standard calls.
This can be helpful if you have opted into a beta program and need to communicate with a non-public endpoint, or
otherwise modify your request in a way that the SDK does not support.

===================
 Creating a Signer
===================

Constructing a Signer instance requires a few pieces of information.  By default, the SDK uses the values in
the config file at ``~/.oraclebmc/config``.  You can manually specify the required fields, or use a config loader
to pull in the values from a file:

.. code-block:: python

    from oraclebmc.signer import Signer
    config = {
        'tenancy': 'ocid1.tenancy.oc1..aaaaaaaa[...]',
        'user': 'ocid1.user.oc1..aaaaaaaa[...]',
        'fingerprint': '20:3b:97:13:55:1c:[...]',
        'private_key_file_location': '~/.oraclebmc/config',
        'pass_phrase': 'hunter2'  # optional
    }


    # Or load directly from a file
    from oraclebmc.config import from_file
    config = from_file('~/.oraclebmc/config')


    auth = Signer(**config)


==================
 Using the Signer
==================

Once you have an instance of the auth handler, simply include it in the ``auth=`` when making a call with requests.

.. code-block:: python

    import requests

    url = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918/instances[...]'
    response = requests.get(url, auth=auth)

Remember that the result will come back as a json blob, and is not automatically unpacked into the corresponding
model instance.  You will need to handle the (de)serialization yourself.

The following creates a new user by talking to the identity endpoint:

.. code-block:: python

    endpoint = 'https://identity.us-phoenix-1.oraclecloud.com/20160918/users'
    body = {
        'compartment_id': config['tenancy'],  # root compartment
        'name': 'TestUserPleaseIgnore',
        'description': 'Created without the Identity Service Client'
    }

    response = requests.post(endpoint, json=body, auth=auth)
    response.raise_for_status()

    print(response.json['id'])
