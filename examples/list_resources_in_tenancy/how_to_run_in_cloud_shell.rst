-----------------------------
Executing using Cloud Shell:
-----------------------------

.. code-block::

    1. Create virtual env of python
       python3 -m venv python_venv
       source python_venv/bin/activate

    2. install oci sdk package
       pip install oci

    3. clone the oci sdk repo
       git clone https://github.com/oracle/oci-python-sdk

    4. Execute
       cd $HOME/oci-python-sdk/examples/list_resources_in_tenancy
       python list_all_ipsec_tunnels_in_tenancy.py -dt
       python list_all_virtual_circuits_in_tenancy.py -dt
       python list_compute_tags_in_tenancy.py -dt
       python list_dbsystem_with_maintenance_in_tenancy.py -dt


