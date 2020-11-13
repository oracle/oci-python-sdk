-----------------------------
Executing using Cloud Shell:
-----------------------------

.. code-block::

    1. install oci sdk package
       pip3 install --user oci

    2. clone the oci sdk repo
       git clone https://github.com/oracle/oci-python-sdk

    3. Execute
       cd $HOME/oci-python-sdk/examples/object_storage
       python3 object_storage_bulk_copy.py    -dt -parameters...
       python3 object_storage_bulk_delete.py  -dt -parameters...
       python3 object_storage_bulk_restore.py -dt -parameters...
       python3 object_storage_list_objects.py -dt -parameters...








