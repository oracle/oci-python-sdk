.. _backward-compatibility:

Backward Compatibility
~~~~~~~~~~~~~~~~~~~~~~
The top level namespace for the Python SDK has been changed from ``oraclebmc`` to ``oci``, so all of the documentation now references ``oci``. If you installed the package using ``pip install oraclebmc`` you can continue to reference ``oraclebmc`` in your code and when interpreting the documentation you can replace ``oci`` with ``oraclebmc`` (i.e. if there is a class defined in the docs as ``oci.base_client.BaseClient`` there will also exist a class ``oraclebmc.base_client.BaseClient``).

Note that the ``oraclebmc`` package is being deprecated and will be removed March 2018 so we encourage users to upgrade to ``oci``.