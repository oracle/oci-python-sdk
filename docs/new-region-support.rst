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

For regions in the oraclecloud.com realm, even if the <Region enum> does not contain the new region, the forward compatibility of the SDK can automatically handle it. You can pass new region names just as you would pass ones that are already defined.

============
Other Realms
============

For regions in realms other than oraclecloud.com, you can use the following workarounds to reach new regions with earlier versions of the SDK:


