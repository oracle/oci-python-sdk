.. _sdk-enable-selective-service-imports

Enable Selective Service Imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If users experience slowdowns in their applications/scripts while importing the ``oci`` module for python SDK, then, they can
disable importing all the services (enabled by default) by setting the following environment variable:-

::

    export OCI_PYTHON_SDK_NO_SERVICE_IMPORTS=True

After enabling this, users will have to import individual services and modules that are needed in place of the ``import oci``
line. For example, the script  `here <https://github.com/oracle/oci-python-sdk#about>`__ can be modified to:-

.. code-block:: python

    from oci import identity
    from oci import config

    config = config.from_file()

    identity_client = identity.IdentityClient(config)

    user = identity_client.get_user(config["user"]).data

    print(user)
