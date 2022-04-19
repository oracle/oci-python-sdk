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
This can be helpful if you need to make an authenticated request to an alternate endpoint or to an
Oracle Cloud Infrastructure API not yet supported in the SDK.

===================
 Creating a Signer
===================

The Signer used as part of making raw requests can be either an `Instance Principals-based <https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm>`__ signer or one that uses a user OCID and private key.  

Signer with user OCID and private key 
--------------------------------------

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

Instance Principals-based Signer
---------------------------------

An Instance Principals-based signer can be created as follows:

.. code-block:: python

    import oci
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

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

    endpoint = 'https://identity.us-phoenix-1.oci.oraclecloud.com/20160918/users/'
    body = {
        'compartmentId': config['tenancy'],  # root compartment
        'name': 'TestUser',
        'description': 'Created with a raw request'
    }

    response = requests.post(endpoint, json=body, auth=auth)

    response.raise_for_status()
    print(response.json()['id'])

Using an Instance Principals-based Signer
------------------------------------------

The Instance Principals-based Signer uses a security token to authenticate calls against Oracle Cloud Infrastructure services. This token has an expiration time and the Signer will automatically handle refreshing the token when it is near expiry. However, it is possible that the security token held by the signer is valid (from an expiration time perspective) but the request fails with a 401 (NotAuthenticated) error because of, for example, changes in the dynamic group that an instance is a part of or the policies applied to that dynamic group.

You can account for this by retrying on a 401. If the request fails with a 401 on a subsequent retry, this may point to other issues and you should not keep retrying in this circumstance. For example:

.. code-block:: python

    import oci
    import requests

    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    call_attempts = 0
    while call_attempts < 2:
        # This call is just an example. Provide your own appropriate method (e.g. get() instead of post()), endpoint and body
        response = requests.post(endpoint, json=body, auth=signer)
        if response.ok:
            return response
        else:
            call_attempts += 1
            if response.status_code == 401 and call_attempts < 2:
                signer.refresh_security_token()
            else:
                response.raise_for_status()


