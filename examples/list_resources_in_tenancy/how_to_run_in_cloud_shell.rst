-----------------------------
Executing using Cloud Shell:
-----------------------------

.. code-block::

    1. install oci sdk package
       pip3 install --user oci

    2. clone the oci sdk repo
       git clone https://github.com/oracle/oci-python-sdk

    3. Execute
       cd $HOME/oci-python-sdk/examples/list_resources_in_tenancy
       python3 list_all_ipsec_tunnels_in_tenancy.py -dt
       python3 list_all_virtual_circuits_in_tenancy.py -dt
       python3 list_compute_tags_in_tenancy.py -dt
       python3 list_dbsystem_with_maintenance_in_tenancy.py -dt
       python3 list_bv_backups_in_tenancy.py -dt
       python3 list_limits_per_compartments.py -dt

    4. Help with --help


