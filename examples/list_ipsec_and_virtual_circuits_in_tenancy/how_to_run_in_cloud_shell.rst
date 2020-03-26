-----------------------------
Executing using Cloud Shell:
-----------------------------

.. code-block::

    1. Create virtual env of python
       python -m venv python_venv
       source python_venv/bin/activate

    2. install oci sdk package
       pip install oci

    3. clone the oci sdk repo
       cd $HOME
       git init
       git clone https://github.com/oracle/oci-python-sdk

    4. Config OCI config file - ~/.oci/config
       Please follow SDK config documentation - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm

    5. Execute
       cd $HOME/oci-python-sdk/examples/list_ipsec_and_virtual_circuits_in_tenancy
       python list_all_ipsec_tunnels_in_tenancy.py
       python list_all_virtual_circuits_in_tenancy.py


