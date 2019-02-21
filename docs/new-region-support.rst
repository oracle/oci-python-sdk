.. _new-region-support:

.. raw:: html

    <script type='text/javascript'>
        var oldDocsHost = 'oracle-bare-metal-cloud-services-python-sdk';
        if (window.location.href.indexOf(oldDocsHost) != -1) {
            window.location.href = 'https://oracle-bare-metal-cloud-services-python-sdk.readthedocs.io/en/latest/deprecation-notice.html';
        }
    </script>

New Region Support
~~~~~~~~~~~~~~~~~~~~~~

If you are using a version of the SDK released prior to the announcement of a new region, you may need to use a workaround to reach it, depending on whether the region is in the oraclecloud.com realm.

A *region* is a localized geographic area. For more information on regions and how to identify them, see `Regions and Availability Domains <https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm>`_

A *realm* is a set of regions that share entities. You can identify your realm by looking at the domain name at the end of the network address. For example, the realm for ``xyz.abc.123.oraclecloud.com`` is ``oraclecloud.com``.

=====================
oraclecloud.com Realm
=====================

For regions in the oraclecloud.com realm, the forward compatibility of the SDK can automatically handle it. You can pass new region names just as you would pass ones that are already defined. For more information on passing region names in the configuration, see :doc:`configuration`.

============
Other Realms
============

For regions in realms other than oraclecloud.com, you can use the following workarounds to reach new regions with earlier versions of the SDK.

NOTE: Be sure to supply the appropriate endpoints for your region.

You can set the endpoint on an initialized client via the base client::
    
    client.base_client.endpoint = 'https://identity.us-gov-phoenix-1.oraclegovcloud.com'

If you are authenticating via instance principals, you can set the federation_endpoint for the region using InstancePrincipalsSecurityTokenSigner when initializing the signer::
    
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner(federation_endpoint='https://auth.us-gov-phoenix-1.oraclegovcloud.com/v1/x509')

If the correct federation_endpoint for the region is not passed in, you will see the following error during instance principals authentication::
    
    oci._vendor.requests.exceptions.ConnectionError: HTTPSConnectionPool(host='auth.us-gov-phoenix-1.oraclecloud.com', port=443): Max retries exceeded with url: /v1/x509 (Caused by NewConnectionError('<oci._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x7f5c91002ba8>: Failed to establish a new connection: [Errno -2] Name or service not known',))
