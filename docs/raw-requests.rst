.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

Raw Requests
~~~~~~~~~~~~

The Python SDK exposes a custom :class:`requests.auth.AuthBase` which you can use to sign non-standard calls.
This can be helpful if you need to make a OCI- authenticated request to an alternate endpoint or to a
OCI API not yet supported in the SDK.

===================
 Creating a Signer
===================

Constructing a Signer instance requires a few pieces of information.  By default, the SDK uses the values in
the config file at ``~/.oci/config``.  You can manually specify the required fields, or use a config loader
to pull in the values from a file:

.. code-block:: python

    from oci.signer import Signer
    auth = Signer(
        tenancy='ocid1.tenancy.oc1..aaaaaaaa[...]',
        user='ocid1.user.oc1..aaaaaaaa[...]',
        fingerprint='20:3b:97:13:55:1c:[...]',
        private_key_file_location='~/.oci/oci_api_key.pem',
        pass_phrase='hunter2'  # optional
    )


    # Or load directly from a file
    from oci.config import from_file
    config = from_file('~/.oci/config')
    auth = Signer(
        tenancy=config['tenancy'],
        user=config['user'],
        fingerprint=config['fingerprint'],
        private_key_file_location=config['key_file'],
        pass_phrase=config['pass_phrase']
    )


==================
 Using the Signer
==================

Once you have an instance of the auth handler, simply include it as the ``auth=`` param when using Requests.

.. code-block:: python

    import requests

    url = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918/instances[...]'
    response = requests.get(url, auth=auth)

Remember that the result will come back in its raw form and is not unpacked into a model instance.
You will need to handle the (de)serialization yourself.

The following creates a new user by talking to the identity endpoint:

.. code-block:: python

    endpoint = 'https://identity.us-phoenix-1.oraclecloud.com/20160918/users/'
    body = {
        'compartmentId': config['tenancy'],  # root compartment
        'name': 'TestUser',
        'description': 'Created with a raw request'
    }

    response = requests.post(endpoint, json=body, auth=auth)

    response.raise_for_status()
    print(response.json()['id'])
