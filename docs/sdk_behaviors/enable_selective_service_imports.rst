.. _sdk-enable-selective-service-imports

Enable Selective Service Imports for Python 3.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

.. note::
    Deferred imports have been enabled by default in v2.88.1 of the oci-python-sdk when using Python 3.7+.
    With deferred imports, only the modules that you explicitly import in your code will be imported,
    thereby reducing the initial load time significantly. If you are either using Python 3.6 or using a version older
    than v2.88.1, then follow the instructions mentioned in the section above to enable selective imports in your code.

    PS: If the lazy imports are causing an issue with your code then you can opt-out of this feature by setting the
    environment variable `OCI_PYTHON_SDK_LAZY_IMPORTS_DISABLED` to True.